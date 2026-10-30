# `CAGradientLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 0 instance variables, 10 properties, 28 instance methods, 3 class methods

## Properties

```
@property (T@,&) colorMap;
@property (T@"NSArray",C) interpolations;
@property (TB) premultiplied;
@property (T^{CGColorSpace=}) colorSpace;
@property (Td) noiseScale;
@property (T@"NSArray",C) colors;
@property (T@"NSArray",C) locations;
@property (T{CGPoint=dd}) startPoint;
@property (T{CGPoint=dd}) endPoint;
@property (T@"NSString",C) type;
```

## Class methods

```
+[CAGradientLayer defaultValueForKey:];
+[CAGradientLayer _hasRenderLayerSubclass];
+[CAGradientLayer CA_automaticallyNotifiesObservers:];
```

## Instance methods

```
-[CAGradientLayer setColors:];
-[CAGradientLayer colors];
-[CAGradientLayer setLocations:];
-[CAGradientLayer locations];
-[CAGradientLayer didChangeValueForKey:];
-[CAGradientLayer interpolations];
-[CAGradientLayer _copyRenderLayer:layerFlags:commitFlags:];
-[CAGradientLayer setColorSpace:];
-[CAGradientLayer _renderLayerDefinesProperty:];
-[CAGradientLayer _renderLayerPropertyAnimationFlags:];
-[CAGradientLayer setStartPoint:];
-[CAGradientLayer implicitAnimationForKeyPath:];
-[CAGradientLayer startPoint];
-[CAGradientLayer endPoint];
-[CAGradientLayer colorSpace];
-[CAGradientLayer setType:];
-[CAGradientLayer type];
-[CAGradientLayer setPremultiplied:];
-[CAGradientLayer CA_validateValue:forKey:];
-[CAGradientLayer setInterpolations:];
-[CAGradientLayer premultiplied];
-[CAGradientLayer _colorSpaceDidChange];
-[CAGradientLayer _renderBackgroundInContext:];
-[CAGradientLayer colorMap];
-[CAGradientLayer noiseScale];
-[CAGradientLayer setColorMap:];
-[CAGradientLayer setEndPoint:];
-[CAGradientLayer setNoiseScale:];
```
