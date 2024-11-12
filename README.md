Job Scraper

A Python-based automation tool that scrapes job listings from specified websites, filters jobs based on education requirements, and sends email notifications for new job postings. This tool is designed to run on a daily schedule, either locally or via AWS Lambda.

---

Features

- **Web Scraping**: Scrapes job postings from a predefined job listing website.
- **Job Comparison**: Compares current job postings with previous ones to identify new postings.
- **Job Filtering**: Uses OpenAI to filter jobs based on education requirements (college degree or not).
- **Email Notifications**: Sends an email with the filtered job listings.
- **Daily Scheduling**: The program can be scheduled to run daily using Python's scheduling libraries or AWS Lambda.

---

Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

Follow the steps below to set up the project locally:

1. Clone the repository**:
   ```bash
   git clone https://github.com/your-username/job-scraper-notifier.git
   cd job-scraper-notifier
2. Install (using pip install) all requirements in the requirements.txt file
