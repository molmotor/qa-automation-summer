| Test ID | Steps                                                                                           | Expected Result                          | Actual Result            | Pass/Fail |
|---------|-------------------------------------------------------------------------------------------------|------------------------------------------|--------------------------|-----------|
|TC00     |type "tomsmith" under username & "SuperSecretPassword!" under password, then click "Login" Button|get login successful and next page loading|Logged in secure area     |Pass       |
|TC01     |type "TomSmith" under username & "SuperSecretPassword!" under password, then click "Login" Button|get login successful and next page loading|Your username is invalid! |Fail      |
|TC02     |type "tomsmith" under username & leave blank under password, then click "Login" Button           |Your Password is invalid!                 |Your Password is invalid! |Pass      |
|TC03     |leave blank under username & "SuperSecretPassword!" under password, then click "Login" Button    |Your Username is invalid!                 |Your Username is Invalid! |Pass       |
|TC04     |type "tomsmith " under username & "SuperSecretPassword!" under password, then click "Login" Button|get login successful and next page loading|Your username is invalid!|Fail       |


