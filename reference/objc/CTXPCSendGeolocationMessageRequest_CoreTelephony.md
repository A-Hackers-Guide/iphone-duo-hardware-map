# `CTXPCSendGeolocationMessageRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 4 properties, 10 instance methods, 2 class methods

## Properties

```
@property (T@"CTLazuliMessageID",R,N) messageID;
@property (T@"CTLazuliMessageGeoLocationPush",R,N) geoLocationPush;
@property (T@"CTLazuliDestination",R,N) destination;
@property (T@"CTLazuliGroupChatUri",R,N) groupChatURI;
```

## Class methods

```
+[CTXPCSendGeolocationMessageRequest allowedClassesForArguments];
+[CTXPCSendGeolocationMessageRequest isSensitiveMessage];
```

## Instance methods

```
-[CTXPCSendGeolocationMessageRequest destination];
-[CTXPCSendGeolocationMessageRequest requiredEntitlement];
-[CTXPCSendGeolocationMessageRequest messageID];
-[CTXPCSendGeolocationMessageRequest ct_shortName];
-[CTXPCSendGeolocationMessageRequest security];
-[CTXPCSendGeolocationMessageRequest performRequestWithHandler:completionHandler:];
-[CTXPCSendGeolocationMessageRequest geoLocationPush];
-[CTXPCSendGeolocationMessageRequest initWithContext:destination:messageID:geoLocationPush:security:];
-[CTXPCSendGeolocationMessageRequest groupChatURI];
-[CTXPCSendGeolocationMessageRequest initWithContext:groupChatURI:messageID:geoLocationPush:security:];
```
