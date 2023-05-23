#initialize data
train_time_range = ('2014-06-01','2020-12-31')
test_time_range = ('2021-01-01','2023-04-30')
ConsumerDiscretionary = {'sh.600519':'贵州茅台','sz.000858':'五粮液','sh.601888':'中国中免'}
Tech = {'sz.002594':'比亚迪','sz.002230':'科大讯飞','sz.000725':'京东方A'}
Fina = {'sh.601398':"工商银行",'sh.601939':'建设银行','sh.601628':"中国人寿"}
Health = {'sh.600276':'恒瑞医药','sz.300015':'爱尔眼科','sh.600436':'片仔癀'}
Ind = {'sh.601899':'紫金矿业','sh.600309':'万华化学','sh.601012':'隆基绿能'}
ConStaple = {'sh.600887':'伊利股份','sz.002714':'牧原股份','sz.000895':'双汇发展'}
Energy = {'sh.601857':"中国石油",'sh.600028':'中国石化','sh.601088':'中国神华'}
RE = {'sh.601668':'中国建筑','sh.601390':'中国中铁','sz.000002':'万科A'}
comm = {'sz.002352':'顺丰控股','sh.601766':'中国中车','sh.600029':'南方航空'}
Utility = {'sh.600941':"中国移动",'sh.601728':'中国电信','sh.600900':'长江电力'}

stock_d = dict()

# put all stocks into dictionary as {sz.002594 : 比亚迪}
for d in (Tech,Fina,Health,Ind,ConStaple,Energy,RE,comm,Utility,ConsumerDiscretionary):
    for key, value in d.items():
        stock_d[key] = value