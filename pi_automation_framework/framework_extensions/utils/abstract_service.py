import httplib2, json, urllib
#from utils.log.logger_manager import LoggerManager
from xml.dom.minidom import parseString as parse_string_to_xml_minidom
#from service_lib.parsers.body import JsonLegacyBodyParser, JsonMetaBodyParser
import warnings
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
 
class AbstractService(object):
    """
    AbstractService is the base class for all Service classes.  It provides a constructor
    and a few other generic methods related to maknig a service call and working with ServiceSession.
    """
     
#     def __init__(self, conf_manager, conf_location, service_session, body_parsers='LEGACY'):
#         """
#         This method initializes a new instance of a Service object.
#         input:
#         conf_manager - The ConfManager instance to be associated with this service.
#         conf_location - A list of strings representing the location within the conf_manager confs
#                         of the ServiceDescription representing this service.
#         service_session - The ServiceSession instance to associate with this Service (The ServiceSession
#                           that will have the methods of this Service registered to it.)
#         body_parsers - A list of AbstractBodyParser derived objects to register to the service class.
#         output:
#         N/A
#         exceptions:
#         N/A
#         """
#          
#         test_logger_root = service_session.loggers.test_absolute
#         code_logger_root = service_session.loggers.code_absolute
#         self_type = type(self)
#         self.loggers = LoggerManager(test_logger_root, 'service', code_logger_root, self_type.__name__)
#         self._conf_manager = conf_manager
#         self._conf_location = conf_location
#         conf_cursor = conf_manager
#         for key in conf_location:
#             conf_cursor = getattr(conf_cursor, key)
#         self.loggers.code_logger.debug('Found ServiceDescriptor in conf.')
#         self._service_def = conf_cursor
#         self._service_session = service_session
#         self._parsed_body_keymap_parsers = {}
#         self._all_bases_for_registered_keymap_parsers = []
#         self._body_parser_registry = {}
#         if body_parsers == 'LEGACY':
#             warnings.warn(('Loading default parsers is deprecated functionality.  Service classes should explicitly pass a list '
#                            'of body parsers to super.__init__() in their __init__() methods.'), DeprecationWarning, stacklevel=2)
#             self.register_body_parser(JsonLegacyBodyParser)
#             self.register_body_parser(JsonMetaBodyParser)
#         else:
#             for parser in body_parsers:
#                 self.register_body_parser(parser)
     
    def _call(self, relative_path, method, body=None, url_content=None, headers=None, response_format='JSON', ssl=()):
        """
        The generic method that constructs and submits the request and receives and deserializes
        the response from a service.  The formatting of the request is determined by the protocol
        defined in the ServiceDefinition.
        input:
        relative_path - The path of this service relative to the root url defined in the
                        ServiceDefinition.
        method - The type of request (GET, POST, PUT, DELETE) to be made, as a string.
        body - A dictionary containing the information to be encoded in the service call body.
               'format' : The encoding to format the request body in (JSON/XML).
               'content' : A dictionary containing a key/value pair for each element to be submitted in the body.
               Defaults to None, which will not include any body.
        url_content - A dictionary containing a key/value pair for each piece of data to submit as a URL argument.
                      Defaults to None, which will not add any args to the URL.
        headers - A dictionary containing a key/value pair for each element to add to the header.  Defaults to None,
                  which will cause the call to be made with no headers.
        response_format - A string describing the format we expect to receive from the service (controls deserialization).
                          Defaults to 'JSON', must be 'JSON' or 'XML'.
        output:
        The deserialized response from the service.
        exceptions:
        NotImplementedError - Raised when a valid protocol is defined, but the serializer for that
                              protocol has not yet been implemented.
        ValueError - Raised when the protocol for the service is invalid.
        """
         
        args = []
        kwargs = {}
        if body and 'format' in body and 'content' in body:
            if body['format'] == 'XML':
                raise NotImplementedError("XML protocol has not yet been implemented.")
                logger.debug('Serialized XML request data.')
            elif body['format'] == 'JSON':
                kwargs['body'] = json.dumps(body['content'])
                logger.debug('Serialized JSON request data.')
            else:
                raise ValueError('The body format is invalid.  Found %s.' % body['format'])
        elif body:
            raise ValueError('A body has been received but it does not contain a format and/or content.')
        url = relative_path#self._service_def.url + 
        if url_content:
            url += '?' + urllib.urlencode(url_content)
        args.append(url)
        args.append(method)
        if headers:
            kwargs['headers'] = headers
        http = httplib2.Http()
        if ssl:
            http.add_credentials(ssl)
        logger.debug('Service call (%s to %s):\n%s' % (args[1], args[0], kwargs))
        try:
            service_response = http.request(*args, **kwargs)
        except httplib2.CertificateHostnameMismatch:
            logger.debug('SSL certificate validation failed.  Retrying without certificate validation.')
            http.disable_ssl_certificate_validation = True
            service_response = http.request(*args, **kwargs)
        logger.debug('Service response:\n%s\n%s' % (service_response[0], service_response[1]))
        service_response = ServiceResponse(service_response, response_format)
        return service_response
     
     
    def _parse_response(self, response, value_key_map, response_format):
        """
        This method is intended to be called from within the individual service calls in the subclasses of AbstractService.
        It will parse an entire service response.
        input:
        response - A string with the entire response from the service.
        value_key_map - A dictionary containing an element for each item in the service response body that should be extracted
                        in to the dictionary returned.  Each element should have the format:
                        resulting_dict_key_name : [service_result_dict_key_1, service_result_dict_key_2...]
                        For example:
                        'demo_val' : ['demo', 'val']
                        Would cause the dictionary returned to contain a key of name demo_val which would have a value of
                        response['demo']['value']
        response_format - Value representing the expected response format for the given service response being parsed.  
        output:
        A dict containing all the extracted values on success or errors on failure, along with a 'success' key containing a
        boolean value representing whether the service operated without errors or not.
        exceptions:
        N/A
        """
         
        body = response.body
        return_value = {'headers' : response.headers}
        if response_format in self._body_parser_registry:
            body_parser = self._body_parser_registry[response_format](body)
            return_value.update(body_parser.parse(value_key_map))
        else:
            raise ValueError('No body parser registered for format code %d.' % response_format)
        return return_value
     
#     def register_body_parser(self, parser, overwrite_existing=False):
#          
#         if parser.BODY_FORMAT_CODE is None:
#             raise ValueError('BODY_FORMAT_CODE for parser is None.  Check class construction.')
#         if parser.BODY_FORMAT_CODE in self._body_parser_registry and not overwrite_existing:
#             raise ValueError('Parser already registered for body format %d.'%  parser.BODY_FORMAT_CODE)
#         self._body_parser_registry[parser.BODY_FORMAT_CODE] = parser
 
 
 
class ServiceResponse(object):
    """
    A ServiceResponse instance represents the response from a service call.  It deserializes the response during
    initialization.
    """
     
    def __init__(self, http_response, encoding, logger_context=None):
        """
        This method initializes a ServiceResponse.  The contents of the response is deserialized during this process.
        input:
        http_response - The response received from the service call.
        encoding - The encoding of the body of the response (XML or JSON)
        logger_context - A list representing the test and code logger roots for this ServiceResponse.  If None,
                         logging is suppressed.  Defaults to None.
        output:
        N/A
        exceptions:
        NotImplementedError - Raised for any valid encoding for which a parser has not yet been implemented.
        ValueError - Raised when an invalid encoding is passed.
        """
         
#         if logger_context:
#             self.loggers = LoggerManager(logger_context[0], 'service_response', logger_context[1], 'ServiceResponse')
        self.headers = http_response[0]
        if encoding == 'JSON':
            self.body = json.loads(http_response[1])
#             if logger_context:
            logger.debug('Deserialized JSON body.')
        elif encoding =='XML':
            self.body = parse_string_to_xml_minidom(http_response[1])
#             if logger_context:
            logger.debug('Deserialized XML body.')
        else:
            raise ValueError('encoding must be JSON or XML.  Got %s.' % encoding)