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
* Doctests are extremely terse, with little "room" for additional setup. This can help encourage smaller, more atomic, easier to test code.

## Warning!

This code is very experimental. But I tbink the technique is very interesting and has a lot of potential. Much work is needed to make it robust. If you like this idea but hate python - go away and rewrite this in whatever language you desire - but please take the concept further.

See: https://github.com/schwa/SwiftDocTest/issues/1

## Installation

This is a python module so use pip to install. (You should be using virtual environments too. If you know what that means - great)

```shell
    pip install --user git+https://github.com/schwa/SwiftDocTest.git
```

## How to use

Decorate your Swift code with doc comments containing unit tests. Each doc comment must have one or more :test: segments and each :test: must have a corresponding expected :result:. The unit tests are generated so that the test result is compared to your expected result. This means the the output of both segments must conform to the Comparable protocol.

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

Run swiftdoc command line tool. By default it searches all swift files in the specified directory.

```shell
swiftdoc --output UnitTests --import FrameworkNameToImport .
```

Import the generated code into your Unit Test targets.

Yes, the process could do with more automagication.

## CLI Usage

```
Usage: swiftdoc [OPTIONS] INPUT_DIR

  Produce unit test source files from correctly formatted Swift doc comments

Options:
  --output OUTPUT_DIR  Output directory for unit test files.
  --imports IMPORT     Imports to include in every Unit Test file.
  --help               Show this message and exit.
```
