# `BWNodeOutputMediaProperties`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 17 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"NSString" _associatedAttachedMediaKey;
@"BWNodeOutput" _owningNodeOutput;
@"BWFormat" _resolvedFormat;
@"BWFormat" _liveFormat;
@"BWPixelBufferPool" _preparedPixelBufferPool;
@"BWPixelBufferPool" _livePixelBufferPool;
i _preparedPixelBufferPoolSize;
i _livePixelBufferPoolSize;
@"BWDataBufferPool" _preparedDataBufferPool;
@"BWDataBufferPool" _liveDataBufferPool;
i _preparedDataBufferPoolSize;
i _liveDataBufferPoolSize;
i _resolvedRetainedBufferCount;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferPoolsLock;
I _mediaType;
```

## Properties

```
@property (T@"BWFormat",&,N,V_liveFormat) liveFormat;
@property (TI,R,N,V_mediaType) mediaType;
@property (T@"BWFormat",&,N) resolvedFormat;
@property (T@"BWPixelBufferPool",&,N,V_preparedPixelBufferPool) preparedPixelBufferPool;
@property (Ti,N,V_preparedPixelBufferPoolSize) preparedPixelBufferPoolSize;
@property (T@"BWPixelBufferPool",&,N) livePixelBufferPool;
@property (Ti,N,V_livePixelBufferPoolSize) livePixelBufferPoolSize;
@property (T@"BWDataBufferPool",&,N,V_preparedDataBufferPool) preparedDataBufferPool;
@property (Ti,N,V_preparedDataBufferPoolSize) preparedDataBufferPoolSize;
@property (T@"BWDataBufferPool",&,N) liveDataBufferPool;
@property (Ti,N,V_liveDataBufferPoolSize) liveDataBufferPoolSize;
@property (T@"BWPixelBufferPool",R,N) preparedOrLivePixelBufferPool;
@property (T@"BWDataBufferPool",R,N) preparedOrLiveDataBufferPool;
@property (T@"BWVideoFormat",R,N) resolvedVideoFormat;
@property (T@"BWPointCloudFormat",R,N) resolvedPointCloudFormat;
@property (Ti,N,V_resolvedRetainedBufferCount) resolvedRetainedBufferCount;
@property (T@"BWVideoFormat",R,N) liveVideoFormat;
```

## Instance methods

```
-[BWNodeOutputMediaProperties liveFormat];
-[BWNodeOutputMediaProperties _makePreparedPixelBufferPoolLiveLocked];
-[BWNodeOutputMediaProperties setLiveDataBufferPoolSize:];
-[BWNodeOutputMediaProperties init];
-[BWNodeOutputMediaProperties setPreparedSharedPixelBufferPool:];
-[BWNodeOutputMediaProperties dealloc];
-[BWNodeOutputMediaProperties setLivePixelBufferPoolSize:];
-[BWNodeOutputMediaProperties preparedPixelBufferPool];
-[BWNodeOutputMediaProperties preparedPixelBufferPoolSize];
-[BWNodeOutputMediaProperties resolvedRetainedBufferCount];
-[BWNodeOutputMediaProperties preparedOrLivePixelBufferPool];
-[BWNodeOutputMediaProperties setLivePixelBufferPool:];
-[BWNodeOutputMediaProperties setPreparedDataBufferPool:];
-[BWNodeOutputMediaProperties resolvedFormat];
-[BWNodeOutputMediaProperties preparedOrLiveDataBufferPool];
-[BWNodeOutputMediaProperties setResolvedFormat:];
-[BWNodeOutputMediaProperties setNodePreparedDataBufferPool:];
-[BWNodeOutputMediaProperties liveDataBufferPoolSize];
-[BWNodeOutputMediaProperties setLiveDataBufferPool:];
-[BWNodeOutputMediaProperties setPreparedPixelBufferPool:];
-[BWNodeOutputMediaProperties _setOwningNodeOutput:associatedAttachedMediaKey:];
-[BWNodeOutputMediaProperties liveVideoFormat];
-[BWNodeOutputMediaProperties setPreparedPixelBufferPoolSize:];
-[BWNodeOutputMediaProperties resolvedPointCloudFormat];
-[BWNodeOutputMediaProperties setLiveFormat:];
-[BWNodeOutputMediaProperties livePixelBufferPoolSize];
-[BWNodeOutputMediaProperties liveDataBufferPool];
-[BWNodeOutputMediaProperties preparedDataBufferPoolSize];
-[BWNodeOutputMediaProperties setPreparedSharedDataBufferPool:];
-[BWNodeOutputMediaProperties _makePreparedDataBufferPoolLiveLocked];
-[BWNodeOutputMediaProperties setPreparedDataBufferPoolSize:];
-[BWNodeOutputMediaProperties resolvedVideoFormat];
-[BWNodeOutputMediaProperties mediaType];
-[BWNodeOutputMediaProperties livePixelBufferPool];
-[BWNodeOutputMediaProperties preparedDataBufferPool];
-[BWNodeOutputMediaProperties setNodePreparedPixelBufferPool:];
-[BWNodeOutputMediaProperties setResolvedRetainedBufferCount:];
```
