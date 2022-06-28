from brownie import accounts, config, SimpleStorage


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == expected


def test_updating_storage():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    simple_storage.store(42, {"from": account})
    updated_value = simple_storage.retrieve()
    expected = 42
    print(updated_value)
    # Assert
    assert updated_value == expected
