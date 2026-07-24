import sys
from backupcfg import job1, job2, job3, job4

"""
***************************************************************************

 TITLE: File Backups

 AUTHOR: T. Peirce - 30028720@students.sunitafe.edu.au

 DATE: 24/06/2026

 PURPOSE: Script designed to perform backup tasks

 

 VERSION 1.0 | DATE 24/07/26

 ------------------------------------------------------------------------

 v0.1      | 24/03/26 | TP | Initial version

 v0.2      | 26/04/26 | TP | Minor tweaks to code to condense text

 v1.0      | 24/07/26 | TP | Initial program release

***************************************************************************
"""

###################
#Maps each job to their definition
###################
job_mapping = {
    "job1": job1,
    "job2": job2,
    "job3": job3,
    "job4": job4
}
###################
#Allows for bash commands to run program
###################
if len(sys.argv) > 1:
    job_name = sys.argv[1]
    if job_name in job_mapping:
        job_mapping[job_name]()
    else:
        print(f'ERROR: Command "{job_name}" does not exist; Use job1, job2, job3, job4, or job5.')
else:
    print("Usage: python3 backup.py [job#]")