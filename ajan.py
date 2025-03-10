"""
TicTacToe Oyuncusu
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Oyun tahtasının başlangıç durumunu döndürür.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Tahtada bir sonraki sıraya sahip olan oyuncuyu döndürür.
    """
    raise NotImplementedError


def actions(board):
    """
    Tahtada mevcut olan tüm olası eylemlerin (i, j) kümesini döndürür.
    """
    raise NotImplementedError


def result(board, action):
    """
    Tahta üzerinde (i, j) hamlesini yaptıktan sonra ortaya çıkan tahtayı döndürür.
    """
    raise NotImplementedError


def winner(board):
    """
    Eğer varsa, oyunun galibini döndürür.
    """
    raise NotImplementedError


def terminal(board):
    """
    Oyun bittiyse True, bitmediyse False döndürür.
    """
    raise NotImplementedError


def utility(board):
    """
    X oyunu kazandıysa 1, O kazandıysa -1, aksi takdirde 0 döndürür.
    """
    raise NotImplementedError


def minimax(board):
    """
    Tahtadaki mevcut oyuncu için en uygun eylemi döndürür.
    """
    raise NotImplementedError
