[app]
title = CompassApp
package.name = compassapp
package.domain = com.yourname
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
version = 0.1

# CRITICAL: Added pyjnius
requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 1

# ANDROID SPECIFIC
android.api = 33
android.minapi = 21
# CRITICAL: Added sensor permissions
android.permissions = INTERNET, VIBRATE, HIGH_SAMPLING_RATE_SENSORS
android.accept_sdk_license = True