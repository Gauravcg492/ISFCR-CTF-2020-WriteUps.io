# Get It!!!

+ Method 1 
	+ Crash the server by passing invalid parameters.
	+ Due to absence of try catch on server side.
	+ Flask code will spill on error logs.
	+ grep the flag or take the flag from error logs.

+ Method 2
	+ Go through the source
	+ Find the Debugging information in the script
	+ Analyse the code snippet to get the id and password
	+ id = armstrong no. of length > 3
	+ password = regex (a)\*bc
	+ Pass the parameters get the request.
	