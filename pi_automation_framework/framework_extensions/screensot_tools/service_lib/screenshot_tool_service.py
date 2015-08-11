from framework_extensions.utils.abstract_service import AbstractService
from framework_extensions.screensot_tools.conf_lib.Constants    import TT_Constants
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TargetPixelService(AbstractService):

    def svc_call_target_pixel(self, **kwargs):
        #header = self._retrieve_default_header(**kwargs)
        logger.info('Start reading svc_call_target_pixel...')
        pixel=kwargs['pixel_id']
        advertiser=kwargs['advertiser_id']
        query='?pixel=%s&advertiser=%s'%(pixel,advertiser)
        response = self._call(TT_Constants['Base_URL']+'tools/t1_chrome/targetpixel%s'%query, 'GET')
        #response.headers['status'] , 'Failed to parse response for article version history service'
        logger.info('Finishing svc_call_target_pixel...')
        return response

