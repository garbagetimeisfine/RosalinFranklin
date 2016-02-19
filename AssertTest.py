import scipy
import scipy.special

def compute_likelihood_binomial(p, successes, trials):
    assert p >= 0, "Negative Probability"
    assert p <= 1, "probability > 1!"
    assert successes <= trials, "More Sucesses than trials!"
    
    log_likelihood = successes * scipy.log(p) + (trials - successes) * scipy.log(1.0 - p)
    return scipy.exp(log_likelihood) * scipy.special.binom(trials, successes)
    