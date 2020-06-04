import justpy as jp
import time
import sqlite3
from modules.monitor import adjust_temp

wp = jp.WebPage(delete_flag=False)
clock_div = jp.Span(
    text="Loading...", classes="text-5xl m-1 p-1 bg-gray-300 font-mono", a=wp
)
my_paragraph_design = (
    "w-64 bg-blue-500 m-2 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
)


def submit_temp(self, current_temp, target_temp):
    self.x = adjust_temp(current_temp, target_temp)


def my_click(self, msg):
    self.text = "I was clicked"
    print(msg.event_type)
    print(msg["event_type"])
    print(msg)


def home():
    in1 = jp.Input(a=wp, classes=input_classes, placeholder="Target Temperature")
    in2 = jp.Input(a=wp, classes=input_classes, placeholder="Current Temperature")
    d.on("click", my_click)
    return wp


jp.justpy(home)
