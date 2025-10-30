"""
CP1404 Practical
Wimbledon data handler
Estimated: 45 mins
Actual:
"""

FILE_NAME = "wimbledon.csv"


def main():
    """Display wimbledon championship data from a csv"""
    wimbledon_results = read_csv(FILE_NAME)
    champion_to_wins = count_champion_wins(wimbledon_results)
    winning_countries = find_winning_countries(wimbledon_results)

    print("Wimbledon Champions:")
    max_name_length = max(len(champion) for champion in champion_to_wins)
    for champion, wins in champion_to_wins.items():
        print(f"{champion:<{max_name_length}} {wins}")

    print(f"\nThese {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(winning_countries))


def read_csv(file_name, skip_header=True):
    """Read csv file and returns a list of lists of each row and column."""
    with open(file_name, "r", encoding="utf-8-sig") as in_file:
        if skip_header:
            in_file.readline()
        return [line.split(",") for line in in_file.read().split("\n")]


def count_champion_wins(wimbledon_results: list):
    """Calculate number of wins per champion from a list structured
    like [[Year, Country, Champion, Country, Runner-up, Score], [...]]."""
    champion_to_wins = {}
    for match in wimbledon_results:
        champion = match[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def find_winning_countries(wimbledon_results: list):
    """Find the set of countries that have won a championship."""
    winning_countries = set()
    for match in wimbledon_results:
        winning_countries.add(match[1])
    return sorted(winning_countries)


main()
