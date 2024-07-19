# PortKnocker-Qt

PortKnocker-Qt is a GUI Full-Python utility developed with the Qt Framework to enable opening/closing a specific port configuration on your server.

## License

The GNU Affero General Public License is a free, **copyleft** license for software and other kinds of works, specifically designed to ensure cooperation with the community in the case of network server software.

## Description

Port opening is two-fold : the client side for which the functionalities are provided by **PortKnocker-Qt** and the server side for which the functionalities are provided by a knocking daemon such as *knockd*. 

### On the server side

The server side daemon interacts with the firewall (which is on the same server -- or not) by sending commands in order to open or close ports. To be fully functional, the server must be configured with the same sequence of ports and protocols used by the user-defined configurations stored in PortKnocker-Qt. If the combination of ports and protocols don't match between the server and the client, no port will open nor close and you might be clicking insanely to no avail :-).

### Security Considerations

Your digital security cannot rely on unique measures. If someone is determined to get to your computer, time always plays against you . Port Knocking is nice because it makes it harder to get to your ressources but it must be supplemented with other security measures.

## Installation Instructions

### As is - Native Python

The easier way to install PortKnocker-Qt is to set up a virtualenv in ./PortKnocker-Qt directory. Installing a virtual environment is strongly advised to prevent messing with your current Python installation. This way you are sure to install every package needed defined in *requirements.txt*. 

#### Downloading package 

```
$ git clone https://github.com/soualidjerbi/portKnocker-Qt.git
```

#### Installing the virtual environment

There are many ways to install a virtual environment. Choose the method that fits best for you. 

- Lightweight  : This method does not let you choose the python version. Create the virtual environment dirctly with the python [venv](https://peps.python.org/pep-0405/) module

```
$ python -m venv <directory>
```

- More elaborate : Use [virtualenv](https://virtualenv.pypa.io/en/latest/user_guide.html) to install the virtual environment and select one of the different versions of python you already have on your computer with : 

```
$ virtualenv --python="/path/to/python3.xx" "/path/to/new/virtualenv/"
```

- Finest : use [anaconda or miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) to install the virtual environment. "conda create -n myenv python=3.9"

for each method refer to to the linked documentation.

### Install the required packages and run!

Just use requirements.txt file inside the portKnocker-Qt directory

```
$ cd portKnocker-Qt
$ pip install -r requirements.txt
$ python QtMain.py
```

### Using PyInstaller to build the executable

This is a useful method for easy distribution as a ready-to-use package.
Follow the steps described above to install a virtual environement, then execute the following command

```
$ pyinstaller -y QtPortKnocker.spec
```

## User Guide

Should be straightforward. To be continued, though.
FQDN as well as IP addresses are allowed.

![alt text](https://github.com/soualidjerbi/portKnocker-Qt/blob/main/mainWindow.png)


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## Other personal objectives I pursue

This project is also intended to be educational. So far, this project helped me better understanding :

- [x] the [QT Framework](https://doc.qt.io/) to create user interfaces with Python,
- [x] [QT Designer](https://doc.qt.io/qt-6/qtdesigner-manual.html) to create user interfaces
- [x] the object oriented programming (still a lot to learn though)
- [x] the use of [pyinstaller](https://pyinstaller.org/en/stable/) to distribute packaged apps, simple and ready-to-use on Mac OS (family requirement...) or Windows (not tried yet...)
- [x] the use of virtual envirements as described above
- [x] the use of [visual studio code](https://code.visualstudio.com/) to do the job
- [x] how useful AI can be to develop faster. [Codeium](https://codeium.com/) has my preference so far but I also use [ChatGPT](https://chatgpt.com) from time to time, mainly to get a better grasp of Python coding concepts, tools, design patterns and so on. Youtube is also a good friend and I deeply extend all my thanks to [Mariya](https://www.youtube.com/@PythonSimplified), [Arjan](https://www.youtube.com/@ArjanCodes), [James Murphy](https://www.youtube.com/@mCoding) and [Federico Azzurro - Indently](https://www.youtube.com/@Indently). Check their channels out, they all are awesome.
- [x] the use of git tools and github.com to share what I learn and get some feedback to improve. Maybe try something bigger later
- [x] the kind of licence which fits better to my personal ideas
- [x] how to write this README.md and use the Markdown language
- [x] how to **Test code** with Python
- [ ] why and how to use @staticmethod (for utility Classes in my context)
- [ ] many other things I didn't think about yet :smile:

