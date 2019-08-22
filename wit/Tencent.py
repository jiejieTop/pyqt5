
import re
import json
import time
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.iotexplorer.v20190423 import iotexplorer_client, models 

# 服务器类
class WISG(object):
    def __init__(self):
        self.data = {
            'pn':'null',
            'pg':'null',
            'dn':'null', 
            'bn':0,
            'time':0,
            'lv':0,
            'speed':0,
            'led':0,
            'beep':0,
            'sm':0,
            'call':0
        }
    pass

    def data_decoding(self,json_data):
        self.data['pn'] = json_data['pn']['Value']
        self.data['pg'] = json_data['pg']['Value']
        self.data['bn'] = json_data['bn']['Value']
        self.data['time'] = json_data['time']['Value']
        self.data['lv'] = json_data['lv']['Value']
        self.data['speed'] = json_data['speed']['Value']
        self.data['led'] = json_data['led']['Value']
        self.data['beep'] = json_data['beep']['Value']
        self.data['sm'] = json_data['sm']['Value']
        self.data['call'] = json_data['call']['Value']
        self.data['dn'] = json_data['dn']['Value']  
        print(self.data)
        return self.data
        pass


    def extract_data(self):
        resp = self.get_recv_data()
        recv_data_str = str(resp)
        exception_str = "Exception"     #判断是否有异常
        exception = recv_data_str.find(exception_str)
        # print("exception = %d"%exception)
        if(exception > 0):  #出现异常
            print("Exception")
            return
        # 没有异常
        # print("--------------")
        # print(type(resp))
        # print(resp)
        # print("--------------")
        
        recv_data = resp['Data']
        js = json.loads(recv_data)
        
        return self.data_decoding(js)

        pass


    def get_recv_data(self):
        try: 
            cred = credential.Credential("AKID17yf8NhCh3FDwRmrjPr7CPM7g0VmEa6k", "oSxMWR8amjSvZJsDLGxUlncBW1FGLIdl") 
            httpProfile = HttpProfile()
            httpProfile.endpoint = "iotexplorer.tencentcloudapi.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = iotexplorer_client.IotexplorerClient(cred, "ap-guangzhou", clientProfile) 

            req = models.DescribeDeviceDataRequest()
            params = '{"ProductId":"V1868Z8B3A","DeviceName":"wit120"}'
            req.from_json_string(params)

            resp = client.DescribeDeviceData(req)
            # print(resp.to_json_string()) 
            # recv_data_str = str(resp)
            js = json.loads(resp.to_json_string())
            # js = json.dumps(resp)
            # print(js)

            return js
            

        except TencentCloudSDKException as err: 
            print(err) 
        pass


def main():
    start = WISG()
    while True:
        start.extract_data()
        time.sleep(6)



if __name__ == "__main__":
    main()
