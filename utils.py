# coding:utf-8
import datetime
import redis as redis

redis_host = ""
r = redis.StrictRedis(host=redis_host, port=6379)


# 获取上个月时间函数
def get_before_month_time(month_time):
    target_month = month_time.month - 1
    if target_month <= 0:
        month_time = datetime.date(year=month_time.year - 1, month=12, day=1)
    else:
        month_time = datetime.date(year=month_time.year, month=target_month, day=1)
    return month_time


# 数组连接成字符串
def contain_array(l, tp):
    if tp == "sql":
        return '"' + '","'.join(str(s) for s in l) + '"'
    else:
        return ",".join(str(s) for s in l)


def del_tag_redis(tag_id):
    return r.hdel("zcg_market_commodityservice:getCommodityIdsByPageNumber:" + tag_id)


def del_set_key_value(key, value):
    return r.hdel(key, value)


list_a = [1, 2, 3, 4, 5]
# print contain_array(list_a, "sql")
d = r.hget("zcg_market_commodityservice:getCommodityIdsByPageNumber:TG160708161254759",
           "0_[2, 3, 5]_2")
num = r.hdel("zcg_market_commodityservice:getCommodityIdsByPageNumber:TG160708161254759",
             "28_[0, 1, 2, 3, 5, 6]_2")
