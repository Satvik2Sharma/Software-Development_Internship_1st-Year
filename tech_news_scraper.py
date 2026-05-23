# 🌐 TECH NEWS WEB SCRAPER
# Internship Task 6
# 👨‍💻 Developed by: Satvik Sharma

import requests
from bs4 import BeautifulSoup
print("""
========================================
🌐 TECH NEWS WEB SCRAPER
========================================
""")
url = "https://news.ycombinator.com/"
try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all("span", class_="titleline")
    print("\n📰 TOP TECH HEADLINES\n")
    for index, headline in enumerate(headlines[:10], start=1):
        title = headline.get_text()
        print(f"{index}️⃣ {title}")
    print("\n✅ Web scraping completed successfully!\n")
except Exception as e:
    print(f"\n❌ Error occurred: {e}\n")
