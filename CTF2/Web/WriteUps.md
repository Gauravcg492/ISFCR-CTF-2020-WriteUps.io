# General - Web


## Lebron

* The challenge asks you to Help Lebron.
* Navigate to the help button in the website beneath a set of quotes by lebron
	<img src = "./Files/Lebron.png" alt = "Web Page"/>
* Click the Help button.
* Intercept the request being sent through Burpsuite or by observing the network tab on the browser.
* You may use postman or curl (Any similar tools) to make a request to the webserver.
* Notice the response headers.
	<img src = "./Files/Request.png" alt = "Postman Request"/>
* We can observe a content Location header.
* Sending a get Request to the content-Location (/l3bfl4g) or navigating to the page gives the flag.
	<img src = "./Files/LebFlag.png" alt = "Flag"/>

---

## Elliot Alderson

* The Challenge asks you to befriend Elliot Alderson.
* Once you click the green tick.You will be directed to the below page :
	<img src = "./Files/Elliot.png" alt = "Elliot Challenge"/>
* A classic reference to Mister Robot (TV series).
* Based on the reference you may navigate to the robots.txt page of the website.
	<img src = "./Files/Robot.png" alt = "Robots.txt"/>
* By navigating to the  /.elli0t_fl4g end point you will see some text.
	<img src = "./Files/ElliotFlag.png" alt = "Elliot Flag "/>
* The given text is a JWT token.It can be identified by the three dots injeced inbetween the text.
* Use a JWT online decoder to get the flag.
	<img src = "./Files/JWT.png" alt = "JWT decoder Output"/>
* The given flag field is not of the form CTF{}.
* By noticing the '=' symbol at the end.You man understand that it is base64 encoded.
* Decoding the base64 flag will give you the right flag.
	<img src = "./Files/B64.png" alt = "Base64 decoded Flag"/>

---

## Messi

---

## Nadal

 
---
## Restricted Entry

### Challenge Description

Opening the site tells us that we don't have the authentication to view further. We need to see how the site is authenticating a user to figure out what to do.

### Hint

```
Viewing the source code almost always helps.
```

### Solution

The script tag in the body of the HTML file shows us that it's fetching a local storage item called authKey, and passing it to the atob() function, which used to get plaintext from BASE64, and comparing it to "admin". Therefore, we encode "admin" in Base64 and store it in the local storage key value pair. This gets us the key ***CTF{W3ak_@uth3nt1cat10n}*** 

---

## Message from the Future

### Challenge Description

The site tells us there's a message, but since it's from the future it can only be accessed on an iPhone 30. We need to find out how to access the message

### Hint

```
Again, viewing the source code works.
```

### Solution

The script tag in the body of the HTML file shows us a few things. First, it's setting a cookie called 'userType' to 'normal'. This comes in handy later on. The code then makes a post request to /futuremessage, which we need to emulate. However, since we need to use an iPhone 30, we change the User-Agent header of the request to iPhone 30. This then tells us that we don't have admin privileges to view the code. Inspecting the POST function used in the source code, we can see that one of the headers sent is 'cookie' which passes the site's cookies. The cookie was initially called userType set to normal. When we make the POST request, we set a cookie header, and pass "userType=admin" to emulate being an admin. And voila, you get the key - ***CTF{W3lc0m3_t0_th3_futur3}***

---