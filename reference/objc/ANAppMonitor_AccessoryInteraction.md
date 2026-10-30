# `ANAppMonitor`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"RBSProcessMonitor" _processMonitor;
@"NSObject<OS_dispatch_queue>" _queue;
@? _findMyAppDidBackgroundOrExitHandler;
```

## Properties

```
@property (T@?,C,V_findMyAppDidBackgroundOrExitHandler) findMyAppDidBackgroundOrExitHandler;
```

## Instance methods

```
-[ANAppMonitor initWithQueue:];
-[ANAppMonitor dealloc];
-[ANAppMonitor findMyAppDidBackgroundOrExitHandler];
-[ANAppMonitor processMonitor:didProvideUpdate:forProcessHandle:];
-[ANAppMonitor setFindMyAppDidBackgroundOrExitHandler:];
```
