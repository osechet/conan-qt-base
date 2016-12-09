
import os
from conans import ConanFile, CMake
from conans.tools import os_info

# This easily allows to copy the package in other user or channel
CHANNEL = os.getenv("CONAN_CHANNEL", "testing")
USERNAME = os.getenv("CONAN_USERNAME", "osechet")

class QtBaseTestConan(ConanFile):
    """ Qt Base Conan package test """

    requires = "QtBase/5.6.2@%s/%s" % (USERNAME, CHANNEL)
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake", "virtualenv"

    def build(self):
        cmake = CMake(self.settings)
        if os_info.is_windows and self.settings.compiler == "gcc":
            # When using MinGW Makefiles, CMake complains if sh is in the path.
            # Since icu's configure needs sh, we force CMake to use 'Unix Makefiles'
            self.run('cmake "%s" %s -G "Unix Makefiles"'
                     % (self.conanfile_directory, cmake.command_line))
        else:
            self.run('cmake "%s" %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def test(self):
        if self.settings.os == "Windows":
            self.run("activate && %s %s" % (os.sep.join([".", "bin", "helloworld"]), "conan"))
            self.run("activate && %s %s" % (os.sep.join([".", "bin", "helloworld2"]), "conan"))
            #self.run("activate && %s %s" % (os.sep.join([".", "bin", "hellogui"]), "conan"))
        else:
            self.run("%s %s" % (os.sep.join([".", "bin", "helloworld"]), "conan"))
            self.run("%s %s" % (os.sep.join([".", "bin", "helloworld2"]), "conan"))
            #self.run("%s %s" % (os.sep.join([".", "bin", "hellogui"]), "conan"))
