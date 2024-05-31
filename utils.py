from models import Movie
from collections import defaultdict

def calculate_intervals():
    winners = Movie.query.filter_by(winner=True).all()
    producer_wins = defaultdict(list)

    for movie in winners:
        producers = [p.strip() for p in movie.producers.split(',')]
        for producer in producers:
            producer_wins[producer].append(movie.year)

    intervals = []
    for producer, years in producer_wins.items():
        if len(years) > 1:
            sorted_years = sorted(years)
            for i in range(len(sorted_years) - 1):
                interval = sorted_years[i + 1] - sorted_years[i]
                intervals.append({
                    "producer": producer,
                    "interval": interval,
                    "previousWin": sorted_years[i],
                    "followingWin": sorted_years[i + 1]
                })

    if not intervals:
        return [], []

    min_interval = min(intervals, key=lambda x: x['interval'])
    max_interval = max(intervals, key=lambda x: x['interval'])

    min_intervals = [interval for interval in intervals if interval['interval'] == min_interval['interval']]
    max_intervals = [interval for interval in intervals if interval['interval'] == max_interval['interval']]

    return min_intervals, max_intervals
