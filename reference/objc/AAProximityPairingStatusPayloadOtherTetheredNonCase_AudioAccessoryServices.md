# `AAProximityPairingStatusPayloadOtherTetheredNonCase`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AAProximityPairingStatusPayloadGeneral`
- Protocols: `AATetheredProximityPairingPayload`
- 2 instance variables, 14 properties, 9 instance methods, 1 class methods

## Instance variables

```
C _lidOpenCount;
B _showProxStatus;
```

## Properties

```
@property (TC,R) primaryLocation;
@property (TB,R) outOfBoxMode;
@property (TC,R,V_lidOpenCount) lidOpenCount;
@property (TB,R,V_showProxStatus) showProxStatus;
@property (TC,R) color;
@property (TB,R) mainBatteryValid;
@property (TC,R) mainBatteryLevel;
@property (TB,R) mainBatteryCharging;
@property (TB,R) chargingDEOC;
@property (TB,R) chargingOBC;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AAProximityPairingStatusPayloadOtherTetheredNonCase supportedPID:];
```

## Instance methods

```
-[AAProximityPairingStatusPayloadOtherTetheredNonCase color];
-[AAProximityPairingStatusPayloadOtherTetheredNonCase describeProperties];
-[AAProximityPairingStatusPayloadOtherTetheredNonCase primaryLocation];
-[AAProximityPairingStatusPayloadOtherTetheredNonCase lidOpenCount];
-[AAProximityPairingStatusPayloadOtherTetheredNonCase mainBatteryCharging];
-[AAProximityPairingStatusPayloadOtherTetheredNonCase mainBatteryLevel];
-[AAProximityPairingStatusPayloadOtherTetheredNonCase mainBatteryValid];
-[AAProximityPairingStatusPayloadOtherTetheredNonCase outOfBoxMode];
-[AAProximityPairingStatusPayloadOtherTetheredNonCase showProxStatus];
```
