from django.http import HttpResponse

def index(request):
    line1 = '<h1 style="text-align:center">英雄联盟</h1>'
    line4 = '<hr>'
    line2 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fn.sinaimg.cn%2Fsinakd202163s%2F218%2Fw640h378%2F20210603%2F538e-kracxep9541309.jpg&refer=http%3A%2F%2Fn.sinaimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1672561977&t=27dea2e1d2665382aaf70c50e3bde99b" width=1000>'
    line3 = '<a href="/game/play">进入游戏界面</a>'
    return HttpResponse(line1 + line4 + line2 + line4 + line3)

def play(request):
    line1 = '<h1 style="text-align:center">游戏界面</h1>'
    line2 = '<a href="/game/">返回主界面</a>'
    line3 = '<img src="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fdingyue.ws.126.net%2F2020%2F0321%2F062401b6j00q7jm6u0018c000tq00ggm.jpg&refer=http%3A%2F%2Fdingyue.ws.126.net&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1672561963&t=e884d7b3db3dbce63f0a160dc13171f4" width=1500>'
    line4 = '<hr>'
    return HttpResponse(line1 + line3 + line4 + line2)
