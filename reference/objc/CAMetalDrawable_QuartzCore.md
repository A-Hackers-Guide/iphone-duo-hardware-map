# `CAMetalDrawable`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMetalDrawable`, `CAMetalDrawableSPI`, `MTLDrawableSPI`
- 30 instance variables, 29 properties, 67 instance methods, 0 class methods

## Instance variables

```
^{_CAMetalDrawablePrivate={Atomic={?=i}}IIIQQQQd^{_CAMetalLayerPrivate}^{__IOSurface}@@@Q@^{CGColorSpace}@@Cb1b1b1b1b1b1b1b1b1b1b1} _priv;
@"<MTLTexture>" _cachedTexture;
@"CAMetalLayer" _layer;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _dirtyRect;
Q _drawableID;
@"IOSurfaceSharedEvent" _sharedEvent;
I _insertSeed;
@"NSMutableArray" _presentedHandlers;
Q _status;
d _presentedTime;
B _presentScheduledInsertSeedValid;
I _presentScheduledInsertSeed;
@"NSMutableArray" _presentScheduledHandlers;
{atomic<bool>="__a_"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>="__a_value"AB}} _callbacksErased;
{SpinLock="_l"{?="x"i}} _handlersLock;
B _didComposite;
B _hasExplicitDeadlines;
B _needsLowLatency;
B _didFinish;
I _updateSeed;
I _surfaceID;
f _clientPreferredLatency;
d _timeAcquired;
d _timePresentCalled;
d _targetTimestamp;
d _targetSamplingTimestamp;
d _targetPresentationTimestamp;
d _presentDeadline;
d _minimumPresentationDuration;
{CATimingFramePacingLatency="latency"d"frame_duration"d} _preferredLatency;
```

## Properties

```
@property (TQ,N,V_drawableID) drawableID;
@property (T@"IOSurfaceSharedEvent",&,N,V_sharedEvent) sharedEvent;
@property (TI,N,V_insertSeed) insertSeed;
@property (TI,N,V_updateSeed) updateSeed;
@property (TB,N,V_didComposite) didComposite;
@property (TQ,N,V_status) status;
@property (Td,N,V_presentedTime) presentedTime;
@property (TI,N,V_presentScheduledInsertSeed) presentScheduledInsertSeed;
@property (TB,N,V_presentScheduledInsertSeedValid) presentScheduledInsertSeedValid;
@property (TI,N,V_surfaceID) surfaceID;
@property (Td,N,V_timeAcquired) timeAcquired;
@property (Td,N,V_timePresentCalled) timePresentCalled;
@property (Td,N,V_targetTimestamp) targetTimestamp;
@property (Td,N,V_targetSamplingTimestamp) targetSamplingTimestamp;
@property (Td,N,V_targetPresentationTimestamp) targetPresentationTimestamp;
@property (Td,N,V_presentDeadline) presentDeadline;
@property (TB,N,V_hasExplicitDeadlines) hasExplicitDeadlines;
@property (Td,N,V_minimumPresentationDuration) minimumPresentationDuration;
@property (T{CATimingFramePacingLatency=dd},N,V_preferredLatency) preferredLatency;
@property (TB,N,V_needsLowLatency) needsLowLatency;
@property (Tf,N,V_clientPreferredLatency) clientPreferredLatency;
@property (TB,N,V_didFinish) didFinish;
@property (T@"<MTLTexture>",R) texture;
@property (T@"CAMetalLayer",R) layer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_dirtyRect) dirtyRect;
```

## Instance methods

```
-[CAMetalDrawable present];
-[CAMetalDrawable presentScheduledInsertSeed];
-[CAMetalDrawable targetTimestamp];
-[CAMetalDrawable setTargetPresentationTimestamp:];
-[CAMetalDrawable addPresentedHandler:];
-[CAMetalDrawable didScheduledPresent];
-[CAMetalDrawable updateSeed];
-[CAMetalDrawable setTimeAcquired:];
-[CAMetalDrawable setTargetSamplingTimestamp:];
-[CAMetalDrawable sharedEvent];
-[CAMetalDrawable surfaceID];
-[CAMetalDrawable layer];
-[CAMetalDrawable needsLowLatency];
-[CAMetalDrawable minimumPresentationDuration];
-[CAMetalDrawable targetPresentationTimestamp];
-[CAMetalDrawable cachedTexture];
-[CAMetalDrawable setTargetTimestamp:];
-[CAMetalDrawable newTextureWithResourceIndex:];
-[CAMetalDrawable didPresentAtTime:];
-[CAMetalDrawable setInsertSeed:];
-[CAMetalDrawable dirtyRect];
-[CAMetalDrawable waitOnCommandQueue:];
-[CAMetalDrawable setDirtyRect:];
-[CAMetalDrawable dealloc];
-[CAMetalDrawable timeAcquired];
-[CAMetalDrawable preferredLatency];
-[CAMetalDrawable presentWithOptions:];
-[CAMetalDrawable signalOnCommandQueue:];
-[CAMetalDrawable clientPreferredLatency];
-[CAMetalDrawable setSurfaceID:];
-[CAMetalDrawable initWithDrawablePrivate:layer:waitStart:];
-[CAMetalDrawable targetSamplingTimestamp];
-[CAMetalDrawable status];
-[CAMetalDrawable texture];
-[CAMetalDrawable setSharedEvent:];
-[CAMetalDrawable setPresentDeadline:];
-[CAMetalDrawable setDidComposite:];
-[CAMetalDrawable hasPresentedHandlers];
-[CAMetalDrawable presentScheduledInsertSeedValid];
-[CAMetalDrawable releasePrivateReferences:];
-[CAMetalDrawable setNeedsLowLatency:];
-[CAMetalDrawable priv];
-[CAMetalDrawable release];
-[CAMetalDrawable setDidFinish:];
-[CAMetalDrawable didComposite];
-[CAMetalDrawable setHasExplicitDeadlines:];
-[CAMetalDrawable setDrawableID:];
-[CAMetalDrawable didFinish];
-[CAMetalDrawable setClientPreferredLatency:];
-[CAMetalDrawable presentAfterMinimumDuration:];
-[CAMetalDrawable drawableID];
-[CAMetalDrawable setUpdateSeed:];
-[CAMetalDrawable presentAtTime:];
-[CAMetalDrawable setPreferredLatency:];
-[CAMetalDrawable setPresentedTime:];
-[CAMetalDrawable presentDeadline];
-[CAMetalDrawable setPresentScheduledInsertSeed:];
-[CAMetalDrawable setMinimumPresentationDuration:];
-[CAMetalDrawable setTimePresentCalled:];
-[CAMetalDrawable setPresentScheduledInsertSeedValid:];
-[CAMetalDrawable hasExplicitDeadlines];
-[CAMetalDrawable insertSeed];
-[CAMetalDrawable setStatus:];
-[CAMetalDrawable estimateTargets];
-[CAMetalDrawable addPresentScheduledHandler:];
-[CAMetalDrawable timePresentCalled];
-[CAMetalDrawable presentedTime];
```
