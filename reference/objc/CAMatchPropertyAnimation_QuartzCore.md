# `CAMatchPropertyAnimation`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAAnimation`
- 0 instance variables, 6 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"CALayer",W) sourceLayer;
@property (TQ) sourceLayerRenderId;
@property (TI) sourceContextId;
@property (T@"NSString",C) keyPath;
@property (TB,GisAdditive) additive;
@property (TB) allowsDeferredSourceTracking;
```

## Instance methods

```
-[CAMatchPropertyAnimation setSourceLayer:];
-[CAMatchPropertyAnimation setSourceContextId:];
-[CAMatchPropertyAnimation sourceLayer];
-[CAMatchPropertyAnimation sourceContextId];
-[CAMatchPropertyAnimation isAdditive];
-[CAMatchPropertyAnimation keyPath];
-[CAMatchPropertyAnimation setKeyPath:];
-[CAMatchPropertyAnimation setAdditive:];
-[CAMatchPropertyAnimation _setCARenderAnimation:layer:];
-[CAMatchPropertyAnimation _propertyFlagsForLayer:];
-[CAMatchPropertyAnimation sourceLayerRenderId];
-[CAMatchPropertyAnimation allowsDeferredSourceTracking];
-[CAMatchPropertyAnimation setSourceLayerRenderId:];
-[CAMatchPropertyAnimation applyForTime:presentationObject:modelObject:];
-[CAMatchPropertyAnimation setAllowsDeferredSourceTracking:];
-[CAMatchPropertyAnimation _copyRenderAnimationForLayer:];
```
