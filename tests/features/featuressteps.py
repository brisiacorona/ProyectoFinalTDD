
[1;37mFeature: Generating envents and testing login                       [1;30m# features/esenario.feature:1[0m

[1;37m  Scenario: Login                                                   [1;30m# features/esenario.feature:3[0m
[0;33m    Given:  Open page: http://127.0.0.1:5000/appointments           [1;30m# features/esenario.feature:4[0m
[0;33m    When: Inser email: "moon.prinsses@hotmail.com"                  [1;30m# features/esenario.feature:5[0m
[0;33m    And: Insert password: "mayra"                                   [1;30m# features/esenario.feature:6[0m
[0;33m    Then: The user log                                              [1;30m# features/esenario.feature:7[0m

[1;37m  Scenario: Create Appoiment                                        [1;30m# features/esenario.feature:9[0m
[0;33m    Given: The user is log                                          [1;30m# features/esenario.feature:10[0m
[0;33m    When: Insert a tittle of meeting: "Cita con alejandro"          [1;30m# features/esenario.feature:11[0m
[0;33m    And: Insert a start: "2013-10-11 17:30:00"                      [1;30m# features/esenario.feature:12[0m
[0;33m    And: Insert a end: "2013-10-11 20:00:00"                        [1;30m# features/esenario.feature:13[0m
[0;33m    And: Check allday: "true"                                       [1;30m# features/esenario.feature:14[0m
[0;33m    And: Insert a Location: "Description"                           [1;30m# features/esenario.feature:15[0m
[0;33m    Adn: Insert a description: "Hablar de los avances del proyecto" [1;30m# features/esenario.feature:16[0m
[0;33m    Adn: Submit the button save                                     [1;30m# features/esenario.feature:17[0m
[0;33m    Then: The meeting is success                                    [1;30m# features/esenario.feature:18[0m

[1;37m  Scenario: Edit Appoiment                                          [1;30m# features/esenario.feature:21[0m
[0;33m    Given: Stay in edit template                                    [1;30m# features/esenario.feature:22[0m
[0;33m    when: Update data Chedule id title: "CIta con el viejo"         [1;30m# features/esenario.feature:23[0m
[0;33m    When: Insert a tittle of meeting: "Cita con alejandro"          [1;30m# features/esenario.feature:11[0m
[0;33m    And: Insert a start: "2013-10-11 17:30:00"                      [1;30m# features/esenario.feature:12[0m
[0;33m    And: Insert a end: "2013-10-11 20:00:00"                        [1;30m# features/esenario.feature:13[0m
[0;33m    And: Check allday: "true"                                       [1;30m# features/esenario.feature:14[0m
[0;33m    And: Insert a Location: "Description"                           [1;30m# features/esenario.feature:15[0m
[0;33m    Adn: Insert a description: "Hablar de los avances del proyecto" [1;30m# features/esenario.feature:16[0m
[0;33m    Adn: Submit the button save                                     [1;30m# features/esenario.feature:17[0m
[0;33m    And: All fields are !none                                       [1;30m# features/esenario.feature:31[0m
[0;33m    Then: The edit is success                                       [1;30m# features/esenario.feature:32[0m

[1;37m  Scenario: Delete Appoiment                                        [1;30m# features/esenario.feature:34[0m
[0;33m    Given: Stay in delete template                                  [1;30m# features/esenario.feature:35[0m
[0;33m    when: Delete data Chedule id title: "Cita con el viejo"         [1;30m# features/esenario.feature:36[0m
[0;33m    Adn: Submit the button delete                                   [1;30m# features/esenario.feature:37[0m
[0;33m    And: All fields are delete                                      [1;30m# features/esenario.feature:38[0m
[0;33m    Then: The edit is success                                       [1;30m# features/esenario.feature:32[0m

[1;37m  Scenario: Consult Appoiment                                       [1;30m# features/esenario.feature:41[0m
[0;33m    Given: Stay in delete template                                  [1;30m# features/esenario.feature:35[0m
[0;33m    when: Delete data Chedule id title: "Cita con el viejo"         [1;30m# features/esenario.feature:36[0m
[0;33m    Adn: Submit the button delete                                   [1;30m# features/esenario.feature:37[0m
[0;33m    And: All fields are delete                                      [1;30m# features/esenario.feature:38[0m
[0;33m    Then: The edit is success                                       [1;30m# features/esenario.feature:32[0m

[1;37m  Scenario: List appoitments                                        [1;30m# features/esenario.feature:48[0m
[0;33m    Given: Open page "http://127.0.0.1/appointments/"               [1;30m# features/esenario.feature:49[0m
[0;33m    Then: You can see all appoitments "Cita con el viejo"           [1;30m# features/esenario.feature:50[0m

[1;37m1 feature ([0;31m0 passed[1;37m)[0m
[1;37m6 scenarios ([0;31m0 passed[1;37m)[0m
[1;37m36 steps ([0;33m36 undefined[1;37m, [1;32m0 passed[1;37m)[0m

[0;33mYou can implement step definitions for undefined steps with these snippets:

# -*- coding: utf-8 -*-
from lettuce import step

@step(u'Given:  Open page: http://127.0.0.1:5000/appointments')
def given_open_page_http_127_0_0_1_5000_appointments(step):
    assert False, 'This step must be implemented'
@step(u'When: Inser email: "([^"]*)"')
def when_inser_email_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'And: Insert password: "([^"]*)"')
def and_insert_password_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'Then: The user log')
def then_the_user_log(step):
    assert False, 'This step must be implemented'
@step(u'Given: The user is log')
def given_the_user_is_log(step):
    assert False, 'This step must be implemented'
@step(u'When: Insert a tittle of meeting: "([^"]*)"')
def when_insert_a_tittle_of_meeting_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'And: Insert a start: "([^"]*)"')
def and_insert_a_start_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'And: Insert a end: "([^"]*)"')
def and_insert_a_end_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'And: Check allday: "([^"]*)"')
def and_check_allday_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'And: Insert a Location: "([^"]*)"')
def and_insert_a_location_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'Adn: Insert a description: "([^"]*)"')
def adn_insert_a_description_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'Adn: Submit the button save')
def adn_submit_the_button_save(step):
    assert False, 'This step must be implemented'
@step(u'Then: The meeting is success')
def then_the_meeting_is_success(step):
    assert False, 'This step must be implemented'
@step(u'Given: Stay in edit template')
def given_stay_in_edit_template(step):
    assert False, 'This step must be implemented'
@step(u'when: Update data Chedule id title: "([^"]*)"')
def when_update_data_chedule_id_title_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'And: All fields are !none')
def and_all_fields_are_none(step):
    assert False, 'This step must be implemented'
@step(u'Then: The edit is success')
def then_the_edit_is_success(step):
    assert False, 'This step must be implemented'
@step(u'Given: Stay in delete template')
def given_stay_in_delete_template(step):
    assert False, 'This step must be implemented'
@step(u'when: Delete data Chedule id title: "([^"]*)"')
def when_delete_data_chedule_id_title_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'Adn: Submit the button delete')
def adn_submit_the_button_delete(step):
    assert False, 'This step must be implemented'
@step(u'And: All fields are delete')
def and_all_fields_are_delete(step):
    assert False, 'This step must be implemented'
@step(u'Given: Open page "([^"]*)"')
def given_open_page_group1(step, group1):
    assert False, 'This step must be implemented'
@step(u'Then: You can see all appoitments "([^"]*)"')
def then_you_can_see_all_appoitments_group1(step, group1):
    assert False, 'This step must be implemented'[0m
