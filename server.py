from flask import Flask,render_template,request,jsonify,redirect
import smtplib
from email.message import EmailMessage

app = Flask(__name__)




website_mail_list = [
    {
        "id":1,
        "website_name": "Novexo",
        "website_url": "https://itzzhayden17.github.io/novexo/",
        "go_to_email_address" : "anray743@gmail.com"
    }
]


@app.route('/')
def home():
    return "Server active"

@app.route('/submit-email/<int:website_id>', methods=['POST'])
def submit_email(website_id):
    for website in website_mail_list:
        if website['id'] == website_id:

            email = EmailMessage() #creating an email object
            email['from'] = website['website_name'] #from the website name
            email['to'] = website['go_to_email_address'] #to the email address
            email['subject'] = f"You have a new message from your website {website['website_name']}" #subject of the email

            data_from_fe = request.form.to_dict() #getting the data from the frontend
            name_fe = data_from_fe['name']
            email_fe = data_from_fe['email']
            message_fe = data_from_fe['message']

            email.set_content(f"Name: {name_fe}\nEmail: {email_fe}\nMessage: {message_fe}") #content of the email

            with smtplib.SMTP(host="smtp.gmail.com",port=587) as smtp: #usual stuff for sending over Gmail
                smtp.ehlo() #tells gmail this is a server
                smtp.starttls() #starts encryption
                smtp.login("sony.anray743@gmail.com","nyrn pfuh reqz yomc")
                smtp.send_message(email) 
                return redirect(website['website_url']) #redirects to the website
        
    return jsonify({"error": f"Website with ID {website_id} not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)