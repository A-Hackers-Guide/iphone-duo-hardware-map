# `IOSurfaceSharedEventListener`

- Image: [`/System/Library/Frameworks/IOSurface.framework/IOSurface`](../userland/System__Library__Frameworks__IOSurface.framework__IOSurface.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
^{IONotificationPort=} _notificationPort;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
```

## Instance methods

```
-[IOSurfaceSharedEventListener init];
-[IOSurfaceSharedEventListener dealloc];
-[IOSurfaceSharedEventListener _notifyEventPort:event:atValue:block:];
-[IOSurfaceSharedEventListener initWithDispatchQueue:];
```
