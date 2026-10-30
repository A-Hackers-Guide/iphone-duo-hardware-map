# `CMHealthTrackerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
^v fLocationdConnection;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
@"NSObject<OS_dispatch_queue>" fAppQueue;
```

## Instance methods

```
-[CMHealthTrackerInternal init];
-[CMHealthTrackerInternal dealloc];
-[CMHealthTrackerInternal _teardown];
-[CMHealthTrackerInternal _queryMetMinutesFromDate:toDate:handler:];
-[CMHealthTrackerInternal _queryVO2MaxInputsFromRecord:handler:];
```
