import common

class Tests(common.Test):
    inputs = [
        '\n',
        'a\n',
        'ab\n',
        'abc\n',
        'abcd\n',
        'abcdefghi\n',
        'abcdefghijklmnopqrs\n',
        'abcdefghijklmnopqrstuvwzyzABC\n',
        'abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLM\n',
        'abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVW\n',
        'abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456\n',
        ]

    def test_d1_1(self):
        # Single lines to Decimal-1.
        self.request('../d1')
        outputs = ['''\
 10
''', '''\
 97,  10
''', '''\
 97,  98,  10
''', '''\
 97,  98,  99,  10
''', '''\
 97,  98,  99, 100,  10
''', '''\
 97,  98,  99, 100, 101, 102, 103, 104, 105,  10
''', '''\
 97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
112, 113, 114, 115,  10
''', '''\
 97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
112, 113, 114, 115, 116, 117, 118, 119, 122, 121, 122,  65,  66,  67,  10
''', '''\
 97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
112, 113, 114, 115, 116, 117, 118, 119, 122, 121, 122,  65,  66,  67,  68,
 69,  70,  71,  72,  73,  74,  75,  76,  77,  10
''', '''\
 97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
112, 113, 114, 115, 116, 117, 118, 119, 122, 121, 122,  65,  66,  67,  68,
 69,  70,  71,  72,  73,  74,  75,  76,  77,  78,  79,  80,  81,  82,  83,
 84,  85,  86,  87,  10
''', '''\
 97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
112, 113, 114, 115, 116, 117, 118, 119, 122, 121, 122,  65,  66,  67,  68,
 69,  70,  71,  72,  73,  74,  75,  76,  77,  78,  79,  80,  81,  82,  83,
 84,  85,  86,  87,  88,  89,  90,  48,  49,  50,  51,  52,  53,  54,  10
''']
        for input, output in zip(self.inputs, outputs):
            self.assertEqual(self.encode(input), output)

    def test_d1_2(self):
        # Block of lines to Decimal-1.
        self.request('../d1')
        input = ''.join(self.inputs)
        output = '''\
 10,  97,  10,  97,  98,  10,  97,  98,  99,  10,  97,  98,  99, 100,  10,
 97,  98,  99, 100, 101, 102, 103, 104, 105,  10,  97,  98,  99, 100, 101,
102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115,  10,
 97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
112, 113, 114, 115, 116, 117, 118, 119, 122, 121, 122,  65,  66,  67,  10,
 97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
112, 113, 114, 115, 116, 117, 118, 119, 122, 121, 122,  65,  66,  67,  68,
 69,  70,  71,  72,  73,  74,  75,  76,  77,  10,  97,  98,  99, 100, 101,
102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
117, 118, 119, 122, 121, 122,  65,  66,  67,  68,  69,  70,  71,  72,  73,
 74,  75,  76,  77,  78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  10,
 97,  98,  99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111,
112, 113, 114, 115, 116, 117, 118, 119, 122, 121, 122,  65,  66,  67,  68,
 69,  70,  71,  72,  73,  74,  75,  76,  77,  78,  79,  80,  81,  82,  83,
 84,  85,  86,  87,  88,  89,  90,  48,  49,  50,  51,  52,  53,  54,  10
'''
        self.assertEqual(self.encode(input), output)

    def test_d1_3(self):
        # Single lines to Decimal-1 and back.
        self.request('../d1')
        for input in self.inputs:
            self.assertEqual(self.decode(self.encode(input)), input)

    def test_d1_4(self):
        # Block of lines to Decimal-1 and back.
        self.request('../d1')
        input = ''.join(self.inputs)
        self.assertEqual(self.decode(self.encode(input)), input)

    def test_d2_1(self):
        # Single lines to Decimal-2.
        self.request('../d2')
        outputs = ['''\
 10
''', '''\
24842
''', '''\
24930,  10
''', '''\
24930, 25354
''', '''\
24930, 25444,  10
''', '''\
24930, 25444, 25958, 26472, 26890
''', '''\
24930, 25444, 25958, 26472, 26986, 27500, 28014, 28528, 29042, 29450
''', '''\
24930, 25444, 25958, 26472, 26986, 27500, 28014, 28528, 29042, 29556,
30070, 30586, 31098, 16706, 17162
''', '''\
24930, 25444, 25958, 26472, 26986, 27500, 28014, 28528, 29042, 29556,
30070, 30586, 31098, 16706, 17220, 17734, 18248, 18762, 19276, 19722
''', '''\
24930, 25444, 25958, 26472, 26986, 27500, 28014, 28528, 29042, 29556,
30070, 30586, 31098, 16706, 17220, 17734, 18248, 18762, 19276, 19790,
20304, 20818, 21332, 21846, 22282
''', '''\
24930, 25444, 25958, 26472, 26986, 27500, 28014, 28528, 29042, 29556,
30070, 30586, 31098, 16706, 17220, 17734, 18248, 18762, 19276, 19790,
20304, 20818, 21332, 21846, 22360, 22874, 12337, 12851, 13365, 13834
''']
        for input, output in zip(self.inputs, outputs):
            self.assertEqual(self.encode(input), output)

    def test_d2_2(self):
        # Block of lines to Decimal-2.
        self.request('../d2')
        input = ''.join(self.inputs)
        output = '''\
 2657,  2657, 25098, 24930, 25354, 24930, 25444,  2657, 25187, 25701,
26215, 26729,  2657, 25187, 25701, 26215, 26729, 27243, 27757, 28271,
28785, 29299,  2657, 25187, 25701, 26215, 26729, 27243, 27757, 28271,
28785, 29299, 29813, 30327, 31353, 31297, 16963,  2657, 25187, 25701,
26215, 26729, 27243, 27757, 28271, 28785, 29299, 29813, 30327, 31353,
31297, 16963, 17477, 17991, 18505, 19019, 19533,  2657, 25187, 25701,
26215, 26729, 27243, 27757, 28271, 28785, 29299, 29813, 30327, 31353,
31297, 16963, 17477, 17991, 18505, 19019, 19533, 20047, 20561, 21075,
21589, 22103,  2657, 25187, 25701, 26215, 26729, 27243, 27757, 28271,
28785, 29299, 29813, 30327, 31353, 31297, 16963, 17477, 17991, 18505,
19019, 19533, 20047, 20561, 21075, 21589, 22103, 22617, 23088, 12594,
13108, 13622,  10
'''
        self.assertEqual(self.encode(input), output)

    def test_d2_3(self):
        # Single lines to Decimal-2 and back.
        self.request('../d2')
        for input in self.inputs:
            self.assertEqual(self.decode(self.encode(input)), input)

    def test_d2_4(self):
        # Block of lines to Decimal-2 and back.
        self.request('../d2')
        input = ''.join(self.inputs)
        self.assertEqual(self.decode(self.encode(input)), input)

    def test_d4_1(self):
        # Single lines to Decimal-4.
        self.request('../d4')
        outputs = ['''\
 10
''', '''\
24842
''', '''\
 6382090
''', '''\
1633837834
''', '''\
1633837924,  10
''', '''\
1633837924, 1701209960, 26890
''', '''\
1633837924, 1701209960, 1768581996, 1835954032, 1903325962
''', '''\
1633837924, 1701209960, 1768581996, 1835954032, 1903326068,
1970698106, 2038055234, 17162
''', '''\
1633837924, 1701209960, 1768581996, 1835954032, 1903326068,
1970698106, 2038055234, 1128547654, 1195919690, 1263291658
''', '''\
1633837924, 1701209960, 1768581996, 1835954032, 1903326068,
1970698106, 2038055234, 1128547654, 1195919690, 1263291726,
1330663762, 1398035798, 22282
''', '''\
1633837924, 1701209960, 1768581996, 1835954032, 1903326068,
1970698106, 2038055234, 1128547654, 1195919690, 1263291726,
1330663762, 1398035798, 1465407834,  808530483,  875902474
''']
        for input, output in zip(self.inputs, outputs):
            self.assertEqual(self.encode(input), output)

    def test_d4_2(self):
        # Block of lines to Decimal-4.
        self.request('../d4')
        input = ''.join(self.inputs)
        output = '''\
 174131809, 1644847458, 1661624674, 1667500641, 1650680933,
1718052969,  174154339, 1684366951, 1751738987, 1819111023,
1886483059,  174154339, 1684366951, 1751738987, 1819111023,
1886483059, 1953855095, 2054781505, 1111689825, 1650680933,
1718052969, 1785425005, 1852797041, 1920169077, 1987541625,
2051097155, 1145390663, 1212762699, 1280117345, 1650680933,
1718052969, 1785425005, 1852797041, 1920169077, 1987541625,
2051097155, 1145390663, 1212762699, 1280134735, 1347506771,
1414878807,  174154339, 1684366951, 1751738987, 1819111023,
1886483059, 1953855095, 2054781505, 1111704645, 1179076681,
1246448717, 1313820753, 1381192789, 1448564825, 1513107762,
 859059510,  10
'''
        self.assertEqual(self.encode(input), output)

    def test_d4_3(self):
        # Single lines to Decimal-4 and back.
        self.request('../d4')
        for input in self.inputs:
            self.assertEqual(self.decode(self.encode(input)), input)

    def test_d4_4(self):
        # Block of lines to Decimal-4 and back.
        self.request('../d4')
        input = ''.join(self.inputs)
        self.assertEqual(self.decode(self.encode(input)), input)

    def test_x1_1(self):
        # Single lines to Hexadecimal-1.
        self.request('../x1')
        outputs = ['''\
0x0A
''', '''\
0x61, 0x0A
''', '''\
0x61, 0x62, 0x0A
''', '''\
0x61, 0x62, 0x63, 0x0A
''', '''\
0x61, 0x62, 0x63, 0x64, 0x0A
''', '''\
0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x0A
''', '''\
0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C,
0x6D, 0x6E, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x0A
''', '''\
0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C,
0x6D, 0x6E, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x7A,
0x79, 0x7A, 0x41, 0x42, 0x43, 0x0A
''', '''\
0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C,
0x6D, 0x6E, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x7A,
0x79, 0x7A, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A,
0x4B, 0x4C, 0x4D, 0x0A
''', '''\
0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C,
0x6D, 0x6E, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x7A,
0x79, 0x7A, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A,
0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56,
0x57, 0x0A
''', '''\
0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C,
0x6D, 0x6E, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x7A,
0x79, 0x7A, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A,
0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56,
0x57, 0x58, 0x59, 0x5A, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x0A
''']
        for input, output in zip(self.inputs, outputs):
            self.assertEqual(self.encode(input), output)

    def test_x1_2(self):
        # Block of lines to Hexadecimal-1.
        self.request('../x1')
        input = ''.join(self.inputs)
        output = '''\
0x0A, 0x61, 0x0A, 0x61, 0x62, 0x0A, 0x61, 0x62, 0x63, 0x0A, 0x61, 0x62,
0x63, 0x64, 0x0A, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69,
0x0A, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B,
0x6C, 0x6D, 0x6E, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x0A, 0x61, 0x62, 0x63,
0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F,
0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x7A, 0x79, 0x7A, 0x41,
0x42, 0x43, 0x0A, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69,
0x6A, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F, 0x70, 0x71, 0x72, 0x73, 0x74, 0x75,
0x76, 0x77, 0x7A, 0x79, 0x7A, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47,
0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x0A, 0x61, 0x62, 0x63, 0x64, 0x65,
0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F, 0x70, 0x71,
0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x7A, 0x79, 0x7A, 0x41, 0x42, 0x43,
0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F,
0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x0A, 0x61, 0x62, 0x63,
0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F,
0x70, 0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x7A, 0x79, 0x7A, 0x41,
0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D,
0x4E, 0x4F, 0x50, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59,
0x5A, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x0A
'''
        self.assertEqual(self.encode(input), output)

    def test_x1_3(self):
        # Single lines to Hexadecimal-1 and back.
        self.request('../x1')
        for input in self.inputs:
            self.assertEqual(self.decode(self.encode(input)), input)

    def test_x1_4(self):
        # Block of lines to Hexadecimal-1 and back.
        self.request('../x1')
        input = ''.join(self.inputs)
        self.assertEqual(self.decode(self.encode(input)), input)

    def test_x2_1(self):
        # Single lines to Hexadecimal-2.
        self.request('../x2')
        outputs = ['''\
0x0A
''', '''\
0x610A
''', '''\
0x6162, 0x0A
''', '''\
0x6162, 0x630A
''', '''\
0x6162, 0x6364, 0x0A
''', '''\
0x6162, 0x6364, 0x6566, 0x6768, 0x690A
''', '''\
0x6162, 0x6364, 0x6566, 0x6768, 0x696A, 0x6B6C, 0x6D6E, 0x6F70,
0x7172, 0x730A
''', '''\
0x6162, 0x6364, 0x6566, 0x6768, 0x696A, 0x6B6C, 0x6D6E, 0x6F70,
0x7172, 0x7374, 0x7576, 0x777A, 0x797A, 0x4142, 0x430A
''', '''\
0x6162, 0x6364, 0x6566, 0x6768, 0x696A, 0x6B6C, 0x6D6E, 0x6F70,
0x7172, 0x7374, 0x7576, 0x777A, 0x797A, 0x4142, 0x4344, 0x4546,
0x4748, 0x494A, 0x4B4C, 0x4D0A
''', '''\
0x6162, 0x6364, 0x6566, 0x6768, 0x696A, 0x6B6C, 0x6D6E, 0x6F70,
0x7172, 0x7374, 0x7576, 0x777A, 0x797A, 0x4142, 0x4344, 0x4546,
0x4748, 0x494A, 0x4B4C, 0x4D4E, 0x4F50, 0x5152, 0x5354, 0x5556,
0x570A
''', '''\
0x6162, 0x6364, 0x6566, 0x6768, 0x696A, 0x6B6C, 0x6D6E, 0x6F70,
0x7172, 0x7374, 0x7576, 0x777A, 0x797A, 0x4142, 0x4344, 0x4546,
0x4748, 0x494A, 0x4B4C, 0x4D4E, 0x4F50, 0x5152, 0x5354, 0x5556,
0x5758, 0x595A, 0x3031, 0x3233, 0x3435, 0x360A
''']
        for input, output in zip(self.inputs, outputs):
            self.assertEqual(self.encode(input), output)

    def test_x2_2(self):
        # Block of lines to Hexadecimal-2.
        self.request('../x2')
        input = ''.join(self.inputs)
        output = '''\
0x0A61, 0x0A61, 0x620A, 0x6162, 0x630A, 0x6162, 0x6364, 0x0A61,
0x6263, 0x6465, 0x6667, 0x6869, 0x0A61, 0x6263, 0x6465, 0x6667,
0x6869, 0x6A6B, 0x6C6D, 0x6E6F, 0x7071, 0x7273, 0x0A61, 0x6263,
0x6465, 0x6667, 0x6869, 0x6A6B, 0x6C6D, 0x6E6F, 0x7071, 0x7273,
0x7475, 0x7677, 0x7A79, 0x7A41, 0x4243, 0x0A61, 0x6263, 0x6465,
0x6667, 0x6869, 0x6A6B, 0x6C6D, 0x6E6F, 0x7071, 0x7273, 0x7475,
0x7677, 0x7A79, 0x7A41, 0x4243, 0x4445, 0x4647, 0x4849, 0x4A4B,
0x4C4D, 0x0A61, 0x6263, 0x6465, 0x6667, 0x6869, 0x6A6B, 0x6C6D,
0x6E6F, 0x7071, 0x7273, 0x7475, 0x7677, 0x7A79, 0x7A41, 0x4243,
0x4445, 0x4647, 0x4849, 0x4A4B, 0x4C4D, 0x4E4F, 0x5051, 0x5253,
0x5455, 0x5657, 0x0A61, 0x6263, 0x6465, 0x6667, 0x6869, 0x6A6B,
0x6C6D, 0x6E6F, 0x7071, 0x7273, 0x7475, 0x7677, 0x7A79, 0x7A41,
0x4243, 0x4445, 0x4647, 0x4849, 0x4A4B, 0x4C4D, 0x4E4F, 0x5051,
0x5253, 0x5455, 0x5657, 0x5859, 0x5A30, 0x3132, 0x3334, 0x3536,
0x0A
'''
        self.assertEqual(self.encode(input), output)

    def test_x2_3(self):
        # Single lines to Hexadecimal-2 and back.
        self.request('../x2')
        for input in self.inputs:
            self.assertEqual(self.decode(self.encode(input)), input)

    def test_x2_4(self):
        # Block of lines to Hexadecimal-2 and back.
        self.request('../x2')
        input = ''.join(self.inputs)
        self.assertEqual(self.decode(self.encode(input)), input)

    def test_x4_1(self):
        # Single lines to Hexadecimal-4.
        self.request('../x4')
        outputs = ['''\
0x0A
''', '''\
0x610A
''', '''\
0x61620A
''', '''\
0x6162630A
''', '''\
0x61626364, 0x0A
''', '''\
0x61626364, 0x65666768, 0x690A
''', '''\
0x61626364, 0x65666768, 0x696A6B6C, 0x6D6E6F70, 0x7172730A
''', '''\
0x61626364, 0x65666768, 0x696A6B6C, 0x6D6E6F70, 0x71727374, 0x7576777A,
0x797A4142, 0x430A
''', '''\
0x61626364, 0x65666768, 0x696A6B6C, 0x6D6E6F70, 0x71727374, 0x7576777A,
0x797A4142, 0x43444546, 0x4748494A, 0x4B4C4D0A
''', '''\
0x61626364, 0x65666768, 0x696A6B6C, 0x6D6E6F70, 0x71727374, 0x7576777A,
0x797A4142, 0x43444546, 0x4748494A, 0x4B4C4D4E, 0x4F505152, 0x53545556,
0x570A
''', '''\
0x61626364, 0x65666768, 0x696A6B6C, 0x6D6E6F70, 0x71727374, 0x7576777A,
0x797A4142, 0x43444546, 0x4748494A, 0x4B4C4D4E, 0x4F505152, 0x53545556,
0x5758595A, 0x30313233, 0x3435360A
''']
        for input, output in zip(self.inputs, outputs):
            self.assertEqual(self.encode(input), output)

    def test_x4_2(self):
        # Block of lines to Hexadecimal-4.
        self.request('../x4')
        input = ''.join(self.inputs)
        output = '''\
0x0A610A61, 0x620A6162, 0x630A6162, 0x63640A61, 0x62636465, 0x66676869,
0x0A616263, 0x64656667, 0x68696A6B, 0x6C6D6E6F, 0x70717273, 0x0A616263,
0x64656667, 0x68696A6B, 0x6C6D6E6F, 0x70717273, 0x74757677, 0x7A797A41,
0x42430A61, 0x62636465, 0x66676869, 0x6A6B6C6D, 0x6E6F7071, 0x72737475,
0x76777A79, 0x7A414243, 0x44454647, 0x48494A4B, 0x4C4D0A61, 0x62636465,
0x66676869, 0x6A6B6C6D, 0x6E6F7071, 0x72737475, 0x76777A79, 0x7A414243,
0x44454647, 0x48494A4B, 0x4C4D4E4F, 0x50515253, 0x54555657, 0x0A616263,
0x64656667, 0x68696A6B, 0x6C6D6E6F, 0x70717273, 0x74757677, 0x7A797A41,
0x42434445, 0x46474849, 0x4A4B4C4D, 0x4E4F5051, 0x52535455, 0x56575859,
0x5A303132, 0x33343536, 0x0A
'''
        self.assertEqual(self.encode(input), output)

    def test_x4_3(self):
        # Single lines to Hexadecimal-4 and back.
        self.request('../x4')
        for input in self.inputs:
            self.assertEqual(self.decode(self.encode(input)), input)

    def test_x4_4(self):
        # Block of lines to Hexadecimal-4 and back.
        self.request('../x4')
        input = ''.join(self.inputs)
        self.assertEqual(self.decode(self.encode(input)), input)

    def test_o1_1(self):
        # Single lines to Octal-1.
        self.request('../o1')
        outputs = ['''\
0012
''', '''\
0141, 0012
''', '''\
0141, 0142, 0012
''', '''\
0141, 0142, 0143, 0012
''', '''\
0141, 0142, 0143, 0144, 0012
''', '''\
0141, 0142, 0143, 0144, 0145, 0146, 0147, 0150, 0151, 0012
''', '''\
0141, 0142, 0143, 0144, 0145, 0146, 0147, 0150, 0151, 0152, 0153, 0154,
0155, 0156, 0157, 0160, 0161, 0162, 0163, 0012
''', '''\
0141, 0142, 0143, 0144, 0145, 0146, 0147, 0150, 0151, 0152, 0153, 0154,
0155, 0156, 0157, 0160, 0161, 0162, 0163, 0164, 0165, 0166, 0167, 0172,
0171, 0172, 0101, 0102, 0103, 0012
''', '''\
0141, 0142, 0143, 0144, 0145, 0146, 0147, 0150, 0151, 0152, 0153, 0154,
0155, 0156, 0157, 0160, 0161, 0162, 0163, 0164, 0165, 0166, 0167, 0172,
0171, 0172, 0101, 0102, 0103, 0104, 0105, 0106, 0107, 0110, 0111, 0112,
0113, 0114, 0115, 0012
''', '''\
0141, 0142, 0143, 0144, 0145, 0146, 0147, 0150, 0151, 0152, 0153, 0154,
0155, 0156, 0157, 0160, 0161, 0162, 0163, 0164, 0165, 0166, 0167, 0172,
0171, 0172, 0101, 0102, 0103, 0104, 0105, 0106, 0107, 0110, 0111, 0112,
0113, 0114, 0115, 0116, 0117, 0120, 0121, 0122, 0123, 0124, 0125, 0126,
0127, 0012
''', '''\
0141, 0142, 0143, 0144, 0145, 0146, 0147, 0150, 0151, 0152, 0153, 0154,
0155, 0156, 0157, 0160, 0161, 0162, 0163, 0164, 0165, 0166, 0167, 0172,
0171, 0172, 0101, 0102, 0103, 0104, 0105, 0106, 0107, 0110, 0111, 0112,
0113, 0114, 0115, 0116, 0117, 0120, 0121, 0122, 0123, 0124, 0125, 0126,
0127, 0130, 0131, 0132, 0060, 0061, 0062, 0063, 0064, 0065, 0066, 0012
''']
        for input, output in zip(self.inputs, outputs):
            self.assertEqual(self.encode(input), output)

    def test_o1_2(self):
        # Block of lines to Octal-1.
        self.request('../o1')
        input = ''.join(self.inputs)
        output = '''\
0012, 0141, 0012, 0141, 0142, 0012, 0141, 0142, 0143, 0012, 0141, 0142,
0143, 0144, 0012, 0141, 0142, 0143, 0144, 0145, 0146, 0147, 0150, 0151,
0012, 0141, 0142, 0143, 0144, 0145, 0146, 0147, 0150, 0151, 0152, 0153,
0154, 0155, 0156, 0157, 0160, 0161, 0162, 0163, 0012, 0141, 0142, 0143,
0144, 0145, 0146, 0147, 0150, 0151, 0152, 0153, 0154, 0155, 0156, 0157,
0160, 0161, 0162, 0163, 0164, 0165, 0166, 0167, 0172, 0171, 0172, 0101,
0102, 0103, 0012, 0141, 0142, 0143, 0144, 0145, 0146, 0147, 0150, 0151,
0152, 0153, 0154, 0155, 0156, 0157, 0160, 0161, 0162, 0163, 0164, 0165,
0166, 0167, 0172, 0171, 0172, 0101, 0102, 0103, 0104, 0105, 0106, 0107,
0110, 0111, 0112, 0113, 0114, 0115, 0012, 0141, 0142, 0143, 0144, 0145,
0146, 0147, 0150, 0151, 0152, 0153, 0154, 0155, 0156, 0157, 0160, 0161,
0162, 0163, 0164, 0165, 0166, 0167, 0172, 0171, 0172, 0101, 0102, 0103,
0104, 0105, 0106, 0107, 0110, 0111, 0112, 0113, 0114, 0115, 0116, 0117,
0120, 0121, 0122, 0123, 0124, 0125, 0126, 0127, 0012, 0141, 0142, 0143,
0144, 0145, 0146, 0147, 0150, 0151, 0152, 0153, 0154, 0155, 0156, 0157,
0160, 0161, 0162, 0163, 0164, 0165, 0166, 0167, 0172, 0171, 0172, 0101,
0102, 0103, 0104, 0105, 0106, 0107, 0110, 0111, 0112, 0113, 0114, 0115,
0116, 0117, 0120, 0121, 0122, 0123, 0124, 0125, 0126, 0127, 0130, 0131,
0132, 0060, 0061, 0062, 0063, 0064, 0065, 0066, 0012
'''
        self.assertEqual(self.encode(input), output)

    def test_o1_3(self):
        # Single lines to Octal-1 and back.
        self.request('../o1')
        for input in self.inputs:
            self.assertEqual(self.decode(self.encode(input)), input)

    def test_o1_4(self):
        # Block of lines to Octal-1 and back.
        self.request('../o1')
        input = ''.join(self.inputs)
        self.assertEqual(self.decode(self.encode(input)), input)

    def test_o2_1(self):
        # Single lines to Octal-2.
        self.request('../o2')
        outputs = ['''\
0012
''', '''\
0060412
''', '''\
0060542, 0012
''', '''\
0060542, 0061412
''', '''\
0060542, 0061544, 0012
''', '''\
0060542, 0061544, 0062546, 0063550, 0064412
''', '''\
0060542, 0061544, 0062546, 0063550, 0064552, 0065554, 0066556, 0067560,
0070562, 0071412
''', '''\
0060542, 0061544, 0062546, 0063550, 0064552, 0065554, 0066556, 0067560,
0070562, 0071564, 0072566, 0073572, 0074572, 0040502, 0041412
''', '''\
0060542, 0061544, 0062546, 0063550, 0064552, 0065554, 0066556, 0067560,
0070562, 0071564, 0072566, 0073572, 0074572, 0040502, 0041504, 0042506,
0043510, 0044512, 0045514, 0046412
''', '''\
0060542, 0061544, 0062546, 0063550, 0064552, 0065554, 0066556, 0067560,
0070562, 0071564, 0072566, 0073572, 0074572, 0040502, 0041504, 0042506,
0043510, 0044512, 0045514, 0046516, 0047520, 0050522, 0051524, 0052526,
0053412
''', '''\
0060542, 0061544, 0062546, 0063550, 0064552, 0065554, 0066556, 0067560,
0070562, 0071564, 0072566, 0073572, 0074572, 0040502, 0041504, 0042506,
0043510, 0044512, 0045514, 0046516, 0047520, 0050522, 0051524, 0052526,
0053530, 0054532, 0030061, 0031063, 0032065, 0033012
''']
        for input, output in zip(self.inputs, outputs):
            self.assertEqual(self.encode(input), output)

    def test_o2_2(self):
        # Block of lines to Octal-2.
        self.request('../o2')
        input = ''.join(self.inputs)
        output = '''\
0005141, 0005141, 0061012, 0060542, 0061412, 0060542, 0061544, 0005141,
0061143, 0062145, 0063147, 0064151, 0005141, 0061143, 0062145, 0063147,
0064151, 0065153, 0066155, 0067157, 0070161, 0071163, 0005141, 0061143,
0062145, 0063147, 0064151, 0065153, 0066155, 0067157, 0070161, 0071163,
0072165, 0073167, 0075171, 0075101, 0041103, 0005141, 0061143, 0062145,
0063147, 0064151, 0065153, 0066155, 0067157, 0070161, 0071163, 0072165,
0073167, 0075171, 0075101, 0041103, 0042105, 0043107, 0044111, 0045113,
0046115, 0005141, 0061143, 0062145, 0063147, 0064151, 0065153, 0066155,
0067157, 0070161, 0071163, 0072165, 0073167, 0075171, 0075101, 0041103,
0042105, 0043107, 0044111, 0045113, 0046115, 0047117, 0050121, 0051123,
0052125, 0053127, 0005141, 0061143, 0062145, 0063147, 0064151, 0065153,
0066155, 0067157, 0070161, 0071163, 0072165, 0073167, 0075171, 0075101,
0041103, 0042105, 0043107, 0044111, 0045113, 0046115, 0047117, 0050121,
0051123, 0052125, 0053127, 0054131, 0055060, 0030462, 0031464, 0032466,
0012
'''
        self.assertEqual(self.encode(input), output)

    def test_o2_3(self):
        # Single lines to Octal-2 and back.
        self.request('../o2')
        for input in self.inputs:
            self.assertEqual(self.decode(self.encode(input)), input)

    def test_o2_4(self):
        # Block of lines to Octal-2 and back.
        self.request('../o2')
        input = ''.join(self.inputs)
        self.assertEqual(self.decode(self.encode(input)), input)

    def test_o4_1(self):
        # Single lines to Octal-4.
        self.request('../o4')
        outputs = ['''\
0012
''', '''\
0060412
''', '''\
030261012
''', '''\
014130461412
''', '''\
014130461544, 0012
''', '''\
014130461544, 014531463550, 0064412
''', '''\
014130461544, 014531463550, 015132465554, 015533467560,
016134471412
''', '''\
014130461544, 014531463550, 015132465554, 015533467560,
016134471564, 016535473572, 017136440502, 0041412
''', '''\
014130461544, 014531463550, 015132465554, 015533467560,
016134471564, 016535473572, 017136440502, 010321042506,
010722044512, 011323046412
''', '''\
014130461544, 014531463550, 015132465554, 015533467560,
016134471564, 016535473572, 017136440502, 010321042506,
010722044512, 011323046516, 011724050522, 012325052526,
0053412
''', '''\
014130461544, 014531463550, 015132465554, 015533467560,
016134471564, 016535473572, 017136440502, 010321042506,
010722044512, 011323046516, 011724050522, 012325052526,
012726054532, 006014231063, 006415233012
''']
        for input, output in zip(self.inputs, outputs):
            self.assertEqual(self.encode(input), output)

    def test_o4_2(self):
        # Block of lines to Octal-4.
        self.request('../o4')
        input = ''.join(self.inputs)
        output = '''\
001230205141, 014202460542, 014302460542, 014331005141,
014230662145, 014631664151, 001230261143, 014431263147,
015032265153, 015433267157, 016034271163, 001230261143,
014431263147, 015032265153, 015433267157, 016034271163,
016435273167, 017236275101, 010220605141, 014230662145,
014631664151, 015232666155, 015633670161, 016234672165,
016635675171, 017220241103, 010421243107, 011022245113,
011423205141, 014230662145, 014631664151, 015232666155,
015633670161, 016234672165, 016635675171, 017220241103,
010421243107, 011022245113, 011423247117, 012024251123,
012425253127, 001230261143, 014431263147, 015032265153,
015433267157, 016034271163, 016435273167, 017236275101,
010220642105, 010621644111, 011222646115, 011623650121,
012224652125, 012625654131, 013214030462, 006315032466,
0012
'''
        self.assertEqual(self.encode(input), output)

    def test_o4_3(self):
        # Single lines to Octal-4 and back.
        self.request('../o4')
        for input in self.inputs:
            self.assertEqual(self.decode(self.encode(input)), input)

    def test_o4_4(self):
        # Block of lines to Octal-4 and back.
        self.request('../o4')
        input = ''.join(self.inputs)
        self.assertEqual(self.decode(self.encode(input)), input)

if __name__ == '__main__':
    import unittest
    unittest.main()