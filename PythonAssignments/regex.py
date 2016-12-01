import re

def get_matching_words(regex):
    words = ["/users/darril/description", "a", "abc", "/users/238", "base", "aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

    return [word for word in words if re.search(regex, word)]

if get_matching_words("baby"):
    print "match"
    print get_matching_words("baby")
else:
    print "no match"

print "Words containing v: " + str(get_matching_words("v"))
print "Words containing ss: " + str(get_matching_words("ss"))
print "Words ending with an e: " + str(get_matching_words("e$"))
print "Words that contain a 'b', any character(s), then another 'b': " + str(get_matching_words("b*b"))
print "Words that contain a 'b', any single character, then another 'b': " + str(get_matching_words("b.b"))
print "Words that contain a 'b', any characters (including zero), then another 'b': " + str(get_matching_words("b*b"))

print "All words that include users" + str(get_matching_words("/(users)\/[0-9]"))
print "All words that include users/darril" + str(get_matching_words("/(users)\/[a-z]*\/[A-Z]*"))

# print "All words that include all five vowels in order: " + str(get_matching_words("aeiou"))

# All words that contain a double letter
# This expression returns all words with at least two letters:
#  print get_matching_words("(\w){2}")
# This expression works on regexr and pythex to identify words that have at least two matching letters:
#  (\w){2}(\1)
# I expected this to work in python, but it returns an empty set
#  print get_matching_words("(\w){2}(\1)")

# Seems to return everything with two or more letters (didn't return "a")
# print get_matching_words("(\w){2}")

# Returns nothing
# print get_matching_words("(\w){2}(\1)")

# if get_matching_words("(\w){2,}(\1)"):
#     print "match"
# else:
#     print "no match"

# Returns nothing
# print get_matching_words("(\w){2}(\1)")

# Returns nothing
# print get_matching_words("(\w){2,}(\1)")

# Returns nothing
# print get_matching_words("(\w){2,}(\2)")

# Returns nothing
# print get_matching_words("(\w)\2{2,}")

# print get_matching_words("(\w){2}(\1)")
# print get_matching_words("(\w){2,}(\2)")

# All words that only use the letters in 'regular expression' (each letter can appear any number of times)
