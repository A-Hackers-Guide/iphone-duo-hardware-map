# `ULElevationUpdaterDelegate`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ULElevationRoutineBridgeDelegate`
- 3 instance variables, 4 properties, 2 instance methods, 0 class methods

## Instance variables

```
^{ULElevationUpdater=^^?^{ULDatabaseStoreInterface}@} fElevationUpdater;
f fElevationChangeThreshold;
@"NSObject<OS_dispatch_queue>" fQueue;
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
-[ULElevationUpdaterDelegate handleElevationSamples:error:enumerationCompleted:trajectoryIndex:semaphore:];
-[ULElevationUpdaterDelegate initWithUpdater:elevationChangeThreshold:queue:];
```
