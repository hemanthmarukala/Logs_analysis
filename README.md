# Logs-Analysis
Part of the Udacity Nano Degree Full Stack.

## The purpose of this project
Analysis of the given data and create a reporting tool to analyse and print the best authors, articles etc. 

## Prerequirements
[Python](https://www.python.org/download/releases/3.0/)-3.X
[PostgreSQL](https://www.postgresql.org/)-latest version.
[Vagrant](https://www.vagrantup.com/)
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) are required to run SQL database server and web app. 
[Database] - Preinstalled in the ubuntu image located in vagrant folder. 

## How to run
1. Download or clone repository on you machine.
2. Navigate to vagrant directory. 
3. Initialte the virtual machine using $vagrant up.
4. SSH to the virtual machine using $vagrant ssh.
5. Run logs_analysis.py file to analyse the log data. 
6. A text file will be created showing the analysis data. 
7. Shutdown the VM. 

## Files
This project database is comprised of 2 files:
- logs_analysis.py	 
Internal reporting tool.
- report.txt
A Sample result of the analytic tool. 

## Code Quality
PEP-8 Standard
