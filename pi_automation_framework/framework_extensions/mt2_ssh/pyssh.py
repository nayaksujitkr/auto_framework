#!/usr/bin/env python

import sys
import socket
import paramiko
import time
import select
import logging
#=================================
# Class: PySSH
#=================================

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PySSH(object):


   
    def __init__ (self):
        self.ssh = None
        self.transport = None 
    
    def disconnect (self):
        if self.transport is not None:
           self.transport.close()
           logger.info('ssh transport disconnect...')
        if self.ssh is not None:
           self.ssh.close()
           logger.info('ssh disconnect...')
 
    def connect(self,desired_cap):#hostname,username,password,port=22):
        self.hostname = desired_cap['hostname']
        self.username = desired_cap['username']
        self.password = desired_cap['password']
        self.port = desired_cap['port']
 
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.load_system_host_keys()
        try:
            if desired_cap['username']=='pixel':
                pkey_file=desired_cap['pkeyfile']
                key = paramiko.RSAKey.from_private_key_file(pkey_file)
                self.ssh.connect(desired_cap['hostname'],port=desired_cap['port'],username=desired_cap['username'],pkey=key)
            else:  
                self.ssh.connect(desired_cap['hostname'],port=desired_cap['port'],username=desired_cap['username'],password=desired_cap['password'])
            self.transport=self.ssh.get_transport()
        except (socket.error,paramiko.AuthenticationException) as message:
            print "ERROR: SSH connection to "+self.hostname+" failed: " +str(message)
            sys.exit(1)
        return  self.transport is not None

    def get_pixel_logs(self,**kwargs):
        if kwargs['log_type']=='udb':
            find_udb_log_file=self.runcmd("current_log_location=$(ls -rt --group-directories-first /apps/pixel/log/udb | tail -n 1)")
            retrive_pixel_logs=self.runcmd("grep -nr '%s' /apps/pixel/log/udb/${current_log_location}"%kwargs['search_string'])
        if kwargs['log_type']=='pixel':
            find_udb_log_file=self.runcmd("current_log_location=$(ls -rt --group-directories-first /apps/pixel/log/pixel | tail -n 1)")
            retrive_pixel_logs=self.runcmd("grep -nr '%s' /apps/pixel/log/pixel/${current_log_location}"%kwargs['search_string'])
        return retrive_pixel_logs
    
    def runcmd(self,cmd,sudoenabled=False):
        self.transport=self.ssh.get_transport()
        pixel_logs=""
        if sudoenabled:
            fullcmd="echo " + self.password + " |   sudo -S -p '' " + cmd
        else:
            fullcmd=cmd
        if self.transport is None:
            return "ERROR: connection was not established"
        session=self.transport.open_session()
        #session.set_combine_stderr(True)
        #print "fullcmd ==== "+fullcmd
        if sudoenabled:
            session.get_pty()
        session.exec_command(fullcmd)
#         stdout = session.makefile('rb', -1)
#         #print stdout.read()
#         output=stdout.read()
#         session.close()
        while True:
            if session.exit_status_ready():
                break
            rl, wl, xl = select.select([session], [], [], 0.0)
            if len(rl) > 0:
                pixel_logs= session.recv(1024)
                print pixel_logs
                session.close()
                #self.ssh.close()
        return pixel_logs