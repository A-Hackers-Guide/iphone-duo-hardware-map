# `OTJoiningConfiguration`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 8 instance variables, 8 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _isInitiator;
B _testsEnabled;
@"NSString" _protocolType;
@"NSString" _uniqueDeviceID;
@"NSString" _uniqueClientID;
@"NSString" _pairingUUID;
Q _epoch;
q _timeout;
```

## Properties

```
@property (T@"NSString",&,N,V_protocolType) protocolType;
@property (T@"NSString",&,N,V_uniqueDeviceID) uniqueDeviceID;
@property (T@"NSString",&,N,V_uniqueClientID) uniqueClientID;
@property (T@"NSString",&,N,V_pairingUUID) pairingUUID;
@property (TQ,N,V_epoch) epoch;
@property (TB,N,V_isInitiator) isInitiator;
@property (TB,N,V_testsEnabled) testsEnabled;
@property (Tq,V_timeout) timeout;
```

## Class methods

```
+[OTJoiningConfiguration supportsSecureCoding];
```

## Instance methods

```
-[OTJoiningConfiguration isInitiator];
-[OTJoiningConfiguration setIsInitiator:];
-[OTJoiningConfiguration epoch];
-[OTJoiningConfiguration setEpoch:];
-[OTJoiningConfiguration timeout];
-[OTJoiningConfiguration setTimeout:];
-[OTJoiningConfiguration encodeWithCoder:];
-[OTJoiningConfiguration initWithCoder:];
-[OTJoiningConfiguration setPairingUUID:];
-[OTJoiningConfiguration enableForTests];
-[OTJoiningConfiguration initWithProtocolType:uniqueDeviceID:uniqueClientID:pairingUUID:epoch:isInitiator:];
-[OTJoiningConfiguration pairingUUID];
-[OTJoiningConfiguration protocolType];
-[OTJoiningConfiguration setProtocolType:];
-[OTJoiningConfiguration setTestsEnabled:];
-[OTJoiningConfiguration setUniqueClientID:];
-[OTJoiningConfiguration setUniqueDeviceID:];
-[OTJoiningConfiguration testsEnabled];
-[OTJoiningConfiguration uniqueClientID];
-[OTJoiningConfiguration uniqueDeviceID];
```
