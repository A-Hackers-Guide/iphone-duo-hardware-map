# `CTXPCSendDeviceSettingsRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 7 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliDestination",R,N) destination;
@property (T@"CTLazuliMessageID",R,N) messageID;
@property (T@"CTLazuliSuggestedActionSettings",R,N) settings;
```

## Class methods

```
+[CTXPCSendDeviceSettingsRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCSendDeviceSettingsRequest destination];
-[CTXPCSendDeviceSettingsRequest requiredEntitlement];
-[CTXPCSendDeviceSettingsRequest messageID];
-[CTXPCSendDeviceSettingsRequest settings];
-[CTXPCSendDeviceSettingsRequest ct_shortName];
-[CTXPCSendDeviceSettingsRequest performRequestWithHandler:completionHandler:];
-[CTXPCSendDeviceSettingsRequest initWithContext:destination:messageID:settings:];
```
