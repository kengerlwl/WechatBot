# coding=utf-8
import os
import pika
# import pymongo
# import pymysql
# from dbutils.pooled_db import PooledDB
# from elasticsearch import Elasticsearch
from redis import ConnectionPool, StrictRedis





def redis_pool(config, db_key):
    print(config[db_key])
    return StrictRedis(**config[db_key])


def rabbitmq_conn(config, db_key):
    rabbitmq_config = config[db_key]
    # RabbitMQ连接配置
    rabbitmq_params = pika.ConnectionParameters(
        host=rabbitmq_config['host'],  # RabbitMQ服务器地址
        port=rabbitmq_config['port'],         # RabbitMQ端口
        virtual_host=rabbitmq_config['virtual_host'],  # 虚拟主机，默认是'/'
        credentials=pika.credentials.PlainCredentials(rabbitmq_config['username'], rabbitmq_config['password'])  # 用户名和密码
    )
    rabbitmq_conn = pika.BlockingConnection(rabbitmq_params)
    return rabbitmq_conn


# def mysql_conn(config, db_key):
#     config[db_key]['port'] = int(config[db_key]['port'])
#     conn = pymysql.connect(**config[db_key])
#     return conn


# def mysql_pool(config, db_key):
#     for key in config["MYSQL_POOL"]:
#         config["MYSQL_POOL"][key] = int(config["MYSQL_POOL"][key])
#     config[db_key]['port'] = int(config[db_key]['port'])
#     pool = PooledDB(creator=pymysql, **config[db_key], **config["MYSQL_POOL"])
#     return pool

# def mongo_pool(config, db_key):
#     return pymongo.MongoClient(config[db_key]["uri"])


# def elastic_conn(config, base_path):
#     ca_path = os.path.join(base_path, config["ELASTIC"]["ca_cert"])
#     es_client = Elasticsearch(
#         config["ELASTIC"]["es_url"],
#         ca_certs=ca_path,
#         basic_auth=(
#             config["ELASTIC"]["username"],
#             config["ELASTIC"]["password"]
#         ),
#         request_timeout=30 * 60
#     )
#     return es_client




# 对应的数据库连接池配置
# {
#   "MYSQL": {
#     "host": "***********",
#     "user": "github",
#     "passwd": "***********",
#     "db": "github_robot",
#     "port": 12806,
#     "charset": "utf8mb4"
#   },
#   "REDIS": {
#     "host": "***********",
#     "port": "12879",
#     "db": 2,
#     "password": "***********"
#   },
#   "MONGO": {
#     "uri": "mongodb://***********"
#   },
#   "ELASTIC": {
#     "es_url": "https://***********",
#     "ca_cert": "Config/certs/ca.crt",
#     "username": "elastic",
#     "password": "***********"
#   },
#   "TASK": {
#     "node": "xeon",
#     "process": 8,
#     "data_bin": "2020",
#     "page_size": 10000,
#     "win_path": "Z:\\TrainData\\EventList",
#     "srv_path": "/data/DataBin/TrainData/EventList"
#   }
# }
