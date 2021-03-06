'''
Script to use nmap to help verify ports are open on certain devices.
Nmap: Nmap is a free and open-source network scanning tool. https://pypi.org/project/python3-nmap/
import nmap3
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("your-host.com")
# And you would get your results in json
'''

import nmap3
import click


@click.group(help='Port Scanner')
def scan_port():
	pass

@scan_port.command(help = 'Returns Port Scan Results')
@click.argument('port_number')
def scan_port(port_number):
   
    # take the range of ports to  
    # be scanned 
    begin = 75
    end = 80

    # assign the target ip to be scanned to 
    # a variable 
    target = '127.0.0.1'

    # instantiate a PortScanner object 
    scanner = nmap3.PortScanner() 

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
        
if __name__ == "__init__" :
    scan_port('80')
