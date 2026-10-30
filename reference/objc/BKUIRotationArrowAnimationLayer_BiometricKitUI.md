# `BKUIRotationArrowAnimationLayer`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 13 instance variables, 13 properties, 45 instance methods, 2 class methods

## Instance variables

```
q _orientation;
d _radius;
d _arrowAngle;
d _arrowlength;
@"UIColor" _color;
@"CALayer" _arrowContainer;
@? _getOrientation;
@"CAShapeLayer" _arrowLayerLeft;
@"CAShapeLayer" _arrowLayerRight;
@"CAShapeLayer" _circleLayer;
@"CAShapeLayer" _rotationLayer;
{CGSize="width"d"height"d} _containerSize;
{CGPoint="x"d"y"d} _hostCenter;
```

## Properties

```
@property (Td,N,V_radius) radius;
@property (Td,N,V_arrowAngle) arrowAngle;
@property (Td,N,V_arrowlength) arrowlength;
@property (T{CGSize=dd},N,V_containerSize) containerSize;
@property (T{CGPoint=dd},N,V_hostCenter) hostCenter;
@property (T@"UIColor",&,N,V_color) color;
@property (T@"CALayer",&,N,V_arrowContainer) arrowContainer;
@property (T@?,C,N,V_getOrientation) getOrientation;
@property (T@"CAShapeLayer",&,N,V_arrowLayerLeft) arrowLayerLeft;
@property (T@"CAShapeLayer",&,N,V_arrowLayerRight) arrowLayerRight;
@property (T@"CAShapeLayer",&,N,V_circleLayer) circleLayer;
@property (T@"CAShapeLayer",&,N,V_rotationLayer) rotationLayer;
@property (Tq,N,V_orientation) orientation;
```

## Class methods

```
+[BKUIRotationArrowAnimationLayer animatorByEmbedding:color:radiusForOrientation:];
+[BKUIRotationArrowAnimationLayer animatorWith:color:radiusForOrientation:];
```

## Instance methods

```
-[BKUIRotationArrowAnimationLayer containerSize];
-[BKUIRotationArrowAnimationLayer setOrientation:];
-[BKUIRotationArrowAnimationLayer setColor:];
-[BKUIRotationArrowAnimationLayer setContainerSize:];
-[BKUIRotationArrowAnimationLayer init];
-[BKUIRotationArrowAnimationLayer orientation];
-[BKUIRotationArrowAnimationLayer setRadius:];
-[BKUIRotationArrowAnimationLayer color];
-[BKUIRotationArrowAnimationLayer radius];
-[BKUIRotationArrowAnimationLayer layoutSublayers];
-[BKUIRotationArrowAnimationLayer resetLayout];
-[BKUIRotationArrowAnimationLayer arrowContainer];
-[BKUIRotationArrowAnimationLayer setArrowContainer:];
-[BKUIRotationArrowAnimationLayer circleLayer];
-[BKUIRotationArrowAnimationLayer setCircleLayer:];
-[BKUIRotationArrowAnimationLayer arrowLayerRight];
-[BKUIRotationArrowAnimationLayer setArrowlength:];
-[BKUIRotationArrowAnimationLayer _animateArrowClockwise:duration:animationDelay:];
-[BKUIRotationArrowAnimationLayer _animateArrowCounterClockwise:duration:animationDelay:];
-[BKUIRotationArrowAnimationLayer _animateArrowPaths:delay:duration:];
-[BKUIRotationArrowAnimationLayer _animateArrowUpsideDown:duration:animationDelay:];
-[BKUIRotationArrowAnimationLayer _extendedInit:];
-[BKUIRotationArrowAnimationLayer _landscapeAnimationImpl:duration:animationDelay:];
-[BKUIRotationArrowAnimationLayer _layoutArrowContainer:];
-[BKUIRotationArrowAnimationLayer _layoutArrowSubLayers];
-[BKUIRotationArrowAnimationLayer _resetHideCircleLayerStrokeTo:];
-[BKUIRotationArrowAnimationLayer _rotateRotationLayerBy:startTime:fromDegree:toDegree:];
-[BKUIRotationArrowAnimationLayer _updateCircleLayerLayout:];
-[BKUIRotationArrowAnimationLayer _zeroOutArrowStroke];
-[BKUIRotationArrowAnimationLayer animateDirectionPath:orientation:duration:animationDelay:];
-[BKUIRotationArrowAnimationLayer arrowAngle];
-[BKUIRotationArrowAnimationLayer arrowLayerLeft];
-[BKUIRotationArrowAnimationLayer arrowlength];
-[BKUIRotationArrowAnimationLayer enableDebug:];
-[BKUIRotationArrowAnimationLayer getOrientation];
-[BKUIRotationArrowAnimationLayer hostCenter];
-[BKUIRotationArrowAnimationLayer initWith:radiusForOrientation:arrowAngle:arrowLength:color:];
-[BKUIRotationArrowAnimationLayer rotationLayer];
-[BKUIRotationArrowAnimationLayer setArrowAngle:];
-[BKUIRotationArrowAnimationLayer setArrowLayerLeft:];
-[BKUIRotationArrowAnimationLayer setArrowLayerRight:];
-[BKUIRotationArrowAnimationLayer setGetOrientation:];
-[BKUIRotationArrowAnimationLayer setHostCenter:];
-[BKUIRotationArrowAnimationLayer setRotationLayer:];
-[BKUIRotationArrowAnimationLayer stopAnimationRemoveStroke];
```
