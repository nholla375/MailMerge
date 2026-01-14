# Automated Invitation Letter Generator

A Python script that reads a template letter and a list of names, then automatically creates personalized letters for each recipient. Each letter is saved as a separate file, ready to send.

## Features

* Reads a base letter template from a file
* Loads multiple names from a text file
* Replaces placeholders with actual names
* Generates individualized output files
* Simple and efficient file handling

## How It Works

1. The program reads a starting letter template.
2. It loads a list of invitee names.
3. The placeholder `[name]` is replaced with each person’s name.
4. A new personalized letter is created and saved for each recipient.

## File Structure

```
├── Input
│   ├── Letters
│   │   └── starting_letter.txt
│   └── Names
│       └── invited_names.txt
└── Output
    └── ReadyToSend
        └── letter_for_<name>.txt
```

## Requirements

* Python 3.x
* No external libraries required

## Running the Script

```bash
python main.py
```

## Learning Goals

This project was built to practice:

* File input/output (reading and writing files)
* String manipulation
* Looping through data
* Basic automation with Python
* Rewrite it to sound more **professional or portfolio-ready**
* Help you standardize **all your project READMEs** into one cohesive repo style
