from log import get_custom_logger

log = get_custom_logger()


def before_all(context):
    context.url = "https://api.spotify.com/v1/artists/"
    context.token = "Bearer BQC25JXxyTjjsx8ZHtcX4v0pXzqYOifElXwOCnhjj4C5MFLRvwdlC339EDBqNl3z_NmmP9VYbXBPkB5CWA9KdnDEZc8zEJgBOMVf7zf9F4vqWHcC4ZBIUCHz7khpNCayug0alpe1YW90HRf2_2w"
    log.info("Spotify OAuth token set to: " + context.token)


def before_scenario(context, scenario):
    log.info("***************** SCENARIO STARTS: " + scenario.name + " *****************")


def after_scenario(context, scenario):
    log.info("****************** SCENARIO ENDS: " + scenario.name + " ******************")
