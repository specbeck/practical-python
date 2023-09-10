class Stock:
    """A Stock holding instance having attributes name, shares and price."""

    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        """Cost of a stock as shares * price"""
        return self.shares * self.price

    def sell(self, nshares):
        """Sell a specified number of shares"""
        self.shares -= nshares
