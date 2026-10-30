# `CMActivityManagerInternal`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
^v fLocationdConnection;
@? fActivityHandler;
@"NSObject<OS_dispatch_queue>" fPrivateQueue;
B fSubscribedToMotionState;
@"NSObject<OS_dispatch_semaphore>" fSidebandOverrideSemaphore;
@"NSObject<OS_dispatch_queue>" fSidebandOverrideQueue;
B fSidebandOverrideWaiting;
q fSidebandOverrideResult;
@"NSObject<OS_dispatch_semaphore>" fMotionStateSimSemaphore;
@"NSObject<OS_dispatch_queue>" fMotionStateSimQueue;
B fMotionStateSimWaiting;
q fMotionStateSimResult;
q fMotionStateYouthSimResult;
```

## Instance methods

```
-[CMActivityManagerInternal connect];
-[CMActivityManagerInternal init];
-[CMActivityManagerInternal dealloc];
-[CMActivityManagerInternal disconnect];
-[CMActivityManagerInternal overrideOscarSideband:withState:];
-[CMActivityManagerInternal simulateMotionState:withState:withHint:];
-[CMActivityManagerInternal simulateMotionStateYouthWithState:];
-[CMActivityManagerInternal startActivityUpdatesWithHandlerPrivate:];
-[CMActivityManagerInternal stopActivityUpdatesPrivate];
```
