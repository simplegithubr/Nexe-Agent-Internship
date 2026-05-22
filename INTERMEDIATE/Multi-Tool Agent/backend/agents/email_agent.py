import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Dict
import os

class EmailAgent:
    def __init__(self, smtp_host=None, smtp_port=None, smtp_user=None, smtp_password=None):
        self.smtp_host = smtp_host or os.getenv('SMTP_HOST', 'smtp.gmail.com')
        self.smtp_port = int(smtp_port or os.getenv('SMTP_PORT', 587))
        self.smtp_user = smtp_user or os.getenv('SMTP_USER')
        self.smtp_password = smtp_password or os.getenv('SMTP_PASSWORD')

    def send_email(self, recipient: str, subject: str, body: str, html: bool = False) -> Dict:
        """
        Send an email

        Args:
            recipient: Email address of recipient
            subject: Email subject
            body: Email body content
            html: Whether body is HTML (default: False)

        Returns:
            Dictionary with status and message
        """
        if not all([self.smtp_user, self.smtp_password]):
            return {
                'success': False,
                'message': 'SMTP credentials not configured'
            }

        try:
            msg = MIMEMultipart('alternative')
            msg['From'] = self.smtp_user
            msg['To'] = recipient
            msg['Subject'] = subject

            if html:
                msg.attach(MIMEText(body, 'html'))
            else:
                msg.attach(MIMEText(body, 'plain'))

            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)

            return {
                'success': True,
                'message': f'Email sent successfully to {recipient}'
            }

        except Exception as e:
            return {
                'success': False,
                'message': f'Failed to send email: {str(e)}'
            }
