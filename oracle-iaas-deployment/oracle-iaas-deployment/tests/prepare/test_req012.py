import pytest

@pytest.mark.test_prepare('test_environment_preparation')
def test_service(host, stage, record_xml_attribute):
        
    record_xml_attribute("classname", stage)
    record_xml_attribute("name", "req012-service")
        
    service = host.service("oracle-rdbms.service")
    assert service.is_enabled == True
    
    serviceFile = host.file("/etc/systemd/system/oracle-rdbms.service")
    assert serviceFile.is_directory == False
    assert serviceFile.user == "root"
    assert serviceFile.group == "root"
    assert serviceFile.mode == 0o644

    # grep -qs -- <string> <path_to_file>
    expected_output = [
        "Description=Oracle Database(s) and Listener",
        "Requires=network.target",
        "LimitMEMLOCK=infinity",
        "LimitNOFILE=65535",
        "Type=forking",
        "RemainAfterExit=yes",
        "User=oracle",
        "Group=oinstall",
        "Restart=no",
        "ExecStart=/opt/oracle/admin/scripts/oracleInit.sh start",
        "ExecStop=/opt/oracle/admin/scripts/oracleInit.sh stop",
        "WantedBy=multi-user.target",
    ]
    
    for value in expected_output:
        assert serviceFile.contains(value) == True
    