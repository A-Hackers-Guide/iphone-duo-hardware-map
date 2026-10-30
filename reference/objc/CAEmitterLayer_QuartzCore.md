# `CAEmitterLayer`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 0 instance variables, 24 properties, 56 instance methods, 3 class methods

## Properties

```
@property (T^{CGPath=}) emitterPath;
@property (T@"NSArray",C) emitterRects;
@property (Tf) emitterDuration;
@property (Tf) spinBias;
@property (T@"NSArray",C) emitterBehaviors;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}}) cullRect;
@property (Td) cullMinZ;
@property (Td) cullMaxZ;
@property (Td) updateInterval;
@property (T@"NSArray",C) emitterCells;
@property (Tf) birthRate;
@property (Tf) lifetime;
@property (T{CGPoint=dd}) emitterPosition;
@property (Td) emitterZPosition;
@property (T{CGSize=dd}) emitterSize;
@property (Td) emitterDepth;
@property (T@"NSString",C) emitterShape;
@property (T@"NSString",C) emitterMode;
@property (T@"NSString",C) renderMode;
@property (TB) preservesDepth;
@property (Tf) velocity;
@property (Tf) scale;
@property (Tf) spin;
@property (TI) seed;
```

## Class methods

```
+[CAEmitterLayer defaultValueForKey:];
+[CAEmitterLayer _hasRenderLayerSubclass];
+[CAEmitterLayer CA_automaticallyNotifiesObservers:];
```

## Instance methods

```
-[CAEmitterLayer reloadValueForKeyPath:];
-[CAEmitterLayer preservesDepth];
-[CAEmitterLayer seed];
-[CAEmitterLayer didChangeValueForKey:];
-[CAEmitterLayer _copyRenderLayer:layerFlags:commitFlags:];
-[CAEmitterLayer _renderLayerDefinesProperty:];
-[CAEmitterLayer _renderLayerPropertyAnimationFlags:];
-[CAEmitterLayer setPreservesDepth:];
-[CAEmitterLayer implicitAnimationForKeyPath:];
-[CAEmitterLayer setScale:];
-[CAEmitterLayer velocity];
-[CAEmitterLayer scale];
-[CAEmitterLayer setUpdateInterval:];
-[CAEmitterLayer renderMode];
-[CAEmitterLayer CA_validateValue:forKey:];
-[CAEmitterLayer lifetime];
-[CAEmitterLayer setVelocity:];
-[CAEmitterLayer setRenderMode:];
-[CAEmitterLayer updateInterval];
-[CAEmitterLayer emitterPosition];
-[CAEmitterLayer setEmitterMode:];
-[CAEmitterLayer setEmitterSize:];
-[CAEmitterLayer emitterDuration];
-[CAEmitterLayer setEmitterPath:];
-[CAEmitterLayer _colorSpaceDidChange];
-[CAEmitterLayer birthRate];
-[CAEmitterLayer cullMaxZ];
-[CAEmitterLayer cullMinZ];
-[CAEmitterLayer cullRect];
-[CAEmitterLayer emitterBehaviors];
-[CAEmitterLayer emitterCells];
-[CAEmitterLayer emitterDepth];
-[CAEmitterLayer emitterMode];
-[CAEmitterLayer emitterPath];
-[CAEmitterLayer emitterRects];
-[CAEmitterLayer emitterShape];
-[CAEmitterLayer emitterSize];
-[CAEmitterLayer emitterZPosition];
-[CAEmitterLayer setBirthRate:];
-[CAEmitterLayer setCullMaxZ:];
-[CAEmitterLayer setCullMinZ:];
-[CAEmitterLayer setCullRect:];
-[CAEmitterLayer setEmitterBehaviors:];
-[CAEmitterLayer setEmitterCells:];
-[CAEmitterLayer setEmitterDepth:];
-[CAEmitterLayer setEmitterDuration:];
-[CAEmitterLayer setEmitterPosition:];
-[CAEmitterLayer setEmitterRects:];
-[CAEmitterLayer setEmitterShape:];
-[CAEmitterLayer setEmitterZPosition:];
-[CAEmitterLayer setLifetime:];
-[CAEmitterLayer setSeed:];
-[CAEmitterLayer setSpin:];
-[CAEmitterLayer setSpinBias:];
-[CAEmitterLayer spin];
-[CAEmitterLayer spinBias];
```
