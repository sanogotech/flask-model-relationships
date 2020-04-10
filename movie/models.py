from  . import db


actors = db.Table(
    "actors",
    db.Column("actor_id", db.Integer, db.ForeignKey("actor.id")),
    db.Column("movie_id", db.Integer, db.ForeignKey("movie.id")),
)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    release_date = db.Column(db.DateTime)
    actors = db.relationship("Actor", secondary=actors, backref="movies", lazy="select")

    def release_year(self):
        return self.release_date.strftime("%Y")

    def to_json(self):

        return {
            "id": self.id,
            "title": self.title,
            "director": self.director.last_name if self.director else None,
            "director_id": self.director.id if self.director else None,
            "release_date": self.release_date if self.release_date else None,
            "actors": [ {"id": a.id, "name": a.last_name} for a in self.actors] if self.actors else None
        }


class Director(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    movies = db.relationship(
        "Movie", backref=db.backref("director", lazy="joined"), lazy="select"
    )
    guild = db.relationship(
        "GuildMembership", backref="director", lazy="select", uselist=False
    )


# m = Movie(...)
# m.director.first_name


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    guild = db.relationship(
        "GuildMembership", backref="actor", lazy="select", uselist=False
    )


class GuildMembership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guild = db.Column(db.String(255))
    direcotr_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    actor_id = db.Column(db.Integer, db.ForeignKey("actor.id"))
