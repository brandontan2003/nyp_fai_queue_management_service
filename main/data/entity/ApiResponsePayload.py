class ApiResponsePayload:
    def __init__(self, status, message):
        self.status = status
        self.message = message

    def to_json(self):
        return {
            "status": self.status,
            "message": self.message
        }
