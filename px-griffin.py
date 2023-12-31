import requests
import argparse
import json
import os
import time
print ("""
 .-----------------------------.
 |  Tool   : PX-Griffin        |
 |  Author : @shyam_the_hacker | 
 |  version: 0.3               |           
 '-----------------------------'           
                 ^      (\_/)    
                 '----- (O.o)    
                        (> <)\n""")
time.sleep(2)



def track_ip(ip, output_path=None):
    url = f"http://ip-api.com/json/{ip}"
    res = requests.get(url)
    data = json.loads(res.content)

    result = f"IP Information for {ip}:\n"
    result += f"\t[+]IP\t\t {data['query']}\n"
    result += f"\t[+]STATUS\t {data['status']}\n"
    result += f"\t[+]CITY\t\t {data['city']}\n"
    result += f"\t[+]ISP\t\t {data['isp']}\n"
    result += f"\t[+]COUNTRY\t {data['countryCode']}\n"
    result += f"\t[+]REG NAME\t {data['regionName']}\n"
    result += f"\t[+]TIME ZONE\t {data['timezone']}\n"
    result += f"\t[+]ZIP\t\t {data['zip']}\n"
    result += f"\t[+]LAT\t\t {data['lat']}\n"
    result += f"\t[+]LON\t\t {data['lon']}\n"
    result += f"\t[+]AS\t\t {data.get('as', 'N/A')}\n"
    result += f"\t[+]ORG\t\t {data.get('org', 'N/A')}\n"

    if output_path:
        if os.path.isdir(output_path):
            output_file = os.path.join(output_path, "ip_info.txt")
        else:
            output_file = output_path

        with open(output_file, "w") as file:
            file.write(result)
        print(f"Results saved to {output_file}")
    else:
        print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ipaddress", help="Enter IP Address TO Track", required=True)
    parser.add_argument("-o", "--output", help="Specify output file or folder")
    args = parser.parse_args()
    ip = args.ipaddress
    output_path = args.output

    track_ip(ip, output_path)



