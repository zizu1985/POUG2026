import pytest

@pytest.mark.test_prepare('test_environment_preparation')
def test_oraenv_file(host, stage, record_xml_attribute):
        
    record_xml_attribute("classname", stage)
    record_xml_attribute("name", "req008-oraenv")

    file = host.file("/usr/local/bin/ora.env")
    assert file.is_directory == False
    assert file.user == "root"
    assert file.group == "oinstall"
    assert file.mode == 0o755