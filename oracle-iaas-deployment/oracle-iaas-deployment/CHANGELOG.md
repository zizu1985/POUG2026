# Changelog

All notable changes to this project will be documented in this file.

## [1.3.17] - 2026-08-15

### Changed
- Add CIS audit policy as part of new database creation

## [1.3.16] - 2026-07-21

### Changed
- Add support for installing Oracle Database software not in standard Oracle Inventory location

## [1.3.15] - 2026-07-10

### Changed
- Replaced hardcoded values in the Jenkins launch command with variables (e.g., prep_role_version, oracle_env_prep_version, role_manage_fs_version).       
- Converted the long Jenkins Python command to a multiline format for easier maintenance.
- Improved comments and consistency throughout the variables block.
- Use Env prepartion pipline in version 1.2.1

## [1.3.14] - 2026-06-21

### Added
- Psu apply role supports RHEL9

## [1.3.13] - 2026-06-10

### Added
- Add Cohesity support for databases in DC2 data center

## [1.3.12] - 2026-01-16

### Fixed
- Fixed Python interpreter issue with ansible by auto select python3 over python2

## [1.3.12] - 2025-12-16

### Changed
- Update tag for ansible-playbook_oracle_soft_install

## [1.3.11] - 2025-12-01

### Fixed
- Updated gitlab token

## [1.3.10] - 2025-11-06

### Added
- Add support for Oracle PSU 19.29

## [1.3.9] - 2025-10-07

### Fixed
- Change THP test in test_req006 to be synchronized with preparation OS Team code

### Changed
- role_manage_filesystem_version used in preparation stage changed to newest version 2.3.2

## [1.3.8] - 2025-09-29

### Added
- Calling preparation stage pipeline with version 1.1.1 which supports RHEL8 and RHEL9 
- Tests for preparation stage support RHEL8 and RHEL9

## [1.3.7] - 2025-09-22

### Added
- Crucial tests exposed as separated stage in pipeline, executed after environment preparation stage
- New set of tests written in testinfra library
- 10 new requirements added for check database server, covered by tests.
- add support for Oracle version 19.28
### Fixed
- Pipeline run with default input parameters vallues (in MR pipeline) has CI associated with Change Request created

## [1.3.6] - 2025-06-12

### Added
- Requirements created as required by ITQA team.
- [JIRA-2861] Create Oracle Installation Diagrams using Kroki framework

## [1.3.5] - 2025-06-02

### Added
- Add support for Oracle PSU 19.27
### Fixed
- Fixed validation check_business_service function by upgrade itsm runner images to version 1.0.2
- Fixed issue with not needed check size_db if action is createdb
### Changed
- Upgrade itsm runner images to version 1.0.2

## [1.3.4] - 2025-04-25

### Added
- Input parameters validation

## [1.3.3] - 2025-04-09

### Added
- New database marked as Qualified in ServiceNow
- Automatic test added for checking if Qualified checkbox is checked
- Create initial verion of Readme file (README.md)
- Automatic test added for checking if proper backup retention is set
### Fixed
- db_name is not required parameter for every automatic test case
- incorrect backup retention assigned to environment type

## [1.3.2] - 2025-02-07

### Fixed
- Fixed gitlab pull database token issue in before_script actions.

## [1.3.1] - 2024-12-06

### Added
- Make email notification on failure default.
- Added rc true for python launcher.

## [1.3.0] - 2024-12-05

### Added
- Update .gitlab-ci.yml file - change prod variables for snow and jenkins job
### Fixed
- Fixing issue with Linux pipeline apiuser

## [1.2.0] - 2024-11-27

### Added
- Add change number for snow CRQ update
### Fixed
- Fix change creation function bug
- Add before_script seciont for stages where ansible connects to host
### Changed
- Change success email description
- Change mail description failled nd passed
- Change email string
- Update email description
- Update change creation description
- Change default action to installsw (Oracle software installation)
- Update message string for email communication

## [1.1.0] - 2024-11-21

### Added
- Add vault variables for secret and tags
- Add log support level variable
### Changed
- Update runner tags in default
- Change istm snow lib to feature-xyz

## [1.0.0] - 2024-10-24

### Added
- Oracle IaaS New Database deployment pipeline migrated from jenkins to gitlab

[1.3.17]: https://example.com/databases/oracle/bundle/oracle-iaas-deployment/-/compare/1.3.16...1.3.17?from_project_id=136139
[1.3.16]: https://example.com/databases/oracle/bundle/oracle-iaas-deployment/-/compare/1.3.15...1.3.16?from_project_id=136139
[1.3.15]: https://example.com/databases/oracle/bundle/oracle-iaas-deployment/-/compare/1.3.14...1.3.15?from_project_id=136139
[1.3.14]: https://example.com/databases/oracle/bundle/oracle-iaas-deployment/-/compare/1.3.13...1.3.14?from_project_id=136139
[1.3.13]: https://example.com/databases/oracle/bundle/oracle-iaas-deployment/-/compare/1.3.12...1.3.13?from_project_id=136139