# `UITextSearching` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 13 instance methods, 0 class methods

## Properties

```
@property (T@"UITextRange",R) selectedTextRange;
@property (TB,?,R,N) supportsTextReplacement;
@property (T@"<NSObject><NSCopying>",?,R) selectedTextSearchDocument;
```

## Instance methods

```
-[UITextSearching selectedTextRange];
-[UITextSearching performTextSearchWithQueryString:usingOptions:resultAggregator:];
-[UITextSearching clearAllDecoratedFoundText];
-[UITextSearching compareFoundRange:toRange:inDocument:];
-[UITextSearching decorateFoundTextRange:inDocument:usingStyle:];
-[UITextSearching compareOrderFromDocument:toDocument:];
-[UITextSearching replaceAllOccurrencesOfQueryString:usingOptions:withText:];
-[UITextSearching replaceFoundTextInRange:inDocument:withText:];
-[UITextSearching scrollRangeToVisible:inDocument:];
-[UITextSearching selectedTextSearchDocument];
-[UITextSearching shouldReplaceFoundTextInRange:inDocument:withText:];
-[UITextSearching supportsTextReplacement];
-[UITextSearching willHighlightFoundTextRange:inDocument:];
```
