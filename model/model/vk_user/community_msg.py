@@ -3,6 +3,7 @@


def write_msg(user_ids, text, keyboard=None, attachment=None):
    """отправка сообщений от сообщества, используется в longpoll поэтому здесь на не в классе VkUser"""
    vk_session.method('messages.send',
                      {"user_id": user_ids, "message": text, "random_id": randint(1, 1000), "keyboard": keyboard,
                       "attachment": attachment})
