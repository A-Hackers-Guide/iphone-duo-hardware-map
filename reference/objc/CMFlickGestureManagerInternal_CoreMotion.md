# `CMFlickGestureManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@? fEventHandler;
@"NSOperationQueue" fEventQueue;
^v fConnection;
@"NSObject<OS_dispatch_queue>" fConnectionQueue;
B fServiceEnabled;
d fTimestamp;
q fEventType;
^{Dispatcher=^^?@} fFlickGestureStateDispatcher;
B fRegisteredForNotifications;
```

## Instance methods

```
-[CMFlickGestureManagerInternal init];
-[CMFlickGestureManagerInternal dealloc];
-[CMFlickGestureManagerInternal teardownPrivate];
```
