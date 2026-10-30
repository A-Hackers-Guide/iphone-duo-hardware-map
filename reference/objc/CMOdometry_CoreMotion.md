# `CMOdometry`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 22 instance variables, 22 properties, 34 instance methods, 1 class methods

## Instance variables

```
B _buffered;
B _isDOTBiasChangePossible;
B _isMounted;
B _isZUPT;
f _rotationArbitraryToTrueNorth;
@"NSNumber" _deltaPositionX;
@"NSNumber" _deltaPositionY;
@"NSNumber" _deltaPositionZ;
@"NSNumber" _deltaVelocityX;
@"NSNumber" _deltaVelocityY;
@"NSNumber" _deltaVelocityZ;
@"NSNumber" _quaternionX;
@"NSNumber" _quaternionY;
@"NSNumber" _quaternionZ;
@"NSNumber" _quaternionW;
Q _referenceFrame;
q _staticFlag;
@"NSNumber" _deltaPositionUncertaintyX;
@"NSNumber" _deltaPositionUncertaintyY;
@"NSNumber" _deltaPositionUncertaintyZ;
q _deviceLocation;
q _dataSource;
```

## Properties

```
@property (TB,R,N,V_isDOTBiasChangePossible) isDOTBiasChangePossible;
@property (TB,R,N,V_isMounted) isMounted;
@property (TB,R,N,V_isZUPT) isZUPT;
@property (T@"NSNumber",R,N,V_deltaPositionX) deltaPositionX;
@property (T@"NSNumber",R,N,V_deltaPositionY) deltaPositionY;
@property (T@"NSNumber",R,N,V_deltaPositionZ) deltaPositionZ;
@property (T@"NSNumber",R,N,V_deltaVelocityX) deltaVelocityX;
@property (T@"NSNumber",R,N,V_deltaVelocityY) deltaVelocityY;
@property (T@"NSNumber",R,N,V_deltaVelocityZ) deltaVelocityZ;
@property (T@"NSNumber",R,N,V_quaternionX) quaternionX;
@property (T@"NSNumber",R,N,V_quaternionY) quaternionY;
@property (T@"NSNumber",R,N,V_quaternionZ) quaternionZ;
@property (T@"NSNumber",R,N,V_quaternionW) quaternionW;
@property (TQ,R,N,V_referenceFrame) referenceFrame;
@property (Tf,R,N,V_rotationArbitraryToTrueNorth) rotationArbitraryToTrueNorth;
@property (Tq,R,N,V_staticFlag) staticFlag;
@property (T@"NSNumber",R,N,V_deltaPositionUncertaintyX) deltaPositionUncertaintyX;
@property (T@"NSNumber",R,N,V_deltaPositionUncertaintyY) deltaPositionUncertaintyY;
@property (T@"NSNumber",R,N,V_deltaPositionUncertaintyZ) deltaPositionUncertaintyZ;
@property (Tq,R,N,V_deviceLocation) deviceLocation;
@property (TB,R,N,GisBuffered,V_buffered) buffered;
@property (Tq,R,N,V_dataSource) dataSource;
```

## Class methods

```
+[CMOdometry supportsSecureCoding];
```

## Instance methods

```
-[CMOdometry quaternionW];
-[CMOdometry isMounted];
-[CMOdometry quaternionZ];
-[CMOdometry deltaPositionY];
-[CMOdometry quaternionY];
-[CMOdometry deltaPositionX];
-[CMOdometry deltaPositionZ];
-[CMOdometry deviceLocation];
-[CMOdometry rotateArbitraryToTrueNorth];
-[CMOdometry initWithDeltaPositionX:deltaPositionY:deltaPositionZ:deltaVelocityX:deltaVelocityY:deltaVelocityZ:quaternionX:quaternionY:quaternionZ:quaternionW:rotationArbitraryToTrueNorth:staticFlag:dataSource:timestamp:continuousTimestamp:];
-[CMOdometry deltaVelocityZ];
-[CMOdometry dealloc];
-[CMOdometry referenceFrame];
-[CMOdometry deltaPositionUncertaintyY];
-[CMOdometry deltaVelocityX];
-[CMOdometry isDOTBiasChangePossible];
-[CMOdometry initWithDeltaPositionX:deltaPositionY:deltaPositionZ:deltaVelocityX:deltaVelocityY:deltaVelocityZ:quaternionX:quaternionY:quaternionZ:quaternionW:rotationArbitraryToTrueNorth:staticFlag:isDOTBiasChangePossible:isMounted:isZUPT:timestamp:continuousTimestamp:];
-[CMOdometry isZUPT];
-[CMOdometry initWithDeltaPositionX:deltaPositionY:deltaPositionZ:deltaVelocityX:deltaVelocityY:deltaVelocityZ:quaternionX:quaternionY:quaternionZ:quaternionW:timestamp:continuousTimestamp:];
-[CMOdometry dataSource];
-[CMOdometry quaternionX];
-[CMOdometry deltaPositionUncertaintyZ];
-[CMOdometry encodeWithCoder:];
-[CMOdometry rotationArbitraryToTrueNorth];
-[CMOdometry deltaVelocityY];
-[CMOdometry description];
-[CMOdometry initWithCoder:];
-[CMOdometry initWithDeltaPositionX:deltaPositionY:deltaPositionZ:deltaVelocityX:deltaVelocityY:deltaVelocityZ:quaternionX:quaternionY:quaternionZ:quaternionW:rotationArbitraryToTrueNorth:staticFlag:deltaPositionUncertaintyX:deltaPositionUncertaintyY:deltaPositionUncertaintyZ:deviceLocation:buffered:dataSource:timestamp:continuousTimestamp:];
-[CMOdometry copyWithZone:];
-[CMOdometry initWithDeltaPositionX:deltaPositionY:deltaPositionZ:deltaVelocityX:deltaVelocityY:deltaVelocityZ:quaternionX:quaternionY:quaternionZ:quaternionW:rotationArbitraryToTrueNorth:staticFlag:isDOTBiasChangePossible:isMounted:isZUPT:dataSource:timestamp:continuousTimestamp:];
-[CMOdometry initWithDeltaPositionX:deltaPositionY:deltaPositionZ:deltaVelocityX:deltaVelocityY:deltaVelocityZ:quaternionX:quaternionY:quaternionZ:quaternionW:rotationArbitraryToTrueNorth:staticFlag:isDOTBiasChangePossible:isMounted:isZUPT:deltaPositionUncertaintyX:deltaPositionUncertaintyY:deltaPositionUncertaintyZ:deviceLocation:buffered:dataSource:timestamp:continuousTimestamp:];
-[CMOdometry deltaPositionUncertaintyX];
-[CMOdometry isBuffered];
-[CMOdometry staticFlag];
```
