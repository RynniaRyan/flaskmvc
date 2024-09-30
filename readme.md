[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/RynniaRyan/flaskmvc)

# Project Description
This command-line application is allows for student participations to be showcased in various competitions. Enabling efficient management, data collection, and recognition of achievements.

[Project Requirments]
- Create Competition
- Import competition results from file
- View competitions list
- View competition results

# Template Used
Created using a template for flask applications structured in the Model View Controller pattern.

# Dependencies
* Python3/pip3
* Packages listed in requirements.txt

# Installing Dependencies
```bash
$ pip install -r requirements.txt
```

# Initializing the Database
```bash
$ flask init
```

# Project Flask Commands
To execute the command, invoke with `flask` followed by the command name and enter the relevant parameters when prompted. These commands are separated into two distinct groups: (1) Competition (2) Student.

_Competiiton Commands_
```bash
$ flask competition list
```
```bash
$ flask competition create
```
```bash
$ flask competition add-result
```
```bash
$ flask competition view-result
```

_Student Commands_
```bash
$ flask student list
```
```bash
$ flask student view-participation
```