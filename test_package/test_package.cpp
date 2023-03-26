#include <cstdlib>
#include "tinynurbs/tinynurbs.h"

int main (int argc, char * argv[]) {
    tinynurbs::Curve<float> crv; // Planar curve using float32
    crv.control_points = {glm::vec3(-1, 0, 0), // std::vector of 3D points
                        glm::vec3(0, 1, 0),
                        glm::vec3(1, 0, 0)
                        };
    crv.knots = {0, 0, 0, 1, 1, 1}; // std::vector of floats
    crv.degree = 2;
    printf("tinynurbs success include.\n");

    return EXIT_SUCCESS;
}