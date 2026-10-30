# `ULBleIdentityBridge`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"CBDiscovery" _cbDiscovery;
@"NSObject<OS_dispatch_queue>" _queue;
@"<ULBleIdentityBridgeDelegate>" _delegate;
```

## Properties

```
@property (T@"CBDiscovery",&,N,V_cbDiscovery) cbDiscovery;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"<ULBleIdentityBridgeDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[ULBleIdentityBridge startMonitoring];
-[ULBleIdentityBridge initWithDelegate:];
-[ULBleIdentityBridge queue];
-[ULBleIdentityBridge stopMonitoring];
-[ULBleIdentityBridge setDelegate:];
-[ULBleIdentityBridge delegate];
-[ULBleIdentityBridge setQueue:];
-[ULBleIdentityBridge _deviceFoundHandler:];
-[ULBleIdentityBridge setCbDiscovery:];
-[ULBleIdentityBridge cbDiscovery];
```
