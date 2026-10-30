# `CMDistributedSensingManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
^v _locationdConnection;
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"NSObject<OS_dispatch_queue>" _clientQueue;
@"<CMDistributedSensingDelegate>" _delegate;
@"CMDistributedSensingManager" _manager;
```

## Instance methods

```
-[CMDistributedSensingManagerInternal init];
-[CMDistributedSensingManagerInternal dealloc];
-[CMDistributedSensingManagerInternal _teardown];
-[CMDistributedSensingManagerInternal _registerForVehicleStateUpdates];
-[CMDistributedSensingManagerInternal _handleDaemonMessage:data:];
-[CMDistributedSensingManagerInternal _unregisterForVehicleStateUpdates];
```
