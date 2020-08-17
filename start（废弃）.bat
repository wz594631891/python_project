@echo off
::声明采用UTF-8编码

chcp 65001
title 【定时爬虫任务】By【xk_wang】
::cd /d "F:\7.Code Dancing\00_测试题集锦\爬虫"
echo 当前路径: %cd%
set SLEEP=3600
:Repeat
py -3 adobe_stock.py
py -3 microsoft_stock.py
py -3 nasdaq_stock.py

::清屏
cls
echo 当前路径: %cd%
:: timeout自带pause效果，即 press a key to continue ...
timeout %SLEEP%
goto Repeat
::运行完批处理, 停留在cmd窗口
::pause
::exit
::可用