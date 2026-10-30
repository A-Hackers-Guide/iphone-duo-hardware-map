# `CMGNSSMotionManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<CLConnectionClient, std::default_delete<CLConnectionClient>>=""{?="__ptr_"^{CLConnectionClient}}} _locationdConnection;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (TB,R,N,GisGNSSMotionAvailable) gnssMotionAvailable;
```

## Instance methods

```
-[CMGNSSMotionManager init];
-[CMGNSSMotionManager dealloc];
-[CMGNSSMotionManager isGNSSMotionAvailable];
-[CMGNSSMotionManager startGNSSMotionUpdatesWithUpdateFrequency:];
-[CMGNSSMotionManager stopGNSSMotionUpdates];
```
