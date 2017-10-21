import sys


# My Solution
def decompress(input):
    if not input:
        return ""

    digit_end = 0
    while input[digit_end].isdigit():
        digit_end += 1

    if digit_end == 0:
        return input.replace(r"[]", "")

    times = int(input[:digit_end])

    bracket_start = digit_end
    bracket_end = bracket_start + 1
    temp = bracket_start
    counter = 0

    for i in range(bracket_start, len(input)):
        c = input[i]
        if c == "[":
            counter += 1
        elif c == "]":
            counter -= 1

        if counter == 0:
            bracket_end = i
            break

    return (
        (times * decompress(input[bracket_start+1: bracket_end]))
        + decompress(input[bracket_end+1:])
    )


# print(decompress("3[abc]4[ab]c"))
# print(decompress("2[3[a]b]"))
# print(decompress("a[]b"))
# print(decompress("0[abc]1[a]"))

# Google Solution
def decomp(text, start=0, times=1):
    """
    Iterate over and decompress the compressed string.
    This approach makes use of nested Python iterators, which is a
    very clean way of expressing expansion of nested iterated items.
    Args:
        text: The entire string to decompress.  It's unobvious, but nice
          to have the whole string plus an index; this allows any error
          detection code to report the absolute index of a problematic
          character.
        start: The starting index within 'text'.  We decompress from
          'start' up through the matching close-brace or end-of-string.
        times: The number of times to repeat decompression.
    """
    # Repeat iteration over our sub-chunk N times.
    for _ in range(times):
        i = start
        # Until we hit the end of the string, or end of our chunk...
        while i < len(text) and text[i] != ']':
            # Emit letters as themselves.
            if text[i].islower():
                yield text[i]
        # If it's not a letter, it must be digit(s).  Convert to integer.
        else:
            sub_times = 0
            while text[i].isdigit():
                sub_times = sub_times * 10 + int(text[i])
                i += 1
            i += 1  # Skip past open-bracket
            # Start an iterator over the sub-chunk.
            for item in decomp(text, i, sub_times):
                # Iterator generates many characters, and then at the very end,
                # it generates an integer.  Provide characters up to our caller,
                # and use the integer to advance our index 'i' to end-of-chunk.
                if isinstance(item, basestring):
                    yield item
                else:
                    i = item
            # Advance 'i' to the next letter, or skip the close-bracket, whichever.
            i += 1
    # Don't emit the trailing integer if we are doing the outermost call.  This
    # test could be moved to the decompress() call instead; we would check there
    # to see if the result item was basestring or int, just as we do above, but
    # I suspect that check would be more expensive than a simple integer
    # comparison here, where the type is known.
    if start > 0:
        yield i


def decompress(text):
    # We could wrap 'text' to add a leading '1[' and trailing ']' to allow a
    # little bit of simplification in the logic in decomp(), but the
    # simplification would lead to harder-to-read code, as well as requiring
    # O(n) additional time, and a temporary requirement for O(n + 3) additional
    # space during the copy operation.
    #
    # This is O(decompressed-length) for speed (probably), and up to
    # O(compressed-length/4) for additional storage.  In this implementation,
    # the storage requirement is well-disguised: It appears on the function call
    # stack, rather than in declared variables.  E.g., consider a worst-case
    # input of: 1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[1[xx]]]]]]]]]]]]]]]]]]]]
    # which would require a stack depth of 20.
    #
    # The (probably) for the big-O depends on how well Python implements
    # resumption of nested iteration.  At worst, the string above would require
    # a full stack descent, then ascent for *each* of the two 'x' characters,
    # for a total of O(n^2) time.  Another very well-hidden possible cost.
    for letter in decomp(text):
        sys.stdout.write(letter)
        sys.stdout.write('')

    if __name__ == '__main__':
        decompress(sys.argv[1])
