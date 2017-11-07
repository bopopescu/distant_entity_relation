import urllib2, socket
import pyprind
socket.setdefaulttimeout(1)

# read the list of proxy IPs in proxyList
#proxyList = ['172.30.1.1:8080', '172.30.3.3:8080'] # there are two sample proxy ip

def is_bad_proxy(pip):
    try:
        proxy_handler = urllib2.ProxyHandler({'http': pip})
        opener = urllib2.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib2.install_opener(opener)
        req=urllib2.Request('http://www.google.com')  # change the url address here
        sock=urllib2.urlopen(req)
    except urllib2.HTTPError, e:
#        print 'Error code: ', e.code
        return e.code
    except Exception, detail:

 #       print "ERROR:", detail
        return 1
    return 0


#i=52


#j=256

#k=[3128]
#for i in range(50,500):
#    for j in range(50,500):
       # for l in range(2)
#a='172.16.69.131:3128'
#print ai

count=1
bar=pyprind.ProgBar(50,monitor=True)
file=open('Proxy_list2.txt','r+')
for f in file:
    if is_bad_proxy(f):
        o=0
        print count
        count=count+1
    else:
        print count
        print f
        count=count+1
