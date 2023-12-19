#!/usr/bin/env python3.6

import subprocess
import argparse

def check_haproxy_conns(url, user, password, warning, critical):
    curl_command = f'curl -s -u {user}:{password} -H "Accept: application/json" {url}/stats | grep conns'
    
    try:
        result = subprocess.run(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        current_conns = int(output.split('=')[1].split(';')[0].strip())
        
        perfdata = f"'current_conns'={current_conns};{warning};{critical}"
        
        if current_conns >= critical:
            print(f'CRITICAL - Current connections: {current_conns} | {perfdata}')
            exit(2)
        elif current_conns >= warning:
            print(f'WARNING - Current connections: {current_conns} | {perfdata}')
            exit(1)
        else:
            print(f'OK - Current connections: {current_conns} | {perfdata}')
            exit(0)
            
    except subprocess.CalledProcessError as e:
        print(f'UNKNOWN - Error executing command: {e}')
        exit(3)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check HAProxy current connections.')
    parser.add_argument('url', help='HAProxy URL')
    parser.add_argument('user', help='HAProxy username')
    parser.add_argument('password', help='HAProxy password')
    parser.add_argument('-w', '--warning', type=int, help='Warning threshold for current connections')
    parser.add_argument('-c', '--critical', type=int, help='Critical threshold for current connections')
    
    args = parser.parse_args()
    
    check_haproxy_conns(args.url, args.user, args.password, args.warning, args.critical)

