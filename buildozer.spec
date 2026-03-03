[app]
# (str) Title of your application
title = CompassApp

# (str) Package name
package.name = compassapp

# (str) Package domain (reverse domain style)
package.domain = com.yourname

# (str) Source code location
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,ttf

# (str) Application version
version = 0.1

# (list) Application requirements
# Added pyjnius and pinned Cython for build stability
requirements = python3,kivy,pyjnius,cython==0.29.33

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 1

# =================================================================
# Android specific configuration
# =================================================================

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK directory (if empty, it will be auto-installed)
# android.sdk = 

# (str) Android NDK version (FIX: pinned to stable 25b)
android.ndk = 25b

# (int) Android NDK API to use (Match with minapi)
android.ndk_api = 21

# (list) Permissions
android.permissions = INTERNET, VIBRATE, HIGH_SAMPLING_RATE_SENSORS

# (bool) Skip checking of the NDK/SDK versions (set to False)
android.skip_update = False

# (bool) Accept SDK license
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# =================================================================
# Buildozer settings
# =================================================================

# (int) Log level (2 = verbose, helpful for debugging)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1