### How to use: ###
 1. Clone this repository.
 2. Create a `.env` file in your local repository.
 3. Update this `.env` file with your email and app password as mentioned below. Remember, this email address will be used to send all the mails.
 ```
EMAIL="YOUR EMAIL GOES HERE"
PASSWORD="THE APP PASSWORD GMAIL GENERATES FOR YOU GOES HERE"
 ```
4. Open the `Template` folder, you will see a `template.html` file there, you may replace it with the template of your choice. To insert variables in the template use `${variable}` this syntax.
5. These variables are passed from the `main.py` file as key value pairs. The application is using `mako template` for inserting variables.
6. If you have images included in your html template, make sure you host them somewhere and update the `src` of each `img` with the correct url. Local URLs won't work when you will send the mails.
7. Open `sheet.xlsx`. The first column by default expects EMAILS and the second column by default expects NAME. You can modify the code and get it done your way. Don't include any headers.
8. You're all set. Execute the python file and start sending the mails.

### Setting up Gmail ###
- Open your GMAIL Account.
- Go to `Manage your google account`.
- Look for 2 step verification and enable it by following the instructions.
- After enabling the 2 step verification, again go to `Manage your google account`, right below `2 step verification` you will find `App password`.
- Click on `App password`, then select `Mail` and `Windows Computer` and proceed.
- It will provide you with a password, use this password inside the `.env` file.