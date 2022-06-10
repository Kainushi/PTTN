import pytest
from main import switch_game_status, Player, Enemy, spawner, enemy_garbage_collector

def test_switch_game_status():
    game_status = "MENU"
    with pytest.raises(ValueError):
        switch_game_status("MENU", game_status=game_status)
    with pytest.raises(ValueError):
        switch_game_status("menu", game_status=game_status)

def test_Player():
    player = Player()
    assert player.score == 0
    player.score = 1
    assert player.score == 1
    player.score = 10_000_000_000
    assert player.score == 999999

def test_Enemy_function():
    enemy = Enemy("Villager",(0,0))
    assert 3 <= enemy.hp <= 10
    assert .1 <= enemy.speed <= .5

def test_spawner_function():
    e=[]
    player = Player()
    spawn_timer = 0
    spawner(e, spawn_timer=spawn_timer, player=player)
    assert len(e) == 0
    spawn_timer = 5001
    spawner(e, spawn_timer=spawn_timer, player=player)
    assert len(e) == 1
    assert e[0].hp != 0

def test_enemy_garbage_collector_function():
    player = Player()
    enemy = Enemy()
    enemy._hp = 1
    e = [enemy]
    enemy_garbage_collector(e,player=player)
    assert len(e) == 1
    assert player.score == 0
    e[0]._hp = 0
    enemy_garbage_collector(e, player=player)
    assert len(e) == 0
    assert player.score == 1
