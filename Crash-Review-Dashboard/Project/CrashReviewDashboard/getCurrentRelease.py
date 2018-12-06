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
    'Kijiji IT': '594d6206785c7f06d4493c76',
    'Alamaula AR': '592874b196046a66e3feaabe'
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
    if elementcount == 1:
        latestbuildnumber =list(latestbuilddict[0].values())[0]
        print(latestbuildnumber)
    else:
        for x in range(0,elementcount):
            a=list(latestbuilddict[x].values())[0]
            b=a.split(" ")[0].replace(".","")
            latestbuildnumber1=latestbuildnumber.split(" ")[0].replace(".","")
            print(x,a,b,latestbuildnumber1)
            if int(b)>int(latestbuildnumber1):
                latestbuildnumber=a
    print(latestbuildnumber)
    return latestbuildnumber


def get_release_build_number_for_and_country(country):
    headers = {"Authorization": "Bearer abdd6982242fea92221908bf996d9dcba31df046d596ff8b54041b17f9511c9d"}
    url_prefix = 'https://api-dash.fabric.io/graphql?relayDebugName='
    external_id = and_country_externalId_dict[country]
    session = get_session(external_id,headers,url_prefix)
    return session

def get_release_build_number_for_ios_country(country):
    headers = {"Authorization": "Bearer 6a45cc1cb11f44dc3d1198ca3bc818013b82cb7a38646cceec50ba41e5d3a1aa"}
    url_prefix = 'https://api-dash.fabric.io/graphql?relayDebugName='
    external_id = iOS_country_externalId_dict[country]
    session = get_session(external_id,headers,url_prefix)
    return session

def get_all_current_release_build_number_for_ios_country():
    headers = {"Authorization": "Bearer 6a45cc1cb11f44dc3d1198ca3bc818013b82cb7a38646cceec50ba41e5d3a1aa"}
    url_prefix = 'https://api-dash.fabric.io/graphql?relayDebugName='
    countrylist =["Kijiji CA","Gumtree AU","Gumtree ZA","Gumtree UK","Vivanuncios MX","Kijiji IT","Alamaula AR"]
    currentreleaselist = []
    for country in countrylist:
        external_id = iOS_country_externalId_dict[country]
        session = get_session(external_id,headers,url_prefix)
        print(country,session)
        currentreleaselist.append(session)
    return currentreleaselist

def get_all_current_release_build_number_for_and_country():
    headers = {"Authorization": "Bearer abdd6982242fea92221908bf996d9dcba31df046d596ff8b54041b17f9511c9d"}
    url_prefix = 'https://api-dash.fabric.io/graphql?relayDebugName='
    currentreleaselist = []
    countrylist =["Kijiji CA","Gumtree AU","Gumtree ZA","Vivanuncios MX","Kijiji IT","Alamaula AR","Gumtree IE","Gumtree PL"]
    for country in countrylist:
        external_id = and_country_externalId_dict[country]
        session = get_session(external_id,headers,url_prefix)
        print(country,session)
        currentreleaselist.append(session)
    return currentreleaselist


if __name__ == '__main__':
    get_all_current_release_build_number_for_and_country()
