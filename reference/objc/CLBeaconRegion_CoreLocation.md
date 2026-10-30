# `CLBeaconRegion`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CLRegion`
- 5 instance variables, 7 properties, 28 instance methods, 2 class methods

## Instance variables

```
B _notifyEntryStateOnDisplay;
i _definitionMask;
@"NSUUID" _UUID;
@"NSNumber" _major;
@"NSNumber" _minor;
```

## Properties

```
@property (Ti,R,N,V_definitionMask) definitionMask;
@property (T@"CLBeaconIdentityConstraint",R,C,N) beaconIdentityConstraint;
@property (T@"NSUUID",R,C,N,V_UUID) UUID;
@property (T@"NSUUID",R,C,N) proximityUUID;
@property (T@"NSNumber",R,C,N,V_major) major;
@property (T@"NSNumber",R,C,N,V_minor) minor;
@property (TB,V_notifyEntryStateOnDisplay) notifyEntryStateOnDisplay;
```

## Class methods

```
+[CLBeaconRegion supportsSecureCoding];
+[CLBeaconRegion any];
```

## Instance methods

```
-[CLBeaconRegion major];
-[CLBeaconRegion init];
-[CLBeaconRegion UUID];
-[CLBeaconRegion dealloc];
-[CLBeaconRegion minor];
-[CLBeaconRegion encodeWithCoder:];
-[CLBeaconRegion hash];
-[CLBeaconRegion description];
-[CLBeaconRegion initWithCoder:];
-[CLBeaconRegion copyWithZone:];
-[CLBeaconRegion isEqual:];
-[CLBeaconRegion initWithIdentifier:];
-[CLBeaconRegion proximityUUID];
-[CLBeaconRegion _measuredPowerForDevice];
-[CLBeaconRegion beaconIdentityConstraint];
-[CLBeaconRegion definitionMask];
-[CLBeaconRegion initWithBeaconIdentityConstraint:identifier:];
-[CLBeaconRegion initWithProximityUUID:identifier:];
-[CLBeaconRegion initWithProximityUUID:major:identifier:];
-[CLBeaconRegion initWithProximityUUID:major:minor:identifier:];
-[CLBeaconRegion initWithUUID:identifier:];
-[CLBeaconRegion initWithUUID:major:identifier:];
-[CLBeaconRegion initWithUUID:major:minor:identifier:];
-[CLBeaconRegion initWithUUID:major:minor:identifier:notifyEntryStateOnDisplay:];
-[CLBeaconRegion notifyEntryStateOnDisplay];
-[CLBeaconRegion peripheralDataWithMeasuredPower:];
-[CLBeaconRegion setGutsWithProximityUUID:major:minor:notifyOnDisplay:];
-[CLBeaconRegion setNotifyEntryStateOnDisplay:];
```
