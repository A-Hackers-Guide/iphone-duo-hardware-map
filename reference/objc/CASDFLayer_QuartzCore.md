# `CASDFLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 0 instance variables, 6 properties, 17 instance methods, 3 class methods

## Properties

```
@property (T@"CASDFEffect",&) effect;
@property (Td) smoothness;
@property (Td) gaussianRadius;
@property (Td) effectOffset;
@property (TB) mergeElements;
@property (TB) experimentalCulling;
```

## Class methods

```
+[CASDFLayer defaultValueForKey:];
+[CASDFLayer _hasRenderLayerSubclass];
+[CASDFLayer CA_automaticallyNotifiesObservers:];
```

## Instance methods

```
-[CASDFLayer reloadValueForKeyPath:];
-[CASDFLayer setGaussianRadius:];
-[CASDFLayer setExperimentalCulling:];
-[CASDFLayer setMergeElements:];
-[CASDFLayer mergeElements];
-[CASDFLayer effectOffset];
-[CASDFLayer smoothness];
-[CASDFLayer gaussianRadius];
-[CASDFLayer setSmoothness:];
-[CASDFLayer didChangeValueForKey:];
-[CASDFLayer _copyRenderLayer:layerFlags:commitFlags:];
-[CASDFLayer experimentalCulling];
-[CASDFLayer _renderLayerDefinesProperty:];
-[CASDFLayer initWithLayer:];
-[CASDFLayer effect];
-[CASDFLayer setEffect:];
-[CASDFLayer setEffectOffset:];
```
