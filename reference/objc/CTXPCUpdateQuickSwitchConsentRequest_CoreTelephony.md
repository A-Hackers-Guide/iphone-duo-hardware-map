# `CTXPCUpdateQuickSwitchConsentRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CTXPCRequestMessage`
- 0 instance variables, 2 properties, 6 instance methods, 1 class methods

## Properties

```
@property (TB,R,N) accepted;
@property (T@"NSString",R,N) iccid;
```

## Class methods

```
+[CTXPCUpdateQuickSwitchConsentRequest allowedClassesForArguments];
```

## Instance methods

```
-[CTXPCUpdateQuickSwitchConsentRequest requiredEntitlement];
-[CTXPCUpdateQuickSwitchConsentRequest ct_shortName];
-[CTXPCUpdateQuickSwitchConsentRequest iccid];
-[CTXPCUpdateQuickSwitchConsentRequest performRequestWithHandler:completionHandler:];
-[CTXPCUpdateQuickSwitchConsentRequest accepted];
-[CTXPCUpdateQuickSwitchConsentRequest initWithAccepted:iccid:];
```
