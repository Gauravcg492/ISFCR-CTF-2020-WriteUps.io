# Existential Crisis

  + Inspect the page
  + See the alt of the image tag
  + Get the file name
  + Access the file
  + Copy the flag

# Help!!!

 + Open the Webpage
 + Inspect 
 + Find the hidden Link (There are 2 Links - Must warn the participants)
 + Read the flag - (Not too straight forward)
 + CTF{MINDTHEGAP}

# Find ME!!!

+ Go to Site.

+ Method 1
	+ look at robots.txt
	+ Gives you hint to pes website with an apropriate request header
	+ Navigate to the PESU website.
	+ Find the appropriate request to get user data based on SRN's.
	+ Guess the correct SRN.

+ Method 2	[Not the right way but still a pretty impressive method]
	+ Use the scholarship document providied by college
	+ Seach for the name Hatim
	+ Get the correct SRN.

# Efficient Storage
  + Open the Webpage
  + Inspect 
  + Find the hidden Link (There are 2 Links - Must warn the participants)
  + Method 1
  	+ Website Link mentions compression.
  	+ Huffman coding is a commonly used lossless data compression algorithm.
  	+ Use Huffman coding to get the flag.
  	+ <u style = "color:blue">https://www.dcode.fr/huffman-tree-compression</u>

  + Method 2
  	+ Solving by hand.
  	+ Inorder to make the flag easier to get
  	+ The flag was written based on food products.
  	+ Upon decrypting by hand you will arrive at something that looks like 
  		ctf{Ramen_15_better ...
  	+ Based on this people would have a fair idea of what the flag would be and would hence make the mappin easier.

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
	
# Charity is Important