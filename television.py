class Television:
    """
    Class for controlling the variables involved with a television
    """

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__(self) -> None:
        """
        Method to set default values of the tv
        """

        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL
    

    def power(self) -> None:
        """
        Method for turning tv power status on (True) and off (False)
        """

        if self.status:
            self.status = False
        else:
            self.status = True


    def mute(self) -> None:
        """
        Method for muting (True) and unmuting (False) the tv volume
        """

        if self.status:
            if self.muted:
                self.muted = False
            else:
                self.muted = True


    def channel_up(self) -> None:
        """
        Method for moving the channel value up one
        """
        if self.status:
            if self.channel == self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL
            else:
                self.channel += 1
    

    def channel_down(self) -> None:
        """
        Method for moving the channel value down one
        """
        if self.status:
            if self.channel == self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL
            else:
                self.channel -= 1
    

    def volume_up(self) -> None:
        """
        Method for moving the volume value up one
        """
        if self.status:
            self.muted = False
            if self.volume != self.MAX_VOLUME:
                self.volume += 1
    

    def volume_down(self) -> None:
        """
        Method for moving the volume value down one
        """
        if self.status:
            self.muted = False
            if self.volume != self.MIN_VOLUME:
                self.volume -= 1
    
    def __str__(self) -> str:
        """
        Method for building return string and getting values of tv
        return: Power, channel, and volume status as stirng
        """
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {0 if self.muted else self.volume}'