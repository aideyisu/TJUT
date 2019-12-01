
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


二-前奏：spark前置scala安装
一句话 ： sudo apt-get install scala
安装后使用shell scala -version检查版本问题
即可完成安装

三-hadoop
将hadoop的tar包解压
tar -zxvf hadoop-3.2.1.tar.fz -C /usr/local/
进入对应目录
sudo gedit /etc/profile
在末尾追加
##JAVA
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
export PATH=$PATH:$JAVA_HOME/bin

#HADOOP_HOME
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin

随后使用source /etc/profile

再使用hadoop发现有输出，完成配置

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
