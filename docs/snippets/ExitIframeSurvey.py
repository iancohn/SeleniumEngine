# Detect and decline/exit an iFrame window
#
# modify the variables and place the snippet in a
# CDATA tag as an item in your selenium_options array

elementIdIframe = ''
elementIdExitButton = ''

self.output('Checking to see if there is an iFrame.')
if browser.find_elements_by_id(elementIdIframe) == []:
  self.output('No iFrame detected. Continuing', verbose_level=3)
else:
  self.output('Website has displayed an iFrame... Declining it now.')
  browser.switch_to.frame(browser.find_element_by_id(elementIdIframe))
  browser.find_element_by_id(elementIdExitButton).click()
