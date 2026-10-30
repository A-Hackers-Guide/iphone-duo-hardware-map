# `CTQuickSwitchManager`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CoreTelephonyClientQuickSwitchStateDelegateInternal`
- 3 instance variables, 5 properties, 7 instance methods, 2 class methods

## Instance variables

```
{queue="fObj"{object="fObj"^{dispatch_object_s}}} _queue;
@"CoreTelephonyClient" _client;
@"<CTQuickSwitchManagerDelegate>" _delegate;
```

## Properties

```
@property (T@"<CTQuickSwitchManagerDelegate>",W,N) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CTQuickSwitchManager registerForLaunchOnQuickSwitchStateEvents:];
+[CTQuickSwitchManager unregisterForLaunchOnQuickSwitchStateEvents:];
```

## Instance methods

```
-[CTQuickSwitchManager init];
-[CTQuickSwitchManager dealloc];
-[CTQuickSwitchManager setDelegate:];
-[CTQuickSwitchManager delegate];
-[CTQuickSwitchManager quickSwitchStateDidChange:];
-[CTQuickSwitchManager getDeviceState:];
-[CTQuickSwitchManager getPhoneNumberStateForSuffix:completion:];
```
