def compute_ppl(
    model_type: str,
    model: Dict[str, Any],
    utterances: List[List[str]],
    laplace: bool,
    vocab: set[str]
) -> float:

    log_prob_sum = 0.0
    N = 0

    for utt in utterances:
        utt = map_oov(utt, vocab)
        seq = [START] + utt + [END]

        if model_type == "unigram":
            for w in seq:
                p = p_unigram(w, model)
                if p == 0:
                    return float("inf")
                log_prob_sum += math.log(p)
                N += 1

        elif model_type == "bigram":
            for i in range(len(seq) - 1):
                p = p_bigram(seq[i], seq[i + 1], model, laplace)
                if p == 0:
                    return float("inf")
                log_prob_sum += math.log(p)
                N += 1

        elif model_type == "trigram":
            for i in range(len(seq) - 2):
                p = p_trigram(seq[i], seq[i + 1], seq[i + 2], model, laplace)
                if p == 0:
                    return float("inf")
                log_prob_sum += math.log(p)
                N += 1

    return math.exp(-log_prob_sum / N)