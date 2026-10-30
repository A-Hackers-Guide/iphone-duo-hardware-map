# `CMMagicMountManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
{CMMagicMountStateStruct="timestamp"d"mountStatus"q"propertyC"C} _currentMagicMountState;
@? _magicMountStateHandler;
@"NSOperationQueue" _magicMountStateQueue;
^{Dispatcher=^^?@} _magicMountStateDispatcher;
^v _connection;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
B _serviceEnabled;
B _apWakesAllowed;
```

## Instance methods

```
-[CMMagicMountManagerInternal connect];
-[CMMagicMountManagerInternal init];
-[CMMagicMountManagerInternal dealloc];
-[CMMagicMountManagerInternal teardownPrivate];
-[CMMagicMountManagerInternal sendAPWakesRequestPrivate];
-[CMMagicMountManagerInternal sendServiceRequestPrivate];
```
