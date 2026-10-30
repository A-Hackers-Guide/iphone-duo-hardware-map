# `CLBeacon`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 1 instance variables, 8 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"CLBeaconInternal" _internal;
```

## Properties

```
@property (T@"NSDate",R,C,N) timestamp;
@property (T@"NSUUID",R,C,N) UUID;
@property (T@"NSUUID",R,C,N) proximityUUID;
@property (T@"NSNumber",R,C,N) major;
@property (T@"NSNumber",R,C,N) minor;
@property (Tq,R,N) proximity;
@property (Td,R,N) accuracy;
@property (Tq,R,N) rssi;
```

## Class methods

```
+[CLBeacon supportsSecureCoding];
```

## Instance methods

```
-[CLBeacon rssi];
-[CLBeacon major];
-[CLBeacon proximity];
-[CLBeacon UUID];
-[CLBeacon dealloc];
-[CLBeacon timestamp];
-[CLBeacon referenceFrame];
-[CLBeacon accuracy];
-[CLBeacon minor];
-[CLBeacon encodeWithCoder:];
-[CLBeacon description];
-[CLBeacon initWithCoder:];
-[CLBeacon copyWithZone:];
-[CLBeacon setReferenceFrame:];
-[CLBeacon proximityUUID];
-[CLBeacon initWithProximityUUID:major:minor:proximity:accuracy:rssi:];
-[CLBeacon initWithUUID:major:minor:proximity:accuracy:rssi:timestamp:];
```
