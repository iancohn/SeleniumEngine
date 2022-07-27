# Select an option from a dropdown menu
elementIdDropdownMenu = '' # Set this to the element ID of the drop down menu.
tagNameDdOption = 'option' # Set this to the tag name of each option in the drop down
selectOption = '' # Set this to the text of the option you want to select

dropdown = browser.find_elements_by_id(elementIdDropdownMenu)
if len(dropdown) == 0:
  self.output('No dropdown.', verbose_level=2)
  raise ProcessorError('Dropdown not found')
elif len(dropdown) > 1:
  self.output('Multiple dropdowns with id={} exist.'.format(elementIdDropdownMenu))
  raise ProcessorError('Ambiguous dropdown menu selection.')
else:  
  self.output('Dropdown menu found. Continuing')
  for ddOption in dropdown[0].find_elements_by_tag_name(tagNameDdOption):
    self.output('Option text is {}'.format(ddOption.text), verbose_level=3)
    self.output('fnmatch Result: {}'.format(fnmatch.fnmatch(ddOption.text, selectOption)), verbose_level=3)
    if fnmatch.fnmatch(ddOption.text, selectOption) == True:
      self.output('Found match in drop down menu: {}'.format(ddOption.text), verbose_level=2)
      self.output('Selecting option', verbose_level=2)
      ddOption.click()
      break
    else:
      self.output('No Match',verbose_level=3)
      self.output("Option ({}) does not match search term ({}). Continuing.".format(ddOption.text, selectOption), verbose_level=3)
