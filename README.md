# Foldora - File & Directory Manager CLI Tool

Foldora is a Python command-line interface (CLI) tool designed to help you efficiently manage files and directories.

## Features

Foldora provides essential file and directory operations, including:

- Listing files and directories.
- Creating directories and files.
- Purging files and directories.
- Displaying file contents.

## Installation

To install Foldora, clone the repository and navigate to the project directory:

- PS: Make sure python is installed in case you're new to Python.

```sh
pip install foldora
```

## Usage

Run Foldora using the `fd` command followed by the desired operation.

### Listing Files and Directories
Lists all files and directories in the current or specified paths.

**Command:**
```sh
fd l [optional_paths]
```

**Examples:**
```sh
fd l           # List contents of the current directory
fd l /path/to/directory1 /path/to/directory2  # List contents of specific directories
```

### Creating Directories
Creates one or more directories.

**Command:**
```sh
fd d directory1 directory2 ...
```

**Example:**
```sh
fd d new_folder another_folder
```

### Creating Files
Creates one or more files in the current directory or a specified path.

**Command:**
```sh
fd f '[-p path]' file1 file2 ...
```

**Examples:**
```sh
fd f file1.txt file2.txt  # Create files in the current directory
fd f -p /path/to/directory file1.txt file2.txt  # Create files in a specified directory
```

### Purging Files and Directories
Deletes specified files and directories with user confirmation.

**Command:**
```sh
fd p file1 directory1 ...
```

**Example:**
```sh
fd p old_file.txt unused_folder
```

### Displaying File Contents
Shows the content of one or more files.

**Command:**
```sh
fd c file1 file2 ...
```

**Example:**
```sh
fd c notes.txt log.txt
```

## Contributing
Feel free to submit pull requests or open issues to enhance Foldora!

## License
This project is licensed under the MIT License.
