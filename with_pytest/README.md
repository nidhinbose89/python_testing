# Add pytest.ini
> with the pythonpath so that imports within tests work

# Run from root folder `with_pytest`
>> pytest -k map  # will get all tests with name `map` - k is key!
##### use `breakpoint()` to debug!

# To get coverage with pytest for `scripts` folder
>>> pytest --cov scripts