# 首先，将PyOfficeRobot模块导入到我们的代码块中。
from PyOfficeRobot.core.WeChatType import *
from Config import *
import Kit
# 获取当前微信客户端
wx = WeChat()
# 获取会话列表
wx.GetSessionList()

def send_msg_to_target_object(msg, who):
    # 目标对象，无论是好友还是群聊，都可以通过这个方法发送消息
    wx.ChatWith(who)

    wx.SendMsg(msg, who = who)





# 处理从队列接收到的消息
def process_queue_message(ch, method, properties, body):
    """
    处理从队列接收到的消息的回调函数
    :param ch: pika.Channel 表示与 RabbitMQ 之间的连接通道，可用于执行消息操作。
    :param method: pika.spec.Basic.Deliver 包含有关传递消息的方法信息，如交换机、路由键等。
    :param properties: pika.spec.BasicProperties 包含消息的属性，这些属性可以是用户自定义的或者是 RabbitMQ 本身定义的。
    :param body: bytes 实际的消息内容，以字节序列的形式传递。
    :return: None
    """
    data = json.loads(body)

    # 加载body中的数据
    msg = data["message"]
    target = data["target"]
    print("the target is:", target, "  the message is:", msg)
    try:
        send_msg_to_target_object(msg, target)
        # 手动确认消息
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        print("send message error:", e)
        # 重新获取当前微信客户端
        wx = WeChat()
        wx.GetSessionList()



# 向某人发送消息（以`文件传输助手`为例）
msg = 'kenger bot test'
who = '文件传输助手'
target_group = "bot通知群"

if __name__ == '__main__':
    # send_msg_to_target_object(msg, target_group)


    conf = get_config()
    queue_name = conf["rabbitmq"]["queue_name"]
    connection = Kit.rabbitmq_conn(conf, "rabbitmq")
    channel = connection.channel()
    channel.queue_declare(queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=process_queue_message, auto_ack=False)
    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()