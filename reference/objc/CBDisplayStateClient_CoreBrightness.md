# `CBDisplayStateClient`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"BrightnessSystemClientInternal" _bsci;
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _queue;
B _active;
@"CBDisplayHandle" _displayHandle;
B _highLuminanceAODsupported;
@"<CBDisplayStateClientDelegate>" _completionDelegate;
```

## Properties

```
@property (T@"<CBDisplayStateClientDelegate>",&,N,V_completionDelegate) completionDelegate;
@property (TB,R,N) supported;
@property (TB,R,N,V_highLuminanceAODsupported) highLuminanceAODsupported;
@property (Tq,R,N) displayMode;
```

## Instance methods

```
-[CBDisplayStateClient supported];
-[CBDisplayStateClient init];
-[CBDisplayStateClient dealloc];
-[CBDisplayStateClient displayMode];
-[CBDisplayStateClient activate];
-[CBDisplayStateClient cancel];
-[CBDisplayStateClient initWithDisplayID:];
-[CBDisplayStateClient setCompletionDelegate:];
-[CBDisplayStateClient completionDelegate];
-[CBDisplayStateClient displayModeWithError:];
-[CBDisplayStateClient highLuminanceAODsupported];
-[CBDisplayStateClient switchToFlipbookState:error:];
-[CBDisplayStateClient transitionToDisplayMode:withDuration:error:];
-[CBDisplayStateClient _displayModeChangeCompletionHandler:];
-[CBDisplayStateClient _removeCompletionDelegate];
```
