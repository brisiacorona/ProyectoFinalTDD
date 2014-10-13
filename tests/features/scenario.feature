Feature: Do appointments

Scenario: Open the page
	Given: Enter the URL "http://127.0.0.1:5000/appointments/"
	When: Data entry field "username" with "moon.prinsses@hotmail.com"
	And: Data entry field "password" with "mayra"
	And: Click the button submit

Scenario: Create new appoitment
	Given: Enter the URL "http://127.0.0.1:5000/appointments/create/"
	When: Data entry field "title" with "Cita con el abogado"
	And: Data entry field "start" with "2010-11-11 12:00:00"
	And: Data entry field "end" with "2010-11-11 13:00:00"
	And: Data entry field "location" with "Rio Grande"
	And: Data entry field "description" with "Notariar el titulo"
	And: Click the button submit

Scenario: Consult appoitment
	Given: Enter the URL "http://127.0.0.1:5000/appointments/2/"
	Then: You can see "appointment-detail" contains "alguna cosa"

Scenario: If the appointments dont exist
	Given: Enter the URL "http://127.0.0.1:5000/appointments/0/"
	Then: You can see error "Not Found"

Scenario: Edit a given appointment
	Given: Enter the URL "http://127.0.0.1:5000/appointments/2/edit"
	When: You update the field "title" with "Nuevo"
	And: Click the button submit
	Then: You can see that the element with class "appointment-detail" contains "Titulo Nuevo"

Scenario: Edit a date given appointment
	Given: Enter the URL "http://127.0.0.1:5000/appointments/2/edit"
	When: You update the field "start" with actual date
	And: Click the button submit
	Then: You can see that the element with class "appointment-detail" contains the actual date

Scenario: List all appoitments
	Given: Enter the URL "http://127.0.0.1:5000/appointments/"
	Then I see at least "2" appoitments with the class "appointment-detail"

Scenario: Delete appoitment
	Given: Enter the URL "http://127.0.0.1:5000/appointments/"
	When: You can select the appointment with the title "cita"
	And: You can do click in the button "appointment-delete-link"
	And: Enter the URL "http://127.0.0.1:5000/appointments/"
	Then: You can see that the element with the class "appointment-detail" not contains "junta importante"