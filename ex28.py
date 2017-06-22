True and True | True | # ok
False and True | False | # ok
1 == 1 and 2 == 1 | True and False | False # ok
"test" == "test" | True # ok
1 == 1 or 2 != 1 | True # ok
True and 1 == 1 | True # ok
False and 0 != 0 | False # ok
True or 1 == 1 | True # ok
"test" == "testing"| False # ok
1 != 0 and 2 == 1 | True and False | False # ok
"test" != "testing" | True # ok
"test" == 1 | False # ok
not (True and False) | True # ok
not (1 == 1 and 0 != 1) | not (True and True) | False # ok
not (10 == 1 or 1000 == 1000) | not (False or True) | False # my was True # ups
not (1 != 10 or 3 == 4) | not (True or False) | False # oka
not ("testing" == "testing" and "Zed" == "Cool Guy") | not (True and False) | True # ok
1 == 1 and (not ("testing" == 1 or 1 == 0)) | True and (not (False or False)) | True and True | True # ok
"chunky" == "bacon" and (not(3 == 4 or 3 == 3)) | False and (not (False or True)) | False and True | False # ok
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) | True and (not (True or False)) | True and False | False # ok 
