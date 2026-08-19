"""
Parse the json output from mongodb and look for the created user and
permissions.
"""
from __future__ import unicode_literals
from __future__ import print_function

import os
import json
import re
import pytest

@pytest.mark.test_installsw('test_oracle_soft_install')
@pytest.mark.test_createdb('test_oracle_db_create')
def test_oracle(pathdir, db_name, db_host, level_support, stage, record_xml_attribute):
        
    record_xml_attribute("classname", stage)
    record_xml_attribute("name", "req001-oracle-install")

    filename = '{}/oracle_check_{}.out'
    filename = filename.format(pathdir,db_name)

    # Check that the file contains valid json
    assert os.path.isfile(filename), 'Output file does not exist'
    with open(filename) as file:
        content = file.read()
        assert 'SUCCESSFULLY' in content, 'Output has no SUCCESSFULLY field'
