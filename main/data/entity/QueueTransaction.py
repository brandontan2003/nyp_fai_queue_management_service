import datetime


class QueueTransaction:
    def __init__(self, transaction_id, symptoms, status="IN_QUEUE", created_date=datetime.datetime.now()):
        self.transaction_id = transaction_id
        self.symptoms = symptoms
        self.status = status
        self.created_date = created_date

