import random

class RandomSearch:
    """
        for random search what is needed

            - a function to asend to
            - an initial value
            - step value
            - step-lenght parameter
            - how many random guesses in each step
    """

    def __init__(self, fn, step, init_value, step_lenght_param, step_count=50, guess_count=100, try_count=5):
        self.fn = fn
        self.step = step
        self.init_value = init_value
        self.step_lenght_param = step_lenght_param
        self.step_count = step_count
        self.guess_count = guess_count
        self.try_count = try_count
        self.secure_random = random.SystemRandom()

    def random_input(self, values):
        arg_count = len(self.init_value)
        result = []
        for i in range(0, arg_count):
            rand = self.secure_random.uniform(-self.step, self.step) * self.step_lenght_param
            result.append(values[i] + rand)
        return result

    def do_run(self):
        input_value = self.init_value
        output = self.fn(*input_value)
        best_inputs = []
        best_inputs.append(input_value)
        for s in range(0, self.step_count):
            current_step__best_input = input_value
            for n in range(0, self.guess_count):
                input_value = self.random_input(current_step__best_input)
                new_output = self.fn(*input_value)
                if new_output < output:
                    current_step__best_input = input_value
                    output = new_output
            best_inputs.append(current_step__best_input)
            
        return output, best_inputs

    def run(self):
        value, inputs = self.do_run()
        for i in range(0, self.try_count):
            new_value, new_inputs = self.do_run()
            if new_value < value:
                value = new_value
                inputs = new_inputs

        return value, inputs

