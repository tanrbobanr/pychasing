# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.1.7] - 2023-06-03

### Added

- Added a (somewhat hacky) hotfix for Ballchasing's somewhat broken continuation token system.
- Added this changelog.

### Changed

- Updated `pyproject.toml` to include more information (and in a better visual format).
- Updated `LICENSE` to include the current year.

### Fixed

- Fixed the `.xbl` and `.psn` enums to correspond to the correct values (`xbox` and `ps4` respectively).

### Removed

- Removed the use of the `prepr` module, as it was essentially unused throughout the entire module.

## [0.1.8] - 2023-06-04

### Changed

- `Client.__init__` no longer requires the `auto_rate_limit` and `patreon_tier` arguments to be instantiated (defaults are `True` and `PatreonTier.none` respectively).
- `patreon_tier` in `Client.__init__` now allows for strings to be used in addition to the dedicated enum.
