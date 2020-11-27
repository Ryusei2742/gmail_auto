import smtplib
from email.mime.text import MIMEText

class Mailer: #メールを送信するクラス

#初期化
    def __init__(self, addr_to, subject, body):
        self.password = "" #Gmailのログインパスワード アプリパスワードを作っておく
        self.addr_from = "" #送信元アドレス
        self.addr_to = addr_to
        self.charset = "ISO-2022-JP"
        self.subject = subject
        self.body = body

#メールの設定
    def send(self):
        msg = MIMEText(self.body.encode(self.charset), 'plain', self.charset)
        msg['Subject'] = self.subject
        msg['From'] = self.addr_from
        msg['To'] = self.addr_to

        #gmailのsmtp経由で送信
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(self.addr_from, self.password)
        smtp.send_message(msg)
        smtp.close()

def create_mail_body(full_name):

    body = """
#本文
""".format(full_name)

    return body

#動作確認
import sys
import csv

#引数からファイル名を取得
filename = 'list.csv' #宛先を記録したcsvファイルのパス

#CSVから読み込み
with open(filename, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        """全員に対して送る"""
        # CSVからメール送信に必要な情報を抽出
        full_name = row[0]
        email = row[1]
        #内容
        addr_to = email
        subject = "Pyhtonによるテストメール"
        body = create_mail_body(full_name)
        mailer = Mailer(addr_to, subject, body)
        mailer.send()