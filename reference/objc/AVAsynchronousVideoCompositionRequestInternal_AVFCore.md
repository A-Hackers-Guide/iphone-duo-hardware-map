# `AVAsynchronousVideoCompositionRequestInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" _session;
@"AVVideoCompositionRenderContext" _renderContext;
^{OpaqueFigVideoCompositorFrame=} _compositionFrame;
{?="value"q"timescale"i"flags"I"epoch"q} _compositionTime;
@"NSDictionary" _sourceVideoFrameTimedSamplesByTrackID;
@"NSArray" _sourceTrackIDsInClientOrder;
@"NSDictionary" _sourceSampleBufferTimedSamplesByTrackID;
@"NSArray" _sourceSampleBufferTrackIDsInClientOrder;
@"<AVVideoCompositionInstruction>" _instruction;
B _isFinished;
@"NSArray" _lookupableSpatialVideoConfigurations;
```

## Properties

```
@property (T@"AVWeakReference",&,N,V_session) session;
@property (T@"AVVideoCompositionRenderContext",&,N,V_renderContext) renderContext;
@property (T^{OpaqueFigVideoCompositorFrame=},N,V_compositionFrame) compositionFrame;
@property (T{?=qiIq},N,V_compositionTime) compositionTime;
@property (T@"NSDictionary",&,N,V_sourceVideoFrameTimedSamplesByTrackID) sourceVideoFrameTimedSamplesByTrackID;
@property (T@"NSArray",&,N,V_sourceTrackIDsInClientOrder) sourceTrackIDsInClientOrder;
@property (T@"NSDictionary",&,N,V_sourceSampleBufferTimedSamplesByTrackID) sourceSampleBufferTimedSamplesByTrackID;
@property (T@"NSArray",&,N,V_sourceSampleBufferTrackIDsInClientOrder) sourceSampleBufferTrackIDsInClientOrder;
@property (T@"<AVVideoCompositionInstruction>",&,N,V_instruction) instruction;
@property (TB,N,V_isFinished) isFinished;
@property (T@"NSArray",C,N,V_lookupableSpatialVideoConfigurations) lookupableSpatialVideoConfigurations;
```

## Instance methods

```
-[AVAsynchronousVideoCompositionRequestInternal isFinished];
-[AVAsynchronousVideoCompositionRequestInternal dealloc];
-[AVAsynchronousVideoCompositionRequestInternal setSession:];
-[AVAsynchronousVideoCompositionRequestInternal session];
-[AVAsynchronousVideoCompositionRequestInternal renderContext];
-[AVAsynchronousVideoCompositionRequestInternal setIsFinished:];
-[AVAsynchronousVideoCompositionRequestInternal setInstruction:];
-[AVAsynchronousVideoCompositionRequestInternal instruction];
-[AVAsynchronousVideoCompositionRequestInternal compositionTime];
-[AVAsynchronousVideoCompositionRequestInternal setSourceTrackIDsInClientOrder:];
-[AVAsynchronousVideoCompositionRequestInternal compositionFrame];
-[AVAsynchronousVideoCompositionRequestInternal lookupableSpatialVideoConfigurations];
-[AVAsynchronousVideoCompositionRequestInternal setCompositionFrame:];
-[AVAsynchronousVideoCompositionRequestInternal setCompositionTime:];
-[AVAsynchronousVideoCompositionRequestInternal setLookupableSpatialVideoConfigurations:];
-[AVAsynchronousVideoCompositionRequestInternal setRenderContext:];
-[AVAsynchronousVideoCompositionRequestInternal setSourceSampleBufferTimedSamplesByTrackID:];
-[AVAsynchronousVideoCompositionRequestInternal setSourceSampleBufferTrackIDsInClientOrder:];
-[AVAsynchronousVideoCompositionRequestInternal setSourceVideoFrameTimedSamplesByTrackID:];
-[AVAsynchronousVideoCompositionRequestInternal sourceSampleBufferTimedSamplesByTrackID];
-[AVAsynchronousVideoCompositionRequestInternal sourceSampleBufferTrackIDsInClientOrder];
-[AVAsynchronousVideoCompositionRequestInternal sourceTrackIDsInClientOrder];
-[AVAsynchronousVideoCompositionRequestInternal sourceVideoFrameTimedSamplesByTrackID];
```
