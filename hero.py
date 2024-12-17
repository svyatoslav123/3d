key_switch_camera = "c"
key_switch_mode = "z"
key_forward = "w"
key_back = "s"
key_left = "a"
key_right = "d"
key_up = "e"
key_down =  "q"


key_turn_left = "n"
key_turn_right = "m"

class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModel("smily")
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBird()
        self.accept_events()

    def cameraBird(self):
        base.disableMouse()
        base.camera.seTH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraON = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False

        def changeView(self):
            if self.cameraOn:
                self.cameraUp()
            else:
                self.cameraBird()

        def turn_left(self):
            self.hero.setH((self.hero.getH()+ 5)% 360)
        def turn_right(self):
            self.hero.setH((self.hero.getH() + 5) % 360)

        def look_at(self, angle):
            x_from = round(self.hero.getX())
            y_from = round(self.hero.getY())
            z_from = round(self.hero.getZ())

            dx, dy = self.check_dir(angle)
            x_to = x_from + dx
            y_to = y_from + dy
            return x_to,y_to,z_from

        def just_move(self, angle):
            pos = self.look_at(angle)
            self.hero.setPos(pos)

        def move_to(self, angle):
            if self.mode:
                self.just_move(angle)

        def chack_dir(self, angle):
            if angle >= 0 and angle <= 20:
                return (0, -1)
            elif angle <= 65:
                return (1, -1)
            elif angle <= 110:
                return (1, 0)
            elif angle <= 155:
                return (1, -1)
            elif angle <= 200:
                return (1, -1)
            elif angle <= 245:
                return (1, -1)
            elif angle <= 290:
                return (1, -1)
            elif angle <= 335:
                return (1, -1)
        



