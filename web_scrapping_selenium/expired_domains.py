from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.common.keys import Keys # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import time
import csv

# Login credentials
username = "username"
password = "contraseña"

# Initialize the WebDriver
driver = webdriver.Chrome()

# Number of pages to scrape
page_limit = 1000

def get_table_data():
    """Extract data from the table and return it as a list of lists."""
    wait = WebDriverWait(driver, 20)
    try:
        # Wait until the table is present
        table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "base1")))
        rows = table.find_elements(By.TAG_NAME, "tr")

        data = []
        for row in rows[1:]:  # Skip the header row
            cols = row.find_elements(By.TAG_NAME, "td")
            row_data = [col.text for col in cols]
            data.append(row_data)
        return data
    except Exception as e:
        print(f"An error occurred while extracting the table: {e}")
        return []

try:
    # Navigate to the login page
    driver.get("https://www.expireddomains.net/login/")

    # Wait for the login fields to be present
    wait = WebDriverWait(driver, 20)
    username_field = wait.until(EC.presence_of_element_located((By.ID, "inputLogin")))
    password_field = driver.find_element(By.ID, "inputPassword")

    # Enter credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for the session to be active and redirected
    wait.until(EC.url_contains("member.expireddomains.net"))

    # Navigate to the expired domains page
    driver.get("https://member.expireddomains.net/domains/expiredcom/")

    all_data = []
    start = 0
    while start <= page_limit:
        # Extract data from the table on the current page
        data = get_table_data()
        if not data:
            break
        all_data.extend(data)

        # Move to the next page
        start += 25
        next_url = f"https://member.expireddomains.net/domains/expiredcom/?start={start}"
        
        # Wait before loading the next page
        time.sleep(10)  # Wait for 10 seconds to avoid hitting request limits
        
        driver.get(next_url)

        # Wait for the new page to fully load
        try:
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "base1")))
        except Exception as e:
            print(f"Could not load the page {next_url}. Stopping search.")
            break

    # Save the collected data to a CSV file
    with open('/expired_domains.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(all_data)

    print("Data extracted and saved to expired_domains.csv.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    time.sleep(5)  # Wait for 5 seconds before closing to see the results
    driver.quit()
