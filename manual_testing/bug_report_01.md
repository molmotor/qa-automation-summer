## White Space Case

### Steps to Reproduce:
- Type "tomsmith " (make sure to add the white space) under username 
- Type "SuperSecretPassword!" under password
- Click Login

### Expected Result:
Login successful and moved to secure area

### Actual Result:
Your username is invalid!

### Sevirity:
Low, they will probably try again and possibly get it right, maybe they'll give up and call support, a whitespace in username doesnt pose a security risk, and should be treated as the correct username, But for Password, it should be whitespace sensitive

Regards, molmotor