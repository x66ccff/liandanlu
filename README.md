# liandanlu
Python package for managing ML linux server

## Install

```bash
python setup.py install
```

## Quick Start

### get the memory usage

```python
>>> import liandanlu as ldl
>>> ldl.gpu.get_memory_list()
[0]
```

### auto run when gpu is free
```python
>>> import liandanlu as ldl
>>> ldl.run_when_gpu_free(gpu_index=0,command='echo hello') 
显存占用: 0  编号: 0  低于10时运行echo hello
hello
```

### notice wechat when gpu is free
```python
>>> import liandanlu as ldl
>>> ldl.notice_when_gpu_free(gpu_index=0,title='hi',content='wechat!',key='your key') 
```


## Roadmap

1. 支持低代码根据GPU显存触发各种操作，如执行代码，通知手机等
2. 顺序执行 python 代码
