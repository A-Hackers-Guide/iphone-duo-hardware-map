# `AVQueuedSampleBufferRendering` (protocol)

- Image: [`/usr/lib/swift/libswiftAVFoundation.dylib`](../userland/usr__lib__swift__libswiftAVFoundation.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 3 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T^{OpaqueCMTimebase=},R,&) timebase;
@property (TB,R,GisReadyForMoreMediaData) readyForMoreMediaData;
@property (TB,R,N) hasSufficientMediaDataForReliablePlaybackStart;
```

## Instance methods

```
-[AVQueuedSampleBufferRendering timebase];
-[AVQueuedSampleBufferRendering isReadyForMoreMediaData];
-[AVQueuedSampleBufferRendering stopRequestingMediaData];
-[AVQueuedSampleBufferRendering flush];
-[AVQueuedSampleBufferRendering hasSufficientMediaDataForReliablePlaybackStart];
-[AVQueuedSampleBufferRendering requestMediaDataWhenReadyOnQueue:usingBlock:];
-[AVQueuedSampleBufferRendering enqueueSampleBuffer:];
```
