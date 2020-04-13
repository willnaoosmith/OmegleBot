# coding: utf-8

from selenium import webdriver
import time

textToSend = """
i'm a bot, beep bop
"""

browser = webdriver.Firefox(executable_path='/home/user/desktop/geckodriver')

browser.get('https://www.omegle.com')
browser.maximize_window()
time.sleep(3)

ChatButton = browser.find_element_by_id('textbtn').click()
time.sleep(2)

alreadySent = False
LastAnswer = False

while True:
	try:
		content = browser.page_source
		Disconnected = content.find('Stranger has disconnected')
		Disconnected2 = content.find('You have disconnected')
		IsAnswered = content.find('Stranger:')

		if Disconnected != -1 or Disconnected2 != 1:
			DisconnectButton = browser.find_element_by_class_name("disconnectbtn").click()
			time.sleep(2)
			alreadySent = False
			print("Conversation Ended")

		else:

			if alreadySent == False:
				TextBox = browser.find_element_by_class_name("chatmsg")
				TextBox.send_keys(textToSend)
				time.sleep(1)
				SendButton = browser.find_element_by_class_name("sendbtn").click()
				alreadySent = True
				print("Conversation Started")

			else:
						
				if IsAnswered != -1:

					query = browser.find_elements_by_class_name("strangermsg")
					answer = query[-1].find_element_by_tag_name("span")

					if LastAnswer != answer.text:

						print(answer.text)
						LastAnswer = answer.text

					else:
						pass

					time.sleep(2)

				else:
					pass
	except:
		pass
