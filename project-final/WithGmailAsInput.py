import imaplib
import email
from bs4 import BeautifulSoup
import project.sentiment_mod as s
import matplotlib.pyplot as plt


class Gmail:
    def __init__(self, userMail = None, userPass = None):
        self.uMail = userMail
        self.uPass = userPass
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')
        self.mail.login(self.uMail,self.uPass)
        self.mail.list()
        self.mail.select("inbox")
        self.POS = 0
        self.NEG = 0



    def compute(self):
        errorCount = 0
        result, data = self.mail.uid('search', None, "ALL")
        data2 = data[0].split()

        try:
            for i in range(0, len(data[0])):
                latest_email_uid = data2[-i]
                result, data = self.mail.uid('fetch', latest_email_uid, '(RFC822)')
                raw_email = data[0][1]

                raw_email = raw_email.decode('utf-8')

                email_message = email.message_from_string(raw_email)

                body = ""

                if email_message.is_multipart():
                    for part in email_message.walk():
                        ctype = part.get_content_type()
                        cdispo = str(part.get('Content-Disposition'))

                        # skip any text/plain (txt) attachments
                        if ctype == 'text/plain' and 'attachment' not in cdispo:
                            body = part.get_payload(decode=True)  # decode
                            break
                # not multipart - i.e. plain text, no attachments, keeping fingers crossed
                else:
                    body = email_message.get_payload(decode=True)

                try:
                    body = body.decode('utf-8')

                    flag = bool(BeautifulSoup(body, "html.parser").find())

                    if flag == True:
                        body = BeautifulSoup(body, 'html.parser').get_text()

                    sentiment_value = s.sentiment(body)
                    if sentiment_value == 'pos':
                        self.POS += 1
                        print("POS: ", self.POS)
                    else:
                        self.NEG += 1
                        print("NEG: ", self.NEG)

                    # print(body, sentiment_value, confidence)
                    output = open("gmail_out.txt", "a")
                    output.write(sentiment_value)
                    output.write('\n')
                    output.close()
                except Exception as e:
                    errorCount = errorCount + 1
        except Exception as e:
            str1 = 'positive = '+str(self.POS)
            str2 = 'negative = '+str(self.NEG)
            slices = [self.POS, self.NEG]
            activities = [str1, str2]
            cols = ['c','r']


            plt.figure()

            plt.pie(slices,
                    labels=activities,
                    colors=cols)

            plt.legend()

            plt.title('Sentiment Analysis')
            plt.show()

    def get_POS_NEG(self):
        return self.POS, self.NEG