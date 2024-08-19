class Queries:
    CREATE_REVIEW_RESULTS_TABLE = """
    CREATE TABLE IF NOT EXISTS restauran_review(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    instagram_username TEXT,
    visit_date DATE,
    food_rating INTEGER,
    cleanliness_rating INTEGER,
    extra_comments TEXT
    )
    """


    INSERT_INTO_RESTAURANT_REVIEW = """
    insert into restauran_review  values(?, ?, ?, ?, ?, ?, ?)
    
    
    """