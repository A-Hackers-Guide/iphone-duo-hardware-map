# `CAShapeLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 0 instance variables, 12 properties, 31 instance methods, 3 class methods

## Properties

```
@property (T^{CGPath=}) path;
@property (T^{CGColor=}) fillColor;
@property (T@"NSString",C) fillRule;
@property (T^{CGColor=}) strokeColor;
@property (Td) strokeStart;
@property (Td) strokeEnd;
@property (Td) lineWidth;
@property (Td) miterLimit;
@property (T@"NSString",C) lineCap;
@property (T@"NSString",C) lineJoin;
@property (Td) lineDashPhase;
@property (T@"NSArray",C) lineDashPattern;
```

## Class methods

```
+[CAShapeLayer defaultValueForKey:];
+[CAShapeLayer _hasRenderLayerSubclass];
+[CAShapeLayer CA_automaticallyNotifiesObservers:];
```

## Instance methods

```
-[CAShapeLayer _renderForegroundInContext:];
-[CAShapeLayer lineWidth];
-[CAShapeLayer lineCap];
-[CAShapeLayer lineJoin];
-[CAShapeLayer setLineWidth:];
-[CAShapeLayer didChangeValueForKey:];
-[CAShapeLayer _copyRenderLayer:layerFlags:commitFlags:];
-[CAShapeLayer setFillColor:];
-[CAShapeLayer _renderLayerDefinesProperty:];
-[CAShapeLayer fillColor];
-[CAShapeLayer _renderLayerPropertyAnimationFlags:];
-[CAShapeLayer implicitAnimationForKeyPath:];
-[CAShapeLayer setStrokeColor:];
-[CAShapeLayer strokeColor];
-[CAShapeLayer setPath:];
-[CAShapeLayer path];
-[CAShapeLayer miterLimit];
-[CAShapeLayer setLineCap:];
-[CAShapeLayer setLineJoin:];
-[CAShapeLayer setMiterLimit:];
-[CAShapeLayer lineDashPattern];
-[CAShapeLayer setStrokeStart:];
-[CAShapeLayer _colorSpaceDidChange];
-[CAShapeLayer fillRule];
-[CAShapeLayer lineDashPhase];
-[CAShapeLayer setFillRule:];
-[CAShapeLayer setLineDashPattern:];
-[CAShapeLayer setLineDashPhase:];
-[CAShapeLayer setStrokeEnd:];
-[CAShapeLayer strokeEnd];
-[CAShapeLayer strokeStart];
```
