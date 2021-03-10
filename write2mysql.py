#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# @author: James Zhang
# @data  : 2021/3/9
import re

import pymysql

class MysqlWrite:

    def __init__(self, database_name):
        self._database_name = database_name
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='NeuMobile123$',
                                    db=self._database_name)
        self.cursor = self.conn.cursor()

    def __str__(self):
        return 'DB:{}'.format(self._database_name)

    def insert_project_ios(self, project_name):
        sql_cmd_r = 'select * from project_info_iosproject where project_name=%s'
        sql_cmd_c = 'insert into project_info_iosproject (project_name, project_logo) value ' \
                    '(%s, %s)'
        # check project is whether exits
        self.cursor.execute(sql_cmd_r, project_name)
        if not self.cursor.fetchone():
            project_logo = 'imgs/project_info/{}.png'
            if re.match(r'.*Sky Sport Now.*', project_name):
                project_logo = project_logo.format('SkySportNow')
            elif re.match(r'.*Euroleague.*', project_name):
                project_logo = project_logo.format('EuroLeague')
            elif re.match(r'.*insight.*', project_name):
                project_logo = project_logo.format('insight')
            elif re.match(r'.*btn.*', project_name, re.IGNORECASE):
                project_logo = project_logo.format('BTN2GO')
            elif re.match(r'.*Sky Box Office.*', project_name):
                project_logo = project_logo.format('SkyBoxOffice')
            elif re.match(r'.*espn.*', project_name, re.IGNORECASE):
                project_logo = project_logo.format('ESPN')
            elif re.match(r'.*feitv.*', project_name):
                project_logo = project_logo.format('FEITV')
            elif re.match(r'.*ufc.*', project_name, re.IGNORECASE):
                project_logo = project_logo.format('UFC')
            elif re.match(r'.*Game Pass.*', project_name):
                project_logo = project_logo.format('GamePass')
            elif re.match(r'.*rugbypass.*', project_name, re.IGNORECASE):
                project_logo = project_logo.format('rugbypass')
            elif re.match(r'.*wnba.*', project_name, re.IGNORECASE):
                project_logo = project_logo.format('wnba')
            elif re.match(r'.*Fan Pass.*', project_name):
                project_logo = project_logo.format('FanPass')
            elif re.match(r'.*GamePass.*', project_name):
                project_logo = project_logo.format('NFLGamePass')
            elif re.match(r'.*PokerGO.*', project_name):
                project_logo = project_logo.format('PokerGO')
            elif re.match(r'.*CRTV.*', project_name):
                project_logo = project_logo.format('CRTV')
            elif re.match(r'.*nba.*', project_name, re.IGNORECASE):
                project_logo = project_logo.format('nba')
            elif re.match(r'.*ufc-tv.*', project_name):
                project_logo = project_logo.format('ufc-tv')
            elif re.match(r'.*SKY_TV.*', project_name):
                project_logo = project_logo.format('SkySportNow')
            elif re.match(r'.*lidom.*', project_name, re.IGNORECASE):
                project_logo = project_logo.format('Lidom')
            elif re.match(r'.*cntv.*', project_name, re.IGNORECASE):
                project_logo = project_logo.format('CNTV')
            elif re.match(r'.*speedway.*', project_name, re.IGNORECASE):
                project_logo = project_logo.format('Speedwa')
            elif re.match(r'.*tigohn.*', project_name, re.IGNORECASE):
                project_logo = project_logo.format('TIGOHN')
            else:
                project_logo = project_logo.format('Neulion')
            self.cursor.execute(sql_cmd_c, (project_name, project_logo))
        self.commit()
        return project_name

    def insert_project_android(self, project_name):
        sql_cmd_r = 'select * from project_info_androidproject where project_name=%s'
        sql_cmd_c = 'insert into project_info_androidproject (project_name, project_logo) value ' \
                    '(%s, %s)'
        # check project is whether exits
        self.cursor.execute(sql_cmd_r, project_name)
        if not self.cursor.fetchone():
            project_logo = 'imgs/project_info/{}.png'
            if re.match(r'.*Sky Sport Now.*', project_name):
                project_logo = project_logo.format('SkySportNow')
            elif re.match(r'.*Euroleague.*', project_name):
                project_logo = project_logo.format('EuroLeague')
            elif re.match(r'.*insight.*', project_name):
                project_logo = project_logo.format('insight')
            elif re.match(r'.*btn2go.*', project_name):
                project_logo = project_logo.format('BTN2GO')
            elif re.match(r'.*Sky Box Office.*', project_name):
                project_logo = project_logo.format('SkyBoxOffice')
            elif re.match(r'.*espn.*', project_name):
                project_logo = project_logo.format('ESPN')
            elif re.match(r'.*feitv.*', project_name):
                project_logo = project_logo.format('FEITV')
            elif re.match(r'.*ufc.*', project_name):
                project_logo = project_logo.format('UFC')
            elif re.match(r'.*Game Pass.*', project_name):
                project_logo = project_logo.format('GamePass')
            elif re.match(r'.*rugbypass.*', project_name):
                project_logo = project_logo.format('rugbypass')
            elif re.match(r'.*wnba.*', project_name):
                project_logo = project_logo.format('wnba')
            elif re.match(r'.*Fan Pass.*', project_name):
                project_logo = project_logo.format('FanPass')
            elif re.match(r'.*GamePass.*', project_name):
                project_logo = project_logo.format('NFLGamePass')
            elif re.match(r'.*PokerGO.*', project_name):
                project_logo = project_logo.format('PokerGO')
            elif re.match(r'.*CRTV.*', project_name):
                project_logo = project_logo.format('CRTV')
            elif re.match(r'.*nba.*', project_name):
                project_logo = project_logo.format('nba')
            elif re.match(r'.*ufc-tv.*', project_name):
                project_logo = project_logo.format('ufc-tv')
            else:
                project_logo = project_logo.format('Neulion')
            self.cursor.execute(sql_cmd_c, (project_name, project_logo ))

        self.commit()
        return project_name

    def insert_build_record_ios(self, build_record):
        sql_cmd_r = 'select nid from project_info_iosbuild where project_id=%s and project_version=%s'
        sql_cmd_c = 'insert into project_info_iosbuild (project_version, date, x_framework, framework, project_id) value' \
                    ' (%s, %s, %s, %s, %s)'
        sql_cmd_u = 'update project_info_iosbuild set date=%s, x_framework=%s, framework=%s where nid=%s'

        # check build record is whether exits.
        self.cursor.execute(sql_cmd_r, (build_record['project_id'], build_record['project_version']))
        res = self.cursor.fetchone()
        if res:
            self.cursor.execute(sql_cmd_u, (build_record['date'], build_record['x_framework'], build_record['framework'],
                                            res[0]))
        else:
            self.cursor.execute(sql_cmd_c, (build_record['project_version'], build_record['date'], build_record['x_framework'],
                                             build_record['framework'], build_record['project_id']))

        self.commit()

    def insert_build_record_android(self, build_record):
        sql_cmd_r = 'select nid from project_info_androidbuild where package_name=%s and package_version_name=%s ' \
                    'and product_flavor_name=%s and module_name=%s'
        sql_cmd_c = 'insert into project_info_androidbuild (package_name, package_version_name, module_name, ' \
                    'product_flavor_name, package_mini_sdk, package_mapping_url, deeplink_scheme, git_sha_code, ' \
                    'git_branch_name, date, snapshot, library_coordinate_list, project_id, package_version_code) value ' \
                    '(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        sql_cmd_u = 'update project_info_androidbuild set package_target_sdk=%s, package_mini_sdk=%s, ' \
                    'package_mapping_url=%s, deeplink_scheme=%s, git_sha_code=%s, git_branch_name=%s, date=%s, snapshot=%s, ' \
                    'library_coordinate_list=%s, package_version_code=%s where nid=%s'

        # check build record is whether exits.
        self.cursor.execute(sql_cmd_r, (build_record['package_name'], build_record['package_version_name'],
                                         build_record['product_flavor_name'], build_record['module_name']))
        res = self.cursor.fetchone()
        if res:
            self.cursor.execute(sql_cmd_u, (build_record['package_target_sdk'], build_record['package_mini_sdk'],
                                             build_record['package_mapping_url'], build_record['deeplink_scheme'],
                                             build_record['git_sha_code'], build_record['git_branch_name'],
                                             build_record['date'], build_record['snapshot'],
                                             build_record['library_coordinate_list'],
                                            build_record['package_version_code'], res[0]))
        else:
            self.cursor.execute(sql_cmd_c, (build_record['package_name'], build_record['package_version_name'],
                                             build_record['module_name'], build_record['product_flavor_name'],
                                             build_record['package_mini_sdk'], build_record['package_mapping_url'],
                                             build_record['deeplink_scheme'], build_record['git_sha_code'],
                                             build_record['git_branch_name'], build_record['date'],
                                             build_record['snapshot'], build_record['library_coordinate_list'],
                                             build_record['project_id'], build_record['package_version_code']))

        self.commit()

    def commit(self):
        self.conn.commit()

    def cursor_close(self):
        self.cursor.close()

    def conn_close(self):
        self.conn.close()