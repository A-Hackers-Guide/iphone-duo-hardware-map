# `CAMExpandableMenuButton`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `CAMAccessibilityHUDItemProvider`
- 14 instance variables, 18 properties, 76 instance methods, 1 class methods

## Instance variables

```
B _expanded;
B __trackingViewHighlighted;
q _layoutStyle;
q _selectedIndex;
q _orientation;
@"NSMutableArray" __menuItems;
@"UIView" __headerView;
@"NSIndexSet" __shownIndexesWhileCollapsed;
@"NSMutableIndexSet" __highlightedIndexesWhileCollapsed;
@"UIView" __padBackgroundView;
@"UIView" __trackingView;
@"<CAMExpandableMenuButtonDelegate>" _expandableMenuDelegate;
@"CAMTouchingGestureRecognizer" _touchingGestureRecognizer;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _tappableEdgeInsets;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V__menuItems) _menuItems;
@property (T@"UIView",R,N,V__headerView) _headerView;
@property (T@"NSIndexSet",R,C,N,V__shownIndexesWhileCollapsed) _shownIndexesWhileCollapsed;
@property (T@"NSMutableIndexSet",R,C,N,V__highlightedIndexesWhileCollapsed) _highlightedIndexesWhileCollapsed;
@property (T@"UIView",R,N,V__padBackgroundView) _padBackgroundView;
@property (T@"UIView",&,N,S_setTrackingView:,V__trackingView) _trackingView;
@property (TB,N,G_isTrackingViewHighlighted,S_setTrackingViewHighlighted:,V__trackingViewHighlighted) _trackingViewHighlighted;
@property (T@"<CAMExpandableMenuButtonDelegate>",W,N,V_expandableMenuDelegate) expandableMenuDelegate;
@property (T@"CAMTouchingGestureRecognizer",R,N,V_touchingGestureRecognizer) touchingGestureRecognizer;
@property (Tq,N,V_layoutStyle) layoutStyle;
@property (Tq,N,V_selectedIndex) selectedIndex;
@property (TB,R,N,GisExpanded,V_expanded) expanded;
@property (Tq,N,V_orientation) orientation;
@property (T{UIEdgeInsets=dddd},N,V_tappableEdgeInsets) tappableEdgeInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMExpandableMenuButton expansionDuration];
```

## Instance methods

```
-[CAMExpandableMenuButton setLayoutStyle:];
-[CAMExpandableMenuButton setOrientation:animated:];
-[CAMExpandableMenuButton setOrientation:];
-[CAMExpandableMenuButton layoutStyle];
-[CAMExpandableMenuButton intrinsicContentSize];
-[CAMExpandableMenuButton headerView];
-[CAMExpandableMenuButton selectedIndex];
-[CAMExpandableMenuButton isExpanded];
-[CAMExpandableMenuButton alignmentRectInsets];
-[CAMExpandableMenuButton initWithLayoutStyle:];
-[CAMExpandableMenuButton orientation];
-[CAMExpandableMenuButton touchingGestureRecognizer];
-[CAMExpandableMenuButton layoutSubviews];
-[CAMExpandableMenuButton _handleTouchGesture:];
-[CAMExpandableMenuButton _preferredContentSizeCategoryDidChange];
-[CAMExpandableMenuButton reloadData];
-[CAMExpandableMenuButton setTappableEdgeInsets:];
-[CAMExpandableMenuButton setSelectedIndex:];
-[CAMExpandableMenuButton initWithCoder:];
-[CAMExpandableMenuButton selectedByAccessibilityHUDManager:];
-[CAMExpandableMenuButton tappableEdgeInsets];
-[CAMExpandableMenuButton initWithFrame:];
-[CAMExpandableMenuButton hudItemForAccessibilityHUDManager:];
-[CAMExpandableMenuButton startCollapsingWithProposedFrame:];
-[CAMExpandableMenuButton startExpansionWithProposedFrame:];
-[CAMExpandableMenuButton titleForMenuItemAtIndex:];
-[CAMExpandableMenuButton _viewToTrackForTouchAtLocation:];
-[CAMExpandableMenuButton alignmentRectForFrame:expanded:];
-[CAMExpandableMenuButton frameForAlignmentRect:expanded:];
-[CAMExpandableMenuButton _applyHeaderViewForCurrentExpansionState];
-[CAMExpandableMenuButton _applyMenuItemAlphaForCurrentExpansionState];
-[CAMExpandableMenuButton _applyMenuItemColorsForCurrentState];
-[CAMExpandableMenuButton _applyMenuItemTextAlignmentAndShadowForCurrentOrientation];
-[CAMExpandableMenuButton _convertAllSubviewsToProposedFrame:];
-[CAMExpandableMenuButton _createPadBackgroundView];
-[CAMExpandableMenuButton _headerView];
-[CAMExpandableMenuButton _highlightedIndexesWhileCollapsed];
-[CAMExpandableMenuButton _isTrackingViewHighlighted];
-[CAMExpandableMenuButton _layoutForPadCollapsedPortraitButton:];
-[CAMExpandableMenuButton _layoutForPadExpandedPortraitButton:];
-[CAMExpandableMenuButton _layoutForPadStyle:expanded:];
-[CAMExpandableMenuButton _layoutForPhoneCollapsedLandscapeButton:];
-[CAMExpandableMenuButton _layoutForPhoneCollapsedPortraitButton:];
-[CAMExpandableMenuButton _layoutForPhoneExpandedLandscapeButton:];
-[CAMExpandableMenuButton _layoutForPhoneExpandedPortraitButton:];
-[CAMExpandableMenuButton _layoutForPhoneStyle:expanded:];
-[CAMExpandableMenuButton _layoutMenuButton:expanded:];
-[CAMExpandableMenuButton _menuItems];
-[CAMExpandableMenuButton _padBackgroundView];
-[CAMExpandableMenuButton _padCollapsedIntrinsicContentSize];
-[CAMExpandableMenuButton _selectedLabel];
-[CAMExpandableMenuButton _setTrackingView:];
-[CAMExpandableMenuButton _setTrackingViewHighlighted:];
-[CAMExpandableMenuButton _shownIndexesWhileCollapsed];
-[CAMExpandableMenuButton _trackingView];
-[CAMExpandableMenuButton _updateFromExpansionChangeAnimated:];
-[CAMExpandableMenuButton _updateFromOrientationChangeAnimated:];
-[CAMExpandableMenuButton _updateFromSelectedIndexChange];
-[CAMExpandableMenuButton _wantsHeaderViewToBeVisible];
-[CAMExpandableMenuButton collapseMenuAnimated:];
-[CAMExpandableMenuButton collapsedSelectedLabelHorizontalMargin];
-[CAMExpandableMenuButton completeExpansionToProposedFrame:];
-[CAMExpandableMenuButton expandMenuAnimated:];
-[CAMExpandableMenuButton expandableMenuDelegate];
-[CAMExpandableMenuButton finishCollapsingAnimated:];
-[CAMExpandableMenuButton finishExpansionAnimated:];
-[CAMExpandableMenuButton intrinsicContentSizeForExpansion:];
-[CAMExpandableMenuButton numberOfMenuItems];
-[CAMExpandableMenuButton padHeaderViewContentInsetLeft];
-[CAMExpandableMenuButton prepareHeaderViewForExpanding:];
-[CAMExpandableMenuButton setExpandableMenuDelegate:];
-[CAMExpandableMenuButton setHighlighted:forIndex:];
-[CAMExpandableMenuButton shouldAllowExpansion];
-[CAMExpandableMenuButton shouldIgnoreMenuInteraction];
-[CAMExpandableMenuButton shownIndexesWhileCollapsed];
-[CAMExpandableMenuButton wantsSelectedItemToBeVisible];
```
