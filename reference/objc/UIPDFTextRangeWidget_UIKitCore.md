# `UIPDFTextRangeWidget`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIPDFSelectionWidget`, `CALayerDelegate`
- 22 instance variables, 7 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"CALayer" _startSelectionGrabber;
@"CALayer" _startBar;
@"CALayer" _endSelectionGrabber;
@"CALayer" _endBar;
@"CALayer" _startHandle;
@"CALayer" _endHandle;
@"CALayer" _fixedSelectionGrabber;
@"UIPDFPageView" _pageView;
d _handleHeight;
d _handleWidth;
{CGPoint="x"d"y"d} _initialSelectionPointOnPage;
d _offsetX;
d _offsetY;
Q _startIndex;
Q _endIndex;
^{CGColor=} _grabberColor;
q _startRectangle;
q _endRectangle;
B _startLeft;
B _endRight;
d _startX;
d _endX;
```

## Properties

```
@property (T@"UIPDFPageView",N,V_pageView) pageView;
@property (T{CGPoint=dd},R,N,V_initialSelectionPointOnPage) initialSelectionPointOnPage;
@property (T{CGPoint=dd},R,N) currentSelectionPointOnPage;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPDFTextRangeWidget hide];
-[UIPDFTextRangeWidget setSelection:];
-[UIPDFTextRangeWidget init];
-[UIPDFTextRangeWidget dealloc];
-[UIPDFTextRangeWidget drawLayer:inContext:];
-[UIPDFTextRangeWidget remove];
-[UIPDFTextRangeWidget description];
-[UIPDFTextRangeWidget layout];
-[UIPDFTextRangeWidget layoutEndSelectionGrabber:transform:width:extraHeight:unitSize:];
-[UIPDFTextRangeWidget currentSelectionPointOnPage];
-[UIPDFTextRangeWidget endTracking];
-[UIPDFTextRangeWidget hitTest:fixedPoint:preceeds:];
-[UIPDFTextRangeWidget initialSelectionPointOnPage];
-[UIPDFTextRangeWidget layoutStartSelectionGrabber:transform:width:extraHeight:unitSize:];
-[UIPDFTextRangeWidget layoutWidget];
-[UIPDFTextRangeWidget pageView];
-[UIPDFTextRangeWidget selectedPointFor:];
-[UIPDFTextRangeWidget selectionRectangle];
-[UIPDFTextRangeWidget setPageView:];
-[UIPDFTextRangeWidget setSelectedGrabber:];
-[UIPDFTextRangeWidget track:];
-[UIPDFTextRangeWidget viewOffset];
```
