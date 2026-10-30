# `FigExternalSyncDeviceDiscoverySessionDelegateHandler`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigExternalSyncDeviceDiscoverySessionManagerDelegate`
- 2 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigCaptureSource=} _source;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _sourceLock;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FigExternalSyncDeviceDiscoverySessionDelegateHandler initWithSource:];
-[FigExternalSyncDeviceDiscoverySessionDelegateHandler forceCleanup];
-[FigExternalSyncDeviceDiscoverySessionDelegateHandler externalSyncDeviceDiscoverySessionManager:connectedDevicesDidChange:];
-[FigExternalSyncDeviceDiscoverySessionDelegateHandler externalSyncDeviceDiscoverySessionManager:connectedSyncEntitiesDidChange:];
```
