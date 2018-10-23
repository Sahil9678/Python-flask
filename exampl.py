import requests  # supports a fully restful API

r = requests.get('http://127.0.0.1:5000/read')
print 'Status Code:', r.status_code  # 200
print r.json()

print 'All Headers:', r.headers
# {'X-XSS-Protection': '1; mode=block', 'Content-Security-Policy': ...

print 'Content-type in Header:', r.headers['content-type']
# application/json; charset=utf-8

print 'Binary Response:', r.content
# [{"id":"7588981508","type":"PushEvent" ...

print 'Encoding:', r.encoding  # utf-8
print 'Response:', r.text