from scrape import scrape
from compare import compare_jobs
from repeater import schedule_job
from emailer import send_email
from openai_filter import filter_jobs
from datetime import datetime

oldJobList = []

current_date = datetime.now().date()
formatted_date = datetime.now().strftime("%B %d, %Y")

def check_new_jobs():
    global oldJobList
    
    print("Checking for new jobs...\n")
    
    try:
        newJobList = scrape()
        if not newJobList:
            print("\nNo jobs were scraped. Please check the scrape function.")
            return
        
        addedJobs = compare_jobs(oldJobList, newJobList)
        
        if addedJobs:
            print("\nNew jobs found!\n")
            output = []
            for idx, job in enumerate(addedJobs, start=1):
                job_title = job['title']
                job_url = list(job['href'])[0] if job['href'] else "No URL found"
                job_info = f"{idx}. Title: {job_title}, URL: {job_url}"
                output.append(job_info)
            
            job_list_str = "\n".join(output)
            
            # Filter jobs
            filtered_jobs = filter_jobs(job_list_str)
            
            if filtered_jobs:
                print(f"\nFiltered Jobs:\n{filtered_jobs}")
                
                email_body = filtered_jobs
                subject = "New Job Alerts " + formatted_date
                to_email = "sample-emailgmail.com" 
                from_email = "sample-email@gmail.com" 
                password = "sample-password"
                
                send_email(subject, email_body, to_email, from_email, password)
                
                oldJobList = newJobList
            else:
                print("\nNo jobs matched the filter criteria.")
        else:
            print("\nNo new jobs found.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

check_new_jobs()

schedule_job(check_new_jobs, "11:31")
