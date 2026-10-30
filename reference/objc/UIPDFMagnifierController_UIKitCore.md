# `UIPDFMagnifierController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CALayerDelegate`
- 23 instance variables, 5 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"UIWindow" _textEffectsWindow;
@"UIView" _textEffectsSubView;
@"CALayer" _loLayer;
@"CALayer" _hiLayer;
@"CALayer" _imageContainer;
@"CALayer" _imageLayer;
@"CAShapeLayer" _selectionLayer;
@"CALayer" _maskLayer;
d _power;
{CGSize="width"d"height"d} _magnifierSize;
B _loupe;
{CGPoint="x"d"y"d} _touchPoint;
{CGPoint="x"d"y"d} _pointToMagnify;
d _enlargementScale;
@"CALayer" _leftBar;
@"CALayer" _leftGrabber;
@"CALayer" _rightBar;
@"CALayer" _rightGrabber;
{CGSize="width"d"height"d} _controlPointSize;
^{CGColor=} _grabberColor;
Q _pageRotation;
B _visible;
@"UIPDFPageView" pageView;
```

## Properties

```
@property (T@"UIPDFPageView",N,VpageView) pageView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIPDFMagnifierController hide];
-[UIPDFMagnifierController visible];
-[UIPDFMagnifierController init];
-[UIPDFMagnifierController dealloc];
-[UIPDFMagnifierController drawLayer:inContext:];
-[UIPDFMagnifierController _show];
-[UIPDFMagnifierController addBling];
-[UIPDFMagnifierController addTextRangeHandles];
-[UIPDFMagnifierController convertPointToEnlargedSpace:];
-[UIPDFMagnifierController convertPointToRotatedPage:];
-[UIPDFMagnifierController convertRectToEnlargedSpace:];
-[UIPDFMagnifierController convertRectToRotatedPage:];
-[UIPDFMagnifierController convertViewPointToEnlargedSpace:];
-[UIPDFMagnifierController imageReceived:data:];
-[UIPDFMagnifierController isSelectionUniformlyRotated:];
-[UIPDFMagnifierController move];
-[UIPDFMagnifierController pageView];
-[UIPDFMagnifierController placeImage];
-[UIPDFMagnifierController pointToMagnifyInPDFSpace];
-[UIPDFMagnifierController setImageContainerMask];
-[UIPDFMagnifierController setImageContainerPositionLoupe];
-[UIPDFMagnifierController setImageContainerPositionMagnifier];
-[UIPDFMagnifierController setLayerPositions];
-[UIPDFMagnifierController setPageView:];
-[UIPDFMagnifierController setPosition:viewPoint:];
-[UIPDFMagnifierController setPower];
-[UIPDFMagnifierController setSelectionPath];
-[UIPDFMagnifierController setSelectionPath:bounds:transform:];
-[UIPDFMagnifierController setTextRangeHandlePositions];
-[UIPDFMagnifierController showLoupe];
-[UIPDFMagnifierController showMagnifier];
-[UIPDFMagnifierController tearDownLayers];
-[UIPDFMagnifierController viewPointInTextEffectsSpace];
```
