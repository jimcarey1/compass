[app]

# (str) Title of your application
title = MyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (reverse domain style)
package.domain = com.venom

# (str) Source code location
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json,ttf

# (str) Application version
version = 0.1

# (int) Android version code (increment for every Play Store update)
android.version_code = 1

# (list) Requirements
requirements = python3,kivy

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 1

# ----------------------------------------------------------------
# ANDROID CONFIGURATION
# ----------------------------------------------------------------

# Target Android API
android.api = 33

# Minimum supported API
android.minapi = 21

# NDK version (stable)
android.ndk = 25b

# Stable build tools (avoid preview versions)
android.build_tools = 33.0.2

# Permissions
android.permissions = INTERNET

# Use OpenGL ES 2
android.opengl_es2 = True

# Accept SDK licenses automatically (important for CI)
android.accept_sdk_license = True

# Use SDL2 bootstrap (default for Kivy)
android.bootstrap = sdl2

# ----------------------------------------------------------------
# DEBUGGING
# ----------------------------------------------------------------

# Log level (2 = verbose, good for CI debugging)
log_level = 2