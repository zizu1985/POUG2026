import pytest

@pytest.mark.parametrize(
    "sysctl_key,expected,os8_valid,os9_valid",
    [
        ("fs.file-max", "6815744", "true", "true"),
        ("kernel.sem", "300\t128000\t200\t8192", "true", "true"),
        ("kernel.shmmni", "4096", "true", "true"),
        ("kernel.msgmni", "2878", "true", "true"),
        ("kernel.msgmax", "8192", "true", "true"),
        ("kernel.msgmnb", "65536", "true", "true"),
        ("kernel.sched_min_granularity_ns", "10000000", "true", "false"),
        ("kernel.sched_wakeup_granularity_ns", "15000000", "true", "false"),
        ("net.core.rmem_default", "262144",  "true", "true"),
        ("net.core.rmem_max", "4194304", "true", "true"),
        ("net.core.wmem_default", "262144", "true", "true"),
        ("net.core.wmem_max", "1048576", "true", "true"),
        ("fs.aio-max-nr", "3145728", "true", "true"),
        ("net.ipv4.ip_local_port_range", "9000\t65500", "true", "true"),
        ("vm.swappiness", "0", "true", "true"),
        ("vm.dirty_writeback_centisecs", "100", "true", "true"),
        ("vm.dirty_expire_centisecs", "500", "true", "true"),
        ("vm.dirty_background_ratio", "3", "true", "true"),
        ("vm.dirty_ratio", "15", "true", "true"),
    ]
)
@pytest.mark.test_prepare('test_environment_preparation')
def test_kernel_parameters(host, stage, os_version, record_xml_attribute, sysctl_key, expected, os8_valid, os9_valid):
    
    record_xml_attribute("classname", stage)
    record_xml_attribute("name", "req007-kernel-parameters")
    run_test = False
    
    # evaluate if check should be run
    if os_version == "8" and os8_valid == "true":
        run_test = True
    elif os_version == "9" and os9_valid == "true":
        run_test = True
        
    # test kernel parameters
    if run_test:
        cmd = f'sysctl -a 2>/dev/null | grep "{sysctl_key} =" | tr -d " " | cut -d= -f2'
        res_cmd = host.run(cmd)
        assert res_cmd.succeeded == True
        assert res_cmd.stdout.strip() == expected
    else:
        pytest.skip()