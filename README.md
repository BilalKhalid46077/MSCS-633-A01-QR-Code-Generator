# MSCS-633-A01-QR-Code-Generator

## QR Code Generator

## Project Overview

This project is a simple QR Code Generator developed using Python.

The application allows the user to enter a website URL and automatically generates a QR code for that URL. The generated QR code is saved as a PNG image file.

For this assignment, the application was tested using the following website:

**https://www.bioxsystems.com/**

## Purpose of the Project

The main purpose of this project is to demonstrate how Python can be used to generate QR codes from URL addresses.

QR codes are two-dimensional machine-readable codes that can store different types of information, including website URLs.

## Technologies Used

* Python
* qrcode Python library
* Pillow
* Visual Studio Code
* GitHub

## Requirements

Before running the program, make sure Python is installed on your computer.

The required Python package is listed in the `requirements.txt` file.

## Installation

### 1. Clone or download this repository

Download the project files from this GitHub repository.

### 2. Open the project folder

Open the project folder in Visual Studio Code.

### 3. Install the required library

Open the VS Code terminal and run:

```bash
python -m pip install -r requirements.txt
```

If necessary, the library can also be installed using:

```bash
python -m pip install qrcode[pil]
```

## How to Run the Program

Open the terminal in Visual Studio Code and run:

```bash
python qr_code_generator.py
```

The program will ask the user to enter a URL.

For example:

```text
https://www.bioxsystems.com/
```

After entering the URL, the application generates the QR code and saves it as:

```text
qr_code.png
```

The generated QR code can be scanned using a smartphone QR code scanner.

## Features

* Accepts a URL from the user
* Performs basic URL validation
* Generates a QR code
* Saves the QR code as a PNG image
* Provides messages showing the status of the operation
* Includes basic error handling
* Uses functions to keep the code organized


## Conclusion

This project demonstrates a simple practical use of Python for generating QR codes. The `qrcode` library makes it possible to create and save QR codes with only a small amount of Python code.

The project also demonstrates basic programming practices such as functions, input validation, exception handling, comments, and clear program structure.
