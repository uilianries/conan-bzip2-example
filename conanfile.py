from conans import ConanFile, CMake


class FoobarConan(ConanFile):
    name = "foobar"
    version = "0.1.0"
    license = "MIT"
    url = "https://github.com/uilianries/conan-bzip2-example"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*"
    requires = "bzip2/1.0.6@conan/stable"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.install()
