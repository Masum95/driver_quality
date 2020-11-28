def get_message(percent):
    if 0 <= percent <= 0.5:
        return """Your completion rate is very low.You will get suspended if you do not increase your completion 
        rate. """

    if 0.51 <= percent <= 0.70:
        return """Your completion rate is low. You will get less requests if you do not increase your completion 
        rate. """

    if 0.71 <= percent <= 1.0:
        return """Please complete more to get more requests."""