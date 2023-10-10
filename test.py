from main import create_tables, insert_sample_data, complex_sql_query

def test_create_tables():
    print("Running test_create_tables...")
    create_tables()
    print("test_create_tables passed!")

def test_insert_sample_data():
    print("Running test_insert_sample_data...")
    insert_sample_data()
    print("test_insert_sample_data passed!")

def test_complex_sql_query():
    print("Running test_complex_sql_query...")
    results = complex_sql_query()
    for row in results:
        print(row)
    print("test_complex_sql_query passed!")

if __name__ == "__main__":
    try:
        test_create_tables()
        test_insert_sample_data()
        test_complex_sql_query()
        print("All tests passed!")
    except AssertionError as e:
        print(f"Test failed with assertion error: {e}")
    except Exception as e:
        print(f"Test failed with error: {e}")
