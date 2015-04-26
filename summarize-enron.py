__author__ = 'gavinhenderson'

import sys
import csv
import time
import datetime
from operator import itemgetter
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

email_csv_file = sys.argv[1]
print(email_csv_file)
#email_csv_file = open('enron-event-history-all.csv')
email_csv_file = open(email_csv_file)



email_csv = csv.reader(email_csv_file)
print(email_csv)

sender = []
recipient = []
time_sent = []
unique_sender = []
emails_sent = []
emails_sent_multi = []
unique_recipient = []
emails_received = []
time_received = []

for row in email_csv:
    # sender.append(row[2])
    #time_sent.append(int(row[0])/1000)
    multi_recipient = row[3].split("|")
    #print(multi_recipient)
    if row[2] not in unique_sender:
        unique_sender.append(row[2])
        emails_sent.append(1)
        emails_sent_multi.append(0)
        emails_received.append(0)
    else:
        emails_sent[unique_sender.index(row[2])] += 1
    for k in range(multi_recipient.__len__()):
        sender.append(row[2])
        time_sent.append(int(row[0]) / 1000)
        remove_marks = multi_recipient[k].split("@")
        remove_marks = remove_marks[0].split("/")
        remove_marks = remove_marks[0].split(" AT")
        remove_marks = remove_marks[0].lower()
        recipient.append(remove_marks)
        time_received.append(int(row[0]) / 1000)
        emails_sent_multi[unique_sender.index(row[2])] += 1
        if remove_marks not in unique_sender:
            unique_sender.append(remove_marks)
            emails_sent_multi.append(0)
            emails_sent.append(0)
            emails_received.append(1)
        else:
            emails_received[unique_sender.index(remove_marks)] += 1


email_csv_file.close()

user_activity = zip(unique_sender, emails_sent, emails_received)
user_activity = sorted(user_activity, key=itemgetter(1), reverse=True)
user_activity_multi = zip(unique_sender, emails_sent_multi, emails_received)
user_activity_multi = sorted(user_activity_multi, key=itemgetter(1), reverse=True)

with open('User_Activity.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(user_activity)

fp.close()

with open('User_Activity_Multi.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(user_activity_multi)

fp.close()
# print(recipient)

super_user = [item[0] for item in user_activity_multi]
super_user = super_user[0:4]
s_user1 = super_user[0]
s_user2 = super_user[1]
s_user3 = super_user[2]
s_user4 = super_user[3]
time_sent=np.array(time_sent)
time_received=np.array(time_received)
user_ind = [i for i, x in enumerate(sender) if x == s_user1]
s_user1_time_sent = time_sent[user_ind]
user_ind = [i for i, x in enumerate(sender) if x == s_user2]
s_user2_time_sent = time_sent[user_ind]
user_ind = [i for i, x in enumerate(sender) if x == s_user3]
s_user3_time_sent = time_sent[user_ind]
user_ind = [i for i, x in enumerate(sender) if x == s_user4]
s_user4_time_sent = time_sent[user_ind]
user_ind = [i for i, x in enumerate(recipient) if x == s_user1]
s_user1_time_received = time_received[user_ind]
user_ind = [i for i, x in enumerate(recipient) if x == s_user2]
s_user2_time_received = time_received[user_ind]
user_ind = [i for i, x in enumerate(recipient) if x == s_user3]
s_user3_time_received = time_received[user_ind]
user_ind = [i for i, x in enumerate(recipient) if x == s_user4]
s_user4_time_received = time_received[user_ind]

sec_week = 7*24*60*60
week_interval = (time_sent[-1] - time_sent[0])//sec_week
dt_old=time_sent[0]
time_bin = []
time_bin.append(time_sent[0])
s_user1_received = []
s_user2_received = []
s_user3_received = []
s_user4_received = []
s_user1_sent = []
s_user2_sent = []
s_user3_sent = []
s_user4_sent = []

for dt in xrange(week_interval):
    dt_new=dt_old + sec_week
    time_bin.append(dt_new)
    
    temp_bin = np.where(s_user1_time_sent < dt_new)
    s_user1_time_sent = np.delete(s_user1_time_sent,temp_bin[0])
    temp_bin = temp_bin[0].__len__()
    s_user1_sent.append(temp_bin)
    temp_bin = np.where(s_user1_time_received < dt_new)
    s_user1_time_received = np.delete(s_user1_time_received,temp_bin[0])
    temp_bin = temp_bin[0].__len__()
    s_user1_received.append(temp_bin)
    
    temp_bin = np.where(s_user2_time_sent < dt_new)
    s_user2_time_sent = np.delete(s_user2_time_sent,temp_bin[0])
    temp_bin = temp_bin[0].__len__()
    s_user2_sent.append(temp_bin)
    temp_bin = np.where(s_user2_time_received < dt_new)
    s_user2_time_received = np.delete(s_user2_time_received,temp_bin[0])
    temp_bin = temp_bin[0].__len__()
    s_user2_received.append(temp_bin)
    
    temp_bin = np.where(s_user3_time_sent < dt_new)
    s_user3_time_sent = np.delete(s_user3_time_sent,temp_bin[0])
    temp_bin = temp_bin[0].__len__()
    s_user3_sent.append(temp_bin)
    temp_bin = np.where(s_user3_time_received < dt_new)
    s_user3_time_received = np.delete(s_user3_time_received,temp_bin[0])
    temp_bin = temp_bin[0].__len__()
    s_user3_received.append(temp_bin)
    
    temp_bin = np.where(s_user4_time_sent < dt_new)
    s_user4_time_sent = np.delete(s_user4_time_sent,temp_bin[0])
    temp_bin = temp_bin[0].__len__()
    s_user4_sent.append(temp_bin)
    temp_bin = np.where(s_user4_time_received < dt_new)
    s_user4_time_received = np.delete(s_user4_time_received,temp_bin[0])
    temp_bin = temp_bin[0].__len__()
    s_user4_received.append(temp_bin)
    
    dt_old = dt_new


start_date = datetime.datetime.fromtimestamp(int(time_bin[0]))
end_date = datetime.datetime.fromtimestamp(int(time_bin[-1]))
time_axis = mdates.drange(start_date,end_date,datetime.timedelta(weeks=1))

fig = plt.figure()

plt.plot_date(time_axis, s_user1_sent, ls='-', marker='o', label=super_user[0])
plt.plot_date(time_axis, s_user2_sent, ls='-', marker='x', label=super_user[1])
plt.plot_date(time_axis, s_user3_sent, ls='-', marker='^', label=super_user[2])
plt.plot_date(time_axis, s_user4_sent, ls='-', marker='H', label=super_user[3])
plt.title('Number of Emails Sent Per Week')
plt.ylabel('Emails Sent')
plt.grid(True)
plt.legend()

fig.autofmt_xdate(rotation=45)
fig.tight_layout()

#fig.show()
plt.savefig('Emails_Sent.png')

fig = plt.figure()

plt.plot_date(time_axis, s_user1_received, ls='-', marker='o', label=super_user[0])
plt.plot_date(time_axis, s_user2_received, ls='-', marker='x', label=super_user[1])
plt.plot_date(time_axis, s_user3_received, ls='-', marker='^', label=super_user[2])
plt.plot_date(time_axis, s_user4_received, ls='-', marker='H', label=super_user[3])
plt.title('Number of Emails Received Per Week')
plt.ylabel('Emails Received')
plt.grid(True)
plt.legend()

fig.autofmt_xdate(rotation=45)
fig.tight_layout()

#fig.show()
plt.savefig('Emails_Received.png')

#print(user_activity_multi[1:10])
#print(time_sent)

print(time.ctime(time_sent[0]))
#print(time.strftime("%Y %m", time_sent[0]))
print(super_user)


