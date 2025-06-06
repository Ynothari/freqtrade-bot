from copy import deepcopy

from freqtrade.constants import Config


def sanitize_config(config: Config, *, show_sensitive: bool = False) -> Config:
    """
    Remove sensitive information from the config.
    :param config: Configuration
    :param show_sensitive: Show sensitive information
    :return: Configuration
    """
    if show_sensitive:
        return config
    keys_to_remove = [
        "exchange.key",
        "exchange.api_key",
        "exchange.apiKey",
        "exchange.secret",
        "exchange.password",
        "exchange.uid",
        "exchange.account_id",
        "exchange.accountId",
        "exchange.wallet_address",
        "exchange.walletAddress",
        "exchange.private_key",
        "exchange.privateKey",
        "telegram.token",
        "telegram.chat_id",
        "discord.webhook_url",
        "api_server.password",
        "webhook.url",
    ]
    config = deepcopy(config)
    for key in keys_to_remove:
        if "." in key:
            nested_keys = key.split(".")
            nested_config = config
            for nested_key in nested_keys[:-1]:
                nested_config = nested_config.get(nested_key, {})
            if nested_keys[-1] in nested_config:
                nested_config[nested_keys[-1]] = "REDACTED"
        else:
            if key in config:
                config[key] = "REDACTED"

    return config
