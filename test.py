import pytest
from game_session import GameSession

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

        gs.remove(addr_A)
        with pytest.raises(ValueError) as e:
            gs.inquiry(addr_A)
        assert(str(e.value) == "This address is not registerd")

        gs.register(addr_A)
        sess_id_A, player_num_A = gs.inquiry(addr_A)
        assert(sess_id_A == 0)
        assert(player_num_A == 0)
