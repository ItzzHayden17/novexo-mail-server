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
            email['from'] = "no-reply@novexo.co.za" #from the website name
            email['to'] = website['go_to_email_address'] #to the email address
            email['subject'] = f"You have a new message from your website {website['website_name']}" #subject of the email

            data_from_fe = request.form.to_dict() #getting the data from the frontend
            name_fe = data_from_fe['name']
            email_fe = data_from_fe['email']
            message_fe = data_from_fe['message']
            number_fe = data_from_fe['number']

            email.set_content(f"Name: {name_fe}\nEmail: {email_fe}\nMessage: {message_fe} \nNumber: {number_fe}") #content of the email

            try:
                with smtplib.SMTP_SSL(host="mail21.domains.co.za", port=465) as smtp:  # Use SMTP_SSL for port 465
                    smtp.login("no-reply@novexo.co.za", "eA@0vmw%K&SP")  # Login with your credentials
                    smtp.send_message(email)  # Send the email
                    return redirect(website["website_url"])
                print("Email sent successfully!")
            except Exception as e:
                print(f"Failed to send email: {e}")
        


if __name__ == '__main__':
    app.run(debug=True)