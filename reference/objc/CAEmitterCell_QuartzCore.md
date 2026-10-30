# `CAEmitterCell`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `CAPropertyInfo`, `NSSecureCoding`, `CAMediaTiming`
- 3 instance variables, 56 properties, 132 instance methods, 7 class methods

## Instance variables

```
[2^v] _attr;
^v _state;
I _flags;
```

## Properties

```
@property (T@"NSString",C) particleType;
@property (Td) orientationLatitude;
@property (Td) orientationLongitude;
@property (Td) orientationRange;
@property (Td) rotation;
@property (Td) rotationRange;
@property (Tf) mass;
@property (Tf) massRange;
@property (T@"NSString",C) contentsFrameMode;
@property (TI) contentsFrameCount;
@property (TI) contentsFramesPerRow;
@property (Tf) contentsFramesPerSecond;
@property (T@"NSArray",C) emitterBehaviors;
@property (T@"NSString",C) name;
@property (TB,GisEnabled) enabled;
@property (Tf) birthRate;
@property (Tf) lifetime;
@property (Tf) lifetimeRange;
@property (Td) emissionLatitude;
@property (Td) emissionLongitude;
@property (Td) emissionRange;
@property (Td) velocity;
@property (Td) velocityRange;
@property (Td) xAcceleration;
@property (Td) yAcceleration;
@property (Td) zAcceleration;
@property (Td) scale;
@property (Td) scaleRange;
@property (Td) scaleSpeed;
@property (Td) spin;
@property (Td) spinRange;
@property (T^{CGColor=}) color;
@property (Tf) redRange;
@property (Tf) greenRange;
@property (Tf) blueRange;
@property (Tf) alphaRange;
@property (Tf) redSpeed;
@property (Tf) greenSpeed;
@property (Tf) blueSpeed;
@property (Tf) alphaSpeed;
@property (T@,&) contents;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}}) contentsRect;
@property (Td) contentsScale;
@property (T@"NSString",C) minificationFilter;
@property (T@"NSString",C) magnificationFilter;
@property (Tf) minificationFilterBias;
@property (T@"NSArray",C) emitterCells;
@property (T@"NSDictionary",C) style;
@property (Td) beginTime;
@property (Td) duration;
@property (Tf) speed;
@property (Td) timeOffset;
@property (Tf) repeatCount;
@property (Td) repeatDuration;
@property (TB) autoreverses;
@property (T@"NSString",C) fillMode;
```

## Class methods

```
+[CAEmitterCell supportsSecureCoding];
+[CAEmitterCell properties];
+[CAEmitterCell defaultValueForKey:];
+[CAEmitterCell CA_automaticallyNotifiesObservers:];
+[CAEmitterCell automaticallyNotifiesObserversForKey:];
+[CAEmitterCell CAMLParserStartElement:];
+[CAEmitterCell emitterCell];
```

## Instance methods

```
-[CAEmitterCell setAutoreverses:];
-[CAEmitterCell setColor:];
-[CAEmitterCell setBeginTime:];
-[CAEmitterCell setSpeed:];
-[CAEmitterCell didChangeValueForKey:];
-[CAEmitterCell fillMode];
-[CAEmitterCell setContents:];
-[CAEmitterCell CAMLTypeForKey:];
-[CAEmitterCell setRepeatCount:];
-[CAEmitterCell setFillMode:];
-[CAEmitterCell rotation];
-[CAEmitterCell repeatCount];
-[CAEmitterCell debugDescription];
-[CAEmitterCell contents];
-[CAEmitterCell CAMLParser:setValue:forKey:];
-[CAEmitterCell valueForUndefinedKey:];
-[CAEmitterCell speed];
-[CAEmitterCell setMass:];
-[CAEmitterCell setTimeOffset:];
-[CAEmitterCell repeatDuration];
-[CAEmitterCell dealloc];
-[CAEmitterCell autoreverses];
-[CAEmitterCell contentsScale];
-[CAEmitterCell setScale:];
-[CAEmitterCell velocity];
-[CAEmitterCell setValue:forKeyPath:];
-[CAEmitterCell style];
-[CAEmitterCell timeOffset];
-[CAEmitterCell CA_copyRenderValue];
-[CAEmitterCell setValue:forKey:];
-[CAEmitterCell setStyle:];
-[CAEmitterCell duration];
-[CAEmitterCell isEnabled];
-[CAEmitterCell setRotation:];
-[CAEmitterCell color];
-[CAEmitterCell scale];
-[CAEmitterCell valueForKey:];
-[CAEmitterCell contentsRect];
-[CAEmitterCell shouldArchiveValueForKey:];
-[CAEmitterCell encodeWithCAMLWriter:];
-[CAEmitterCell setContentsScale:];
-[CAEmitterCell setEnabled:];
-[CAEmitterCell CAMLTypeSupportedForKey:];
-[CAEmitterCell setRepeatDuration:];
-[CAEmitterCell encodeWithCoder:];
-[CAEmitterCell setContentsRect:];
-[CAEmitterCell valueForKeyPath:];
-[CAEmitterCell CA_validateValue:forKey:];
-[CAEmitterCell setName:];
-[CAEmitterCell setValue:forUndefinedKey:];
-[CAEmitterCell initWithCoder:];
-[CAEmitterCell mass];
-[CAEmitterCell lifetime];
-[CAEmitterCell setDuration:];
-[CAEmitterCell setVelocity:];
-[CAEmitterCell CA_prepareRenderValue];
-[CAEmitterCell copyWithZone:];
-[CAEmitterCell name];
-[CAEmitterCell beginTime];
-[CAEmitterCell alphaRange];
-[CAEmitterCell alphaSpeed];
-[CAEmitterCell birthRate];
-[CAEmitterCell blueRange];
-[CAEmitterCell blueSpeed];
-[CAEmitterCell contentsFrameCount];
-[CAEmitterCell contentsFrameMode];
-[CAEmitterCell contentsFramesPerRow];
-[CAEmitterCell contentsFramesPerSecond];
-[CAEmitterCell emissionLatitude];
-[CAEmitterCell emissionLongitude];
-[CAEmitterCell emissionRange];
-[CAEmitterCell emitterBehaviors];
-[CAEmitterCell emitterCells];
-[CAEmitterCell greenRange];
-[CAEmitterCell greenSpeed];
-[CAEmitterCell lifetimeRange];
-[CAEmitterCell magnificationFilter];
-[CAEmitterCell massRange];
-[CAEmitterCell minificationFilter];
-[CAEmitterCell minificationFilterBias];
-[CAEmitterCell orientationLatitude];
-[CAEmitterCell orientationLongitude];
-[CAEmitterCell orientationRange];
-[CAEmitterCell particleType];
-[CAEmitterCell redRange];
-[CAEmitterCell redSpeed];
-[CAEmitterCell rotationRange];
-[CAEmitterCell scaleRange];
-[CAEmitterCell scaleSpeed];
-[CAEmitterCell setAlphaRange:];
-[CAEmitterCell setAlphaSpeed:];
-[CAEmitterCell setBirthRate:];
-[CAEmitterCell setBlueRange:];
-[CAEmitterCell setBlueSpeed:];
-[CAEmitterCell setContentsFrameCount:];
-[CAEmitterCell setContentsFrameMode:];
-[CAEmitterCell setContentsFramesPerRow:];
-[CAEmitterCell setContentsFramesPerSecond:];
-[CAEmitterCell setEmissionLatitude:];
-[CAEmitterCell setEmissionLongitude:];
-[CAEmitterCell setEmissionRange:];
-[CAEmitterCell setEmitterBehaviors:];
-[CAEmitterCell setEmitterCells:];
-[CAEmitterCell setGreenRange:];
-[CAEmitterCell setGreenSpeed:];
-[CAEmitterCell setLifetime:];
-[CAEmitterCell setLifetimeRange:];
-[CAEmitterCell setMagnificationFilter:];
-[CAEmitterCell setMassRange:];
-[CAEmitterCell setMinificationFilter:];
-[CAEmitterCell setMinificationFilterBias:];
-[CAEmitterCell setOrientationLatitude:];
-[CAEmitterCell setOrientationLongitude:];
-[CAEmitterCell setOrientationRange:];
-[CAEmitterCell setParticleType:];
-[CAEmitterCell setRedRange:];
-[CAEmitterCell setRedSpeed:];
-[CAEmitterCell setRotationRange:];
-[CAEmitterCell setScaleRange:];
-[CAEmitterCell setScaleSpeed:];
-[CAEmitterCell setSpin:];
-[CAEmitterCell setSpinRange:];
-[CAEmitterCell setVelocityRange:];
-[CAEmitterCell setXAcceleration:];
-[CAEmitterCell setYAcceleration:];
-[CAEmitterCell setZAcceleration:];
-[CAEmitterCell spin];
-[CAEmitterCell spinRange];
-[CAEmitterCell velocityRange];
-[CAEmitterCell xAcceleration];
-[CAEmitterCell yAcceleration];
-[CAEmitterCell zAcceleration];
```
