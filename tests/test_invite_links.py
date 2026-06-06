import unittest
from pathlib import Path

APP_HTML = Path(__file__).resolve().parents[1] / "tic-tac-toe" / "index.html"


def app_source() -> str:
    return APP_HTML.read_text(encoding="utf-8")


class InviteLinkTests(unittest.TestCase):
    def test_page_reads_room_code_from_invite_url_on_load(self):
        src = app_source()

        self.assertIn("URLSearchParams", src)
        self.assertIn("window.location.search", src)
        self.assertIn("handleInviteLink", src)
        self.assertTrue("joinGame(inviteCode)" in src or "joinGame(codeFromUrl)" in src)

    def test_copy_button_copies_full_invite_url_not_just_room_code(self):
        src = app_source()

        self.assertIn("buildInviteUrl", src)
        self.assertIn("new URL(window.location.href)", src)
        self.assertTrue("searchParams.set('room', code)" in src or 'searchParams.set("room", code)' in src)
        self.assertIn("navigator.clipboard.writeText(buildInviteUrl(roomCode))", src)

    def test_join_input_accepts_invite_url_or_room_code(self):
        src = app_source()

        self.assertIn("extractRoomCode", src)
        self.assertIn("rawJoinValue", src)
        self.assertTrue("new URL(raw" in src or "new URL(value" in src)
        self.assertIn("joinGame(code)", src)


if __name__ == "__main__":
    unittest.main()
