from collections import defaultdict
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # Create a set to store the invalid transactions.
        invalids = set()

        # Create a dictionary to group transactions by name for easy access.
        # The dictionary will map names to a set of tuples, each containing the time and city of a transaction.
        transactionDict = defaultdict(set)

        # First pass: Collect all transactions, grouped by name.
        for transaction in transactions:
            # Split the transaction string into its components.
            name, time, amount, city = transaction.split(',')
            # Convert time to an integer for comparison.
            time = int(time)
            # Add the time and city of the current transaction to the set for this name.
            transactionDict[name].add((time, city))
        
        # Second pass: Check each transaction against the criteria for being invalid.
        for transaction in transactions:
            # Split the transaction string into its components again.
            name, time, amount, city = transaction.split(',')
            # Convert time and amount to integers for comparison.
            time, amount = int(time), int(amount)

            # If the transaction amount is greater than $1000, it's invalid.
            if amount > 1000:
                invalids.add(transaction)
            # If not, we need to check the time and city against other transactions.
            else:
                # Compare with other transactions of the same name.
                for other_time, other_city in transactionDict[name]:
                    # Check if the transaction occurs within 60 minutes of another transaction with the same name in a different city.
                    if abs(time - other_time) <= 60 and city != other_city:
                        # If so, it's invalid.
                        invalids.add(transaction)
                        # Once an invalid transaction is found, no need to check more.
                        break

        # Return the list of invalid transactions by filtering from the original list.
        return [t for t in transactions if t in invalids]