from math import log10, floor, ceil


def safe_divide(numerator, denominator):
    if denominator == 0:
        return float("inf") if numerator >= 0 else float("-inf")
    return numerator / denominator


def to_str(num, digits=8):
    if num == 0:
        return f"{0:.{digits}f}"
    if num == float("inf"):
        return "inf"
    if num == float("-inf"):
        return "-inf"
    exp = ceil(log10(abs(num)))
    scaled = num / (10**exp)
    truncated = round(scaled, digits)
    num = truncated * (10**exp)
    return f"{round(num, digits)}"
