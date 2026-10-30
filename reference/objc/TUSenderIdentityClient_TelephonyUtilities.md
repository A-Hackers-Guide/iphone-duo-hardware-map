# `TUSenderIdentityClient`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"<TUCoreTelephonyClient>" _client;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"<TUCoreTelephonyClient>",&,N,V_client) client;
```

## Instance methods

```
-[TUSenderIdentityClient init];
-[TUSenderIdentityClient queue];
-[TUSenderIdentityClient setClient:];
-[TUSenderIdentityClient client];
-[TUSenderIdentityClient inEmergencyMode];
-[TUSenderIdentityClient isWhitelistedEmergencyNumberForDigits:senderIdentityUUID:error:];
-[TUSenderIdentityClient isEmergencyNumberForDigits:senderIdentityUUID:];
-[TUSenderIdentityClient isEmergencyNumberForDigits:senderIdentityUUID:error:];
-[TUSenderIdentityClient isRTTAvailableForSenderIdentityUUID:];
-[TUSenderIdentityClient isRTTRelaySupportedForSenderIdentityUUID:];
-[TUSenderIdentityClient isRTTSupportedForSenderIdentityUUID:];
-[TUSenderIdentityClient isTTYAvailableForSenderIdentityUUID:];
-[TUSenderIdentityClient isTTYEnabledForSenderIdentityUUID:];
-[TUSenderIdentityClient isTTYHardwareAvailableForSenderIdentityUUID:];
-[TUSenderIdentityClient isTTYHardwareEnabledForSenderIdentityUUID:];
-[TUSenderIdentityClient isTTYHardwareSupportedForSenderIdentityUUID:];
-[TUSenderIdentityClient isTTYSoftwareAvailableForSenderIdentityUUID:];
-[TUSenderIdentityClient isTTYSoftwareEnabledForSenderIdentityUUID:];
-[TUSenderIdentityClient isTTYSoftwareSupportedForSenderIdentityUUID:];
-[TUSenderIdentityClient isTTYSupportedForSenderIdentityUUID:];
-[TUSenderIdentityClient isWhitelistedEmergencyNumberForDigits:senderIdentityUUID:];
-[TUSenderIdentityClient shouldShowEmergencyCallbackModeAlertForSenderIdentityUUID:];
-[TUSenderIdentityClient shouldShowEmergencyCallbackModeAlertForSenderIdentityUUID:error:];
-[TUSenderIdentityClient testEmergencyHandleForAccountUUID:error:];
```
