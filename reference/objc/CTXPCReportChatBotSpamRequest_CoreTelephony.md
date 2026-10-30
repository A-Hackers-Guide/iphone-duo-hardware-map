# `CTXPCReportChatBotSpamRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCSubscriptionContextRequest`
- 0 instance variables, 3 properties, 7 instance methods, 1 class methods

## Properties

```
@property (T@"CTLazuliDestination",R,N) destination;
@property (T@"CTLazuliChatBotSpamReportInformation",R,N) spamReportInfo;
@property (T@"CTLazuliOperationID",R,N) operationID;
```

## Class methods

```
+[CTXPCReportChatBotSpamRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCReportChatBotSpamRequest destination];
-[CTXPCReportChatBotSpamRequest operationID];
-[CTXPCReportChatBotSpamRequest requiredEntitlement];
-[CTXPCReportChatBotSpamRequest ct_shortName];
-[CTXPCReportChatBotSpamRequest performRequestWithHandler:completionHandler:];
-[CTXPCReportChatBotSpamRequest initWithContext:destination:spamReportInfo:operationID:];
-[CTXPCReportChatBotSpamRequest spamReportInfo];
```
