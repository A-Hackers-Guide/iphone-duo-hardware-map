# `CMDeviceOrientationManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} fSampleLock;
^{Dispatcher=^^?@} fDeviceOrientationDispatcher;
@? fDeviceOrientationHandler;
@"NSOperationQueue" fDeviceOrientationQueue;
@"NSObject<OS_dispatch_semaphore>" fDeviceOrientationSemaphore;
B fDidSignalSemaphore;
i fOrientationCallbackMode;
B fEnableOrientationNotification;
{Sample="timestamp"d"orientation"i} fLatestDeviceOrientationSample;
{Sample="timestamp"d"orientation"i} fLastSignificantOrientationSample;
```

## Instance methods

```
-[CMDeviceOrientationManagerInternal init];
-[CMDeviceOrientationManagerInternal dealloc];
```
