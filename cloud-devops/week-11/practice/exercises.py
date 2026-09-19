"""Learner-owned small exercises. Contracts and hints: lessons 2, 3, 10."""


def monthly_total(hours, compute_hourly, storage, ipv4_hourly, logs, reserve):
    """Return total cost from six nonnegative numeric inputs; reject negatives with ValueError."""
    raise NotImplementedError("Lesson 2: estimate every category")


def rule_allows(rules, port, source):
    """Exact-match teaching model, NOT an AWS policy engine.
    rules: list of {'port': int, 'source': str}; source is a CIDR label.
    True when same port and either same source or 0.0.0.0/0 is present.
    """
    raise NotImplementedError("Lesson 3: trace each rule")


def failing_requests(events):
    """Return request_id values, in input order, for status >= 500. Empty input returns []."""
    raise NotImplementedError("Lesson 10: select useful evidence")
