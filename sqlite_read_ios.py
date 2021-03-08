#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/8

import sqlite3
from collections import namedtuple

ios_build_record = namedtuple('iOSProject', 'id project_name project_version date framework')
ios_framework_record = namedtuple('Framework', 'framework_name framework_version')

def get_ios_build_record():
    conn = sqlite3.connect('flaskr.sqlite')
    cur = conn.cursor()
    cur.execute('select * from iOSProject')

    for record in cur.fetchall():
        yield record

    cur.close()
    conn.close()


def get_ios_framework_detail(record: ios_build_record):
    conn = sqlite3.connect('flaskr.sqlite')
    cur = conn.cursor()
    cur.execute('select frameworkName, frameworkVersion from Framework where projectName=? and '
                'projectVersion=?', (record.project_name, record.project_version))

    for framework in cur.fetchall():
        yield framework

    cur.close()
    conn.close()


def ios_build_framework_merger():
    build_gen = get_ios_build_record()
    for record in build_gen:
        record = ios_build_record(*record, [])
        framework_gen = get_ios_framework_detail(record)
        for framework in framework_gen:
            record.framework.append(framework)
        yield record


if __name__ == '__main__':
    ios_build_framework_merger()