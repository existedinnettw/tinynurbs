import os
from conan import ConanFile
from conan.tools.files import copy
from conan.tools.cmake import cmake_layout, CMake
from conan.tools.build import check_min_cppstd

class SumConan(ConanFile):
    '''
    ref
    ---
    https://github.com/conan-io/examples2/blob/main/tutorial/creating_packages/other_packages/header_only_gtest/conanfile.py
    '''
    name = "tinynurbs"
    version = "0.1"
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "include/*", "tests/*"
    # We can avoid copying the sources to the build folder in the cache
    no_copy_source = True
    generators = "CMakeToolchain", "CMakeDeps"

    def validate(self):
        check_min_cppstd(self, 14)

    def requirements(self):
        self.requires("glm/[~0.9.9]")
        self.test_requires("catch2/[~2.13]")

    def layout(self):
        cmake_layout(self)

    def build(self):
        if not self.conf.get("tools.build:skip_test", default=False):
            cmake = CMake(self)
            cmake.configure(build_script_folder="tests") #variables={"BUILD_TESTS":True}
            # cmake.configure(build_script_folder=".")
            cmake.build()
            # self.run(os.path.join(self.cpp.build.bindir, "test_sum"))
            cmake.test()

    def package(self):
        # This will also copy the "include" folder
        copy(self, "*.h", self.source_folder, self.package_folder)

    def package_id(self):
        self.info.clear()
