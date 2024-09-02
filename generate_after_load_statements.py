#!/usr/bin/env python3

TEMPLATE = "$$ SELECT setval('{table}_{table}_id_seq', (SELECT GREATEST(MAX({table}_id), 1) FROM {table})); $$"


def generate(tables: list[str]):
    print(
        ",\n".join(
            TEMPLATE.format(table=table) for table in tables
        )
    )


# you can generate this from the output of psql's \dt with this regex:
# public \|\W*(\w+)\W*\| table \| .+
# "$1",
tables = [
    "admin",
    "admin_flag",
    "admin_log",
    "admin_log_player",
    "admin_messages",
    "admin_notes",
    "admin_rank",
    "admin_rank_flag",
    "admin_watchlists",
    "antag",
    "assigned_user_id",
    "ban_template",
    "connection_log",
    "job",
    "play_time",
    "player",
    "player_round",
    "preference",
    "profile",
    "profile_loadout",
    "profile_loadout_group",
    "profile_role_loadout",
    "role_whitelists",
    "round",
    "server",
    "server_ban",
    "server_ban_exemption",
    "server_ban_hit",
    "server_role_ban",
    "server_role_unban",
    "server_unban",
    "trait",
    "uploaded_resource_log",
    "whitelist",
]

if __name__ == "__main__":
    generate(tables=tables)
