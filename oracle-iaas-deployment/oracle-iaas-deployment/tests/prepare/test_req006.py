import pytest

@pytest.mark.test_prepare('test_environment_preparation')
def test_hugepages(host, stage, os_version, record_xml_attribute):
        
    record_xml_attribute("classname", stage)
    record_xml_attribute("name", "req006-hugepages")
    
    if os_version == "8":
        enabled_content = host.file("/sys/kernel/mm/transparent_hugepage/enabled").content_string.strip()
        
        # Ensure "never" is set as the active THP state
        assert "never" in enabled_content, \
            f"Transparent Huge Pages not disabled as expected in RHEL 8. Found: {enabled_content}"
        
        # Validate HugePages_Total is 0
        hugepages_total = host.check_output('grep -i HugePages_Total /proc/meminfo | awk \'{print $2}\'').strip()
        assert hugepages_total == '0', \
            f"Expected HugePages_Total to be 0 in RHEL 8, but found: {hugepages_total}"
        
        # Validate nr_hugepages is 0
        nr_hugepages = host.file("/proc/sys/vm/nr_hugepages").content_string.strip()
        assert nr_hugepages == "0", \
            f"Expected nr_hugepages to be 0 in RHEL 8, but found: {nr_hugepages}"
    elif os_version == "9":
        grub_content = host.file("/etc/default/grub").content_string.strip()

        # Ensure the `transparent_hugepage=never` is present in the GRUB configuration
        assert "transparent_hugepage=never" in grub_content, \
            f"Expected 'transparent_hugepage=never' in GRUB configuration for RHEL 9, but found: {grub_content}"

        # Validate HugePages_Total is 0
        hugepages_total = host.check_output('grep -i HugePages_Total /proc/meminfo | awk \'{print $2}\'').strip()
        assert hugepages_total == '0', \
            f"Expected HugePages_Total to be 0 in RHEL 9, but found: {hugepages_total}"
        
        # Validate nr_hugepages is 0
        nr_hugepages = host.file("/proc/sys/vm/nr_hugepages").content_string.strip()
        assert nr_hugepages == "0", \
            f"Expected nr_hugepages to be 0 in RHEL 9, but found: {nr_hugepages}"
    else: # Not supported version for test
        pytest.skip(f"Unsupported OS release version for check: {os_version}")