import requests 
from bs4 import BeautifulSoup

#Url to the jobsite (using tottal job as an examples)
url =  'https://www.totaljobs.com/jobs/in-london'

r = requests.get(url)

#print(r)

# parsing the html to beautiful soup
html_soup= BeautifulSoup(r.content, 'html.parser')

# Targeting the jobs container
job_details = html_soup.find('div', class_='ResultsContainer-sc-1rtv0xy-2')

# Pulling out the needed tags
job_titles =job_details.find_all(['h2','li','dl'])

company_name =job_details.find_all('div', class_='sc-fzoiQi')

total_job_info = job_titles + company_name

# Printing out the content of the tags

for job_title in total_job_info:
    print(job_title.text)






