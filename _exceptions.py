"""
`discord.py` Tools
~~~~~~~~~~~~~~~~~~~

A set of wrappers and tools for `discord.py`.

DISCLAIMER: You are not permitted to use, modify,
or redistribute any portion of this code without 
the direct consent of the author.

:copyright: (c) 2022-present tanrbobanr

@author: C., Tanner; tanrbobanr; tannerbcorcoran@gmail.com
"""


__title__ = "Discord/Python Tools"
__author__ = "C., Tanner; tanrbobanr; tannerbcorcoran@gmail.com"
__copyright__ = "Copyright 2022-present tanrbobanr"
__version__ = "1.0.5"


from discord.ext import commands as __commands
from discord     import app_commands as __app_commands


class VariableEnforcementFailure(Exception):
    pass


class CheckFailure(__commands.CheckFailure, __app_commands.CheckFailure):
    pass


class HasRoleFailure(__commands.CheckFailure, __app_commands.CheckFailure):
    pass


class IsUserFailure(__commands.CheckFailure, __app_commands.CheckFailure):
    pass


class InChannelFailure(__commands.CheckFailure, __app_commands.CheckFailure):
    pass


class InGuildFailure(__commands.CheckFailure, __app_commands.CheckFailure):
    pass


class InDMFailure(__commands.CheckFailure, __app_commands.CheckFailure):
    pass


class InCategoryFailure(__commands.CheckFailure, __app_commands.CheckFailure):
    pass


class BotEnabledFailure(__commands.CheckFailure, __app_commands.CheckFailure):
    pass


class NotFound(Exception):
    pass


class Unmentionable(Exception):
    pass


class DiscordServerStatsHalted(Exception):
    pass


class Cancelled(Exception):
    pass


class TimedOut(Exception):
    pass


class Skipped(Exception):
    pass


class Ballchasing:
    class MissingAPIKey(Exception):
        pass


    class APIUnaccessible(Exception):
        pass


    class DuplicateReplay(Exception):
        pass


    class InvalidInput(Exception):
        pass


    class PendingReplay(Exception):
        pass


    class FailedReplay(Exception):
        pass


    class UnknownStatusCode(Exception):
        pass

    
    class RateLimitExceeded(Exception):
        pass


    class DuplicateName(Exception):
        pass
