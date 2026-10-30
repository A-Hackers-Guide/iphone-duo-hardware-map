# `TUConversationVirtualParticipantConfig`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 17 instance methods, 4 class methods

## Instance variables

```
B _serverCertValidationEnabled;
Q _connectionRetryIntervalMillis;
Q _connectionMaxAttempts;
Q _rpcStreamRetryIntervalMillis;
Q _rpcStreamMaxAttempts;
@"NSString" _serverCertHostnameOverride;
@"NSString" _serverCertLeafMarkerOIDOverride;
@"NSData" _idsAliasingSalt;
```

## Properties

```
@property (TQ,R,N,V_connectionRetryIntervalMillis) connectionRetryIntervalMillis;
@property (TQ,R,N,V_connectionMaxAttempts) connectionMaxAttempts;
@property (TQ,R,N,V_rpcStreamRetryIntervalMillis) rpcStreamRetryIntervalMillis;
@property (TQ,R,N,V_rpcStreamMaxAttempts) rpcStreamMaxAttempts;
@property (TB,R,N,V_serverCertValidationEnabled) serverCertValidationEnabled;
@property (T@"NSString",R,C,N,V_serverCertHostnameOverride) serverCertHostnameOverride;
@property (T@"NSString",R,C,N,V_serverCertLeafMarkerOIDOverride) serverCertLeafMarkerOIDOverride;
@property (T@"NSData",C,N,V_idsAliasingSalt) idsAliasingSalt;
```

## Class methods

```
+[TUConversationVirtualParticipantConfig supportsSecureCoding];
+[TUConversationVirtualParticipantConfig serverCertHostnameUserDefaultsKey];
+[TUConversationVirtualParticipantConfig serverCertLeafMarkerOIDUserDefaultsKey];
+[TUConversationVirtualParticipantConfig serverCertValidationEnabledUserDefaultsKey];
```

## Instance methods

```
-[TUConversationVirtualParticipantConfig encodeWithCoder:];
-[TUConversationVirtualParticipantConfig hash];
-[TUConversationVirtualParticipantConfig description];
-[TUConversationVirtualParticipantConfig initWithCoder:];
-[TUConversationVirtualParticipantConfig copyWithZone:];
-[TUConversationVirtualParticipantConfig isEqual:];
-[TUConversationVirtualParticipantConfig idsAliasingSalt];
-[TUConversationVirtualParticipantConfig serverCertLeafMarkerOIDOverride];
-[TUConversationVirtualParticipantConfig connectionMaxAttempts];
-[TUConversationVirtualParticipantConfig connectionRetryIntervalMillis];
-[TUConversationVirtualParticipantConfig initWithConnectionRetryIntervalMillis:connectionMaxAttempts:rpcStreamRetryIntervalMillis:rpcStreamMaxAttempts:serverCertValidationEnabled:serverCertHostnameOverride:serverCertLeafMarkerOIDOverride:];
-[TUConversationVirtualParticipantConfig isEqualToConversationVirtualParticipantConfig:];
-[TUConversationVirtualParticipantConfig rpcStreamMaxAttempts];
-[TUConversationVirtualParticipantConfig rpcStreamRetryIntervalMillis];
-[TUConversationVirtualParticipantConfig serverCertHostnameOverride];
-[TUConversationVirtualParticipantConfig serverCertValidationEnabled];
-[TUConversationVirtualParticipantConfig setIdsAliasingSalt:];
```
