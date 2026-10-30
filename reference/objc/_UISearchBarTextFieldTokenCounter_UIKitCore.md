# `_UISearchBarTextFieldTokenCounter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
@ _textStorageObservation;
@"NSTextStorage" _textStorage;
@"NSMutableIndexSet" _tokenCharacterIndexes;
```

## Properties

```
@property (T@"NSIndexSet",R,N) tokenCharacterIndexes;
@property (T{_NSRange=QQ},R,N) characterRangeOfAllTokens;
```

## Instance methods

```
-[_UISearchBarTextFieldTokenCounter indexOfTokenAtCharacterIndex:];
-[_UISearchBarTextFieldTokenCounter initWithTextStorage:];
-[_UISearchBarTextFieldTokenCounter _addCharacterIndexesOfTokensInRange:toIndexSet:];
-[_UISearchBarTextFieldTokenCounter characterIndexForSelectingOrRemovingTokenAtIndex:];
-[_UISearchBarTextFieldTokenCounter _handleProcessEditing];
-[_UISearchBarTextFieldTokenCounter characterRangeOfTextAfterLastToken];
-[_UISearchBarTextFieldTokenCounter tokenCharacterIndexes];
-[_UISearchBarTextFieldTokenCounter characterIndexForInsertingTokenAtIndex:];
-[_UISearchBarTextFieldTokenCounter characterRangeForSubrangeOfTextAfterLastToken:];
-[_UISearchBarTextFieldTokenCounter subrangeOfTextAfterLastTokenForCharacterRange:];
-[_UISearchBarTextFieldTokenCounter tokenAtCharacterIndex:];
-[_UISearchBarTextFieldTokenCounter characterRangeOfAllTokens];
```
