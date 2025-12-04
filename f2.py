print("nathan was here")
def count_ngrams(
    utterances: List[List[str]]
) -> Tuple[
    Counter[str],
    Counter[Tuple[str, str]],
    Counter[Tuple[str, str, str]]
]:
    uni: Counter[str] = Counter()
    bi: Counter[Tuple[str, str]] = Counter()
    tri: Counter[Tuple[str, str, str]] = Counter()

    for utt in utterances:
        seq = [START] + utt + [END]

        uni.update(seq)

        for i in range(len(seq) - 1):
            bi[(seq[i], seq[i + 1])] += 1

        for i in range(len(seq) - 2):
            tri[(seq[i], seq[i + 1], seq[i + 2])] += 1

    return uni, bi, tri