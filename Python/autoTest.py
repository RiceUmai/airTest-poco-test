# import unity poco driver from this path
from poco.drivers.unity3d import UnityPoco
import time
import sys

# -*- encoding=utf8 -*-
__author__ = "test"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

# BlueStacksから接続する場合、devices=["android://127.0.0.1:5037/{BlueStacksのADBアドレス}",]
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:49652",])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)

poco = UnityPoco()

# ==========================
# ==========================
# GUI Demo uiのButtonを押す
newgame_btn = poco('Newgame', type='Button')
newgame_btn.click()

contunue_btn = poco('Continue', type='Button')
contunue_btn.focus('anchor').click()

settings_btn = poco('Settings', type='Button')
settings_btn.click()


# ==========================
# ==========================
# GameplaySetting PageのボタンとSliaderを操作
settings = poco('SettingsWindow')
settings.wait_for_appearance()

gameplay_btn = poco('Gameplay', type='Button')
gameplay_btn.click()

gamePlayWindow = poco('GamePlayWindow')
gamePlayWindow.wait_for_appearance()

settingsSlders = gamePlayWindow.offspring(type = 'Slider').child('Handle Slide Area')

for slider in settingsSlders:
    startSlide = slider.focus([0, 0.5])
    endSlide = slider.focus([1, 0.5])
    startSlide.drag_to(endSlide)    
    endSlide.drag_to(startSlide)


AOToggle = gamePlayWindow.offspring(type = 'Toggle').child('Checkmark')
AOToggle.click()
AOToggle.click()

close_btn = gamePlayWindow.child('Panel').child(type='Button')
close_btn.click()
gamePlayWindow.wait_for_disappearance()


# ==========================
# ==========================
# VideoSetting PageのボタンとSliaderを操作

video_btn = poco('Video', type='Button')
video_btn.click()
videoWindow = poco('VideoWindow')
videoWindow.wait_for_appearance()

videoSettingSliders = videoWindow.offspring(type= 'Slider').child('Handle Slide Area')

for slider in videoSettingSliders:
    startSlide = slider.focus([0, 0.5])
    endSlide = slider.focus([1, 0.5])
    startSlide.drag_to(endSlide)
    endSlide.drag_to(startSlide)
    
videoSettingToggles = videoWindow.offspring(type= 'Toggle').child('Checkmark')

for toggle in videoSettingToggles:
    toggle.click()
    toggle.click()

close_btn = videoWindow.child('Panel').child(type='Button')
close_btn.click()
videoWindow.wait_for_disappearance()

# ==========================
# ==========================
# AudioSetting PageのボタンとSliaderを操作

audio_btn = poco('Audio', type='Button')
audio_btn.click()

audioWindow = poco('AudioWindow')
audioSettingSliders = audioWindow.offspring(type= 'Slider').child('Handle Slide Area')

for slider in audioSettingSliders:
    startSlide = slider.focus([0, 0.5])
    endSlide = slider.focus([1, 0.5])
    startSlide.drag_to(endSlide)
    endSlide.drag_to(startSlide)
    
close_btn = audioWindow.child('Panel').child(type='Button')
close_btn.click()
audioSettingSliders.wait_for_disappearance()

# ==========================
# ==========================
#  Settingsページから出すボタンを押す
back_btn = poco('Back', type='Button')
back_btn.click()
