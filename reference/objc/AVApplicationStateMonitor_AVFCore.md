# `AVApplicationStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _ivarAccessQueue;
B _hostApplicationInForeground;
@ _didEnterBackgroundNotificationToken;
@ _willEnterForegroundNotificationToken;
```

## Properties

```
@property (TB,GisHostApplicationInForeground,SsetHostApplicationInForeground:) hostApplicationInForeground;
```

## Class methods

```
+[AVApplicationStateMonitor initialize];
+[AVApplicationStateMonitor sharedApplicationStateMonitor];
```

## Instance methods

```
-[AVApplicationStateMonitor _willEnterForeground:];
-[AVApplicationStateMonitor init];
-[AVApplicationStateMonitor dealloc];
-[AVApplicationStateMonitor _didEnterBackground:];
-[AVApplicationStateMonitor _hostApplicationHasForegroundExemption];
-[AVApplicationStateMonitor setHostApplicationInForeground:];
-[AVApplicationStateMonitor isHostApplicationInForeground];
```
