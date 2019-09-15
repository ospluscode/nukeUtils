import nuke
import PySide.QtGui
import os

"""
Notify the user when a render is done: play sound, create popup window
"""

show_notification = True
play_sound = True
sound_file = "{}/01.wav".format(os.path.dirname(__file__))

def notify_user():
    """
    Play sound, create popup window
    :return: None
    """
    if play_sound:
        PySide.QtGui.QSound.play(sound_file)
    if show_notification:
        nuke.message("Finished rendering")
