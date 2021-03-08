#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/8

import sqlite3
from collections import namedtuple

android_build_record = namedtuple('Package', 'id package package_name package_version_code '
                                             'product_flavor_name package_version_name package_target_sdk '
                                             'package_mini_sdk package_mapping_url deeplink_scheme date '
                                             'git_sha_code git_branch_name module_name library')

android_library_record = namedtuple('PackageLibrary', 'library_group library_name library_version')


def get_android_build_record():
    conn = sqlite3.connect('flaskr.sqlite')
    cur = conn.cursor()
    cur.execute('select * from Package')
    for i in cur.fetchall():
        yield i
        
    cur.close()
    conn.close()


def get_android_library_detail(record):
    conn = sqlite3.connect('flaskr.sqlite')
    cur = conn.cursor()
    cur.execute('select libraryGroup, libraryName, libraryVersion from PackageLibrary where package=? and'
                ' packageName=? and productFlavorName=? and packageVersionName=?',
                (record.package, record.package_name, record.product_flavor_name, record.package_version_name))

    for i in cur.fetchall():
        yield i

    cur.close()
    conn.close()


def android_build_library_merger():
    build_gen = get_android_build_record()
    for record in build_gen:
        record = android_build_record(*record, [])
        library_gen = get_android_library_detail(record)
        for library in library_gen:
            library = android_library_record(*library)
            record.library.append(library)
        yield record


if __name__ == '__main__':
    record_gen = android_build_library_merger()




