# `UIRefreshControl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- 11 instance variables, 12 properties, 61 instance methods, 4 class methods

## Instance variables

```
q _style;
@"_UIRefreshControlContentView" _contentView;
d _refreshControlHeight;
d _visibleHeight;
d _snappingHeight;
d _additionalTopInset;
B _insetsApplied;
B _adjustingInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _appliedInsets;
@"<_UIRefreshControlHosting>" _host;
q _refreshControlState;
```

## Properties

```
@property (Tq,R,N,V_refreshControlState) refreshControlState;
@property (Tq,R,N) style;
@property (Td,R,N) _refreshControlHeight;
@property (Td,R,N) _snappingHeight;
@property (Td,R,N) _visibleHeight;
@property (TB,R,N) _hostAdjustsContentOffset;
@property (TB,R,N) _areInsetsBeingApplied;
@property (T{UIEdgeInsets=dddd},R,N,G_appliedInsets) appliedInsets;
@property (T@"<_UIRefreshControlHosting>",W,N,G_host,S_setHost:) _host;
@property (TB,R,N,GisRefreshing) refreshing;
@property (T@"UIColor",&,N) tintColor;
@property (T@"NSAttributedString",&,N) attributedTitle;
```

## Class methods

```
+[UIRefreshControl _contentViewClassForStyle:];
+[UIRefreshControl _setAllowsUnsupportedMacIdiomBehavior:];
+[UIRefreshControl _defaultColor];
+[UIRefreshControl _allowsUnsupportedMacIdiomBehavior];
```

## Instance methods

```
-[UIRefreshControl _controlEventsForActionTriggered];
-[UIRefreshControl _tintColor];
-[UIRefreshControl _scrollView];
-[UIRefreshControl _setTintColor:];
-[UIRefreshControl sizeToFit];
-[UIRefreshControl init];
-[UIRefreshControl setAttributedTitle:];
-[UIRefreshControl dealloc];
-[UIRefreshControl _update];
-[UIRefreshControl _contentView];
-[UIRefreshControl initWithStyle:];
-[UIRefreshControl style];
-[UIRefreshControl setBounds:];
-[UIRefreshControl setBackgroundColor:];
-[UIRefreshControl sizeThatFits:];
-[UIRefreshControl setTintColor:];
-[UIRefreshControl attributedTitle];
-[UIRefreshControl encodeWithCoder:];
-[UIRefreshControl setFrame:];
-[UIRefreshControl description];
-[UIRefreshControl tintColor];
-[UIRefreshControl initWithCoder:];
-[UIRefreshControl _populateArchivedSubviews:];
-[UIRefreshControl didMoveToSuperview];
-[UIRefreshControl initWithFrame:];
-[UIRefreshControl beginRefreshing];
-[UIRefreshControl _setRefreshControlState:notify:];
-[UIRefreshControl _snappingHeight];
-[UIRefreshControl _addInsetHeight:];
-[UIRefreshControl _addInsets];
-[UIRefreshControl _appliedInsets];
-[UIRefreshControl _areInsetsBeingApplied];
-[UIRefreshControl _attributedTitle];
-[UIRefreshControl _canTransitionFromState:toState:];
-[UIRefreshControl _didScroll];
-[UIRefreshControl _endRefreshingAnimated:];
-[UIRefreshControl _host];
-[UIRefreshControl _hostAdjustsContentOffset];
-[UIRefreshControl _impactIntensityForVelocity:];
-[UIRefreshControl _isApplyingInsets];
-[UIRefreshControl _originForContentOffset:];
-[UIRefreshControl _recomputeNewState];
-[UIRefreshControl _refreshControlHeight];
-[UIRefreshControl _removeInsetHeight:];
-[UIRefreshControl _removeInsets];
-[UIRefreshControl _resizeToFitContents];
-[UIRefreshControl _scrollViewHeight];
-[UIRefreshControl _setAttributedTitle:];
-[UIRefreshControl _setHost:];
-[UIRefreshControl _setVisibleHeight:];
-[UIRefreshControl _stiffnessForVelocity:];
-[UIRefreshControl _updateConcealingMask];
-[UIRefreshControl _updateHiddenStateIfNeeded];
-[UIRefreshControl _updateSnappingHeight];
-[UIRefreshControl _visibleHeight];
-[UIRefreshControl _visibleHeightForContentOffset:origin:];
-[UIRefreshControl endRefreshing];
-[UIRefreshControl isRefreshing];
-[UIRefreshControl refreshControlState];
-[UIRefreshControl revealedFraction];
-[UIRefreshControl setRefreshControlState:];
```
