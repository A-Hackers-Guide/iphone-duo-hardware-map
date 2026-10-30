# `CMPickupManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" fPrivateQueue;
^{Dispatcher=^^?@} fDispatcher;
@"<CMPickupDelegate>" _delegate;
```

## Properties

```
@property (T@"<CMPickupDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[CMPickupManager isPickupAvailable];
```

## Instance methods

```
-[CMPickupManager init];
-[CMPickupManager dealloc];
-[CMPickupManager setDelegate:];
-[CMPickupManager delegate];
-[CMPickupManager onPickupStateUpdated:];
-[CMPickupManager startPickupUpdates];
-[CMPickupManager stopPickupUpdates];
```
