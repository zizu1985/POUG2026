"""
    Verify backup retention is set correctly:
        Development, Test and Sanpit -> 14 days
        Production -> 21 days
    Only valid for stage test_oracle_db_create
"""
from __future__ import unicode_literals
from __future__ import print_function

import os
import json
import re
import pytest

@pytest.mark.test_createdb('test_oracle_db_create')
def test_backupconfiguration(pathdir, db_name, db_host, level_support, stage, record_xml_attribute):

    bkpConfig = '{}/{}.cfg'
    bkpConfig = bkpConfig.format(pathdir,db_name)
    retention = 0
    retention_prod = 21
    retention_nonprod = 14
    retention_config = 0

    record_xml_attribute("classname", stage)
    record_xml_attribute("name", "req003-backup-retention")

    # Check if backup config file exists
    assert os.path.isfile(bkpConfig), 'Backup config file does not exist'
    with open(bkpConfig, 'r') as file:

        # Read each line in the file
        for line in file:
        
            # Find line with backup retention
            if "RETENTION_DAYS" in line:
                retention = line.strip().split('=')[1].strip()
                if retention.isdigit():
                    retention = int(retention)
                    if level_support == 'Production':
                        assert retention == retention_prod, 'Incorrect retention for production'
                    elif level_support in ['Sandpit','Development','Test']:
                        assert retention == retention_nonprod, 'Incorrect retention for non-production'
                    else:
                        assert False, 'Incorrect level_support value'
                    retention_config = 1
                else:
                    assert False, 'Incorrect retention value in backup config'
                break
                
        if retention_config == 0:
            assert False, 'No retention configuration in backup configuration'
        
