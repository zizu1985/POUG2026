import pytest

@pytest.mark.test_prepare('test_environment_preparation')
def test_shared_mem_test(host, stage, record_xml_attribute):
            
    record_xml_attribute("classname", stage)
    record_xml_attribute("name", "req013-shared-mem")

    res_cmd = host.run("MEM=$(awk '/MemTotal/ {print $2}' /proc/meminfo) && MSHM=$(df -k /dev/shm | awk '{print $2}' | tail -1) && MEM80=$(($MEM*80/100)) && echo $(($MEM80 - $MSHM))")
    assert res_cmd.succeeded == True
    assert int((res_cmd.stdout).strip()) <= 10000