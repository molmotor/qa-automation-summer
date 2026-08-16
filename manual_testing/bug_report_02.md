# TC12 Bug Report

# Steps to Reproduce
  Type "tomsmith" in username field, Type "SuperSecretPassword!" in passowrd, click Login button, Click Logout, then click the Browser's Back Button

# Expected Result
  Clicking Login should take you to Secure Area (success), Logout should take you back to login page, back button should keep you in login page, requiring re entry of username and password

# Actual Result
   Clicking Login takes you to Secure Area (success), Logout takes you back to login page, back button re takes you to Secure Area, without the need of re entring username/password. Refreshing the cached secure-are page after using the Back Button redirects to the login page, confirming no active session presists


# Severity
  medium, for shared computers, if the client leaves their computer at work or something, an intruder could gain access to the secure area in the name of the actual owner. and while its only visual, meaning no changes/interactions can be made, but there may be some sensitive information saved in the cache, which still poses risk to the security of the user