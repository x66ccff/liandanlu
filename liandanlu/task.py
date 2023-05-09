import time
from . import notice
from . import gpu
import os

def notice_when_gpu_free(gpu_index,
                    memory_threshold = 10,
                    freq_second = 60,
                    log = True,
                    key = None,
                    n_check = 3,
                    title = "GPU is free now",
                    content = ""):
    '''当 GPU 占用率低的时候通知手机，只触发一次

    memory_threshold (MB)
    time_threshold (s)
    key (str)
    '''
    n_hit = 0
    
    assert key is not None
    assert type(key) is str
    while True:
        # 获取当前 GPU 显存占用率
        gpu_mem_list = gpu.get_memory_list()

        if gpu_mem_list is not None:
            # 打印当前占用率
            usage = gpu_mem_list[gpu_index]
            if log:
                print(f"显存占用: {usage}  编号: {gpu_index}  低于{memory_threshold}时通知手机")
            if usage < memory_threshold:
                n_hit += 1
            else:
                n_hit = 0
            
            if n_hit > n_check:
                # 触发 foo 函数
                notice.send_to_wechat(title,content,key)
                exit()
        # 等待 1 分钟
        time.sleep(freq_second)

def run_when_gpu_free(gpu_index,
                    memory_threshold = 10,
                    freq_second = 60,
                    n_check = 3,
                    log = True,
                    command = None):
    '''当 GPU 占用率低的时候通知手机，只触发一次

    memory_threshold (MB)
    time_threshold (s)
    key (str)
    n_check 检查多少次，如果都满足条件才触发
    '''
    n_hit = 0
    
    assert command is not None
    assert type(command) is str
    while True:
        # 获取当前 GPU 显存占用率
        gpu_mem_list = gpu.get_memory_list()

        if gpu_mem_list is not None:
            # 打印当前占用率
            usage = gpu_mem_list[gpu_index]
            if log:
                print(f"显存占用: {usage}  编号: {gpu_index}  低于{memory_threshold}时运行{command}")
            if usage < memory_threshold:
                n_hit += 1
            else:
                n_hit = 0
            
            if n_hit > n_check:
                # 执行脚本
                os.system(command)
                exit()
        # 等待 1 分钟
        time.sleep(freq_second)