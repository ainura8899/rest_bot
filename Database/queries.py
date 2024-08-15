class Queries:
    CREATE_REVIEW_RESULTS_TABLE = """
    CREATE IF NOT EXISTS TABLE restauran_review(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name = State()
    instagram_username = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()
    )
    """