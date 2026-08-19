import pytest

@pytest.mark.test_prepare('test_environment_preparation')
def test_oratab_file(host, stage, record_xml_attribute):

    record_xml_attribute("classname", stage)
    record_xml_attribute("name", "req010-oratab")

    file = host.file("/etc/oratab")
    assert file.is_directory == False
    assert file.user == "oracle"
    assert file.group == "oinstall"
    assert file.mode == 0o640