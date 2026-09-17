from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os

load_dotenv()

account_email = os.getenv("ACCOUNT_EMAIL")
account_password = os.getenv("ACCOUNT_PASSWORD")
URL = "https://appbrewery.github.io/gym/"

# Chrome setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Explicit wait
wait = WebDriverWait(driver, 10)

# Login
login_button = driver.find_element(By.ID, value="login-button")
login_button.click()
email = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
email.send_keys(account_email)
password = wait.until(EC.presence_of_element_located((By.ID, "password-input")))
password.send_keys(account_password)
submit_button = wait.until(EC.presence_of_element_located((By.ID, "submit-button")))
submit_button.click()
wait.until(EC.url_contains("/gym/schedule/"))
print("Successfully logged in!")
print("Current URL:", driver.current_url)

# Counters
classes_booked = 0
waitlists_joined = 0
already_booked_waitlisted = 0
total_processed = 0
class_results = []

# Find all day groups
day_groups = driver.find_elements(By.CSS_SELECTOR, "div[id^='day-group-']")
for day_group in day_groups:
    day_title = day_group.find_element(By.CSS_SELECTOR, "h2[id^='day-title-']")
    print("DAY:", day_title.text)

    # Only process Tuesday and Thursday
    if "Tue" in day_title.text or "Thu" in day_title.text:
        class_cards = day_group.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

        for class_card in class_cards:
            class_time = class_card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']")
            print("TIME:", class_time.text)

            # Only process 6 PM classes
            if "6:00 PM" in class_time.text:
                total_processed += 1
                
                button = class_card.find_element(By.TAG_NAME, "button")
                button_text = button.text
                class_name = class_card.text.splitlines()[0]
                
                if button_text == "Booked":
                    already_booked_waitlisted += 1
                    class_results.append(f"[Already Booked] {class_name} on {day_title.text}")
                    print("✓ Already booked:", class_name)

                elif button_text == "Waitlisted":
                    already_booked_waitlisted += 1
                    class_results.append(f"[Already Waitlisted] {class_name} on {day_title.text}")
                    print("✓ Already on waitlist:", class_name)

                elif button_text == "Join Waitlist":
                    button.click()
                    waitlists_joined += 1
                    class_results.append(f"[New Waitlist] {class_name} on {day_title.text}")
                    print("✓ Joined waitlist for:", class_name)

                elif button_text == "Book Class":
                    button.click()
                    classes_booked += 1
                    class_results.append(f"[New Booking] {class_name} on {day_title.text}")
                    print("✓ Booked:", class_name)    

# Booking summary
print("\n--- BOOKING SUMMARY ---")
print("Classes booked:", classes_booked)
print("Waitlists joined:", waitlists_joined)
print("Already booked/waitlisted:", already_booked_waitlisted)
print("Total Tuesday & Thursday 6pm classes:", total_processed)
print("\n--- DETAILED CLASS LIST ---")
for result in class_results:
    print("•", result)

# Verify bookings
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")
driver.get(URL + "my-bookings/")
wait.until(EC.url_contains("my-bookings"))
verified_bookings = []
for result in class_results:
    try:
        class_name = result.split("] ")[1].split(" on ")[0]
        booking = driver.find_element(By.XPATH, f"//*[contains(text(), '{class_name}')]")
        verified_bookings.append(class_name)
        if "Waitlist" in result:
            print(f"✓ Verified: {class_name} (Waitlist)")
        else:
            print(f"✓ Verified: {class_name}")
    except NoSuchElementException:
        print(f"Not found: {class_name}")

# Compare expected vs actual
print("\n--- VERIFICATION RESULT ---")
expected = len(class_results)
found = len(verified_bookings)
print("Expected:", expected, "bookings")
print("Found:", found, "bookings")
if expected == found:
    print("SUCCESS: All bookings verified!")
else:
    print("MISMATCH: Missing", expected - found, "bookings")