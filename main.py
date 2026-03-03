import kivy
kivy.require("2.3.1")

from kivy.app import App
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.animation import Animation
from kivy.clock import Clock

from jnius import autoclass, PythonJavaClass, java_method
from math import degrees

# Android classes
PythonActivity = autoclass("org.kivy.android.PythonActivity")
Context = autoclass("android.content.Context")
SensorManager = autoclass("android.hardware.SensorManager")
Sensor = autoclass("android.hardware.Sensor")


class SensorListener(PythonJavaClass):
    __javainterfaces__ = ["android/hardware/SensorEventListener"]
    __javacontext__ = "app"

    def __init__(self, app, sensor_manager):
        super().__init__()
        self.app = app
        self.sensor_manager = sensor_manager

    @java_method("(Landroid/hardware/SensorEvent;)V")
    def onSensorChanged(self, event):
        # Rotation vector gives better compass accuracy
        rotation_matrix = [0.0] * 9
        orientation = [0.0] * 3

        SensorManager.getRotationMatrixFromVector(
            rotation_matrix, event.values
        )
        SensorManager.getOrientation(rotation_matrix, orientation)

        azimuth = degrees(orientation[0])
        azimuth = (azimuth + 360) % 360

        # Update UI on main thread
        Clock.schedule_once(lambda dt: self.app.update_angle(azimuth))

    @java_method("(Landroid/hardware/Sensor;I)V")
    def onAccuracyChanged(self, sensor, accuracy):
        pass


class CompassImage(Image):
    angle = NumericProperty(0)


class CompassApp(App):
    def build(self):
        self.img = CompassImage(
            source="needle.jpeg",  # Add your needle image
            allow_stretch=True,
            keep_ratio=True,
        )

        activity = PythonActivity.mActivity
        sensor_service = activity.getSystemService(Context.SENSOR_SERVICE)
        self.sensor_manager = sensor_service

        rotation_sensor = self.sensor_manager.getDefaultSensor(
            Sensor.TYPE_ROTATION_VECTOR
        )

        self.listener = SensorListener(self, self.sensor_manager)

        self.sensor_manager.registerListener(
            self.listener,
            rotation_sensor,
            SensorManager.SENSOR_DELAY_GAME,
        )

        return self.img

    def update_angle(self, new_angle):
        anim = Animation(angle=new_angle, d=0.2, t="out_quad")
        anim.start(self.img)
        self.img.canvas.before.clear()
        self.img.canvas.before.add(
            kivy.graphics.PushMatrix()
        )
        self.img.canvas.before.add(
            kivy.graphics.Rotate(
                angle=-new_angle,
                origin=self.img.center,
            )
        )
        self.img.canvas.after.clear()
        self.img.canvas.after.add(
            kivy.graphics.PopMatrix()
        )

    def on_pause(self):
        self.sensor_manager.unregisterListener(self.listener)
        return True

    def on_resume(self):
        activity = PythonActivity.mActivity
        sensor_service = activity.getSystemService(Context.SENSOR_SERVICE)
        self.sensor_manager = sensor_service
        rotation_sensor = self.sensor_manager.getDefaultSensor(
            Sensor.TYPE_ROTATION_VECTOR
        )
        self.sensor_manager.registerListener(
            self.listener,
            rotation_sensor,
            SensorManager.SENSOR_DELAY_GAME,
        )


if __name__ == "__main__":
    CompassApp().run()