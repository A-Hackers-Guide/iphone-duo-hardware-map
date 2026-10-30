# `CTXPCFetchRenderInformationRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 9 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliDestination",R,N) destination;
@property (T@"CTLazuliOperationID",R,N) operationID;
@property (T@"CTLazuliChatBotSearchMetaData",R,N) metaData;
```

## Class methods

```
+[CTXPCFetchRenderInformationRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCFetchRenderInformationRequest destination];
-[CTXPCFetchRenderInformationRequest operationID];
-[CTXPCFetchRenderInformationRequest requiredEntitlement];
-[CTXPCFetchRenderInformationRequest metaData];
-[CTXPCFetchRenderInformationRequest ct_shortName];
-[CTXPCFetchRenderInformationRequest performRequestWithHandler:completionHandler:];
-[CTXPCFetchRenderInformationRequest initWithContext:destination:];
-[CTXPCFetchRenderInformationRequest initWithContext:destination:operationID:];
-[CTXPCFetchRenderInformationRequest initWithContext:destination:operationID:metaData:];
```
