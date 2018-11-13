from conans import ConanFile


class Protobuf(ConanFile):
    name = "protobuf"
    version = "1.0"
    options = {"lite": [True, False]}
    default_options = {"lite": False}

    def package_info(self):
        if self.options.lite == "lite":
            self.cpp_info.libs = ["libprotobuf-lite"]
        else:
            self.cpp_info.libs = ["libprotobuf", "libprotoc"]
