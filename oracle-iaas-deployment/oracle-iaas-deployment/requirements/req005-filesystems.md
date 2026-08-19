### req005-filesystems.md

Check all required filesystems have been created correctly on database server.<br>

**Conditions:** Action set to prepare or full <br>
**Acceptance criteria:** All required filesystems have been correctly configured ( **{{ db_name }}** represents database name):<br>
a) /opt/oracle filesystem configured<br>
b) /var/opt/oracle filesystem configured<br>
c) /opt/oracle filesystem configured<br>
d) /oracle_agent filesystem configured<br>
e) /opt/oracle/export filesystem configured<br>
f) /var/opt/oracle/{{ db_name }}/databases filesystem configured<br>
g) /var/opt/oracle/{{ db_name }}/fra filesystem configured<br>