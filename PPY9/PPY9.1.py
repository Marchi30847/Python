import inspect
from functools import wraps


# Task1
def call_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"{func.__name__} was called {wrapper.call_count} times")
        return func()

    wrapper.call_count = 0
    return wrapper


@call_counter
def foo():
    print("foo")


@call_counter
def bar():
    print("bar")


for i in range(10):
    foo()
    bar()


# Task2
def validate_args(**validators):
    def decorator(func):
        sig = inspect.signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()

            for name, validator in validators.items():
                if name in bound.arguments:
                    value = bound.arguments[name]
                    if not validator(value):
                        raise ValueError(f"Invalid value for '{name}': {value!r}")
                else:
                    raise ValueError(f"No argument '{name}' to validate")

            return func(*args, **kwargs)

        return wrapper

    return decorator


@validate_args(age=lambda age: age >= 18, email=lambda email: "@" in email)
def register_user(name, age, email):
    print(f"Registering {name} with {age} years old and {email}")


register_user(name="John", age=20, email="<EMAIL@>")


# Task3
def memorise(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        wrapper.storage.append(res)
        print(f"Results for {func.__name__}: {wrapper.storage}")
        return res

    wrapper.storage = []
    return wrapper


@memorise
def add(a, b):
    return a + b


add(1, 2)
add(6, 4)
add(-1, 3)

# Task4
import json, yaml, toml


def convert(from_format, to_format):
    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            raw = func(*args, **kwargs)

            match from_format:
                case "json":
                    data = raw
                case "yaml":
                    data = yaml.safe_load(raw)
                case "toml":
                    data = toml.loads(raw)
                case _:
                    raise ValueError(f"Unsupported input format: {from_format}")

            match to_format:
                case "json":
                    return json.dumps(data, indent=4)
                case "yaml":
                    return yaml.dump(data, sort_keys=False)
                case "toml":
                    return toml.dumps(data)
                case _:
                    raise ValueError(f"Unsupported output format: {to_format}")

        return wrapper

    return decorator


@convert("json", "yaml")
def produces_json():
    return {
        "name": "Alice",
        "age": 30,
        "is_active": True
    }


@convert("yaml", "toml")
def produces_yaml():
    return (
        "name: Bob\n"
        "age: 25\n"
        "skills:\n"
        "  - Python\n"
        "  - YAML\n"
    )


@convert("toml", "json")
def produces_toml():
    return (
        "name = 'Charlie'\n"
        "age = 40\n"
        "active = true\n"
    )


print("JSON → YAML:")
print(produces_json())

print("\nYAML → TOML:")
print(produces_yaml())

print("\nTOML → JSON:")
print(produces_toml())
