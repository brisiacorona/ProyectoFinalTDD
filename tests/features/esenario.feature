Feature: Generating envents and testing login 

Scenario: Login
  Given:  Open page: http://127.0.0.1:5000/appointments
  When: Insert email: "moon.prinsses@hotmail.com"
  And: Insert password: "mayra"
  Then: The user log

Scenario: Create Appoiment
  Given: The user is log
  When: Insert a tittle of meeting: "Cita con alejandro"
  And: Insert a start: "2013-10-11 17:30:00"
  And: Insert a end: "2013-10-11 20:00:00"
  And: Check allday: "true"
  And: Insert a Location: "Description"
  Adn: Insert a description: "Hablar de los avances del proyecto"
  Adn: Submit the button save
  Then: The meeting is success


Scenario: Edit Appoiment
  Given: Stay in edit template
  when: Update data Chedule id title: "CIta con el viejo"
  When: Insert a tittle of meeting: "Cita con alejandro"
  And: Insert a start: "2013-10-11 17:30:00"
  And: Insert a end: "2013-10-11 20:00:00"
  And: Check allday: "true"
  And: Insert a Location: "Description"
  Adn: Insert a description: "Hablar de los avances del proyecto"
  Adn: Submit the button save
  And: All fields are !none
  Then: The edit is success

Scenario: Delete Appoiment
  Given: Stay in delete template
  when: Delete data Chedule id title: "Cita con el viejo"
  Adn: Submit the button delete
  And: All fields are delete
  Then: The edit is success

Scenario: Consult Appoiment
  Given: Stay in delete template
  when: Delete data Chedule id title: "Cita con el viejo"
  Adn: Submit the button delete
  And: All fields are delete
  Then: The edit is success

Scenario: List appoitments
  Given: Open page "http://127.0.0.1/appointments/"
  Then: You can see all appoitments "Cita con el viejo"