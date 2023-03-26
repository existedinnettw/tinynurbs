find_package(Catch2 3 REQUIRED)
find_package(GLM REQUIRED)
add_executable(unittests test_main.cpp
                         test_curve.cpp test_rational_curve.cpp
                         test_surface.cpp test_rational_surface.cpp)
target_link_libraries(unittests PRIVATE Catch2::Catch2WithMain)
# target_include_directories(unittests PRIVATE ${GLM_INCLUDE_DIRS})
# target_link_libraries(unittests PRIVATE glm::glm)
target_link_libraries(unittests PRIVATE tinynurbs)
enable_testing() #no idea why, but after add it here, conan work
add_test(NAME unittests COMMAND unittests)
