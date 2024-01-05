# # job_scrape_dev api key = wYWlE1pHJzlbUpIeCtsh46iWu29mg9z1PeSWiJDYFL1gniTatqQ025ZsPdwPeATW
from src import scrape_jobs

jobs = scrape_jobs(
    site_name=["linkedin"],
    search_term="software engineer",
    location="PUNE",
    results_wanted=2,
    country_indeed='india'  # only needed for indeed / glassdoor
)

print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("jobs.csv", index=False) # to_xlsx