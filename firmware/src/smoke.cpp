#include <iostream>
#include "lfr_control.hpp"
int main() {
    float s[lfr::kSensorCount] = {};
    s[6] = 1.0f; s[7] = 1.0f;
    const lfr::Position p = lfr::estimate_position(s);
    lfr::PidState state;
    const float correction = lfr::pid_step(p.error, 0.01f, lfr::PidConfig(), state);
    const lfr::MotorCommand cmd = lfr::mix_and_limit(0.4f, correction);
    std::cout << "line_detected=" << p.line_detected
              << " error=" << p.error
              << " left=" << cmd.left << " right=" << cmd.right << "\n";
    return p.line_detected ? 0 : 1;
}
