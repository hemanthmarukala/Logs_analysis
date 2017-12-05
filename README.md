# Logs-Analysis
Part of the Udacity Nano Degree Full Stack.

## The purpose of this project
Analysis of the given data and create a reporting tool to analyse and print the best authors, articles etc. 

## Prerequirements
[Python](https://www.python.org/download/releases/3.0/)-3.X
[PostgreSQL](https://www.postgresql.org/)-latest version.
[Vagrant](https://www.vagrantup.com/)
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) are required to run SQL database server and web app. 
[Database] - Preinstalled in the ubuntu image provided by vagrant. 

## Files
This project database is comprised of 3 tables:
- logs_analysis.py	 
Internal reporting tool.
- report.txt
A Sample result of the analytic tool.


## Environmant Setup:
1. Install Vagrant and Virtual Box
2. Download the data file. 
3. Download or clone repository on you machine.


## Running the software:
1. Initialte the virtual machine using "$vagrant up".
2. SSH to the virtual machine using "$vagrant ssh".
3. Download the newsdata.sql database file and add the database file to the PSQL engine on the VM. 
5. Navigate to vagrant directory on the virtual machine. 
6. Go to logs directory with `cd /vagrant/logs`.
7. Run logs_analysis.py file to analyse the log data. 
8. A text file will be created showing the analysis data. 
9. Shutdown the VM. 


## Code Quality
PEP-8 Standard
