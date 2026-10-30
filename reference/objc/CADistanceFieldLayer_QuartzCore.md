# `CADistanceFieldLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 0 instance variables, 6 properties, 18 instance methods, 3 class methods

## Properties

```
@property (T@"NSString",C) renderMode;
@property (TB) invertsShape;
@property (T^{CGColor=}) foregroundColor;
@property (Td) offset;
@property (Td) sharpness;
@property (Td) lineWidth;
```

## Class methods

```
+[CADistanceFieldLayer defaultValueForKey:];
+[CADistanceFieldLayer _hasRenderLayerSubclass];
+[CADistanceFieldLayer CA_automaticallyNotifiesObservers:];
```

## Instance methods

```
-[CADistanceFieldLayer setForegroundColor:];
-[CADistanceFieldLayer lineWidth];
-[CADistanceFieldLayer setLineWidth:];
-[CADistanceFieldLayer didChangeValueForKey:];
-[CADistanceFieldLayer _copyRenderLayer:layerFlags:commitFlags:];
-[CADistanceFieldLayer _renderLayerDefinesProperty:];
-[CADistanceFieldLayer _renderImageCopyFlags];
-[CADistanceFieldLayer _renderLayerPropertyAnimationFlags:];
-[CADistanceFieldLayer sharpness];
-[CADistanceFieldLayer renderMode];
-[CADistanceFieldLayer setOffset:];
-[CADistanceFieldLayer foregroundColor];
-[CADistanceFieldLayer setRenderMode:];
-[CADistanceFieldLayer offset];
-[CADistanceFieldLayer _colorSpaceDidChange];
-[CADistanceFieldLayer invertsShape];
-[CADistanceFieldLayer setInvertsShape:];
-[CADistanceFieldLayer setSharpness:];
```
