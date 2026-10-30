# `CMAltitudeData`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 1 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
@ _internal;
```

## Properties

```
@property (T@"NSNumber",R,N) relativeAltitude;
@property (T@"NSNumber",R,N) pressure;
```

## Class methods

```
+[CMAltitudeData supportsSecureCoding];
```

## Instance methods

```
-[CMAltitudeData dealloc];
-[CMAltitudeData pressure];
-[CMAltitudeData encodeWithCoder:];
-[CMAltitudeData description];
-[CMAltitudeData initWithCoder:];
-[CMAltitudeData copyWithZone:];
-[CMAltitudeData initWithAltitude:andTimestamp:atBaseAltitude:];
-[CMAltitudeData initWithTimestamp:pressure:relativeAltitude:];
-[CMAltitudeData relativeAltitude];
```
