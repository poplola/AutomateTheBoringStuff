# import webbrowser, request
# webbrowser.open('https://inventwithpython.com/')

# # ========== Downloading a Web Page with the requests.get() Function ==========
# import requests
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(res))
# print(res.status_code == requests.codes.ok, res.status_code)
# print(len(res.text))
# print(res.text[:250])

# import requests
# res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# print(res.status_code)
# res.raise_for_status
# print(res.raise_for_status)

# # ========== Checking for Errors ==========
# import requests
# res = requests.get('https://inventwithpython.com/page_that_does_not_exist') 
# try:
#     res.raise_for_status() 
# except Exception as exc:
#     print('There was a problem: %s' % (exc))

# # ========== SAVING DOWNLOADED FILES TO THE HARD DRIVE ==========
# import requests
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# res.raise_for_status()
# playFile = open('RomeoAndJuliet.txt', 'wb')
# for chunk in res.iter_content(100000):
# 	playFile.write(chunk)
# playFile.close()


# # TODO: Download the image.
# print(f"Downloading image {comicUrl}")
# res = requests.get(comicUrl)
# res.raise_for_status

# # Save the image to ./xkcd.
# imageFile = open(os.path.join(downloadFolder, os.path.basename(comicUrl)), 'wb')

# for chunk in res.iter_content(10000): 
#     imageFile.write(chunk)
# imageFile.close()


# from selenium import webdriver
# browser = webdriver.Safari()
# url = "https://inventwithpython.com"
# browser.get(url)
# try:
#     elem = browser.find_element_by_class_name('display-3')
#     # elem = browser.find_element_by_tag_name('display-3')
#     print('Found <%s> element with that class name!' % (elem.tag_name)) 
# except:
#     print('Was not able to find an element with that name.')
# # browser.close()

# l = [1, 2, 2, 1, 5, 9, 2, 5]
# nl = str(list(set(l)))
# print(nl)