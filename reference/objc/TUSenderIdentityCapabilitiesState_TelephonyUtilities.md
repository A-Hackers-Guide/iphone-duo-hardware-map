# `TUSenderIdentityCapabilitiesState`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`, `TUPubliclyAccessibleCopying`
- 6 instance variables, 10 properties, 18 instance methods, 1 class methods

## Instance variables

```
B _supportsSimultaneousVoiceAndData;
@"NSUUID" _senderIdentityUUID;
@"TUCTCapabilitiesState" _csCallingCapabilitiesState;
@"TUCTCapabilitiesState" _voLTECallingCapabilitiesState;
@"TUCTCapabilitiesState" _wiFiCallingCapabilitiesState;
@"TUThumperCTCapabilitiesState" _thumperCallingCapabilitiesState;
```

## Properties

```
@property (T@"NSUUID",R,C,N,V_senderIdentityUUID) senderIdentityUUID;
@property (TB,N,V_supportsSimultaneousVoiceAndData) supportsSimultaneousVoiceAndData;
@property (T@"TUCTCapabilitiesState",C,N,V_csCallingCapabilitiesState) csCallingCapabilitiesState;
@property (T@"TUCTCapabilitiesState",C,N,V_voLTECallingCapabilitiesState) voLTECallingCapabilitiesState;
@property (T@"TUCTCapabilitiesState",C,N,V_wiFiCallingCapabilitiesState) wiFiCallingCapabilitiesState;
@property (T@"TUThumperCTCapabilitiesState",C,N,V_thumperCallingCapabilitiesState) thumperCallingCapabilitiesState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUSenderIdentityCapabilitiesState supportsSecureCoding];
```

## Instance methods

```
-[TUSenderIdentityCapabilitiesState publiclyAccessibleCopyWithZone:];
-[TUSenderIdentityCapabilitiesState supportsSimultaneousVoiceAndData];
-[TUSenderIdentityCapabilitiesState publiclyAccessibleCopy];
-[TUSenderIdentityCapabilitiesState setSupportsSimultaneousVoiceAndData:];
-[TUSenderIdentityCapabilitiesState wiFiCallingCapabilitiesState];
-[TUSenderIdentityCapabilitiesState setCsCallingCapabilitiesState:];
-[TUSenderIdentityCapabilitiesState initWithSenderIdentityUUID:];
-[TUSenderIdentityCapabilitiesState voLTECallingCapabilitiesState];
-[TUSenderIdentityCapabilitiesState encodeWithCoder:];
-[TUSenderIdentityCapabilitiesState description];
-[TUSenderIdentityCapabilitiesState initWithCoder:];
-[TUSenderIdentityCapabilitiesState setWiFiCallingCapabilitiesState:];
-[TUSenderIdentityCapabilitiesState copyWithZone:];
-[TUSenderIdentityCapabilitiesState senderIdentityUUID];
-[TUSenderIdentityCapabilitiesState setThumperCallingCapabilitiesState:];
-[TUSenderIdentityCapabilitiesState thumperCallingCapabilitiesState];
-[TUSenderIdentityCapabilitiesState setVoLTECallingCapabilitiesState:];
-[TUSenderIdentityCapabilitiesState csCallingCapabilitiesState];
```
