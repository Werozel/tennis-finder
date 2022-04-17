from dataclasses import dataclass

from flask_babel import gettext


@dataclass
class Skill:
    title: str
    description: str
    value: float


valid_skills = [
    Skill(
        value=2.0,
        title=gettext("NTRP 2.0 - New player"),
        description=gettext("Has no or limited tennis experience and is still working primarily on getting the ball into play.")
    ),
    Skill(
        value=2.5,
        title=gettext("NTRP 2.5 - Beginner"),
        description=gettext("Learning to judge where the ball is going. Can sustain a short rally of slow pace with other players of the same ability.")
    ),
    Skill(
        value=3.0,
        title=gettext("NTRP 3.0 - Beginner to intermediate"),
        description=gettext("Fairly consistent when hitting medium-paced shots, but is not comfortable with all strokes and lacks execution when trying for directional control, depth or power.")
    ),
    Skill(
        value=3.5,
        title=gettext("NTRP 3.5 - Intermediate player"),
        description=gettext("Has good stroke dependability with directional control on shots, but still lacks depth and variety. Starting to exhibit more aggressive net play and has improved court coverage.")
    ),
    Skill(
        value=4.0,
        title=gettext("NTRP 4.0 - Intermediate to advanced player"),
        description=gettext("Dependable strokes, including directional intent, on both forehand and backhand sides on moderate shots, plus the ability to use lobs, overheads, approach shots and volleys with some success.")
    ),
    Skill(
        value=4.5,
        title=gettext("NTRP 4.5 - Advanced player"),
        description=gettext("This player has begun to master the use of power and spins and is beginning to handle pace, has sound footwork, can control depth of shots, and is beginning to vary tactics according to opponents. This player can hit first serves with power and accuracy and place the second serve and is able to rush the net successfully.")
    ),
    Skill(
        value=5.0,
        title=gettext("NTRP 5.0 - Elite player"),
        description=gettext("This player has good shot anticipation and frequently has an outstanding shot or attribute around which a game may be structured. This player can regularly hit winners or force errors off of short balls, can put away volleys, can successfully execute lobs, drop shots, half volleys and overhead smashes, and has good depth and spin on most second serves.")
    )
]
