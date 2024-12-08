def give_bmi(height: list[int | float], weight: list[int | float]
             ) -> list[int | float]:
    """
Return the bmi of a person
    """
    try:
        bmi = [w / (h ** 2) for h, w in zip(height, weight)]
        return bmi
    except Exception:
        print("Please verify your arguments")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
Is used to limit the array
    """
    try:
        result = [b > limit for b in bmi]
        return result
    except Exception:
        print("Please verify your arguments")
