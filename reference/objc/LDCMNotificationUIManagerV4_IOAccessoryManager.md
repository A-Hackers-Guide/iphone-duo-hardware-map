# `LDCMNotificationUIManagerV4`

- Image: [`/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`](../userland/System__Library__PrivateFrameworks__IOAccessoryManager.framework__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"IOPortLDCMManagerV4" _ldcmManager;
{?="isNotificationPosted"B"lastNotificationTime"d"isReinsertion"B"notification"^{__CFUserNotification}"notificationRunLoopSource"^{__CFRunLoopSource}"runloop"^{__CFRunLoop}"notificationUIManager"@"LDCMNotificationUIManagerV4"} _liquidNotificationContext;
```

## Properties

```
@property (T@"IOPortLDCMManagerV4",W,N,V_ldcmManager) ldcmManager;
@property (T{?=BdB^{__CFUserNotification}^{__CFRunLoopSource}^{__CFRunLoop}@},N,V_liquidNotificationContext) liquidNotificationContext;
```

## Instance methods

```
-[LDCMNotificationUIManagerV4 initWithParams::];
-[LDCMNotificationUIManagerV4 setOverride:];
-[LDCMNotificationUIManagerV4 setLdcmManager:];
-[LDCMNotificationUIManagerV4 ldcmManager];
-[LDCMNotificationUIManagerV4 liquidNotificationContext];
-[LDCMNotificationUIManagerV4 setLiquidNotificationContext:];
-[LDCMNotificationUIManagerV4 showUI::];
```
