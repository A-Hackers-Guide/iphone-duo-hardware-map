# `ANSystemUtils`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ANSystemUtilsProtocol`
- 0 instance variables, 4 properties, 10 instance methods, 0 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ANSystemUtils dataWithContentsOfURL:options:error:];
-[ANSystemUtils date];
-[ANSystemUtils dispatchAfter:queue:block:];
-[ANSystemUtils cfPreferencesCopyValueWithKey:applicationID:userName:hostName:];
-[ANSystemUtils cfPreferencesSetValueWithKey:value:applicationID:userName:hostName:];
-[ANSystemUtils cfAbsoluteTimeGetCurrent];
-[ANSystemUtils cfPreferencesSynchronizeWithApplicationID:userName:hostName:];
-[ANSystemUtils machContinuousTime];
-[ANSystemUtils showUserNotificationWithTimeout:flags:dictionary:handler:];
-[ANSystemUtils triggerAutoBugCaptureWithQueue:description:];
```
