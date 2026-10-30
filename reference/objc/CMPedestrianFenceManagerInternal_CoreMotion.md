# `CMPedestrianFenceManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
^v fLocationdConnection;
@? fFenceHandler;
@? fStatusHandler;
@"NSObject<OS_dispatch_queue>" fPrivateQueue;
```

## Instance methods

```
-[CMPedestrianFenceManagerInternal init];
-[CMPedestrianFenceManagerInternal dealloc];
-[CMPedestrianFenceManagerInternal _clearFence:force:];
-[CMPedestrianFenceManagerInternal _setFence:withRadius:wake:delay:withCompletion:];
-[CMPedestrianFenceManagerInternal _setInSession:withStatusHandler:];
```
