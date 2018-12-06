import json
import requests
from datetime import datetime
import datetime
import time

app_version = '6.16.0'
build_number = '14990'


and_country_externalId_dict = {
    'Gumtree AU': '5925cf3cf08b0a7026ef6f14',
    'Kijiji CA': '5925d905f08b0a6fddef6f3a',
    'Kijiji IT': '5925d92a65d380459d102175',
    'Gumtree ZA': '5925d8e0a1954846ff3d15f5',
    'Vivanuncios MX': '5925d94f96046a6689feaaae',
    'Gumtree PL': '5925cdafa7ec2842352e28e5',
    'Alamaula AR': '58dbe22b1b5c090a942f5dd9',
    'Gumtree IE': '58a33e08a25bb81820bcd6d6'
}


def set_time():
    """set the searching start_time and end_time
    :return: start_time,end_time
    """
    sync_hour = '08:00:00'
    suffix_time = '07:59:59'
    current_day = datetime.datetime.now()
    current_hour = datetime.datetime.now().strftime('%H:%M:%S')

    if current_hour > sync_hour:
        tomorrow_day = current_day + datetime.timedelta(days=+1)
        end_day = tomorrow_day.strftime('%Y-%m-%d')
        start_day = (current_day + datetime.timedelta(days=-6)).strftime('%Y-%m-%d')
    else:
        end_day = current_day.strftime('%Y-%m-%d')
        start_day = (current_day + datetime.timedelta(days=-7)).strftime('%Y-%m-%d')
    end = end_day + ' ' + suffix_time
    start = start_day + ' ' + sync_hour

    end_time = int(time.mktime(time.strptime(end, "%Y-%m-%d %H:%M:%S")))
    start_time = int(time.mktime(time.strptime(start, "%Y-%m-%d %H:%M:%S")))

    print(end_time)
    print(start_time)
    return start_time, end_time


def get_session(external_id, start_time, end_time, headers, url_prefix, build_version):
    """fetch session response from firebase, parse out session data, and return the sum session
    :return: total_session data
    """
    total_session = 0
    session_url = url_prefix + "SessionAndUserMetrics"
    session_data = {
        "query": "query SessionAndUserMetrics($externalId_0:String!,$start_1:UnixTimestamp!,$end_2:UnixTimestamp!) {project(externalId:$externalId_0) {answers {_totalSessionsForBuilds322SY4:totalSessionsForBuilds(synthesizedBuildVersions:[\"" + build_version + "\"],start:$start_1,end:$end_2) {synthesizedBuildVersion,values {timestamp,value}},_dauByBuilds1UDP3H:dauByBuilds(builds:[\"" + build_version + "\"],start:$start_1,end:$end_2) {scalar,values {timestamp,value}}},id}}",
        "variables": {"externalId_0": external_id, "start_1": start_time, "end_2": end_time}}
    session_request = requests.post(session_url, json=session_data, headers=headers)
    content = json.loads(session_request.content)
    content_1 = content.get('data').get('project').get('answers')
    content_2 = [value for key, value in content_1.items() if '_totalSessionsForBuilds']
    content_3 = content_2[0][0].get('values')
    print("7 days session list")
    for i in range(0, len(content_3)):
        a = content_3[i].get('value')
        print(a)
        total_session += a
    print("total_session")
    print(total_session)
    return total_session


def get_crash(external_id, start_time, end_time, headers, url_prefix, build_version):
    """
    fetch crash response from firebase, parse out crash data, and return the sum crash
    :return: total_crash data
    """
    crash_url = url_prefix + 'AppTimeseries'
    crash_data = {
        "query": "query AppTimeseries($externalId_0:String!,$type_1:IssueType!,$start_2:UnixTimestamp!,$end_3:UnixTimestamp!,$granularity_4:TimeseriesGranularity!,$filters_5:IssueFiltersType!) {project(externalId:$externalId_0) {crashlytics {_appTimeseries3IQOvl:appTimeseries(synthesizedBuildVersions:[\"" + build_version + "\"],type:$type_1,start:$start_2,end:$end_3,granularity:$granularity_4,filters:$filters_5) {eventsCount,impactedDevices}},id}}",
        "variables": {"externalId_0": external_id, "type_1": "crash", "start_2": start_time, "end_3": end_time, "granularity_4": "day", "filters_5": {}}}
    crash_request = requests.post(crash_url, json=crash_data, headers=headers)
    content_4 = json.loads(crash_request.content)
    total_crash = 0
    content_5 = content_4.get('data').get('project').get('crashlytics')
    content_6 = [value for key, value in content_5.items() if '_appTimeseries']
    print("7 days crash list")
    for i in content_6[0].get('eventsCount'):
        i = i[1]
        print(i)
        total_crash += i
    print("total_crash")
    print(total_crash)
    return total_crash


def get_crash_rate_for_country(country):
    build_version = app_version + " (" + build_number + ")"
    headers = {"Authorization": "Bearer af6c7d0c6e1d0d8403af6d555f3a4c8e037caac84e631c998ef80376f2f9abfe"}
    url_prefix = 'https://api-dash.fabric.io/graphql?relayDebugName='
    time = set_time()
    start_time = time[0]
    end_time = time[1]

    # count out the crash session
    print("===="+country+"====")
    external_id = and_country_externalId_dict[country]
    crash_session = '0%'
    attachment = {
        "country": country,
        "version_number": app_version,
        "build_number": build_number,
        "crash_rate": crash_session
    }
    session = get_session(external_id, start_time, end_time, headers, url_prefix, build_version)
    crash = get_crash(external_id, start_time, end_time, headers, url_prefix, build_version)
    if session > 0 and crash > 0:
        crash_session = ('%.2f%%' % (crash / session * 100))
        attachment['crash_rate'] = crash_session
        print("crash rate")
        print(crash_session)
    else:
        print("0 crash, no need to send data")
        attachment['crash_rate'] = crash_session
        print("crash rate")
        print(crash_session)
    return crash_session


if __name__ == '__main__':
    get_crash_rate_for_country('Gumtree AU')
