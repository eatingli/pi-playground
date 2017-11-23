# Power Off Trigger
判定GPIO，連續一定的次數沒有被觸發，則關機。設定開機自動執行。

# 相關技術

## Systemd
- 設定開機時執行
- [參考資料](https://www.raspberrypi.org/documentation/linux/usage/systemd.md)

## GPIO
- PI GPIO
- [參考資料](http://yehnan.blogspot.tw/2012/07/raspberry-pigpioled.html)

## optparse
- 選項處理
- [參考資料](http://www.cnblogs.com/captain_jack/archive/2011/01/11/1933366.html)

# 使用
- 在 systemd 中啟用
- 執行 power-off-trigger.py --trig 10 --period 5