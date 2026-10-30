# `SBUserNotificationCenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"NSMutableArray" _userNotifications;
@"NSObject<OS_dispatch_mach>" _machChannel;
```

## Instance methods

```
-[SBUserNotificationCenter initWithApplicationController:];
-[SBUserNotificationCenter start];
-[SBUserNotificationCenter _dispatchUserNotification:flags:replyPort:auditToken:];
-[SBUserNotificationCenter _userNotificationDone:];
```
