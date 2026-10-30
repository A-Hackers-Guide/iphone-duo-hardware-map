# `CTXPCSendOneToManyGeoLocationRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 7 instance methods, 2 class methods

## Properties

```
@property (T@"CTLazuliDestinationList",R,N) destinationList;
@property (T@"CTLazuliMessageID",R,N) messageID;
@property (T@"CTLazuliMessageGeoLocationPush",R,N) push;
```

## Class methods

```
+[CTXPCSendOneToManyGeoLocationRequest allowedClassesForArguments];
+[CTXPCSendOneToManyGeoLocationRequest isSensitiveMessage];
```

## Instance methods

```
-[CTXPCSendOneToManyGeoLocationRequest requiredEntitlement];
-[CTXPCSendOneToManyGeoLocationRequest messageID];
-[CTXPCSendOneToManyGeoLocationRequest ct_shortName];
-[CTXPCSendOneToManyGeoLocationRequest performRequestWithHandler:completionHandler:];
-[CTXPCSendOneToManyGeoLocationRequest push];
-[CTXPCSendOneToManyGeoLocationRequest destinationList];
-[CTXPCSendOneToManyGeoLocationRequest initWithContext:to:withMessageID:withGeoPush:];
```
