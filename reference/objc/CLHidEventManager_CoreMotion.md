# `CLHidEventManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<CLHidEventManagerDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
@"HIDEventSystemClient" _manager;
@"NSMutableArray" _matching;
```

## Properties

```
@property (T@"<CLHidEventManagerDelegate>",N,V_delegate) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_delegateQueue) delegateQueue;
@property (T@"HIDEventSystemClient",R,N,V_manager) manager;
@property (T@"NSMutableArray",&,N,V_matching) matching;
```

## Instance methods

```
-[CLHidEventManager setMatching:];
-[CLHidEventManager dealloc];
-[CLHidEventManager manager];
-[CLHidEventManager setDelegate:];
-[CLHidEventManager delegate];
-[CLHidEventManager matching];
-[CLHidEventManager delegateQueue];
-[CLHidEventManager initWithDelegate:queue:matching:type:];
```
