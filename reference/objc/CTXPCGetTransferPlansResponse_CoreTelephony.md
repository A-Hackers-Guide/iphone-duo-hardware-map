# `CTXPCGetTransferPlansResponse`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCResponseMessage`
- 0 instance variables, 2 properties, 4 instance methods, 1 class methods

## Properties

```
@property (T@"CTRemoteDeviceList",R,N) devices;
@property (TB,R) isFlexPolicyOn;
```

## Class methods

```
+[CTXPCGetTransferPlansResponse allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCGetTransferPlansResponse ct_shortName];
-[CTXPCGetTransferPlansResponse devices];
-[CTXPCGetTransferPlansResponse initWithRemtoeDevices:isFlexPolicyOn:];
-[CTXPCGetTransferPlansResponse isFlexPolicyOn];
```
