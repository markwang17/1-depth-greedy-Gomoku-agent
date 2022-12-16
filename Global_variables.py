import re

black = [[0 for _ in range(15)] for __ in range(15)]
white = [[0 for _ in range(15)] for __ in range(15)]
flag = [[0 for _ in range(15)] for __ in range(15)]

# tier 1
pattern_win = [re.compile(r'11111')]
# tier 2
pattern_tier2 = [re.compile(r'011110')]
# tier 3
# has 2 place to upgrade
pattern_premium_tier3 = [re.compile(r'0011100')]
# 1 place to upgrade
pattern_tier3 = [re.compile(r'010110'),re.compile(r'011010'),
                 re.compile(r'0011102'), re.compile(r'2011100'),
                 re.compile(r'11011'), re.compile(r'011112'),
                 re.compile(r'10111'), re.compile(r'11101'),
                 re.compile(r'211110')]
# tier 4
# 4 place to upgrade
pattern_tier4_rank1 = [re.compile(r'001100')]
# 3 place to upgrade
pattern_tier4_rank2 = [re.compile(r'0010100')]
# 2 place to upgrade
pattern_tier4_rank3 = [re.compile(r'201100'), re.compile(r'001102'),
                       re.compile(r'001112'), re.compile(r'010112'),
                       re.compile(r'011012'), re.compile(r'211100'),
                       re.compile(r'001112'), re.compile(r'211010'),
                       re.compile(r'210110'), re.compile(r'10011'),
                       re.compile(r'11001'), re.compile(r'10101'),
                       re.compile(r'2011102'), re.compile(r'00100100'),
                       re.compile(r'2010100'), re.compile(r'2010010'),
                       re.compile(r'0010102'), re.compile(r'0100102')]

all_patterns = [pattern_win, pattern_tier2, pattern_premium_tier3,
                pattern_tier3, pattern_tier4_rank1, pattern_tier4_rank2,
                pattern_tier4_rank3]

all_scores = [100000, 10000, 1500, 1000, 200, 150, 100]

board_scores = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
                [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
                [0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0],
                [0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 3, 2, 1, 0],
                [0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
                [0, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 0],
                [0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
                [0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
                [0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
                [0, 1, 2, 3, 4, 5, 6, 6, 6, 5, 4, 3, 2, 1, 0],
                [0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
