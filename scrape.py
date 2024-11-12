from requests_html import HTMLSession

def scrape():
    try:
        session = HTMLSession()
        url = 'https://sarkarinaukri.com/category/job-news/railway-jobs/'
        print(f"\nFetching jobs from {url}")
        
        r = session.get(url)
        r.html.render(sleep=1, keep_page=True, scrolldown=1)

        jobs = r.html.find('h3')
        if not jobs:
            print("No jobs found on the page. Please check the HTML structure or the URL.")
        
        jobList = []
        for item in jobs:
            job = {
                'title': item.text,
                'href': item.absolute_links
            }
            if job['href']:  # Check if href is not empty
                jobList.append(job)
        
        return jobList
    except Exception as e:
        print(f"Error in scrape: {e}")
        return []
