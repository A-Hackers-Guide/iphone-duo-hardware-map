# `CMIndoorOutdoorManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _internalQueue;
@"<CMIndoorOutdoorDelegate>" _delegate;
@"CMIndoorOutdoorManager" _sender;
^v _connection;
B _startedUpdates;
```

## Instance methods

```
-[CMIndoorOutdoorManagerInternal init];
-[CMIndoorOutdoorManagerInternal dealloc];
-[CMIndoorOutdoorManagerInternal _teardown];
-[CMIndoorOutdoorManagerInternal _lastKnownIndoorOutdoorStateWithHandler:];
-[CMIndoorOutdoorManagerInternal _startIndoorOutdoorUpdates];
-[CMIndoorOutdoorManagerInternal _stopIndoorOutdoorUpdates];
```
