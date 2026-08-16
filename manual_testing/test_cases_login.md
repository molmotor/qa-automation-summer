# Manual Test Cases — Login Page
**Site under test:** https://the-internet.herokuapp.com/login
**Valid credentials:** username `tomsmith`, password `SuperSecretPassword!`

| Test ID | Steps | Expected Result | Actual Result | Pass/Fail |
|---------|-------|------------------|----------------|-----------|
| TC00 | Type "tomsmith" under username & "SuperSecretPassword!" under password, then click "Login" | Get login successful and next page loading | Logged in secure area | Pass |
| TC01 | Type "TomSmith" under username & "SuperSecretPassword!" under password, then click "Login" | Get login successful and next page loading | Your username is invalid! | Fail |
| TC02 | Type "tomsmith" under username & leave blank under password, then click "Login" | Your Password is invalid! | Your Password is invalid! | Pass |
| TC03 | Leave blank under username & "SuperSecretPassword!" under password, then click "Login" | Your Username is invalid! | Your Username is Invalid! | Pass |
| TC04 | Type "tomsmith " under username (trailing space) & "SuperSecretPassword!" under password, then click "Login" | Get login successful and next page loading | Your username is invalid! | Fail |
| TC05 | Leave both username and password blank, then click "Login" | Your username is invalid! | Your username is invalid! | Pass |
| TC06 | Type "tomsmith" under username & "supersecretpassword!" (wrong case) under password, then click "Login" | Your password is invalid! | Your password is invalid! | Pass |
| TC07 | Type "tomsmith" under username & "SuperSecretPassword! " (trailing space) under password, then click "Login" | Get login successful and next page loading | Your password is invalid! | Fail |
| TC08 | Type `' OR '1'='1` under username & "SuperSecretPassword!" under password, then click "Login" | Your username is invalid! (no SQL injection bypass) | Your username is invalid! | Pass |
| TC09 | Type `<script>alert(1)</script>` under username & any password, then click "Login" | Your username is invalid!, no script executes | Your username is invalid!, no alert triggered | Pass |
| TC10 | Without logging in, navigate directly to `/secure` URL | Redirected to login page with a "must login" message | "You must login to view the secure area!" | Pass |
| TC11 | Log in successfully, then click "Logout" on the secure page | Returned to login page with logout confirmation | "You logged out of the secure area!" | Pass |
| TC12 | Log in, log out, then click the browser's Back button | Should not show secure content again; requires re-login | Secure page displayed again — "You logged into a secure area!" — without re-authenticating | Fail |
| TC13 | Type a very long string (1000+ characters) under username & "SuperSecretPassword!" under password, then click "Login" | Your username is invalid!, no crash or error page | Your username is invalid! | Pass |
| TC14 | Type " tomsmith" (leading space) under username & "SuperSecretPassword!" under password, then click "Login" | Get login successful and next page loading | Your username is invalid! | Fail |

