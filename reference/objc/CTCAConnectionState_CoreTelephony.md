# `CTCAConnectionState`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 16 instance methods, 1 class methods

## Instance variables

```
q _connectionStatus;
q _syncStatus;
q _registrationStatus;
q _congestionStatus;
@"NSNumber" _rssi;
@"CTCATransmissionProgress" _currentTransmissionProgress;
```

## Properties

```
@property (Tq,N,V_connectionStatus) connectionStatus;
@property (Tq,N,V_syncStatus) syncStatus;
@property (Tq,N,V_registrationStatus) registrationStatus;
@property (Tq,N,V_congestionStatus) congestionStatus;
@property (T@"NSNumber",&,N,V_rssi) rssi;
@property (T@"CTCATransmissionProgress",&,N,V_currentTransmissionProgress) currentTransmissionProgress;
```

## Class methods

```
+[CTCAConnectionState supportsSecureCoding];
```

## Instance methods

```
-[CTCAConnectionState rssi];
-[CTCAConnectionState setConnectionStatus:];
-[CTCAConnectionState setRssi:];
-[CTCAConnectionState setRegistrationStatus:];
-[CTCAConnectionState encodeWithCoder:];
-[CTCAConnectionState registrationStatus];
-[CTCAConnectionState description];
-[CTCAConnectionState initWithCoder:];
-[CTCAConnectionState syncStatus];
-[CTCAConnectionState copyWithZone:];
-[CTCAConnectionState connectionStatus];
-[CTCAConnectionState setCurrentTransmissionProgress:];
-[CTCAConnectionState congestionStatus];
-[CTCAConnectionState currentTransmissionProgress];
-[CTCAConnectionState setCongestionStatus:];
-[CTCAConnectionState setSyncStatus:];
```
