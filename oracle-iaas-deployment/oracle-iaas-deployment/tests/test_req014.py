"""
    Test if database CIS audit policy is applied correctly.
"""
from __future__ import unicode_literals
from __future__ import print_function

import os
import json
import re
import pytest
from pathlib import Path

@pytest.mark.test_createdb('test_oracle_db_create')
def test_CIS_policy(oracle_conn,pathdir, db_name, db_host, db_port, level_support, stage, record_xml_attribute,iscidefault=False):

    if db_host and db_name and db_port:

        sql_path = Path(__file__).parent.parent / "scripts" / "check_audit_policy.sql"
        sql = sql_path.read_text()
        cur = oracle_conn.cursor()
        cur.execute(sql)
        
        (result,) = cur.fetchone()     
        result = int(result)  
        
        if iscidefault:
            assert result >= 0, "Database doest not have CIS Audit Policy enabled"
        else:
            assert result >= 1, "Database doest not have CIS Audit Policy enabled"

    else:
        pytest.skip("Cannot get database credentials")
