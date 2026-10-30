# `UITextSearchingFindSession`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIFindSession`
- 18 instance variables, 3 properties, 42 instance methods, 0 class methods

## Instance variables

```
B _isSearching;
B _awaitingFirstResults;
B _readyToPerformDelayedSearchOperations;
B _needsResultCountUpdate;
@"UITextRange" _highlightedTextRange;
@"<NSObject><NSCopying>" _highlightedDocument;
@"NSMutableOrderedSet" _sortedDocumentIdentifiers;
@"NSMutableDictionary" _sortedResultsByDocument;
@"NSMutableArray" _blocksAwaitingSearchResults;
@"NSString" _lastSearchQuery;
@"UITextSearchOptions" _lastSearchOptions;
@"_UITextSearchingFindSessionAggregator" _aggregator;
@"UITextRange" _highlightedRangeBeforeSubsequentSearch;
@"<NSObject><NSCopying>" _highlightedDocumentBeforeSubsequentSearch;
{?="supportsTextReplacement"b1"shouldReplaceFoundTextInRange"b1"replaceFoundTextInRange"b1"replaceAllOccurrencesOfQueryString"b1"willHighlightFoundTextRange"b1"scrollRangeToVisible"b1"shouldBeginTextSearchOperation"b1"didBeginTextSearchOperation"b1"didEndTextSearchOperation"b1"searchResultDisplayStyle"b1"selectedTextSearchDocument"b1"compareOrderFromDocument"b1"compareFoundRangeToRange"b1} _searchableObjectConformsTo;
@"UIFindInteraction" _parentInteraction;
@"<UITextSearching>" _searchableObject;
@"<UITextSearching>" _stronglyHeldSearchableObject;
```

## Properties

```
@property (TB,R,N,GisSearching,V_isSearching) searching;
@property (T@"<UITextSearching>",W,N,V_searchableObject) searchableObject;
@property (T@"<UITextSearching>",&,N,V_stronglyHeldSearchableObject) stronglyHeldSearchableObject;
```

## Instance methods

```
-[UITextSearchingFindSession searchableObject];
-[UITextSearchingFindSession reset];
-[UITextSearchingFindSession resultCount];
-[UITextSearchingFindSession isSearching];
-[UITextSearchingFindSession setSearchableObject:];
-[UITextSearchingFindSession replaceAllInstancesOfSearchQuery:withReplacementString:options:];
-[UITextSearchingFindSession _allFoundRanges];
-[UITextSearchingFindSession _performDelayedSearchOperations];
-[UITextSearchingFindSession highlightNextResultInDirection:];
-[UITextSearchingFindSession performSearchWithQuery:options:];
-[UITextSearchingFindSession _documentComparator];
-[UITextSearchingFindSession _finishedSearching];
-[UITextSearchingFindSession _foundRange:forSearchString:inDocument:];
-[UITextSearchingFindSession _hasResults];
-[UITextSearchingFindSession _invalidateAllFoundRanges];
-[UITextSearchingFindSession _invalidateFoundRange:inDocument:];
-[UITextSearchingFindSession _isCurrentSearchQueryValid];
-[UITextSearchingFindSession _nearestRangeToSelectedRangeInDocument:];
-[UITextSearchingFindSession _nextItemInOrderedSet:usingComparator:fromItem:inDirection:loopAround:];
-[UITextSearchingFindSession _nextResultRelativeToRange:document:inDirection:];
-[UITextSearchingFindSession _performBlockWhenSearchResultsAreAvailable:];
-[UITextSearchingFindSession _readilyHighlightNearestRangeToSelectedRangeIfNecessary];
-[UITextSearchingFindSession _readilyHighlightNextResultInDirection:];
-[UITextSearchingFindSession _replaceHighlightedTextRangeWithReplacementString:];
-[UITextSearchingFindSession _setHighlightedRange:inDocument:];
-[UITextSearchingFindSession _setNeedsResultCountUpdate];
-[UITextSearchingFindSession _setReadyToPerformDelayedSearchOperations];
-[UITextSearchingFindSession _textRangeComparatorForDocument:];
-[UITextSearchingFindSession _updateResultCountLabel];
-[UITextSearchingFindSession _updateSearchableObjectProtocolConformance];
-[UITextSearchingFindSession allowsReplacementForCurrentlyHighlightedResult];
-[UITextSearchingFindSession highlightNearestFoundRangeToSelectedRangeIfNecessary];
-[UITextSearchingFindSession highlightedResultIndex];
-[UITextSearchingFindSession initWithSearchableObject:];
-[UITextSearchingFindSession initWithStronglyHeldSearchableObject:];
-[UITextSearchingFindSession invalidateFoundResults];
-[UITextSearchingFindSession parentInteraction];
-[UITextSearchingFindSession performSingleReplacementWithSearchQuery:replacementString:options:];
-[UITextSearchingFindSession setParentInteraction:];
-[UITextSearchingFindSession setStronglyHeldSearchableObject:];
-[UITextSearchingFindSession stronglyHeldSearchableObject];
-[UITextSearchingFindSession supportsReplacement];
```
