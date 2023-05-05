import requests

def send_to_wechat(title,content="",key=None):
    ''' 向 Server 酱发送信息，使用前请设定个人 ldl.key '''
    assert key is not None # 使用前请设定个人 ldl.key
    url ="https://sctapi.ftqq.com/"+ str(key) +".send?title=" +title +"&desp="+content
    re = requests.get(url)
    is_success = True if '"errno":0' in re.text else False
    if is_success:
        return True,None # 如果成功，不返回错误信息
    else:
        return False,re.text # 如果失败，返回错误信息