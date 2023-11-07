import pytest
from game_session import GameSession
from turfwar_game import TurfWarGame
from field_map import FieldMap

class Test:
    def testGameSession(self):
        gs = GameSession()

        addr_A = ("192.168.0.1", 5000)
        gs.register(addr_A)
        sess_id_A, player_num_A = gs.inquiry(addr_A)
        assert(sess_id_A == 0)
        assert(player_num_A == 0)

        addr_B = ("192.168.0.2", 5000)
        gs.register(addr_B)
        sess_id_B, player_num_B = gs.inquiry(addr_B)
        assert(sess_id_B == 0)
        assert(player_num_B == 1)

        re_sess_id_A, re_player_num_A = gs.inquiry(addr_A)
        assert(sess_id_A == re_sess_id_A)
        assert(player_num_A == re_player_num_A)

        addr_C = ("192.168.0.3", 5000)
        gs.register(addr_C)
        sess_id_C, player_num_C = gs.inquiry(addr_C)
        addr_D = ("192.168.0.4", 5000)
        gs.register(addr_D)
        sess_id_D, player_num_D = gs.inquiry(addr_D)
        assert(sess_id_C == 1)
        assert(player_num_C == 0)
        assert(sess_id_D == 1)
        assert(player_num_D == 1)

        gs.remove_from_id(sess_id_A)
        with pytest.raises(ValueError) as e:
            gs.inquiry(addr_A)
        assert(str(e.value) == f"This address({addr_A}) is not registerd")

        with pytest.raises(ValueError) as e:
            gs.inquiry(addr_B)
        assert(str(e.value) == f"This address({addr_B}) is not registerd")

        addr_E = ("192.168.0.5", 5000)
        gs.register(addr_E)
        sess_id_E, player_num_E = gs.inquiry(addr_E)
        assert(sess_id_E == 2)
        assert(player_num_E == 0)

    def testFieldMap(self):
        fm = FieldMap.create_flatmap()
        field_map_2d = fm.get_2d_map()
        field_map_flatten = fm.get_flatten_map()

        assert(field_map_2d.shape == (6, 6))
        assert(len(field_map_flatten) == 6 * 6)

        fm.paint_at(4, 4, "a")
        updated_map_2d = fm.get_2d_map()
        assert(updated_map_2d[4][4] == "a")

        with pytest.raises(ValueError) as e:
            fm.paint_at(0, 0, "a")
        assert(str(e.value) == "There is obstacle block at (0, 0).")

        with pytest.raises(ValueError) as e:
            fm.paint_at(6, 3, "a")
        assert(str(e.value) == "This point is unavailable.")

    def testTurfWarGame(self):
        game = TurfWarGame()
        field_map = game.get_map()
        assert(len(field_map) == 36)

        fm = FieldMap.create_flatmap()
        assert(all(field_map == fm.get_flatten_map()))

        p_id = 0
        p_behavior = ""
        game.step(p_id, p_behavior)
