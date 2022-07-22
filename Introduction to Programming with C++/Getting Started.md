# Getting Started
## What is C++?
A **computer program** is a set of machine-readable <span style = "color:lightblue">machine-readable instructions</span> for a computer to accmplish a task.

**John von Neumann**, a mathematician in 1945, designed the computer architecture still used today. The computer reads information stored in <span style = "color:lightblue">memory</span> and sends it to the <span style = "color:lightblue">central processing unit (CPU)</span> and the <span style = "color:lightblue">arithmetic logic unit (ALU)</span> for processing.

The following table summarizes the *readability* of different types of programming languages.

|**language** | **readability** |
|:------------:|:---------------:|
|   machine    |      *???*      |
|   assembly   |      hard       |
|  high-level  |      easy       |

**Maintaining** means to modify and enhance the code. High-level languages, such as C++, are easier to remember, faster to write, less error-prone and easier to maintain than low-level languages.

A **compiler** (e.g., gcc/g++ or VC++) translates source code from higher-level programming languages to machine code which is then run. This document uses the **GNU gcc/g++ compiler**.

Invented by Danish computer scientist **Bjarne Stroustrup** in 1998, C++ is an <span style = "color:lightblue">object-oriented programming (OOP)</span> language and focuses on manipulating <span style = "color:lightblue">objects</span> to accomplish tasks. Compared to other programming languages, C++ is more low-level, allowing instructions to be sent directly to computer components.

## Installation on macOS
We install the ==C/C++ extension== on Visual Studio Code, the relevant compiler, and prepare to build and run C++ programs.
### Instructions
1. Install Visual Studio Code for macOS.
2. Install C/C++ extension on VSCode.
3. Set **g++** as the default compiler.
	1. Check version of **clang** and **g++** with `clang -v`.
	2. Install **Homebrew**. [^1]
	3. Install **GCC**.
	   ```bash
	   brew search gcc
	   brew install gcc@9
	   gcc-9 -v (gcc version 9.3.0)
		```
	1. Change configuration parameters and environment variables. Run `nano ~/.bash_profile` and add the following to the file. [^2]
	   ```bash
	   alias gcc='gcc-9'
	   alias cc='gcc-9'
	   alias g++='g++-9'
	   alias c++='c++-9'
		```
	1. Write the file, save and exit.
	2. Run `source ~/.bash_profile`.
	3. Run `g++ -v` to verify installation process.
1. Create your first program.
	1. Open a new folder.
	2. Create a new file with a `.cpp` file extension.
	3. Type code to output `'hello world'`.
2. Add **Code Runner** extension.
	1. Install the **Code Runner** extension.
	2. Open **Command Palette** and search for ==Search Preferences: Open Settings (JSON)== and open the `settings.json` file.
	3. Add the following to the file.
	   ```json
	   {
		   "update.mode" : "none",
		   "code-runner.customCommand" : "make",
		   "code-runner.runInTerminal" : true,
		   "code-runner.saveFileBeforeRun" : true,
		   "code-runner.saveAllFilesBeforeRun" : true,
		   "code-runner.ignoreSelection" : true,
		   "code-runner.clearPreviousOutput" : true,
		   "terminal.integrated.scrollback" : 10240,
		   "files.eol" : "\n",
		   "code-runner.executorMap" : {
			   "cpp" : "cd $dir && /usr/local/bin/g++-9 -std=c++11 $fileName  -o $fileNameWithoutExt && $dir$fileNameWithoutExt"
		   }
	   }
		```

## Installation on Windows

[^1]: **Homebrew**: a package manager for macOS users
[^2]: `nano`: default text editor for Linux (*see notes on Linux*)