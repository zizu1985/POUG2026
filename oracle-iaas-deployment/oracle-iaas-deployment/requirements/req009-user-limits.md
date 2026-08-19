### req009-user-limits.md

Check if OS limits hav been correctly set for user oracle on server. <br>

**Conditions:** Action set to prepare or full <br>
**Acceptance criteria:** OS limits have been correctly created on database server for oracle user:<br>
a) The maximum number of open file descriptors for oracle user is 131072<br>
b) The maximum number of processes available to oracle user is 131072<br>
c) The maximum stack size for oracle user is 32768<br>
d) The maximum size of core files created is set to unlimited<br>
e) The maximum size that can be locked into memory is 50000000<br>

