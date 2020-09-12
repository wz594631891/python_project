#!/bin/bash
#启动股票脚本
#weekday=\date +%a
#if(("$weekday" != "周日" && "$weekday" != "周六" ))
#else

#fi

while((1));do
    date | tee -a log.txt #同时输出到终端和日志
	py -3 /E/python_project/covid_us.py | tee -a log.txt # 美国疫情现有确诊监控
	py -3 /E/python_project/huaan_nasdaq.py | tee -a log.txt # 月涨幅年化率
	py -3 /E/python_project/huaan_nasdaq2.py | tee -a log.txt # 华安跌幅是否超5%
	# adobe、微软、纳斯达克指数评价
	py -3 /E/python_project/adobe_stock.py| tee -a log.txt
	py -3 /E/python_project/microsoft_stock.py| tee -a log.txt
	py -3 /E/python_project/nasdaq_stock.py| tee -a log.txt
	py -3 /E/python_project/vix.py| tee -a log.txt
	# 华安,大成,广发纳斯达克基金限额
	py -3 /E/python_project/nasdaq_limit.py| tee -a log.txt
	py -3 /E/python_project/nasdaq_limit2.py| tee -a log.txt
	py -3 /E/python_project/nasdaq_limit3.py| tee -a log.txt

	sleep 3600
done