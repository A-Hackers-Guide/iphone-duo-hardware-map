# `KCAESGCMDuplexSession`

- Image: [`/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`](../userland/System__Library__PrivateFrameworks__KeychainCircle.framework__KeychainCircle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 11 instance variables, 11 properties, 33 instance methods, 3 class methods

## Instance variables

```
B _asSender;
@"NSString" _pairingUUID;
@"NSString" _altDSID;
@"NSString" _flowID;
@"NSString" _deviceSessionID;
Q _piggybackingVersion;
Q _epoch;
Q _context;
@"NSData" _secret;
^{?=[16C]} _send;
^{?=[16C]} _receive;
```

## Properties

```
@property (TB,V_asSender) asSender;
@property (TQ,V_context) context;
@property (T@"NSData",&,V_secret) secret;
@property (T^{?=[16C]},V_send) send;
@property (T^{?=[16C]},V_receive) receive;
@property (T@"NSString",&,V_pairingUUID) pairingUUID;
@property (T@"NSString",&,V_altDSID) altDSID;
@property (T@"NSString",&,V_flowID) flowID;
@property (T@"NSString",&,V_deviceSessionID) deviceSessionID;
@property (TQ,V_piggybackingVersion) piggybackingVersion;
@property (TQ,V_epoch) epoch;
```

## Class methods

```
+[KCAESGCMDuplexSession supportsSecureCoding];
+[KCAESGCMDuplexSession sessionAsReceiver:context:];
+[KCAESGCMDuplexSession sessionAsSender:context:];
```

## Instance methods

```
-[KCAESGCMDuplexSession epoch];
-[KCAESGCMDuplexSession send];
-[KCAESGCMDuplexSession setAltDSID:];
-[KCAESGCMDuplexSession altDSID];
-[KCAESGCMDuplexSession flowID];
-[KCAESGCMDuplexSession setEpoch:];
-[KCAESGCMDuplexSession dealloc];
-[KCAESGCMDuplexSession setContext:];
-[KCAESGCMDuplexSession encodeWithCoder:];
-[KCAESGCMDuplexSession initWithCoder:];
-[KCAESGCMDuplexSession setDeviceSessionID:];
-[KCAESGCMDuplexSession context];
-[KCAESGCMDuplexSession deviceSessionID];
-[KCAESGCMDuplexSession setFlowID:];
-[KCAESGCMDuplexSession setPairingUUID:];
-[KCAESGCMDuplexSession pairingUUID];
-[KCAESGCMDuplexSession secret];
-[KCAESGCMDuplexSession setSecret:];
-[KCAESGCMDuplexSession GCM:context:iv:size:data:processed:tag:error:];
-[KCAESGCMDuplexSession receive];
-[KCAESGCMDuplexSession asSender];
-[KCAESGCMDuplexSession decryptAndVerify:error:];
-[KCAESGCMDuplexSession encrypt:error:];
-[KCAESGCMDuplexSession encryptCapsuleSize:IV:];
-[KCAESGCMDuplexSession initAsReceiver:context:];
-[KCAESGCMDuplexSession initAsSender:context:];
-[KCAESGCMDuplexSession initWithSecret:context:as:];
-[KCAESGCMDuplexSession initWithSecret:context:as:altDSID:pairingUUID:piggybackingVersion:epoch:];
-[KCAESGCMDuplexSession piggybackingVersion];
-[KCAESGCMDuplexSession setAsSender:];
-[KCAESGCMDuplexSession setPiggybackingVersion:];
-[KCAESGCMDuplexSession setReceive:];
-[KCAESGCMDuplexSession setSend:];
```
