# `TUConversationProvider`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 5 properties, 24 instance methods, 7 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSArray" _supportedMediaTypes;
@"TUConversationProviderConfiguration" _providerConfiguration;
```

## Properties

```
@property (T@"NSObject<OS_tcc_identity>",R,C,N) assumedIdentity;
@property (TQ,R,N) defaultAVMode;
@property (T@"NSArray",R,C,N,V_supportedMediaTypes) supportedMediaTypes;
@property (T@"TUConversationProviderConfiguration",&,N,V_providerConfiguration) providerConfiguration;
@property (T@"NSString",R,C,N,V_identifier) identifier;
```

## Class methods

```
+[TUConversationProvider supportsSecureCoding];
+[TUConversationProvider providerForIdentifier:];
+[TUConversationProvider telephonyWithSharePlayProvider];
+[TUConversationProvider expanseProvider];
+[TUConversationProvider unknownProvider];
+[TUConversationProvider faceTimeProvider];
+[TUConversationProvider matchesDefaultProviderIdentifier:];
```

## Instance methods

```
-[TUConversationProvider assumedIdentity];
-[TUConversationProvider identifier];
-[TUConversationProvider supportsLinks];
-[TUConversationProvider defaultAVMode];
-[TUConversationProvider isEqualToConversationProvider:];
-[TUConversationProvider initWithConversationProvider:];
-[TUConversationProvider bundleIdentifier];
-[TUConversationProvider initWithConfiguration:];
-[TUConversationProvider supportsAVMode:];
-[TUConversationProvider supportsVideo];
-[TUConversationProvider encodeWithCoder:];
-[TUConversationProvider pseudonymFeatureID];
-[TUConversationProvider hash];
-[TUConversationProvider providerConfiguration];
-[TUConversationProvider description];
-[TUConversationProvider initWithCoder:];
-[TUConversationProvider isTelephonyWithSharePlayProvider];
-[TUConversationProvider supportedMediaTypes];
-[TUConversationProvider copyWithZone:];
-[TUConversationProvider isEqual:];
-[TUConversationProvider isDefaultProvider];
-[TUConversationProvider supportsSharePlay];
-[TUConversationProvider setProviderConfiguration:];
-[TUConversationProvider supportsMediaType:];
```
