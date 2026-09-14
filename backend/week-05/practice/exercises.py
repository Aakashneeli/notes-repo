"""Learner SQL strings. Keep functions and return a parameterized SQL query.
The runner binds values separately: use :published, never string formatting.
"""
def published_page():
    """Return id,title for published=:published, ascending id, limit 2."""
    raise NotImplementedError("Lesson 3")

def author_counts():
    """Return name,n for ALL authors, including zero; ascending author id."""
    raise NotImplementedError("Lesson 5")
