BDD_Castle_Hill_Gaming
This is repository contain files for Swag Labs Login demo test 
The scenarios which are check are as follows 

Scenario:Successful Login
 Given I am on the Sauce Demo Login Page
 When I fill the account information for account StandardUser into the Username field and the Password field
 And I click the Login Button
 Then I am redirected to the Sauce Demo Main Page
 And I verify the App Logo exist

Scenario: Failed Login
 Given I am on the Sauce Demo Login Page
 When I fill the account information for account LockedOutUser into the Username field and the Password field
 And I click the Login Button
 Then I verify the Error Message contains the text "Sorry, this user has been banned."

Instruction to Run 
1.	Download this repository 
2.	Run the bat file in command prompt 
3.	Test run and reports are stored in report folder 
4.	Go to the report folder and open index.html in browser 
5.	Failure screenshot is placed in the Failurescreenshot folder
