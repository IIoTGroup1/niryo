"""
...
"""


def valid_ip(ip_address: str) -> bool:
  """
  Makes a crude attempt at validating the given IP address.
  """
  dots = 0
  for char in ip_address:
    if char == '.':
      dots += 1
  return True if dots==3 else False
