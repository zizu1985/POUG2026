import pytest

@pytest.mark.parametrize("flag, result",[("-n", "131072"),("-u", "131072"),("-s", "32768"),("-c", "unlimited"),("-l", "50000000")])
@pytest.mark.test_prepare('test_environment_preparation')
def test_limit_file(flag, result, host, stage, record_xml_attribute):
        
    record_xml_attribute("classname", stage)
    record_xml_attribute("name", "req009-user-limits")

    # /etc/security/limits.d/99-oracle.conf ownership
    file = host.file("/etc/security/limits.d/99-oracle.conf")
    assert file.is_directory == False
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o644
    
    # The maximum number of open file descriptors
    #res_cmd = host.run(f'ulimit {flag}')
    res_cmd = host.run("ulimit {0}".format(flag))
    assert res_cmd.succeeded == True
    assert (res_cmd.stdout).strip() == result
    