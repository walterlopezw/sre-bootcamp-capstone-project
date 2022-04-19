import re
import socket
import struct
from netaddr import *

class CidrMaskConvert:
    def cidr_to_mask(self, val):
        # Check if the value is in range
        if int(val) < 1 or int(val) > 255:
            return 'Invalid'
        
        host_bits = 32 - int(val)
        netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
        return netmask

    def mask_to_cidr(self, val):
        octet_list = val.split('.')
        # Check if we have 4 octets
        if len(octet_list) > 4:
            return 'Invalid'

        # Check if all the values are 0
        octet_to_int = [int(x) for x in octet_list]
        if sum(octet_to_int) == 0:
            return 'Invalid'
        
        octet_list = val.split('.')
        negative_offset = 0

        for octet in reversed(octet_list):
            binary = format(int(octet), '08b')
            for char in reversed(binary):
                if char == '1':
                    break
                negative_offset += 1

        return '{0}'.format(32-negative_offset)


class IpValidate:
    def ipv4_validation(self, val):
        if re.match(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",val):
            
            if IPAddress(val).is_private():
                return "Private"
            
            if IPAddress(val).is_loopback():
                return "Loopback"
            
            return "Public"
        else:
            return False
        # try:
        #     socket.inet_pton(socket.AF_INET, val)
        # except AttributeError:  # no inet_pton here, sorry
        #     try:
        #         socket.inet_aton(val)
        #     except socket.error:
        #         return False
        #     return val.count('.') < 4 > 4
        # except socket.error:  # not a valid address
        #     return False
        # return True



# convert = CidrMaskConvert()
# print(convert.cidr_to_mask(1))
# print(convert.cidr_to_mask(0))
# print(convert.mask_to_cidr('0.0.0.0'))
# check_ip = IpValidate()
# print(check_ip.ipv4_validation('127.0.0.1'))
# print(check_ip.ipv4_validation('192.168.1.2.3'))