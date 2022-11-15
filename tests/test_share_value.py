from brownie import Contract, accounts, chain, ShareValueHelper
import pytest

def test_helper(helper):
    vault = Contract('0xa354F35829Ae975e850e23e9615b11Da1B3dC4DE')
    decimals = vault.decimals()
    amount = 1_000_000 * 10 ** decimals
    
    # Convert to shares
    shares_precise = helper.amountToShares(vault, amount)
    shares_imprecise = amount * 10**decimals // vault.pricePerShare()
    print(f'\n-- Converting {amount} tokens to shares --')
    print(f'Precise: {shares_precise}')
    print(f'Imprecise: {shares_imprecise}')

    # Convert to amount
    amount_precise = helper.sharesToAmount(vault, amount)
    amount_imprecise = vault.pricePerShare() * amount // 10**decimals
    print(f'\n-- Converting {amount} shares to underlying amount --')
    print(f'Precise: {amount_precise}')
    print(f'Imprecise: {amount_imprecise}')