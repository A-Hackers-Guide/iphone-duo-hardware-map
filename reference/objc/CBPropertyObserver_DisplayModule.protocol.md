# `CBPropertyObserver` (protocol)

- Image: [`/System/Library/ControlCenter/Bundles/DisplayModule.bundle/DisplayModule`](../userland/System__Library__ControlCenter__Bundles__DisplayModule.bundle__DisplayModule.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 3 instance methods, 0 class methods

## Properties

```
@property (T@"NSSet",R) properties;
@property (T@"NSObject<OS_dispatch_queue>",R) notifyQueue;
```

## Instance methods

```
-[CBPropertyObserver properties];
-[CBPropertyObserver notifyQueue];
-[CBPropertyObserver observeValue:forKey:andHandle:withContext:];
```
