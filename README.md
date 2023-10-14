# Drone Detector

Capture images from a camera in full resolution and attempt to detect anomalies in the sky.

<div align=center>
    <img src="https://i.imgur.com/VfOyigA.png">
</div>

## Documentation

Preliminary system architecture can be found under `docs/`.

📢 Currently, the code **must run on a 64-bit raspbian OS**! 📢 

## Installation

In a virtual environment, install this package in **editable** mode:
```
pip install -e .
bash install_apt_dependencies.sh
pip install -r requirements.txt
```

For development, also install lint tools:
```
pip install -r dev-requirements.txt
```