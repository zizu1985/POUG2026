import pytest

@pytest.mark.test_prepare('test_environment_preparation')
def test_oratab_file(host, stage, record_xml_attribute):

    record_xml_attribute("classname", stage)
    record_xml_attribute("name", "req011-scripts")

    res_cmd = host.run('ls -l /opt/oracle/admin/scripts | wc -l')
    assert res_cmd.succeeded == True
    assert (res_cmd.stdout).strip() >= "0"