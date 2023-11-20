def soundex(name):
    """
    The Soundex algorithm assigns a 1-letter + 3-digit code to strings,
    with the intention that strings pronounced the same but spelled
    differently have identical encodings; words pronounced similarly
    should have similar encodings.
    """
    soundex_coding = [' ', ' ', ' ', ' ']
    soundex_coding_index = 1

    # Mapping of letters to Soundex digits
    mappings = "01230120022455012623010202"

    soundex_coding[0] = name[0].upper()

    for i in range(1, len(name)):
        char_code = ord(name[i].upper()) - 65

        if 0 <= char_code <= 25:
            if mappings[char_code] != '0':
                if mappings[char_code] != soundex_coding[soundex_coding_index - 1]:
                    soundex_coding[soundex_coding_index] = mappings[char_code]
                    soundex_coding_index += 1

                    if soundex_coding_index > 3:
                        break

    if soundex_coding_index <= 3:
        while soundex_coding_index <= 3:
            soundex_coding[soundex_coding_index] = '0'
            soundex_coding_index += 1

    return ''.join(soundex_coding)


def main():
   

    names1 = ["Johnson", "Adams", "Davis", "Simons", "Richards", "Taylor", "Carter", "Stevenson",
              "Taylor", "Smith", "McDonald", "Harris", "Sim", "Williams", "Baker", "Wells", "Fraser", "Jones",
              "Wilks", "Hunt", "Sanders", "Parsons", "Robson", "Harker"]

    names2 = ["Jonson", "Addams", "Davies", "Simmons", "Richardson", "Tailor", "Chater",
              "Stephenson", "Naylor", "Smythe", "MacDonald", "Harrys", "Sym", "Wilson", "Barker", "Wills",
              "Frazer", "Johns", "Wilkinson", "Hunter", "Saunders", "Pearson", "Robertson", "Parker"]

    for i in range(len(names1)):
        s1 = soundex(names1[i])
        s2 = soundex(names2[i])
        print("{:20s}{:4s} {:20s}{:4s}".format(names1[i], s1, names2[i], s2))


if __name__ == "__main__":
    main()
