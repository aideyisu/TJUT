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
sudo chown -R {你的用户名} ./flume
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
