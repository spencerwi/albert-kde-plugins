#!/bin/bash

INSTALL_DIR="$XDG_DATA_HOME/albert/python/plugins/kde_windows"
if [ ! -d "$INSTALL_DIR" ] ; then
	mkdir -p "$INSTALL_DIR"
fi
cp __init__.py "$INSTALL_DIR/__init__.py"
