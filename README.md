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
Download Vagrant from *vagrantup.com*, install the version for your operating system. If Vagrant is sucessfully installed, you will be able to run ```vagrant --version``` in your terminal to see the version number.
#### (3) Download the VM configuration
Download and unzip *FSND-Virtual-Machine.zip*. This will give you a directory called FSND-Virtual-Machine. Use ```cd``` command to navigate to the FSND-Virtual-Machine directory and use ```ls``` command to see the files in it.
#### (4) Start the VM
From your terminal, inside the **vagrant** subdirectory, run the command ```vagrant up```. This will cause vagrant to download Linux operating system and install it. When ```vagrant up``` is finished running, you will get your shell prompt back. At this point, you can run ```vagrant ssh``` to log into your newly installed Linux VM.
#### (5) Running the database
The PostgreSQL database server will automatically be started inside the VM. You can use ```psql``` command-line tool to access it and run SQL statements.
#### (6) Logging out and in
If you type ```exit``` or ```Ctrl+D``` at the shell prompt inside the VM, you will be logged out, and put back into your host computer's shell. To log back in, make sure you're in the same directory and type ```vagrant ssh``` again. If you reboot your computer, you will need to run ```vagrant up``` to restart the VM.

### 2. Download the data
Download and unzip *newsdata.zip*. The file inside is called *newsdata.sql*. Put this file into the **vagrant** directory, which is shared with your virtual machine. To have the reporting tool correctly run, you have to load the site's data into your local database. To load the data, use the command ```psql -d news -f newsdata.sql```. Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.

### 3. Run the python file
Before you run **logs_analysis.py**, make sure it is in the same folder with your database. In your vagrant shell, use command ```pyhon logs_analysis.py``` to run this file, and you will see the results output on the terminal.

## Notes
The questions are:

**1. What are the most popular three articles of all time?** Which articles have been accessed the most? 

**2. Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? 

**3. On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

For the third quesion, ```create view``` query is used. The five views are:

1. total_visit_per_day: daily total visit group by day
2. errors: all the errors' information
3. error_per_day: errors group by day
4. refined_log: join view1 and view3
5. final_result: calculate the error rate per day
