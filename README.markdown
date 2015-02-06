# SwiftDocTest

DocTest for Swift

Generates UnitTests from Swift doc comments.

Very much inspired by [Python's doctest module](https://docs.python.org/2/library/doctest.html)

See [NSHipster](http://nshipster.com/swift-documentation/) for information on Swift's doc-comment format

## Why?

Writing python doctests is extremely easy and incredibly fast. I wondered if I could bring something similar to swift.

The advantages of doctests are:

* Unit tests are right next to the code being tested. (This can help obviate the need for code coverage - which is good because swift has no code coverage tools yet).
* Unit tests double as examples of how to use the API.
* Doctests are extremely terse, with "room" for additional setup. This can help encourage smaller, more-atomic, easier to test code.

## Warning!

This code is super experimental. But I tbink the technique is very interesting and has a lot of potential. 

See: https://github.com/schwa/SwiftDocTest/issues/1

## Installation

This is a python module so use pip to install. (You should be using virtual environments too. But if you don't know what that means just use sudo pip below).

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

Import the generated code into your Unit Test targets.

## CLI Usage

```
Usage: swiftdoc [OPTIONS] INPUT_DIR

  Produce unit test source files from correctly formatted Swift doc comments

Options:
  --output OUTPUT_DIR  Output directory for unit test files.
  --imports IMPORT     Imports to include in every Unit Test file.
  --help               Show this message and exit.
```
