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
    exports_sources = "include/*", "tests/*", "CMakeLists.txt", "cmake/*"
    # We can avoid copying the sources to the build folder in the cache
    no_copy_source = True
    generators = "CMakeToolchain", "CMakeDeps"

    def validate(self):
        check_min_cppstd(self, 14)

    def requirements(self):
        self.requires("glm/[~0.9.9]")
        self.test_requires("catch2/[~2]") #2.13, #for ver3, it's not support gcc5 in conan recipe setting for catch2 ver3.
        self.build_requires("cmake/[>=3.22 <3.26]") #for catch2

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure() #variables={"BUILD_TESTS":True}
        # cmake.configure(build_script_folder="test")
        cmake.build()
        if not self.conf.get("tools.build:skip_test", default=False):
            # cmake = CMake(self)
            # cmake.configure() #variables={"BUILD_TESTS":True}
            # # cmake.configure(build_script_folder="test")
            # cmake.build()
            # self.run(os.path.join(self.cpp.build.bindir, "test_sum"))
            cmake.test()

    def package(self):
        # This will also copy the "include" folder
        copy(self, "*.h", self.source_folder, self.package_folder)
        # cmake = CMake(self)
        # cmake.install()

    def package_id(self):
        self.info.clear()

    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "tinynurbs")
        self.cpp_info.set_property("cmake_target_name", "tinynurbs::tinynurbs")
        # self.cpp_info.bindirs = []
        # self.cpp_info.libdirs = []
