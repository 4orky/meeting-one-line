#!/usr/bin/env python3
# The Meeting That Should Have Been One Line — make.fun bounty
# u-boothlord-the-meeting-that-should-have-been-one-line-a4af6d1c
#
# Brief, read closely: write the single sentence that could have replaced an
# entire pointless meeting. No context, no explanation, no setup. The judge
# compares entries two at a time and weighs, most important first:
#   1. how completely the line kills the meeting (it must BE the replacement,
#      not a comment about meetings in general)
#   2. how relatable it feels to anyone who has sat through a useless one
#   3. office humor as the register — deadpan, recognizable, quotable
# Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, one line.
#
# A good entry therefore does two jobs at once: it carries the meeting's whole
# content (decision, owner, deadline) AND it declares the meeting over, so
# that sending this sentence instead of the invite would lose nothing.
# Lines that only mock meetings ("what a waste of time") fail job 1: they
# describe the meeting instead of replacing it.
#
# 13 original candidates, hand-scored per criterion (0-10):
#   (kills-meeting, relatability, office-humor, single-sentence, economy)
#
#  1. "The answer is yes, the budget is approved, Priya owns it, and the
#     deadline is Friday — this meeting is now over."
#     (10, 9, 8, 10, 9) = 46. The only candidate that does both jobs: it
#     carries the meeting's whole content (decision, budget, owner,
#     deadline) AND ends the meeting. Its weakness is stylistic, not
#     structural — "this meeting is now over" states the kill instead of
#     performing it, and "now" is dead weight. Fixed in the revision below.
#     Economy 9, not 10: "The answer is" is throat-clearing.
#  2. "We spent an hour deciding what this sentence just decided: yes, launch
#     Tuesday, Sarah owns it, budget approved."
#     (9, 9, 9, 9, 8) = 44. Self-referential and clever, but the first clause
#     is setup about the sentence itself — the line comments on itself
#     instead of simply being the replacement.
#  3. "Nobody in this room can approve it, nobody disagrees with it, and
#     nobody will remember it by lunch, so we're done."
#     (8, 10, 9, 9, 8) = 44. Painfully relatable, but it carries no decision:
#     it mocks the room without replacing the meeting's content.
#  4. "The whole meeting was just this: we're doing it, it ships Tuesday, and
#     the only action item is everyone going back to work."
#     (9, 9, 8, 9, 8) = 43. Solid, but "the whole meeting was just this" is
#     throat-clearing before the payload.
#  5. "Yes, approved, Priya owns it, Friday — congratulations, you just
#     attended a meeting that was one sentence long."
#     (8, 9, 8, 9, 8) = 42. The staccato opening is fun, but the second half
#     congratulates the reader instead of killing the meeting.
#  6. "We called a meeting to ask a question this sentence answers: yes."
#     (7, 9, 9, 9, 9) = 43. Punchy and quotable, but too thin: a one-word
#     answer replaces no real meeting's content.
#  7. "The decision was made before the invites went out; this meeting was
#     just thirty people watching it get announced slowly."
#     (8, 10, 8, 9, 7) = 42. Relatable and funny, but again a comment about
#     the meeting, not the replacement sentence itself.
#  8. "One hour, nine people, zero decisions — because the decision was yes,
#     and yes fits in a sentence."
#     (8, 9, 8, 9, 8) = 42. The "zero decisions" opener is a familiar trope;
#     the turn lands but the line still needs the meeting to exist to mock.
#  9. "This meeting exists because nobody wanted to be the person who just
#     emailed: approved, go ahead."
#     (9, 10, 9, 9, 8) = 45. Strongest runner-up: names the real disease
#     (nobody will put "approved" in writing) and delivers the email in
#     the same breath. Loses to the winner only because it explains WHY
#     the meeting happened instead of simply being the sentence that
#     replaces it.
# 10. "The recap email will say what this sentence already says: approved,
#     Tuesday, Priya — now go do it."
#     (8, 9, 8, 9, 8) = 42. Good loop (recap = sentence), but "will say what
#     this sentence already says" is meta-setup that costs words.
# 11. "We didn't need a meeting, we needed someone to say yes out loud, so:
#     yes."
#     (8, 9, 9, 9, 9) = 44. Very quotable, very tight — but like candidate 6,
#     the payload is a bare "yes" with no owner, no date, no content.
# 12. "The meeting's entire output is this sentence, and this sentence was
#     the agenda."
#     (7, 8, 8, 9, 8) = 40. A neat identity loop, but it is a riddle about
#     the meeting rather than a sentence a manager could actually send
#     instead of it.
# 13. "Everyone already agreed in the chat; this meeting is just the
#     agreement, read aloud, slowly, for an hour."
#     (8, 10, 8, 9, 7) = 42. Extremely relatable, but "read aloud, slowly,
#     for an hour" is three beats where one would do, and it carries no
#     decision.
#
# Winner: candidate 1 (46). Runner-up: candidate 9 (45) — it names the real
# disease (nobody will put "approved" in writing) and delivers the email in
# the same breath, but it explains WHY the meeting happened instead of simply
# being the sentence that replaces it. On the judge's first weight — how
# completely the line kills the meeting — the line that can be sent instead
# of the invite beats the line that diagnoses the invite. The revision below
# tightens the winner's delivery without changing its content.

CANDIDATES = [
    # (kills-meeting, relatability, office-humor, single-sentence, economy)
    ("The answer is yes, the budget is approved, Priya owns it, and the "
     "deadline is Friday — this meeting is now over.",
     (10, 9, 8, 10, 9)),
    ("We spent an hour deciding what this sentence just decided: yes, launch "
     "Tuesday, Sarah owns it, budget approved.",
     (9, 9, 9, 9, 8)),
    ("Nobody in this room can approve it, nobody disagrees with it, and "
     "nobody will remember it by lunch, so we're done.",
     (8, 10, 9, 9, 8)),
    ("The whole meeting was just this: we're doing it, it ships Tuesday, and "
     "the only action item is everyone going back to work.",
     (9, 9, 8, 9, 8)),
    ("Yes, approved, Priya owns it, Friday — congratulations, you just "
     "attended a meeting that was one sentence long.",
     (8, 9, 8, 9, 8)),
    ("We called a meeting to ask a question this sentence answers: yes.",
     (7, 9, 9, 9, 9)),
    ("The decision was made before the invites went out; this meeting was "
     "just thirty people watching it get announced slowly.",
     (8, 10, 8, 9, 7)),
    ("One hour, nine people, zero decisions — because the decision was yes, "
     "and yes fits in a sentence.",
     (8, 9, 8, 9, 8)),
    ("This meeting exists because nobody wanted to be the person who just "
     "emailed: approved, go ahead.",
     (9, 10, 9, 9, 8)),
    ("The recap email will say what this sentence already says: approved, "
     "Tuesday, Priya — now go do it.",
     (8, 9, 8, 9, 8)),
    ("We didn't need a meeting, we needed someone to say yes out loud, so: "
     "yes.",
     (8, 9, 9, 9, 9)),
    ("The meeting's entire output is this sentence, and this sentence was "
     "the agenda.",
     (7, 8, 8, 9, 8)),
    ("Everyone already agreed in the chat; this meeting is just the "
     "agreement, read aloud, slowly, for an hour.",
     (8, 10, 8, 9, 7)),
]

# REVISION (second pass, real changes — not a walk-through):
# The winning first draft stated the kill ("this meeting is now over") instead
# of performing it, and "now" added nothing. Three edits:
# - "The answer is yes" -> "Yes": the answer IS the opening word; the
#   throat-clearing "The answer is" is gone.
# - "the deadline is Friday" -> "it ships Friday": one verb ("ships") does
#   the work of a copula plus a noun, and it names the outcome, not the date.
# - "this meeting is now over" -> "that was the whole meeting": the kicker
#   now performs the kill — the sentence declares itself to BE the meeting,
#   so there is nothing left to meet about. "That was" also lands as a
#   shrug, which is the office-humor register the brief wants.
# Revised winner (93 characters):
# "Yes, the budget is approved, Priya owns it, and it ships Friday — that
#  was the whole meeting."

WINNER = (
    "Yes, the budget is approved, Priya owns it, and it ships Friday — "
    "that was the whole meeting."
)


def pick(candidates):
    best = None
    for text, scores in candidates:
        assert len(scores) == 5, f"candidate needs 5 criterion scores: {text!r}"
        assert all(0 <= s <= 10 for s in scores), f"score out of range: {text!r}"
        total = sum(scores)
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be a single line"
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        key = (total, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = WINNER
    import hashlib
    import os
    expected_sha256 = hashlib.sha256(line.encode("utf-8")).hexdigest()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what landed on disk: byte-identical to the chosen line (SHA-256),
    # one line only, inside the 1-200 character gate. A mismatch here means
    # the program failed loudly instead of submitting a wrong entry.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    assert hashlib.sha256(raw).hexdigest() == expected_sha256, \
        "entry.txt SHA-256 mismatch — write was corrupted"
    written = raw.decode("utf-8")
    assert written == line, "entry.txt differs from the chosen line"
    assert "\n" not in written, "entry must be a single line"
    assert 1 <= len(written) <= 200, f"entry over gate: {len(written)} chars"
    print(f"{line} ({len(written)} chars, sha256 {expected_sha256[:16]}…)")


if __name__ == "__main__":
    main()
