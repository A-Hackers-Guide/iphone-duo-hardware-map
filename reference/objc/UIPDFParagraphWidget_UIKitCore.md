# `UIPDFParagraphWidget`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIPDFSelectionWidget`, `CALayerDelegate`
- 13 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"CAShapeLayer" _trackingBorder;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialRect;
B _tracking;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _currentTrackingRect;
@"CALayer" _leftGrabber;
@"CALayer" _rightGrabber;
@"CALayer" _topGrabber;
@"CALayer" _bottomGrabber;
@"CALayer" _selectedGrabber;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundsInPDFSpace;
^{CGColor=} _grabberColor;
@"UIPDFPageView" _pageView;
{CGPoint="x"d"y"d} _initialSelectionPointOnPage;
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
-[UIPDFParagraphWidget hide];
-[UIPDFParagraphWidget setSelection:];
-[UIPDFParagraphWidget init];
-[UIPDFParagraphWidget dealloc];
-[UIPDFParagraphWidget drawLayer:inContext:];
-[UIPDFParagraphWidget remove];
-[UIPDFParagraphWidget layout];
-[UIPDFParagraphWidget adjustRect:toPoint:];
-[UIPDFParagraphWidget currentSelectionPointOnPage];
-[UIPDFParagraphWidget endTracking];
-[UIPDFParagraphWidget hitTest:fixedPoint:preceeds:];
-[UIPDFParagraphWidget initialSelectionPointOnPage];
-[UIPDFParagraphWidget pageView];
-[UIPDFParagraphWidget selectedPointFor:];
-[UIPDFParagraphWidget selectionBoundsInEffectsSpace];
-[UIPDFParagraphWidget selectionRectangle];
-[UIPDFParagraphWidget setPageView:];
-[UIPDFParagraphWidget setSelectedGrabber:];
-[UIPDFParagraphWidget setSelectedGrabberPosition:];
-[UIPDFParagraphWidget track:];
-[UIPDFParagraphWidget viewOffset];
```
