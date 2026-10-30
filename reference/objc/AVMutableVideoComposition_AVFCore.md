# `AVMutableVideoComposition`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVVideoComposition`
- 1 instance variables, 9 properties, 34 instance methods, 9 class methods

## Instance variables

```
@"AVMutableVideoCompositionInternal" _mutableVideoComposition;
```

## Properties

```
@property (T#,&,N) customVideoCompositorClass;
@property (T{?=qiIq},N) frameDuration;
@property (Ti,N) sourceTrackIDForFrameTiming;
@property (T{CGSize=dd},N) renderSize;
@property (Tf,N) renderScale;
@property (T@"NSArray",C,N) instructions;
@property (T@"AVVideoCompositionCoreAnimationTool",&,N) animationTool;
@property (T@"NSArray",C,N) sourceSampleDataTrackIDs;
@property (T@"NSArray",C,N) outputBufferDescription;
```

## Class methods

```
+[AVMutableVideoComposition videoComposition];
+[AVMutableVideoComposition makeSpatialVideoConfigurationsFromVideoTracks:];
+[AVMutableVideoComposition videoCompositionWithAsset:applyingCIFiltersWithHandler:];
+[AVMutableVideoComposition videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:];
+[AVMutableVideoComposition videoCompositionWithPropertiesOfAsset:];
+[AVMutableVideoComposition videoCompositionWithPropertiesOfAsset:completionHandler:];
+[AVMutableVideoComposition videoCompositionWithPropertiesOfAsset:prototypeInstruction:];
+[AVMutableVideoComposition videoCompositionWithPropertiesOfAsset:prototypeInstruction:completionHandler:];
+[AVMutableVideoComposition videoCompositionWithPropertiesOfAsset:videoGravity:];
```

## Instance methods

```
-[AVMutableVideoComposition renderSize];
-[AVMutableVideoComposition instructions];
-[AVMutableVideoComposition colorPrimaries];
-[AVMutableVideoComposition setColorPrimaries:];
-[AVMutableVideoComposition setInstructions:];
-[AVMutableVideoComposition renderScale];
-[AVMutableVideoComposition setSourceTrackIDForFrameTiming:];
-[AVMutableVideoComposition setRenderScale:];
-[AVMutableVideoComposition animationTool];
-[AVMutableVideoComposition builtInCompositorName];
-[AVMutableVideoComposition colorTransferFunction];
-[AVMutableVideoComposition colorYCbCrMatrix];
-[AVMutableVideoComposition customVideoCompositorClass];
-[AVMutableVideoComposition frameDuration];
-[AVMutableVideoComposition outputBufferDescription];
-[AVMutableVideoComposition perFrameHDRDisplayMetadataPolicy];
-[AVMutableVideoComposition setAnimationTool:];
-[AVMutableVideoComposition setBuiltInCompositorName:];
-[AVMutableVideoComposition setColorTransferFunction:];
-[AVMutableVideoComposition setColorYCbCrMatrix:];
-[AVMutableVideoComposition setCustomVideoCompositorClass:];
-[AVMutableVideoComposition setFrameDuration:];
-[AVMutableVideoComposition setOutputBufferDescription:];
-[AVMutableVideoComposition setPerFrameHDRDisplayMetadataPolicy:];
-[AVMutableVideoComposition setRenderSize:];
-[AVMutableVideoComposition setSourceSampleDataTrackIDs:];
-[AVMutableVideoComposition setSourceSampleDataTrackWindowsForTrackIDs:];
-[AVMutableVideoComposition setSourceVideoTrackWindowsForTrackIDs:];
-[AVMutableVideoComposition setSpatialVideoConfigurations:];
-[AVMutableVideoComposition sourceSampleDataTrackIDs];
-[AVMutableVideoComposition sourceSampleDataTrackWindowsForTrackIDs];
-[AVMutableVideoComposition sourceTrackIDForFrameTiming];
-[AVMutableVideoComposition sourceVideoTrackWindowsForTrackIDs];
-[AVMutableVideoComposition spatialVideoConfigurations];
```
