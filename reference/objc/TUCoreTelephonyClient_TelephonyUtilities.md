# `TUCoreTelephonyClient`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `TUEmergencyCoreTelephonyClient`, `TUTTYCoreTelephonyClient`, `TUCoreTelephonyClient`
- 2 instance variables, 14 properties, 37 instance methods, 3 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
@"CoreTelephonyClient" _client;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"CoreTelephonyClient",R,N,V_client) client;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[TUCoreTelephonyClient RTTSettingsClass];
+[TUCoreTelephonyClient RTTTelephonyUtilitiesClass];
+[TUCoreTelephonyClient sharedRTTTelephonyUtilities];
```

## Instance methods

```
-[TUCoreTelephonyClient initWithQueue:];
-[TUCoreTelephonyClient init];
-[TUCoreTelephonyClient queue];
-[TUCoreTelephonyClient client];
-[TUCoreTelephonyClient inEmergencyMode];
-[TUCoreTelephonyClient subscriptionForLabelIdentifier:];
-[TUCoreTelephonyClient isDialAssistSupportedForSubscriptionLabelIdentifier:error:];
-[TUCoreTelephonyClient isEmergencyNumberForDigits:subscription:error:];
-[TUCoreTelephonyClient isEmergencyNumberForDigits:subscriptionUUID:error:];
-[TUCoreTelephonyClient isRTTRelaySupportedForSubscription:];
-[TUCoreTelephonyClient isRTTRelaySupportedForSubscriptionUUID:];
-[TUCoreTelephonyClient isRTTSupportedForSubscription:];
-[TUCoreTelephonyClient isRTTSupportedForSubscriptionUUID:];
-[TUCoreTelephonyClient isTTYEnabledForSubscription:];
-[TUCoreTelephonyClient isTTYEnabledForSubscriptionUUID:];
-[TUCoreTelephonyClient isTTYHardwareAvailableForSubscription:];
-[TUCoreTelephonyClient isTTYHardwareAvailableForSubscriptionUUID:];
-[TUCoreTelephonyClient isTTYHardwareEnabledForSubscription:];
-[TUCoreTelephonyClient isTTYHardwareEnabledForSubscriptionUUID:];
-[TUCoreTelephonyClient isTTYHardwareSupportedForSubscription:];
-[TUCoreTelephonyClient isTTYHardwareSupportedForSubscriptionUUID:];
-[TUCoreTelephonyClient isTTYSoftwareAvailableForSubscription:];
-[TUCoreTelephonyClient isTTYSoftwareAvailableForSubscriptionUUID:];
-[TUCoreTelephonyClient isTTYSoftwareEnabledForSubscription:];
-[TUCoreTelephonyClient isTTYSoftwareEnabledForSubscriptionUUID:];
-[TUCoreTelephonyClient isTTYSoftwareSupportedForSubscription:];
-[TUCoreTelephonyClient isTTYSoftwareSupportedForSubscriptionUUID:];
-[TUCoreTelephonyClient isTTYSupportedForSubscription:];
-[TUCoreTelephonyClient isTTYSupportedForSubscriptionUUID:];
-[TUCoreTelephonyClient isWhitelistedEmergencyNumberForDigits:subscription:error:];
-[TUCoreTelephonyClient isWhitelistedEmergencyNumberForDigits:subscriptionUUID:error:];
-[TUCoreTelephonyClient objectForKey:subscriptionLabelIdentifier:error:];
-[TUCoreTelephonyClient preferredTransportMethodForSubscription:];
-[TUCoreTelephonyClient shouldShowEmergencyCallbackModeAlertForSubscription:error:];
-[TUCoreTelephonyClient shouldShowEmergencyCallbackModeAlertForSubscriptionUUID:error:];
-[TUCoreTelephonyClient subscriptionForUUID:];
-[TUCoreTelephonyClient testEmergencyHandleForSubscriptionLabelIdentifier:error:];
```
