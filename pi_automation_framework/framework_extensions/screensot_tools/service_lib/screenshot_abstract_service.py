from framework_extensions.utils import AbstractService#service_tools,data_tools
#from intertester_extensions.scoop.utils import populate_newarticle_content_common_obj
#in abstract
class ScoopAbstractService(AbstractService):
    def __init__(self, conf_manager , conf_location , service_session , body_parsers=None):
        if body_parsers is None :
            body_parsers  = (service_tools.body_parsers.JsonBodyParserScoop,)#JsonLegacyBodyParser
        super(ScoopAbstractService,self).__init__(conf_manager, conf_location , service_session , body_parsers)
        
    def _retrieve_default_header(self,**kwargs):
        data_user = kwargs.pop('user', self._service_session.user)
        desired_cookies = self._conf_manager._confs['scoop'].misc_values.cookie_names
        
        try:
            cookies_string = data_tools.get_cookie_string_for_request_header(desired_cookies, data_user, kwargs.pop('cookies', {}))#
        except ValueError:
            cookies_string = ''
        return  {'Cookie' : cookies_string, 'content_type' : 'application/json; charset=utf-8' }

    
    def _retrieve_article_bootstrap_api(self,**kwargs):
        header = self._retrieve_default_header(**kwargs)
        #asset_id=self._set_article_id_filter(kwargs.pop('new_article_options'))
        if 'new_article_options' in kwargs:#hasattr(kwargs,'new_article_options') : #making it backward compatible
            asset_id=list(self._set_article_id_filter(kwargs.pop('new_article_options')))[0]
        else:
            asset_id=kwargs['asset_id']
        response = self._call('/resources/app/content/article/bootstrap/article/%s'%asset_id, 'GET', headers=header)
        return_value = self._parse_response(response, {}, service_tools.BODY_FORMATS.JSON.SCOOP)#LEGACY
        assert  return_value['success'] , 'Failed to parse response for bootstrap api'
        #return_value['asset_object'] = populate_newarticle_content_common_obj.from_newarticle_service_asset_content(return_value['rough_parsed_body']['results'][0])
        return return_value
    
    def _set_article_id_filter(self,article_data):
        return {article_data.content_id if hasattr(article_data , 'content_id') else None}