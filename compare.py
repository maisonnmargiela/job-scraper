def compare_jobs(oldJobList, newJobList):
    try:
        addedJobs = []

        oldJobSet = {(job['title'], tuple(job['href'])) for job in oldJobList}

        for job in newJobList:
            job_tuple = (job['title'], tuple(job['href']))

            if job_tuple not in oldJobSet:
                addedJobs.append(job)

        return addedJobs
    except Exception as e:
        print(f"Error in compare_jobs: {e}")
        return []
