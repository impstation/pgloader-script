#!/usr/bin/env python3

TEMPLATE = "$$ SELECT setval('{table}_{table}_id_seq', (SELECT GREATEST(MAX({table}_id), 1) FROM {table})); $$"


def generate(tables: list[str]):
    print(
        ",\n".join(
            TEMPLATE.format(table=table) for table in tables
        )
    )


# you can generate these like so:
# SELECT table_name FROM information_schema.columns WHERE column_name = table_name || '_id' ORDER BY table_name;
# then double check the output
tables = [
    "admin_flag",
    "admin_log",
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
    "preference",
    "profile",
    "profile_loadout",
    "profile_loadout_group",
    "profile_role_loadout",
    "round",
    "server",
    "server_ban",
    "server_ban_hit",
    "server_role_ban",
    "trait",
    "uploaded_resource_log",
]

if __name__ == "__main__":
    generate(tables=tables)
