#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import signal
import gi
import time
import urllib
import os
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3, GObject
from threading import Thread

import dbus
session_bus = dbus.SessionBus()
spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
spotify_interface = dbus.Interface(spotify_bus, "org.freedesktop.DBus.Properties")
spotify_properties = spotify_interface.GetAll("org.mpris.MediaPlayer2.Player")
metadata = spotify_properties["Metadata"]

for key, value in spotify_properties.items():
    print key, value

cwd = os.getcwd()
trackId = metadata['mpris:trackid']
playBackStatus = spotify_properties['PlaybackStatus']
urllib.urlretrieve(metadata['mpris:artUrl'], 'spotify-art.png');

font_sans = {'A':u'𝖠','B':u'𝖡','C':u'𝖢','D':u'𝖣','E':u'𝖤','F':u'𝖥','G':u'𝖦','H':u'𝖧','I':u'𝖨','J':u'𝖩','K':u'𝖪','L':u'𝖫','M':u'𝖬','N':u'𝖭','O':u'𝖮','P':u'𝖯','Q':u'𝖰','R':u'𝖱','S':u'𝖲','T':u'𝖳','U':u'𝖴','V':u'𝖵','W':u'𝖶','X':u'𝖷','Y':u'𝖸','Z':u'𝖹','a':u'𝖺','b':u'𝖻','c':u'𝖼','d':u'𝖽','e':u'𝖾','f':u'𝖿','g':u'𝗀','h':u'𝗁','i':u'𝗂','j':u'𝗃','k':u'𝗄','l':u'𝗅','m':u'𝗆','n':u'𝗇','o':u'𝗈','p':u'𝗉','q':u'𝗊','r':u'𝗋','s':u'𝗌','t':u'𝗍','u':u'𝗎','v':u'𝗏','w':u'𝗐','x':u'𝗑','y':u'𝗒','z':u'𝗓'}
font_bold = {'A':u'𝗔','B':u'𝗕','C':u'𝗖','D':u'𝗗','E':u'𝗘','F':u'𝗙','G':u'𝗚','H':u'𝗛','I':u'𝗜','J':u'𝗝','K':u'𝗞','L':u'𝗟','M':u'𝗠','N':u'𝗡','O':u'𝗢','P':u'𝗣','Q':u'𝗤','R':u'𝗥','S':u'𝗦','T':u'𝗧','U':u'𝗨','V':u'𝗩','W':u'𝗪','X':u'𝗫','Y':u'𝗬','Z':u'𝗭','a':u'𝗮','b':u'𝗯','c':u'𝗰','d':u'𝗱','e':u'𝗲','f':u'𝗳','g':u'𝗴','h':u'𝗵','i':u'𝗶','j':u'𝗷','k':u'𝗸','l':u'𝗹','m':u'𝗺','n':u'𝗻','o':u'𝗼','p':u'𝗽','q':u'𝗾','r':u'𝗿','s':u'𝘀','t':u'𝘁','u':u'𝘂','v':u'𝘃','w':u'𝘄','x':u'𝘅','y':u'𝘆','z':u'𝘇'}
font_italics = {'A':u'𝘈','B':u'𝘉','C':u'𝘊','D':u'𝘋','E':u'𝘌','F':u'𝘍','G':u'𝘎','H':u'𝘏','I':u'𝘐','J':u'𝘑','K':u'𝘒','L':u'𝘓','M':u'𝘔','N':u'𝘕','O':u'𝘖','P':u'𝘗','Q':u'𝘘','R':u'𝘙','S':u'𝘚','T':u'𝘛','U':u'𝘜','V':u'𝘝','W':u'𝘞','X':u'𝘟','Y':u'𝘠','Z':u'𝘡','a':u'𝘢','b':u'𝘣','c':u'𝘤','d':u'𝘥','e':u'𝘦','f':u'𝘧','g':u'𝘨','h':u'𝘩','i':u'𝘪','j':u'𝘫','k':u'𝘬','l':u'𝘭','m':u'𝘮','n':u'𝘯','o':u'𝘰','p':u'𝘱','q':u'𝘲','r':u'𝘳','s':u'𝘴','t':u'𝘵','u':u'𝘶','v':u'𝘷','w':u'𝘸','x':u'𝘹','y':u'𝘺','z':u'𝘻'}
font_bold_italics = {'A':u'𝘼','B':u'𝘽','C':u'𝘾','D':u'𝘿','E':u'𝙀','F':u'𝙁','G':u'𝙂','H':u'𝙃','I':u'𝙄','J':u'𝙅','K':u'𝙆','L':u'𝙇','M':u'𝙈','N':u'𝙉','O':u'𝙊','P':u'𝙋','Q':u'𝙌','R':u'𝙍','S':u'𝙎','T':u'𝙏','U':u'𝙐','V':u'𝙑','W':u'𝙒','X':u'𝙓','Y':u'𝙔','Z':u'𝙕','a':u'𝙖','b':u'𝙗','c':u'𝙘','d':u'𝙙','e':u'𝙚','f':u'𝙛','g':u'𝙜','h':u'𝙝','i':u'𝙞','j':u'𝙟','k':u'𝙠','l':u'𝙡','m':u'𝙢','n':u'𝙣','o':u'𝙤','p':u'𝙥','q':u'𝙦','r':u'𝙧','s':u'𝙨','t':u'𝙩','u':u'𝙪','v':u'𝙫','w':u'𝙬','x':u'𝙭','y':u'𝙮','z':u'𝙯'}


class Indicator():
    def __init__(self):
        self.app = 'test123'
        iconpath = cwd + '/spotify-art.png'
        self.indicator = AppIndicator3.Indicator.new(self.app, iconpath, AppIndicator3.IndicatorCategory.OTHER)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())
        self.setLabel(metadata)
        self.update = Thread(target=self.show_seconds)
        self.update.setDaemon(True)
        self.update.start()

    def create_menu(self):
        menu = Gtk.Menu()
        item_1 = Gtk.MenuItem('Toggle')
        item_1.connect('activate', self.playPause)
        menu.append(item_1)
        menu_sep = Gtk.SeparatorMenuItem()
        menu.append(menu_sep)
        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect('activate', self.stop)
        menu.append(item_quit)
        menu.show_all()
        return menu

    def playPause(self, something):
        command = "dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause"
        os.system(command)

    def show_seconds(self):
        global trackId
        global playBackStatus
        while True:
            time.sleep(1)
            spotify_properties = spotify_interface.GetAll("org.mpris.MediaPlayer2.Player")
            metadata = spotify_properties['Metadata']
            if trackId != metadata['mpris:trackid']:
                trackId = metadata['mpris:trackid']
                urllib.urlretrieve(metadata['mpris:artUrl'], 'spotify-art.png')
                GObject.idle_add(self.indicator.set_icon, cwd + '/spotify-art.png')
                self.setLabel(metadata)
            if playBackStatus != spotify_properties['PlaybackStatus']:
                playBackStatus = spotify_properties['PlaybackStatus']
                self.setLabel(metadata)

    def setLabel(self, metadata):
        global playBackStatus
        headphones = u'🎧'
        if playBackStatus == 'Playing':
            playing = u'⏵'
        else:
            playing = u'⏸'
        title = (" " + playing + " " + self.set_font(metadata['xesam:title'], 'bold_italics') + self.set_font(" by ", 'italics') + self.set_font(metadata['xesam:artist'][0], 'sans') + "  ")
        GObject.idle_add(self.indicator.set_label, title, self.app, priority=GObject.PRIORITY_DEFAULT)

    def set_font(self, string, style='bold'):
        global font_bold
        new_string = u''
        for char in string:
            if style == 'bold':
                if char in font_bold:
                    new_string += font_bold[char]
                else:
                    new_string += char
            elif style == 'italics':
                if char in font_italics:
                    new_string += font_italics[char]
                else:
                    new_string += char
            elif style == 'sans':
                if char in font_sans:
                    new_string += font_sans[char]
                else:
                    new_string += char
            elif style == 'bold_italics':
                if char in font_bold_italics:
                    new_string += font_bold_italics[char]
                else:
                    new_string += char
        return new_string

    def stop(self, source):
        Gtk.main_quit()

Indicator()
GObject.threads_init()
signal.signal(signal.SIGINT, signal.SIG_DFL)
Gtk.main()
