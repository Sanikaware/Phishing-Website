import pickle

def main():
    with open("ml_model.pkl", "rb") as f:
        model = pickle.load(f)

    print("Model type:", type(model))
    # Try to print model parameters if available
    if hasattr(model, "get_params"):
        print("Model parameters:", model.get_params())
    # Try to print training score if available (requires test data, so just check if method exists)
    if hasattr(model, "score"):
        print("Model has 'score' method, but no test data provided to evaluate accuracy.")
    else:
        print("Model does not have 'score' method.")

if __name__ == "__main__":
    main()
