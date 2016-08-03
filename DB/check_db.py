import postgresql.driver as pg_driver


db = pg_driver.connect(
    user='postgres',
    password='postgres',
    host='192.168.99.100',
    database='personal_data',
    port='5432'
)


for current_email_id_1 in db.prepare("SELECT count(*) FROM customer WHERE status_id = 1"):
    current_email_id_1[0]

email = current_email_id_1[0]
print(email)


assert email != 0



if email == 0:
    print("ook")
else:
    print('bad')



db.close()