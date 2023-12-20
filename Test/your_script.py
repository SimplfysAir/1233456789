# your_script.py
import requests
from googlesearch import search

def get_official_link(company_name):
    query = f"{company_name} official site"
    for link in search(query, num=1, stop=1, pause=2):
        return link

if __name__ == "__main__":
    company_name = input("Enter the company name: ")
    official_link = get_official_link(company_name)
    print(f"The official site of {company_name} is: {official_link}")
