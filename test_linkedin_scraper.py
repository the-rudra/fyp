from src import scrape_jobs

jobs = scrape_jobs(
    site_name=["linkedin"],
    search_term="software engineer",
    location="PUNE",
    results_wanted=10,
    country_indeed='india'  # only needed for indeed / glassdoor
)

print(f"Found {len(jobs)} jobs")
print(jobs.head())
jobs.to_csv("jobs.csv", index=False) # to_xlsx

