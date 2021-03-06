#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        DS18B20.py
#
#  Project :     
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      maxim.stassevich$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["DS18B20", "DS18B20Class", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(DS18B20.additionnal_import) ENABLED START -----#
import os
import glob
import time
import threading


class readDS18B20(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.running = True
        self.fault = False
        self.temperature1 = None
        self.temperature2 = None
        self.temperature3 = None
        self.temperature4 = None
        self.temperature5 = None
        self.temperature6 = None
        self.temperature7 = None
        self.temperature8 = None
        
        self.temperatures = [self.temperature1, self.temperature2, self.temperature3,         self.temperature4, self.temperature5, self.temperature6, self.temperature7, self.temperature8]
        
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')
        base_dir = '/sys/bus/w1/devices/'
        """device_folder1 = glob.glob(base_dir + '28*')[0]
        device_folder2 = glob.glob(base_dir + '28*')[1]
        device_folder3 = glob.glob(base_dir + '28*')[2]
        device_folder4 = glob.glob(base_dir + '28*')[3]
        device_folder5 = glob.glob(base_dir + '28*')[4]
        device_folder6 = glob.glob(base_dir + '28*')[5]
        device_folder7 = glob.glob(base_dir + '28*')[6]
        device_folder8 = glob.glob(base_dir + '28*')[7]"""
        device_folder1 = "/sys/bus/w1/devices/" + "28-000008db3a81"
        device_folder2 = "/sys/bus/w1/devices/" + "28-000008da0993"
        device_folder3 = "/sys/bus/w1/devices/" + "28-000008dc5b84"
        device_folder4 = "/sys/bus/w1/devices/" + "28-000008db6e65"
        device_folder5 = "/sys/bus/w1/devices/" + "28-000008da81d1"
        device_folder6 = "/sys/bus/w1/devices/" + "28-000008daee21"
        device_folder7 = "/sys/bus/w1/devices/" + "28-000007f1c401"
        device_folder8 = "/sys/bus/w1/devices/" + "28-000007f1764c"
        device_file1 = device_folder1 + '/w1_slave'
        device_file2 = device_folder2 + '/w1_slave'
        device_file3 = device_folder3 + '/w1_slave'
        device_file4 = device_folder4 + '/w1_slave'
        device_file5 = device_folder5 + '/w1_slave'
        device_file6 = device_folder6 + '/w1_slave'
        device_file7 = device_folder7 + '/w1_slave'
        device_file8 = device_folder8 + '/w1_slave'
        self.device_files = [device_file1, device_file2, device_file3, device_file4, device_file5, device_file6, device_file7, device_file8]
        
        print "Starting thread"
        
    def run(self):
        while self.running:
            for i in range(len(self.device_files)):
                try:
                    self.temperatures[i] = float(self.read_temp(self.device_files[i]))                    
                    self.fault = False                
                except:
                    self.temperatures[i] = -300.00      
                    self.fault = True
                    time.sleep(0.3)
        print "Thread exited"
        
    def stop(self):
        print "Exiting thread.."
        self.running = False
        #self.wait()
    
    def read_temp_raw(self, device_file):
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
    
    def read_temp(self, device_file):
        lines = self.read_temp_raw(device_file)
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_temp_raw(device_file)
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c
                
    def getData(self):
        return self.fault, self.temperatures




#----- PROTECTED REGION END -----#	//	DS18B20.additionnal_import

# Device States Description
# ON : 
# OFF : 


class DS18B20 (PyTango.Device_4Impl):
    """Class to control DS18B20"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(DS18B20.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	DS18B20.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        DS18B20.init_device(self)
        #----- PROTECTED REGION ID(DS18B20.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	DS18B20.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(DS18B20.delete_device) ENABLED START -----#
        self.DS18B20.stop()
        #----- PROTECTED REGION END -----#	//	DS18B20.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_temperature1_read = 0.0
        self.attr_temperature2_read = 0.0
        self.attr_temperature3_read = 0.0
        self.attr_temperature4_read = 0.0
        self.attr_temperature5_read = 0.0
        self.attr_temperature6_read = 0.0
        self.attr_temperature7_read = 0.0
        self.attr_temperature8_read = 0.0
        #----- PROTECTED REGION ID(DS18B20.init_device) ENABLED START -----#
        self.set_state(PyTango.DevState.ON)
        self.set_status("Device is in ON state")
        self.DS18B20 = readDS18B20()
        self.DS18B20.start()
        #----- PROTECTED REGION END -----#	//	DS18B20.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(DS18B20.always_executed_hook) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	DS18B20.always_executed_hook

    # -------------------------------------------------------------------------
    #    DS18B20 read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_temperature1(self, attr):
        self.debug_stream("In read_temperature1()")
        #----- PROTECTED REGION ID(DS18B20.temperature1_read) ENABLED START -----#
        attr.set_value(self.attr_temperature1_read)
        
        #----- PROTECTED REGION END -----#	//	DS18B20.temperature1_read
        
    def is_temperature1_allowed(self, attr):
        self.debug_stream("In is_temperature1_allowed()")
        if attr==PyTango.AttReqType.READ_REQ:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        else:
            state_ok = not(self.get_state() in [])
        #----- PROTECTED REGION ID(DS18B20.is_temperature1_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	DS18B20.is_temperature1_allowed
        return state_ok
        
    def read_temperature2(self, attr):
        self.debug_stream("In read_temperature2()")
        #----- PROTECTED REGION ID(DS18B20.temperature2_read) ENABLED START -----#
        attr.set_value(self.attr_temperature2_read)
        
        #----- PROTECTED REGION END -----#	//	DS18B20.temperature2_read
        
    def is_temperature2_allowed(self, attr):
        self.debug_stream("In is_temperature2_allowed()")
        if attr==PyTango.AttReqType.READ_REQ:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        else:
            state_ok = not(self.get_state() in [])
        #----- PROTECTED REGION ID(DS18B20.is_temperature2_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	DS18B20.is_temperature2_allowed
        return state_ok
        
    def read_temperature3(self, attr):
        self.debug_stream("In read_temperature3()")
        #----- PROTECTED REGION ID(DS18B20.temperature3_read) ENABLED START -----#
        attr.set_value(self.attr_temperature3_read)
        
        #----- PROTECTED REGION END -----#	//	DS18B20.temperature3_read
        
    def is_temperature3_allowed(self, attr):
        self.debug_stream("In is_temperature3_allowed()")
        if attr==PyTango.AttReqType.READ_REQ:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        else:
            state_ok = not(self.get_state() in [])
        #----- PROTECTED REGION ID(DS18B20.is_temperature3_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	DS18B20.is_temperature3_allowed
        return state_ok
        
    def read_temperature4(self, attr):
        self.debug_stream("In read_temperature4()")
        #----- PROTECTED REGION ID(DS18B20.temperature4_read) ENABLED START -----#
        attr.set_value(self.attr_temperature4_read)
        
        #----- PROTECTED REGION END -----#	//	DS18B20.temperature4_read
        
    def is_temperature4_allowed(self, attr):
        self.debug_stream("In is_temperature4_allowed()")
        if attr==PyTango.AttReqType.READ_REQ:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        else:
            state_ok = not(self.get_state() in [])
        #----- PROTECTED REGION ID(DS18B20.is_temperature4_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	DS18B20.is_temperature4_allowed
        return state_ok
        
    def read_temperature5(self, attr):
        self.debug_stream("In read_temperature5()")
        #----- PROTECTED REGION ID(DS18B20.temperature5_read) ENABLED START -----#
        attr.set_value(self.attr_temperature5_read)
        
        #----- PROTECTED REGION END -----#	//	DS18B20.temperature5_read
        
    def is_temperature5_allowed(self, attr):
        self.debug_stream("In is_temperature5_allowed()")
        if attr==PyTango.AttReqType.READ_REQ:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        else:
            state_ok = not(self.get_state() in [])
        #----- PROTECTED REGION ID(DS18B20.is_temperature5_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	DS18B20.is_temperature5_allowed
        return state_ok
        
    def read_temperature6(self, attr):
        self.debug_stream("In read_temperature6()")
        #----- PROTECTED REGION ID(DS18B20.temperature6_read) ENABLED START -----#
        attr.set_value(self.attr_temperature6_read)
        
        #----- PROTECTED REGION END -----#	//	DS18B20.temperature6_read
        
    def is_temperature6_allowed(self, attr):
        self.debug_stream("In is_temperature6_allowed()")
        if attr==PyTango.AttReqType.READ_REQ:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        else:
            state_ok = not(self.get_state() in [])
        #----- PROTECTED REGION ID(DS18B20.is_temperature6_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	DS18B20.is_temperature6_allowed
        return state_ok
        
    def read_temperature7(self, attr):
        self.debug_stream("In read_temperature7()")
        #----- PROTECTED REGION ID(DS18B20.temperature7_read) ENABLED START -----#
        attr.set_value(self.attr_temperature7_read)
        
        #----- PROTECTED REGION END -----#	//	DS18B20.temperature7_read
        
    def is_temperature7_allowed(self, attr):
        self.debug_stream("In is_temperature7_allowed()")
        if attr==PyTango.AttReqType.READ_REQ:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        else:
            state_ok = not(self.get_state() in [])
        #----- PROTECTED REGION ID(DS18B20.is_temperature7_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	DS18B20.is_temperature7_allowed
        return state_ok
        
    def read_temperature8(self, attr):
        self.debug_stream("In read_temperature8()")
        #----- PROTECTED REGION ID(DS18B20.temperature8_read) ENABLED START -----#
        attr.set_value(self.attr_temperature8_read)
        
        #----- PROTECTED REGION END -----#	//	DS18B20.temperature8_read
        
    def is_temperature8_allowed(self, attr):
        self.debug_stream("In is_temperature8_allowed()")
        if attr==PyTango.AttReqType.READ_REQ:
            state_ok = not(self.get_state() in [PyTango.DevState.OFF])
        else:
            state_ok = not(self.get_state() in [])
        #----- PROTECTED REGION ID(DS18B20.is_temperature8_allowed) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	DS18B20.is_temperature8_allowed
        return state_ok
        
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(DS18B20.read_attr_hardware) ENABLED START -----#
        fault, temperatures = self.DS18B20.getData()
        """if fault == True:
            if self.get_state() != PyTango.DevState.OFF:
                self.set_state(PyTango.DevState.OFF)
                self.set_status("Device is in OFF state")
        else:
            if self.get_state() != PyTango.DevState.ON:
                self.set_state(PyTango.DevState.ON)
                self.set_status("Device is in ON state")"""
        self.attr_temperature1_read = temperatures[0]
        self.attr_temperature2_read = temperatures[1]
        self.attr_temperature3_read = temperatures[2]
        self.attr_temperature4_read = temperatures[3]
        self.attr_temperature5_read = temperatures[4]
        self.attr_temperature6_read = temperatures[5]
        self.attr_temperature7_read = temperatures[6]
        self.attr_temperature8_read = temperatures[7]
        #----- PROTECTED REGION END -----#	//	DS18B20.read_attr_hardware


    # -------------------------------------------------------------------------
    #    DS18B20 command methods
    # -------------------------------------------------------------------------
    

    #----- PROTECTED REGION ID(DS18B20.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	DS18B20.programmer_methods

class DS18B20Class(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(DS18B20.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	DS18B20.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        }


    #    Command definitions
    cmd_list = {
        }


    #    Attribute definitions
    attr_list = {
        'temperature1':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'label': "Temperature1",
                'unit': "�C",
            } ],
        'temperature2':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'label': "Temperature2",
                'unit': "�C",
            } ],
        'temperature3':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'label': "Temperature3",
                'unit': "�C",
            } ],
        'temperature4':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'label': "Temperature4",
                'unit': "�C",
            } ],
        'temperature5':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'label': "Temperature5",
                'unit': "�C",
            } ],
        'temperature6':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'label': "Temperature6",
                'unit': "�C",
            } ],
        'temperature7':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'label': "Temperature7",
                'unit': "�C",
            } ],
        'temperature8':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'label': "Temperature8",
                'unit': "�C",
            } ],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(DS18B20Class, DS18B20, 'DS18B20')
        #----- PROTECTED REGION ID(DS18B20.add_classes) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	DS18B20.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
