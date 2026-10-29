#pragma once
#include <algorithm>
#include <cmath>
#include <cstddef>

namespace lfr {
static const std::size_t kSensorCount = 14;

struct Calibration {
    float minimum[kSensorCount];
    float maximum[kSensorCount];
    float threshold = 0.15f; // normalized activation threshold, configurable
};

struct Position {
    bool line_detected;
    float error; // normalized [-1, +1]; negative = left, positive = right
};

inline float clamp(float value, float low, float high) {
    return std::max(low, std::min(value, high));
}

inline Position estimate_position(const float normalized[kSensorCount],
                                  float activation_threshold = 0.15f) {
    float weighted_sum = 0.0f, total = 0.0f;
    for (std::size_t i = 0; i < kSensorCount; ++i) {
        const float v = clamp(normalized[i], 0.0f, 1.0f);
        if (v >= activation_threshold) {
            const float coordinate = -1.0f + 2.0f * static_cast<float>(i) /
                                             static_cast<float>(kSensorCount - 1);
            weighted_sum += coordinate * v;
            total += v;
        }
    }
    if (total <= 1e-6f) return {false, 0.0f};
    return {true, clamp(weighted_sum / total, -1.0f, 1.0f)};
}

inline float normalize_adc(float raw, float minimum, float maximum,
                           bool line_is_high = true) {
    if (maximum <= minimum) return 0.0f;
    float v = clamp((raw - minimum) / (maximum - minimum), 0.0f, 1.0f);
    return line_is_high ? v : 1.0f - v;
}

struct PidConfig { float kp = 0.7f, ki = 0.0f, kd = 0.02f, integral_limit = 0.5f; };
struct PidState { float integral = 0.0f, previous_error = 0.0f; bool initialized = false; };

inline float pid_step(float error, float dt_seconds, const PidConfig& cfg, PidState& state) {
    if (!(dt_seconds > 0.0f) || !std::isfinite(dt_seconds)) return 0.0f;
    state.integral = clamp(state.integral + error * dt_seconds,
                           -cfg.integral_limit, cfg.integral_limit);
    const float derivative = state.initialized ? (error - state.previous_error) / dt_seconds : 0.0f;
    state.previous_error = error;
    state.initialized = true;
    return cfg.kp * error + cfg.ki * state.integral + cfg.kd * derivative;
}

struct MotorCommand { float left; float right; };
inline MotorCommand mix_and_limit(float base, float correction, float max_command = 1.0f) {
    max_command = clamp(max_command, 0.0f, 1.0f);
    return {clamp(base + correction, -max_command, max_command),
            clamp(base - correction, -max_command, max_command)};
}
} // namespace lfr
