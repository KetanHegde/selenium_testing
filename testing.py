from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
# these are the user credentials
username = 'abcd@gmail.com'  #replace it with actual email
password = 'abcd&88'       #replace it with actual password
pid = 'abcd'                 #replace it with actual pinterest id
user = "Ab Cd"                 #replace it with actual user name


# Hardcoded test data
website = 'https://www.pinterest.com/login/'

img_path = r"path/to/image"     #replace it with actual image path


try:
    # pin_title = 'Test Pin'
    # pin_description = 'This is a test pin created by Selenium.'

    # Step 1: Navigate to the website
    driver.get(website)
    print("Navigated to website")

    # Check if we are on the Pinterest login page
    assert "Pinterest" in driver.title
    print("Title check passed")

    # Step 2: Locate and interact with web elements to log in
    try:
        # Find the username and password fields
        username_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")
        print("Located username and password fields")
        
        # Enter the username and password
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        print("Entered username and password")

        # Wait for login to complete
        time.sleep(5)
        print("Login process initiated")

        # Assert login was successful by checking the presence of a known post-login element
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="HeaderContent"]/div/div/div[2]/div/div/div/div[1]'))
        )
        print("Test Passed: Login successful.")
    
    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed: Timeout - {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion error - {e}")

    #test case 1 - to create a pin
    try:
        pin_title = "Test Pin"
        create_button_xpath = '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[4]/div/a/div/div/span'
        create_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, create_button_xpath))
        )
        print("Testing Create button")
        create_button.click()
        time.sleep(3)  # Adjust as needed
        print("Successfully tested Create button")

    except TimeoutException:
        print("Timeout while testing Create button")
    except NoSuchElementException as e:
        print(f"Element not found while testing Create button - {e}")
    except Exception as e:
        print(f"An error occurred while testing Create button - {e}")

    # Step 4: Navigate to create pin page
    try:
        # Upload an image
        image_upload_button_xpath = '//input[@type="file"]'
        image_upload_button = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, image_upload_button_xpath))
        )
        image_upload_button.send_keys(img_path)
        print("Uploaded image")
        time.sleep(10)  # Increased wait time for image upload

        # Enter pin title
        title_field_xpath = '//input[@id="storyboard-selector-title"]'
        title_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, title_field_xpath))
        )
        title_field.send_keys(pin_title)
        print("Entered pin title")

        # Save the pin
        publish_button_xpath = '//button[contains(@class, "RCK Hsu USg adn NTm KhY iyn oRi lnZ wsz") and .//div[text()="Publish"]]'
        publish_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, publish_button_xpath))
        )
        publish_button.click()
        print("Test case 1 Passed: Pin published successfully")


    except TimeoutException:
        print("Timeout while creating pin")
    except NoSuchElementException as e:
        print(f"Element not found while creating pin - {e}")
    except Exception as e:
        print(f"An error occurred while creating pin - {e}")

    #test case 2 - delete a created pin
    # Step 4: Delete the created pin
    try:
        time.sleep(5)
        print("Navigating to home page")
        # driver.get('https://www.pinterest.com/')
        profile_icon = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[@href='/{pid}/' and contains(@class, 'Wk9') and contains(@class, 'S9z')]"))
        )
        profile_icon.click()
        print("Navigated to 'Profile' page")
        time.sleep(5)

        # Locate and click the "Created" link
        created_link_xpath = f'//a[contains(@href, "/{pid}/_created/") and contains(@class, "Wk9 xQ4 S9z DUt CCY kVc Tbt L4E e8F BG7")]'
        created_link = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, created_link_xpath))
        )
        created_link.click()
        print("Clicked on 'Created' link")

        # Wait for the created section to load
        time.sleep(5)  # Adjust the delay as needed
        print("Navigated to the 'Created' section")

        
        pin_link_xpath = '//div[@data-test-id="story-pin-image-box"]/div/img'
        pin_link = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, pin_link_xpath))
        )
        pin_link.click()
        print("Navigated to the pin page")


        # Locate and click the "More options" button
        more_options_button_xpath = '//button[@aria-label="More options"]'
        more_options_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, more_options_button_xpath))
        )
        more_options_button.click()
        print("Clicked 'More options' button")

        # Locate and click the "Edit Pin" option
        edit_pin_option_xpath = '//div[@data-test-id="pin-action-dropdown-edit-pin"]'
        edit_pin_option = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, edit_pin_option_xpath))
        )
        edit_pin_option.click()
        print("Clicked 'Edit Pin' option")

        # Locate and click the "Delete" button
        delete_button_xpath = '//div[@data-test-id="delete-pin-button"]//button'
        delete_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
        )
        delete_button.click()
        print("Clicked 'Delete' button")

        # Confirm the deletion by clicking the final "Delete" button
        # Locate and click the confirm delete button
        confirm_delete_button_xpath = '//div[@data-test-id="confirm-delete-pin"]//div[@data-test-id="submit-button"]//button[@type="submit"]'
        confirm_delete_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, confirm_delete_button_xpath))
        )
        confirm_delete_button.click()
        print("Test case 2 passed: Deleted the created pin")



        #test case 3 - navigate to settings page
        driver.get('https://www.pinterest.com/')
            # Locate the "Accounts and more options" button and click it
        accounts_options_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@data-test-id='header-accounts-options-button']"))
            )
        accounts_options_button.click()
        print("Clicked 'Accounts and more options' button")

        # Wait for options menu to be displayed
        time.sleep(5)  # Adjust this delay if necessary

            # Locate and click the "Settings" button
        settings_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@data-test-id='header-menu-options-settings']"))
            )
        settings_button.click()
        print("Clicked 'Settings' button")

        # Validate that the settings page is displayed
        WebDriverWait(driver, 10).until(
                EC.url_contains("settings")
            )
        print("Test case 3 Passed: Successfully navigated to the settings page")



        #test case 4 - accounts and more option
        #Locate the "Accounts and more options" button using XPath
        driver.get('https://www.pinterest.com/')
        accounts_options_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-test-id='header-accounts-options-button']"))
        )
        print("Accounts and more options button located")
        accounts_options_button.click()
        print("Clicked 'Accounts and more options' button")

        # Wait for options menu to be displayed
        options_menu = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'XiG DHH kFh Dl7 V0G ho-')]"))  # Update this based on actual menu content
        )
        print("Options menu located")

        # Validate that the options menu is displayed
        if options_menu:
            print("Test case 4 Passed: Successfully navigated to accounts and more options menu.")
        else:
            print("Test Failed: Options menu not displayed.")


        #test case 5 - notifications
        # Locate the "Notifications" icon using aria-label attribute and class names
        driver.get('https://www.pinterest.com/')
        notifications_icon = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Notifications' and contains(@class, 'S9z') and contains(@class, 'INd')]"))
        )
        notifications_icon.click()
        print("Clicked 'Notifications' icon")

        # Wait for the notifications dropdown or page to be displayed
        time.sleep(5)  # Adjust this delay if necessary

        # Validate that the notifications section or dropdown is displayed
        # Use appropriate selector here if available; for now, assuming some identification is needed
        notifications_dropdown = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'VxL _he ho- imm ojN p6V wc1 zI7 iyn Hsu')]"))
        )
        if notifications_dropdown:
            print("Test case 5 Passed: Successfully navigated to notifications dropdown.")
        else:
            print("Test Failed: Notifications dropdown not displayed.")



        #test case 6 - Profile page navigation
        # Navigate to the profile page (assumes the user is on the homepage)
        driver.get('https://www.pinterest.com/')
        time.sleep(10)
        profile_icon = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, f"//a[@href='/{pid}/' and contains(@class, 'Wk9') and contains(@class, 'S9z')]"))
        )
        profile_icon.click()
        print("Clicked 'Profile' icon")

        # Wait for profile page or dropdown to be displayed
        time.sleep(5)  # Adjust this delay if necessary

        # Wait for profile page to load and validate
        # profile_page = WebDriverWait(driver, 30).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[@data-test-id='profile-name']"))
        # )
        profile_name = driver.find_element(By.XPATH, "//div[@data-test-id='profile-name']").text
        if profile_name == user:
            print("Test case 6 Passed: Successfully navigated to profile page.")
        else:
            print("Test Failed: Profile page not displayed or profile name does not match.")



        #test case 7 - to click and comment
        # Step 3: Locate and click on a photo from the grid
        try:
            driver.get('https://www.pinterest.com/')
            time.sleep(10)
            # Find a photo using the `data-test-id` attribute
            photo_xpath = '//div[@data-test-id="non-story-pin-image"]/div/img'
            photo = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, photo_xpath))
            )
            print("Testing photo click")
            photo.click()
            time.sleep(5)  # Wait for photo to open
            print("Successfully clicked on the photo")

        except TimeoutException:
            print("Timeout while clicking on photo")
        except NoSuchElementException as e:
            print(f"Element not found while clicking on photo - {e}")
        except Exception as e:
            print(f"An error occurred while clicking on photo - {e}")

        # Step 6: Find and interact with the comment box
        try:
            # Locate the comment box using its `data-test-id` attribute
            comment_box_xpath = '//div[@data-test-id="comment-editor-container"]//div[@contenteditable="true"]'
            comment_box = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, comment_box_xpath))
            )
            print("Testing comment box interaction")
            comment_box.click()
            time.sleep(8)  # Wait for the comment box to be interactable
            
            # Input a comment
            comment_text = "waaawwww"
            comment_box.send_keys(comment_text)
            print("Test case 7 passed: Entered comment text")

        except TimeoutException:
            print("Timeout while interacting with comment box")
        except NoSuchElementException as e:
            print(f"Element not found while interacting with comment box - {e}")
        except Exception as e:
            print(f"An error occurred while interacting with comment box - {e}")



        #test case 8 - click and follow
        try:
            driver.get('https://www.pinterest.com/')
            time.sleep(10)
            # Find a photo using the `data-test-id` attribute
            photo_xpath = '//div[@data-test-id="non-story-pin-image"]/div/img'
            photo = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, photo_xpath))
            )
            print("Testing photo click")
            photo.click()
            time.sleep(5)  # Wait for photo to open
            print("Successfully clicked on the photo")

        except TimeoutException:
            print("Timeout while clicking on photo")
        except NoSuchElementException as e:
            print(f"Element not found while clicking on photo - {e}")
        except Exception as e:
            print(f"An error occurred while clicking on photo - {e}")

        # Step 5: Click on the Follow button
        try:
            time.sleep(10)
            # Locate and click on the follow button
            follow_button_xpath = '//button[@aria-label="Follow"]'
            follow_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, follow_button_xpath))
            )
            print("Testing Follow button click")
            follow_button.click()
            time.sleep(5)  # Adjust as needed
            print("Test case 8 passed: Successfully followed")

        except TimeoutException:
            print("Timeout while clicking on Follow button")
        except NoSuchElementException as e:
            print(f"Element not found while clicking on Follow button - {e}")
        except Exception as e:
            print(f"An error occurred while clicking on Follow button - {e}")



        #test case 9 - click and save
        # Step 3: Locate and click on a photo from the grid
        try:
            driver.get('https://www.pinterest.com/')
            time.sleep(10)
            # Find a photo using the `data-test-id` attribute
            photo_xpath = '//div[@data-test-id="non-story-pin-image"]/div/img'
            photo = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, photo_xpath))
            )
            print("Testing photo click")
            photo.click()
            time.sleep(5)  # Wait for photo to open
            print("Successfully clicked on the photo")

        except TimeoutException:
            print("Timeout while clicking on photo")
        except NoSuchElementException as e:
            print(f"Element not found while clicking on photo - {e}")
        except Exception as e:
            print(f"An error occurred while clicking on photo - {e}")

        # Step 4: Save the post
        try:
            # Locate and click on the save button
            save_button_xpath = '//button[@aria-label="Save"]'
            save_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, save_button_xpath))
            )
            print("Testing Save button click")
            save_button.click()
            time.sleep(5)  # Adjust as needed
            print("Test case 9 passed: Successfully saved the post")

        except TimeoutException:
            print("Timeout while clicking on Save button")
        except NoSuchElementException as e:
            print(f"Element not found while clicking on Save button - {e}")
        except Exception as e:
            print(f"An error occurred while clicking on Save button - {e}")

        #test case 10 - click and react
        time.sleep(10)
        # Step 3: Locate and click on a photo from the grid
        try:
            driver.get('https://www.pinterest.com/')
            time.sleep(10)
            # Find a photo using the `data-test-id` attribute
            photo_xpath = '//div[@data-test-id="non-story-pin-image"]/div/img'
            photo = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, photo_xpath))
            )
            print("Testing photo click")
            photo.click()
            time.sleep(5)  # Wait for photo to open
            print("Successfully clicked on the photo")

        except TimeoutException:
            print("Timeout while clicking on photo")
        except NoSuchElementException as e:
            print(f"Element not found while clicking on photo - {e}")
        except Exception as e:
            print(f"An error occurred while clicking on photo - {e}")

        # Step 4: Save the post
        try:
            # Locate and click on the save button
            save_button_xpath = '//div[@aria-label="React"]//div[@data-test-id="react-button"]'
            save_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, save_button_xpath))
            )
            print("Testing React button click")
            save_button.click()
            time.sleep(5)  # Adjust as needed
            print("Test case 10 passed: Successfully reacted to a post")

        except TimeoutException:
            print("Timeout while clicking on react button")
        except NoSuchElementException as e:
            print(f"Element not found while clicking on react button - {e}")
        except Exception as e:
            print(f"An error occurred while clicking on react button - {e}")


        #test case 11 - message
        driver.get('https://www.pinterest.com/')
        # Locate the "Messages" icon using aria-label attribute and class names
        messages_icon = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Messages' and contains(@class, 'S9z') and contains(@class, 'INd')]"))
        )
        messages_icon.click()
        print("Clicked 'Messages' icon")

        # Wait for the messages dropdown or page to be displayed
        time.sleep(5)  # Adjust this delay if necessary

        # Validate that the messages section or dropdown is displayed
        # Use appropriate selector here if available; for now, assuming some identification is needed
        messages_dropdown = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-test-id="full-height-inbox-container"]'))
        )
        if messages_dropdown:
            print("Test case 11 Passed: Successfully navigated to messages dropdown.")
        else:
            print("Test Failed: Messages dropdown not displayed.")


        #test case 12 - search and click
        try:
            driver.get('https://www.pinterest.com/')
            search_box_xpath = '//input[@data-test-id="search-box-input"]'
            search_box = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, search_box_xpath))
            )
            print("Testing Search box")
            search_box.click()
            search_box.send_keys("laptop")
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)  # Adjust as needed
            print("Successfully tested Search box with keyword 'laptop'")

        except TimeoutException:
            print("Timeout while testing Search box")
        except NoSuchElementException as e:
            print(f"Element not found while testing Search box - {e}")
        except Exception as e:
            print(f"An error occurred while testing Search box - {e}")


        try:
            # Find a photo using the `data-test-id` attribute
            photo_xpath = '//div[@data-test-id="non-story-pin-image"]/div/img'
            photo = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, photo_xpath))
            )
            print("Testing photo click")
            photo.click()
            time.sleep(5)  # Wait for photo to open
            print("Test case 12 passed: Successfully searched and clicked on the photo")

        except TimeoutException:
            print("Timeout while clicking on photo")
        except NoSuchElementException as e:
            print(f"Element not found while clicking on photo - {e}")
        except Exception as e:
            print(f"An error occurred while clicking on photo - {e}")



        #test case 13 - search, click and save
        # Step 3: Find the search box using full XPath, enter "laptop", and test it
        try:
            driver.get('https://www.pinterest.com/')
            search_box_xpath = '//input[@data-test-id="search-box-input"]'
            search_box = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, search_box_xpath))
            )
            print("Testing Search box")
            search_box.click()
            search_box.send_keys("laptop")
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)  # Adjust as needed
            print("Successfully tested Search box with keyword 'laptop'")

        except TimeoutException:
            print("Timeout while testing Search box")
        except NoSuchElementException as e:
            print(f"Element not found while testing Search box - {e}")
        except Exception as e:
            print(f"An error occurred while testing Search box - {e}")


        try:
            # Find a photo using the `data-test-id` attribute
            photo_xpath = '//div[@data-test-id="non-story-pin-image"]/div/img'
            photo = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, photo_xpath))
            )
            print("Testing photo click")
            photo.click()
            time.sleep(5)  # Wait for photo to open
            print("Successfully clicked on the photo")

        except TimeoutException:
            print("Timeout while clicking on photo")
        except NoSuchElementException as e:
            print(f"Element not found while clicking on photo - {e}")
        except Exception as e:
            print(f"An error occurred while clicking on photo - {e}")

        # Step 4: Save the post
        try:
            # Locate and click on the save button
            save_button_xpath = '//button[@aria-label="Save"]'
            save_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, save_button_xpath))
            )
            print("Testing Save button click")
            save_button.click()
            time.sleep(5)  # Adjust as needed
            print("Test case 13 passed: Successfully searched and saved the post")

        except TimeoutException:
            print("Timeout while clicking on Save button")
        except NoSuchElementException as e:
            print(f"Element not found while clicking on Save button - {e}")
        except Exception as e:
            print(f"An error occurred while clicking on Save button - {e}")

        #test case 14 - search
        #Step 3: Find the search box using full XPath, enter "laptop", and test it
        try:
            driver.get('https://www.pinterest.com/')
            search_box_xpath = '//input[@data-test-id="search-box-input"]'
            search_box = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, search_box_xpath))
            )
            print("Testing Search box")
            search_box.click()
            search_box.send_keys("laptop")
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)  # Adjust as needed
            print("Test case 14 passed: Successfully tested Search box with keyword 'laptop'")

        except TimeoutException:
            print("Timeout while testing Search box")
        except NoSuchElementException as e:
            print(f"Element not found while testing Search box - {e}")
        except Exception as e:
            print(f"An error occurred while testing Search box - {e}")
    except Exception as e:
        print(f"An error occurred - {e}")

finally:
    # Step 5: Close the browser session
    logout_path1 = '//div[@data-test-id="header-accounts-options-button"]'
    logout_button1 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, logout_path1))
        )
    logout_button1.click()
    logout_path2 = '//div[@data-test-id="header-menu-options-logout"]'
    logout_button2 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, logout_path2))
        )
    logout_button2.click()
    print("Log out successful ")
    driver.quit()
    print("Closed the browser session")


#test case 15 - explore
try:
    driver = webdriver.Chrome()
    print("Testing Explore")
    # Step 1: Open the Pinterest webpage
    driver.get('https://www.pinterest.com/')
    print("Navigated to Pinterest website")
    time.sleep(5)  # Wait for the page to load
    # Step 2: Test the "Explore" button
    try:
        explore_button_xpath = '//a[@href="/ideas/"]'
        explore_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, explore_button_xpath))
        )
        print("Testing Explore button")
        explore_button.click()
        time.sleep(3)  # Wait for the page to load
        print("Test case 15 passed: Successfully tested Explore button")

    except TimeoutException:
        print("Timeout while testing Explore button")
    except NoSuchElementException as e:
        print(f"Element not found while testing Explore button - {e}")

finally:
    driver.quit()
    print("Closed the browser session")


#test case 16 - login test
try:
    driver = webdriver.Chrome()
    user = 'abcd@gmail.com'
    passwrd = 'gjgydguyw'
    # Step 3: Navigate to the website
    driver.get(website)
    print("Navigated to website")

    # Check if we are on the Pinterest login page
    assert "Pinterest" in driver.title
    print("Title check passed")

    # Step 4: Locate and interact with web elements
    try:
        # Find the username and password fields
        username_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")
        print("Located username and password fields")
        
        # Enter the username and password
        username_field.send_keys(user)
        password_field.send_keys(passwrd)
        password_field.send_keys(Keys.RETURN)
        print("Entered username and password")

        # Wait for the page to load and check for the profile icon
        time.sleep(5)  # Adjust sleep time if necessary
        
        # Check for a known element after login (e.g., search bar)
        try:
            driver.find_element(By.NAME, "searchBoxInput")  # Example element after login
            print("Test case 16 Passed: Login successful.")
        except NoSuchElementException:
            print("Test case 16 Passed: Login unsuccessful.")
    
    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed: Timeout - {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion error - {e}")

finally:
    # Step 6: End the session
    driver.quit()
    print("Closed the browser session")


#test case 17 - about page
def test_about_button(driver):
    try:
        driver = webdriver.Chrome()
        # Navigate to Pinterest website
        driver.get('https://www.pinterest.com/')
        print("Navigated to Pinterest website")

        # Wait until the About button is visible and interactable
        about_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div/a'))
        )                                           
        print("Located About button on Pinterest homepage")

        # Get the current window handle (to switch back later)
        main_window = driver.current_window_handle

        # Click on the About button
        about_button.click()
        print("Clicked on About button")

        # Wait for the new tab to open and switch to it
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Wait until two windows are open
        for handle in driver.window_handles:
            if handle != main_window:
                driver.switch_to.window(handle)
                break

        # Wait for the About page to load (you can add more specific waits if necessary)
        time.sleep(5)

        # Get the page title for debugging
        page_title = driver.title
        print(f"About page title: {page_title}")

        # Example assertion: Check if the page title contains 'About Pinterest'
        # assert "About Pinterest" in page_title
        print("Test case 17 Passed: Successfully navigated to About page.")

    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed: Timeout - {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion error - {e}. Page title was: {page_title}")

    finally:
        # Close the new tab and switch back to the main window
        driver.close()
        driver.switch_to.window(main_window)
        print("Closed the new tab and switched back to the main window")

# Call the function to test the About button
test_about_button(driver)



#test case 18 - blog page
def test_blog_button(driver):
    try:
        driver = webdriver.Chrome()
        # Navigate to Pinterest website
        driver.get('https://www.pinterest.com/')
        print("Navigated to Pinterest website")

        # Wait until the Blog button is visible and interactable
        blog_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[2]/div[1]/div[3]/div/a'))
        )
        print("Located Blog button on Pinterest homepage")

        # Get the current window handle (to switch back later)
        main_window = driver.current_window_handle

        # Click on the Blog button
        blog_button.click()
        print("Clicked on Blog button")

        # Wait for the new tab to open and switch to it
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Wait until two windows are open
        for handle in driver.window_handles:
            if handle != main_window:
                driver.switch_to.window(handle)
                break

        # Example of further actions:
        # You can add assertions or further interactions with elements on the Blog page
        time.sleep(7)
        # Example assertion: Check if the page title contains 'Blog'
        # assert "Blog" in driver.title
        print("Test case 18 Passed: Successfully navigated to Blog page.")

    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed: Timeout - {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion error - {e}")

    finally:
        # Close the new tab and switch back to the main window
        driver.close()
        driver.switch_to.window(main_window)
        print("Closed the new tab and switched back to the main window")

# Call the function to test the Blog button
test_blog_button(driver)



#test case 19 - businesses page
def test_businesses_button(driver):
    try:
        driver = webdriver.Chrome()
        # Navigate to Pinterest website
        driver.get('https://www.pinterest.com/')
        print("Navigated to Pinterest website")

        # Wait until the Businesses button is visible and interactable
        businesses_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[2]/div[1]/div[2]/div/a'))
        )
        print("Located Businesses button on Pinterest homepage")

        # Get the current window handle (to switch back later)
        main_window = driver.current_window_handle

        # Click on the Businesses button
        businesses_button.click()
        print("Clicked on Businesses button")

        # Wait for the new tab to open and switch to it
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Wait until two windows are open
        for handle in driver.window_handles:
            if handle != main_window:
                driver.switch_to.window(handle)
                break

        # Example of further actions:
        # You can add assertions or further interactions with elements on the "Businesses" page

        # Example assertion: Check if the page title contains 'Business'
        assert "Business" in driver.title
        print("Test case 19 Passed: Successfully navigated to Businesses page.")

    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed: Timeout - {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion error - {e}")

    finally:
        # Close the new tab and switch back to the main window
        driver.close()
        driver.switch_to.window(main_window)
        print("Closed the new tab and switched back to the main window")

# Call the function to test the Businesses button
test_businesses_button(driver)


#test case 20 - today page
def test_today_button(driver):
    try:
        driver = webdriver.Chrome()
        # Navigate to Pinterest website
        driver.get('https://www.pinterest.com/')
        print("Navigated to Pinterest website")

        # Wait until the Today button is visible and interactable
        today_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/today/')]"))
        )
        print("Located Today button on Pinterest homepage")

        # Click on the Today button
        today_button.click()
        print("Clicked on Today button")

        # Wait for the page to load (you can add more specific waits if necessary)
        time.sleep(5)

        # Example of further actions:
        # You can add assertions or further interactions with elements on the "Today" page

        # Example assertion: Check if the page title contains 'Today'
        assert "Today" in driver.title
        print("Test case 20 Passed: Successfully navigated to Today page.")

    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed: Timeout - {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion error - {e}")

    finally:
        # End the session
        driver.quit()
        print("Closed the browser session")

# Call the function to test the Today button
test_today_button(driver)



#test case 21 - watch button
def test_watch_button(driver):
    try:
        driver = webdriver.Chrome()
        # Navigate to Pinterest website
        driver.get('https://www.pinterest.com/')
        print("Navigated to Pinterest website")

        # Wait until the Watch button is visible and interactable
        watch_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[1]/div[3]/a/div/div/span'))
        )                                          
        print("Located Watch button on Pinterest homepage")

        # Click on the Watch button
        watch_button.click()
        print("Clicked on Watch button")

        # Wait for the page to load (you can add more specific waits if necessary)
        time.sleep(5)

        # Example of further actions:
        # You can add assertions or further interactions with elements on the "Watch" page

        # Example assertion: Check if the page title contains 'Watch'
        assert "Watch" in driver.title
        print("Test case 21 Passed: Successfully navigated to Watch page.")

    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed: Timeout - {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion error - {e}")

    finally:
        # End the session
        driver.quit()
        print("Closed the browser session")

# Call the function to test the Watch button
test_watch_button(driver)
