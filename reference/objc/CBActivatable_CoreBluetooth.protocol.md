# `CBActivatable` (protocol)

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 2 properties, 6 instance methods, 0 class methods

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N) dispatchQueue;
@property (T@?,C,N) invalidationHandler;
```

## Instance methods

```
-[CBActivatable dispatchQueue];
-[CBActivatable activateWithCompletion:];
-[CBActivatable setInvalidationHandler:];
-[CBActivatable setDispatchQueue:];
-[CBActivatable invalidate];
-[CBActivatable invalidationHandler];
```
