# `LAUIRenderLoop`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationPrivateUI.framework/LocalAuthenticationPrivateUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationPrivateUI.framework__LocalAuthenticationPrivateUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 10 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"<LAUIRenderLoopDelegate>" _delegate;
B _drawing;
B _invalidated;
@"CADisplayLink" _display_link;
B _has_high_fps_reason;
B _background;
B _delegate_observes_effective_paused;
B _delegate_observes_runnable;
B _in_application_context;
B _effective_paused;
B _paused;
B _runnable;
I _high_fps_reason;
@"UIScreen" _screen;
{CAFrameRateRange="minimum"f"maximum"f"preferred"f} _preferred_fps_range;
```

## Properties

```
@property (TI,N,V_high_fps_reason) highFrameRateReason;
@property (T@"UIScreen",R,W,N,V_screen) screen;
@property (TB,R,N,GisInvalidated,V_invalidated) invalidated;
@property (TB,R,N,GisDrawing,V_drawing) drawing;
@property (TB,N,GisInApplicationContext,V_in_application_context) inApplicationContext;
@property (T{CAFrameRateRange=fff},N,V_preferred_fps_range) preferredFrameRateRange;
@property (TB,N,GisPaused,V_paused) paused;
@property (TB,R,N,GeffectiveIsPaused,V_effective_paused) effectivePaused;
@property (TB,R,N,GisRunnable,V_runnable) runnable;
@property (T@"<LAUIRenderLoopDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[LAUIRenderLoop _applicationDidBecomeActive:];
-[LAUIRenderLoop _applicationWillEnterForeground:];
-[LAUIRenderLoop _applicationDidEnterBackground:];
-[LAUIRenderLoop setHighFrameRateReason:];
-[LAUIRenderLoop screen];
-[LAUIRenderLoop isPaused];
-[LAUIRenderLoop init];
-[LAUIRenderLoop setPreferredFrameRateRange:];
-[LAUIRenderLoop dealloc];
-[LAUIRenderLoop isDrawing];
-[LAUIRenderLoop highFrameRateReason];
-[LAUIRenderLoop preferredFrameRateRange];
-[LAUIRenderLoop isInvalidated];
-[LAUIRenderLoop invalidate];
-[LAUIRenderLoop setPaused:];
-[LAUIRenderLoop setDelegate:];
-[LAUIRenderLoop delegate];
-[LAUIRenderLoop setInApplicationContext:];
-[LAUIRenderLoop _didInvalidate];
-[LAUIRenderLoop isRunnable];
-[LAUIRenderLoop _isForcingPause];
-[LAUIRenderLoop attachToScreen:];
-[LAUIRenderLoop _didDraw];
-[LAUIRenderLoop _willDraw];
-[LAUIRenderLoop effectiveIsPaused];
-[LAUIRenderLoop isInApplicationContext];
```
