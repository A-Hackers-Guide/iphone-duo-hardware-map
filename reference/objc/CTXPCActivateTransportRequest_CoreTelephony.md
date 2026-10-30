# `CTXPCActivateTransportRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCRequestMessage`
- 0 instance variables, 4 properties, 8 instance methods, 1 class methods

## Properties

```
@property (TQ,R,N) endpoint;
@property (TQ,R,N) role;
@property (T@"NSString",R,N) remoteDeviceId;
@property (T@"NSDictionary",R,N) remoteDeviceInfo;
```

## Class methods

```
+[CTXPCActivateTransportRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCActivateTransportRequest requiredEntitlement];
-[CTXPCActivateTransportRequest ct_shortName];
-[CTXPCActivateTransportRequest endpoint];
-[CTXPCActivateTransportRequest role];
-[CTXPCActivateTransportRequest performRequestWithHandler:completionHandler:];
-[CTXPCActivateTransportRequest initWithEndpoint:role:remoteDeviceId:remoteDeviceInfo:];
-[CTXPCActivateTransportRequest remoteDeviceId];
-[CTXPCActivateTransportRequest remoteDeviceInfo];
```
