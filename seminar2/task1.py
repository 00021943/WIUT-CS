def calculate_total_marks():
    # Get the number of components
    num_components = int(input("Input number of components: "))

    total_weight = 0

    for i in range(1, num_components + 1):
        # Get the component name
        component_name = input(f"Input component {i} name: ")

        # Get the component weighting
        component_weight = int(input(f"Input component {i} weighting (%): "))

        # Add the component weight to the total
        total_weight += component_weight

    # Output the total
    print(f"Total: {total_weight}%")


# Run the function
calculate_total_marks()
