from manim import *
class Triangles(Scene):
    def construct(self):
        triangle1 = Triangle()  # create first triangle
        triangle2 = Triangle()  # create second triangle
        triangle3 = Triangle()  # create a triangle
        triangle1.set_fill(GREEN, opacity=0.5)  # set the color and transparency        
        triangle1.set_stroke(GREEN, width=4)  # set stroke 
        triangle2.set_fill(GREEN, opacity=0.5)  # set the color and transparency
        triangle2.set_stroke(GREEN, width=4)  # set the color and transparency
        triangle3.set_fill(GREEN, opacity=0.5)  # set the color and transparency
        triangle3.set_stroke(GREEN, width=4)  # set the color and transparency

        #No doubt there's a way to create lots of shapes at one time and set all their properties to be identcal.

        v1 = triangle1.get_vertices()[0]-triangle1.get_vertices()[1] # Get first "unit cell" vector from vertices. 
        v2 = triangle1.get_vertices()[1]-triangle1.get_vertices()[2] # Get second "unit cell" vector from vertices.

        u1 = Tex(r"$\mathbf{a}$").align_to(triangle1,UL) # Define text for unit cell vector. Position isn't good. Need normal to triangle edge and midpoint. Good resource here: https://stackoverflow.com/questions/57684480/how-to-determine-the-edge-center-of-a-polygon
        u2 = Tex(r"$\mathbf{b}$").align_to(triangle1,DOWN) #
        u1arrow = Arrow(start=triangle1.get_vertices()[1], end=triangle1.get_vertices()[0], color=WHITE, buff=0, stroke_width=2) #Define arrow. Doesn't look pretty.
        u2arrow = Arrow(start=triangle1.get_vertices()[1], end=triangle1.get_vertices()[2], color=WHITE, buff=0, stroke_width=2)

        mid1 = (triangle1.get_vertices()[1]+triangle1.get_vertices()[0])/2 #Find midpoint between 0 and 1 vertices of triangle 1.
        dot1 = Dot(point=mid1, radius=0.1) # Put a dot there to confirm location.

        # Start test animation:
        self.play(DrawBorderThenFill(triangle1), run_time = 1)  # show the shapes on screen
        self.play(Create(dot1))
        self.play(Create(u1arrow))
        self.play(Write(v1))  # show the shapes on screen
        self.play(Create(u2arrow))
        self.play(Write(v2))  # show the shapes on screen
        self.play(DrawBorderThenFill(triangle2), run_time = 1)  # show the shapes on screen
        self.play(triangle2.animate.shift(t1))
        self.play(DrawBorderThenFill(triangle3), run_time = 1)  # show the shapes on screen
        self.play(triangle3.animate.shift(t2))

        #The "script":
        # 1. Show the hexagonal lattice produced by the LJ simulation. (Need array of dots or circles)
        # 2. Show the triangles connecting the dots.
        # 3. Draw "lattice vector" and show mathematical representations.
        # 4. Tile, showing no space-filling occurs without rotation.
        # 5. Restart, this time showing a parallelgram with primitive unit cell.
        # 6. Run through the same process, this time tiling correctly via translation.
        # 7. Finally, show other non-primitive options for the unit cell. The hexagonal conventional, for example, better shows the symmetry.
