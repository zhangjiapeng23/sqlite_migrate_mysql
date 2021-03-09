#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/9
import json
import re

from sqlite_read_ios import ios_build_framework_merger
from write2mysql import MysqlWrite


def filter_data_ios():
    gen_record = ios_build_framework_merger()
    for record in gen_record:
        record_dict = {}
        record_dict['project_version'] = record.project_version
        record_dict['project_id'] = record.project_name
        record_dict['date'] = record.date

        for framework in record.framework:
            if re.match(r'\d+\.\d+\.0\d+', framework.framework_version)\
                    or 'x' in str(framework.framework_version):
                record_dict['x_framework'] = True
                break
        else:
            record_dict['x_framework'] = False
        # serialize record list
        framework_list = list()
        for framework in record.framework:
            framework_dict = dict()
            framework_dict['frameworkName'] = framework.framework_name
            framework_dict['frameworkVersion'] = framework.framework_version
            framework_list.append(framework_dict)
        framework_json = json.dumps(framework_list)
        record_dict['framework'] = framework_json
        yield record_dict


if __name__ == '__main__':
    print('database migrate start!')
    mysql = MysqlWrite('web_platform')

    gen_record_dict = filter_data_ios()
    for record_dict in gen_record_dict:
        project_name = record_dict['project_id']
        mysql.insert_project_ios(project_name)
        mysql.insert_build_record_ios(build_record=record_dict)

    mysql.cursor_close()
    mysql.conn_close()
    print('database migrate completed!')
