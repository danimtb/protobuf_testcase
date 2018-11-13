import os
from conans import ConanFile


class Protoc(ConanFile):
    name = "protoc_installer"
    version = "1.0"
    build_requires = "protobuf/1.0@conan/stable"

    def package_info(self):
            self.env_info.path.append(os.path.join(self.package_folder, "protoc_folder"))
            self.env_info.PROTOC_BIN = os.path.normpath(os.path.join(self.package_folder, "protoc_folder", "bin", "protoc.exe"))