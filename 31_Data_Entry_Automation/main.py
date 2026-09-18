from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import requests

google_form_url = "https://forms.gle/fSskPQTNFiFug7ZT6"
zillow_clone_url = "https://appbrewery.github.io/Zillow-Clone/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36",
    "Accept-Language": "en-US"
}

# Get the Zillow webpage
response = requests.get(zillow_clone_url, headers=headers)
response.raise_for_status()
website_html = response.text

# Parse the webpage using BeautifulSoup
soup = BeautifulSoup(website_html, "html.parser")

# Extract property addresses
address = soup.find_all(name="address", attrs={"data-test": "property-card-addr"})
property_address = [" ".join(adr.getText().split("|")[0].split()) for adr in address]

# Extract property prices
price = soup.find_all(name="span", attrs={"data-test": "property-card-price"})
property_price = [rate.getText().strip().split("+")[0].split("/")[0] for rate in price]

# Extract property links 
link = soup.find_all(name="a", attrs={"data-test": "property-card-link"})
property_link = list(dict.fromkeys(web_link.get("href") for web_link in link))

# Set up Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(google_form_url)

# Explicit wait
wait = WebDriverWait(driver, 10)

# Click "Submit another response" after each submission
def submit_another_response():
    response = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Submit another response")))
    response.click()
    
# Fill and submit the form for each property
for i in range(len(property_address)):
    inputs = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input[type='text'][aria-disabled='false']")))
    inputs[0].send_keys(property_address[i])
    inputs[1].send_keys(property_price[i])
    inputs[2].send_keys(property_link[i])
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
    submit_button.click()
    submit_another_response()
print("Data entered successfully in the Google Form!")





