import nmap
   
# take the range of ports to 
# be scanned
begin = 1
end = 1047
  
# assign the target ip to be scanned to
# a variable
target = input("enter target host:>>>")
   
# instantiate a PortScanner object
scanner = nmap.PortScanner()
   
for i in range(begin,end+1):
   
    # scan the target port
    res = scanner.scan(target,str(i))
   
    # the result is a dictionary containing 
    # several information we only need to
    # check if the port is opened or closed
    # so we will access only that information 
    # in the dictionary
    res = res['scan'][target]['tcp'][i]['state']
   
    print(f'port {i} is {res}.')
