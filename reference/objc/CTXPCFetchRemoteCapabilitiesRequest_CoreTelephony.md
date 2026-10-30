# `CTXPCFetchRemoteCapabilitiesRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 7 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliDestination",R,N) destination;
@property (T@"CTLazuliFetchRemoteCapabilitiesOptions",R,N) options;
@property (T@"CTLazuliOperationID",R,N) operationID;
```

## Class methods

```
+[CTXPCFetchRemoteCapabilitiesRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCFetchRemoteCapabilitiesRequest destination];
-[CTXPCFetchRemoteCapabilitiesRequest operationID];
-[CTXPCFetchRemoteCapabilitiesRequest requiredEntitlement];
-[CTXPCFetchRemoteCapabilitiesRequest ct_shortName];
-[CTXPCFetchRemoteCapabilitiesRequest performRequestWithHandler:completionHandler:];
-[CTXPCFetchRemoteCapabilitiesRequest options];
-[CTXPCFetchRemoteCapabilitiesRequest initWithContext:destination:options:operationID:];
```
