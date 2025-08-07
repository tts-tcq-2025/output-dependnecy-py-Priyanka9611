alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    return 200
    
def test_failed_alert(f):
    global alert_failure_count, network_alert_stub
    alert_failure_count = 0

    def fail_stub(c):
        return 500

    network_alert_stub = fail_stub
    alert_in_celcius(f)
    assert alert_failure_count == 1
    
def test_success_alert(f):
    global alert_failure_count, network_alert_stub
    alert_failure_count = 0

    def success_stub(c):
        return 500

    network_alert_stub = success_stub
    alert_in_celcius(f)
    assert alert_failure_count == 0
    
def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0


alert_in_celcius(400.5)
alert_in_celcius(303.6)
test_failed_alert(400.5)
test_success_alert(300)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
