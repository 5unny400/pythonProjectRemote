"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2025/2/11
"""
import base64
import hashlib
import json
import time
import uuid
import urllib

import requests


SF_REQ_URL = "https://sfapi-sbox.sf-express.com/std/service"
checkword = "unt82zJNEgRRONO3OTYB1rFrWplgB1S8"
accessToken = "3C96367F8D65488084F70A9B98C57324"


def call_express(data):
    """

    """
    print("express request:" + str(data))
    res = requests.post(SF_REQ_URL, data=data)
    res_msg = res.json()
    # response_bean = ResponseBean(**res_msg)
    # print("express response:" + json.dumps(res_msg, ensure_ascii=False))
    return res_msg


def get_msg_digest(data, timestamp) -> str:
    source_str = urllib.parse.quote_plus(data + timestamp + checkword)  # noqa
    # 先md5加密然后base64加密
    m = hashlib.md5()
    m.update(source_str.encode("utf-8"))
    md5_str = m.digest()
    msg_digest = base64.b64encode(md5_str).decode("utf-8")
    return msg_digest


def get_express_common_params():
    timestamp = str(int(time.time()))
    request_id = uuid.uuid1()
    msgData = dict({
        "header": {
            "deptCode": "755",
            "oprId": "13099090",
            "accessCode": ""
        },
        "content": {
            "param": {
                "lang_code": "1",
                "waybill_no": "SF7444495001186",
                "api": "get_waybill_info",
                "partner_id": "GZLS4K8L",
                "city_id": "755",
                "area_code": "755Y"
            }
        }
    })
    param_str = json.dumps(msgData)
    msgDigest = get_msg_digest(param_str, timestamp)
    # msgDigest 和 accessToken 二选一即可
    param_dict = dict(
        msgData=param_str,
        # msgDigest=msgDigest,
        accessToken=accessToken,
        timestamp=timestamp,
        serviceCode="COM_RECE_EOS_QUERY_WAYBILL_INFO",
        requestID=request_id,
        partnerID="Y1CYPXL2",
    )
    data = call_express(data=param_dict)
    return data


print(get_express_common_params())
