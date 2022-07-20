class paipuchuli():
    def __init__(self, paipu, target):
        self.target = target
        self.paipu = paipu
        self.generate(paipu[7])

    def generate(self, paipu_1):
        tupian = 0
        self.ten = [0] * 4
        self.label = []
        self.qipaiku_0 = [0] * 24
        self.qipaiku_1 = [0] * 24
        self.qipaiku_2 = [0] * 24
        self.qipaiku_3 = [0] * 24
        self.dora = [0] * 5
        self.reach = [0] * 4
        self.dora_count = 0
        self.qipai_0_count = 0
        self.qipai_1_count = 0
        self.qipai_2_count = 0
        self.qipai_3_count = 0
        mo_0 = re.compile(r"[T]\d\d*")
        mo_1 = re.compile(r"[U]\d\d*")
        mo_2 = re.compile(r"[V]\d\d*")
        mo_3 = re.compile(r"[W]\d\d*")
        qi_0 = re.compile(r"[D]\d\d*")
        qi_1 = re.compile(r"[E]\d\d*")
        qi_2 = re.compile(r"[F]\d\d*")
        qi_3 = re.compile(r"[G]\d\d*")
        for num, i in enumerate(paipu_1):
            if isinstance(i, str):
                if self.target == 3:
                    if re.match(mo_3, i):
                        self.hai.append(i[1:])
                        tupian = tupian + 1
                        print('图片 %d' % (len(self.hai)))
                    elif re.match(qi_0, i) != None:
                        self.qipaiku_0[self.qipai_0_count] = i[1:]
                        self.qipai_0_count += 1
                    elif re.match(qi_1, i) != None:
                        self.qipaiku_1[self.qipai_1_count] = i[1:]
                        self.qipai_1_count += 1
                    elif re.match(qi_2, i) != None:
                        self.qipaiku_2[self.qipai_2_count] = i[1:]
                        self.qipai_2_count += 1
                    elif re.match(qi_3, i) != None:
                        self.qipaiku_3[self.qipai_3_count] = i[1:]
                        self.qipai_3_count += 1
                        self.label.append(i[1:])
                        self.hai.remove(i[1:])
                elif self.target == 0:
                    if re.match(mo_0, i):
                        self.hai.append(i[1:])
                        tupian = tupian + 1
                        print('图片 %d' % (len(self.hai)))
                    elif re.match(qi_0, i) != None:
                        self.qipaiku_0[self.qipai_0_count] = i[1:]
                        self.qipai_0_count += 1
                        self.label.append(i[1:])
                        self.hai.remove(i[1:])
                    elif re.match(qi_1, i) != None:
                        self.qipaiku_1[self.qipai_1_count] = i[1:]
                        self.qipai_1_count += 1
                    elif re.match(qi_2, i) != None:
                        self.qipaiku_2[self.qipai_2_count] = i[1:]
                        self.qipai_2_count += 1
                    elif re.match(qi_3, i) != None:
                        self.qipaiku_3[self.qipai_3_count] = i[1:]
                        self.qipai_3_count += 1

                elif self.target == 1:
                    if re.match(mo_1, i):
                        self.hai.append(i[1:])
                        tupian = tupian + 1
                        print('图片 %d' % (len(self.hai)))
                    elif re.match(qi_0, i) != None:
                        self.qipaiku_0[self.qipai_0_count] = i[1:]
                        self.qipai_0_count += 1
                    elif re.match(qi_1, i) != None:
                        self.qipaiku_1[self.qipai_1_count] = i[1:]
                        self.qipai_1_count += 1
                        self.label.append(i[1:])
                        self.hai.remove(i[1:])
                    elif re.match(qi_2, i) != None:
                        self.qipaiku_2[self.qipai_2_count] = i[1:]
                        self.qipai_2_count += 1
                    elif re.match(qi_3, i) != None:
                        self.qipaiku_3[self.qipai_3_count] = i[1:]
                        self.qipai_3_count += 1

                elif self.target == 2:
                    if re.match(mo_2, i):
                        self.hai.append(i[1:])
                        tupian = tupian + 1
                        print('图片 %d' % (len(self.hai)))
                    elif re.match(qi_0, i) != None:
                        self.qipaiku_0[self.qipai_0_count] = i[1:]
                        self.qipai_0_count += 1
                    elif re.match(qi_1, i) != None:
                        self.qipaiku_1[self.qipai_1_count] = i[1:]
                        self.qipai_1_count += 1
                    elif re.match(qi_2, i) != None:
                        self.qipaiku_2[self.qipai_2_count] = i[1:]
                        self.qipai_2_count += 1
                        self.label.append(i[1:])
                        self.hai.remove(i[1:])
                    elif re.match(qi_3, i) != None:
                        self.qipaiku_3[self.qipai_3_count] = i[1:]
                        self.qipai_3_count += 1


            else:
                if i.tag == 'INIT':
                    if self.target == 0:
                        self.hai = list(i.attrib['hai0'].split(','))
                    elif self.target == 1:
                        self.hai = list(i.attrib['hai1'].split(','))
                    elif self.target == 2:
                        self.hai = list(i.attrib['hai2'].split(','))
                    elif self.target == 3:
                        self.hai = list(i.attrib['hai3'].split(','))

                    ten = i.attrib['ten'].split(',')
                    for t in range(4):
                        self.ten[t] = int(ten[t])
                    oya = i.attrib['oya']
                    ten = list(i.attrib['ten'].split(','))
                    seed = list(i.attrib['seed'].split(','))
                    self.benchang = seed[1]
                    self.gongtuo = seed[2]
                    self.dora[self.dora_count] = seed[5]
                    self.dora_count = self.dora_count + 1
                elif i.tag == "REACH":
                    if i.attrib['step'] == '1':
                        self.reach[int(i.attrib['who'])] = 1
                    elif i.attrib['step'] == '2':
                        ten = i.attrib['ten'].split(',')
                        for i in range(4):
                            self.ten[i] = int(ten[i])
                elif i.tag == "DORA":
                    self.dora[self.dora_count] = i.attrib['hai']
                    self.dora_count = self.dora_count + 1
                elif i.tag == "N":
                    m = int(i.attrib['m'])
                    kui = (m & 3)
                    if m & (1 << 2):
                        # chi
                        kind = 0
                        t = (m & 0xFC00) >> 10
                        r = t % 3
                        t = math.floor(t / 3)
                        t = math.floor(t / 7) * 9 + (t % 7)
                        t *= 4
                        h = [t + 4 * 0 + ((m & 0x0018) >> 3), t + 4 * 1 + ((m & 0x0060) >> 5),
                             t + 4 * 2 + ((m & 0x0180) >> 7)]
                    elif m & (1 << 3):
                        # peng
                        kind = 1
                        t = (m & 0xFE00) >> 9
                        r = t % 3
                        t = math.floor(t / 3)
                        t *= 4
                        h = [t, t, t]
                    elif m & (1 << 4):
                        # jia gang
                        kind = 2
                        added = (m & 0x0060) >> 5
                        t = (m & 0xFE00) >> 9
                        r = t % 3
                        t = math.floor(t / 3)
                        t *= 4
                        h = [t, t, t, t]
                    else:
                        # ming an gang
                        hai0 = (m & 0xFF00) >> 8
                        if (not kui):
                            # ankang
                            kind = 3
                            hai0 = (hai0 & ~3) + 3
                        else:
                            # mingkang
                            kind = 4
                        t = math.floor(hai0 / 4) * 4
                        h = [t, t, t, t]
                    if int(i.attrib['who']) == self.target:
                        if kind == 0 or kind == 1:
                            self.hai.append(paipu_1[num - 1][1:])
                        elif kind == 3:
                            self.hai.remove(str(h[0])
                            # print(len(self.label))
                            # print(self.label)

