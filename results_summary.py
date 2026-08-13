results = [
       {"test_name": "login_valid", "status": "pass"},
       {"test_name": "login_wrong_password", "status": "fail"},
       {"test_name": "login_has_space", "status": "fail"},
       {"test_name": "login_wrong", "status": "fail"},
       {"test_name": "login_valid_password_valid", "status": "pass"},
   ]

passed = 0
failed = 0
for result in results:
    if result["status"] == "pass":
        passed += 1
    else:
        failed += 1

print(passed,"passed,",failed,"failed." )