import unittest
from pathlib import Path

APP_HTML = Path(__file__).resolve().parents[1] / "tic-tac-toe" / "index.html"


class GameEndEffectsAndRematchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = APP_HTML.read_text(encoding="utf-8")

    def test_game_has_canvas_overlay_for_endgame_effects(self):
        self.assertIn('<canvas id="ending-effects-canvas"', self.source)
        self.assertIn('class EndingEffectsController', self.source)
        self.assertIn('playEndingEffect(effect)', self.source)

    def test_winner_loser_and_tie_effect_entry_points_exist(self):
        for token in [
            'class WinnerFireworksEffect',
            'class LoserExplosionEffect',
            'class TieCosmicStalemateEffect',
            "playEndingEffect('winner')",
            "playEndingEffect('loser')",
            "playEndingEffect('tie')",
        ]:
            self.assertIn(token, self.source)

    def test_finished_game_triggers_effect_once_per_result(self):
        self.assertIn('lastEndingEffectKey', self.source)
        self.assertIn('maybePlayEndingEffect(data)', self.source)
        self.assertIn("const effect = data.winner === 'draw' ? 'tie'", self.source)
        self.assertIn("data.winner === mySymbol ? 'winner' : 'loser'", self.source)

    def test_rematch_requires_both_players_and_alternates_first_player(self):
        for token in [
            'rematchRequests',
            'nextFirstPlayer',
            'requestRematch',
            "[mySymbol]: true",
            'otherSymbol(mySymbol)',
            'currentTurn: nextFirstPlayer',
            'nextFirstPlayer: otherSymbol(nextFirstPlayer)',
        ]:
            self.assertIn(token, self.source)


if __name__ == "__main__":
    unittest.main()
