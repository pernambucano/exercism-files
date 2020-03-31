def latest(scores):
    return scores[-1]


def personal_best(scores):
    max_score = 0
    for i in scores:
        if i > max_score:
            max_score = i
    return max_score


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[:3]
