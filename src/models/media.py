class Media:
    def __init__(self, title, media_type, release_date, id):
        self.title = title
        self.media_type = media_type
        self.release_date = release_date
        self.id = id

    def __repr__(self):
        return f"<Media(title={self.title}, media_type={self.media_type}, release_date={self.release_date}, id={self.id})>"

class Movie(Media):
    def __init__(self, title, release_date, id):
        super().__init__(title, "movie", release_date, id)

class TVShow(Media):
    def __init__(self, title, release_date, id):
        super().__init__(title, "tv", release_date, id)

class Episode:
    def __init__(self, title, season_number, episode_number, release_date, id):
        self.title = title
        self.season_number = season_number
        self.episode_number = episode_number
        self.release_date = release_date
        self.id = id

    def __repr__(self):
        return f"<Episode(title={self.title}, season_number={self.season_number}, episode_number={self.episode_number}, release_date={self.release_date}, id={self.id})>"