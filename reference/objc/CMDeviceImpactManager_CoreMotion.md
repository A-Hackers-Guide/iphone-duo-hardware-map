# `CMDeviceImpactManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 8 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<CLConnectionClient, std::default_delete<CLConnectionClient>>=""{?="__ptr_"^{CLConnectionClient}}} _locationdConnection;
@"NSObject<OS_dispatch_queue>" _queue;
@? _handler;
@"NSOperationQueue" _handlerQueue;
```

## Properties

```
@property (TB,R,N,GisDeviceImpactAvailable) deviceImpactAvailable;
```

## Instance methods

```
-[CMDeviceImpactManager init];
-[CMDeviceImpactManager dealloc];
-[CMDeviceImpactManager clearDeviceImpactCacheWithCompletion:];
-[CMDeviceImpactManager isDeviceImpactAvailable];
-[CMDeviceImpactManager queryDeviceImpactsWithCompletion:];
-[CMDeviceImpactManager simulateHighAccelDeviceImpactWithTimeOffset:peakAcceleration:completion:];
-[CMDeviceImpactManager startDeviceImpactUpdatesToQueue:withHandler:];
-[CMDeviceImpactManager stopDeviceImpactUpdates];
```
