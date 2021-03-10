#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/9
import json

from sqlite_read_android import android_build_library_merger
from write2mysql import MysqlWrite


def filter_data():
    gen_record = android_build_library_merger()
    for record in gen_record:
        record_dict = {}
        # package: com.nbaimd.gametiem.nba2011
        # package_name: nba
        record_dict['package_name'] = record.package
        record_dict['package_version_name'] = record.package_version_name
        record_dict['module_name'] = record.module_name if record.module_name else 'app'
        record_dict['product_flavor_name'] = record.product_flavor_name
        record_dict['package_target_sdk'] = record.package_target_sdk
        record_dict['package_mini_sdk'] = record.package_mini_sdk
        package_mapping_url = '/media/android_mapping/'
        if record.module_name:
            package_mapping_url = package_mapping_url + record.module_name + \
                                  '_' + record.package + '_' + record.package_version_name +\
                                  '_mapping.text'
        else:
            package_mapping_url = package_mapping_url + record.package + '_' +\
                                  record.package_version_name + '_mapping.text'
        record_dict['package_mapping_url'] = package_mapping_url
        record_dict['deeplink_scheme'] = record.deeplink_scheme
        record_dict['git_sha_code'] = record.git_sha_code
        record_dict['git_branch_name']= record.git_branch_name
        record_dict['date'] = record.date
        for library in record.library:
            if '-SNAPSHOT' in library.library_version:
                record_dict['snapshot'] = True
                break
        else:
            record_dict['snapshot'] = False
        # serialize record list
        library_list = list()
        for library in record.library:
            library_dict = dict()
            library_dict['group'] = library.library_group
            library_dict['name'] = library.library_name
            library_dict['currentVersion'] = library.library_version
            library_list.append(library_dict)
        library_json = json.dumps(library_list)
        record_dict['library_coordinate_list'] = library_json
        record_dict['project_id'] = record.package_name
        record_dict['package_version_code'] = record.package_version_code
        yield record_dict


if __name__ == '__main__':
    print('database migrate start!')
    mysql = MysqlWrite('web_platform')

    gen_record_dict = filter_data()
    for record_dict in gen_record_dict:
        project_name = record_dict['project_id']
        mysql.insert_project_android(project_name)
        mysql.insert_build_record_android(build_record=record_dict)

    mysql.cursor_close()
    mysql.conn_close()
    print('database migrate completed!')
