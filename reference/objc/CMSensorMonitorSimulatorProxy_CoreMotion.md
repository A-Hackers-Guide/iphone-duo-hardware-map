# `CMSensorMonitorSimulatorProxy`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<CLConnectionClient, std::default_delete<CLConnectionClient>>=""{?="__ptr_"^{CLConnectionClient}}} fLocationdConnection;
@? fHandler;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
```

## Instance methods

```
-[CMSensorMonitorSimulatorProxy dealloc];
-[CMSensorMonitorSimulatorProxy _simulateMotionSensorDataForType:payload:withHandler:];
-[CMSensorMonitorSimulatorProxy initWithSensorMonitorTests];
```
