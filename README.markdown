# SwiftDocTest

DocTest for Swift

Generates UnitTests from Swift doc comments

## Installation

Use pip to install

```shell
    pip install git+https://github.com/schwa/SwiftDocTest.git
```

## How to use

Create doc comments for your Swift code like so:

```swift
/**
 :test:   floor(CGPoint(x:10.9, y:-10.5))
 :result: CGPoint(x:10, y:-11)
*/
public func floor(value:CGPoint) -> CGPoint {
    return value.map(floor)
}

/**
 :test:   ceil(CGPoint(x:10.9, y:-10.5))
 :result: CGPoint(x:11, y:-10)
*/
public func ceil(value:CGPoint) -> CGPoint {
    return value.map(ceil)
}
```

Run swiftdoc command line tool

```shell
swiftdoc --output UnitTests --import FrameworkNameToImport .
```

## CLI Usage

```
Usage: swiftdoc [OPTIONS] INPUT_DIR

  Produce unit test source files from correctly formatted Swift doc comments

Options:
  --output OUTPUT_DIR  Output directory for unit test files.
  --imports IMPORT     Imports to include in every Unit Test file.
  --help               Show this message and exit.
```