# Copypaste stuff to telegram
import time
keyboard.send_keys("<ctrl>+c")

window.activate("Telegram.TelegramDesktop", matchClass=True)
keyboard.send_keys("\"<ctrl>+v")
time.sleep(0.1)
keyboard.send_keys("\" ")

#keyboard.send_keys("\""+text+"\" ")
