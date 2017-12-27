def differentTeams(skills):
    skills_to_freq = {}

    for skill in skills:
        skills_to_freq[skill] = 1 + skills_to_freq.get(skill, 0)

    for skill in "pcmbz":
        if skill not in skills_to_freq:
            return 0

    return min(skills_to_freq.values())


print(differentTeams("pcmpcmbbbzz"))
