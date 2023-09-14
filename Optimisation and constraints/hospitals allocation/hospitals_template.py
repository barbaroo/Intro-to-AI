import random


class Space():

    def __init__(self, height, width, num_hospitals):
        """Create a new state space with given dimensions."""
        self.height = height
        self.width = width
        self.num_hospitals = num_hospitals
        self.houses = set()
        self.hospitals = set()

    def add_house(self, row, col):
        """
        TODO: Add a house at a particular location in the state space.
        """
        self.houses.___((row, col))

    def available_spaces(self):
        """
        TODO: Return all cells not currently used by a house or hospital.
        """
        # Consider all possible cells
        candidates = set(
            (___, ___)
            for row in range(self.___)
            for col in range(self.___)
        )

        # TODO: Remove all houses and hospitals from candidates
        # You can use a loop or set operations
        for ___ in self.___:
            ___.remove(house)
        for hospital in self.hospitals:
            ___.remove(hospital)

        return candidates

    def hill_climb(self, maximum=None, image_prefix=None, log=False):
        """
        TODO: Implement the hill-climbing algorithm to find an optimal solution.
        """
        count = 0

        # Start by initializing hospitals randomly
        self.hospitals = set()
        for i in range(self.num_hospitals):
            # Add available spaces for hospitals
            self.hospitals.add(random.choice(list(self.___())))
        if log:
            print("Initial state: cost", self.get_cost(self.hospitals))
        if image_prefix:
            self.output_image(f"{image_prefix}{str(count).zfill(3)}.png")

        # Continue until we reach the maximum number of iterations
        while maximum is None or ___ < maximum:
            best_neighbors = []
            best_neighbor_cost = None

            # TODO: Iterate through hospitals and their neighbors to find best neighbor
            # Use self.get_neighbors and self.get_cost
            for ___ in self.___:

                # Consider all neighbors for that hospital
                for replacement in self.get_neighbors(*hospital):

                    # Generate a neighboring set of hospitals.
                    # You might want to remove the previous hospital position and add the replacement
                    neighbor = self.hospitals.___()
                    neighbor.___(hospital)
                    neighbor.___(replacement)

            # TODO: Decide whether to move to the best neighbor or not based on its cost

                    # Check if neighbor is best so far. You will have to compare the current cost with the best cost.
                    cost = self.___(neighbor)
                    if best_neighbor_cost is None or ___ < ___:
                        best_neighbor_cost = ___
                        best_neighbors = [neighbor]
                    elif ___ == ___:
                        best_neighbors.append(neighbor)


           # None of the neighbors are better than the current state. 
           # What happens to the hospital positions in this case?
            if ___ >= self.get_cost(self.___):
                return self.___

            # Move to a highest-valued neighbor
            else:
                if log:
                    print(f"Found better neighbor: cost {best_neighbor_cost}")
                self.hospitals = random.choice(best_neighbors)

            # Generate image
            if image_prefix:
                self.output_image(f"{image_prefix}{str(count).zfill(3)}.png")



    def random_restart(self, maximum, image_prefix=None, log=False):
        """
        TODO: Repeats hill-climbing multiple times to potentially find better solutions.
        """
        best_hospitals = None
        best_cost = None

        # TODO: Implement the random restart logic
        # Use self.hill_climb and self.get_cost

        # The number of iterations for random_restart is given as an input

        for i in range(___):
            hospitals = self.___()
            cost = self.___(___)
            if ___ is None or cost < ___:
                best_cost = cost
                best_hospitals = ___
                if log:
                    print(f"{i}: Found new best state: cost {cost}")
            else:
                if log:
                    print(f"{i}: Found state: cost {cost}")

            if image_prefix:
                self.output_image(f"{image_prefix}{str(i).zfill(3)}.png")

        return ___

    def get_cost(self, hospitals):
        """
        TODO: Calculate the sum of distances from houses to the nearest hospital.
        """
        cost = 0

        # TODO: For each house, find the nearest hospital and add its distance to the cost

        for house in self.___:
            cost += min(
                abs(___[0] - ___[0]) + abs(___[1] - ___[1])
                for hospital in hospitals
            )

        return ___

    def get_neighbors(self, row, col):
        """
        TODO: Return neighbors not already containing a house or hospital.
        """
        # Neighbors are calculated along rows and columns.

        candidates = [
            (row - 1, col),
            (___ + ___, ___),
            (___, ___ - ___),
            (___, ___ + ___)
        ]

        # TODO: Get neighboring coordinates and filter out those that are already occupied

        neighbors = []
        for r, c in candidates:
            if (___, ___) in self.___ or (___, ___) in self.___:
                continue
            if 0 <= r < self.___ and 0 <= c < self.___:
                neighbors.append((___, ___))
        return neighbors

    def output_image(self, filename):
        """Generates image with all houses and hospitals."""
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        cost_size = 40
        padding = 10

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.width * cell_size,
             self.height * cell_size + cost_size + padding * 2),
            "white"
        )
        house = Image.open("assets/images/House.png").resize(
            (cell_size, cell_size)
        )
        hospital = Image.open("assets/images/Hospital.png").resize(
            (cell_size, cell_size)
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 30)
        draw = ImageDraw.Draw(img)

        for i in range(self.height):
            for j in range(self.width):

                # Draw cell
                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                draw.rectangle(rect, fill="black")

                if (i, j) in self.houses:
                    img.paste(house, rect[0], house)
                if (i, j) in self.hospitals:
                    img.paste(hospital, rect[0], hospital)

        # Add cost
        draw.rectangle(
            (0, self.height * cell_size, self.width * cell_size,
             self.height * cell_size + cost_size + padding * 2),
            "black"
        )
        draw.text(
            (padding, self.height * cell_size + padding),
            f"Cost: {self.get_cost(self.hospitals)}",
            fill="white",
            font=font
        )

        img.save(filename)


# Create a new space and add houses randomly
s = Space(height=10, width=20, num_hospitals=3)
for i in range(15):
    s.add_house(random.randrange(s.height), random.randrange(s.width))

# Use local search to determine hospital placement
hospitals = s.hill_climb(image_prefix="hospitals", log=True)

