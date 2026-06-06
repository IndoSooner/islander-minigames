import unittest
from pathlib import Path

PREVIEW = Path(__file__).resolve().parents[1] / "animations" / "ending-effects-preview.html"


class AnimationPreviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = PREVIEW.read_text(encoding="utf-8")

    def test_preview_file_exists(self):
        self.assertTrue(PREVIEW.exists())

    def test_expected_controls_are_present(self):
        for text in [
            "Play Winner Fireworks",
            "Play Loser Explosion",
            "Play Tie Stalemate",
            "Side-by-side",
            "Replay",
        ]:
            self.assertIn(text, self.source)

    def test_animation_entry_points_are_present(self):
        for name in [
            "class WinnerFireworks",
            "class LoserNuclearExplosion",
            "class TieCosmicStalemate",
            "function play(newMode)",
            "requestAnimationFrame(animate)",
        ]:
            self.assertIn(name, self.source)

    def test_tie_animation_has_cosmic_stalemate_direction(self):
        for phrase in [
            "Cosmic Stalemate",
            "Perfectly matched",
            "glowing X and O",
            "balanced eclipse",
        ]:
            self.assertIn(phrase, self.source)

    def test_preview_is_standalone_vanilla_canvas(self):
        self.assertIn("<canvas id=\"effectsCanvas\"></canvas>", self.source)
        self.assertNotIn("<script src=", self.source)
        self.assertNotIn("import ", self.source)


if __name__ == "__main__":
    unittest.main()
