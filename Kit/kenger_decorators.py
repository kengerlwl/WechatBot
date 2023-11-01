import time 
import functools
from flask import request
from Config import *
import Kit

# 用于验证请求的token的装饰器
def verify_request_token(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        token = None
        if request.method == 'GET':
            # 获取请求参数中的token
            token = request.args.get('token')
        elif request.method == 'POST':
            # 获取请求参数中的token
            token = request.data.get('token')


        if token:
            conf = get_config()
            conf_token = conf["secrets"]['token']
            if token != conf_token:
                return Kit.common_rsp(data="token error", status="Forbidden")
        else:
            return Kit.common_rsp(data="token error", status="Forbidden")
        
        return func(*args, **kwargs)
    return wrapper


# 统计函数执行时间的装饰器
def timer(func): 
    @functools.wraps(func)
    def wrapper(*args, **kwargs): 
        print(f"Executing {func.__name__}...")
        start_time = time.time() 
        result = func(*args, **kwargs) 
        end_time = time.time() 
        print(f"{func.__name__} took {end_time - start_time:.2f} seconds to execute.") 
        return result 
    return wrapper 


@timer 
def my_data_processing_function(): 
    time.sleep(1) 
    return "Finished processing."


# 缓存函数执行结果的装饰器
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print("cache hit")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)





# 用于验证函数输入有效性的装饰器
def validate_input(func): 
    @functools.wraps(func)
    def wrapper(*args, **kwargs): 
        valid_data = False  # 初始化数据有效性为 False

        # 在这里添加你的数据验证逻辑
        data = args[0]  # 获取传递给被装饰函数的第一个参数（假设 data 就是第一个参数）

        if data is not None:
            valid_data = True  # 如果数据不为 None，认为数据有效

        if valid_data: 
            return func(*args, **kwargs) 
        else: 
            raise ValueError("Invalid data. Please check your inputs.") 

    return wrapper 

@validate_input 
def analyze_data(data): 
    # 在这里添加你的数据分析代码
    print("Data analysis is being performed.")





# @log_results: 日志输出
# 在运行复杂的数据分析时，跟踪每个函数的输出变得至关重要。
# @log_results 装饰器可以帮助我们记录函数的结果，以便于调试和监控。
def log_results(func): 
    @functools.wraps(func)
    def wrapper(*args, **kwargs): 
        result = func(*args, **kwargs) 
        with open("results.log", "a") as log_file: 
            log_file.write(f"{func.__name__} - Result: {result}\n") 
        return result 

    return wrapper 

@log_results 
def calculate_metrics(data): 
    # 在这里添加你的指标计算代码
    # 假设这里计算了一些指标并将结果返回
    return {"metric1": 0.85, "metric2": 0.92}




import time 

def retry(max_attempts, delay): 
    def decorator(func): 
        @functools.wraps(func)
        def wrapper(*args, **kwargs): 
            attempts = 0 
            while attempts < max_attempts: 
                try: 
                    return func(*args, **kwargs) 
                except Exception as e: 
                    print(f"Attempt {attempts + 1} failed. Retrying in {delay} seconds.") 
                    attempts += 1 
                    time.sleep(delay) 
            raise Exception("Max retry attempts exceeded.") 
        return wrapper 
    return decorator 

@retry(max_attempts=3, delay=2) 
def fetch_data_from_api(api_url): 
    # 在这里添加你的从 API 获取数据的代码
    # 假设这里是一个模拟，每次都会抛出异常
    print("Fetching data from API...")
    raise Exception("API request failed")




if __name__ == "__main__":

    # time_decorator test case
    # my_data_processing_function()

    # memoize test case
    # 测试 fibonacci 函数
    # print(fibonacci(10))  # 输出: 55

    # 测试 analyze_data 函数
    # analyze_data(None)  # 这里传递了 None 作为示例数据


    # # 测试 calculate_metrics 函数
    # data = ...  # 你的数据
    # result = calculate_metrics(data)
    # print("Metrics calculated:", result)



    # 测试 fetch_data_from_api 函数, 会重试3次
    try:
        fetch_data_from_api("https://example.com/api/data")
    except Exception as e:
        print("Exception:", e)