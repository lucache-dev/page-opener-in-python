import threading
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import PySimpleGUI as sg

def open_page(url, interval, stop_event):
    while not stop_event.is_set():
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
            time.sleep(interval)
            driver.quit()
        except Exception as e:
            sg.popup_error(f"Error: {e}")
            break

sg.theme('Reddit')
layout = [
    [sg.Text('Page URL'), sg.Input(key='url')],
    [sg.Text('Interval (seconds)'), sg.Input(key='interval', size=(10,1))],
    [sg.Button('Start'), sg.Button('Stop')],
]

window = sg.Window('Browser Page Opener', layout)
thread = None
stop_event = threading.Event()

while True:
    event, values = window.read(timeout=100)
    if event == sg.WIN_CLOSED:
        stop_event.set()
        break

    if event == 'Start':
        url = values['url']
        try:
            interval = int(values['interval'])
            if not url:
                sg.popup_error("Please enter a URL.")
                continue
            stop_event.clear()
            if thread is None or not thread.is_alive():
                thread = threading.Thread(target=open_page, args=(url, interval, stop_event), daemon=True)
                thread.start()
        except ValueError:
            sg.popup_error("Please enter a valid number for interval.")

    if event == 'Stop':
        stop_event.set()

window.close()
