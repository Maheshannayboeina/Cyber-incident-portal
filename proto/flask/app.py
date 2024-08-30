from flask import Flask, request, jsonify, render_template
import joblib
app = Flask(__name__)

# Load the machine learning model
model = joblib.load('cyberattack_classifier.pkl')

# Attack details dictionary
attack_details = {
    "financial fraud": {
        "info": "Involves deceitful practices to illegally obtain funds from victims. This includes unauthorized banking transactions, Ponzi schemes, and phishing for financial data.",
        "post_attack_steps": [
            "Immediately report the unauthorized transaction to your bank.",
            "Freeze the affected accounts to prevent further unauthorized use.",
            "Change all associated passwords and security questions.",
            "File a complaint with your local police station or cybercrime police station."
        ],
        "helplines": {
            "Cyber Crime Helpline Number": "1930",
            "National Cyber Crime Reporting Portal": "https://cybercrime.gov.in/",
            "Reserve Bank of India (RBI) Helpline": "14440"
        }
    },
    "social media account hacked": {
        "info": "Unauthorized access and misuse of someone’s social media account, often to spread false information or to scam friends and followers.",
        "post_attack_steps": [
            "Change your password immediately and log out of all other devices.",
            "Enable two-factor authentication for enhanced security.",
            "Notify your friends and followers about the breach.",
            "Use the platform’s built-in recovery process to regain control."
        ],
        "helplines": {
            "National Cyber Crime Reporting Portal": "https://cybercrime.gov.in/",
            "Facebook Help Center": "https://www.facebook.com/help",
            "Twitter Help Center": "https://help.twitter.com",
            "Instagram Help Center": "https://help.instagram.com"
        }
    },
    "identity theft": {
        "info": "Theft of personal information to impersonate someone and carry out fraudulent activities like opening new credit accounts.",
        "post_attack_steps": [
            "Notify banks, financial institutions, and credit bureaus about the theft.",
            "Place a fraud alert on your credit reports.",
            "File an FIR at your local police station.",
            "Monitor your accounts and statements regularly for suspicious activity."
        ],
        "helplines": {
            "Cyber Crime Helpline Number": "1930",
            "National Cyber Crime Reporting Portal": "https://cybercrime.gov.in/"
        }
    },
    "ransomware": {
        "info": "A type of malicious software that encrypts the victim’s data and demands a ransom for its release.",
        "post_attack_steps": [
            "Disconnect the affected device from all networks.",
            "Avoid paying the ransom; instead, seek professional IT assistance.",
            "Report the incident to local law enforcement.",
            "Restore data from backups if available."
        ],
        "helplines": {
            "Cyber Crime Helpline Number": "1930",
            "Indian Computer Emergency Response Team (CERT-In)": "incident@cert-in.org.in"
        }
    },
    "phishing": {
        "info": "Deceptive emails or messages that appear to be from legitimate sources to steal sensitive data like login credentials or financial information.",
        "post_attack_steps": [
            "Do not click on suspicious links or download attachments from unknown sources.",
            "Change passwords for accounts that might have been compromised.",
            "Report the phishing attempt to the relevant platform."
        ],
        "helplines": {
            "National Cyber Crime Reporting Portal": "https://cybercrime.gov.in/"
        }
    },
    "online shopping scam": {
        "info": "Fraudulent e-commerce websites or sellers that deceive customers into paying for goods that are never delivered.",
        "post_attack_steps": [
            "Contact your bank or payment provider to dispute the transaction.",
            "Report the seller or website to consumer protection authorities.",
            "Provide evidence of the scam to help investigations."
        ],
        "helplines": {
            "Cyber Crime Helpline Number": "1930",
            "National Consumer Helpline": "1800-11-4000"
        }
    },
    "malware": {
        "info": "Malicious software designed to damage or disable computers and computer systems, including viruses, worms, and trojan horses.",
        "post_attack_steps": [
            "Run a full system scan using reliable antivirus software.",
            "Remove or quarantine the detected threats.",
            "Update your software and operating system to the latest versions."
        ],
        "helplines": {
            "Indian Computer Emergency Response Team (CERT-In)": "incident@cert-in.org.in"
        }
    },
    "cyberbullying": {
        "info": "Bullying or harassment using digital platforms, often involving threats, spreading lies, or sharing private photos without consent.",
        "post_attack_steps": [
            "Document and save evidence of the cyberbullying.",
            "Block the bully on all platforms and report their behavior.",
            "Seek support from friends, family, or professional counseling."
        ],
        "helplines": {
            "National Cyber Crime Reporting Portal": "https://cybercrime.gov.in/",
            "Local Police Station": "Contact your local police"
        }
    },
    "social engineering": {
        "info": "Manipulating people into giving up confidential information, often by pretending to be a trustworthy individual.",
        "post_attack_steps": [
            "Be cautious of unsolicited requests for personal information.",
            "Verify the identity of the person or organization before sharing sensitive data.",
            "Educate yourself and others on common social engineering tactics."
        ],
        "helplines": {
            "Cyber Crime Helpline Number": "1930",
            "National Cyber Crime Reporting Portal": "https://cybercrime.gov.in/"
        }
    },
    "vishing": {
        "info": "Voice phishing attacks that trick victims into revealing personal information over the phone.",
        "post_attack_steps": [
            "Do not share personal information over unsolicited calls.",
            "Contact your bank or the organization directly using official contact numbers.",
            "Report the incident to the relevant authorities."
        ],
        "helplines": {
            "Cyber Crime Helpline Number": "1930",
            "National Cyber Crime Reporting Portal": "https://cybercrime.gov.in/"
        }
    },
    "blackmailing": {
        "info": "Threatening to reveal compromising information unless demands are met, often involving financial extortion.",
        "post_attack_steps": [
            "Do not engage with the blackmailer or give in to their demands.",
            "Collect and save evidence of the threats.",
            "Report the incident to law enforcement."
        ],
        "helplines": {
            "Cyber Crime Helpline Number": "1930",
            "National Cyber Crime Reporting Portal": "https://cybercrime.gov.in/"
        }
    }
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')  

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')





@app.route('/service')
def service():
    return render_template('service.html')



@app.route('/learn')
def learn():
    return render_template('project.html')


##edit 


@app.route('/predict', methods=['POST'])
def predict():
    description = request.form['description']
    prediction = model.predict([description])[0]
    
    # Normalize the prediction to match the dictionary keys
    normalized_prediction = prediction.strip().lower()
    details = attack_details.get(normalized_prediction, {
        "info": "Information not available.",
        "post_attack_steps": ["N/A"],
        "helplines": {"N/A": "N/A"}
    })

    return render_template('predict.html', 
                           prediction=prediction, 
                           info=details['info'], 
                           steps=details['post_attack_steps'], 
                           helplines=details['helplines'])

if __name__ == "__main__":
    app.run(debug=True)

    