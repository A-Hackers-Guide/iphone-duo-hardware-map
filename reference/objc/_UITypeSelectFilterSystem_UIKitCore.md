# `_UITypeSelectFilterSystem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
q _userInputLength;
@"NSArray" _words;
@"NSString" _lastCharacterFromUserInput;
@"NSString" _typeSelectString;
Q _mask;
@"NSMutableString" _acronym;
@"NSMutableArray" _wordsWithoutPunc;
@"NSMutableIndexSet" _matchingRanges;
@"NSString" _inputString;
```

## Properties

```
@property (T@"NSString",&,N,V_inputString) inputString;
```

## Instance methods

```
-[_UITypeSelectFilterSystem _isValidMatchingRangeForString:];
-[_UITypeSelectFilterSystem filterResultForTypeSelectItem:];
-[_UITypeSelectFilterSystem _stringWithoutPunctuation:];
-[_UITypeSelectFilterSystem setInputString:];
-[_UITypeSelectFilterSystem _lengthForWithoutPunctuationMatch:];
-[_UITypeSelectFilterSystem _matchingRangeWithLocation:length:];
-[_UITypeSelectFilterSystem _acronymMatching];
-[_UITypeSelectFilterSystem inputString];
```
