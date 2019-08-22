from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException 
from tencentcloud.iotexplorer.v20190423 import iotexplorer_client, models 


# 服务器类
class TencentSend(object):
  def __init__(self):
        self.data = {
            'pn':'null',
            'pg':'null',
            'bn':0,
            'time':0,
            'lv':0,
            'speed':0,
            'led':0,
            'beep':0,
            'sm':0,
            'call':0, 
            'dn':'null'
        }
  pass
  
  def send_data(self, data):
    try: 
      cred = credential.Credential("AKID17yf8NhCh3FDwRmrjPr7CPM7g0VmEa6k", "oSxMWR8amjSvZJsDLGxUlncBW1FGLIdl") 
      httpProfile = HttpProfile()
      httpProfile.endpoint = "iotexplorer.tencentcloudapi.com"

      clientProfile = ClientProfile()
      clientProfile.httpProfile = httpProfile
      client = iotexplorer_client.IotexplorerClient(cred, "ap-guangzhou", clientProfile) 

      req = models.ControlDeviceDataRequest()
      self.data = data
      
      params = '{"ProductId":"V1868Z8B3A","DeviceName":"wit120","Data":"{\\"bn\\":%d,\\"speed\\":%d,\\"led\\":%d,\\"beep\\":%d}"}'\
      %(self.data['bn'], self.data['speed'], self.data['led'], self.data['beep'])
      req.from_json_string(params)

      resp = client.ControlDeviceData(req) 
      print(resp.to_json_string()) 

    except TencentCloudSDKException as err: 
      print(err) 



def main():
    data1 = {
        'pn':'null',
        'pg':'null',
        'bn':66,
        'time':0,
        'lv':0,
        'speed':36,
        'led':1,
        'beep':0,
        'sm':0,
        'call':0, 
        'dn':'null'
    }
    start = TencentSend()
    start.send_data(data1)

if __name__ == "__main__":
    main()
