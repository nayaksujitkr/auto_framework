from string import ascii_letters, digits
import random
 
def random_string(minimum_length, maximum_length=None, acceptable_characters=None, prefix='', suffix='', internal_repeat_ok=True):
     
    if acceptable_characters is None:
        acceptable_characters = ascii_letters + digits
    if not internal_repeat_ok and minimum_length > (len(acceptable_characters) + len(prefix) + len(suffix)):
        raise ValueError('Cannot create a string of length %d without repeats with the provided acceptable characters.')
    if maximum_length is not None:
        if maximum_length < minimum_length:
            raise ValueError('maximum_length must be greater than minimum_length if provided.')
        if not internal_repeat_ok and maximum_length > len(acceptable_characters):
            maximum_length = len(acceptable_characters)
        target_length = random.randrange(minimum_length, maximum_length)
    else:
        target_length = minimum_length
    generated_string = prefix
    counter = len(prefix)
    while counter <= target_length - len(suffix):
        next_character = random.choice(acceptable_characters)
        generated_string += next_character
        if not internal_repeat_ok:
            index = acceptable_characters.index(next_character)
            acceptable_characters = acceptable_characters[:index]+acceptable_characters[index+1:]
        counter += 1
    return generated_string