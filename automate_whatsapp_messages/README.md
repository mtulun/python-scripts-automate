# Step 1: Install pywhatkit
Open up terminal and run the following command.

```bash
pip install pywhatkit
```
You can check out all the dependencies this library installed with the command pip list.


# Step 2: Send a message to someone on WhatsApp
Log in to your WhatsApp account through WhatsApp Web.
To send a message to a WhatsApp contact with Python and pywhatkit, we use the .sendwhatmsg method as shown in the code below (insert your contact number instead).
import pywhatkit

## syntax: phone number with country code, message, hour and minutes

```bash
pywhatkit.sendwhatmsg('+91xxxxxxxx', 'Your Message', 12, 01)
````

This code means it will send ‘Your Message’ to contact X at “12:01”. Now run this code and you will see a message like this —
In 10 seconds, web.WhatsApp.com will open, and after 15 seconds, a message will be delivered by Whatsapp.
Great!! You have successfuly sent a message using python.


# Step 3: Send a message to a group on WhatsApp
We can also send messages to a specific group on WhatsApp, but first, we have to get the group link.
Once you have the link of the group, we have to use the .sendwhatmsg_to_group method. This method is similar to the one we used in step 2, but now we insert a group link.

```bash
import pywhatkit
#syntax: group link, message, hour and minutes
pywhatkit.sendwhatmsg_to_group("group-link", "Your Message", 12, 01)
```