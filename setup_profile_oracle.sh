#!/usr/bin/bash
echo 'JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.262.b10-0.el8_2.x86_64/jre' >> /home/oracle/.bash_profile
echo 'ORACLE_HOME=/home/oracle/app/oracle/product/11.2.0/client_1' >> /home/oracle/.bash_profile
echo 'ORACLE_BASE=/home/oracle/app/oracle' >> /home/oracle/.bash_profile
echo 'PATH=$PATH:$ORACLE_HOME/bin' >> /home/oracle/.bash_profile
echo 'export JAVA_HOME' >> /home/oracle/.bash_profile
echo 'export ORACLE_HOME' >> /home/oracle/.bash_profile
echo 'export PATH' >> /home/oracle/.bash_profile
echo 'export ORACLE_BASE' >> /home/oracle/.bash_profile
