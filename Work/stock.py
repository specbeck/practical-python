from typedproperty import String, Integer, Float

class Stock:
    """A Stock holding instance having attributes name, shares and price."""

    name = String('name')
    shares = Integer('shares')
    price = Float('price')

    # __slots__ = ('name', '_shares', 'price')
    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock({self.name!r}, {self.shares!r}, {self.price!r})"


    @property
    def cost(self):
        """Cost of a stock as shares * price"""
        return self.shares * self.price

    def sell(self, nshares):
        """Sell a specified number of shares"""
        self.shares -= nshares
