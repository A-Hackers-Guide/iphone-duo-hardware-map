# `_UITextViewSearchableObject`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UITextSearching`
- 10 instance variables, 8 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _decoratedTextRanges;
@"NSMutableSet" _decorationAttributes;
@"UITextSearchingDimmingView" _dimmingView;
@"UITextHighlightView" _highlightView;
B _dimmingViewVisible;
B _highlightViewVisible;
@"UIImageView" _highlightContentsImageView;
@"UITextRange" _highlightedTextRange;
@"UITextRange" _visuallyHighlightedTextRange;
@"UITextView" _textView;
```

## Properties

```
@property (T@"UITextView",R,W,N,V_textView) textView;
@property (T@"UITextRange",R) selectedTextRange;
@property (TB,?,R,N) supportsTextReplacement;
@property (T@"<NSObject><NSCopying>",?,R) selectedTextSearchDocument;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextViewSearchableObject selectedTextRange];
-[_UITextViewSearchableObject textView];
-[_UITextViewSearchableObject initWithTextView:];
-[_UITextViewSearchableObject _ensureSubviewOrder];
-[_UITextViewSearchableObject performTextSearchWithQueryString:usingOptions:resultAggregator:];
-[_UITextViewSearchableObject _usesTransientHighlightBehavior];
-[_UITextViewSearchableObject _activeFindSession];
-[_UITextViewSearchableObject _performTextSearchWithQueryString:usingOptions:resultHandler:];
-[_UITextViewSearchableObject _rangeProvider];
-[_UITextViewSearchableObject _setDimmingViewVisible:];
-[_UITextViewSearchableObject _setHighlightViewVisible:];
-[_UITextViewSearchableObject _updateHighlightLabelForMatchedRange:];
-[_UITextViewSearchableObject _wordTerminationCharacteristicsForRange:];
-[_UITextViewSearchableObject clearAllDecoratedFoundText];
-[_UITextViewSearchableObject clearHighlightView];
-[_UITextViewSearchableObject compareFoundRange:toRange:inDocument:];
-[_UITextViewSearchableObject decorateFoundTextRange:inDocument:usingStyle:];
-[_UITextViewSearchableObject didBeginFindSession];
-[_UITextViewSearchableObject didEndFindSession];
-[_UITextViewSearchableObject layoutManagedSubviews];
-[_UITextViewSearchableObject replaceAllOccurrencesOfQueryString:usingOptions:withText:];
-[_UITextViewSearchableObject replaceFoundTextInRange:inDocument:withText:];
-[_UITextViewSearchableObject scrollRangeToVisible:inDocument:];
-[_UITextViewSearchableObject shouldReplaceFoundTextInRange:inDocument:withText:];
-[_UITextViewSearchableObject supportsTextReplacement];
-[_UITextViewSearchableObject targetedPreviewForHighlightRange:];
-[_UITextViewSearchableObject useSelectionForFind];
-[_UITextViewSearchableObject willHighlightFoundTextRange:inDocument:];
```
