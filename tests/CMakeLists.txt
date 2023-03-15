find_package(Catch2 3 REQUIRED)
add_executable(unittests test_main.cpp
                         test_curve.cpp test_rational_curve.cpp
                         test_surface.cpp test_rational_surface.cpp)
target_link_libraries(unittests PRIVATE Catch2::Catch2WithMain)
target_include_directories(unittests PRIVATE ${GLM_INCLUDE_DIRS})
target_link_libraries(unittests PUBLIC tinynurbs::tinynurbs)
add_test(NAME unittests COMMAND unittests)
