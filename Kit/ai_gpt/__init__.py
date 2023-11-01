# from Config import *
# import random
# from revChatGPT.V1 import Chatbot


# def querry_once(prompt):
#     accessToken = get_config()["gpt_account"]["access_token"]
#     chatbot = Chatbot(config={
#       "access_token": accessToken
#     })

#     # 利用随机数，实现1/10的概率，让机器人清空对话
#     if random.randint(0, 10) == 0 :
#         chatbot.clear_conversations()  
#     ask_rsp = chatbot.ask(
#         prompt,
#         model = "gpt-3.5-turbo"
#     )
#     rsp = ""
#     for rsp in ask_rsp:
#         pass
#     return rsp



# def movie_query_once(movie_title):
#     # movie_name = "PIYO-165 「い～っぱい舐めて柔らかくしてからお尻責めてあげる」べろべろアナル舐めメスイキ痴女子校生の誘惑 花狩舞 幾田真知 倉本蓳"
#     # movie_name = "'夫婦交歓～戻れない夜～【第01話】 [中文字幕] - H動漫/裏番/線上看 - Hanime1.me'"
#     movie_name = movie_title
#     movie_prompt = f"""
#     假设你是一个电影标签名字json处理器，负责帮我从一段文字中提取出电影的名字和作者然后生成相应的json。下面的```块内是待处理的文字。
#     ```
#     {
#         movie_name
#     }
#     ```
#     请按照下面要求依次执行：
#     1. 请找到主演者的名字，主演的名字可能不止一个，也可能没有。
#     2. 请找到影片名字，影片名字一般不是英文字母+数字的组合
#     3. 找到影片名字`origin_name`后，翻译成中文给`chinese_name`
#     4. 请保证输出的简洁，影片名字中的/符号，以及网站信息等无关信息请剔除
#     5. 除了最终输出格式的要求输出json，其他请务必什么也不要输出，更不要解释，请严格控制输出
#     6. 最终的输出格式为json格式：
#     {{
#         "actors":"xxx",
#         "origin_name":"xxx",   // 输出原始的片名
#         "chinese_name":"xxx"   // 输出origin_name翻译为中文后的名字。

#     }}

#     具体例子如下：
#     ```
#     输入：PIYO-165 「い～っぱい舐めて柔らかくしてからお尻責めてあげる」べろべろアナル舐めメスイキ痴女子校生の誘惑 花狩舞 幾田真知 倉本蓳
#     输出：{{"actors": "花狩舞, 幾田真知, 倉本蓳", "origin_name": "い～っぱい舐めて柔らかくしてからお尻責めてあげる", "chinese_name": "舔舐充分后责罚臀部的诱惑 舌舔肛门的淫乱女子校生"}}
#     ```
#     """
#     # 注意，prompt设计的精确，要先提取出日本名字，然后说让翻译为中文名字。然后处理器比处理人员好点。
#     print(movie_prompt)
#     rsp = querry_once(movie_prompt)
#     try:
#         ans_json = json.loads(rsp['message'])
#     except:
#         ans_json = {
#             "actors":"xxx",
#             "origin_name":rsp['message'],  
#             "chinese_name":rsp['message']  
#         }
#     return ans_json

# if __name__ == "__main__":
#     # movie_query_once("PIYO-165 「い～っぱい舐めて柔らかくしてからお尻責めてあげる」べろべろアナル舐めメスイキ痴女子校生の誘惑 花狩舞 幾田真知 倉本蓳")
#     movie_query_once("'夫婦交歓～戻れない夜～【第01話】 [中文字幕] - H動漫/裏番/線上看 - Hanime1.me'")