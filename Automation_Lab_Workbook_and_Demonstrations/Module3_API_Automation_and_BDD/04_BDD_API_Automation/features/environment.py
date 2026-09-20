def before_scenario(context, scenario):
    context.response = None
    print(f"\nStarting: {scenario.name}")


def after_scenario(context, scenario):
    print(f"Finished: {scenario.name} - {scenario.status}")