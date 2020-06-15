def get_random_name():
    import random
    xing = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
    ming = '豫章故郡洪都新府星分翼轸地接衡庐襟三江而带五湖'
    X = random.choice(xing)
    M = "".join(random.choice(ming) for i in range(2))
    print(X + M)


def create_open_user():
    # 创建开放用户，包括了appid和key
    # open user
    import os
    import binascii
    appid = binascii.hexlify(os.urandom(5)).decode('utf-8')
    key = binascii.hexlify(os.urandom(16)).decode('utf-8')
    print('Create open user(%s, %s) done' % (appid, key))
    return appid, key


def demo():
    ...
    import datetime
    print((datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
    start_date = end_date = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    print(start_date)
    print(end_date)


def str_bin():
    _str = ''
    _bin = ' '.join([bin(ord(c)).replace('0b', '') for c in _str])
    print(_bin)
    _str = ''.join([chr(i) for i in [int(b, 2) for b in _bin.split(' ')]])
    print(_str)


def get_session():
    import requests
    res = requests.post(url='xxx', data={'username': 'xxx', 'password': 'xxx'})
    print(res.headers['Set-Cookie'].split(';')[0])


def base64_():
    import base64
    s = b'printer'
    b = b'printer@gzlgst'
    print(s)
    s = base64.b64encode(s)
    b = base64.b64encode(b)
    print(s)
    print(b)
    s = base64.b64decode(s)
    print(s)


def find_file():
    from pathlib import Path

    source_path = r'./项目内容/取号机日志/取号机项目数据/data/runtime/'

    pattern = '**/2019-07-31/register/face/*id(*_*_1)*.jpg'

    path = Path(source_path)

    target_files = path.glob(pattern)

    target_files = [str(file) for file in path.glob(pattern)]

    print(target_files)


def excel():
    import xlrd
    import xlwt

    limit = 5000
    readbook = "20191210.xls"
    savebook = "."
    data = xlrd.open_workbook(readbook)
    # 获取sheet
    table = data.sheets()[0]

    # 行数
    nrows = table.nrows
    # 列数
    ncols = table.ncols + 1

    sheets = nrows / limit

    if not sheets.is_integer():
        sheets = sheets + 1

    title_row = table.row_values(0)
    title_row.insert(0, '原序号')

    for i in range(0, int(sheets)):
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('名单')
        for col in range(0, ncols):
            worksheet.write(0, col, title_row[col])
            f.write('\n')
        for row in range(1, limit + 1):
            newRow = row + limit * i
            if newRow < nrows:
                row_content = table.row_values(newRow)
                row_content.insert(0, newRow + 1)
                for col in range(ncols):
                    worksheet.write(row, col, row_content[col])
                    f.write('\n')
        workbook.save(savebook + "/" + str(i) + ".xls")


def ram_str(num):
    import random
    import string
    return ''.join([random.choice(string.ascii_lowercase) for _ in range(random.randint(0, num))])


def to_str(data):
    try:
        return str(int(float(data)))
    except Exception:
        return str(data)


def alert():
    import re
    import datetime

    alert_ip = {
        '10.225.0.199': '行政楼-认证机-4楼1号',
        '10.225.0.198': '行政楼-认证机-4楼2号',
        '10.225.0.197': '行政楼-认证机-4楼3号',
        '10.225.0.196': '行政楼-认证机-5楼4号',
        '10.225.0.195': '行政楼-认证机-5楼5号',
        '10.225.0.194': '行政楼-认证机-5楼6号',
        '10.225.0.192': '行政楼-注册机1号',
        '10.225.1.81': '凯月楼-认证机1号',
        '10.225.1.82': '凯月楼-认证机2号',
        '10.225.1.83': '凯月楼-认证机3号',
        '10.225.1.84': '凯月楼-认证机4号',
        '10.225.1.85': '凯月楼-注册机1号',
        '10.225.1.86': '凯月楼-认证机11号',
        '10.225.1.87': '凯月楼-认证机7号',
        '10.225.1.88': '凯月楼-认证机8号',
        '10.225.1.89': '凯月楼-认证机9号',
        '10.225.1.90': '凯月楼-认证机10号',
        '10.225.1.65': '凯月楼-管理电脑',
        '10.225.0.202': '凯月楼-管理电脑',
        '10.225.1.118': '凯达楼-认证机30号',
        '10.225.1.119': '凯达楼-认证机31号',
        '10.225.1.120': '凯达楼-认证机32号',
        '10.225.1.121': '凯达楼-认证机33号',
        '10.225.1.122': '凯达楼-认证机34号',
        '10.225.1.123': '凯达楼-认证机35号',
        '10.225.1.124': '凯达楼-注册机1号',
        '10.225.1.117': '凯达楼-服务器',
        '10.225.1.125': '凯达楼-管理电脑',
        '10.225.1.220': '加压站-注册机1号',
        '10.225.1.221': '加压站-认证机50号',
        '10.225.1.222': '加压站-认证机51号',
        '10.225.1.218': '加压站-服务器',
        '10.225.1.219': '加压站-管理电脑',
        '10.225.1.227': '知识城-一体机60号',
        '10.225.1.228': '知识城-服务器',
        '10.225.1.226': '知识城-管理电脑',
        '10.225.2.181': '广垦饭堂-认证机70号',
        '10.225.2.182': '广垦饭堂-认证机71号',
        '10.225.2.183': '广垦饭堂-认证机72号',
        '10.225.2.184': '广垦饭堂-认证机73号',
        '10.225.2.185': '广垦饭堂-认证机74号',
        '10.225.2.186': '广垦饭堂-注册机1号',
        '10.225.2.187': '广垦饭堂-主服务器',
        '10.225.2.188': '广垦饭堂-备服务器',
        '10.225.2.189': '广垦饭堂-管理电脑',
    }

    content = """
        ----------------------------------------
        服务器mysql错误:
        > 时间:2019-12-16T15:25:04.212820Z
        > 错误信息:10.225.1.117服务器连接超时
        > 当前状态为:0
        > ip:10.225.2.186


        ----------------------------------------
        服务器mysql错误:
        > 时间:2019-12-16T16:01:09.226854Z
        > 错误信息:10.225.1.117服务器连接超时
        > 当前状态为:0
        > ip:10.225.1.226


        ----------------------------------------
        服务器mysql错误:
        > 时间:2019-12-16T16:28:03.248487Z
        > 错误信息:10.225.1.117服务器连接超时
        > 当前状态为:0
        > ip:10.225.1.218


        ----------------------------------------
    """
    res = re.findall(r'.*> 当前状态为:(.*).*', content)
    for old_status in res:
        if old_status == '0':
            new_status = '与凯月主服务器断开连接'
        else:
            new_status = '重新与凯月主服务器连接'

        content = content.replace('> 当前状态为:%s' % old_status, '> 当前状态为:%s' % new_status)

    res = re.findall(r'.*> 时间:(\d*-\d*-\d*T\d*:\d*:\d*.\d*Z).*', content)
    for utc_string in res:
        utc_dt = datetime.datetime.strptime(utc_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        localtime_dt = utc_dt + datetime.timedelta(hours=8)
        localtime_string = datetime.datetime.strftime(localtime_dt, "%Y-%m-%d %H:%M:%S")
        content = content.replace(utc_string, localtime_string)

    res = re.findall(r'.*> ip:(.*).*', content)
    for ip in res:
        if ip in alert_ip:
            ip_message = '> ip:%s\n> 备注:%s' % (ip, alert_ip[ip])
            content = content.replace('> ip:%s' % ip, ip_message)
    print(content)


def middleware():
    middle = (
        '123',
        '456'
    )
    print(type(middle))


def compare():
    import xlrd

    new_wb = xlrd.open_workbook('new.xlsx')
    table = new_wb.sheets()[0]
    nrows = table.nrows
    new_data = {}
    for row in range(1, nrows):
        row_content = table.row_values(row)
        new_data[row_content[4]] = row_content[3]

    old_wb = xlrd.open_workbook('old.xlsx')
    table = old_wb.sheets()[0]
    nrows = table.nrows
    old_data = {}
    for row in range(1, nrows):
        row_content = table.row_values(row)
        old_data[row_content[4]] = row_content[3]

    for k, v in new_data.items():
        if k in old_data:
            if v != old_data[k]:
                print('%s:%s not equal to old_data %s' % (k, v if v else 'None', old_data[k]))
        else:
            print('%s not in old_data' % k)


def airwave_log():
    with open('log.log', 'r', encoding='utf-8') as f:
        content = f.readline()
        while content:
            # print(content)
            if '10.115.1.84' in content:
                break
            content = f.readline()
        print(content)


def game():
    import re
    import json
    import ast
    import chardet
    import requests
    # with open('data.json', 'r', encoding='utf-8') as f:
    #     datas = json.load(f)
    # print(datas.keys())
    # print(datas.get('equipskillconfig'))

    # res = requests.get('http://www.guajigame.com/_qingbian/js/data/gamedata.js')
    # res = requests.get('http://wdhtiger.com/_qingbian//js/data/gamedata.js')
    # content = res.text
    # with open('gamedata.js', 'w', encoding='utf-8') as f:
    #     f.write(res.text)
    # content = res.text

    with open('gamedata.js', 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('\n', '').replace('\'', '')
    js_content = content.split('var')
    js_content = filter(None, js_content)
    datas = {}
    for index, value in enumerate(js_content):
        value = value.replace(' ', '')
        value = value.split('=')
        title = value[0]
        data = value[1]
        data = ast.literal_eval(data)
        datas[title] = data

    js_datas = {}
    for key, values in datas.items():
        for k, value in values.items():
            name = value['NAME']
            if key not in js_datas:
                js_datas[key] = [name]
            else:
                js_datas[key].append(name)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(js_datas, f, ensure_ascii=False, indent=4)

    # print(content)

    # datas = {}
    # monstertable = []
    # for k, v in datas.items():
    #     monstertable.append(v['NAME'])


def jiami():

    data = 'appid=78ba28bf6a&external_account_id=18850260579&status=0&timestamp=1583310929&key=cd66105e4238144cae26b4d94c13a4a8'
    data = 'appid=486acfd497&external_account_id=123456&timestamp=1583311821&key=1b1ee0f1f5441446980a601c2e568366'
    key = 'cd66105e4238144cae26b4d94c13a4a8'

    def hmac1(key, data):
        print('-------------------hamc1')
        import binascii
        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives import hmac as _hmac
        key = key.encode('utf-8')
        data = data.encode('utf-8')

        h = _hmac.HMAC(key, hashes.SHA256(), backend=default_backend())
        h.update(data)

        digest = h.finalize()

        hex_digest = binascii.hexlify(digest)

        #  upper_digest = hex_digest.upper()
        lower_digest = hex_digest.lower()
        decode_digest = lower_digest.decode('utf-8')

        return decode_digest

    def hmac2(key, data):
        import hmac
        from hashlib import sha256
        key = key.encode('utf-8')
        data = data.encode('utf-8')
        # 哈希加密，算法为sha256
        signature = hmac.new(key, data, digestmod=sha256)
        # 获取十六进制数据字符串的签名
        signature = signature.hexdigest()
        # 签名转小写
        signature = signature.lower()

        return signature

    signature1 = hmac1(key, data)
    print(signature1)

    signature2 = hmac2(key, data)
    print(signature1 == signature2)

    print(len('人生苦短，我用Python'.encode('utf-8')))


def subway():
    def hmac2(key, data):
        import hmac
        from hashlib import sha256
        key = key.encode('utf-8')
        data = data.encode('utf-8')
        # 哈希加密，算法为sha256
        signature = hmac.new(key, data, digestmod=sha256)
        # 获取十六进制数据字符串的签名
        signature = signature.hexdigest()
        # 签名转小写
        signature = signature.lower()

        return signature

    def sign(data, key):
        # sort
        sorted_data = sorted(data.items(), key=lambda items: items[0])

        # join
        joined_data = '&'.join([item[0] + '=' + str(item[1]) for item in sorted_data if item[0] != 'sign' and item[1] != '' and item[1] is not None])
        joined_data = joined_data + "&key=" + key

        # sign
        signature = hmac2(key, joined_data)

        return signature

    import requests
    import time

    key = '1b1ee0f1f5441446980a601c2e568366'
    appid = '486acfd497'
    datas = [
        {'url': 'http://10.0.0.221:8015/record/query/', 'method': 'get', 'data': {'record_id': '1', 'key': key, 'appid': appid, 'timestamp': int(time.time()) + 0}},
        {'url': 'http://10.0.0.221:8015/user/query/', 'method': 'get', 'data': {'external_account_id': '123', 'key': key, 'appid': appid, 'timestamp': int(time.time()) - 0}},
        {'url': 'http://10.0.0.221:8015/user/update/', 'method': 'post', 'data': {'external_account_id': '123', 'key': key, 'appid': appid, 'timestamp': int(time.time()) - 0}},
        {'url': 'http://10.0.0.221:8015/user/delete/', 'method': 'post', 'data': {'external_account_id': '123', 'key': key, 'appid': appid, 'timestamp': int(time.time()) - 0}},
    ]
    with open('test.log', 'w', encoding='utf-8') as f:
        for data in datas:
            status_code = None
            return_data = None
            error = None
            try:
                key = data['data']['key']
                data['data'].pop('key')
                signature = sign(data['data'], key)
                data['data']['sign'] = signature

                if data['method'] == 'get':
                    res = requests.get(url=data['url'], params=data['data'])
                elif data['method'] == 'post':
                    headers = {
                        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary8MA4YWxkTrZu0gW'
                    }
                    res = requests.post(url=data['url'], data=data['data'], headers=headers)
                    print(res.request.headers)
                    print(res.status_code)
                data['data']['key'] = key
                status_code = res.status_code
                if status_code == 200:
                    return_data = res.json()
                    if return_data['code']:
                        error = return_data['msg']
            except KeyError as e:
                error = e

            f.write('url:%s' % data['url'])
            f.write('\n')
            f.write('method:%s' % data['method'])
            f.write('\n')
            f.write('data:%s' % data['data'])
            f.write('\n')
            f.write('status_code:%s' % status_code)
            f.write('\n')
            f.write('return_data:%s' % return_data)
            f.write('\n')
            f.write('error:%s' % error)
            f.write('\n')

            # print('url:%s' % data['url'])
            # print('method:%s' % data['method'])
            # print('data:%s' % data['data'])
            # print('status_code:%s' % status_code)
            # print('return_data:%s' % return_data)
            # print('error:%s' % error)


def cafe_test():
    import requests
    import time

    server_host = '192.168.0.201:8022'

    test_datas = [
        # {'name': '消费人员明细', 'url': 'http://%s/account/get_consume_detail/' % server_host, 'data': {'page': 1, 'limit': 10, 'start_date': '2020-03-01 00:00:00', 'end_date': '2020-04-16 23:59:59', 'cafeteria_name': '凯月楼', 'category_id': 1, 'department_id': 3, 'device_id': 26}, 'method': 'POST'},
        # {'name': '消费分餐', 'url': 'http://%s/account/get_consume_statistic/' % server_host, 'data': {'page': 1, 'limit': 10, 'excel_group_by': 'group_by_device', 'start_month': '2020-04', 'end_month': '2020-04', 'start_date': '2020-03-01 00:00:00', 'end_date': '2020-04-13 23:59:59', 'cafeteria_name': '凯月楼', 'device_id': 26, 'group_by': 'day'}, 'method': 'POST'},
        # {'name': '消费汇总', 'url': 'http://%s/account/get_consume_statistic/' % server_host, 'data': {'page': 1, 'limit': 10, 'excel_group_by': 'group_by_cafeteria', 'start_month': '2020-04', 'end_month': '2020-04', 'start_date': '2020-03-01 00:00:00', 'end_date': '2020-04-13 23:59:59', 'cafeteria_name': '凯月楼', 'group_by': 'day'}, 'method': 'POST'},
        # {'name': '充值新增明细', 'url': 'http://%s/account/get_refund_detail/' % server_host, 'data': {'page': 1, 'limit': 10, 'type': 'TOP_UP', 'first_top_up': 'True', 'start_month': '2020-04', 'end_month': '2020-04', 'start_date': '2020-03-01 00:00:00', 'end_date': '2020-04-13 23:59:59', 'cafeteria_name': '凯月楼', 'department_id': 673, 'category_id': 1, 'method': 'CASH', 'user_id': '10'}, 'method': 'POST'},
        # {'name': '充值明细', 'url': 'http://%s/account/get_refund_detail/' % server_host, 'data': {'page': 1, 'limit': 10, 'type': 'TOP_UP', 'first_top_up': 'False', 'start_month': '2020-04', 'end_month': '2020-04', 'start_date': '2020-03-01 00:00:00', 'end_date': '2020-04-13 23:59:59', 'cafeteria_name': '凯月楼', 'department_id': 673, 'category_id': 1, 'method': 'CASH', 'user_id': '10'}, 'method': 'POST'},
        # {'name': '补贴详情', 'url': 'http://%s/account/get_staff_subsity_detail/?page=1&limit=10&start_date=2020-04-01 00:00:00&end_date=2020-04-30 23:59:59&category_id=&department_id=&is_new_join=' % server_host, 'method': 'GET'},
        # {'name': '打印补贴', 'url': 'http://%s/account/export_staff_subsity_detail/?start_date=2020-04-01 00:00:00&end_date=2020-04-30 23:59:59&category_id=&department_id=&is_new_join=&file_type=pdf&author=admin&sign=cHJpbnRlcg==,cHJpbnRlckBnemxnc3Q=' % server_host, 'method': 'GET'},
        # {'name': '打印消费详情记录', 'url': 'http://%s/account/export_consume_detail/?start_date=2020-01-01 00:00:00&end_date=2020-01-31 23:59:59&cafeteria_name=&category_id=&department_id=&device_id=&file_type=pdf&author=admin&sign=cHJpbnRlcg==,cHJpbnRlckBnemxnc3Q=' % server_host, 'method': 'GET'},
        # {'name': '补贴详情', 'url': 'http://%s/account/get_staff_subsity_detail/?page=1&limit=10&start_date=2020-04-01 00:00:00&end_date=2020-04-30 23:59:59&category_id=2&department_id=&is_new_join=' % server_host, 'method': 'GET'},
        # {'name': '部门补贴', 'url': 'http://%s/account/get_staff_subsity_statistic/?page=1&limit=10&start_date=2020-04-01 00:00:00&end_date=2020-04-30 23:59:59&department_id=&category_id=' % server_host, 'method': 'GET'},
        # {'name': '查看日志', 'url': 'http://%s/user/get_logs/' % server_host, 'method': 'GET'},
        # {'name': '创建角色', 'url': 'http://%s/user/create_role/' % server_host, 'data': {'alias': '111', 'permission_ids': ''}, 'method': 'POST'},
        # {'name': '修改角色', 'url': 'http://%s/user/create_role/' % server_host, 'data': {'alias': '456', 'permission_ids': '', 'role_id': 37}, 'method': 'POST'},
        # {'name': '查看角色', 'url': 'http://%s/user/get_role/' % server_host, 'data': {'role_id': 31}, 'method': 'POST'},
        # {'name': '查看角色列表', 'url': 'http://%s/user/get_roles/' % server_host, 'method': 'GET'},
        # {'name': '查看系统账号', 'url': 'http://%s/user/get_user/?user_id=1' % server_host, 'method': 'GET'},
        # {'name': '查看系统账号列表', 'url': 'http://%s/user/get_users/' % server_host, 'method': 'GET'},
        # {'name': '添加系统管理账号', 'url': 'http://%s/user/create_user/' % server_host, 'method': 'GET'},
        # {'name': '修改系统账号信息', 'url': 'http://%s/user/update_user/' % server_host, 'method': 'GET'},
        # {'name': '删除系统账号', 'url': 'http://%s/user/delete_user/' % server_host, 'method': 'GET'},
        # {'name': '修改系统账号的角色', 'url': 'http://%s/user/update_user_role/' % server_host, 'method': 'GET'},
        # {'name': '查看设备列表', 'url': 'http://%s/authentication/get_devices/' % server_host, 'method': 'GET'},
        # {'name': '修改设备信息', 'url': 'http://%s/authentication/update_device/' % server_host, 'method': 'GET'},
        # {'name': '删除手掌', 'url': 'http://%s/staff/delete_hand/' % server_host, 'data': {}, 'method': 'POST'},
        # {'name': '激活', 'url': 'http://%s/staff/update_staff/' % server_host, 'data': {'staff_id': 649, 'status': 'ENABLED'}, 'method': 'POST'},
        # {'name': '增加单位', 'url': 'http://%s/org/create_department/' % server_host, 'data': {}, 'method': 'POST'},
        # {'name': '修改单位', 'url': 'http://%s/org/update_department/' % server_host, 'data': {}, 'method': 'POST'},
        # {'name': '删除单位', 'url': 'http://%s/org/delete_department/' % server_host, 'data': {}, 'method': 'POST'},
        # {'name': '查询人员补贴设置', 'url': 'http://%s/account/get_staff_subsidy_settings/' % server_host, 'data': {}, 'method': 'GET'},
        # {'name': '创建人员补贴设置', 'url': 'http://%s/account/create_staff_subsidy_settings/' % server_host, 'data': {'staff_id': 3917, 'status': 'DISABLED', 'start_date': '2019-12-01 00:00:00', 'end_date': '2020-05-31 23:59:59'}, 'method': 'POST'},
        # {'name': '更新人员补贴设置', 'url': 'http://%s/account/update_staff_subsidy_settings/' % server_host, 'data': {'id': 2, 'staff_id': 80, 'status': 'DISABLED', 'start_date': '2020-01-01 00:00:00', 'end_date': '2020-02-01 00:00:00'}, 'method': 'POST'},
        # {'name': '删除人员补贴设置', 'url': 'http://%s/account/delete_staff_subsidy_settings/' % server_host, 'data': {'id': 1}, 'method': 'POST'},
        {'name': '查看设置', 'url': 'http://%s/user_info/get_user_default_role_settings/' % server_host, 'data': {}, 'method': 'GET'},
        {'name': '修改设置', 'url': 'http://%s/user_info/update_user_default_role_settings/' % server_host, 'data': {'user_default_role_setting_id': 1, 'role_ids': '1,2'}, 'method': 'POST'},

    ]

    session = requests.session()

    session.post(url='http://%s/administrator/login/' % server_host, data={'adminname': 'admin', 'password': 'admin'})

    for test_data in test_datas:
        now = time.time()
        test_num = 1
        if test_data['method'] == 'GET':
            for i in range(test_num):
                res = session.get(url=test_data['url'])
                if res.status_code != 200:
                    print(res.text)
                else:
                    print(res.status_code)
                    print(res.json())
        else:
            for i in range(test_num):
                res = session.post(url=test_data['url'], data=test_data['data'])
                if res.status_code != 200:
                    print(res.text)
                else:
                    print(res.status_code)
                    print(res.json())
        print('%s:%ss, 食堂服务器预计时间:%s' % (test_data['name'], round((time.time() - now) / test_num, 3), round((time.time() - now) / test_num / 3 * 2, 3)))


def func_time(func):
    def inner(*args, **kw):
        import time
        start_time = time.time()
        result = func(*args, **kw)
        end_time = time.time()
        print('函数%s运行时间为：%s秒' % (func.__name__, round(end_time - start_time, 4)))
        return result
    return inner


def quick_sort(alist, start, end):
    """快速排序"""

    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low - 1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, end)


def main():
    ...
    # get_random_name()

    # create_open_user()

    # demo()

    # get_session()

    # base64_()

    # str_bin()

    # find_file()

    # excel()

    # alert()

    # middleware()

    # compare()

    # airwave_log()

    # game()

    # jiami()

    # subway()

    cafe_test()


if __name__ == '__main__':
    main()
