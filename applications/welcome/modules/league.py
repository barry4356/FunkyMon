import funkyLog
from gluon import current

db = current.db

logger = funkyLog.get_logger()
logger.error("THIS IS A TEST ERROR MESSAGE FROM league.py")

#TODO: These functions were AI generated and need to be reviewed and tested.

logger.error(db(db.auth_user).select(db.auth_user.ALL).as_list())

def get_leagues_for_user(user_id):
    logger.info(f"Fetching leagues for user_id: {user_id}")
    leagues = db(db.league_members.user_id == user_id).select(db.league.ALL, join=db.league.on(db.league.id == db.league_members.league_id))
    league_list = leagues.as_list()
    logger.info(f"Leagues found: {league_list}")
    return league_list

def get_all_leagues():
    logger.info("Fetching all leagues")
    leagues = db(db.league).select()
    league_list = leagues.as_list()
    logger.info(f"All leagues: {league_list}")
    return league_list

def create_league(name, commish_id):
    logger.info(f"Creating league with name: {name}, commish_id: {commish_id}")
    league_id = db.league.insert(name=name, commish_id=commish_id)
    logger.info(f"League created with id: {league_id}")
    return league_id

def add_user_to_league(league_id, user_id): 
    logger.info(f"Adding user_id: {user_id} to league_id: {league_id}")
    membership_id = db.league_members.insert(league_id=league_id, user_id=user_id)
    logger.info(f"User added to league with membership id: {membership_id}")
    return membership_id

def get_league_members(league_id):
    logger.info(f"Fetching members for league_id: {league_id}")
    members = db(db.league_members.league_id == league_id).select(db.auth_user.ALL, join=db.auth_user.on(db.auth_user.id == db.league_members.user_id))
    member_list = members.as_list()
    logger.info(f"Members found: {member_list}")
    return member_list

def draft_player(league_id, player_id, user_id):
    logger.info(f"Drafting player_id: {player_id} for user_id: {user_id} in league_id: {league_id}")
    draft_id = db.draft.insert(league_id=league_id, player_id=player_id, user_id=user_id)
    logger.info(f"Player drafted with draft id: {draft_id}")
    return draft_id
