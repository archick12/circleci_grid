from testrail_api import TestRailAPI

if __name__ == '__main__':
    api = TestRailAPI("https://piluck.testrail.io", "a.a.piluck@gmail.com", "rusiiS8CqY9hVuaH/sM2-ylp5Z2rSieshDNcGS1zw")
    result = api.results.add_result_for_case(
        run_id=1,
        case_id=1,
        status_id=1,
        comment="Pass",
        version="1"
    )