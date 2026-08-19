import pytest

@pytest.mark.test_prepare('test_environment_preparation')
def test_oracle_user(host, stage, record_xml_attribute):
        
    record_xml_attribute("classname", stage)
    record_xml_attribute("name", "req004-test-user")

    oracle_user = host.user("oracle")
    gids = [198, 200]
    assert oracle_user.exists == True
    assert oracle_user.uid == 4808
    assert oracle_user.gid in gids
    assert oracle_user.group == "oinstall"
    assert "oinstall" in oracle_user.groups
    assert "dba" in oracle_user.groups
    assert oracle_user.shell == "/usr/bin/sh"
    assert oracle_user.home == "/home/oinstall/oracle"

