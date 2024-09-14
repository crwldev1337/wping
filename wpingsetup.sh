#!/bin/bash
WPING="wping.py"
WPING_ALIAS="wping"

chmod +x "$WPING"
sudo cp "$WPING" "/usr/local/bin/$WPING_ALIAS"
