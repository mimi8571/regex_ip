import re
import ipaddress
import random
import string

#IPv6 w/ double colon in diff places
def ipv6_all_cases():
    ip_6 = []

    for i in range(0, 8):
        if i == 0:
            ip_6.append(str(ipaddress.IPv6Address(random.randint(0,2**128-1))))
            for e in range(1, 8):
                ip_6.append("::" + ":".join(("%x" %  random.randint(0, 16**4) 
                            for s in range(e))))
        else:
            for n in range(0, 8 - i):
                ip_6.append(":".join(("%x" % random.randint(0, 16**4) for f
                            in range(i))) + "::" + ":".join(("%x" % 
                            random.randint(0, 16**4) for n in range(n))))

    return ip_6


#full IPv4
def ipv4():
    ip_4 = []
    ip_4.append(str(ipaddress.IPv4Address(random.randint(0,2**32-1))))

    return ip_4


#regex test (both ipv4 and ipv6)
def regex_parse(ip_address):
    regex = re.compile(r"(((([0-9A-Fa-f]{1,4}:){1,7}(:[0-9A-Fa-f]{1,4}){1,7})|(:(:[0-9A-Fa-f]{1,4}){1,7})|(([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4})|(([0-9A-Fa-f]{1,4}:){1,7}:))|(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))")

    for i in range(0, len(ip_address)):
        result = regex.match(ip_address[i])
        print(ip_address[i])
        print(result)
        print()


#main function
if __name__ == "__main__":
    ip_6 = ipv6_all_cases()
    ip_4 = ipv4()
    regex_parse(ip_6)
    regex_parse(ip_4)

#    for i in range(0, len(ip_6)):
#        print(ip_6[i])
