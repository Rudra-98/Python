def authenticated_logger(func):
    def decorator(*args, **kwargs):
        # DECORATOR LAYER: Handle authentication & authorization
        print("[DECORATOR] Checking user authentication...")
        user_authenticated = True  # Simulated check

        if not user_authenticated:
            print("[DECORATOR] User not authenticated!")
            return None

        print("[DECORATOR] User authenticated ✓")
        result = func(*args, **kwargs)
        print(f"[DECORATOR] Logging result: {result}")
        return result

    def wrapper(*args, **kwargs):
        # WRAPPER LAYER: Handle performance monitoring
        import time
        print("[WRAPPER] Starting performance timer...")
        start_time = time.time()

        output = decorator(*args, **kwargs)

        end_time = time.time()
        print(f"[WRAPPER] Execution time: {end_time - start_time:.4f} seconds")
        return output

    return wrapper


@authenticated_logger
def fetch_user_data(user_id):
    print(f"[FUNCTION] Fetching data for user {user_id}")
    return {"id": user_id, "name": "Chandu"}


result = fetch_user_data(123)
print(f"\nFinal result: {result}")