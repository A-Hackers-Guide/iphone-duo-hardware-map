# `UIIndexBarView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UIAccessibilityHUDGestureDelegate`
- 17 instance variables, 22 properties, 70 instance methods, 3 class methods

## Instance variables

```
{?="entriesUpdated"b1"displayEntriesUpdated"b1"sizeUpdated"b1"highlightedIndexUpdated"b1"deflectionUpdated"b1"deflectionReset"b1"layoutSubviews"b1"drawRect"b1"trackingDidBegin"b1"trackingChangeHysteresis"b1"trackingDidEnd"b1"updateSectionForTouch"b1"highlightStyleUpdated"b1"indexColorUpdated"b1"legibilityWeightOrPreferredContentSizeUpdated"b1} _visualStyleImplements;
@"UIColor" _indexColor;
@"NSArray" _entries;
@"<UIIndexBarViewDelegate>" _delegate;
Q _drawingInsetsMask;
@"UIColor" _trackingBackgroundColor;
q _highlightStyle;
d _highlightedIndex;
d _deflection;
@"<UIIndexBarVisualStyle>" _visualStyle;
@"NSArray" _displayEntries;
d _cachedDisplayHighlightedIndex;
@"UIColor" _nonTrackingBackgroundColor;
@"UISelectionFeedbackGenerator" _selectionFeedbackGenerator;
@"UIAccessibilityHUDGestureManager" _axHUDGestureManager;
{CGPoint="x"d"y"d} _trackingStartLocationInWindow;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _drawingInsets;
```

## Properties

```
@property (TQ,N,V_drawingInsetsMask) drawingInsetsMask;
@property (Td,N,V_cachedDisplayHighlightedIndex) cachedDisplayHighlightedIndex;
@property (T@"UIColor",C,N,V_nonTrackingBackgroundColor) nonTrackingBackgroundColor;
@property (T{CGPoint=dd},N,V_trackingStartLocationInWindow) trackingStartLocationInWindow;
@property (T@"UISelectionFeedbackGenerator",&,N,V_selectionFeedbackGenerator) selectionFeedbackGenerator;
@property (T@"UIAccessibilityHUDGestureManager",&,N,V_axHUDGestureManager) axHUDGestureManager;
@property (T@"NSArray",C,N,V_entries) entries;
@property (T@"<UIIndexBarViewDelegate>",W,N,V_delegate) delegate;
@property (T{UIEdgeInsets=dddd},N,V_drawingInsets) drawingInsets;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) effectiveBounds;
@property (T@"UIColor",C,N,V_indexColor) indexColor;
@property (T@"UIColor",C,N,V_trackingBackgroundColor) trackingBackgroundColor;
@property (Tq,N,V_highlightStyle) highlightStyle;
@property (Td,N,V_highlightedIndex) highlightedIndex;
@property (Td,N,V_deflection) deflection;
@property (T@"<UIIndexBarVisualStyle>",&,N,V_visualStyle) visualStyle;
@property (T@"NSArray",&,N,V_displayEntries) displayEntries;
@property (Td,R,N) displayHighlightedIndex;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIIndexBarView registerVisualStyle:forIdiom:];
+[UIIndexBarView makeIndexBarView:containerView:forTraits:];
+[UIIndexBarView visualStyleForIndexBarView:];
```

## Instance methods

```
-[UIIndexBarView entries];
-[UIIndexBarView _horizontalSizeClassDidChange];
-[UIIndexBarView touchesEnded:withEvent:];
-[UIIndexBarView _canDrawContent];
-[UIIndexBarView _accessibilityHUDGestureManager:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[UIIndexBarView didMoveToWindow];
-[UIIndexBarView setVisualStyle:];
-[UIIndexBarView _accessibilityHUDGestureManager:HUDItemForPoint:];
-[UIIndexBarView _accessibilityHUDGestureManager:gestureLiftedAtPoint:];
-[UIIndexBarView setEntries:];
-[UIIndexBarView visualStyle];
-[UIIndexBarView cancelTrackingWithEvent:];
-[UIIndexBarView endTrackingWithTouch:withEvent:];
-[UIIndexBarView continueTrackingWithTouch:withEvent:];
-[UIIndexBarView drawRect:];
-[UIIndexBarView layoutSubviews];
-[UIIndexBarView selectionFeedbackGenerator];
-[UIIndexBarView beginTrackingWithTouch:withEvent:];
-[UIIndexBarView touchesBegan:withEvent:];
-[UIIndexBarView touchesMoved:withEvent:];
-[UIIndexBarView canBecomeFocused];
-[UIIndexBarView setBackgroundColor:];
-[UIIndexBarView sizeThatFits:];
-[UIIndexBarView setDelegate:];
-[UIIndexBarView tintColorDidChange];
-[UIIndexBarView delegate];
-[UIIndexBarView setFrame:];
-[UIIndexBarView backgroundColor];
-[UIIndexBarView _updateBackgroundColor];
-[UIIndexBarView setSelectionFeedbackGenerator:];
-[UIIndexBarView initWithFrame:];
-[UIIndexBarView effectiveBounds];
-[UIIndexBarView _accessibilityHUDGestureManager:canCancelGestureRecognizer:];
-[UIIndexBarView _accessibilityHUDGestureManagerCancelsTouchesInView:];
-[UIIndexBarView _defaultCanBecomeFocused];
-[UIIndexBarView _didSelectEntry:atIndex:location:];
-[UIIndexBarView _handleTouches:withEvent:];
-[UIIndexBarView _largeContentViewerEnabledStatusDidChange:];
-[UIIndexBarView _legibilityWeightOrPreferredContentSizeTraitsDidChange];
-[UIIndexBarView _selectEntry:atIndex:];
-[UIIndexBarView _setupAXHUDGestureIfNecessary];
-[UIIndexBarView _updateDisplayEntries];
-[UIIndexBarView _userInteractionStarted];
-[UIIndexBarView _userInteractionStopped];
-[UIIndexBarView axHUDGestureManager];
-[UIIndexBarView cachedDisplayHighlightedIndex];
-[UIIndexBarView deflection];
-[UIIndexBarView displayEntries];
-[UIIndexBarView displayHighlightedIndex];
-[UIIndexBarView drawingInsets];
-[UIIndexBarView drawingInsetsMask];
-[UIIndexBarView highlightStyle];
-[UIIndexBarView highlightedIndex];
-[UIIndexBarView indexColor];
-[UIIndexBarView nonTrackingBackgroundColor];
-[UIIndexBarView resetDeflection:];
-[UIIndexBarView setAxHUDGestureManager:];
-[UIIndexBarView setCachedDisplayHighlightedIndex:];
-[UIIndexBarView setDeflection:];
-[UIIndexBarView setDisplayEntries:];
-[UIIndexBarView setDrawingInsets:];
-[UIIndexBarView setDrawingInsetsMask:];
-[UIIndexBarView setHighlightStyle:];
-[UIIndexBarView setHighlightedIndex:];
-[UIIndexBarView setIndexColor:];
-[UIIndexBarView setNonTrackingBackgroundColor:];
-[UIIndexBarView setTrackingBackgroundColor:];
-[UIIndexBarView setTrackingStartLocationInWindow:];
-[UIIndexBarView trackingBackgroundColor];
-[UIIndexBarView trackingStartLocationInWindow];
```
