# `AVPlayerItemTrack`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 5 properties, 44 instance methods, 1 class methods

## Instance variables

```
@"AVPlayerItemTrackInternal" _playerItemTrack;
```

## Properties

```
@property (T@"NSArray",R,N) outputs;
@property (T{?={?=qiIq}{?=qiIq}},R,N) parsedTimeRange;
@property (T@"AVAssetTrack",R,N) assetTrack;
@property (TB,N,GisEnabled) enabled;
@property (Tf,R) currentVideoFrameRate;
```

## Class methods

```
+[AVPlayerItemTrack playerItemTrackWithFigPlaybackItem:readyForInspection:trackID:asset:playerItem:];
```

## Instance methods

```
-[AVPlayerItemTrack outputs];
-[AVPlayerItemTrack removeOutput:];
-[AVPlayerItemTrack _transferMutesHapticsToFig];
-[AVPlayerItemTrack loudnessInfo];
-[AVPlayerItemTrack setDisableColorMatching:];
-[AVPlayerItemTrack setVideoEnhancementFilterOptions:];
-[AVPlayerItemTrack _attachToFigPlaybackItemOfPlayerItem:];
-[AVPlayerItemTrack videoEnhancementFilterOptions];
-[AVPlayerItemTrack trackID];
-[AVPlayerItemTrack _transferLoudnessInfoToFig];
-[AVPlayerItemTrack _playerItem];
-[AVPlayerItemTrack _transferVideoEnhancementOptionsToFig];
-[AVPlayerItemTrack _setParsedTimeRange:];
-[AVPlayerItemTrack dealloc];
-[AVPlayerItemTrack setLoudnessInfo:];
-[AVPlayerItemTrack _figPlaybackItemIsReadyForInspection];
-[AVPlayerItemTrack assetTrack];
-[AVPlayerItemTrack effectiveLoudnessInfo];
-[AVPlayerItemTrack setMutesHaptics:];
-[AVPlayerItemTrack currentVideoFrameRate];
-[AVPlayerItemTrack _weakReferenceToPlayerItem];
-[AVPlayerItemTrack mutesHaptics];
-[AVPlayerItemTrack hapticVolume];
-[AVPlayerItemTrack isEnabled];
-[AVPlayerItemTrack _initWithFigPlaybackItem:readyForInspection:trackID:asset:playerItem:];
-[AVPlayerItemTrack disableColorMatching];
-[AVPlayerItemTrack _respondToFigPlaybackItemBecomingReadyForInpection];
-[AVPlayerItemTrack effectiveEQPreset];
-[AVPlayerItemTrack _transferHapticVolumeToFig];
-[AVPlayerItemTrack setEnabled:];
-[AVPlayerItemTrack _updateTrackExtractionIDArrayProperty];
-[AVPlayerItemTrack hash];
-[AVPlayerItemTrack description];
-[AVPlayerItemTrack activeHapticChannelIndex];
-[AVPlayerItemTrack _transferEnabledToFig];
-[AVPlayerItemTrack setHapticVolume:];
-[AVPlayerItemTrack parsedTimeRange];
-[AVPlayerItemTrack addOutput:];
-[AVPlayerItemTrack _transferDisableColorMatchingToFig];
-[AVPlayerItemTrack isEqual:];
-[AVPlayerItemTrack willTrimShortDurationAudioSamples];
-[AVPlayerItemTrack setActiveHapticChannelIndex:];
-[AVPlayerItemTrack fallbackTrack];
-[AVPlayerItemTrack _transferActiveHapticChannelIndexToFig];
```
