"""Learner-owned dependencies: service lookup and API-key role check.

Read X-API-Key with APIKeyHeader(auto_error=False). Missing/wrong -> 401 with
WWW-Authenticate: APIKey. Local read key may GET but must receive 403 on writes.
Read dummy key settings once per app creation, never print them. Use
request.app.state.service to obtain this app's service; avoid a global store.
"""
# TODO: implement and wire dependencies after lesson 9.
