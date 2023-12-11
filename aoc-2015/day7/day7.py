import re
import operator

# Setup

gate_func_dict = {
    "CONSTANT": lambda x: x,
    "BOOST": lambda x: x,
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
    "NOT": operator.invert
}
gate_type_regex = '|'.join(gate_func_dict.keys())


class Gate:
    def __init__(self, description):
        config, self.outwire = description.strip().split(" -> ")

        if config.isdigit():
            self.gate_type = "CONSTANT"
            self.outvalue = int(config)
            self.operands = []
        else:
            func_match = re.search(gate_type_regex, config)

            self.gate_type = func_match[0] if func_match else "BOOST"
            self.outvalue = None
            self.operands = [operand.strip() for operand in config.split(
                self.gate_type) if not operand == '']

    def reset(self):
        if self.gate_type != "CONSTANT":
            self.outvalue = None

    def unknown_inputs(self, circuit):
        if self.outvalue:
            return []
        return [op for op in self.operands
                if not op.isdigit() and circuit[op].outvalue is None]

    def eval_operand(self, op, circuit):
        return int(op) if op.isdigit() else circuit[op].outvalue

    def calculate(self, circuit):
        self.outvalue = gate_func_dict[self.gate_type](
            *(self.eval_operand(op, circuit) for op in self.operands))


def get_signal(wire, circuit):
    calculation_stack = [wire]

    while calculation_stack:
        gate = circuit[calculation_stack[0]]
        unknowns = gate.unknown_inputs(circuit)
        if unknowns:
            calculation_stack = unknowns + calculation_stack
        else:
            gate.calculate(circuit)
            calculation_stack.pop(0)

    return circuit[wire].outvalue


with open("input.txt", "r") as input_file:
    gates = [Gate(line) for line in input_file.readlines()]

circuit = {gate.outwire: gate for gate in gates}

# Part One

a_signal = get_signal('a', circuit)

print('--Part One--')
print(a_signal)

# Part Two

for gate in circuit.values():
    gate.reset()

circuit['b'].outvalue = a_signal

print('--Part Two--')
print(get_signal('a', circuit))
