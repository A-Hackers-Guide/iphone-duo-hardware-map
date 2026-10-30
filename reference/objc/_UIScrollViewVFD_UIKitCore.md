# `_UIScrollViewVFD`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIUpdateCompletionObserving`
- 10 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"UIScrollView" _scrollView;
@"_UIScrollViewFPSHUD" _debugOverlay;
I _activeSubreasons;
{_UIUpdateRequest="flags"I"minRate"I"preferredRate"I"maxRate"I"phase"Q"load"Q} _updateRequest;
{_UIUpdateRequestRecord="request"^{_UIUpdateRequest}"reason"I} _updateRecord;
{_UIScrollViewVFDLookupState="staticRateRangePrevious"^{CAFrameRateRange}"staticRateRangeCurrent"^{CAFrameRateRange}"staticRateRangeFramesPrevious"S"staticRateRangeFramesCurrent"S} _lookupState;
q _displayedPresentationTime;
{CGPoint="x"d"y"d} _displayedOrigin;
B _originMoved;
B _engaged;
```

## Instance methods

```
-[_UIScrollViewVFD dealloc];
-[_UIScrollViewVFD _updateCompleted];
```
