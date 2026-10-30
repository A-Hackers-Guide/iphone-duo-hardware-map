# `AVVideoCompositionCoreAnimationTool`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"AVVideoCompositionCoreAnimationToolInternal" _videoCompositionTool;
```

## Class methods

```
+[AVVideoCompositionCoreAnimationTool videoCompositionCoreAnimationToolWithAdditionalLayer:asTrackID:];
+[AVVideoCompositionCoreAnimationTool videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayer:inLayer:];
+[AVVideoCompositionCoreAnimationTool videoCompositionCoreAnimationToolWithPostProcessingAsVideoLayers:inLayer:];
```

## Instance methods

```
-[AVVideoCompositionCoreAnimationTool dealloc];
-[AVVideoCompositionCoreAnimationTool _auxiliaryTrackID];
-[AVVideoCompositionCoreAnimationTool _auxiliaryTrackLayer];
-[AVVideoCompositionCoreAnimationTool _hasLayerAsAuxiliaryTrack];
-[AVVideoCompositionCoreAnimationTool _hasPostProcessingLayers];
-[AVVideoCompositionCoreAnimationTool _postProcessingRootLayer];
-[AVVideoCompositionCoreAnimationTool _postProcessingVideoLayers];
-[AVVideoCompositionCoreAnimationTool initWithMagicTrackID:animationLayer:videoLayers:];
```
