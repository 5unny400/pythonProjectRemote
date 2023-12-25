"""
@FileName：get_hubble_version.py
@Description：
@Author：shenxinyuan
@Time：2023/12/25
"""
import re

hubble_version = "HubbleDB v3.17-20-g40d6d40a-dirty (x86_64-redhat-linux, built 2023/01/13 09:52:28, go1.17.8)"
postgresql_version = "PostgreSQL 13.5 (Ubuntu 20.04.3 LTS) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0, 64-bit"

def _get_server_version_info(hubble_version):
    # v = connection.execute("select version()").scalar()
    v = hubble_version
    m = re.match(
        r".*(?:PostgreSQL|EnterpriseDB) "
        r"(\d+)\.?(\d+)?(?:\.(\d+))?(?:\.\d+)?(?:devel|beta)?",
        v,
    )
    if not m:
        raise AssertionError(
            "Could not determine version from string '%s'" % v
        )
    return tuple([int(x) for x in m.group(1, 2, 3) if x is not None])


print(_get_server_version_info(postgresql_version))
