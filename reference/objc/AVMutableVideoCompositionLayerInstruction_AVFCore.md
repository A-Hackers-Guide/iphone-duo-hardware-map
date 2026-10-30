# `AVMutableVideoCompositionLayerInstruction`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVVideoCompositionLayerInstruction`
- 1 instance variables, 1 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"AVMutableVideoCompositionLayerInstructionInternal" _mutableLayerInstruction;
```

## Properties

```
@property (Ti,N) trackID;
```

## Class methods

```
+[AVMutableVideoCompositionLayerInstruction videoCompositionLayerInstruction];
+[AVMutableVideoCompositionLayerInstruction videoCompositionLayerInstructionWithAssetTrack:];
```

## Instance methods

```
-[AVMutableVideoCompositionLayerInstruction trackID];
-[AVMutableVideoCompositionLayerInstruction setCropRectangle:atTime:];
-[AVMutableVideoCompositionLayerInstruction setCropRectangleRampFromStartCropRectangle:toEndCropRectangle:timeRange:];
-[AVMutableVideoCompositionLayerInstruction setOpacity:atTime:];
-[AVMutableVideoCompositionLayerInstruction setOpacityRampFromStartOpacity:toEndOpacity:timeRange:];
-[AVMutableVideoCompositionLayerInstruction setTrackID:];
-[AVMutableVideoCompositionLayerInstruction setTransform:atTime:];
-[AVMutableVideoCompositionLayerInstruction setTransformRampFromStartTransform:toEndTransform:timeRange:];
```
