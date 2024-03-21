from concurrent.futures import *
import requests
banner='''
   ____ ____        _              
  / ___|  _ \ _ __ (_)_ __   ___   
 | |  _| | | | '_ \| | '_ \ / _ \  
 | |_| | |_| | | | | | | | |  __/_ 
  \____|____/|_| |_|_|_| |_|\___(_)
        关注公众号The security.
        本工具仅用于日常学习使用，禁止用于非法域名收集，否则后果由使用者承担！！！
'''
headers = {
        'User-Agent': 'Mozilla/5.0 (x11; Linux x86_64;rv:68.0)Gecko/20100101 Firefox/68.0'   
    }
def check_domain(url,num_threads=10):     #定义一个检查domain状态的函数
        try:            #这里使用try是因为这样才能避开不存在的url的异常，从而继续执行文件里的下一个参数
            resp = requests.get(url=url,headers=headers,timeout=3)
            if resp.status_code == 200:
                print(f"\033[32m{url}\033[0m")   
            else:                       #基于目标网址存在的情况,状态码为200时返回该url，不为200时返回报错的状态码
                print(f"\033[41m{url}:status code: {resp.status_code}\033[0m")       #\033[41m 代表红色     \033[32m 代表绿色
        except:  
            pass #出现异常的情况下跳过

def domain_check(site,max_workers):
    with open('./domain.txt') as file:
        domains=[f"http://{line.strip()}.{site}" for line in file]
    with ThreadPoolExecutor(max_workers=max_workers) as executor:  
        futures = {executor.submit(check_domain, domain): domain for domain in domains}  
        for future in as_completed(futures):  
            domain = futures[future]   
  
if __name__=='__main__':
    print(banner)
    default_domain="baidu.com"
    target_domain = input("请输入要检查的域名（如baidu.com）: ")  
    if target_domain:
        default_domain=target_domain
    num_threads_input = input("请输入线程数(默认为10): ")  
    max_workers = int(num_threads_input) if num_threads_input.isdigit() else 10  # 转换输入为整数，或默认为10  
    domain_check(default_domain,max_workers)
