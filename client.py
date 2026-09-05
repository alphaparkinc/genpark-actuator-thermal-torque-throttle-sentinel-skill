class ActuatorThermalTorqueThrottleSentinelClient:
    def evaluate_actuator_thermal_margins(self, joint_id='knee_pitch_joint_fl', current_temp_celsius=68.5, max_safe_temp_celsius=85.0, applied_torque_nm=32.4, continuous_rating_nm=30.0):
        temp_margin = round(max_safe_temp_celsius - current_temp_celsius, 1)
        is_overheating = temp_margin < 10.0
        return {
            'sentinel_event_id': 'act_thm_3301',
            'joint_id': joint_id,
            'current_temp_celsius': current_temp_celsius,
            'thermal_safety_margin_celsius': temp_margin,
            'torque_overload_ratio': round(applied_torque_nm / continuous_rating_nm, 2),
            'protective_throttle_state': 'THROTTLE_REDUCE_20_PCT' if is_overheating else 'NOMINAL_OPERATION',
            'cooldown_advisory_sec': 15 if is_overheating else 0,
            'actuator_safety_dossier_url': 'https://actuators.sentinel.genpark.ai/joints/knee_pitch_joint_fl/health.json'
        }
