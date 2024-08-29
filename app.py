
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
url = "(https://Microsoft Copilot.com)"

# Send a GET request
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all articles on the page
articles = soup.find_all("article", class_="blog-post")

# Create lists to store data
titles = []
authors = []
dates = []
summaries = []

# Loop through each article
for article in articles:
    # Extract title
    title = article.find("h2", class_="title").text.strip()
    titles.append(title)
    
    # Extract author
    author = article.find("span", class_="author").text.strip()
    authors.append(author)
    
    # Extract date
    date = article.find("span", class_="date").text.strip()
    dates.append(date)
    
    # Extract summary
    summary = article.find("div", class_="summary").text.strip()
    summaries.append(summary)

# Create a pandas DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Author": authors,
    "Date": dates,
    "Summary": summaries
})

# Save to CSV
df.to_csv("scraped_data.csv", index=False)
 
