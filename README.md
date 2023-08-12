# Airbnb Clone Project


![HBNB](Hbnblogo.png)


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
## Example
```bash
samuel@DESKTOP-3FSFCSN:~/AirBnB_clone$ ./console.py
(hbnb) all
[]
(hbnb) create User
682b5903-54cf-4903-a925-1e26346a28c5
(hbnb) all
["[User] (682b5903-54cf-4903-a925-1e26346a28c5) {'id': '682b5903-54cf-4903-a925-1e26346a28c5', 'created_at': datetime.datetime(2023, 8, 12, 12, 26, 47, 863098), 'updated_at': datetime.datetime(2023, 8, 12, 12, 26, 47, 863129)}"]
(hbnb) show User 682b5903-54cf-4903-a925-1e26346a28c5
[User] (682b5903-54cf-4903-a925-1e26346a28c5) {'id': '682b5903-54cf-4903-a925-1e26346a28c5', 'created_at': datetime.datetime(2023, 8, 12, 12, 26, 47, 863098), 'updated_at': datetime.datetime(2023, 8, 12, 12, 26, 47, 863129)}
(hbnb) update User 682b5903-54cf-4903-a925-1e26346a28c5 password my_pass
(hbnb) show User 682b5903-54cf-4903-a925-1e26346a28c5
[User] (682b5903-54cf-4903-a925-1e26346a28c5) {'id': '682b5903-54cf-4903-a925-1e26346a28c5', 'created_at': datetime.datetime(2023, 8, 12, 12, 26, 47, 863098), 'updated_at': datetime.datetime(2023, 8, 12, 12, 27, 41, 215466), 'password': 'my_pass'}
(hbnb) destroy User 682b5903-54cf-4903-a925-1e26346a28c5
(hbnb) all
[]
(hbnb)
```