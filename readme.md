[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/RynniaRyan/flaskmvc)

# Project Description
This command-line application facilitates the management and display of student participation in various competitions.Key features include the ability to create competitions, upload competition results via CSV file format, display student participation results and rankings, and search for individual students to showcase their achievements across multiple competitions

[Project Requirments]
- Create Competition
- Import competition results from file
- View competitions list
- View competition results

# Template Used
Created using a template for flask applications structured in the Model View Controller pattern.

### NOTE: 
#### All User Model related content is to be ignored

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