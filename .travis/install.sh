#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    brew update || brew update
    brew outdated pyenv || brew upgrade pyenv
    brew install pyenv-virtualenv
    brew install cmake || true

    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi

    pyenv install 2.7.10
    pyenv virtualenv 2.7.10 conan
    pyenv rehash
    pyenv activate conan
elif [[ "$(uname -s)" == 'Linux' ]]; then
    sudo apt-get install -y libgl1-mesa-dev libxcb1 libxcb1-dev \
        libx11-xcb1 libx11-xcb-dev libxcb-keysyms1 libxcb-keysyms1-dev \
        libxcb-image0 libxcb-image0-dev libxcb-shm0 libxcb-shm0-dev \
        libxcb-icccm4 libxcb-icccm4-dev libxcb-sync1 libxcb-sync-dev \
        libxcb-xfixes0-dev libxrender-dev libxcb-shape0-dev \
        libxcb-randr0-dev libxcb-render-util0 libxcb-render-util0-dev \
        libxcb-glx0-dev libxcb-xinerama0 libxcb-xinerama0-dev
fi

pip install conan_package_tools # It install conan too
conan user
