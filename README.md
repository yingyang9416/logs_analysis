# logs_analysis

## What's this

This project is a reporting tool that prints out reports(in plain text) based on the data in PostgreSQL database. The data came from a real-world web application, with fields representing information that a web server would record, such as HTTP status codes and URL paths. The web server and the reporting tool both connect to the same database, allowing information to flow from the web server into the report.

No user input is required in this tool. It answers the questions about the user activity on the news website.

## How to use

### 1. Install the Virtual Machine
The PostgreSQL database and support software needed for this project are provided by a Linux virtual machine (VM). You have to install the VM first. You'll need to install tools called **Vagrant** and **VirtualBox** to install and manage VM.
#### (1) Use a terminal
For **Mac/Linux** systems, your regular terminal prgram will do just fine. For **Windows**, I recommend using **Git Bash** terminal that comes with the Git Software.
#### (2) Istall Vagrant
