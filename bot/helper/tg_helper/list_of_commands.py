from bot import CMD_INDEX

class _BotCommands:
    def __init__(self) -> None:
        self.StartCommand = f'start{CMD_INDEX}'
        self.MirrorCommand = f""
        self.UnzipMirrorCommand = f""
        self.ZipMirrorCommand = f""
        self.CancelMirror = f'cancel{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall{CMD_INDEX}'
        self.ListCommand = f'list{CMD_INDEX}'
        self.SearchCommand = f'search{CMD_INDEX}'
        self.StatusCommand = f'status{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo{CMD_INDEX}'
        self.PingCommand = f'ping{CMD_INDEX}'
        self.RestartCommand = f'restart{CMD_INDEX}'
        self.StatsCommand = f'stats{CMD_INDEX}'
        self.HelpCommand = f'help{CMD_INDEX}'
        self.LogCommand = f'log{CMD_INDEX}'
        self.CloneCommand = f'clone{CMD_INDEX}'
        self.CountCommand = f'count{CMD_INDEX}'
        self.WatchCommand = f'watch{CMD_INDEX}'
        self.ZipWatchCommand = f'{CMD_INDEX}'
        self.DeleteCommand = f'del{CMD_INDEX}'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp{CMD_INDEX}'
        self.LeechSetCommand = f""
        self.SetThumbCommand = f""
        self.LeechCommand = f""
        self.UnzipLeechCommand = f""
        self.ZipLeechCommand = f""
        self.LeechWatchCommand = f""
        self.LeechZipWatchCommand = f""
        
BotCommands = _BotCommands()
