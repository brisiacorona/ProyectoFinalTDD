# -*- coding: utf-8 -*-
from lettuce import *
from lettuce_webdriver.util import AssertContextManager
from lettuce import step
from datetime import datetime
from selenium import webdriver


@before.all
def setup_browser():
    world.browser = webdriver.Firefox()


@after.all
def close_browser(total):
    world.browser.quit()


def find_field_by_class(browser, attribute):
    xpath = "//input[@class='%s']" % attribute
    elems = browser.find_elements_by_xpath(xpath)
    return elems[0] if elems else False


@step(u'Given: Enter the URL "([^"]*)"')
def given_enter_the_url_group1(step, url):
    world.response = world.browser.get(url)


@step(u'When: Data entry field "([^"]*)" with "([^"]*)"')
def when_data_entry_field_group1_with_group2(step, field_id, value):
    with AssertContextManager(step):
        text_field = world.browser.find_element_by_id(field_id)
        text_field.clear()
        text_field.send_keys(value)


@step(u'And: Data entry field "([^"]*)" with "([^"]*)"')
def and_data_entry_field_group1_with_group2(step, field_id, value):
    with AssertContextManager(step):
        text_field = world.browser.find_element_by_id(field_id)
        text_field.clear()
        text_field.send_keys(value)


@step(u'And: Click the button submit')
def and_click_the_button_submit(step):
    with AssertContextManager(step):
        form = world.browser.find_element_by_class_name('form-horizontal')
        form.submit()


@step(u'Then: You can see "(.*?)" contains "(.*?)"')
def element_contains(step, element_class, value):
    with AssertContextManager(step):
        element = world.browser.find_element_by_class_name(element_class)
        assert (value in element.text), "Got %s, %s " % (element.text, value)


@step(u'Then: You can see error "([^"]*)"')
def then_you_can_see_group1(step, title):
	with AssertContextManager(step):
		element = world.browser.find_element_by_tag_name('h2')
		assert title == element.text, "Got %s " % element.text


@step(u'When: You update the field "([^"]*)" with "([^"]*)"')
def when_you_update_the_field_group1_with_group2(step, field_id, value):
    with AssertContextManager(step):
        text_field = world.browser.find_element_by_id(field_id)
        text_field.clear()
        text_field.send_keys(value)

fechaActual = datetime.now().strftime("%Y-%m-%d %l:%M:%S")
fechaActualComparacion = datetime.now().strftime("%Y-%m-%d")


@step(u'Then: You can see that the element with class "([^"]*)" contains "([^"]*)"')
def then_you_can_see_that_the_element_with_class_group1_contains_group2(step, element_class, title):
    with AssertContextManager(step):
        elements = world.browser.find_elements_by_class_name(element_class)
        lst = []
        for e in elements:
            lst.append(e.text)
        assert title not in lst


@step(u'When: You update the field "([^"]*)" with actual date')
def when_you_update_the_field_group1_with_actual_date(step, field_id):
    with AssertContextManager(step):
        text_field = world.browser.find_element_by_id(field_id)
        text_field.clear()
        text_field.send_keys(fechaActual)


@step(u'Then: You can see that the element with class "([^"]*)" contains the actual date')
def then_you_can_see_that_the_element_with_class_group1_contains_the_actual_date(step, element_class):
    with AssertContextManager(step):
        element = world.browser.find_element_by_class_name(element_class)
        assert fechaActualComparacion in element.text, "Got %s " % element.text


@step(u'Then I see at least "([^"]*)" appoitments with the class "([^"]*)"')
def then_i_see_two_appoitments(step, num, element_class):
    with AssertContextManager(step):
        elements = world.browser.find_elements_by_class_name(element_class)
        assert len(elements) > int(num)


@step(u'When: You can select the appointment with the title "([^"]*)"')
def when_you_can_select_the_appointment_with_the_title_group1(step, title):
    with AssertContextManager(step):
        element = world.browser.find_element_by_link_text(title)
        element.click()


@step(u'And: You can do click in the button "([^"]*)"')
def and_you_can_do_click_in_the_button_group1(step, field_class):
    with AssertContextManager(step):
        button = world.browser.find_element_by_class_name(field_class)
        button.click()


@step(u'And: Enter the URL "([^"]*)"')
def and_enter_the_url_group1(step, url):
    world.response = world.browser.get(url)


@step(u'Then: You can see that the element with the class "([^"]*)" not contains "([^"]*)"')
def then_you_can_see_that_the_element_with_the_class_group1_not_contains_group2(step, element_class, title):
    with AssertContextManager(step):
        elements = world.browser.find_elements_by_class_name(element_class)
        lst = []
        for e in elements:
            lst.append(e.text)
        assert title not in lst
