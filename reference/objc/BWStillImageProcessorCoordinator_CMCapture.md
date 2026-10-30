# `BWStillImageProcessorCoordinator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _processorControllersByType;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _processorControllersLock;
```

## Properties

```
@property (T@"NSSet",R,N) processorControllerNames;
```

## Instance methods

```
-[BWStillImageProcessorCoordinator dealloc];
-[BWStillImageProcessorCoordinator description];
-[BWStillImageProcessorCoordinator controllerForType:];
-[BWStillImageProcessorCoordinator addController:];
-[BWStillImageProcessorCoordinator initWithProcessorControllers:];
-[BWStillImageProcessorCoordinator processorControllerNames];
-[BWStillImageProcessorCoordinator releaseControllers];
```
