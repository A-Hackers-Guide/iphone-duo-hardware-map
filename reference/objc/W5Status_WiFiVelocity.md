# `W5Status`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 9 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"W5WiFiStatus" _wifi;
@"W5AWDLStatus" _awdl;
@"W5BluetoothStatus" _bluetooth;
@"W5NetworkStatus" _network;
@"W5PowerStatus" _power;
@"NSArray" _diagnosticsModes;
@"W5SummaryFaults" _lastHrFaults;
@"W5SummaryLinkTests" _lastHrLinkTests;
@"W5SummaryRecoveries" _lastHrRecoveries;
```

## Properties

```
@property (T@"W5WiFiStatus",C,N,V_wifi) wifi;
@property (T@"W5AWDLStatus",C,N,V_awdl) awdl;
@property (T@"W5BluetoothStatus",C,N,V_bluetooth) bluetooth;
@property (T@"W5NetworkStatus",C,N,V_network) network;
@property (T@"W5PowerStatus",C,N,V_power) power;
@property (T@"NSArray",C,N,V_diagnosticsModes) diagnosticsModes;
@property (T@"W5SummaryFaults",C,N,V_lastHrFaults) lastHrFaults;
@property (T@"W5SummaryLinkTests",C,N,V_lastHrLinkTests) lastHrLinkTests;
@property (T@"W5SummaryRecoveries",C,N,V_lastHrRecoveries) lastHrRecoveries;
```

## Class methods

```
+[W5Status supportsSecureCoding];
```

## Instance methods

```
-[W5Status power];
-[W5Status network];
-[W5Status setWifi:];
-[W5Status dealloc];
-[W5Status setBluetooth:];
-[W5Status isEqualToStatus:];
-[W5Status encodeWithCoder:];
-[W5Status conformsToProtocol:];
-[W5Status hash];
-[W5Status description];
-[W5Status initWithCoder:];
-[W5Status wifi];
-[W5Status copyWithZone:];
-[W5Status isEqual:];
-[W5Status setPower:];
-[W5Status setNetwork:];
-[W5Status bluetooth];
-[W5Status awdl];
-[W5Status setAwdl:];
-[W5Status lastHrLinkTests];
-[W5Status diagnosticsModes];
-[W5Status lastHrFaults];
-[W5Status lastHrRecoveries];
-[W5Status setDiagnosticsModes:];
-[W5Status setLastHrFaults:];
-[W5Status setLastHrLinkTests:];
-[W5Status setLastHrRecoveries:];
```
