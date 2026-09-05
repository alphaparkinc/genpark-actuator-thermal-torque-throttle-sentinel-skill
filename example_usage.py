from client import ActuatorThermalTorqueThrottleSentinelClient

def main():
    client = ActuatorThermalTorqueThrottleSentinelClient()
    res = client.evaluate_actuator_thermal_margins()
    print('Actuator Thermal Sentinel: ' + res['sentinel_event_id'] + ' (' + res['joint_id'] + ')')
    print('Temp: ' + str(res['current_temp_celsius']) + 'C (Margin: ' + str(res['thermal_safety_margin_celsius']) + 'C) | State: ' + res['protective_throttle_state'])
    print('Dossier URL: ' + res['actuator_safety_dossier_url'])

if __name__ == '__main__':
    main()
