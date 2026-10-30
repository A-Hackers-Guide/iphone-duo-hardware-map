# `CTXPCConfigureEuiccSimSlotRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCRequestMessage`
- 0 instance variables, 1 properties, 5 instance methods, 1 class methods

## Properties

```
@property (TB,R,N) enableEuicc;
```

## Class methods

```
+[CTXPCConfigureEuiccSimSlotRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCConfigureEuiccSimSlotRequest requiredEntitlement];
-[CTXPCConfigureEuiccSimSlotRequest ct_shortName];
-[CTXPCConfigureEuiccSimSlotRequest performRequestWithHandler:completionHandler:];
-[CTXPCConfigureEuiccSimSlotRequest enableEuicc];
-[CTXPCConfigureEuiccSimSlotRequest initWithEnableEuicc:];
```
