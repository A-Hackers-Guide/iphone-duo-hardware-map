# `AVSampleBufferRenderSynchronizer`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 37 instance methods, 5 class methods

## Instance variables

```
@"AVSampleBufferRenderSynchronizerInternal" _synchronizerInternal;
```

## Properties

```
@property (T@"NSArray",R) renderers;
@property (T^{OpaqueCMTimebase=},R,&) timebase;
@property (Tf,N) rate;
@property (TB,N) delaysRateChangeUntilHasSufficientMediaData;
```

## Class methods

```
+[AVSampleBufferRenderSynchronizer enableSTSLabels];
+[AVSampleBufferRenderSynchronizer _makeSTSLabel];
+[AVSampleBufferRenderSynchronizer _videoRendererForRenderer:];
+[AVSampleBufferRenderSynchronizer currentFigRenderSynchronizerFactory];
+[AVSampleBufferRenderSynchronizer setFigRenderSynchronizerFactory:forQueue:];
```

## Instance methods

```
-[AVSampleBufferRenderSynchronizer timebase];
-[AVSampleBufferRenderSynchronizer rate];
-[AVSampleBufferRenderSynchronizer removeTimeObserver:];
-[AVSampleBufferRenderSynchronizer init];
-[AVSampleBufferRenderSynchronizer dealloc];
-[AVSampleBufferRenderSynchronizer currentTime];
-[AVSampleBufferRenderSynchronizer setRate:];
-[AVSampleBufferRenderSynchronizer addPeriodicTimeObserverForInterval:queue:usingBlock:];
-[AVSampleBufferRenderSynchronizer isDefunct];
-[AVSampleBufferRenderSynchronizer _nameForLogging];
-[AVSampleBufferRenderSynchronizer _addRenderer:error:];
-[AVSampleBufferRenderSynchronizer _addedAudioRendererCount];
-[AVSampleBufferRenderSynchronizer _addedAudioRendererCountInternal];
-[AVSampleBufferRenderSynchronizer _canAddRendererInternal:error:];
-[AVSampleBufferRenderSynchronizer _createOnceTimebaseObserverForRemovalOfRenderer:atTime:];
-[AVSampleBufferRenderSynchronizer _getClientCompletionHandlerForRenderer:];
-[AVSampleBufferRenderSynchronizer _getTimebaseObserverForRenderer:];
-[AVSampleBufferRenderSynchronizer _initializeTimebase];
-[AVSampleBufferRenderSynchronizer _multipleAudioRenderersDisallowed];
-[AVSampleBufferRenderSynchronizer _performRendererRemoval:];
-[AVSampleBufferRenderSynchronizer _removeTimebaseObserverForRenderer:];
-[AVSampleBufferRenderSynchronizer _rendererConfigurationIsValid:];
-[AVSampleBufferRenderSynchronizer _scheduleTimedRendererRemovalAtTime:atTime:withClientCompletionHandler:];
-[AVSampleBufferRenderSynchronizer _setRate:time:atHostTime:];
-[AVSampleBufferRenderSynchronizer _storeObserver:clientCompletionHandler:forRenderer:];
-[AVSampleBufferRenderSynchronizer _updateRateFromTimebase];
-[AVSampleBufferRenderSynchronizer addBoundaryTimeObserverForTimes:queue:usingBlock:];
-[AVSampleBufferRenderSynchronizer addRenderer:];
-[AVSampleBufferRenderSynchronizer copyInternalFigSampleBufferRenderSynchronizer];
-[AVSampleBufferRenderSynchronizer delaysRateChangeUntilHasSufficientMediaData];
-[AVSampleBufferRenderSynchronizer removeRenderer:atTime:completionHandler:];
-[AVSampleBufferRenderSynchronizer removeRenderer:atTime:withCompletionHandler:];
-[AVSampleBufferRenderSynchronizer renderers];
-[AVSampleBufferRenderSynchronizer setDelaysRateChangeUntilHasSufficientMediaData:];
-[AVSampleBufferRenderSynchronizer setRate:time:];
-[AVSampleBufferRenderSynchronizer setRate:time:atHostTime:];
-[AVSampleBufferRenderSynchronizer setRate:time:atHostTime:error:];
```
