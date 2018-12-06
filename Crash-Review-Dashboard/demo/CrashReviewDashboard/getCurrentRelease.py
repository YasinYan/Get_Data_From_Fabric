import json
import requests
from datetime import datetime
import datetime
import time
from sys import argv


and_country_externalId_dict = {
    'Kijiji CA': '5925d905f08b0a6fddef6f3a',
    'Gumtree AU': '5925cf3cf08b0a7026ef6f14',
    'Gumtree ZA': '5925d8e0a1954846ff3d15f5',
    'Vivanuncios MX': '5925d94f96046a6689feaaae',
    'Kijiji IT': '5925d92a65d380459d102175',
    'Alamaula AR': '58dbe22b1b5c090a942f5dd9',
    'Gumtree IE': '58a33e08a25bb81820bcd6d6',
    'Gumtree PL': '5925cdafa7ec2842352e28e5'
}

iOS_country_externalId_dict = {
    'Kijiji CA': '594d60bb5547417471ed2c13',
    'Gumtree AU': '594d6234c491f84d66c0c220',
    'Gumtree ZA': '594d632865d380586e213c38',
    'Gumtree UK': '594d629d9c0aed3faa0cc192',
    'Vivanuncios MX': '594d6469e499b51b661c064b',
    'Kijiji IT': '594d6206785c7f06d4493c76',#need get new accout to check IT
    'Alamaula AR': '592874b196046a66e3feaabe',
    #'Gumtree IE': '594d6268ce404261e3a8edac'
}

def get_session(external_id,headers, url_prefix):
    """fetch session response from firebase, parse out session data, and return the sum session
    :return: total_session data
    """
    total_session = 0
    session_url = url_prefix + "Project_route"
    session_data = {
	"query": "query Project_route($externalId_0:String!) {project(externalId:$externalId_0) {id,...F2}} fragment F0 on ProjectVersion {id,externalId} fragment F1 on Project {id,externalId} fragment F2 on Project {answers {_topBuilds3bGBpV:topBuilds(first:3,days:7) {synthesizedBuildVersion}},_versions4zJYbv:versions(first:100,omitVersionsWithNoEvents:true,days:90) {edges {node {id,externalId,pinned,sortOrder,name,...F0},cursor},pageInfo {hasNextPage,hasPreviousPage}},id,...F1}",
	"variables": {"externalId_0": external_id}
		}
    session_request = requests.post(session_url, json=session_data, headers=headers)
    content = json.loads(session_request.content.decode('utf-8'))
    content_1 = content.get('data').get('project').get('answers')
    latestbuilddict = list(content_1.values())[0]
    elementcount = len(latestbuilddict)
    latestbuildnumber = '0.0.0 (0)'
    for x in (0,elementcount-1):
        a=list(latestbuilddict[x].values())[0]
        b=a.split(" ")[0].replace(".","")
        latestbuildnumber1=latestbuildnumber.split(" ")[0].replace(".","")
        if int(b)>int(latestbuildnumber1):
            latestbuildnumber=a
    print(latestbuildnumber)
    return latestbuildnumber


def get_release_build_number_for_and_country(country):
    headers = {"Authorization": "Bearer 0d8e94e416488cb31c175ac54ae3a61791b6237f95758caf3e2036c73c3f446f"}
    url_prefix = 'https://api-dash.fabric.io/graphql?relayDebugName='
    external_id = and_country_externalId_dict[country]
    session = get_session(external_id,headers,url_prefix)
    return session

def get_release_build_number_for_ios_country(country):
	headers = {"Authorization": "Bearer 6f55338e9f6a3e6c3176f538a7a4c48abc6bd9d864ef478f1b5471588b65cce6"}
	url_prefix = 'https://api-dash.fabric.io/graphql?relayDebugName='
	external_id = iOS_country_externalId_dict[country]
	session = get_session(external_id,headers,url_prefix)
	return session

def get_all_current_release_build_number_for_ios_country():
    headers = {"Authorization": "Bearer 6f55338e9f6a3e6c3176f538a7a4c48abc6bd9d864ef478f1b5471588b65cce6"}
    url_prefix = 'https://api-dash.fabric.io/graphql?relayDebugName='
    currentreleaselist = []
    for country in list(iOS_country_externalId_dict.keys()):
        external_id = iOS_country_externalId_dict[country]
        session = get_session(external_id,headers,url_prefix)
        currentreleaselist.append(session)
    return currentreleaselist

def get_all_current_release_build_number_for_and_country():
    headers = {"Authorization": "Bearer 0d8e94e416488cb31c175ac54ae3a61791b6237f95758caf3e2036c73c3f446f"}
    url_prefix = 'https://api-dash.fabric.io/graphql?relayDebugName='
    currentreleaselist = []
    for country in list(and_country_externalId_dict.keys()):
        external_id = and_country_externalId_dict[country]
        session = get_session(external_id,headers,url_prefix)
        currentreleaselist.append(session)
    return currentreleaselist


if __name__ == '__main__':
    get_release_build_number_for_ios_country('Kijiji CA')
