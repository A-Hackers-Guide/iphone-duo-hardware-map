# `CTServiceDisconnectionStatus`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _activationFailure;
i _contextType;
i _error;
@"NSString" _apnName;
@"NSNumber" _connectionMask;
@"NSNumber" _rawCauseCode;
@"NSNumber" _pdp;
```

## Properties

```
@property (Ti,N,V_contextType) contextType;
@property (T@"NSString",&,N,V_apnName) apnName;
@property (TB,N,V_activationFailure) activationFailure;
@property (T@"NSNumber",&,N,V_connectionMask) connectionMask;
@property (Ti,N,V_error) error;
@property (T@"NSNumber",&,N,V_rawCauseCode) rawCauseCode;
@property (T@"NSNumber",&,N,V_pdp) pdp;
```

## Class methods

```
+[CTServiceDisconnectionStatus supportsSecureCoding];
```

## Instance methods

```
-[CTServiceDisconnectionStatus setError:];
-[CTServiceDisconnectionStatus contextType];
-[CTServiceDisconnectionStatus activationFailure];
-[CTServiceDisconnectionStatus setApnName:];
-[CTServiceDisconnectionStatus setContextType:];
-[CTServiceDisconnectionStatus setPdp:];
-[CTServiceDisconnectionStatus apnName];
-[CTServiceDisconnectionStatus error];
-[CTServiceDisconnectionStatus encodeWithCoder:];
-[CTServiceDisconnectionStatus description];
-[CTServiceDisconnectionStatus initWithCoder:];
-[CTServiceDisconnectionStatus setActivationFailure:];
-[CTServiceDisconnectionStatus pdp];
-[CTServiceDisconnectionStatus copyWithZone:];
-[CTServiceDisconnectionStatus connectionMask];
-[CTServiceDisconnectionStatus rawCauseCode];
-[CTServiceDisconnectionStatus setConnectionMask:];
-[CTServiceDisconnectionStatus setRawCauseCode:];
```
