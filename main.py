"""Compress a pointless meeting into one sendable sentence.

The bounty asks for the sentence that could stand in for a whole
meeting, not a joke about meetings. A strong line therefore has to
do the meeting's work in a single breath: say what was decided, say
who is responsible, say when it lands, and then close the room, so
that sending the line instead of the calendar invite loses nothing.

The judge weighs replacement power first, then how familiar the
moment feels to anyone who has sat through an hour like this, then
the deadpan office tone. A line that only mocks the meeting fails
the first test, however funny it is, because it leaves the decision
unsaid and the meeting still needed.

Thirteen drafts were written by hand and graded out of fifty. The
table further down records each draft by a short nickname, its total
and a one-line note on why it fell short. The draft that won earned
forty-six: it opens with the answer, names the money, names the
owner, names the ship day, and finishes by declaring that the
sentence itself was the meeting. The closest rival earned
forty-five: it explains, very well, why nobody would simply email
the approval, but explaining the meeting is not the same as
replacing it, and replacement is what counts most.

An earlier version of the winner opened by announcing that an
answer was coming and closed by announcing that the meeting was
over. Both halves stated what the line should simply do. Cutting
the announcement from the front and letting the closing clause
perform the ending — the sentence claims to have been the whole
meeting — tightened it without changing any of its facts. That
tightened wording is the entry this program publishes.

The entry must land as UTF-8, on one line, between one and two
hundred characters long. The program writes it, reads the file
back, and compares the bytes on disk with the intended bytes
before it prints anything, so a corrupted write fails loudly
instead of shipping a wrong entry.
"""
from hashlib import sha256
from os import environ
from pathlib import Path


ENTRY = "Yes, the budget is approved, Priya owns it, and it ships Friday — that was the whole meeting."
MIN_CHARS = 1
MAX_CHARS = 200
DEFAULT_TARGET = "/output/entry.txt"
EXPECTED_TOP_SCORE = 46
EXPECTED_TOP_NICKNAME = "opening-yes-budget-owner-ship"


CONSIDERED = [
    ("opening-yes-budget-owner-ship", 46, "Decision, money, owner and ship day in one breath, then the line itself closes the meeting."),
    ("nobody-would-email-approved", 45, "Names the real problem, that nobody will put approval in writing, but explains the meeting rather than replacing it."),
    ("hour-deciding-what-this-decides", 44, "Clever about its own cleverness, and the first half is setup about the sentence instead of the decision."),
    ("needed-someone-to-say-yes-aloud", 44, "Very quotable and very tight, yet the payload is a bare yes with no owner and no date attached."),
    ("room-cannot-approve-or-disagree", 44, "Painfully familiar, but it carries no decision at all, so the meeting would still be needed."),
    ("meeting-was-just-this", 43, "Solid payload, weakened by a throat-clearing opener that spends words before the decision arrives."),
    ("asked-a-question-this-answers", 43, "Punchy and memorable, but a one-word answer replaces no real meeting and its content is too thin."),
    ("decision-made-before-invites", 42, "Relatable and funny, yet it is a comment on the meeting, not a sentence a manager could send instead of it."),
    ("one-hour-nine-people-zero-decisions", 42, "A familiar trope with a decent turn, but it still needs the meeting to exist so it can mock it."),
    ("recap-email-says-what-this-says", 42, "A neat loop between recap and sentence, but the meta framing about the sentence itself costs words."),
    ("whole-output-is-this-sentence", 40, "A tidy identity loop that reads like a riddle, not like a message anyone would actually send."),
    ("agreed-in-chat-read-aloud-slowly", 42, "Extremely familiar, and three slow beats where one would do, with no decision carried."),
    ("yes-approved-priya-friday-congratulations", 42, "A lively staccato opening, then it congratulates the reader instead of ending the meeting.")]
def _score_order(drafts):
    ordered = sorted(drafts, key=lambda item: (-item[1], item[0]))
    return ordered


def _check_text(text):
    if not text:
        raise ValueError("chosen entry is empty")
    if len(text) < MIN_CHARS or len(text) > MAX_CHARS:
        raise ValueError("chosen entry is outside the 1-200 character gate")
    if chr(10) in text or chr(13) in text:
        raise ValueError("chosen entry must stay on one line")
    if text != text.strip():
        raise ValueError("chosen entry has leading or trailing space")
    if text.count("  ") > 0:
        raise ValueError("chosen entry has a doubled space")
    if "—" not in text:
        raise ValueError("chosen entry lost its em-dash turn into the closing clause")
    if not text.endswith("."):
        raise ValueError("chosen entry must end with a full stop")
    if "Priya" not in text or "Friday" not in text:
        raise ValueError("chosen entry lost its owner or its ship day")
    return len(text)


def _target_path():
    override = environ.get("OUTPUT_PATH", "")
    if override:
        return Path(override)
    return Path(DEFAULT_TARGET)


def _publish():
    _check_text(ENTRY)
    ranked = _score_order(CONSIDERED)
    top = ranked[0]
    if top[1] != EXPECTED_TOP_SCORE:
        raise ValueError("top draft score moved; re-check the ranking before publishing")
    if top[0] != EXPECTED_TOP_NICKNAME:
        raise ValueError("top draft is not the expected winner; re-check the ranking before publishing")
    target = _target_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(ENTRY, encoding="utf-8")
    stored = target.read_bytes()
    digest = sha256(stored).hexdigest()
    wanted = sha256(ENTRY.encode("utf-8")).hexdigest()
    if digest != wanted:
        raise ValueError("stored bytes do not match the chosen entry")
    reread = stored.decode("utf-8")
    if reread != ENTRY:
        raise ValueError("stored text drifted from the chosen entry")
    _check_text(reread)
    print("wrote " + str(target) + ": " + reread + " [" + str(len(reread)) + " chars, sha256 " + digest[:12] + "]")
    return 0


raise SystemExit(_publish())
