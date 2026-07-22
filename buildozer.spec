[app]

title = HashGuard
package.name = hashguard
package.domain = org.hashguard

source.dir = app
source.include_exts = py,png,jpg,jpeg,kv,json,txt

version = 1.0

requirements = python3,kivy,kivymd,psutil

orientation = portrait
fullscreen = 0

# Android settings
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WAKE_LOCK

# App icon (optional)
# icon.filename = app/icon.png

# Splash screen (optional)
# presplash.filename = app/presplash.png

# Window size (desktop only)
window.width = 360
window.height = 640

# Logging
log_level = 2

[buildozer]

warn_on_root = 1

# Build output directory
build_dir = .buildozer

# Bin directory
bin_dir = bin
