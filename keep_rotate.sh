#!/bin/bash

SCRIPT_NAME="rotation.sh"
SCRIPT_SOURCE="$(pwd)/$SCRIPT_NAME"
SCRIPT_DEST="$HOME/.local/bin/$SCRIPT_NAME"
DESKTOP_FILE="$HOME/.config/autostart/rotation.desktop"

if [[ ! -f $SCRIPT_SOURCE ]]; then
    echo "Source script $SCRIPT_SOURCE does not exist."
    exit 1
fi

mkdir -p "$HOME/.local/bin"

cp "$SCRIPT_SOURCE" "$SCRIPT_DEST"
chmod +x "$SCRIPT_DEST"

cat << EOF > "$DESKTOP_FILE"
[Desktop Entry]
Type=Application
Exec=$SCRIPT_DEST
Hidden=false
NoDisplay=false
X-GNOME-Automatic-Start=true
X-GNOME-Autostart-enabled=true
Name=Rotation Script
EOF

echo "The $SCRIPT_NAME has been added to autostart."