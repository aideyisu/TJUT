#用以记录大创过程中的一些小困难的解决方案

#因本人此时对Vi || vim 操作甚为生疏，故全改为gedit图形化操作

预备：
首先要更换的软件源到国内地点，：
选择“软件和更新”，从下载自中选择一个国内站点，然后点击关闭
在完成之后，sudo apt-get update 更新索引
至此完成了对应软件源更换配置

一：JAVA安装
https://blog.csdn.net/zbj18314469395/article/details/86064849

①更新软件包列表 : sudo apt-get update
②安装openjdk-8-jdk : sudo apt-get install openjdk-8-jdk
③查看java版本，查看是否安装成功 : java -version

但是此时并没有并没有配置java的部分环境变量，需手动配置
①修改环境变量 : sudo gedit ~/.bashrc
②在文件末尾追加
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export PATH=${JAVA_HOME}/bin:$PATH
③保存关闭后使环境变量马上生效
source ~/.bashrc

java8环境至此安装完毕

二：FLUME安装
https://www.cnblogs.com/soyo/p/7686702.html
①从官网下载最新版本的flume(此时为1.9.0)
在主界面打开终端
cd /usr
sudo mkdir local2
②进入下载界面打开终端
sudo tar -zxvf apache-flume-1.9.0-bin.tar.gz -C /usr/local2
随后从主界面  cd /usr/local2
sudo mv ./apache-flume-1.9.0-bin ./flume
sudo chown -R {你的用户名}:{你的用户名} ./flume
③配置环境变量
sudo gedit ~/.bashrc
文档最后加入
export FLUME_HOME=/usr/local2/flume
export FLUME_CONF_DIR=$FLUME_HOME/conf
export PATH=$PATH:$FLUME_HOME/bin
随即更新
source ~/.bashrc
④配置flume-env.sh
从主界面 cd /usr/local2/flume/conf
sudo cp ./flume-env.sh.template ./flume-env.sh
sudo gedit ./flume-env.sh
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

检验flume安装情况
①检查版本
cd/uar/local2/flume/bin
./flume-ng version     
注 初次可选启动命令
bin/flume-ng agent -n $agent_name -c conf -f conf/flume-conf.properties.template

报错DEBUG
No appenders could be found for logger (org.apache.flume.util.SSLUtil). [原因：-c 未找到路径]
https://blog.csdn.net/u012373815/article/details/54024940


三-前奏：zookeeper kafka前置组件
https://blog.csdn.net/wsk1103/article/details/80399115
首先官网下载最新版，进入下载目录解压
sudo tar -zxvf apache-zookeeper-3.5.5-bin.tar.gz -C /usr/local/services
便于后续识别所以改名
sudo mv ./apache-zookeeper-3.5.5-bin ./zookeeper-3.5.5
进入其中的conf目录 : sudo cp ./zoo_sample.cfg ./zoo.cfg
编辑基本信息 : sudo gedit ./zoo.cfg

# The number of milliseconds of each tick
# 心跳间隔，毫秒
tickTime=2000
# The number of ticks that the initial
# synchronization phase can take
# 配置zookeeper接受客户端初始化连接时最长能忍受多少个时间心跳间隔。
initLimit=10
# The number of ticks that can pass between
# sending a request and getting an acknowledgement
# 这个配置项标识 Leader 与 Follower 之间发送消息，请求和应答时间长度，最长不能超过多少个 tickTime 的时间长度。
syncLimit=5
# the directory where the snapshot is stored.
# do not use /tmp for storage, /tmp here is just
# example sakes.
# 数据存放的位置
dataDir=/home/mengfz/sofrware/zookeeper/zookeeperData
#日志存放的位置
dataLogDir=/home/mengfz/sofrware/zookeeper/zookeeperLog
# the port at which the clients will connect
# 服务器客户端的接口
clientPort=2181
# the maximum number of client connections.
# increase this if you need to handle more clients
#maxClientCnxns=60
#
# Be sure to read the maintenance section of the
# administrator guide before turning on autopurge.
#
# http://zookeeper.apache.org/doc/current/zookeeperAdmin.html#sc_maintenance
#
# The number of snapshots to retain in dataDir
#autopurge.snapRetainCount=3
# Purge task interval in hours
# Set to "0" to disable auto purge feature
#autopurge.purgeInterval=1

# 2888,3888 are election port
# 2888端口是zookeeper服务之间的通讯的端口，3888是zookeeper与其他应用程序通讯的端口。
server.1=localhost:2888:3888

后续验证操作：
①根据dataDir和dataLogDir路径，在主目录下创建对应的文件夹
dataDir=/home/mengfz/sofrware/zookeeper/zookeeperData
dataLogDir=/home/mengfz/sofrware/zookeeper/zookeeperLog
并且在主目录下cd /sofrware/zookeeper/zookeeperData
创建文件 touch myid    其中内容为 1
②启动zookeeper服务器，进入zookeeper/bin目录，执行 sudo ./zkServer.sh start 启动服务器
③检验服务器命令， sudo ./zkCli.sh -server localhost:2181 控制台输出没有报错便是已经启动成功
④停止服务器命令 sudo ./zkServer.sh stop
至此zookeeper已经全部安装完毕

三：KAFKA安装
https://blog.csdn.net/weixin_40782143/article/details/87901289
①进入下载地址下载
sudo tar -zxvf kafka_2.12-2.3.0.tgz -C /opt
②进入opt目录
sudo mv ./kafka_2.12-2.3.0 ./kafka
sudo chown -R {你的用户名}:{你的用户名} /opt/kafka
#sudo chown -R mengfz:mengfz /opt/kafka
③启动服务器
bin/kafka-server-start.sh config/server.properties
看到响应后即可停止服务器
④停止服务器
bin/kafka-server-stop.sh config/server.properties


四-前奏：spark前置scala安装
一句话 ： sudo apt-get install scala
安装后使用shell scala -version检查版本问题
即可完成安装

四：SPARK
http://dblab.xmu.edu.cn/blog/2081-2/
①首先前往官网下载最新安装包
https://spark.apache.org/downloads.html
②进入下载界面，解压至对应路径
sudo tar -zxvf spark-2.4.4-bin-hadoop2.7.tgz -C /usr/local
进入/usr/local路径，改名并赋予权限
sudo mv ./spark-2.4.4-bin-hadoop2.7 ./spark
sudo chown -R mengfz:mengfz ./spark
③进入conf目录，生成配置文件
cp ./spark-env.sh.template ./spark-env.sh
随后打开并编辑之 ： sudo gedit spark-env.sh
在最后加入
export SPARK_DIST_CLASSPATH=$(/usr/local/hadoop/bin/hadoop classpath)

spark后续验证操作：
cd /usr/local/spark
./bin/run-example SparkPi 2>&1 | grep "Pi is"
最终会输出π的近似值
即可完成安装

五：REDIS
https://blog.csdn.net/qq_41822647/article/details/84594200
在ubuntu18.04系统下可直接通过命令安装
①前期准备  更新软件列表和软件 (第二个指令比较慢)
sudo apt-get update
sudo apt-get upgrade
②安装REDIS
sudo apt-get install redis-server
并检查版本
redis-server -v
③测试REDIS 启动服务，启动客户端
redis-server
REDIS-cli

六：mongoDB   官网直安，方便快捷
https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
①导入包管理系统使用的公钥
wget -qO  -  https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add  -
②为MongoDB创建一个列表文件
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
③重新加载本地包数据库
sudo apt-get update
④安装MongoDB包
sudo apt-get install -y mongodb-org

后续验证操作：
①启动MongoDB
sudo service mongod start
②通过检查日志文件的内容验证进程是否成功启动
sudo gedit /var/log/mongodb/mongod.log
而后搜索 27017，可以很快捷的找到
[initandlisten] waiting for connections on port 27017
