[app]

title = MyApp
package.name = mykivyapp
package.domain = com.venom

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf

version = 0.1
android.version_code = 1

requirements = python3,kivy

orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 21
android.ndk = 25b
android.enable_androidx = True

android.permissions = INTERNET
android.opengl_es2 = True

log_level = 2