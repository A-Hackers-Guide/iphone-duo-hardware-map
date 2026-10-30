# `ACCHWComponentAuthServiceParams`

- Image: [`/System/Library/PrivateFrameworks/AccessoryComponentAuth.framework/AccessoryComponentAuth`](../userland/System__Library__PrivateFrameworks__AccessoryComponentAuth.framework__AccessoryComponentAuth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 24 properties, 49 instance methods, 0 class methods

## Instance variables

```
B _skipComms;
B _overrideIdentity;
B _authenticatedSession;
I _moduleAuthService;
I _authFlags;
I _batteryCode;
I _protocolVersion;
@"NSData" _certificateRaw;
@"NSData" _certificate;
@"NSData" _signature;
@"NSData" _deviceNonce;
@"NSData" _challenge;
@"NSDictionary" _certificateInfo;
^{mfi4AuthProtocolSession_s=} _authSession;
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v} _identityKey;
@"NSData" _identityCertificates;
@? _openSessionHandler;
@? _closeSessionHandler;
@? _nvmWriteSessionHandler;
@? _nvmReadSessionHandler;
@? _refreshAccessStateHandler;
@"NSNumber" _componentIndex;
@? _completionHandler;
@? _signingHandler;
```

## Properties

```
@property (TI,N,V_moduleAuthService) moduleAuthService;
@property (TI,N,V_authFlags) authFlags;
@property (T@"NSData",&,N,V_certificateRaw) certificateRaw;
@property (T@"NSData",&,N,V_certificate) certificate;
@property (T@"NSData",&,N,V_signature) signature;
@property (T@"NSData",&,N,V_deviceNonce) deviceNonce;
@property (T@"NSData",&,N,V_challenge) challenge;
@property (T@"NSDictionary",&,N,V_certificateInfo) certificateInfo;
@property (TB,N,V_skipComms) skipComms;
@property (TI,N,V_batteryCode) batteryCode;
@property (TI,N,V_protocolVersion) protocolVersion;
@property (T^{mfi4AuthProtocolSession_s=},V_authSession) authSession;
@property (TB,N,V_overrideIdentity) overrideIdentity;
@property (T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},N,V_identityKey) identityKey;
@property (T@"NSData",&,N,V_identityCertificates) identityCertificates;
@property (TB,N,V_authenticatedSession) authenticatedSession;
@property (T@?,C,V_openSessionHandler) openSessionHandler;
@property (T@?,C,V_closeSessionHandler) closeSessionHandler;
@property (T@?,C,V_nvmWriteSessionHandler) nvmWriteSessionHandler;
@property (T@?,C,V_nvmReadSessionHandler) nvmReadSessionHandler;
@property (T@?,C,V_refreshAccessStateHandler) refreshAccessStateHandler;
@property (T@"NSNumber",&,N,V_componentIndex) componentIndex;
@property (T@?,C,V_completionHandler) completionHandler;
@property (T@?,C,V_signingHandler) signingHandler;
```

## Instance methods

```
-[ACCHWComponentAuthServiceParams setSignature:];
-[ACCHWComponentAuthServiceParams setCompletionHandler:];
-[ACCHWComponentAuthServiceParams completionHandler];
-[ACCHWComponentAuthServiceParams setAuthFlags:];
-[ACCHWComponentAuthServiceParams authFlags];
-[ACCHWComponentAuthServiceParams dealloc];
-[ACCHWComponentAuthServiceParams signature];
-[ACCHWComponentAuthServiceParams protocolVersion];
-[ACCHWComponentAuthServiceParams identityKey];
-[ACCHWComponentAuthServiceParams setProtocolVersion:];
-[ACCHWComponentAuthServiceParams certificate];
-[ACCHWComponentAuthServiceParams setCertificate:];
-[ACCHWComponentAuthServiceParams challenge];
-[ACCHWComponentAuthServiceParams componentIndex];
-[ACCHWComponentAuthServiceParams setComponentIndex:];
-[ACCHWComponentAuthServiceParams setChallenge:];
-[ACCHWComponentAuthServiceParams setAuthSession:];
-[ACCHWComponentAuthServiceParams authSession];
-[ACCHWComponentAuthServiceParams setIdentityKey:];
-[ACCHWComponentAuthServiceParams certificateInfo];
-[ACCHWComponentAuthServiceParams setBatteryCode:];
-[ACCHWComponentAuthServiceParams setDeviceNonce:];
-[ACCHWComponentAuthServiceParams authenticatedSession];
-[ACCHWComponentAuthServiceParams batteryCode];
-[ACCHWComponentAuthServiceParams certificateRaw];
-[ACCHWComponentAuthServiceParams closeSessionHandler];
-[ACCHWComponentAuthServiceParams deviceNonce];
-[ACCHWComponentAuthServiceParams identityCertificates];
-[ACCHWComponentAuthServiceParams moduleAuthService];
-[ACCHWComponentAuthServiceParams nvmReadSessionHandler];
-[ACCHWComponentAuthServiceParams nvmWriteSessionHandler];
-[ACCHWComponentAuthServiceParams openSessionHandler];
-[ACCHWComponentAuthServiceParams overrideIdentity];
-[ACCHWComponentAuthServiceParams refreshAccessStateHandler];
-[ACCHWComponentAuthServiceParams setAuthenticatedSession:];
-[ACCHWComponentAuthServiceParams setCertificateInfo:];
-[ACCHWComponentAuthServiceParams setCertificateRaw:];
-[ACCHWComponentAuthServiceParams setCloseSessionHandler:];
-[ACCHWComponentAuthServiceParams setIdentityCertificates:];
-[ACCHWComponentAuthServiceParams setModuleAuthService:];
-[ACCHWComponentAuthServiceParams setNvmReadSessionHandler:];
-[ACCHWComponentAuthServiceParams setNvmWriteSessionHandler:];
-[ACCHWComponentAuthServiceParams setOpenSessionHandler:];
-[ACCHWComponentAuthServiceParams setOverrideIdentity:];
-[ACCHWComponentAuthServiceParams setRefreshAccessStateHandler:];
-[ACCHWComponentAuthServiceParams setSigningHandler:];
-[ACCHWComponentAuthServiceParams setSkipComms:];
-[ACCHWComponentAuthServiceParams signingHandler];
-[ACCHWComponentAuthServiceParams skipComms];
```
