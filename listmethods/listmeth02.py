#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
print("The second item in the list (port): " + str(my_list[1])
53protocount = proto.count(53)
53protoacount = protoa.cout(53)
print("Count of 53 in proto: ", 53protocount)
print("Count of 53 in protoa: " + 53protoacount)
