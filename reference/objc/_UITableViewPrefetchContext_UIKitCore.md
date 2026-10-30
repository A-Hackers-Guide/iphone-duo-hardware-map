# `_UITableViewPrefetchContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
B _prefetchScheduled;
@? _requestHandler;
@? _cancelHandler;
@? _cellHandler;
@? _cellPruningHandler;
@"NSMutableIndexSet" _outstandingRequests;
q _maxIndex;
d _lastContentOffset;
q _prefetchItemCount;
q _refreshPrefetchThresholdCount;
q _cancelThresholdCount;
{_NSRange="location"Q"length"Q} _lastVisibleIndexRange;
```

## Instance methods

```
-[_UITableViewPrefetchContext description];
-[_UITableViewPrefetchContext _effectiveRefreshDirectionForProposedVisibleIndexRange:withContentOffset:];
-[_UITableViewPrefetchContext _offsetAndValidateRange:firstIndexOffset:lastIndexOffset:];
-[_UITableViewPrefetchContext _validatedRangeWithLocation:length:];
-[_UITableViewPrefetchContext computedPrefetchIndexSet];
```
