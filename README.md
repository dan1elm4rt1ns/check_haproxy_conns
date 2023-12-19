Check HAProxy current connections.

Arguments:
  -h, --help            show this help message and exit
  -U URL, --url URL     HAProxy URL
  -u USER, --user USER  HAProxy username
  -p PASSWORD, --password PASSWORD
                        HAProxy password
  -w WARNING, --warning WARNING
                        Warning threshold for current connections
  -c CRITICAL, --critical CRITICAL
                        Critical threshold for current connections

Example:

./check_haproxy_conns.py -U http://127.0.0.1:32600 -u user -p password -w 300 -c 350
OK - Current connections: 279 | 'current_conns'=279;300;350
