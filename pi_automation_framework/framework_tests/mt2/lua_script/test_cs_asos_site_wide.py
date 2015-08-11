
from framework_extensions.mt2_ssh.pyssh import PySSH
from framework_extensions.mt2_ssh.mt2_httprequest import MT2_HttpRequest
import unittest
import time
from framework_extensions.utils import config_helper
import requests
import select
import  paramiko

testcase_name=[
        {'test_case':'uuid_start_with_7_and_v6_equal_to_male'},
        {'test_case':'uuid_not_start_with_7_and_v6_equal_to_male'},
        {'test_case':'uuid_start_with_7_and_v6_equal_to_female'},
        {'test_case':'uuid_not_start_with_7_and_v6_equal_to_female'},
        {'test_case':'uuid_start_with_7_and_v10_equal_to_1'},
        {'test_case':'uuid_start_with_7_and_v10_equal_to_2'},
        {'test_case':'uuid_start_with_7_and_v10_equal_to_3'},
        {'test_case':'uuid_start_with_7_and_v10_equal_to_4'},
        {'test_case':'uuid_start_with_7_and_v10_equal_to_5'},
        {'test_case':'uuid_start_with_7_and_v3_equal_to_dress'},
    {'test_case':'uuid_start_with_7_and_v3_equal_to_tshirt'},
    {'test_case':'uuid_start_with_7_and_v3_equal_to_t-shirt'},
    {'test_case':'uuid_start_with_7_and_s1_equal_to_notshopped'},
    {'test_case':'uuid_start_with_7_and_s1_equal_to_firstshoppedp12m'},
    {'test_case':'uuid_start_with_7_and_s1_equal_to_firstshoppedover12m'}
        ]

data_set={
'uuid_start_with_7_and_v10_equal_to_1':{'curl_parameter':'&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v10=1',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 795161, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&v10=1','pixel_log_uuid_pixel_search_string':'mt_id=797323&v10=1','pixel_log_child_pixel_search_string':'mt_id=795161&v10=1',
'v10':'1', "uuid": '7fc253a4-acc5-4800-8b40-d1d701b12834','parent_pixel':'773063','child_pixel':'797323','v10_pixel':'795161','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v10=1','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=797323&v10=1','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=795161&v10=1'},



'uuid_start_with_7_and_v10_equal_to_2':{'curl_parameter':'&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v10=2',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 795162, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&v10=2','pixel_log_uuid_pixel_search_string':'mt_id=797323&v10=2','pixel_log_child_pixel_search_string':'mt_id=795162&v10=2',
'v10':'2', "uuid": '7fc253a4-acc5-4800-8b40-d1d701b12834','parent_pixel':'773063','child_pixel':'797323','v10_pixel':'795162 ','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v10=2','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=797323&v10=2','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=795162&v10=2'},
        

'uuid_start_with_7_and_v10_equal_to_3':{'curl_parameter':'&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v10=3',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 795163, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&v10=3','pixel_log_uuid_pixel_search_string':'mt_id=797323&v10=3','pixel_log_child_pixel_search_string':'mt_id=795163&v10=3',
'v10':'3', "uuid": '7fc253a4-acc5-4800-8b40-d1d701b12834','parent_pixel':'773063','child_pixel':'797323','v10_pixel':'795163 ','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v10=3','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=797323&v10=3','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=795163&v10=3'},


'uuid_start_with_7_and_v10_equal_to_4':{'curl_parameter':'&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v10=4',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 795164, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&v10=4','pixel_log_uuid_pixel_search_string':'mt_id=797323&v10=4','pixel_log_child_pixel_search_string':'mt_id=795164&v10=4',
'v10':'4', "uuid": '7fc253a4-acc5-4800-8b40-d1d701b12834','parent_pixel':'773063','child_pixel':'797323','v10_pixel':'795164 ','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v10=4','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=797323&v10=4','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=795164&v10=4'},


'uuid_start_with_7_and_v10_equal_to_5':{'curl_parameter':'&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v10=5',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 795165, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&v10=5','pixel_log_uuid_pixel_search_string':'mt_id=797323&v10=5','pixel_log_child_pixel_search_string':'mt_id=795165&v10=5',
'v10':'5', "uuid": '7fc253a4-acc5-4800-8b40-d1d701b12834','parent_pixel':'773063','child_pixel':'797323','v10_pixel':'795165 ','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v10=5','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=797323&v10=5','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=795165&v10=5'},


'uuid_start_with_7_and_v6_equal_to_male':{'curl_parameter':'&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v6=male',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 795166, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&v6=male','pixel_log_uuid_pixel_search_string':'mt_id=797323&v6=male','pixel_log_child_pixel_search_string':'mt_id=795166&v6=male',
"v6": "male", "uuid": '7fc253a4-acc5-4800-8b40-d1d701b12834','parent_pixel':'773063','child_pixel':'797323','v6_pixel':'795166','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v6=male','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=797323&v6=male','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=795166&v6=male'},

'uuid_not_start_with_7_and_v6_equal_to_male':{'curl_parameter':'&uuid=1c4055b1-3847-4200-bd1b-45ced15a908f&mt_id=773063&v6=male',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(1c4055b1-3847-4200-bd1b-45ced15a908f, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(1c4055b1-3847-4200-bd1b-45ced15a908f, 795166, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&v6=male','pixel_log_uuid_pixel_search_string':'mt_id=797323&v6=male','pixel_log_child_pixel_search_string':'mt_id=795166&v6=male',
"v6": "male", "uuid": '1c4055b1-3847-4200-bd1b-45ced15a908f','parent_pixel':'773063','child_pixel':'797323','v6_pixel':'795166','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=1c4055b1-3847-4200-bd1b-45ced15a908f&mt_id=773063&v6=male','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=1c4055b1-3847-4200-bd1b-45ced15a908f&mt_id=797323&v6=male','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=1c4055b1-3847-4200-bd1b-45ced15a908f&mt_id=795166&v6=male'},

'uuid_not_start_with_7_and_v6_equal_to_female':{'curl_parameter':'&uuid=1c4055b1-3847-4200-bd1b-45ced15a908f&mt_id=773063&v6=female',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(1c4055b1-3847-4200-bd1b-45ced15a908f, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(1c4055b1-3847-4200-bd1b-45ced15a908f, 795167, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&v6=female','pixel_log_uuid_pixel_search_string':'mt_id=797323&v6=female','pixel_log_child_pixel_search_string':'mt_id=795167&v6=female',
"v6": "female", "uuid": '1c4055b1-3847-4200-bd1b-45ced15a908f','parent_pixel':'773063','child_pixel':'797323','v6_pixel':'795167','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=1c4055b1-3847-4200-bd1b-45ced15a908f&mt_id=773063&v6=female','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=1c4055b1-3847-4200-bd1b-45ced15a908f&mt_id=797323&v6=female','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=1c4055b1-3847-4200-bd1b-45ced15a908f&mt_id=795167&v6=female'},

'uuid_start_with_7_and_v6_equal_to_female':{'curl_parameter':'&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v6=female',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 795167, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&v6=female','pixel_log_uuid_pixel_search_string':'mt_id=797323&v6=female','pixel_log_child_pixel_search_string':'mt_id=795167&v6=female',
"v6": "female", "uuid": '7fc253a4-acc5-4800-8b40-d1d701b12834','parent_pixel':'773063','child_pixel':'797323','v6_pixel':'795167','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v6=female','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=797323&v6=female','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=795167&v6=female'},

'uuid_start_with_7_and_s1_equal_to_notshopped':{'curl_parameter':'&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&s1=notshopped',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 795168, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&s1=notshopped','pixel_log_uuid_pixel_search_string':'mt_id=797323&s1=notshopped','pixel_log_child_pixel_search_string':'mt_id=795168&s1=notshopped',
"s1": "notshopped", "uuid": '7fc253a4-acc5-4800-8b40-d1d701b12834','parent_pixel':'773063','child_pixel':'797323','s1_pixel':'795168','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&s1=notshopped','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=797323&s1=notshopped','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=795168&s1=notshopped'},

'uuid_start_with_7_and_s1_equal_to_firstshoppedp12m':{'curl_parameter':'&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&s1=firstshoppedp12m',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 795169, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&s1=firstshoppedp12m','pixel_log_uuid_pixel_search_string':'mt_id=797323&s1=firstshoppedp12m','pixel_log_child_pixel_search_string':'mt_id=795169&s1=firstshoppedp12m',
"s1": "firstshoppedp12m", "uuid": '7fc253a4-acc5-4800-8b40-d1d701b12834','parent_pixel':'773063','child_pixel':'797323','s1_pixel':'795169','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&s1=firstshoppedp12m','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=797323&s1=firstshoppedp12m','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=795169&s1=firstshoppedp12m'},

'uuid_start_with_7_and_s1_equal_to_firstshoppedover12m':{'curl_parameter':'&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&s1=firstshoppedover12m',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 795170, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&s1=firstshoppedover12m','pixel_log_uuid_pixel_search_string':'mt_id=797323&s1=firstshoppedover12m','pixel_log_child_pixel_search_string':'mt_id=795170&s1=firstshoppedover12m',
"s1": "firstshoppedover12m", "uuid": '7fc253a4-acc5-4800-8b40-d1d701b12834','parent_pixel':'773063','child_pixel':'797323','s1_pixel':'795170','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&s1=firstshoppedover12m','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=797323&s1=firstshoppedover12m','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=795170&s1=firstshoppedover12m'},

'uuid_start_with_7_and_v3_equal_to_tshirt':{'curl_parameter':'&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v3=tshirt',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 795171, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&v3=tshirt','pixel_log_uuid_pixel_search_string':'mt_id=797323&v3=tshirt','pixel_log_child_pixel_search_string':'mt_id=795171&v3=tshirt',
"v3": "tshirt", "uuid": '7fc253a4-acc5-4800-8b40-d1d701b12834','parent_pixel':'773063','child_pixel':'797323','v3_pixel':'795171','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v3=tshirt','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=797323&v3=tshirt','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=795171&v3=tshirt'},

'uuid_start_with_7_and_v3_equal_to_t-shirt':{'curl_parameter':'&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v3=t-shirt',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 795171, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&v3=t-shirt','pixel_log_uuid_pixel_search_string':'mt_id=797323&v3=t-shirt','pixel_log_child_pixel_search_string':'mt_id=795171&v3=t-shirt',
"v3": "t-shirt", "uuid": '7fc253a4-acc5-4800-8b40-d1d701b12834','parent_pixel':'773063','child_pixel':'797323','v3_pixel':'795171','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v3=t-shirt','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=797323&v3=t-shirt','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=795171&v3=t-shirt'},

'uuid_start_with_7_and_v3_equal_to_dress':{'curl_parameter':'&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v3=dress',
'udb_log_parent_pixel_search_string':'773063','udb_log_uuid_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 797323, mm",'udb_log_child_pixel_search_string':"addUserToList(7fc253a4-acc5-4800-8b40-d1d701b12834, 795172, mm",
'pixel_log_parent_pixel_search_string':'mt_id=773063&v3=dress','pixel_log_uuid_pixel_search_string':'mt_id=797323&v3=dress','pixel_log_child_pixel_search_string':'mt_id=795171&v3=dress',
"v3": "dress", "uuid": '7fc253a4-acc5-4800-8b40-d1d701b12834','parent_pixel':'773063','child_pixel':'797323','v3_pixel':'795172','expeced_event_in_pixel_log':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=773063&v3=dress','expeced_event_in_pixel_log2':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=797323&v3=dress','expeced_event_in_pixel_log3':'/event/img?mt_nsync&mt_wc=1&uuid=7fc253a4-acc5-4800-8b40-d1d701b12834&mt_id=795172&v3=dress'}

        }
        
class TestMT2(object):


    def setUp(self):
        #super(MT2Test, self).setUp()
        #desired_cap = config_helper.read_config('mt2_cs_n3')
        #self.navigate_to_page(TT_Constants['Base_URL'] + "#/login")
#         desired_cap = config_helper.read_config('mt2_cs_n3')
#         self.ssh = PySSH()
        print "setup insdide..."

        
    def tests_cs_asos_while_fire_pixel(self):
            
        for case in testcase_name:
            yield self.pixel_fire_and_verify_logs, case
            
 
    def pixel_fire_and_verify_logs(self,test):
        data=data_set[test['test_case']]
        issues=[]
        desired_cap = config_helper.read_config('pixel_mt3')
        self.ssh = PySSH()
        self.ssh.connect(desired_cap)
        
        pixel_fire=self.ssh.runcmd("testmt 88 '%s'"%data['curl_parameter'])
        if 'HTTP/1.1 200 OK' not in pixel_fire:
            issues.append('pixel fire does not success..please check')
        
        '''Verify udb logs
            1-verify parent pixel
            2-verify uuid pixel , uuid start with 7
            3-verify child pixel(v6/v10/s1...)
        '''
        retrive_pixel_from_udb_logs=self.ssh.get_pixel_logs(log_type='udb',search_string=data['udb_log_parent_pixel_search_string'])
        if data["udb_log_parent_pixel_search_string"] not in retrive_pixel_from_udb_logs:
            issues.append('retrive_pixel_from_udb_logs does not match with udb_log_parent_pixel_search_string input')

        retrive_pixel_from_udb_logs=self.ssh.get_pixel_logs(log_type='udb',search_string=data['udb_log_child_pixel_search_string'])
        if data["udb_log_child_pixel_search_string"] not in retrive_pixel_from_udb_logs:
            issues.append('retrive_pixel_from_udb_logs:%s does not match with udb_log_child_pixel_search_string input:%s'%(retrive_pixel_from_udb_logs,data["udb_log_child_pixel_search_string"]))
            
        retrive_pixel_from_udb_logs=self.ssh.get_pixel_logs(log_type='udb',search_string=data['udb_log_uuid_pixel_search_string'])
        if 'uuid_not_start_with_7' in test['test_case']:
            if data['udb_log_uuid_pixel_search_string'] in retrive_pixel_from_udb_logs:
                issues.append('retrive_pixel_from_udb_logs should not include child pixel(%s) as uuid not start with 7'%data['child_pixel'])
        else:
            if data['udb_log_uuid_pixel_search_string'] not in retrive_pixel_from_udb_logs:
                issues.append('retrive_pixel_from_udb_logs should include child pixel(%s) as uuid start with 7'%data['child_pixel'])
          
        '''Verify pixel logs
            1-verify parent pixel
            2-verify uuid pixel , uuid start with 7
            3-verify child pixel(v6/v10/s1...)
        '''
        retrive_pixel_from_pixel_logs=self.ssh.get_pixel_logs(log_type='pixel',search_string=data['pixel_log_parent_pixel_search_string'])
        if '%s'%data['expeced_event_in_pixel_log'] not in retrive_pixel_from_pixel_logs:
            issues.append('retrive_pixel_from_pixel_logs:%s does not match with expected input:%s'%(retrive_pixel_from_pixel_logs,data['expeced_event_in_pixel_log']))
          
        retrive_pixel_from_pixel_logs=self.ssh.get_pixel_logs(log_type='pixel',search_string=data['pixel_log_uuid_pixel_search_string'])
        if 'uuid_not_start_with_7' in test['test_case']:
            if '%s'%data['expeced_event_in_pixel_log2'] in retrive_pixel_from_pixel_logs:
                issues.append('retrive_pixel_from_pixel_logs:%s should not include child pixel(%s) as uuid not start with 7'%(retrive_pixel_from_pixel_logs,data['child_pixel']))
            retrive_pixel_from_pixel_logs=self.ssh.get_pixel_logs(log_type='pixel',search_string=data['pixel_log_child_pixel_search_string'])
            if '%s'%data['expeced_event_in_pixel_log3'] not in retrive_pixel_from_pixel_logs:
                issues.append('retrive_pixel_from_pixel_logs should include v6 pixel(%s) as v6=%s'%(data['v6_pixel'],data['v6']))
        else:
            if '%s'%data['expeced_event_in_pixel_log2'] not in retrive_pixel_from_pixel_logs:
                issues.append('retrive_pixel_from_pixel_logs should include child pixel(%s) as uuid start with 7'%data['child_pixel'])
            retrive_pixel_from_pixel_logs=self.ssh.get_pixel_logs(log_type='pixel',search_string=data['pixel_log_child_pixel_search_string'])
            if '%s'%data['expeced_event_in_pixel_log3'] not in retrive_pixel_from_pixel_logs:
                issues.append('retrive_pixel_from_pixel_logs should include v6 pixel(%s) as v6=%s'%(data['v6_pixel'],data['v6']))
        assert not issues, '||'.join(issues)
                       
    def get_pixel_logs(self,cmd):
        desired_cap = config_helper.read_config('pixel_mt3')
        self.ssh = PySSH()
        self.ssh.connect(desired_cap)
        pixel_logs=self.ssh.runcmd(cmd)
        return pixel_logs
        
    def tearDown(self):
        #super(MT2Test, self).tearDown()
        #self.ssh.disconnect()
        print "teardown insdide..."


if __name__ == "__main__":
    unittest.main()
