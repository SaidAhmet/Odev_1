# """
# TicTacToe Oyuncusu
# """

# import math

# X = "X"
# O = "O"
# EMPTY = None


# def initial_state():
#     """
#     Oyun tahtasının başlangıç durumunu döndürür.
#     """
#     return [[EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY]]


# def player(board):
#     """
#     Tahtada bir sonraki sıraya sahip olan oyuncuyu döndürür.
#     """
#     raise NotImplementedError


# def actions(board):
#     """
#     Tahtada mevcut olan tüm olası eylemlerin (i, j) kümesini döndürür.
#     """
#     raise NotImplementedError


# def result(board, action):
#     """
#     Tahta üzerinde (i, j) hamlesini yaptıktan sonra ortaya çıkan tahtayı döndürür.
#     """
#     raise NotImplementedError


# def winner(board):
#     """
#     Eğer varsa, oyunun galibini döndürür.
#     """
#     raise NotImplementedError


# def terminal(board):
#     """
#     Oyun bittiyse True, bitmediyse False döndürür.
#     """
#     raise NotImplementedError


# def utility(board):
#     """
#     X oyunu kazandıysa 1, O kazandıysa -1, aksi takdirde 0 döndürür.
#     """
#     raise NotImplementedError


# def minimax(board):
#     """
#     Tahtadaki mevcut oyuncu için en uygun eylemi döndürür.
#     """
#     raise NotImplementedError

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
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O

def actions(board):
    """
    Tahtada mevcut olan tüm olası eylemlerin (i, j) kümesini döndürür.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions

def result(board, action):
    """
    Tahta üzerinde (i, j) hamlesini yaptıktan sonra ortaya çıkan tahtayı döndürür.
    """
    i, j = action
    if board[i][j] != EMPTY:
        raise ValueError("Geçersiz hamle")
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Eğer varsa, oyunun galibini döndürür.
    """
    # Satırları kontrol et
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
    # Sütunları kontrol et
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]
    # Çaprazları kontrol et
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None

def terminal(board):
    """
    Oyun bittiyse True, bitmediyse False döndürür.
    """
    if winner(board) is not None:
        return True
    if all(board[i][j] != EMPTY for i in range(3) for j in range(3)):
        return True
    return False

def utility(board):
    """
    X oyunu kazandıysa 1, O kazandıysa -1, aksi takdirde 0 döndürür.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Tahtadaki mevcut oyuncu için en uygun eylemi döndürür.
    """
    if terminal(board):
        return None

    current_player = player(board)
    if current_player == X:
        value = -math.inf
        best_action = None
        for action in actions(board):
            new_value = min_value(result(board, action))
            if new_value > value:
                value = new_value
                best_action = action
        return best_action
    else:
        value = math.inf
        best_action = None
        for action in actions(board):
            new_value = max_value(result(board, action))
            if new_value < value:
                value = new_value
                best_action = action
        return best_action

def max_value(board):
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value

def min_value(board):
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value