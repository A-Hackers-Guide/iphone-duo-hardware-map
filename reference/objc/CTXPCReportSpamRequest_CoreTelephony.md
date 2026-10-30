# `CTXPCReportSpamRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 7 instance methods, 2 class methods

## Properties

```
@property (T@"CTLazuliDestination",R,N) destination;
@property (T@"CTLazuliSpamReportInformation",R,N) spamReportInfo;
@property (T@"CTLazuliOperationID",R,N) operationID;
```

## Class methods

```
+[CTXPCReportSpamRequest allowedClassesForArguments];
+[CTXPCReportSpamRequest isSensitiveMessage];
```

## Instance methods

```
-[CTXPCReportSpamRequest destination];
-[CTXPCReportSpamRequest operationID];
-[CTXPCReportSpamRequest requiredEntitlement];
-[CTXPCReportSpamRequest ct_shortName];
-[CTXPCReportSpamRequest performRequestWithHandler:completionHandler:];
-[CTXPCReportSpamRequest initWithContext:destination:spamReportInfo:operationID:];
-[CTXPCReportSpamRequest spamReportInfo];
```
