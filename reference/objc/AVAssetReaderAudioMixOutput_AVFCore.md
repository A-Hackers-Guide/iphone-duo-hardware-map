# `AVAssetReaderAudioMixOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetReaderOutput`
- 1 instance variables, 4 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"AVAssetReaderAudioMixOutputInternal" _audioMixOutputInternal;
```

## Properties

```
@property (T@"NSArray",R,N) audioTracks;
@property (T@"NSDictionary",R,N) audioSettings;
@property (T@"AVAudioMix",C,N) audioMix;
@property (T@"NSString",C,N) audioTimePitchAlgorithm;
```

## Class methods

```
+[AVAssetReaderAudioMixOutput assetReaderAudioMixOutputWithAudioTracks:audioSettings:];
```

## Instance methods

```
-[AVAssetReaderAudioMixOutput init];
-[AVAssetReaderAudioMixOutput dealloc];
-[AVAssetReaderAudioMixOutput audioTimePitchAlgorithm];
-[AVAssetReaderAudioMixOutput description];
-[AVAssetReaderAudioMixOutput _enableTrackExtractionReturningError:];
-[AVAssetReaderAudioMixOutput _asset];
-[AVAssetReaderAudioMixOutput audioSettings];
-[AVAssetReaderAudioMixOutput setAudioTimePitchAlgorithm:];
-[AVAssetReaderAudioMixOutput mediaType];
-[AVAssetReaderAudioMixOutput _setAudioTapProcessor:forTrack:];
-[AVAssetReaderAudioMixOutput _audioCurvesForTrack:];
-[AVAssetReaderAudioMixOutput _audioEffectsParametersForTrack:];
-[AVAssetReaderAudioMixOutput _audioTapProcessorForTrack:];
-[AVAssetReaderAudioMixOutput _audioTimePitchAlgorithmForTrack:];
-[AVAssetReaderAudioMixOutput _setAudioCurves:forTrack:];
-[AVAssetReaderAudioMixOutput _setAudioEffectsParameters:forTrack:];
-[AVAssetReaderAudioMixOutput _setAudioTimePitchAlgorithm:forTrack:];
-[AVAssetReaderAudioMixOutput audioMix];
-[AVAssetReaderAudioMixOutput audioTracks];
-[AVAssetReaderAudioMixOutput initWithAudioTracks:audioSettings:];
-[AVAssetReaderAudioMixOutput setAudioMix:];
```
