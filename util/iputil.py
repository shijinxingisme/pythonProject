import requests
import random
import struct
import json
import socket


# 内部函数：将IP地址转换成long整数
def ip2long(ip):
    return struct.unpack("!L", socket.inet_aton(ip))[0]


# 内部函数：将long整数转换成IP地址
def long2ip(ip):
    return socket.inet_ntoa(struct.pack("!L", ip))


# 获取指定城市的IP地址范围
def getIPRange(city):
    try:
        url = f"http://ip.taobao.com/service/getIpInfo.php?ip={city}"
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            if "code" in result and result["code"] == 0:
                ip_start = result["data"]["start_ip"]
                ip_end = result["data"]["end_ip"]
                return ip_start, ip_end
    except:
        pass
    return None, None


# 随机生成指定城市的IP地址
def generateRandomIP(city):
    try:
        ip_start, ip_end = getIPRange(city)
        if ip_start is not None and ip_end is not None:
            start_ip = ip2long(ip_start)
            end_ip = ip2long(ip_end)
            random_ip = long2ip(random.randint(start_ip, end_ip))
            return random_ip
    except:
        pass
    return None


# 示例：随机生成中国西安市的IP地址
random_ip = generateRandomIP("西安")
if random_ip is not None:
    print("Generated random IP: ", random_ip)
else:
    print("Failed to generate random IP.")
