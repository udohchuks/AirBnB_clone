# Airbnb Clone Project


![HBNB](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230807%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230807T210900Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=83117fbd8b211f00946a0abd38a8b63d3b6c42cf681cd0bbf7774f20e9cc8065)


## Description of the project

The aim of this project is to deploy a replica of the [Airbinb Website](https://www.airbnb.com/).The final version of this project will have:

* A command interpreter to manipulate data without a visual interfaces(for development and testing purposes)

* A front-end website

* A database to manage the backend functionality

* An API that provides a communication interface between the frontend and the backend

## Description of the Command interpreter

## Description of the Command interpreter

| Commands                       | Description                                                        |
| ------------------------------ | ------------------------------------------------------------------ |
| `quit`                         | Quit the console                                                  |
| `help` or `help <command>`     | Display all commands or Display instruction for a specific command |
| `create <class>`               | Create an object                                                  |
| `show <class> <id>`            | Show string representation of an object                           |
| `destroy <class> <id>`         | Delete object                                                     |
| `all` or `all <class>`         | Print string representation of all objects or for a specific class |
| `update <class> <id>`          | Update an object with a certain attribute                        |



## Execution
***clone*** the repo
```
git clone https://github.com/udohchuks/AirBnB_clone.git
```
***Inreractive*** Mode
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```
***Non-interactive*** Mode
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```