type("Hello") # Can use this in interactive window (IDLE)
string3 = "We're #1!"
string4 = 'I said. "Put it over by the llama."'
# text = "She said, "What time is it?"" # SyntaxError: invalid syntax
# zakomentuj linie kodu = alt + 3
# odkomentuj linie kodu = alt + 4

text = "She said, \"What time is it?\""
print(text)  # She said, "What time is it?"

len(text) # Determine the Length of a String.
# Multiline Strings
# The PEP 8 style guide recommends that each line of Python code
# contain no more than seventy-nine characters—including spaces.

paragraph_using_blackslash_method = "This planet has—or rather had—a problem, which was \
this: most of the people living on it were unhappy for pretty much \
of the time. Many solutions were suggested for this problem, but \
most of these were largely concerned with the movements of small \
green pieces of paper, which is odd because on the whole it wasn't \
the small green pieces of paper that were unhappy."

paragraph_using_triple_quoted = """This planet has—or rather had—a problem, which was
this: most of the people living on it were unhappy for pretty much
of the time. Many solutions were suggested for this problem, but
most of these were largely concerned with the movements of small
green pieces of paper, which is odd because on the whole it wasn't
the small green pieces of paper that were unhappy."""

print(" ")
print("Using triple quoted")
print("""An example of a ...
string that spans across multiple lines ...
and also preserves whitespace.""")

print(" ")
print("Using blackslash method")
print("Przykład ... \
string z  ... \
backslash.")

