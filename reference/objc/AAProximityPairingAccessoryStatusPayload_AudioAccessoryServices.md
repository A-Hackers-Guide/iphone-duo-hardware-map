# `AAProximityPairingAccessoryStatusPayload`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AAProximityPairingPayload`
- Protocols: `AAUntetheredProximityPairingPayload`
- 8 instance variables, 30 properties, 28 instance methods, 0 class methods

## Instance variables

```
C _statusFlags1;
C _battery1;
C _battery2;
C _battery3;
C _timeUntilCharged;
C _status2;
C _reserved;
I _firmwareVersionRaw;
```

## Properties

```
@property (TC,R,V_statusFlags1) statusFlags1;
@property (TC,R) lidOpenCount;
@property (TB,R) lidClosed;
@property (TB,R) needsConnection;
@property (TB,R) soundEnabled;
@property (TB,R) connected;
@property (TB,R) faultDetected;
@property (TC,R,V_battery1) battery1;
@property (TB,R) caseBatteryValid;
@property (TC,R) caseBatteryLevel;
@property (TB,R) caseBatteryCharging;
@property (TC,R,V_battery2) battery2;
@property (TB,R) leftBatteryValid;
@property (TC,R) leftBatteryLevel;
@property (TB,R) leftBatteryCharging;
@property (TC,R,V_battery3) battery3;
@property (TB,R) rightBatteryValid;
@property (TC,R) rightBatteryLevel;
@property (TB,R) rightBatteryCharging;
@property (TI,R,V_firmwareVersionRaw) firmwareVersionRaw;
@property (T@"NSString",R,N) firmwareVersion;
@property (TC,R,V_timeUntilCharged) timeUntilCharged;
@property (TB,R) chargingOBC;
@property (TC,R,V_status2) status2;
@property (TB,R) chargingDEOC;
@property (TC,R,V_reserved) reserved;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AAProximityPairingAccessoryStatusPayload connected];
-[AAProximityPairingAccessoryStatusPayload leftBatteryLevel];
-[AAProximityPairingAccessoryStatusPayload firmwareVersion];
-[AAProximityPairingAccessoryStatusPayload reserved];
-[AAProximityPairingAccessoryStatusPayload rightBatteryLevel];
-[AAProximityPairingAccessoryStatusPayload caseBatteryLevel];
-[AAProximityPairingAccessoryStatusPayload initWithData:];
-[AAProximityPairingAccessoryStatusPayload status2];
-[AAProximityPairingAccessoryStatusPayload describeProperties];
-[AAProximityPairingAccessoryStatusPayload needsConnection];
-[AAProximityPairingAccessoryStatusPayload battery1];
-[AAProximityPairingAccessoryStatusPayload battery2];
-[AAProximityPairingAccessoryStatusPayload battery3];
-[AAProximityPairingAccessoryStatusPayload caseBatteryCharging];
-[AAProximityPairingAccessoryStatusPayload caseBatteryValid];
-[AAProximityPairingAccessoryStatusPayload chargingDEOC];
-[AAProximityPairingAccessoryStatusPayload chargingOBC];
-[AAProximityPairingAccessoryStatusPayload faultDetected];
-[AAProximityPairingAccessoryStatusPayload firmwareVersionRaw];
-[AAProximityPairingAccessoryStatusPayload leftBatteryCharging];
-[AAProximityPairingAccessoryStatusPayload leftBatteryValid];
-[AAProximityPairingAccessoryStatusPayload lidClosed];
-[AAProximityPairingAccessoryStatusPayload lidOpenCount];
-[AAProximityPairingAccessoryStatusPayload rightBatteryCharging];
-[AAProximityPairingAccessoryStatusPayload rightBatteryValid];
-[AAProximityPairingAccessoryStatusPayload soundEnabled];
-[AAProximityPairingAccessoryStatusPayload statusFlags1];
-[AAProximityPairingAccessoryStatusPayload timeUntilCharged];
```
