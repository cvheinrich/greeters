# Greeters project

Before running the code, make sure you have the package manager pixi installed. You can install it using the following command:

## Install pixi:

Mac & Linux:

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

Windows:

```bash
powershell -ExecutionPolicy ByPass -c "irm -useb https://pixi.sh/install.ps1 | iex"
```

## Run code:

The code can be run using the following command:

```bash
pixi run start
```

## Add guides and tourists:

For each guide and tourist, you can add their text as a txt file in the `guides` and `tourists` folders respectively. The text files should be named after the guide or tourist's name. The text should be in plain text format and should not contain any special characters or formatting.

## Add conda dependency:

```bash
pixi add <package_name>
```

## Add pypi dependency:

```bash
pixi add --pypi <package_name>
```

## Add dependency group:

```bash
pixi add <package_name> --feature <group_name>
```

## Format code:

```bash
pixi run clean
```
