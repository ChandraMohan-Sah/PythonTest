# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time

# print("[INFO] Launching Chrome browser...")
# driver = webdriver.Chrome()

# print("[INFO] Navigating to Nepali Paisa SARBTM page...")
# driver.get("https://nepalipaisa.com/company/SARBTM")

# # Wait for JavaScript to load the content
# print("[INFO] Waiting for the page to fully load...")
# time.sleep(5)

# print("[INFO] Parsing page source with BeautifulSoup...")
# soup = BeautifulSoup(driver.page_source, 'lxml')

# print("[INFO] Locating the data table...")
# table = soup.find('table', class_='table')
# if table:
#     print("[INFO] Table found.")
# else:
#     print("[ERROR] Could not find the table. Exiting.")
#     driver.quit()
#     exit()

# tbody = table.find('tbody')
# if tbody:
#     print("[INFO] Extracting table rows...")
# else:
#     print("[ERROR] Could not find the tbody in the table.")
#     driver.quit()
#     exit()

# for index, row in enumerate(tbody.find_all('tr'), start=1):
#     cols = [td.text.strip() for td in row.find_all('td')]
#     print(f"[ROW {index}] {cols}")

# print("[INFO] Closing browser...")
# driver.quit()
# print("[INFO] Done.")

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

print("[INFO] Launching Chrome browser...")
driver = webdriver.Chrome()

print("[INFO] Navigating to Nepali Paisa SARBTM page...")
driver.get("https://nepalipaisa.com/company/SARBTM")

# Wait for JavaScript to load the content
print("[INFO] Waiting for the page to fully load...")
time.sleep(5)

print("[INFO] Parsing page source with BeautifulSoup...")
soup = BeautifulSoup(driver.page_source, 'lxml')

print("[INFO] Locating the data table...")
table = soup.find('table', class_='table')
if table:
    print("[INFO] Table found.")
else:
    print("[ERROR] Could not find the table. Exiting.")
    driver.quit()
    exit()

tbody = table.find('tbody')
# After finding tbody
if tbody:
    rows = tbody.find_all('tr')
    if rows:
        print("[INFO] Extracting table rows...")
        data_rows = []
        for index, row in enumerate(rows, start=1):
            cols = [td.text.strip() for td in row.find_all('td')]
            print(f"[ROW {index}] {cols}")
            data_rows.append(cols)
        
        # Save to CSV
        csv_file = 'sarbtm_data.csv'
        print(f"[INFO] Saving data to {csv_file} ...")
        with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(data_rows)
    else:
        print("[WARN] No <tr> rows found in <tbody>.")
else:
    print("[ERROR] Could not find the tbody in the table.")

for index, row in enumerate(tbody.find_all('tr'), start=1):
    cols = [td.text.strip() for td in row.find_all('td')]
    print(f"[ROW {index}] {cols}")

print("[INFO] Closing browser...")
driver.quit()
print("[INFO] Done.")
