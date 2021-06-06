import xml.etree.ElementTree as ET
import applescript

tree = ET.parse('Sessions.XML')
root = tree.getroot()
seqNum = 0

# for child in root:
#     print(child.tag, child.attrib)
# print(root[4].attrib)

# device = root[0].attrib["SessionName"]
# hostIp = root[0].attrib["Host"]
# user = root[0].attrib["Username"]
# passwd = root[0].attrib["ExtraArgs"][4:]
# print (device, hostIp)

# applescript.tell.app('Terminal', 'do script "' + 'sshpass -p ' + passwd + ' ssh ' + user + '@' + hostIp + '"')

for child in root:
    device = child.attrib["SessionName"]
    hostIp = child.attrib["Host"]
    user = child.attrib["Username"]
    protocol = child.attrib["Proto"]
    passwd = child.attrib["ExtraArgs"][4:]
    print (seqNum, hostIp, user, passwd, device, protocol)
    seqNum = seqNum + 1

# deviceNumber = input("deviceNumber to connect:")

# for i in range(30):
    # deviceNumber = input("deviceNumber to connect:")
    # deviceNumber = str(i - 1)
    # print(type(deviceNumber))

    # if not (deviceNumber.isnumeric()):
    #     continue
    # else:
    #     if int(deviceNumber) > (seqNum-1):
    #         continue

    # if ( not (deviceNumber.isnumeric()) and (int(str(deviceNumber)) < (seqNum-1)):
    #     pass
    # else:
    #     print ("non integer")
    #     continue

        # hostIp = root[int(deviceNumber)].attrib["Host"]
        # user = root[int(deviceNumber)].attrib["Username"]
        # passwd = root[int(deviceNumber)].attrib["ExtraArgs"][4:]
        # device = root[int(deviceNumber)].attrib["SessionName"]
        # protocol = root[int(deviceNumber)].attrib["Proto"]
        # print (deviceNumber, hostIp, user, passwd, device, protocol)

        # if protocol == "SSH":
        #     applescript.tell.app('Terminal', 'do script "' + 'sshpass -p ' + passwd + ' ssh ' + user + '@' + hostIp + '"')
        # elif protocol =="Telnet":
        #     applescript.tell.app('Terminal', 'do script "' + 'telnet ' + hostIp + '"')
# Testing git changes
#     for key, value in root[0].attrib.items():
#         device = root[0].attrib["SessionName"]
#         hostIp = root[0].attrib["Host"]
#         user = root[0].attrib["Username"]
#         passwd = root[0].attrib["ExtraArgs"][4:]
#         print (device, hostIp)

# applescript.tell.app('Terminal', 'do script "' + 'sshpass -p ' + passwd + ' ssh ' + user + '@' + hostIp + '"')

# print (hostIp, user, passwd)

# hostIp = "10.76.108.27"
# user = "admin"
# passwd = "Physec123!"

# applescript.tell.app('Terminal', 'do script "' + 'sshpass -p ' + passwd + ' ssh ' + user + '@' + hostIp + '"')
