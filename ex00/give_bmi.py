def give_bmi(height: list[int | float], weight: list[int | float]
             ) -> list[int | float]:
    try:
        bmi = [w / (h ** 2) for h, w in zip(height, weight)]
        return bmi
    except Exception:
        print("Please verify your arguments")


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    try:
        result = [b > limit for b in bmi]
        return result
    except Exception:
        print("Please verify your arguments")
