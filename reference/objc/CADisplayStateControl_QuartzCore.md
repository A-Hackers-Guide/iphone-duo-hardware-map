# `CADisplayStateControl`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
I _server_port;
{ClientIPC="_port"I"_queue"@"NSObject<OS_dispatch_queue>""_source"@"NSObject<OS_dispatch_source>"} _client_ipc;
I _display_id;
^v _display_state;
^v _shmem;
^{Transition=I*^?^?II{SpinLock={?=i}}q@?C} _display_state_transition;
^{Transition=I*^?^?II{SpinLock={?=i}}q@?C} _cloning_state_transition;
```

## Properties

```
@property (Tq,R,N) targetDisplayState;
@property (Tq,R,N) targetCloningState;
@property (Tq,R,N) targetPowerState;
@property (Tq,R,N) displayState;
@property (Tq,R,N) cloningState;
@property (Tq,R,N) powerState;
@property (TB,N,GisCloningDisabled) cloningDisabled;
```

## Instance methods

```
-[CADisplayStateControl powerState];
-[CADisplayStateControl isCloningDisabled];
-[CADisplayStateControl setCloningDisabled:];
-[CADisplayStateControl dealloc];
-[CADisplayStateControl displayState];
-[CADisplayStateControl _copyAllFrameRateAssertionInfo];
-[CADisplayStateControl _copyAllPowerAssertionInfo];
-[CADisplayStateControl _copyStateInfo];
-[CADisplayStateControl _initWithDisplayId:];
-[CADisplayStateControl acquireWirelessDisplayStateControl];
-[CADisplayStateControl cloningState];
-[CADisplayStateControl createFrameRateAssertionWithMaximumFrameRate:identifier:];
-[CADisplayStateControl createPowerAssertionWithReason:identifier:];
-[CADisplayStateControl displayCloningStateDidChange:seed:result:];
-[CADisplayStateControl displayStateDidChange:seed:result:];
-[CADisplayStateControl initializeClientPort];
-[CADisplayStateControl targetCloningState];
-[CADisplayStateControl targetDisplayState];
-[CADisplayStateControl targetPowerState];
-[CADisplayStateControl transitionToCloningState:withCompletion:];
-[CADisplayStateControl transitionToDisplayState:withCompletion:];
```
