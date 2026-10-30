# `ICDocCamOverlayView`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `CAAnimationDelegate`
- 19 instance variables, 22 properties, 56 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_semaphore>" sem;
B _showGridAnimation;
B _rectangleIsActive;
@"NSString" _displayString;
@"ICDocCamImageQuad" _documentQuad;
@"NSArray" _debugRects;
@"UIColor" _rectColor;
@"CAShapeLayer" _llShapeLayer;
@"CAShapeLayer" _lrShapeLayer;
@"CAShapeLayer" _ulShapeLayer;
@"CAShapeLayer" _urShapeLayer;
@"CAShapeLayer" _rectangleShapeLayer;
Q _numberOfMissedFrames;
@"UILabel" _displayStringLabel;
@"CAShapeLayer" _rectangleGridLayer;
@"NSDate" _dateToStartGridAnimation;
@"CAAnimation" _gridAnimation;
@"CAGradientLayer" _gradientMaskLayer;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _previewBounds;
```

## Properties

```
@property (TB,N,V_rectangleIsActive) rectangleIsActive;
@property (T@"CAShapeLayer",&,N,V_llShapeLayer) llShapeLayer;
@property (T@"CAShapeLayer",&,N,V_lrShapeLayer) lrShapeLayer;
@property (T@"CAShapeLayer",&,N,V_ulShapeLayer) ulShapeLayer;
@property (T@"CAShapeLayer",&,N,V_urShapeLayer) urShapeLayer;
@property (T@"CAShapeLayer",&,N,V_rectangleShapeLayer) rectangleShapeLayer;
@property (TQ,V_numberOfMissedFrames) numberOfMissedFrames;
@property (T@"UILabel",&,N,V_displayStringLabel) displayStringLabel;
@property (T@"CAShapeLayer",&,N,V_rectangleGridLayer) rectangleGridLayer;
@property (T@"NSDate",&,N,V_dateToStartGridAnimation) dateToStartGridAnimation;
@property (T@"CAAnimation",&,N,V_gridAnimation) gridAnimation;
@property (T@"CAGradientLayer",&,N,V_gradientMaskLayer) gradientMaskLayer;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},V_previewBounds) previewBounds;
@property (T@"NSArray",&,V_debugRects) debugRects;
@property (T@"NSString",&,V_displayString) displayString;
@property (T@"ICDocCamImageQuad",&,V_documentQuad) documentQuad;
@property (TB,V_showGridAnimation) showGridAnimation;
@property (T@"UIColor",&,V_rectColor) rectColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ICDocCamOverlayView animationDidStop:finished:];
-[ICDocCamOverlayView displayString];
-[ICDocCamOverlayView setDisplayString:];
-[ICDocCamOverlayView initWithCoder:];
-[ICDocCamOverlayView initWithFrame:];
-[ICDocCamOverlayView clearRectangles];
-[ICDocCamOverlayView setupGridLayers];
-[ICDocCamOverlayView calculateCurrentRectangleFromDocumentQuad:];
-[ICDocCamOverlayView calculateRotationTransformForPoint:toPoint:];
-[ICDocCamOverlayView crossProduct:v2:];
-[ICDocCamOverlayView dateToStartGridAnimation];
-[ICDocCamOverlayView debugRects];
-[ICDocCamOverlayView displayStringLabel];
-[ICDocCamOverlayView documentQuad];
-[ICDocCamOverlayView extrudedRectFromRect:];
-[ICDocCamOverlayView frameForContentInView];
-[ICDocCamOverlayView gradientMaskLayer];
-[ICDocCamOverlayView gridAnimation];
-[ICDocCamOverlayView llShapeLayer];
-[ICDocCamOverlayView lrShapeLayer];
-[ICDocCamOverlayView newGridPathFromRect:];
-[ICDocCamOverlayView newPathFromRect:];
-[ICDocCamOverlayView numberOfMissedFrames];
-[ICDocCamOverlayView previewBounds];
-[ICDocCamOverlayView rectColor];
-[ICDocCamOverlayView rectangleGridLayer];
-[ICDocCamOverlayView rectangleIsActive];
-[ICDocCamOverlayView rectangleShapeLayer];
-[ICDocCamOverlayView setDateToStartGridAnimation:];
-[ICDocCamOverlayView setDebugRects:];
-[ICDocCamOverlayView setDisplayStringLabel:];
-[ICDocCamOverlayView setDocumentQuad:];
-[ICDocCamOverlayView setGradientMaskLayer:];
-[ICDocCamOverlayView setGridAnimation:];
-[ICDocCamOverlayView setLlShapeLayer:];
-[ICDocCamOverlayView setLrShapeLayer:];
-[ICDocCamOverlayView setNumberOfMissedFrames:];
-[ICDocCamOverlayView setPreviewBounds:];
-[ICDocCamOverlayView setRectColor:];
-[ICDocCamOverlayView setRectangleGridLayer:];
-[ICDocCamOverlayView setRectangleIsActive:];
-[ICDocCamOverlayView setRectangleShapeLayer:];
-[ICDocCamOverlayView setShowGridAnimation:];
-[ICDocCamOverlayView setUlShapeLayer:];
-[ICDocCamOverlayView setUrShapeLayer:];
-[ICDocCamOverlayView setupRectangleLayer];
-[ICDocCamOverlayView setupShapeLayersIfNeeded];
-[ICDocCamOverlayView showGridAnimation];
-[ICDocCamOverlayView startGridAnimationFromRect:];
-[ICDocCamOverlayView stopGridAnimation];
-[ICDocCamOverlayView tintColorWithAlpha:];
-[ICDocCamOverlayView ulShapeLayer];
-[ICDocCamOverlayView updateGridLayerFromRect:];
-[ICDocCamOverlayView updateRectangleLayerFromRect:];
-[ICDocCamOverlayView updateShapeLayers];
-[ICDocCamOverlayView urShapeLayer];
```
