# `CMPocketStateManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_source>" fQueryTimer;
@"NSObject<OS_dispatch_queue>" fPrivateQueue;
i fCachedState;
{unique_ptr<CLMotionNotifier::Dispatcher, std::default_delete<CLMotionNotifier::Dispatcher>>=""{?="__ptr_"^{Dispatcher}}} fDispatcher;
d fMaxMonitorTime;
@"NSMutableArray" fQueryBlocks;
@"<CMPocketStateDelegate>" _delegate;
```

## Properties

```
@property (T@"<CMPocketStateDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[CMPocketStateManager isPocketStateAvailable];
+[CMPocketStateManager isPocketStateSupported];
```

## Instance methods

```
-[CMPocketStateManager init];
-[CMPocketStateManager dealloc];
-[CMPocketStateManager setDelegate:];
-[CMPocketStateManager delegate];
-[CMPocketStateManager onNotification:];
-[CMPocketStateManager _disableDispatcher];
-[CMPocketStateManager _prepareDispatcher];
-[CMPocketStateManager addToAggdScalarWithName:andScalar:];
-[CMPocketStateManager externalStateToString:];
-[CMPocketStateManager onPocketStateUpdated:];
-[CMPocketStateManager queryStateOntoQueue:andMonitorFor:withTimeout:andHandler:];
-[CMPocketStateManager queryStateOntoQueue:withTimeout:andHandler:];
-[CMPocketStateManager translateExternalState:];
-[CMPocketStateManager translateInternalState:];
```
