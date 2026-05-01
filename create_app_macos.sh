#!/bin/bash
# Create macOS app for ProtectLayer GUI Launcher

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
APP_NAME="ProtectLayer"
APP_PATH="$HOME/Applications/${APP_NAME}.app"
CONTENTS_DIR="$APP_PATH/Contents"
MACOS_DIR="$CONTENTS_DIR/MacOS"

echo "Creating ${APP_NAME} macOS application..."

# Create directory structure
mkdir -p "$MACOS_DIR"

# Create executable script
cat > "$MACOS_DIR/$APP_NAME" << 'APPSCRIPT'
#!/bin/bash
cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")/../.."
python3 gui_launcher.py
APPSCRIPT

chmod +x "$MACOS_DIR/$APP_NAME"

# Create Info.plist
cat > "$CONTENTS_DIR/Info.plist" << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleDevelopmentRegion</key>
    <string>en</string>
    <key>CFBundleExecutable</key>
    <string>ProtectLayer</string>
    <key>CFBundleName</key>
    <string>ProtectLayer</string>
    <key>CFBundleVersion</key>
    <string>1.0</string>
</dict>
</plist>
PLIST

echo "✅ ProtectLayer.app created in ~/Applications/"
echo ""
echo "You can now launch ProtectLayer from Applications folder"
