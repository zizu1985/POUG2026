import pytest

def get_total_mount_size(host, path):

    # Get detailed filesystem statistics
    stat_cmd = host.run(f"stat -f -c '%S %b %a %f' {path}")
    assert stat_cmd.rc == 0
    
    # Parse statvfs output
    block_size, total_blocks, available_blocks, free_blocks = map(int, stat_cmd.stdout.strip().split())
    
    return block_size * total_blocks

@pytest.mark.test_prepare('test_environment_preparation')
def test_filesystems(host, stage, db_name, db_host, db_size, record_xml_attribute):
            
    record_xml_attribute("classname", stage)
    record_xml_attribute("name", "req005-filesystems")
    
    # /opt/oracle filesystem
    mountPoint = host.mount_point("/opt/oracle")
    assert mountPoint.exists == True
    assert get_total_mount_size(host, "/opt/oracle") > 51000000 * 1024

    directory = host.file("/opt/oracle")
    assert directory.is_directory == True
    assert directory.user == "oracle"
    assert directory.group == "oinstall"
    
    # /var/opt/oracle
    mountPoint = host.mount_point("/var/opt/oracle")
    assert mountPoint.exists == True
    assert get_total_mount_size(host, "/var/opt/oracle") > 5000000 * 1024
    
    directory = host.file("/var/opt/oracle")
    assert directory.is_directory == True
    assert directory.user == "oracle"
    assert directory.group == "oinstall"
    
    # /opt/oracle/logs
    mountPoint = host.mount_point("/opt/oracle/logs")
    assert mountPoint.exists == True
    assert get_total_mount_size(host, "/opt/oracle") > 41000000 * 1024

    directory = host.file("/opt/oracle/logs")
    assert directory.is_directory == True
    assert directory.user == "oracle"
    assert directory.group == "oinstall"
    
    # /oracle_agent
    mountPoint = host.mount_point("/oracle_agent")
    assert mountPoint.exists == True
    assert get_total_mount_size(host, "/oracle_agent") > 5000000 * 1024
    
    directory = host.file("/oracle_agent")
    assert directory.is_directory == True
    assert directory.user == "oracle"
    assert directory.group == "oinstall"
    
    # /opt/oracle/export
    mountPoint = host.mount_point("/opt/oracle/export")
    assert mountPoint.exists == True
    assert get_total_mount_size(host, "/opt/oracle/export") > 103000000  * 1024
    
    directory = host.file("/opt/oracle/export")
    assert directory.is_directory == True
    assert directory.user == "oracle"
    assert directory.group == "oinstall"
    
    # /var/opt/oracle/{{ db_name }}/databases
    filesystem = f"/var/opt/oracle/{db_name}/databases"
    mountPoint = host.mount_point(filesystem)
    assert mountPoint.exists == True
    assert get_total_mount_size(host, filesystem) > int(db_size) // 1024 // 1024
    
    filesystem = f"/var/opt/oracle/{db_name}/databases"
    directory = host.file(filesystem)
    assert directory.is_directory == True
    assert directory.user == "oracle"
    assert directory.group == "oinstall"
    
    # /var/opt/oracle/{{ db_name }}/fra
    filesystem = f"/var/opt/oracle/{db_name}/fra"
    mountPoint = host.mount_point(filesystem)
    assert mountPoint.exists == True
    assert get_total_mount_size(host, filesystem) > 52000000 * 1024

    filesystem = f"/var/opt/oracle/{db_name}/fra"
    directory = host.file(filesystem)
    assert directory.is_directory == True
    assert directory.user == "oracle"
    assert directory.group == "oinstall"