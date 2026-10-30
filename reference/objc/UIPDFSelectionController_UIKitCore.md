# `UIPDFSelectionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 17 instance variables, 8 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"UIPDFPageView" _pageView;
B _rangeMode;
@"<UIPDFSelectionWidget><NSObject>" _selectionWidget;
B _resizingWidget;
{CGPoint="x"d"y"d} _selectionFixedPoint;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _selectionBounds;
B _preceeds;
B _isTracking;
{CGPoint="x"d"y"d} _adjustedPoint;
B _hiding;
q _firstIndex;
q _lastIndex;
{CGPoint="x"d"y"d} _startPoint;
B _needsLayout;
B _cancelled;
B _instantModeIsSuspended;
B _instantHighlightMode;
```

## Properties

```
@property (T@"UIPDFPageView",N,V_pageView) pageView;
@property (TB,R,N,V_rangeMode) rangeMode;
@property (T@"<UIPDFSelectionWidget>",R,N,V_selectionWidget) selectionWidget;
@property (TB,R,N,V_isTracking) isTracking;
@property (T{CGPoint=dd},R,N,V_adjustedPoint) adjustedPoint;
@property (T{CGPoint=dd},R,N) initialSelectionPoint;
@property (T{CGPoint=dd},R,N) currentSelectionPoint;
@property (TB,N,V_instantHighlightMode) instantHighlightMode;
```

## Instance methods

```
-[UIPDFSelectionController clearSelection];
-[UIPDFSelectionController init];
-[UIPDFSelectionController dealloc];
-[UIPDFSelectionController isTracking];
-[UIPDFSelectionController description];
-[UIPDFSelectionController selectionWidget];
-[UIPDFSelectionController addSelectionWidget:];
-[UIPDFSelectionController adjustSelection:];
-[UIPDFSelectionController adjustedPoint];
-[UIPDFSelectionController currentSelectionPoint];
-[UIPDFSelectionController endTracking:];
-[UIPDFSelectionController extendSelectionToParagraph];
-[UIPDFSelectionController hideWidget];
-[UIPDFSelectionController initialSelectionPoint];
-[UIPDFSelectionController instantHighlightMode];
-[UIPDFSelectionController layoutSelections];
-[UIPDFSelectionController pageView];
-[UIPDFSelectionController rangeMode];
-[UIPDFSelectionController selectedPointOffset];
-[UIPDFSelectionController selectionHide:];
-[UIPDFSelectionController selectionHideFromAncestor:];
-[UIPDFSelectionController selectionShow:];
-[UIPDFSelectionController selectionShowDelayed:];
-[UIPDFSelectionController selectionShowToAncestor:];
-[UIPDFSelectionController setInstantHighlightMode:];
-[UIPDFSelectionController setPageView:];
-[UIPDFSelectionController setSelectionFor:];
-[UIPDFSelectionController shouldTrackAt:];
-[UIPDFSelectionController startSelectingAt:];
-[UIPDFSelectionController startTracking:andPoint:];
-[UIPDFSelectionController startTracking:showMagnifier:];
-[UIPDFSelectionController suspendInstantHighlightMode];
-[UIPDFSelectionController tracking:andPoint:];
-[UIPDFSelectionController tracking:showMagnifier:];
-[UIPDFSelectionController useParagraphMode];
```
