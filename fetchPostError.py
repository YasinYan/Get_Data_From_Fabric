
# this script is to get post ad error log from fabric, currently only implement for build 19402 CA.
# it will new api_error_text to record all api error and save the matched error payload to post_ad_error_payload.txt


import requests
import json

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
external_id = and_country_externalId_dict['Kijiji CA']
url_prefix = 'https://api-dash.fabric.io/graphql?relayDebugName='
post_error_url = url_prefix + "SingleSession"
pageDirection_2 = "previous"
pageTime_1 = ""
highlight_text = 'You must enter information in the highlighted'

latest_session_data = {
    "query": "query SingleSession($externalId_0:String!) {project(externalId:$externalId_0) {crashlytics {_session3LQIK9:session(externalId:\"latest\",issueId:\"5be4849ef8b88c296318b661\") {externalId,createdAt,buildVersionId,prevSessionId,nextSessionId,sdk {display},os {platform,build,display,name,modified},orientation {device,ui},customLogs {time,message},customKeys {key,value},memory {free,used},storage {free,used},device {architecture,manufacturer,model,name,proximityOn,betaDeviceToken},user {externalId,name,email},stacktraces {exceptions {caption {title,subtitle},interesting,fatal,state,threadName,queueName,crash {name,code,address},exception {message,type,nested},frames {file,offset,line,address,symbol,rawSymbol,owner,library,blamed,native}},errors {caption {title,subtitle},interesting,fatal,state,threadName,queueName,crash {name,code,address},exception {message,type,nested},frames {file,offset,line,address,symbol,rawSymbol,owner,library,blamed,native}},threads {caption {title,subtitle},interesting,fatal,state,threadName,queueName,crash {name,code,address},exception {message,type,nested},frames {file,offset,line,address,symbol,rawSymbol,owner,library,blamed,native}}}}},id}}",
    "variables": {"externalId_0": external_id}}


def get_latest_post_error_log(post_error_url, latest_session_data, headers):
    post_error_log = requests.post(post_error_url, json=latest_session_data, headers=headers)
    pageTime_1 = get_pageTime_1(post_error_log)
    return post_error_log, pageTime_1


def get_previous_post_error_log(post_error_url, session_data, headers):
    post_error_log = requests.post(post_error_url, json=session_data, headers=headers)
    pageTime_1 = get_pageTime_1(post_error_log)
    return pageTime_1


def get_pageTime_1(post_error_log):
    content_json = json.loads(post_error_log.content.decode('utf-8'))
    crashlytics_content = content_json.get('data').get('project').get('crashlytics')
    session_content = [value for key, value in crashlytics_content.items()]
    pageTime_1 = session_content[0].get('createdAt')
    post_error_content = session_content[0].get('stacktraces').get('exceptions')[0]['caption']['subtitle']
    # get('subtitle')

    api_error = post_error_content.split(":")[1]
    save_the_file("api_error.txt",api_error)
    print(api_error)
    if (highlight_text in api_error):
        print(api_error)
        save_the_file("post_ad_error_payload.txt",post_error_content)
    return pageTime_1


def save_the_file(filename,text):
    fo = open(filename, "a")
    fo.write("\n" + text)
    fo.close()

def get_latest_log_of_num(num):
    headers = {"Authorization": "Bearer f046f6fb852cc92b13802fc904a20cd3cb81d1fa66a334780566e1d9fba7c14c",
           "X-CRASHLYTICS-DEVELOPER-TOKEN": "0bb5ea45eb53fa71fa5758290be5a7d5bb867e77"}
    pageTime_1 = get_latest_post_error_log(post_error_url, latest_session_data, headers)[1]

    for index in range(num):
        session_data = {
            "query": "query SingleSession($externalId_0:String!,$pageTime_1:UnixMsTimestamp!,$pageDirection_2:CrashSessionPaginationDirection!) {project(externalId:$externalId_0) {crashlytics {_session4s68lg:session(issueId:\"5be4849ef8b88c296318b661\",pageTime:$pageTime_1,pageDirection:$pageDirection_2) {externalId,createdAt,buildVersionId,prevSessionId,nextSessionId,sdk {display},os {platform,build,display,name,modified},orientation {device,ui},customLogs {time,message},customKeys {key,value},memory {free,used},storage {free,used},device {architecture,manufacturer,model,name,proximityOn,betaDeviceToken},user {externalId,name,email},stacktraces {exceptions {caption {title,subtitle},interesting,fatal,state,threadName,queueName,crash {name,code,address},exception {message,type,nested},frames {file,offset,line,address,symbol,rawSymbol,owner,library,blamed,native}},errors {caption {title,subtitle},interesting,fatal,state,threadName,queueName,crash {name,code,address},exception {message,type,nested},frames {file,offset,line,address,symbol,rawSymbol,owner,library,blamed,native}},threads {caption {title,subtitle},interesting,fatal,state,threadName,queueName,crash {name,code,address},exception {message,type,nested},frames {file,offset,line,address,symbol,rawSymbol,owner,library,blamed,native}}}}},id}}",
            "variables": {"externalId_0": external_id,
                          "pageTime_1": pageTime_1,
                          "pageDirection_2": pageDirection_2}}
        headers = {"Authorization": "Bearer f046f6fb852cc92b13802fc904a20cd3cb81d1fa66a334780566e1d9fba7c14c",
                   "X-CRASHLYTICS-DEVELOPER-TOKEN": "0bb5ea45eb53fa71fa5758290be5a7d5bb867e77"}
        pageTime_1 = get_previous_post_error_log(post_error_url, session_data, headers)

get_latest_log_of_num(1000)
