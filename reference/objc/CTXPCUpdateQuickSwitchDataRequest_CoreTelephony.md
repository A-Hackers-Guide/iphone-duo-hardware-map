# `CTXPCUpdateQuickSwitchDataRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCRequestMessage`
- 0 instance variables, 3 properties, 7 instance methods, 1 class methods

## Properties

```
@property (Tq,R,N) clientID;
@property (T@"NSString",R,N) version;
@property (T@"NSData",R,N) payload;
```

## Class methods

```
+[CTXPCUpdateQuickSwitchDataRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCUpdateQuickSwitchDataRequest clientID];
-[CTXPCUpdateQuickSwitchDataRequest requiredEntitlement];
-[CTXPCUpdateQuickSwitchDataRequest ct_shortName];
-[CTXPCUpdateQuickSwitchDataRequest payload];
-[CTXPCUpdateQuickSwitchDataRequest version];
-[CTXPCUpdateQuickSwitchDataRequest performRequestWithHandler:completionHandler:];
-[CTXPCUpdateQuickSwitchDataRequest initWithClientID:version:payload:];
```
