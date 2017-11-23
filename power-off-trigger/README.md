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

## 直接使用
```bash
    python3 power-off-trigger.py --trig 10 --period 5 --gpio-pin 23
```
## Systemd
- 將主程式移動到 /etc 底下，並給予執行權限
```bash
    sudo mv power-off-trigger.py /etc/power-off-trigger.py
    sudo chmod +x /etc/power-off-trigger.py
```

- 修改啟動指令搞 (如果有需要的話)
```bash
    sudo nano power-off-trigger.service
```

- 將啟動指令搞移動到 /etc/lib/systemd/system 底下
```bash
    sudo mv power-off-trigger.service /etc/lib/systemd/system/power-off-trigger.service
```
- 在 systemd 中啟用
```bash
    sudo systemctl enable power-off-trigger.service
```