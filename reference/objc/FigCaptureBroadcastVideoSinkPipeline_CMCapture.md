# `FigCaptureBroadcastVideoSinkPipeline`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureSinkPipeline`
- 2 instance variables, 1 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"BWBroadcastVideoSinkNode" _broadcastSinkNode;
@"NSString" _videoConnectionID;
```

## Properties

```
@property (T@"NSString",R,N,V_videoConnectionID) videoConnectionID;
```

## Class methods

```
+[FigCaptureBroadcastVideoSinkPipeline initialize];
```

## Instance methods

```
-[FigCaptureBroadcastVideoSinkPipeline flush];
-[FigCaptureBroadcastVideoSinkPipeline dealloc];
-[FigCaptureBroadcastVideoSinkPipeline setMirroringEnabled:];
-[FigCaptureBroadcastVideoSinkPipeline setRotationDegrees:];
-[FigCaptureBroadcastVideoSinkPipeline videoConnectionID];
-[FigCaptureBroadcastVideoSinkPipeline setDiscardsSampleData:];
-[FigCaptureBroadcastVideoSinkPipeline setDroppedFrameReplacementPolicy:];
-[FigCaptureBroadcastVideoSinkPipeline setMaxBufferedFrameCount:];
-[FigCaptureBroadcastVideoSinkPipeline setTestPatternToInject:];
-[FigCaptureBroadcastVideoSinkPipeline addUserAncillaryData:];
-[FigCaptureBroadcastVideoSinkPipeline initWithConfiguration:sourceOutput:graph:name:clientAuditToken:delegate:captureDevice:];
-[FigCaptureBroadcastVideoSinkPipeline setVideoCaptureConnectionConfiguration:];
```
