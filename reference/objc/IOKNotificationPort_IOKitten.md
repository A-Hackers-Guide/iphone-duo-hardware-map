# `IOKNotificationPort`

- Image: [`/System/Library/PrivateFrameworks/IOKitten.framework/IOKitten`](../userland/System__Library__PrivateFrameworks__IOKitten.framework__IOKitten.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
^{IONotificationPort=} _port;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T^{IONotificationPort=},R,N,V_port) port;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (TI,R,N) machPort;
```

## Instance methods

```
-[IOKNotificationPort init];
-[IOKNotificationPort dealloc];
-[IOKNotificationPort machPort];
-[IOKNotificationPort queue];
-[IOKNotificationPort port];
-[IOKNotificationPort initOnDispatchQueue:];
-[IOKNotificationPort initWithMasterPort:onDispatchQueue:];
```
