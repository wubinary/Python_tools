#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import psutil,time
except ImportError:
    print('Error: psutil module not found!')
    exit()


def get_key():

    key_info = psutil.net_io_counters(pernic=True).keys()

    recv = {}
    sent = {}

    for key in key_info:
        recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)
        sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)

    return key_info, recv, sent


def get_rate(func):

    import time

    key_info, old_recv, old_sent = func()

    time.sleep(1)

    key_info, now_recv, now_sent = func()

    net_in = {}
    net_out = {}

    for key in key_info:
        # float('%.2f' % a)
        net_in.setdefault(key, float('%.2f' %((now_recv.get(key) - old_recv.get(key)) / 1024)))
        net_out.setdefault(key, float('%.2f' %((now_sent.get(key) - old_sent.get(key)) / 1024)))

    return key_info, net_in, net_out


while 1:
    try:
         key_info, net_in, net_out = get_rate(get_key)

         for key in key_info:
             # lo 是linux的本机回环网卡，以太网是我win10系统的网卡名
             if key != 'lo' or key == '以太网':
                print('%s\nInput:\t %-5sKB/s\nOutput:\t %-5sKB/s\n' % (key, net_in.get(key), net_out.get(key)))
    except KeyboardInterrupt:
        exit()
