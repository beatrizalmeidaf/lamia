from bs4 import BeautifulSoup
import requests
import re
import time

print('Put some skill that you are not familiar with')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text.strip()
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('div', class_='srp-skills').text.strip()
            more_info = job.header.h2.a['href']
            
            if unfamiliar_skill not in skills:
                with open(f'jobs/{index}.txt', 'w') as f:
                # substitui múltiplos espaços ou tabulações por um único espaço
                    company_name = re.sub(r'\s+', ' ', company_name)
                    skills = re.sub(r'\s+', ' ', skills)
            
                    f.write(f"Company: {company_name}\nSkills: {skills}\nPublished: {published_date}\nMore info: {more_info}\n\n")
                print(f'File saved: {index}')


if  __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)