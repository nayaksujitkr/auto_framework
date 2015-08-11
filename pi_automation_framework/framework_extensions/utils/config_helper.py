import yaml
import sys
import re
import urllib2
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def read_config(server):
    """
        reads server desired_capabilities from test_config yaml.
        Args:
            server: server name
    """
    try:
        with open('C:/Users/snayak/workspace/pi_automation_framework/framework_extensions/utils/config.yaml') as config_file:
            config = yaml.load(config_file)
        try:
            desired_cap = config[server]
            try:
                username = desired_cap["username"]
                password = desired_cap["password"]
                hostname = desired_cap["hostname"]
                port = desired_cap["port"]
                return desired_cap    
            except KeyError as e2:
                logger.info("Please provide valid app hostname/username/password/port_no in test_config.yaml file")
        except KeyError as e3:
            logger.info("Missing configuration for device %s. Please provide valid device configuration in test_config.yaml file" %server)
    except IOError as e:
        logger.info("test_config.yaml file is missing")


