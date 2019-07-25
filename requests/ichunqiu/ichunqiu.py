# -*- coding: utf-8 -*-
#!/usr/bin/python

import requests
import json

def claw(url, data, headers):
        html = requests.post(url = url, data = params, headers = header)

        data = json.loads(html.text)
        length = len(data['course']['result'])
        for i in range(length):
                print(str(data['course']['result'][i]['courseName']) + " " + str(data['course']['result'][i]['presentPrice']) + " " + str(data['course']['result'][i]['buyNumView']))


url = "https://www.ichunqiu.com/courses/ajaxCourses"

header = {
        'Host' : 'www.ichunqiu.com',
        'Connection' : 'close',
        'Content-Length' : '103',
        'Accept' : 'application/json, text/javascript, */*; q=0.01',
        'Origin' : 'https://www.ichunqiu.com',
        'X-Requested-With' : 'XMLHttpRequest',
        'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer' : 'https://www.ichunqiu.com/courses/open-no',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept-Language' : 'en,zh-CN;q=0.9,zh;q=0.8',
        'Cookie' : '__jsluid_s=024058e01a09c97231e431dfdd1b6956; chkphone=acWxNpxhQpDiAchhNuSnEqyiQuDIO0O0O; UM_distinctid=16c136ab7d55fa-0bce4de37514ec-3f75065b-1fa400-16c136ab7d6644; CNZZDATA1262179648=782705684-1563689154-https%253A%252F%252Fwww.ichunqiu.com%252F%7C1563689154; browse=CFlaQlQKAE9YU11EVQJTRFBZSkdeQFBYWVRFR1xRWEFTVl1PXEFLTgBZXUVdQVhOGllZTFRTW0VYWkVFWVxbQElSXU9eR1NEWUFTHFREWUdQUlMGVEBQT0tRWERXXFlCRFFaVV9HU0RQWVxHTEoAT1xTWkJXShpPWFpSV1xBWExEU19YXEJJRV9ZW0NUQlpXUgpSQF9FWUBSEFJEV0tLR1lSUVheRkRHXUNaRFRAXk9YU0pOB0tcRF5QUU4dS1hMU0FaRV9IREVeTlpBTkNbT1pTUkRXU1IcU1ZYQV5IUgZTUlFPTENZRFBOWEJDQ1xVWFJSRlpLWExLWAFPW0VdQlpYG09fSFNXW1NZTENBXlhbUEhFWUtbQVNSXldVGFNAWldbQlUCU0RQWUpHXkBQWFlURUddUVlCU1FRT1tFS04AWV1GX0dQThpZWUxUU1tFWFpFRVlcW0ZJU19PW0hTRllBUxxURFpFWVpTBlRAUE9LUVhEV1xZQkRRW1VeSVNFWllZRUxKAE9fUFpEXEoaT1haUldcQVhMRFNfWFxCSUVRWVhDVEBaV1IKUkBeSVlEUhBSRFdLS0dZUlFYXkZER1pDWE1UQVFPXVtKTgdLXEVRUVtOHUtYTFNBWkVfSERFXk5aRk5BUU9YU1JBX1NSHFNWWEZcQFIGU1JRT0xDWURQTlhCQ0NaVVlbUkRcS1xFS1gBT1tAWEBeWBtPX0hTV1tTWUxDQV5YW1BIRVZLW0dTUl5XVRhTTFBQUwZUQFBPS1FYRFdcWUJEUVtVX0NTRVxZWUdMSgBPWFFbTh1LWExTQVpFX0hERV5OWkZOQFtPWVRSQFxTUhxTVVtNXkRSBlNSUU9MQ1lEUE5YQkNDWlVYUVJFV0taQUtYAU9YQFxCXlgbT19IU1dbU1lMQ0FeWFtQSERcS1hEU1FcV1UYU0RdV1MGVEBQT0tRWERXXFlCRFFbVV9DU0FZWVhGTEoAT1xTW0FfShpPWFpSV1xBWExEU19YXEJJRFpZXUJUQVtXUgpSQlZKGk9YWlJXXEFYTERTX1hcQklEXVlYRVRAXVdSClJAWkNYRFIQUkRXS0tHWVJRWF5GREdaQ1lDVEFeT11SSk4HS1xFWlVbTh1LWExTQVpFX0hERV5OWkZOQF9PXFNSRl9TUhxTVl5AXkRSBlNSUU9MQ1lEUE5YQkNDXVVbUVJHVktdTUtYAU9dQ11OGllZTFRTW0VYWkVFWVxbQUlRWk9dQFNAXEFTCA; Hm_lvt_2d0601bd28de7d49818249cf35d95943=1563887782,1563887798,1563951972,1564025567; ci_session=d7bf4bc30747f6b86570ab17053a4f612c4b08e2; Hm_lpvt_2d0601bd28de7d49818249cf35d95943=1564026333'
        }

for i in range(8):
        params = 'courseTag=&courseDiffcuty=&IsExp=&producerId=&orderField=&orderDirection=&pageIndex=' + str(i) + '&tagType=&isOpen=1'
        claw(url = url, data = params, headers = header)