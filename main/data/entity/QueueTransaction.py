class QueueTransaction:
    def __init__(self, transaction_id, symptoms, status="IN_QUEUE"):
        self.transaction_id = transaction_id
        self.symptoms = symptoms
        self.status = status
