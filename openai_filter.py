# openai_filter.py
import os
import openai
import dotenv

openai.api_key = 'sample-key'

def filter_jobs(job_list):
    # Prepare the prompt for job filtering
    
    prompt = f"Sort this job list into jobs that do not require a college education (can be anything lower than college) and jobs that require a college education. List the jobs with title as well as URLs in their original format without embedding them. Display each job as: Title: Example Job Title, URL: https://example.com without adding any square brackets or 'Apply Here' text.\n{job_list}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": prompt}],
        max_tokens=1500,
        temperature=0.2
    )
    
    # Retrieve and return the filtered job list
    return response.choices[0].message['content'].strip()
