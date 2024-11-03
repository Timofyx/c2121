class BuildingError(Exception):
    def __str__(self):
        return f"With so much material the house cannot be build!"


def check_material(amount_of_material, limit_material):
    if amount_of_material > limit_material:
        return "enough material"
    else:
        raise BuildingError(amount_of_material)


material = 1123
check_material(material, 300)
print(rfd)