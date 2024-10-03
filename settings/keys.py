# Qtile keybindings

from libqtile.config import Key
# from libqtile.command import lazy
from libqtile.lazy import lazy

mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "a", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # Switch window focus to other pane(s) of stack
    ([mod], "space", lazy.layout.next()),

    # ------------ App Configs ------------

    # Menu
    ([mod, "shift"], "Return", lazy.spawn("rofi -show run")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "f", lazy.spawn("firefox")),
    #([mod, "shift"], "g", lazy.spawn("google-chrome-stable")),

    # File Explorer
    ([mod], "t", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Code
    ([mod], "c", lazy.spawn("code-oss")),
    ([mod], "i", lazy.spawn("idea")),

    # Box Machine
    ([mod], "v", lazy.spawn("virt-manager")),

    # DataBase
    ([mod], "d", lazy.spawn("dbeaver")),

    # VideoEditor
    ([mod], "k", lazy.spawn("kdenlive")),
    ([mod], "z", lazy.spawn("shotcut")),

    # AudioEditor
    ([mod], "a", lazy.spawn("audacity")),

    # Photo Editor
    ([mod], "g", lazy.spawn("gimp")),

    # Pulseeffects
    ([mod], "e", lazy.spawn("easyeffects")),

    # Office
    ([mod], "l", lazy.spawn("libreoffice")),

    # Unity
    #([mod], "u", lazy.spawn("unityhub")),

    # Spotify
    ([mod], "s", lazy.spawn("spotube")),

    # Torrent
    ([mod], "q", lazy.spawn("qbittorrent")),

    # ScreenRecorder
    ([mod], "r", lazy.spawn("simplescreenrecorder")),

    # Games
    #([mod, "shift"], "l", lazy.spawn("lutris")),
    #([mod, "shift"], "s", lazy.spawn("steam")),

    # Screenshot
    ([], "Print", lazy.spawn("flameshot gui")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl -- set-sink-volume 0 -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl -- set-sink-volume 0 +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl -- set-sink-mute 0 toggle"
    )),

    # Brightness

    ([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
    ([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),

    ([mod], "m", lazy.spawn("xrandr --output eDP --brightness 1")),
    ([mod], "n", lazy.spawn("xrandr --output eDP --brightness .5")),

    # Player controls
    ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    ([], "XF86AudioNext", lazy.spawn("playerctl next")),
    ([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
]]
