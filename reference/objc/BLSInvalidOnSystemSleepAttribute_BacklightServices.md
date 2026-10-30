# `BLSInvalidOnSystemSleepAttribute`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSAttribute`
- 1 instance variables, 1 properties, 11 instance methods, 3 class methods

## Instance variables

```
d _minimumActiveInterval;
```

## Properties

```
@property (Td,R,N,V_minimumActiveInterval) minimumActiveInterval;
```

## Class methods

```
+[BLSInvalidOnSystemSleepAttribute supportsSecureCoding];
+[BLSInvalidOnSystemSleepAttribute invalidateOnSystemSleep];
+[BLSInvalidOnSystemSleepAttribute invalidateOnSystemSleepAfterMinimumActiveInterval:];
```

## Instance methods

```
-[BLSInvalidOnSystemSleepAttribute initWithXPCDictionary:];
-[BLSInvalidOnSystemSleepAttribute encodeWithXPCDictionary:];
-[BLSInvalidOnSystemSleepAttribute encodeWithCoder:];
-[BLSInvalidOnSystemSleepAttribute hash];
-[BLSInvalidOnSystemSleepAttribute description];
-[BLSInvalidOnSystemSleepAttribute initWithCoder:];
-[BLSInvalidOnSystemSleepAttribute copyWithZone:];
-[BLSInvalidOnSystemSleepAttribute isEqual:];
-[BLSInvalidOnSystemSleepAttribute canBePaused];
-[BLSInvalidOnSystemSleepAttribute minimumActiveInterval];
-[BLSInvalidOnSystemSleepAttribute initWithMinimumActiveInterval:];
```
