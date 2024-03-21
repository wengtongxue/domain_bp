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
def check_domain(url,num_threads=10):
        try:            #这里使用try是因为这样才能避开不存在的url的异常，从而继续执行文件里的下一个参数
            resp = requests.post(url=url,headers=headers,timeout=3)
            if resp.status_code == 200:
                print(url)   
            else:
                print(f"{url}, status code: {resp.status_code}")
        except :  
            pass
def domain_check(site,num_threads):
    with open('./domain.txt') as file:
        domains=[f"http://{line.strip()}.{site}" for line in file]
    with ThreadPoolExecutor(max_workers=num_threads) as executor:  
        futures = {executor.submit(check_domain, domain, num_threads): domain for domain in domains}  

        for future in as_completed(futures):  
            domain = futures[future]  
            try:  
                # 可以在这里处理future.result()，如果有返回值的话  
                pass  
            except Exception as exc:  
                print(f'Generated an exception: {exc}')  
  
if __name__=='__main__':
    print(banner)
    target_domain = input("请输入要检查的域名（如baidu.com）: ")  
    num_threads_input = input("请输入线程数(默认为10): ")  
try:  
    num_threads = int(num_threads_input)  
    if num_threads < 1:  
        raise ValueError("线程数必须为正整数")  
except ValueError:  
    num_threads = 10  # 默认值 
    domain_check(target_domain,num_threads)