# `AVVideoComposition`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`
- 1 instance variables, 14 properties, 60 instance methods, 8 class methods

## Instance variables

```
@"AVVideoCompositionInternal" _videoComposition;
```

## Properties

```
@property (T@"NSString",R,N) colorPrimaries;
@property (T@"NSString",R,N) colorYCbCrMatrix;
@property (T@"NSString",R,N) colorTransferFunction;
@property (T@"NSString",R,N) perFrameHDRDisplayMetadataPolicy;
@property (T#,R,N) customVideoCompositorClass;
@property (T{?=qiIq},R,N) frameDuration;
@property (Ti,R,N) sourceTrackIDForFrameTiming;
@property (T{CGSize=dd},R,N) renderSize;
@property (Tf,R,N) renderScale;
@property (T@"NSArray",R,C,N) instructions;
@property (T@"AVVideoCompositionCoreAnimationTool",R,&,N) animationTool;
@property (T@"NSArray",R,N) sourceSampleDataTrackIDs;
@property (T@"NSArray",R,C,N) outputBufferDescription;
@property (T@"NSArray",R,C,N) spatialVideoConfigurations;
```

## Class methods

```
+[AVVideoComposition initialize];
+[AVVideoComposition _mutableVideoCompositionWithAsset:applyingCIFiltersWithHandler:];
+[AVVideoComposition videoCompositionWithAsset:applyingCIFiltersWithHandler:];
+[AVVideoComposition videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:];
+[AVVideoComposition videoCompositionWithPropertiesOfAsset:];
+[AVVideoComposition videoCompositionWithPropertiesOfAsset:completionHandler:];
+[AVVideoComposition videoCompositionWithPropertiesOfAsset:videoGravity:];
+[AVVideoComposition videoCompositionWithVideoComposition:];
```

## Instance methods

```
-[AVVideoComposition renderSize];
-[AVVideoComposition mutableCopyWithZone:];
-[AVVideoComposition init];
-[AVVideoComposition dealloc];
-[AVVideoComposition instructions];
-[AVVideoComposition colorPrimaries];
-[AVVideoComposition copyWithZone:];
-[AVVideoComposition setColorPrimaries:];
-[AVVideoComposition setInstructions:];
-[AVVideoComposition renderScale];
-[AVVideoComposition _deepCopy];
-[AVVideoComposition _bumpChangeSeed];
-[AVVideoComposition setSourceTrackIDForFrameTiming:];
-[AVVideoComposition setRenderScale:];
-[AVVideoComposition _auxiliaryTrackID];
-[AVVideoComposition _auxiliaryTrackLayer];
-[AVVideoComposition _changeSeed];
-[AVVideoComposition _copyFigVideoCompositor:andSession:recyclingSession:forFigRemaker:error:];
-[AVVideoComposition _hasLayerAsAuxiliaryTrack];
-[AVVideoComposition _hasPostProcessingLayers];
-[AVVideoComposition _isValidReturningExceptionReason:];
-[AVVideoComposition _postProcessingRootLayer];
-[AVVideoComposition _postProcessingVideoLayer];
-[AVVideoComposition _postProcessingVideoLayers];
-[AVVideoComposition _serializableInstructions];
-[AVVideoComposition _setFrameDurationForFrameRate:sourceTrackIDForFrameTiming:];
-[AVVideoComposition _trackWithTrackID:inTracks:];
-[AVVideoComposition animationTool];
-[AVVideoComposition builtInCompositorName];
-[AVVideoComposition colorTransferFunction];
-[AVVideoComposition colorYCbCrMatrix];
-[AVVideoComposition customVideoCompositorClass];
-[AVVideoComposition determineValidityForAsset:timeRange:validationDelegate:completionHandler:];
-[AVVideoComposition frameDuration];
-[AVVideoComposition instructionForFigInstruction:];
-[AVVideoComposition isValidForAsset:timeRange:validationDelegate:];
-[AVVideoComposition isValidForTracks:assetDuration:timeRange:validationDelegate:];
-[AVVideoComposition lookupableSpatialVideoConfigurations];
-[AVVideoComposition outputBufferDescription];
-[AVVideoComposition perFrameHDRDisplayMetadataPolicy];
-[AVVideoComposition setAnimationTool:];
-[AVVideoComposition setBuiltInCompositorName:];
-[AVVideoComposition setColorTransferFunction:];
-[AVVideoComposition setColorYCbCrMatrix:];
-[AVVideoComposition setCustomVideoCompositorClass:];
-[AVVideoComposition setFrameDuration:];
-[AVVideoComposition setLookupableSpatialVideoConfigurations:];
-[AVVideoComposition setOutputBufferDescription:];
-[AVVideoComposition setPerFrameHDRDisplayMetadataPolicy:];
-[AVVideoComposition setRenderSize:];
-[AVVideoComposition setSourceSampleDataTrackIDs:];
-[AVVideoComposition setSourceSampleDataTrackWindowsForTrackIDs:];
-[AVVideoComposition setSourceVideoTrackWindowsForTrackIDs:];
-[AVVideoComposition setSpatialVideoConfigurations:];
-[AVVideoComposition sourceSampleDataTrackIDs];
-[AVVideoComposition sourceSampleDataTrackWindowsForTrackIDs];
-[AVVideoComposition sourceTrackIDForFrameTiming];
-[AVVideoComposition sourceVideoTrackWindowsForTrackIDs];
-[AVVideoComposition spatialVideoConfigurations];
-[AVVideoComposition videoCompositionOutputColorPropertiesWithCustomCompositor:formatDescriptions:colorPrimaries:transferFunction:yCbCrMatrix:perFrameHDRDisplayMetadataPolicy:];
```
