# albert-kde-plugins
Some Albert plugins I've written to make my KDE life more launcher-driven (under Wayland).

## Installation

Each of these plugins comes with an `./install.sh` script in its directory that
installs the plugin into the default Albert Python plugins directory on Linux 
(`$XDG_DATA_HOME/albert/python/plugins/<plugin-name>/`).

## kde_windows

**Default trigger prefix**: `q `

Allows you to search through open windows, kinda like what KRunner does — but in Albert.

This requires you to install [kdotool](https://github.com/jinliu/kdotool),
because [KDE doesn't expose window scripting to DBus](https://invent.kde.org/plasma/kwin/-/issues/243),
which makes life much harder — so I outsource the complexity to `kdotool`.

## kde_night_switch

**Default trigger prefix**: `kns`

Toggles Night Color on KDE. You might have to set Night Color to "always on" for
this to work right.

## koi_theme_switcher

**Default trigger prefix**: `koi `

Controls light mode/dark mode via [Koi](https://github.com/baduhai/Koi).

This depends on [a PR that, as I write this README, hasn't yet been merged into Koi](https://github.com/baduhai/Koi/pull/106),
so if you want to use this and that PR still isn't merged yet, you can use 
[my fork of Koi](https://github.com/spencerwi/Koi/tree/master) temporarily 
(but I don't plan on maintaining that long-term, so you're better off with the 
main Koi repo if the PR *has* been merged by the time you read this).

