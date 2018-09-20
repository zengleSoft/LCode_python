#!/usr/bin/python
# -*- coding: UTF-8 -*-

# from cassandra.cluster import *
from optparse import OptionParser
# from cassandra.auth import PlainTextAuthProvider
import os
import sys
import datetime;
import hashlib


cur_date = datetime.datetime.now()


def parse_args():
    # os.system("echo  'parse_args() begin!' >> /data/extract_data_apps/logs/daily.log")
    parser = OptionParser()
    parser.add_option("-d", "--date", default=cur_date.strftime('%Y-%m-%d'), dest="date", type="string",
                      help="the date to be read", metavar="DATE")
    for option in parser.option_list:
        if option.default != ("NO", "DEFAULT"):
            option.help += (" " if option.help else "") + " [default: %default]"
    (options, args) = parser.parse_args()
    # os.system("echo   options.date >> /data/extract_data_apps/logs/daily.log")
    # fd = open("/data/extract_data_apps/logs/daily.log", "a")
    # fd.write(options.date)
    # fd.write('\n')
    # os.system("echo   'parse_args() finish!' >> /data/extract_data_apps/logs/daily.log")
    return options


# def extract_low(date):
#     os.system('rm -rf /data/daily_datacp/*')
#     os.system("echo 'extract_low begin!' >> /data/extract_data_apps/logs/daily.log")
#     a = datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=-1)
#     yesterday_str = a.strftime('%Y-%m-%d')
#     file_object = open('/data/daily_datacp/all' + yesterday_str + '.csv', 'w')
#     provider = PlainTextAuthProvider(username='zzc', password='pass@david123')
#     cluster = Cluster(['10.45.237.14'], auth_provider=provider)
#     session = cluster.connect('antifraud_robin')
#     session.default_consistency_level = 5
#     rows = session.execute("SELECT * FROM by_day where day='" + yesterday_str.replace('-', '') + "'")
#
#     for user_row in rows:
#         line = ''.join(
#             [str(user_row.day), '|', str(user_row.tid), '|', str(user_row.ztype), '|', str(user_row.zid), '|',
#              str(user_row.disabled), '|', str(user_row.out), '|',
#              (user_row.time + datetime.timedelta(hours=8)).strftime("%Y-%m-%dT%H:%M:%S.%f+0800"), '|',
#              str(user_row.val), '|', str(user_row.usr)])
#         file_object.write(line + '\n')
#
#     file_object.close()
#     # os.system("echo  'extract_low finish!' >> /data/extract_data_apps/logs/daily.log")


# def transfer(date):
#     try:
#         localdir = '/data/daily_datacp'
#
#         os.system("echo  'Tar:' >> /data/extract_data_apps/logs/daily.log")
#         os.system("echo  '=========================' >> /data/extract_data_apps/logs/daily.log")
#         a = datetime.datetime.strptime(date, '%Y-%m-%d') + datetime.timedelta(days=-1)
#         yesterday_str = a.strftime('%Y-%m-%d')
#         localfile = os.path.join(localdir, 'all' + yesterday_str + '.csv')
#         localgz = os.path.join(localdir, yesterday_str.replace('-', '') + '.tgz')
#         localmd5 = os.path.join(localdir, yesterday_str.replace('-', '') + '.md5')
#         os.system('tar -czvf ' + localgz + " " + localfile)
#         md5 = hashlib.md5(open(localgz, 'rb').read()).hexdigest()
#         with open(localmd5, 'w') as fw:
#             fw.write(md5)
#             fw.close()
#
#         os.system("echo  'Transfer:' >> /data/extract_data_apps/logs/daily.log")
#         os.system("echo  '=========================' >> /data/extract_data_apps/logs/daily.log")
#         port = 33773
#         sta = ["124.251.69.116"]
#         USERNAME = "hadoop_ftp"
#         PASSWORD = "S0neQ9bctx2dAsBb"
#
#         # localdir="/data/extract_data_apps/lbwtext20161118.txt"
#         remotedir = "/home/hadoop_ftp/all"
#         for l in sta:
#             t = paramiko.Transport((l, port))
#             t.connect(username=USERNAME, password=PASSWORD)
#             sftp = paramiko.SFTPClient.from_transport(t)
#             sftp.put(localgz, os.path.join(remotedir, yesterday_str.replace('-', '') + '.tgz'))
#             sftp.put(localmd5, os.path.join(remotedir, yesterday_str.replace('-', '') + '.md5'))
#             t.close()
#         os.system("echo  'Transfer finish' >> /data/extract_data_apps/logs/daily.log")
#         return
#     except:
#         os.system(
#             "echo  'python /data/extract_data_apps/daily/daily-extrace-low-app.py --date '" + option.date + " >> /data/extract_data_apps/logs/getall.log")
#         transfer(date)


if __name__ == '__main__':
    option = parse_args()
    # extract_low(option.date)
    # transfer(option.date)
