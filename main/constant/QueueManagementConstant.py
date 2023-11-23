api_v1 = "/api/v1"
webhook = "/webhook"
update_transaction_status = "/update-transaction-status"

date_pattern_format = "%d%m%Y"

estimated_waiting_time_each = 5

# DialogFlow Parameters
query_result = "queryResult"
query_text = "queryText"
intent = "intent"
display_name = "displayName"
parameters = "parameters"
conditions = "conditions"

# Process Status
in_queue = "IN_QUEUE"
cancelled = "CANCELLED"
registered = "REGISTERED"

# Intents Naming
appointment_booking = "appointment_booking"
check_queue = "check_queue"
cancel_appointment = "cancel_appointment"

# Fulfilment Response
registration_successful_response = \
    "Thank you, your appointment has been successfully processed. " \
    "Please show the Transaction ID to the staff in the clinic when your turns nears. This is your Transaction ID: "

something_went_wrong_error = "Something went wrong. Please try again later."

transaction_cancelled_successfully = \
    "Your appointment with Transaction ID %s has been successfully canceled. We appreciate your prompt action. " \
    "If you have any further questions or need assistance, please feel free to contact us. Thank you!"

transaction_registered_successfully = "Transaction ID: %s has been successfully registered with the clinic."

transaction_id_not_found = "Transaction not found. Please verify the transaction ID and try again."

transaction_status_already_cancelled = "This transaction has been cancelled already."

transaction_status_already_registered = "This transaction has been registered. " \
                                        "To cancelled the clinic registration, please find to our clinic staff."

invalid_transaction_status = "This transaction is no longer valid."

next_in_line_success = "You are next in the line, please head down to the clinic now."

display_waiting_time_success = "There are %s of patients ahead of you, the estimated waiting time is %s minutes."


# Update Transaction Status
update_transaction_success = "Transaction status has been updated successfully."
missing_mandatory_field = "Missing Mandatory Fields."
invalid_request_transaction_status = "The transaction status is invalid."
