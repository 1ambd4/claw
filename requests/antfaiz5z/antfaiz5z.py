import requests
import re

img_urls = [
'http://ww1.sinaimg.cn/large/0065oQSqly1ft3fna1ef9j30s210skgd.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fszxi9lmmzj30f00jdadv.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fsysqszneoj30hi0pvqb7.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fswhaqvnobj30sg14hka0.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fsvb1xduvaj30u013175p.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fsq9iq8ttrj30k80q9wi4.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fsp4iok6o4j30j60optbl.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fsoe3k2gkkj30g50niwla.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fsmis4zbe7j30sg16fq9o.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frslruxdr1j30j60ok79c.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fsfq1k9cb5j30sg0y7q61.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fsfq1ykabxj30k00pracv.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fsfq2pwt72j30qo0yg78u.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fsb0lh7vl0j30go0ligni.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fs8tym1e8ej30j60ouwhz.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fs8u1joq6fj30j60orwin.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fs7l8ijitfj30jg0shdkc.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fs35026dloj30j60ov79x.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fs34w0jx9jj30j60ootcn.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fs1vq7vlsoj30k80q2ae5.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frv032vod8j30k80q6gsz.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fs02a9b0nvj30sg10vk4z.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fryyn63fm1j30sg0yagt2.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frv03m8ky5j30iz0rltfp.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frsllc19gfj30k80tfah5.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frslibvijrj30k80q678q.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frrifts8l5j30j60ojq6u.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frqscr5o00j30k80qzafc.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frmuto5qlzj30ia0notd8.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frjd77dt8zj30k80q2aga.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frjd4var2bj30k80q0dlf.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frja502w5xj30k80od410.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1fri9zqwzkoj30ql0w3jy0.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frg40vozfnj30ku0qwq7s.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frevscw2wej30je0ps78h.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frepozc5taj30qp0yg7aq.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frepq6mfvdj30p00wcwmq.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frepqtwifwj30no0ti47n.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1frepr2rhxvj30qo0yjth8.jpg',
'http://ww1.sinaimg.cn/large/0065oQSqly1freprc128lj30sg15m12u.jpg',
]

for i_url in img_urls:
    img_name = re.match(r'(.*)(large/)(.*)',i_url)
    r = requests.get(i_url)
    with open(img_name.group(3), 'wb') as f:
        f.write(r.content)
        print("downloading ", i_url)
    f.close()
print("finished.")
