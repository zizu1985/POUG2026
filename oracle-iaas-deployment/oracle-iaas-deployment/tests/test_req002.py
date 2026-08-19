"""
    Test if Qualified checkbox is checked in SNOW for new database CI
"""
from __future__ import unicode_literals
from __future__ import print_function

import os
import pytest
from xml.dom import minidom

@pytest.mark.test_createdb('test_ci_create_update')
def test_qualifiedcheckbox(pathdir, db_name, db_host, level_support, stage, record_xml_attribute):
        
    record_xml_attribute("classname", stage)
    record_xml_attribute("name", "req002-qualified-test")

    ci_payloadfile = '{}/{}'
    ci_payloadfile = ci_payloadfile.format(pathdir,'ci_payload_info_' + db_name + '.xml')

    # Check if ci info payload file exists
    assert os.path.isfile(ci_payloadfile), 'CI payload file does not exist'

    # Parse the XML file
    xmldoc = minidom.parse(ci_payloadfile)
    # Get a list of all 'item' elements
    itemlist = xmldoc.getElementsByTagName('u_qualified')

    assert len(itemlist) == 1, 'Cannot find qualified checkbox information in SNOW'
    checkboxvalue = itemlist[0].firstChild.nodeValue
    assert checkboxvalue == "true", 'Qualified checkbox is not checked for created/update database'