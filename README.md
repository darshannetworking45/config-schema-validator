# Network Device Variables Validator

Validates structured device-variable dictionaries and reports missing or invalid fields before they are used by automation.

## Main entry points

- `src.validator.SchemaValidationError`
- `src.validator.NetworkSchemaValidator` (`validate_device_vars`)

## Run the tests

```bash
python -m unittest discover -s tests -v
```

The project uses the Python standard library; no third-party package is required.

## Scope

This is a project-specific data validator, not a general JSON Schema implementation. Check the accepted fields in `NetworkSchemaValidator.validate_device_vars`.
