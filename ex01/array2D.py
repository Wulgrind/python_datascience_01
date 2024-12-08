def slice_me(family: list, start: int, end: int) -> list:
    try:
        if not isinstance(family, list) or not all(
                isinstance(row, list) for row in family):
            raise Exception(
                "Provide correct args, first one should be a list of list.")
        val = len(family[0])
        for row in family:
            if len(row) is not val:
                raise Exception("All list indexes must have the same length.")
        endSize = end - start
        if endSize <= 0:
            endSize = 1
        print(f"My shape is : ({len(family)}, {len(family[0])})")
        print(f"My new shape is : ({endSize}, {len(family[0])})")

        return family[start:end]
    except Exception as e:
        print(f"Error : {e}")
