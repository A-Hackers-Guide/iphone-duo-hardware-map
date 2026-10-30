# `CMAngleManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 1 properties, 11 instance methods, 0 class methods

## Instance variables

```
{CLStrongPtr<NSOperationQueue *>="fObjc"@"NSOperationQueue"} fQueue;
{CLStrongPtr<void (^)(CMAngle *)>="fObjc"@?} fHandler;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} fAngleDispatcher;
{CLStrongPtr<NSTimer *>="fObjc"@"NSTimer"} fAngleUpdateTimer;
d _angleUpdateInterval;
```

## Properties

```
@property (Td,N,V_angleUpdateInterval) angleUpdateInterval;
```

## Instance methods

```
-[CMAngleManagerInternal init];
-[CMAngleManagerInternal angleUpdateInterval];
-[CMAngleManagerInternal cancelPendingAngleUpdate];
-[CMAngleManagerInternal isAngleActive];
-[CMAngleManagerInternal notifyAngleChange:];
-[CMAngleManagerInternal onAngleChange:];
-[CMAngleManagerInternal scheduleAngleUpdate];
-[CMAngleManagerInternal setAngleUpdateInterval:];
-[CMAngleManagerInternal setAngleUpdateIntervalPrivate:];
-[CMAngleManagerInternal startAngleUpdatesPrivateToQueue:handler:];
-[CMAngleManagerInternal stopAngleUpdatesPrivate];
```
