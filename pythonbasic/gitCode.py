import requests
# zhangting teach_001branch

class BaseApi:
    def __init__(self,base_url):
    	self.url=base_url
    	self.request=requests.session()

    def get(self,url,**kwargs):
    	return self.request.get(url,**kwargs)

    def post(self,url,data=None,json=None,**kwargs):
    	url=self.url+url
    	return self.request.post(url,data,json,**kwargs)

    def delete(self,url,**kwargs):
    	url=self.url+url
    	return self.request.delete(url,**kwargs)

aa=BaseApi('http://192.168.0.103:83')
rr=aa.get('http://192.168.0.103:83/get')
print(rr.request.url)
print(rr.status_code)
print(rr.content)
print('=========')


r2=aa.post('/post',json={"1":"2"})
print(r2.request.url)
print(r2.status_code)
print(r2.content)
print('=========')


r3=aa.delete('/delete')
print(r3.request.url)
print(r3.status_code)
print(r3.content)
print('~~~~~~~~~~~~~~~~=========')
print(r3.headers['Server'])
print('=========')



