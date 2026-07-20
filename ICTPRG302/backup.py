import sys
from backupcfg import job1, job2, job3, job4

#Maps each job to their definition
job_mapping = {
    "job1": job1,
    "job2": job2,
    "job3": job3,
    "job4": job4
}

#Allows for bash commands to
if len(sys.argv) > 1:
    job_name = sys.argv[1]
    if job_name in job_mapping:
        job_mapping[job_name]()
    else:
        print(f'ERROR: Command "{job_name}" does not exist; Use job1, job2, job3, job4, or job5.')
else:
    print("Usage: python3 backup.py [job#]")
    
#Schedule backups
#Send notification for backup errors