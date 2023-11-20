class ResponsePayload:
    def __init__(self, fulfillment_text):
        self.fulfillment_text = fulfillment_text

    def to_dict(self):
        return {
            "fulfillmentText": self.fulfillment_text
        }
