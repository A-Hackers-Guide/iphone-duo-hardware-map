# `AVAssetReaderVideoCompositionOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetReaderOutput`
- 1 instance variables, 4 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"AVAssetReaderVideoCompositionOutputInternal" _videoCompositionOutputInternal;
```

## Properties

```
@property (T@"NSArray",R,N) videoTracks;
@property (T@"NSDictionary",R,N) videoSettings;
@property (T@"AVVideoComposition",C,N) videoComposition;
@property (T@"<AVVideoCompositing>",R,N) customVideoCompositor;
```

## Class methods

```
+[AVAssetReaderVideoCompositionOutput assetReaderVideoCompositionOutputWithVideoTracks:videoSettings:];
```

## Instance methods

```
-[AVAssetReaderVideoCompositionOutput videoSettings];
-[AVAssetReaderVideoCompositionOutput setVideoComposition:];
-[AVAssetReaderVideoCompositionOutput _formatDescriptions];
-[AVAssetReaderVideoCompositionOutput init];
-[AVAssetReaderVideoCompositionOutput dealloc];
-[AVAssetReaderVideoCompositionOutput description];
-[AVAssetReaderVideoCompositionOutput _enableTrackExtractionReturningError:];
-[AVAssetReaderVideoCompositionOutput _asset];
-[AVAssetReaderVideoCompositionOutput mediaType];
-[AVAssetReaderVideoCompositionOutput videoComposition];
-[AVAssetReaderVideoCompositionOutput _errorForOSStatus:];
-[AVAssetReaderVideoCompositionOutput _prepareForReadingReturningError:];
-[AVAssetReaderVideoCompositionOutput _setVideoComposition:];
-[AVAssetReaderVideoCompositionOutput _setVideoComposition:customVideoCompositorSession:];
-[AVAssetReaderVideoCompositionOutput _videoCompositionProcessorColorProperties];
-[AVAssetReaderVideoCompositionOutput alwaysCopiesSampleData];
-[AVAssetReaderVideoCompositionOutput customVideoCompositor];
-[AVAssetReaderVideoCompositionOutput initWithVideoTracks:videoSettings:];
-[AVAssetReaderVideoCompositionOutput makeLookupableSpatialVideoConfigurations:];
-[AVAssetReaderVideoCompositionOutput sampleDataTrackIDs];
-[AVAssetReaderVideoCompositionOutput videoTracks];
```
