from conans import ConanFile


class Consumer(ConanFile):
    requires = "protobuf/1.0@conan/stable"
    build_requires = "protoc_installer/1.0@conan/stable"
    generators = "cmake"