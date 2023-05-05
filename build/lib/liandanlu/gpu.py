import os

def get_memory_list():
    """获取 GPU 显存占用率，返回 List，表示各个显卡的占用率"""
    try:
        output = os.popen('nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits').read()
        gpu_memory_used = [int(x) for x in output.strip().split('\n')]
        return gpu_memory_used
    except Exception as e:
        print(f"获取 GPU 显存占用率失败: {e}")
        return None
