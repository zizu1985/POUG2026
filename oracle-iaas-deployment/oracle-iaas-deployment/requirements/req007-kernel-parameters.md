### req007-kernel-parameters.md

OS Kernel Parameters have been correctly configured on database server.<br>

**Conditions:** Action set to prepare or full <br>
**Acceptance criteria:**Check kernel parameters have been set correctly on server:<br>
	a) Check fs.file-max parameter<br>
	b) Check kernel.sem parameter<br>
    c) Check kernel.shmmni parameter<br> 	
	d) Check kernel.msgmni parameter<br>
	e) Check kernel.msgmax parameter<br> 
	f) Check kernel.msgmax parameter<br>
	g) Check kernel.sched_min_granularity_ns parameter<br>
	h) Check kernel.sched_wakeup_granularity_ns parameter<br>
	i) Check net.core.rmem_default parameter<br>
	j) Check net.core.rmem_max parameter<br>
	k) Check net.core.wmem_default parameter<br> 
	l) Check net.core.net.core.wmem_max parameter<br>
	m) Check fs.aio-max-nr parameter<br>
	n) Check net.ipv4.ip_local_port_range parameter<br>
	o) Check vm.swappiness parameter<br>
	p) Check vm.dirty_writeback_centisecs parameter<br>
	r) Check vm.dirty_expire_centisecs parameter<br>
	q) Check vm.dirty_background_ratio parameter<br>
	s) Check vm.dirty_ratio parameter <br>