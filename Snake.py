class Snake:
    body = []
    eyes = []

    def __init__(self):

        self.body = []
        self.eyes = []

        # On ajoute au corps du serpent son premier carré
        # avec ses coordonnées, donc sa tête
        coord_sneak = [50, 50, 60, 60]
        self.body.append(coord_sneak)

        # On ajoute à la tête du serpent ses yeux

        self.eyes.append([self.body[0][0] + 6, self.body[0][1] + 2,
                          self.body[0][2] - 2, self.body[0][3] - 6,
                          self.body[0][0] + 6, self.body[0][1] + 6,
                          self.body[0][2] - 2, self.body[0][3] - 2])

    def reset(self):
        self.__init__()

    def _get_body(self, body):
        return body

    def _get_eyes(self, eyes):
        return eyes

    def moveHead(self, direction):

        coord = len(self.body[0])

        if direction == 1:

            x1 = self.body[0][coord - 4]
            y1 = self.body[0][coord - 3]
            x2 = self.body[0][coord - 2]
            y2 = self.body[0][coord - 1]

            x1 = x1 + 10
            x2 = x2 + 10
            y2 = y2 + 10

            self.body[0].append(x1)
            self.body[0].append(y1)
            self.body[0].append(x2)
            self.body[0].append(y2)

        elif direction == 2:

            x1 = self.body[0][coord - 4]
            y1 = self.body[0][coord - 3]
            x2 = self.body[0][coord - 2]
            y2 = self.body[0][coord - 1]

            x1 = x1 - 10
            x2 = x2 - 10
            y2 = y2 + 10

            self.body[0].append(x1)
            self.body[0].append(y1)
            self.body[0].append(x2)
            self.body[0].append(y2)

        elif direction == 3:

            x1 = self.body[0][coord - 4]
            y1 = self.body[0][coord - 3]
            x2 = self.body[0][coord - 2]
            y2 = self.body[0][coord - 1]

            y1 = y1 + 10
            y2 = y2 + 10

            self.body[0].append(x1)
            self.body[0].append(y1)
            self.body[0].append(x2)
            self.body[0].append(y2)

        elif direction == 4:

            x1 = self.body[0][coord - 4]
            y1 = self.body[0][coord - 3]
            x2 = self.body[0][coord - 2]
            y2 = self.body[0][coord - 1]

            x2 = x2 + 10
            y2 = y2 - 10

            self.body[0].append(x1)
            self.body[0].append(y1)
            self.body[0].append(x2)
            self.body[0].append(y2)

        return [x1, y1, x2, y2]

    def moveBody(self, direction, lenImage, dx, dy):

        i = 4
        j = 1

        while j < lenImage:
            self.body[0][len(self.body[0]) - (i)] \
                = self.body[0][len(self.body[0]) - (i + 4)]
            self.body[0][len(self.body[0]) - (i - 1)] \
                = self.body[0][len(self.body[0]) - (i + 3)]
            self.body[0][len(self.body[0]) - (i - 2)] \
                = self.body[0][len(self.body[0]) - (i + 2)]
            self.body[0][len(self.body[0]) - (i - 3)] \
                = self.body[0][len(self.body[0]) - (i + 1)]
            i += 4
            j += 1

        # Avancer du serpent

        self.body[0][0] = self.body[0][0] + dx
        self.body[0][1] = self.body[0][1] + dy
        self.body[0][2] = self.body[0][0] + 10
        self.body[0][3] = self.body[0][1] + 10

        # Gestion des yeux

        if direction == 1:
            self.eyes[0][0] = self.body[0][0] + 2
            self.eyes[0][1] = self.body[0][1] + 2
            self.eyes[0][2] = self.body[0][2] - 6
            self.eyes[0][3] = self.body[0][3] - 6
            self.eyes[0][4] = self.body[0][0] + 2
            self.eyes[0][5] = self.body[0][1] + 6
            self.eyes[0][6] = self.body[0][2] - 6
            self.eyes[0][7] = self.body[0][3] - 2

        elif direction == 2:
            self.eyes[0][0] = self.body[0][0] + 6
            self.eyes[0][1] = self.body[0][1] + 2
            self.eyes[0][2] = self.body[0][2] - 2
            self.eyes[0][3] = self.body[0][3] - 6
            self.eyes[0][4] = self.body[0][0] + 6
            self.eyes[0][5] = self.body[0][1] + 6
            self.eyes[0][6] = self.body[0][2] - 2
            self.eyes[0][7] = self.body[0][3] - 2

        elif direction == 3:
            self.eyes[0][0] = self.body[0][0] + 2
            self.eyes[0][1] = self.body[0][1] + 2
            self.eyes[0][2] = self.body[0][2] - 6
            self.eyes[0][3] = self.body[0][3] - 6
            self.eyes[0][4] = self.body[0][0] + 6
            self.eyes[0][5] = self.body[0][1] + 2
            self.eyes[0][6] = self.body[0][2] - 2
            self.eyes[0][7] = self.body[0][3] - 6

        elif direction == 4:
            self.eyes[0][0] = self.body[0][0] + 2
            self.eyes[0][1] = self.body[0][1] + 6
            self.eyes[0][2] = self.body[0][2] - 6
            self.eyes[0][3] = self.body[0][3] - 2
            self.eyes[0][4] = self.body[0][0] + 6
            self.eyes[0][5] = self.body[0][1] + 6
            self.eyes[0][6] = self.body[0][2] - 2
            self.eyes[0][7] = self.body[0][3] - 2
