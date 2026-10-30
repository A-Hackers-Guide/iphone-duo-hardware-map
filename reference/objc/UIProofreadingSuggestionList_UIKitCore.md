# `UIProofreadingSuggestionList`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 3 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _ranges;
@"NSMutableArray" _suggestions;
@"NSMutableArray" _states;
@"NSMutableArray" _grammarStrings;
@"NSMutableArray" _details;
@"NSMutableArray" _textAlternatives;
```

## Properties

```
@property (TQ,R,N) numberOfSuggestions;
@property (T@"NSArray",R,C,N) pendingSuggestions;
@property (T@"NSString",R,C,N) detailedDescription;
```

## Instance methods

```
-[UIProofreadingSuggestionList init];
-[UIProofreadingSuggestionList rangeAtIndex:];
-[UIProofreadingSuggestionList numberOfSuggestions];
-[UIProofreadingSuggestionList detailedDescription];
-[UIProofreadingSuggestionList addSuggestion:detail:textAlternatives:];
-[UIProofreadingSuggestionList addSuggestionsForString:textChecker:];
-[UIProofreadingSuggestionList adjustRangesForReplacementOfRange:changeInLength:];
-[UIProofreadingSuggestionList detailAtIndex:];
-[UIProofreadingSuggestionList grammarStringAtIndex:];
-[UIProofreadingSuggestionList indexForUUID:];
-[UIProofreadingSuggestionList indexesForUUIDs:];
-[UIProofreadingSuggestionList pendingSuggestions];
-[UIProofreadingSuggestionList suggestionAtIndex:];
-[UIProofreadingSuggestionList suggestionStateAtIndex:];
-[UIProofreadingSuggestionList textAlternativesAtIndex:];
-[UIProofreadingSuggestionList textRangeAtIndex:forClient:];
-[UIProofreadingSuggestionList updateSuggestionState:atIndex:];
```
