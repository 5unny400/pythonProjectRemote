import hashlib


def md5_test():
    uuid_code = '6d4a124cde126b4564167ba4b1f2a559'
    try:
        tmp = uuid_code + 'datagrand_license_copyright_9s^994f@)E'
        md5 = hashlib.md5()
        md5.update(tmp.encode('utf-8'))
        code = md5.hexdigest()
    except Exception:  # NOQA
        code = ''
    print()
    print('The md5 code of the uuid_code and "datagrand_license_copyright_9s^994f@)E" is:', code)


md5_test()
