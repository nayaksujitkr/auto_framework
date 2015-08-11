from framework_tests.Constants    import TT_Constants
from framework_tests.BaseTestCase    import BaseTestCase
from framework_extensions.screensot_tools.service_lib.screenshot_tool_service import TargetPixelService
import unittest
import time
from ddt import ddt, data, file_data, unpack

@ddt
class ScreenshotTargetPixelTest(unittest.TestCase):

    def SetUp(self):
        print "setup insdide..."

    @data((747700, 100507))
    @unpack
    def test_screenshot_target_pixel_ws(self,pixel_id,advertiser_id):
        issues=[]
        targetpixel_ws__obj = TargetPixelService()
        service_response=targetpixel_ws__obj.svc_call_target_pixel(pixel_id=pixel_id,advertiser_id=advertiser_id)

        if service_response.headers['status'] != '200':
            issues.append("Get screenshot target pixel service failed. Status == " + service_response['status'])
            if service_response['errors'] != None:
                issues.append("Get screenshot target_pixel service error == " + str(service_response['errors']))
        else:
            if "RTG Pixel generique R24" != service_response.body["843168"]:
                issues.append("Post screenshot target_pixel should be 'RTG Pixel generique R24' "+". service reponse contains " + str(service_response.body["843168"]))
            if "RTG Pixel generique" != service_response.body["843161"]:
                issues.append("Post screenshot target_pixel should be 'RTG Pixel generique' "+". service reponse contains " + str(service_response.body["843161"]))
        if issues:
            assert False, ' || '.join(issues) 
            
    def tearDown(self):
        print "teardown insdide..."
        
if __name__ == "__main__":
    unittest.main()