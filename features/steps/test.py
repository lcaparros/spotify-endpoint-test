from features.log import get_custom_logger
import requests
import json
from utils import *
from behave import *

log = get_custom_logger()


@Given('An artist ID such as {artist_id}')
def given_an_artist_id(context, artist_id):
    # Actually this method is not necessary, but I include it thinking of we could want to get the artist_id from
    # Spotify API too
    context.artist_id = artist_id
    log.info("Artist Id: " + artist_id)


@when('The artist information is requested')
def request_is_sent(context):
    headers = {
        'Authorization': context.token,
        'Content-Type': "application/json",
        'Accept': "application/json"
    }

    response = requests.request("GET", context.url + context.artist_id, headers=headers)
    context.response = response
    log.info(pretty_request(response.request))


@when('The artist information is requested with no ID')
def request_is_sent_with_no_id(context):
    headers = {
        'Authorization': context.token,
        'Content-Type': "application/json",
        'Accept': "application/json"
    }

    response = requests.request("GET", context.url, headers=headers)
    context.response = response
    log.info(pretty_request(response.request))


@when('The artist information is requested with a non valid OAuth security token')
def request_is_sent_with_no_id(context):
    headers = {
        'Authorization': "Bearer non valid token",
        'Content-Type': "application/json",
        'Accept': "application/json"
    }

    response = requests.request("GET", context.url, headers=headers)
    context.response = response
    log.info(pretty_request(response.request))


@then('A {code} http response code is received')
def response_code_is(context, code):
    log.info(pretty_response(context.response))
    assert context.response.status_code == int(code)


@then('A {code} http response code is received with the message {message}')
def response_code_is_with_message(context, code, message):
    log.info(pretty_response(context.response))
    assert context.response.status_code == int(code)
    assert json.loads(context.response.text)["error"]["message"] == message


@then('The artist information is retrieved')
def artist_information_is(context):
    data = context.response.json()
    for row in context.table:
        actual = ""
        if row["field"] == "spotify_url":
            actual = data["external_urls"]["spotify"]
        elif row["field"] == "followers":
            actual = data["followers"]["total"]
        else:
            actual = data[row["field"]]
        log.info(row["field"] + " field assert:\nExpected result:\n\t" +
                 str(row["value"]) + "\nExpected result:\n\t" + str(actual))
        assert str(actual) == str(row["value"])
