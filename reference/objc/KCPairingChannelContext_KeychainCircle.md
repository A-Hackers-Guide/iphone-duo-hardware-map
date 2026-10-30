# `KCPairingChannelContext`

- Image: [`/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`](../userland/System__Library__PrivateFrameworks__KeychainCircle.framework__KeychainCircle.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 12 instance variables, 12 properties, 27 instance methods, 1 class methods

## Instance variables

```
B _accountIsDBR;
@"NSString" _model;
@"NSString" _modelVersion;
@"NSString" _modelClass;
@"NSString" _osVersion;
@"NSString" _uniqueDeviceID;
@"NSString" _uniqueClientID;
@"NSString" _altDSID;
@"NSString" _flowID;
@"NSString" _deviceSessionID;
@"NSString" _intent;
@"NSString" _capability;
```

## Properties

```
@property (T@"NSString",C,N,V_model) model;
@property (T@"NSString",C,N,V_modelVersion) modelVersion;
@property (T@"NSString",C,N,V_modelClass) modelClass;
@property (T@"NSString",C,N,V_osVersion) osVersion;
@property (T@"NSString",C,N,V_uniqueDeviceID) uniqueDeviceID;
@property (T@"NSString",C,N,V_uniqueClientID) uniqueClientID;
@property (T@"NSString",C,N,V_altDSID) altDSID;
@property (T@"NSString",C,N,V_flowID) flowID;
@property (T@"NSString",C,N,V_deviceSessionID) deviceSessionID;
@property (T@"NSString",C,N,V_intent) intent;
@property (T@"NSString",C,N,V_capability) capability;
@property (TB,N,V_accountIsDBR) accountIsDBR;
```

## Class methods

```
+[KCPairingChannelContext supportsSecureCoding];
```

## Instance methods

```
-[KCPairingChannelContext model];
-[KCPairingChannelContext modelVersion];
-[KCPairingChannelContext setModel:];
-[KCPairingChannelContext osVersion];
-[KCPairingChannelContext setAltDSID:];
-[KCPairingChannelContext altDSID];
-[KCPairingChannelContext setIntent:];
-[KCPairingChannelContext setOsVersion:];
-[KCPairingChannelContext flowID];
-[KCPairingChannelContext intent];
-[KCPairingChannelContext setModelVersion:];
-[KCPairingChannelContext encodeWithCoder:];
-[KCPairingChannelContext initWithCoder:];
-[KCPairingChannelContext setDeviceSessionID:];
-[KCPairingChannelContext isEqual:];
-[KCPairingChannelContext deviceSessionID];
-[KCPairingChannelContext setFlowID:];
-[KCPairingChannelContext setUniqueClientID:];
-[KCPairingChannelContext setUniqueDeviceID:];
-[KCPairingChannelContext uniqueClientID];
-[KCPairingChannelContext uniqueDeviceID];
-[KCPairingChannelContext capability];
-[KCPairingChannelContext setCapability:];
-[KCPairingChannelContext modelClass];
-[KCPairingChannelContext setModelClass:];
-[KCPairingChannelContext accountIsDBR];
-[KCPairingChannelContext setAccountIsDBR:];
```
