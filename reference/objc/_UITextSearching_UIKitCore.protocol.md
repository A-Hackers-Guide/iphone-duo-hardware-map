# `_UITextSearching` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 18 instance methods, 0 class methods

## Properties

```
@property (T@"UITextRange",R) selectedTextRange;
@property (T@"<NSCoding><NSCopying>",?,R) selectedTextSearchDocument;
```

## Instance methods

```
-[_UITextSearching selectedTextRange];
-[_UITextSearching performTextSearchWithQueryString:usingOptions:resultAggregator:];
-[_UITextSearching clearAllDecoratedFoundText];
-[_UITextSearching compareFoundRange:toRange:inDocument:];
-[_UITextSearching decorateFoundTextRange:inDocument:usingStyle:];
-[_UITextSearching compareOrderFromDocument:toDocument:];
-[_UITextSearching didBeginTextSearchOperation];
-[_UITextSearching didEndTextSearchOperation];
-[_UITextSearching offsetFromPosition:toPosition:inDocument:];
-[_UITextSearching replaceAllOccurrencesOfQueryString:usingOptions:withText:];
-[_UITextSearching replaceFoundTextInRange:inDocument:withText:];
-[_UITextSearching scrollRangeToVisible:inDocument:];
-[_UITextSearching searchResultDisplayStyle];
-[_UITextSearching selectedTextSearchDocument];
-[_UITextSearching shouldBeginTextSearchOperation];
-[_UITextSearching shouldReplaceFoundTextInRange:inDocument:withText:];
-[_UITextSearching supportsTextReplacement];
-[_UITextSearching willHighlightFoundTextRange:inDocument:];
```
