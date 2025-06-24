#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="HandGestureController",
    version="1.0.0",
    description="Control presentations with hand gestures detected via webcam",
    author="User",
    packages=find_packages(),
    install_requires=[
        "opencv-python>=4.5.0",
        "mediapipe>=0.8.0",
        "numpy>=1.20.0",
        "PyMuPDF>=1.18.0",
    ],
    entry_points={
        'console_scripts': [
            'hand-gesture-controller=app:main',
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)