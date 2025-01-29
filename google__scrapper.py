from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def google_search(query):
    """
    Function to perform a Google search using Selenium and print the first 10 search results.
    """
    # Set up the Selenium WebDriver (Ensure ChromeDriver is installed)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    options.add_argument("--disable-gpu")  # Disable GPU for better performance
    options.add_argument("--no-sandbox")  # Bypass OS security model (useful in some environments)
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources in Docker/Linux
    
    driver = webdriver.Chrome(options=options)

    try:
        # Open Google Search
        driver.get("https://www.google.com")

        # Accept Cookies (if prompted)
        try:
            consent_button = driver.find_element(By.XPATH, "//button[contains(text(),'Accept all')]")
            consent_button.click()
            time.sleep(1)
        except:
            pass  # No cookie prompt, continue
        
        # Find the search bar and enter the query
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        time.sleep(2)  # Allow time for results to load

        # Extract search result titles and links
        results = driver.find_elements(By.CSS_SELECTOR, "h3")

        print(f"\nTop 10 search results for '{query}':\n")
        for index, result in enumerate(results[:10]):  # Limit to first 10 results
            try:
                title = result.text
                link = result.find_element(By.XPATH, "./ancestor::a").get_attribute("href")
                print(f"{index + 1}. {title}\n   {link}\n")
            except:
                continue  # Skip results without valid links
        
    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()

# Example usage
if __name__ == "__main__":
    search_query = input("Enter your search query: ")
    google_search(search_query)
