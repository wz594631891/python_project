#!/bin/bash
#启动股票脚本
#weekday=date +%a
#if(("$weekday" != "周日" && "$weekday" != "周六" ))
#else

#fi
while((1));do
	py -3 adobe_stock.py&&py -3 microsoft_stock.py&&py -3 nasdaq_stock.py
	sleep 3600
done