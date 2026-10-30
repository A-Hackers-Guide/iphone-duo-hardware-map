# `CLBeaconIdentityCondition`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CLCondition`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"NSUUID" _UUID;
@"NSNumber" _major;
@"NSNumber" _minor;
```

## Properties

```
@property (T@"NSUUID",C,N,V_UUID) UUID;
@property (T@"NSNumber",R,C,N,V_major) major;
@property (T@"NSNumber",R,C,N,V_minor) minor;
```

## Class methods

```
+[CLBeaconIdentityCondition supportsSecureCoding];
+[CLBeaconIdentityCondition any];
```

## Instance methods

```
-[CLBeaconIdentityCondition major];
-[CLBeaconIdentityCondition init];
-[CLBeaconIdentityCondition setUUID:];
-[CLBeaconIdentityCondition initWithUUID:];
-[CLBeaconIdentityCondition UUID];
-[CLBeaconIdentityCondition dealloc];
-[CLBeaconIdentityCondition minor];
-[CLBeaconIdentityCondition encodeWithCoder:];
-[CLBeaconIdentityCondition hash];
-[CLBeaconIdentityCondition description];
-[CLBeaconIdentityCondition initWithCoder:];
-[CLBeaconIdentityCondition copyWithZone:];
-[CLBeaconIdentityCondition isEqual:];
-[CLBeaconIdentityCondition _initWithUUID:major:minor:];
-[CLBeaconIdentityCondition initWithUUID:major:];
-[CLBeaconIdentityCondition initWithUUID:major:minor:];
```
