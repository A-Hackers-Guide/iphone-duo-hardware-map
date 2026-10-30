# `FudPersonalizationRequest`

- Image: [`/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/MobileAccessoryUpdater`](../userland/System__Library__PrivateFrameworks__MobileAccessoryUpdater.framework__MobileAccessoryUpdater.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 21 instance variables, 17 properties, 42 instance methods, 1 class methods

## Instance variables

```
B _cproSet;
B _csecSet;
B _cepoSet;
B _useSSOCredentials;
B _globalSigning;
B _productionMode;
B _securityMode;
B _enableMixMatch;
S _responseAlignment;
i _responseFormat;
I _boardID;
I _chipID;
I _securityDomain;
I _chipEpoch;
@"NSString" _requestName;
@"NSString" _requestPrefix;
Q _ecID;
@"NSData" _extEcID;
@"NSData" _nonceHash;
@"NSArray" _objectList;
@"NSData" _payload;
```

## Properties

```
@property (T@"NSString",R,C,N,V_requestName) requestName;
@property (T@"NSString",&,N,V_requestPrefix) requestPrefix;
@property (Ti,N,V_responseFormat) responseFormat;
@property (TI,N,V_boardID) boardID;
@property (TI,N,V_chipID) chipID;
@property (TQ,N,V_ecID) ecID;
@property (T@"NSData",&,N,V_extEcID) extEcID;
@property (TB,N,V_globalSigning) globalSigning;
@property (TI,N,V_securityDomain) securityDomain;
@property (TB,N,V_productionMode) productionMode;
@property (TB,N,V_securityMode) securityMode;
@property (T@"NSData",&,N,V_nonceHash) nonceHash;
@property (TI,N,V_chipEpoch) chipEpoch;
@property (TB,N,V_enableMixMatch) enableMixMatch;
@property (T@"NSArray",&,N,V_objectList) objectList;
@property (T@"NSData",&,N,V_payload) payload;
@property (TS,N,V_responseAlignment) responseAlignment;
```

## Class methods

```
+[FudPersonalizationRequest supportsSecureCoding];
```

## Instance methods

```
-[FudPersonalizationRequest securityDomain];
-[FudPersonalizationRequest dealloc];
-[FudPersonalizationRequest payload];
-[FudPersonalizationRequest setPayload:];
-[FudPersonalizationRequest setSecurityDomain:];
-[FudPersonalizationRequest encodeWithCoder:];
-[FudPersonalizationRequest initWithCoder:];
-[FudPersonalizationRequest initWithName:];
-[FudPersonalizationRequest securityMode];
-[FudPersonalizationRequest setSecurityMode:];
-[FudPersonalizationRequest boardID];
-[FudPersonalizationRequest chipID];
-[FudPersonalizationRequest setBoardID:];
-[FudPersonalizationRequest setChipID:];
-[FudPersonalizationRequest requestName];
-[FudPersonalizationRequest responseFormat];
-[FudPersonalizationRequest productionMode];
-[FudPersonalizationRequest setProductionMode:];
-[FudPersonalizationRequest chipEpoch];
-[FudPersonalizationRequest ecID];
-[FudPersonalizationRequest enableMixMatch];
-[FudPersonalizationRequest nonceHash];
-[FudPersonalizationRequest setChipEpoch:];
-[FudPersonalizationRequest setEcID:];
-[FudPersonalizationRequest setEnableMixMatch:];
-[FudPersonalizationRequest setNonceHash:];
-[FudPersonalizationRequest isSecurityModeSet];
-[FudPersonalizationRequest requestPrefix];
-[FudPersonalizationRequest setExtEcID:];
-[FudPersonalizationRequest setGlobalSigning:];
-[FudPersonalizationRequest setObjectList:];
-[FudPersonalizationRequest setRequestPrefix:];
-[FudPersonalizationRequest setResponseAlignment:];
-[FudPersonalizationRequest setResponseFormat:];
-[FudPersonalizationRequest extEcID];
-[FudPersonalizationRequest globalSigning];
-[FudPersonalizationRequest isChipEpochSet];
-[FudPersonalizationRequest isProductionModeSet];
-[FudPersonalizationRequest objectList];
-[FudPersonalizationRequest responseAlignment];
-[FudPersonalizationRequest setUseSSOCredentials:];
-[FudPersonalizationRequest useSSOCredentials];
```
