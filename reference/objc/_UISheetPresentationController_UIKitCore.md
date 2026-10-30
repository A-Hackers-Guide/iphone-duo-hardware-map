# `_UISheetPresentationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UISheetPresentationController`
- 2 instance variables, 36 properties, 21 instance methods, 0 class methods

## Instance variables

```
d __preferredRecessedCornerRadius;
@"NSArray" __passthroughViews;
```

## Properties

```
@property (Td,D,N,S_setAdditionalMinimumTopInset:) _additionalMinimumTopInset;
@property (Td,D,N,S_setGrabberTopSpacing:) _grabberTopSpacing;
@property (TB,D,N,S_setWantsBottomAttached:) _wantsBottomAttached;
@property (TB,D,N,S_setAllowsInteractiveDismissWhenFullScreen:) _allowsInteractiveDismissWhenFullScreen;
@property (TB,D,N,S_setAllowsTearOff:) _allowsTearOff;
@property (T@"UIView",&,N,S_setSourceView:) _sourceView;
@property (Tq,D,N,S_setHorizontalAlignment:) _horizontalAlignment;
@property (Td,D,N,S_setMarginInCompactHeight:) _marginInCompactHeight;
@property (Td,D,N,S_setMarginInRegularWidthRegularHeight:) _marginInRegularWidthRegularHeight;
@property (TB,D,N,S_setTucksIntoUnsafeAreaInCompactHeight:) _tucksIntoUnsafeAreaInCompactHeight;
@property (TB,D,N,G_shouldDismissWhenTappedOutside,S_setShouldDismissWhenTappedOutside:) shouldDismissWhenTappedOutside;
@property (TB,D,N,S_setShouldScaleDownBehindDescendantSheets:) _shouldScaleDownBehindDescendantSheets;
@property (TB,D,N,S_setPeeksWhenFloating:) _peeksWhenFloating;
@property (TB,D,N,S_setWantsFullScreen:) _wantsFullScreen;
@property (TB,N,S_setWantsBottomAttachedInCompactHeight:) _wantsBottomAttachedInCompactHeight;
@property (TB,D,N,S_setWantsFloatingInRegularWidthCompactHeight:) _wantsFloatingInRegularWidthCompactHeight;
@property (TB,N,S_setWidthFollowsPreferredContentSizeWhenBottomAttached:) _widthFollowsPreferredContentSizeWhenBottomAttached;
@property (TB,N,S_setWantsGrabber:) _wantsGrabber;
@property (Td,D,N,S_setCornerRadiusForPresentationAndDismissal:) _cornerRadiusForPresentationAndDismissal;
@property (Td,N,S_setPreferredCornerRadius:) _preferredCornerRadius;
@property (Td,N,S_setPreferredRecessedCornerRadius:,V__preferredRecessedCornerRadius) _preferredRecessedCornerRadius;
@property (T@"<_UISheetPresentationControllerDelegate>",W,D,N) delegate;
@property (T@"NSArray",C,N,S_setDetents:) _detents;
@property (Tq,D,N,S_setIndexOfCurrentDetent:) _indexOfCurrentDetent;
@property (Tq,D,N,S_setIndexOfLastUndimmedDetent:) _indexOfLastUndimmedDetent;
@property (Tq,D,N,S_setIndexOfLastUndimmedDetentWhenEdgeAttachedInCompactHeight:) _indexOfLastUndimmedDetentWhenEdgeAttachedInCompactHeight;
@property (Tq,D,N,S_setIndexOfLastUndimmedDetentWhenFloating:) _indexOfLastUndimmedDetentWhenFloating;
@property (T@"NSString",C,D,N,S_setSheetID:) _sheetID;
@property (T@"NSString",C,D,N,S_setHiddenAncestorSheetID:) _hiddenAncestorSheetID;
@property (TB,D,N,G_isHidden,S_setHidden:) _hidden;
@property (Tq,D,N,S_setDetentDirectionWhenFloating:) _detentDirectionWhenFloating;
@property (TB,D,N,S_setPrefersScrollingResizesWhenDetentDirectionIsDown:) _prefersScrollingResizesWhenDetentDirectionIsDown;
@property (TB,N,S_setPrefersScrollingExpandsToLargerDetentWhenScrolledToEdge:) _prefersScrollingExpandsToLargerDetentWhenScrolledToEdge;
@property (T@"NSArray",R,D,N) _detentValues;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,D,N) _currentPresentedViewFrame;
@property (T@"NSArray",C,N,S_setPassthroughViews:,V__passthroughViews) _passthroughViews;
```

## Instance methods

```
-[_UISheetPresentationController _setWidthFollowsPreferredContentSizeWhenBottomAttached:];
-[_UISheetPresentationController _setPassthroughViews:];
-[_UISheetPresentationController _setDetents:];
-[_UISheetPresentationController _sourceView];
-[_UISheetPresentationController _passthroughViews];
-[_UISheetPresentationController _preferredCornerRadius];
-[_UISheetPresentationController _wantsGrabber];
-[_UISheetPresentationController _animateChanges:];
-[_UISheetPresentationController _setWantsGrabber:];
-[_UISheetPresentationController _sendDidChangeSelectedDetentIdentifier];
-[_UISheetPresentationController _detents];
-[_UISheetPresentationController _preferredRecessedCornerRadius];
-[_UISheetPresentationController _setPreferredRecessedCornerRadius:];
-[_UISheetPresentationController _setWantsBottomAttachedInCompactHeight:];
-[_UISheetPresentationController _invalidateDetents];
-[_UISheetPresentationController _setPreferredCornerRadius:];
-[_UISheetPresentationController _prefersScrollingExpandsToLargerDetentWhenScrolledToEdge];
-[_UISheetPresentationController _setPrefersScrollingExpandsToLargerDetentWhenScrolledToEdge:];
-[_UISheetPresentationController _setSourceView:];
-[_UISheetPresentationController _wantsBottomAttachedInCompactHeight];
-[_UISheetPresentationController _widthFollowsPreferredContentSizeWhenBottomAttached];
```
