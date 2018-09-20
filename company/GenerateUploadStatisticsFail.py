#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb


class UploadStatisticsFail(object):
    # 私有属性__
    __tenant_id = 0
    __name = ''
    __stat_month = ''
    __upload_count = 0
    __success_count = 0
    __fail_count = 0
    __fail_reason_alreadyExists = 0
    __fail_reason_pid = 0
    __fail_reason_mobile = 0
    __fail_reason_workPhone = 0
    __fail_reason_homePhone = 0
    __fail_reason_name = 0
    fail_reason_others = 0

    def __init__(self, tenant_id, name, stat_month, upload_count, success_count, fail_count, fail_reason_alreadyExists,
                 fail_reason_pid, fail_reason_mobile, fail_reason_workPhone, fail_reason_homePhone, fail_reason_name,
                 fail_reason_others):
        self.tenant_id = tenant_id
        self.name = name
        self.stat_month = stat_month
        self.upload_count = upload_count
        self.success_count = success_count
        self.fail_count = fail_count
        self.fail_reason_alreadyExists = fail_reason_alreadyExists
        self.fail_reason_pid = fail_reason_pid
        self.fail_reason_mobile = fail_reason_mobile
        self.fail_reason_workPhone = fail_reason_workPhone
        self.fail_reason_homePhone = fail_reason_homePhone
        self.fail_reason_name = fail_reason_name
        self.fail_reason_others = fail_reason_others


def generateSql():
    sql = 'select tenant_id,DATE_FORMAT(upload_time,\'%Y-%m\') months,fail_reason,upload_status,count(1) cnt from upload_record ' \
          'where 1=1 and upload_time is not null group by tenant_id,upload_status,months,fail_reason'
    conn = MySQLdb.connect(host='192.168.111.23', user='root', passwd='12345678', db='mydb')
    cur = conn.cursor(MySQLdb.cursors.DictCursor)
    cur.execute(sql)
    rows = cur.fetchall()
    resultList = []
    tmpDict = {}
    for row in rows:
        tenant_id = row['tenant_id']
        cnt = row['cnt']
        months = row['months']
        # name = row['name']
        fail_reason = row['fail_reason']
        upload_status = row['upload_status']

        if (tmpDict.__contains__(str(tenant_id) + '_' + str(months))):
            usf = tmpDict.get(str(tenant_id) + '_' + str(months))
        else:
            usf = UploadStatisticsFail(tenant_id, 'name', months, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
            tmpDict[str(tenant_id) + '_' + str(months)] = usf
            resultList.append(usf)
        if upload_status == 1:
            usf.success_count = cnt
            usf.upload_count = usf.upload_count + cnt
        else:
            usf.fail_count = usf.fail_count+cnt
            usf.upload_count = usf.upload_count + cnt
            if 'name' in fail_reason:
                usf.fail_reason_name = usf.fail_reason_name+cnt
            elif 'pid' in fail_reason:
                usf.fail_reason_pid = usf.fail_reason_pid+cnt
            elif 'already exists' in fail_reason:
                usf.fail_reason_alreadyExists = usf.fail_reason_alreadyExists+cnt
            elif 'mobile' in fail_reason:
                usf.fail_reason_mobile = usf.fail_reason_mobile+cnt
            elif 'work_phone' in fail_reason:
                usf.fail_reason_workPhone = usf.fail_reason_workPhone+cnt
            elif 'home_phone' in fail_reason:
                usf.fail_reason_homePhone = usf.fail_reason_homePhone+cnt
            else:
                usf.fail_reason_others = usf.fail_reason_others+cnt
    # cur.close()
    # conn.close()
    sqls='insert into upload_statistics_fail (tenant_id,name,stat_month,upload_count,success_count,fail_count,fail_reason_alreadyExists,' \
        'fail_reason_pid,fail_reason_mobile,fail_reason_workPhone,fail_reason_homePhone,fail_reason_name,fail_reason_others) values'
    for usf in resultList:
        sql='(%d,\'%s\',\'%s\',%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)'%(usf.tenant_id,usf.name,usf.stat_month,usf.upload_count,usf.success_count,
                                                      usf.fail_count,usf.fail_reason_alreadyExists,usf.fail_reason_pid,usf.fail_reason_mobile,
                                                      usf.fail_reason_workPhone,usf.fail_reason_homePhone,usf.fail_reason_name,usf.fail_reason_others)
        sqls=sqls+sql+','
    cur.execute(sqls[0:-1])
    conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    generateSql()
