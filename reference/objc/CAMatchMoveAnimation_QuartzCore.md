# `CAMatchMoveAnimation`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAAnimation`
- 0 instance variables, 13 properties, 31 instance methods, 1 class methods

## Properties

```
@property (T@"CALayer",W) sourceLayer;
@property (TQ) sourceLayerRenderId;
@property (TI) sourceContextId;
@property (T@"NSString",C) keyPath;
@property (TB) targetsSuperlayer;
@property (T@"NSArray",C) sourcePoints;
@property (TB) usesNormalizedCoordinates;
@property (TB) appliesX;
@property (TB) appliesY;
@property (TB) appliesScale;
@property (TB) appliesRotation;
@property (TB,GisAdditive) additive;
@property (TB) allowsDeferredSourceTracking;
```

## Class methods

```
+[CAMatchMoveAnimation defaultValueForKey:];
```

## Instance methods

```
-[CAMatchMoveAnimation setSourceLayer:];
-[CAMatchMoveAnimation setSourceContextId:];
-[CAMatchMoveAnimation sourceLayer];
-[CAMatchMoveAnimation sourceContextId];
-[CAMatchMoveAnimation isAdditive];
-[CAMatchMoveAnimation keyPath];
-[CAMatchMoveAnimation setKeyPath:];
-[CAMatchMoveAnimation setAdditive:];
-[CAMatchMoveAnimation _setCARenderAnimation:layer:];
-[CAMatchMoveAnimation appliesRotation];
-[CAMatchMoveAnimation appliesX];
-[CAMatchMoveAnimation sourcePoints];
-[CAMatchMoveAnimation usesNormalizedCoordinates];
-[CAMatchMoveAnimation setAppliesScale:];
-[CAMatchMoveAnimation _propertyFlagsForLayer:];
-[CAMatchMoveAnimation setAppliesY:];
-[CAMatchMoveAnimation setAppliesRotation:];
-[CAMatchMoveAnimation sourceLayerRenderId];
-[CAMatchMoveAnimation targetsSuperlayer];
-[CAMatchMoveAnimation allowsDeferredSourceTracking];
-[CAMatchMoveAnimation setSourceLayerRenderId:];
-[CAMatchMoveAnimation setSourcePoints:];
-[CAMatchMoveAnimation CA_validateValue:forKey:];
-[CAMatchMoveAnimation setAppliesX:];
-[CAMatchMoveAnimation applyForTime:presentationObject:modelObject:];
-[CAMatchMoveAnimation setAllowsDeferredSourceTracking:];
-[CAMatchMoveAnimation setTargetsSuperlayer:];
-[CAMatchMoveAnimation appliesScale];
-[CAMatchMoveAnimation appliesY];
-[CAMatchMoveAnimation setUsesNormalizedCoordinates:];
-[CAMatchMoveAnimation _copyRenderAnimationForLayer:];
```
