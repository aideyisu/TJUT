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

四：spark

首先前往官网下载最新安装包
进入下载界面，解压至对应路径
sudo tar -zxvf spark-2.4.4-bin-hadoop2.7.tgz -C /usr/local
sudo mv ./spark-2.4.4-bin-hadoop2.7 ./spark
