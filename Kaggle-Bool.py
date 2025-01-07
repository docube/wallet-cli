x = True;
print(x);
print(type(x));

def can_run_for_president(age):
    """Can someone of the given age run for the president in Nigeria?"""
    # The Nigerian Constitution says you must be at least 35years old
    return age >= 35;
print("Can a 19-year-old run for president?", can_run_for_president(19));
print("Can a 45-year-old run for president?", can_run_for_president(45));

print(3.0 == 3);
print(3.0 == '3');

def is_odd(n):
    return (n % 2) == 1;

print("Is 100 Odd?", is_odd(100));
print("Is -17 Odd?", is_odd(-17));

def can_run_for_nigerian_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for the president of Nigeria?"""
    # The Nigerian constitution states that you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35);

print(can_run_for_nigerian_president(19, True));
print(can_run_for_nigerian_president(55, False));
print(can_run_for_nigerian_president(55, True));

print(True or True and False);
print(True and False);