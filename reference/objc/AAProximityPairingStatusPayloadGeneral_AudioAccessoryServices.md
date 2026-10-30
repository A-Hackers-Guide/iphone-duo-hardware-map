# `AAProximityPairingStatusPayloadGeneral`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AAProximityPairingPayload`
- 14 instance variables, 35 properties, 38 instance methods, 2 class methods

## Instance variables

```
C _status1;
C _battery1;
C _battery2;
C _status3;
C _colorRaw;
C _misc1;
C _status2;
C _battery3;
C _battery4;
C _battery5;
C _status4;
C _status5;
@"NSData" _lastConnectedHost;
@"NSData" _lastBudInCaseWithCurrentBud;
```

## Properties

```
@property (TC,R,V_status1) status1;
@property (TC,R,V_battery1) battery1;
@property (TC,R,V_battery2) battery2;
@property (TB,R) supportWirelessSplitter;
@property (TC,R,V_status3) status3;
@property (TC,R,V_colorRaw) colorRaw;
@property (TC,R) colorBest;
@property (TC,R,V_misc1) misc1;
@property (TC,R,V_status2) status2;
@property (TC,R) audioState;
@property (TC,R) connectedSourceCount;
@property (TB,R) chargingDEOC;
@property (TB,R) chargingOBC;
@property (TB,R) smartRoutingConnected;
@property (TC,R,V_battery3) battery3;
@property (TB,R) myBatteryValid;
@property (TC,R) myBatteryLevel;
@property (TB,R) myBatteryCharging;
@property (TC,R,V_battery4) battery4;
@property (TB,R) otherBatteryValid;
@property (TC,R) otherBatteryLevel;
@property (TB,R) otherBatteryCharging;
@property (TC,R,V_battery5) battery5;
@property (TB,R) caseBatteryValid;
@property (TC,R) caseBatteryLevel;
@property (TB,R) caseBatteryCharging;
@property (T@"NSData",R,C,N,V_lastConnectedHost) lastConnectedHost;
@property (T@"NSData",R,C,N,V_lastBudInCaseWithCurrentBud) lastBudInCaseWithCurrentBud;
@property (TC,R,V_status4) status4;
@property (TC,R) smartRoutingScoreSource1;
@property (TC,R) smartRoutingScoreSource2;
@property (TC,R,V_status5) status5;
@property (TC,R) idleTime;
@property (TC,R) outOfCaseTime;
@property (TB,R) lastConnectedHostSignedInToICloud;
```

## Class methods

```
+[AAProximityPairingStatusPayloadGeneral proximityPairingStatusPayloadWithData:pid:];
+[AAProximityPairingStatusPayloadGeneral supportedPID:];
```

## Instance methods

```
-[AAProximityPairingStatusPayloadGeneral caseBatteryLevel];
-[AAProximityPairingStatusPayloadGeneral idleTime];
-[AAProximityPairingStatusPayloadGeneral initWithData:];
-[AAProximityPairingStatusPayloadGeneral status2];
-[AAProximityPairingStatusPayloadGeneral audioState];
-[AAProximityPairingStatusPayloadGeneral describeProperties];
-[AAProximityPairingStatusPayloadGeneral status4];
-[AAProximityPairingStatusPayloadGeneral status1];
-[AAProximityPairingStatusPayloadGeneral status3];
-[AAProximityPairingStatusPayloadGeneral status5];
-[AAProximityPairingStatusPayloadGeneral battery1];
-[AAProximityPairingStatusPayloadGeneral battery2];
-[AAProximityPairingStatusPayloadGeneral battery3];
-[AAProximityPairingStatusPayloadGeneral battery4];
-[AAProximityPairingStatusPayloadGeneral battery5];
-[AAProximityPairingStatusPayloadGeneral caseBatteryCharging];
-[AAProximityPairingStatusPayloadGeneral caseBatteryValid];
-[AAProximityPairingStatusPayloadGeneral chargingDEOC];
-[AAProximityPairingStatusPayloadGeneral chargingDEOCSupported];
-[AAProximityPairingStatusPayloadGeneral chargingOBC];
-[AAProximityPairingStatusPayloadGeneral colorBest];
-[AAProximityPairingStatusPayloadGeneral colorRaw];
-[AAProximityPairingStatusPayloadGeneral connectedSourceCount];
-[AAProximityPairingStatusPayloadGeneral lastBudInCaseWithCurrentBud];
-[AAProximityPairingStatusPayloadGeneral lastConnectedHost];
-[AAProximityPairingStatusPayloadGeneral lastConnectedHostSignedInToICloud];
-[AAProximityPairingStatusPayloadGeneral misc1];
-[AAProximityPairingStatusPayloadGeneral myBatteryCharging];
-[AAProximityPairingStatusPayloadGeneral myBatteryLevel];
-[AAProximityPairingStatusPayloadGeneral myBatteryValid];
-[AAProximityPairingStatusPayloadGeneral otherBatteryCharging];
-[AAProximityPairingStatusPayloadGeneral otherBatteryLevel];
-[AAProximityPairingStatusPayloadGeneral otherBatteryValid];
-[AAProximityPairingStatusPayloadGeneral outOfCaseTime];
-[AAProximityPairingStatusPayloadGeneral smartRoutingConnected];
-[AAProximityPairingStatusPayloadGeneral smartRoutingScoreSource1];
-[AAProximityPairingStatusPayloadGeneral smartRoutingScoreSource2];
-[AAProximityPairingStatusPayloadGeneral supportWirelessSplitter];
```
