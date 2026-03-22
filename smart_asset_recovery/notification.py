import smtplib

def send_notification(owner_email,item_id,lat,lon):

    maps = f"https://maps.google.com/?q={lat},{lon}"

    message = f"""
Subject: Item Found

Your item has been found.

Item ID: {item_id}

Finder Location:
{maps}
"""

    server = smtplib.SMTP("smtp.gmail.com",587)

    server.starttls()

    server.login("yourmail@gmail.com","APP_PASSWORD")

    server.sendmail(
    "yourmail@gmail.com",
    owner_email,
    message
    )

    server.quit()