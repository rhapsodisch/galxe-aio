import toml


cfg = toml.load(open('config.toml', 'r', encoding='utf-8'))


WAIT_BETWEEN_ACCOUNTS = cfg.get('WAIT_BETWEEN_ACCOUNTS')
MAX_TRIES = cfg.get('MAX_TRIES')
THREADS_NUM = cfg.get('THREADS_NUM')
DISABLE_SSL = cfg.get('DISABLE_SSL')
CHECKER_UPDATE_STORAGE = cfg.get('CHECKER_UPDATE_STORAGE')
UPDATE_STORAGE_ACCOUNT_INFO = cfg.get('UPDATE_STORAGE_ACCOUNT_INFO')
SKIP_FIRST_ACCOUNTS = cfg.get('SKIP_FIRST_ACCOUNTS')
RANDOM_ORDER = cfg.get('RANDOM_ORDER')
FAKE_TWITTER = cfg.get('FAKE_TWITTER')
FORCE_LINK_EMAIL = cfg.get('FORCE_LINK_EMAIL')
GALXE_CAMPAIGN_IDS = cfg.get('GALXE_CAMPAIGN_IDS')
HIDE_UNSUPPORTED = cfg.get('HIDE_UNSUPPORTED')
SPACES_STATS = cfg.get('SPACES_STATS')
RPCs = cfg.get('RPCs')
