#!/bin/bash
#启动股票脚本
#weekday=date +%a
#if(("$weekday" != "周日" && "$weekday" != "周六" ))
#else

#fi
py -3 /E/python_project/huaan_nasdaq.py
py -3 /E/python_project/huaan_nasdaq2.py
while((1));do
	py -3 /E/python_project/adobe_stock.py&&py -3 /E/python_project/microsoft_stock.py&&py -3 /E/python_project/nasdaq_stock.py
	sleep 3600
done