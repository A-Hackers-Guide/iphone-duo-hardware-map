# `CMOdometryManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 28 instance methods, 3 class methods

## Instance variables

```
@ _internal;
{unique_ptr<CLConnectionClient, std::default_delete<CLConnectionClient>>=""{?="__ptr_"^{CLConnectionClient}}} _locationdConnection;
@"NSObject<OS_dispatch_queue>" _xpcQueue;
@? _backgroundInertialOdometryHandler;
@"NSOperationQueue" _backgroundInertialOdometryQueue;
Q _referenceFrameBIO;
{unique_ptr<CLSettings, std::default_delete<CLSettings>>=""{?="__ptr_"^{CLSettings}}} _motionSettings;
```

## Properties

```
@property (Td,N) odometryUpdateInterval;
```

## Class methods

```
+[CMOdometryManager isAvailable];
+[CMOdometryManager isBackgroundAvailable];
+[CMOdometryManager isNeuralPDRAvailable];
```

## Instance methods

```
-[CMOdometryManager init];
-[CMOdometryManager initPrivate];
-[CMOdometryManager dealloc];
-[CMOdometryManager requestNPDRUpdate];
-[CMOdometryManager stopBackgroundUpdates];
-[CMOdometryManager deallocPrivate];
-[CMOdometryManager enableMotionSimulation:];
-[CMOdometryManager enableMotionSimulationPrivate:];
-[CMOdometryManager feedOdometryData:];
-[CMOdometryManager odometryUpdateInterval];
-[CMOdometryManager requestNPDRUpdatePrivate];
-[CMOdometryManager sendOdometryToClientPrivate];
-[CMOdometryManager setOdometryUpdateInterval:];
-[CMOdometryManager setOdometryUpdateIntervalPrivate:];
-[CMOdometryManager setupBIO];
-[CMOdometryManager startBackgroundUpdatesPrivateUsingReferenceFrame:dataSource:toQueue:withHandler:];
-[CMOdometryManager startBackgroundUpdatesPrivateUsingReferenceFrame:enableNeuralPDR:toQueue:withHandler:];
-[CMOdometryManager startBackgroundUpdatesToQueue:withHandler:];
-[CMOdometryManager startBackgroundUpdatesUsingReferenceFrame:dataSource:toQueue:withHandler:];
-[CMOdometryManager startBackgroundUpdatesUsingReferenceFrame:enableNeuralPDR:toQueue:withHandler:];
-[CMOdometryManager startBackgroundUpdatesUsingReferenceFrame:toQueue:withHandler:];
-[CMOdometryManager startOdometryUpdatesPrivateUsingReferenceFrame:toQueue:withHandler:];
-[CMOdometryManager startOdometryUpdatesToQueue:withHandler:];
-[CMOdometryManager startOdometryUpdatesUsingReferenceFrame:toQueue:withHandler:];
-[CMOdometryManager stopBackgroundUpdatesPrivate];
-[CMOdometryManager stopOdometryUpdates];
-[CMOdometryManager stopOdometryUpdatesPrivate];
-[CMOdometryManager teardownBIO];
```
