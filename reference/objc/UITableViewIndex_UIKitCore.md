# `UITableViewIndex`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UIAccessibilityHUDGestureDelegate`
- 20 instance variables, 17 properties, 61 instance methods, 3 class methods

## Instance variables

```
@"NSArray" _titles;
@"UIFont" _font;
q _selectedSection;
B _pastTop;
B _pastBottom;
{CGSize="width"d"height"d} _cachedSize;
{CGSize="width"d"height"d} _cachedSizeToFit;
@"UIColor" _indexColor;
@"UIColor" _indexBackgroundColor;
@"UIColor" _indexTrackingBackgroundColor;
d _topPadding;
d _bottomPadding;
d _verticalTextHeightEstimate;
@"NSArray" _entries;
q _idiom;
@"UIAccessibilityHUDGestureManager" _axHUDGestureManager;
@"UITableView" _tableView;
Q _drawingInsetsMask;
@"<UITableViewIndexVisualStyle>" _visualStyle;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _drawingInsets;
```

## Properties

```
@property (TQ,N,V_drawingInsetsMask) drawingInsetsMask;
@property (T@"UITableView",W,N,V_tableView) tableView;
@property (T@"NSArray",&,N) titles;
@property (T@"UIFont",&,N) font;
@property (T{UIEdgeInsets=dddd},N,V_drawingInsets) drawingInsets;
@property (T@"UIColor",&,N) indexColor;
@property (T@"UIColor",&,N) indexBackgroundColor;
@property (T@"UIColor",&,N) indexTrackingBackgroundColor;
@property (Tq,R,N,V_selectedSection) selectedSection;
@property (T@"NSString",R,N) selectedSectionTitle;
@property (TB,R,N,V_pastTop) pastTop;
@property (TB,R,N,V_pastBottom) pastBottom;
@property (T@"<UITableViewIndexVisualStyle>",&,N,V_visualStyle) visualStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UITableViewIndex registerVisualStyle:forIdiom:];
+[UITableViewIndex makeTableViewIndex:containerView:forTraits:];
+[UITableViewIndex visualStyleForTableViewIndex:];
```

## Instance methods

```
-[UITableViewIndex tableView];
-[UITableViewIndex _horizontalSizeClassDidChange];
-[UITableViewIndex touchesEnded:withEvent:];
-[UITableViewIndex _accessibilityHUDGestureManager:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UITableViewIndex didMoveToWindow];
-[UITableViewIndex setVisualStyle:];
-[UITableViewIndex _accessibilityHUDGestureManager:HUDItemForPoint:];
-[UITableViewIndex _accessibilityHUDGestureManager:gestureLiftedAtPoint:];
-[UITableViewIndex visualStyle];
-[UITableViewIndex cancelTrackingWithEvent:];
-[UITableViewIndex endTrackingWithTouch:withEvent:];
-[UITableViewIndex continueTrackingWithTouch:withEvent:];
-[UITableViewIndex drawRect:];
-[UITableViewIndex beginTrackingWithTouch:withEvent:];
-[UITableViewIndex touchesBegan:withEvent:];
-[UITableViewIndex touchesMoved:withEvent:];
-[UITableViewIndex canBecomeFocused];
-[UITableViewIndex sizeThatFits:];
-[UITableViewIndex tintColorDidChange];
-[UITableViewIndex setTableView:];
-[UITableViewIndex setFrame:];
-[UITableViewIndex font];
-[UITableViewIndex _shouldAnimatePropertyWithKey:];
-[UITableViewIndex initWithFrame:];
-[UITableViewIndex setFont:];
-[UITableViewIndex pastTop];
-[UITableViewIndex selectedSection];
-[UITableViewIndex _accessibilityHUDGestureManager:canCancelGestureRecognizer:];
-[UITableViewIndex _accessibilityHUDGestureManagerCancelsTouchesInView:];
-[UITableViewIndex _cacheAndMeasureTitles];
-[UITableViewIndex _coreIdiom];
-[UITableViewIndex _displayTitles];
-[UITableViewIndex _dotImage];
-[UITableViewIndex _effectiveBounds];
-[UITableViewIndex _externalDotImage];
-[UITableViewIndex _handleTouches:withEvent:];
-[UITableViewIndex _idiom];
-[UITableViewIndex _indexForEntryAtPoint:];
-[UITableViewIndex _largeContentViewerEnabledStatusDidChange:];
-[UITableViewIndex _legibilityWeightOrPreferredContentSizeTraitsDidChange];
-[UITableViewIndex _minLineSpacingForIdiom:];
-[UITableViewIndex _setIdiom:];
-[UITableViewIndex _setupAXHUDGestureIfNecessary];
-[UITableViewIndex _updateSectionForTouch:withEvent:];
-[UITableViewIndex _visibleBoundsForRect:stride:];
-[UITableViewIndex _willChangeToIdiom:onScreen:];
-[UITableViewIndex drawingInsets];
-[UITableViewIndex drawingInsetsMask];
-[UITableViewIndex indexBackgroundColor];
-[UITableViewIndex indexColor];
-[UITableViewIndex indexTrackingBackgroundColor];
-[UITableViewIndex maximumNumberOfTitlesWithoutTruncationForHeight:];
-[UITableViewIndex pastBottom];
-[UITableViewIndex selectedSectionTitle];
-[UITableViewIndex setDrawingInsets:];
-[UITableViewIndex setDrawingInsetsMask:];
-[UITableViewIndex setIndexBackgroundColor:];
-[UITableViewIndex setIndexColor:];
-[UITableViewIndex setIndexTrackingBackgroundColor:];
-[UITableViewIndex setTitles:];
-[UITableViewIndex titles];
```
