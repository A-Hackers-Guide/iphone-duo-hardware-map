# `BWFigCaptureAttachedAccessoriesMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCConnectionInfoDelegateProtocol`
- 4 instance variables, 6 properties, 6 instance methods, 2 class methods

## Instance variables

```
@"ACCConnectionInfo" _connectionInfoProvider;
@"NSObject<OS_dispatch_queue>" _notificationQueue;
@"NSString" _walletAccessoryUUID;
@"NSString" _batteryPackAccessoryUUID;
```

## Properties

```
@property (TB,R,N) walletAccessoryConnected;
@property (TB,R,N) batteryPackAccessoryConnected;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWFigCaptureAttachedAccessoriesMonitor initialize];
+[BWFigCaptureAttachedAccessoriesMonitor sharedAttachedAccessoriesMonitor];
```

## Instance methods

```
-[BWFigCaptureAttachedAccessoriesMonitor init];
-[BWFigCaptureAttachedAccessoriesMonitor dealloc];
-[BWFigCaptureAttachedAccessoriesMonitor accessoryConnectionDetached:];
-[BWFigCaptureAttachedAccessoriesMonitor accessoryEndpointAttached:transportType:protocol:forConnection:];
-[BWFigCaptureAttachedAccessoriesMonitor batteryPackAccessoryConnected];
-[BWFigCaptureAttachedAccessoriesMonitor walletAccessoryConnected];
```
