from main.constant.QueueManagementConstant import estimated_waiting_time_each, display_waiting_time_success
from main.data.entity.ResponsePayload import ResponsePayload


def get_waiting_time(count):
    actual_count = count - 1
    waiting_time = estimated_waiting_time_each * actual_count
    return ResponsePayload(display_waiting_time_success % (actual_count, waiting_time)).to_dict()

