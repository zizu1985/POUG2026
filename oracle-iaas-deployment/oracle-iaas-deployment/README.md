# oracle-iaas-deployment
Gitlab pipeline to fully setup Oracle 12.2, 18.x, 19.x database software.


## Requirements
This IaC provides the functionality to prepare and install Oracle database on linux systems.

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

- RedHat RHEL 8.x or 9.x Operating System
- Ansible 2.9
- Python 3

## Framework or Coding Technology

-----BEGIN TECH-----\
TECH-Main: Gitlab \
TECH-Testing: pytest, testinfra \
TECH-Auxiliary: ansible-role, ansible-playbook \
TECH-CICD: Gitlab, Jenkins \
-----END TECH-----

## Prerequisites

| **Prerequisite**           | **Description**                                                  |
|:--------------------------:|:----------------------------------------------------------------:|
| Red Hat Enterprise Linux 8.x | This OS should be the one running in the target servers        |
| Red Hat Enterprise Linux 9.x | This OS should be the one running in the target servers        |


## Parameters
----------

`business_service`: ServiceNow Application Service<br>
`server`: Linux Server for operational activity (fqdn)<br>
`action`: What Operation do you want to perform<br>
`version`: Oracle Version Release<br>


## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

List of playbooks that the pipeline uses:

- ansible-role-environment_preparation-oracle # Prepare server for Oracle software installation<br>
- ansible-playbook_oracle_soft_install # Install Oracle software<br>
- ansible-playbook_oracle_db_create # Create new Oracle database<br>
- ansible-role-gis-email # Send emails for communication<br>

List of repositories that the pipeline checkouts:

|           **Software/Framework/Code repository**                                     | **Version/Description** |
|:------------------------------------------------------------------------------------:|:-----------------------:|
| https://example.com/databases/itsm/itsm-snow-db-lib.git                           |         1.0.0           |


## IaC Components

| **Component**  | **Version**  |
|:------------:|:-----------------:|
| [itsm-snow-db-lib](https://example.com/databases/itsm/itsm-snow-db-lib.git ) | 1.0.0 |


## Role Variables

**Prepare server for Oracle software installation**<br>
`server`: Server where roles will be executed against<br>
`db_name`: Oracle database name for naming proper filesystems</br> 
`size_db`: Database size in GB</br>
`version`: Version of database to be installed</br> 
`request_id`: SNOW request id for reference</br> 
`mail_address`: Requestor email address</br> 
`userid`: Userid for reference</br> 
`business_service`: Bussiness Service for new database</br> 
`db_usage`: Is database production/non-production</br> 
`pb_vc_hostname`: VC Hostname</br> 
`pb_vc_cluster`: VC Datacenter</br>
`pb_vc_datacenter`: VC Cluster</br> 

**Install Oracle software**<br>
`version`: Version of database to be installed<br>
`db_sever`: Server where roles will be executed against<br>

**Create new Oracle database**<br>
`dbname`: New Oracle database name<br>
`level_supp`: Oracle database level support<br>
`ora_username`: Oracle username<br>
`ora_password`: Oracle password<br>
`ora_password`: LMS password<br>
`mail_address`: Requestor email address<<br>

**Send emails for communication**<br>
`getit_req`: SNOW request id for reference<br>
`snow_req`: SNOW request id for reference<br>
`component`: Name of component - Oracle Db Deployment<br>
`status_email`: Success or not<br>
`team_email`: Team for receaving email<br>
`header_option`: Option to display in header<<br> 
`ci_name`: CI name<br>     
`hostname`: Hostname<br>   
`DbName`: Database Name<br>    
`Port`: Port number<br> 
`Environment`: Environment type<br>
`action`: action to implement<br>
`oracle_version`: Oracle software version<br>
`action`: action to implement<br>
`snow_desc`: Description for SNOW change<br>

## Environments

Intended to be used in: Sandpit, Test, Development and Production servers

## Tested Versions

| **Operating System** | **Release Date** | **Kernel version** |
|:--------------------:|:----------------:|:------------------:|
| RHEL 8.6       |         2022-05-10       | 4.18.0-372 |
| RHEL 9.2       |         2023-05-10       | 5.14.0-284.11.1.el9_2 |

## Tests

[pytest](https://docs.pytest.org/) scripts are located in the `tests` and `tests\prepare` directory. 

| Unique ID | Requirement                                                                            | Acceptance Criteria | Valid for action        |
|:----------|:---------------------------------------------------------------------------------------|:-------------------:|:-----------------------:|
| req001    | Check Oracle Software / Oracle database have installed                                 |  All checks passed  | installsw createdb full |
| req002    | Test if Qualified checkbox is checked in SNOW for new database CI                      |  All checks passed  | createdb full           |
| req003    | Test if backup retention for database has been set correctly                           |  All checks passed  | createdb full           |
| req004    | Test if oracle user has been correctly prepared on server                              |  All checks passed  | prepare full            |
| req005    | Test if all required filesystems have been correctly prepared on server                |  All checks passed  | prepare full            |
| req006    | Test if Huge Pages have been correctly configured on server                            |  All checks passed  | prepare full            |
| req007    | Test if OS kernel parameters have been set correctly on server                         |  All checks passed  | prepare full            |
| req008    | Test if /usr/local/bin/ora.env has been correctly created on server                    |  All checks passed  | prepare full            |
| req009    | Test if OS limits have been correctly created on database server for oracle user       |  All checks passed  | prepare full            |
| req010    | Test if /etc/oratab has been correctly created on database server                      |  All checks passed  | prepare full            |
| req011    | Test if /opt/oracle/admin/scripts folder has been correctly created on database server |  All checks passed  | prepare full            |
| req012    | Test if service oracle-rdbms has been correctly created on database server             |  All checks passed  | prepare full            |
| req013    | Test if shared memory has been correctly configured on database server.                |  All checks passed  | prepare full            |


## Oracle Installation Diagram

Please use Light mode in Gitlab to see details.
Dark mode is not supported by Kroki.

Pipeline Diagram - Oracle Installation (action == full)
----------------
```seqdiag
seqdiag {
  User
  iCare
  Gitlab
  Jenkins
  ServiceNow
  Nexus
  DatabaseServer
  Splunk

  User -> iCare [label = "1. IaaS Oracle New Database ordered"];
  iCare -> Gitlab [label = "2. Input parameters validation (static parameters)"];
  Gitlab -> ServiceNow [label = "3. Input parameters validation (dynamic parameters)"];
  Gitlab -> Jenkins [label = "4. Launch Oracle Environment Preparation"];
  Jenkins -> Gitlab [label = "5. Environment prepared"];
  Gitlab -> Nexus [label = "6. Download Oracle software binaries"];
  Gitlab <- Nexus [label = "7. Oracle software binaries downloaded"];
  Gitlab -> DatabaseServer [label = "8. Install Oracle software"];
  Gitlab -> Gitlab [label = "9. Test Oracle Software Installation"];
  Gitlab -> Gitlab [label = "10. Create database\nConfigure database\nIntegrate with external systems - Cohecity, LogicMonitor, RDBI"];
  Gitlab -> Nexus [label = "11. Download Oracle Scripts/Cohesity prerequisites"];
  Gitlab <- Nexus [label = "12. Oracle scripts downloaded"];
  Gitlab -> Gitlab [label = "13. Configure Oracle database backup with Cohesity"];
  Gitlab -> Gitlab [label = "14. Test Database Installation"];
  Gitlab -> ServiceNow [label = "15. Create new Configuration Item in SNOW\nCreate upstream relation\nCreate downstream relation"];
  Gitlab <- ServiceNow [label = "16. Configuration Item successfully created in SNOW"];
  Gitlab -> Gitlab [label = "17. Test Configuration Item creation"];
  Gitlab -> ServiceNow [label = "18. Create Change Request - begin"];
  Gitlab <- ServiceNow [label = "19. Create Change Request - begin - confirmation"];
  Gitlab -> Gitlab [label = "20. Validate execution"];
  Gitlab -> ServiceNow [label = "21. Create Change Request - end"];
  Gitlab <- ServiceNow [label = "22. Create Change Request - end - confirmation"];
  Gitlab -> ServiceNow [label = "23. Create incident if necessesary"];
  Gitlab <- ServiceNow [label = "24. Create incident if necessesary - confirmation"];
  Gitlab -> Splunk [label = "25. Register automation work record in Splunk"];
  Gitlab <- Splunk [label = "26. Register automation work record in Splunk - confirmation"];
  Gitlab -> iCare [label = "27. Send email success/fail to user"];
  iCare -> User [label = "28. User enjoys playing with new database :)"];
}
```

Pipeline Diagram - Oracle Installation (action == prepare)
----------------
```seqdiag
seqdiag {
  User
  iCare
  Gitlab
  Jenkins
  ServiceNow
  Splunk

  User -> iCare [label = "1. IaaS Oracle New Database ordered"];
  iCare -> Gitlab [label = "2. Input parameters validation (static parameters)"];
  Gitlab -> ServiceNow [label = "3. Input parameters validation (dynamic parameters)"];
  Gitlab -> Jenkins [label = "4. Launch Oracle Environment Preparation"];
  Jenkins -> Gitlab [label = "5. Environment prepared"];
  Gitlab -> ServiceNow [label = "6. Create Change Request - begin"];
  Gitlab <- ServiceNow [label = "7. Create Change Request - begin - confirmation"];
  Gitlab -> Gitlab [label = "8. Validate execution"];
  Gitlab -> ServiceNow [label = "9. Create Change Request - end"];
  Gitlab <- ServiceNow [label = "10. Create Change Request - end - confirmation"];
  Gitlab -> ServiceNow [label = "11. Create incident if necessesary"];
  Gitlab <- ServiceNow [label = "12. Create incident if necessesary - confirmation"];
  Gitlab -> Splunk [label = "13. Register automation work record in Splunk"];
  Gitlab <- Splunk [label = "14. Register automation work record in Splunk - confirmation"];
  Gitlab -> iCare [label = "15. Send email success/fail to user"];
  iCare -> User [label = "16. User enjoys playing with new prepared database environment :)"];
}
```

Pipeline Diagram - Oracle Installation (action == installsw)
----------------
```seqdiag
seqdiag {
  User
  iCare
  Gitlab
  ServiceNow
  Nexus
  DatabaseServer
  Splunk

  User -> iCare [label = "1. IaaS Oracle New Database ordered"];
  iCare -> Gitlab [label = "2. Input parameters validation (static parameters)"];
  Gitlab -> ServiceNow [label = "3. Input parameters validation (dynamic parameters)"];
  Gitlab -> Nexus [label = "4. Download Oracle software binaries"];
  Gitlab <- Nexus [label = "5. Oracle software binaries downloaded"];
  Gitlab -> DatabaseServer [label = "6. Install Oracle software"];
  Gitlab -> Gitlab [label = "7. Test Oracle Software Installation"];
  Gitlab -> ServiceNow [label = "8. Create Change Request - begin"];
  Gitlab <- ServiceNow [label = "9. Create Change Request - begin - confirmation"];
  Gitlab -> Gitlab [label = "10. Validate execution"];
  Gitlab -> ServiceNow [label = "11. Create Change Request - end"];
  Gitlab <- ServiceNow [label = "12. Create Change Request - end - confirmation"];
  Gitlab -> ServiceNow [label = "13. Create incident if necessesary"];
  Gitlab <- ServiceNow [label = "14. Create incident if necessesary - confirmation"];
  Gitlab -> Splunk [label = "15. Register automation work record in Splunk"];
  Gitlab <- Splunk [label = "16. Register automation work record in Splunk - confirmation"];
  Gitlab -> iCare [label = "17. Send email success/fail to user"];
  iCare -> User [label = "18. User enjoys playing with new database software :)"];
}
```

Pipeline Diagram - Oracle Installation (action == createdb)
----------------
```seqdiag
seqdiag {
  User
  iCare
  Gitlab
  ServiceNow
  Nexus
  DatabaseServer
  Splunk

  User -> iCare [label = "1. IaaS Oracle New Database ordered"];
  iCare -> Gitlab [label = "2. Input parameters validation (static parameters)"];
  Gitlab -> ServiceNow [label = "3. Input parameters validation (dynamic parameters)"];
  Gitlab -> Nexus [label = "4. Download Oracle software binaries"];
  Gitlab <- Nexus [label = "5. Oracle software binaries downloaded"];
  Gitlab -> DatabaseServer [label = "6. Install Oracle software"];
  Gitlab -> Gitlab [label = "7. Test Oracle Software Installation"];
  Gitlab -> ServiceNow [label = "8. Create Change Request - begin"];
  Gitlab <- ServiceNow [label = "9. Create Change Request - begin - confirmation"];
  Gitlab -> Gitlab [label = "10. Validate execution"];
  Gitlab -> ServiceNow [label = "11. Create Change Request - end"];
  Gitlab <- ServiceNow [label = "12. Create Change Request - end - confirmation"];
  Gitlab -> ServiceNow [label = "13. Create incident if necessesary"];
  Gitlab <- ServiceNow [label = "14. Create incident if necessesary - confirmation"];
  Gitlab -> Splunk [label = "15. Register automation work record in Splunk"];
  Gitlab <- Splunk [label = "16. Register automation work record in Splunk - confirmation"];
  Gitlab -> iCare [label = "17. Send email success/fail to user"];
  iCare -> User [label = "18. User enjoys playing with new database :)"];
}
```

## License

GNU license

## Author Information

Tomasz Ziss<br>