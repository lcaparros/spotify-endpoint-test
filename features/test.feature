Feature: Spotify Artists endpoint tests
  Test suite for https://api.spotify.com/v1/artists endpoint

  # Note: As automatizing the provision of a valid OAuth token is not under the scope of this test, please
  # remember that before run those tests you must include a valid OAuth token in environment.py file.
  #
  # Disclaimer: Data associated to this test suite changes usually as it is relative to real Spotify production
  #             data. So please take into account this test case could fail for this reason.

  Scenario: Get artist information
    Given An artist ID such as 6BH2lormtpjy3X9DyrGHVj
    When The artist information is requested
    Then A 200 http response code is received
    And The artist information is retrieved
      | field       | value                                                     |
      | spotify_url | https://open.spotify.com/artist/6BH2lormtpjy3X9DyrGHVj    |
      | followers   | 62355                                                     |
      | href        | https://api.spotify.com/v1/artists/6BH2lormtpjy3X9DyrGHVj |
      | id          | 6BH2lormtpjy3X9DyrGHVj                                    |
      | name        | Bob Marley                                                |
      | popularity  | 45                                                        |

  Scenario Outline: Invalid IDs
    Given An artist ID such as <artistId>
    When The artist information is requested
    Then A <httpCode> http response code is received with the message <message>

    Examples: Invalid ID with the correct lenght
      | artistId               | httpCode | message         |
      | testtesttest0123456789 | 404      | non existing id |
      | testtestte&t0123456789 | 400      | invalid id      |
      | testtestte+t0123456789 | 400      | invalid id      |
      | testtestte,t0123456789 | 400      | invalid id      |
      | testtestte:t0123456789 | 400      | invalid id      |
      | testtestte;t0123456789 | 400      | invalid id      |
      | testtestte=t0123456789 | 400      | invalid id      |
      | testtestte?t0123456789 | 400      | invalid id      |
      | testtestte@t0123456789 | 400      | invalid id      |

    Examples: Not allowed characters
      | artistId | httpCode | message    |
      | &        | 400      | invalid id |
      | +        | 400      | invalid id |
      | ,        | 400      | invalid id |
      | /        | 400      | invalid id |
      | :        | 400      | invalid id |
      | ;        | 400      | invalid id |
      | =        | 400      | invalid id |
      | ?        | 400      | invalid id |
      | @        | 400      | invalid id |

  Scenario: No parameter provided
    When The artist information is requested with no ID
    Then A 400 http response code is received with the message invalid id

  Scenario: Security error
    When The artist information is requested with a non valid OAuth security token
    Then A 401 http response code is received with the message Invalid access token