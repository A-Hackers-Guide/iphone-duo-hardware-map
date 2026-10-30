# `AVAssetMakeReadyForInspectionLoader`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetInspectorLoader`
- 7 instance variables, 0 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"AVAssetInspector" _assetInspector;
^{OpaqueFigFormatReader=} _formatReader;
^{OpaqueFigSimpleMutex=} _loadingMutex;
@"NSMutableArray" _keysAwaitingCompletion;
q _status;
i _basicInspectionFailureCode;
@"NSURL" _URL;
```

## Instance methods

```
-[AVAssetMakeReadyForInspectionLoader lyrics];
-[AVAssetMakeReadyForInspectionLoader isPlayable];
-[AVAssetMakeReadyForInspectionLoader statusOfValueForKey:error:];
-[AVAssetMakeReadyForInspectionLoader hasProtectedContent];
-[AVAssetMakeReadyForInspectionLoader dealloc];
-[AVAssetMakeReadyForInspectionLoader isComposable];
-[AVAssetMakeReadyForInspectionLoader _status];
-[AVAssetMakeReadyForInspectionLoader _isStreaming];
-[AVAssetMakeReadyForInspectionLoader duration];
-[AVAssetMakeReadyForInspectionLoader fragmentCount];
-[AVAssetMakeReadyForInspectionLoader _loadingMutex];
-[AVAssetMakeReadyForInspectionLoader isExportable];
-[AVAssetMakeReadyForInspectionLoader copyWithZone:];
-[AVAssetMakeReadyForInspectionLoader firstFragmentSequenceNumber];
-[AVAssetMakeReadyForInspectionLoader assetInspector];
-[AVAssetMakeReadyForInspectionLoader _copyFormatReader];
-[AVAssetMakeReadyForInspectionLoader figChapterGroupInfo];
-[AVAssetMakeReadyForInspectionLoader initWithURL:];
-[AVAssetMakeReadyForInspectionLoader cancelLoading];
-[AVAssetMakeReadyForInspectionLoader URL];
-[AVAssetMakeReadyForInspectionLoader loadValuesAsynchronouslyForKeys:completionHandler:];
-[AVAssetMakeReadyForInspectionLoader isReadable];
-[AVAssetMakeReadyForInspectionLoader _copyFormatReaderFromFigObjectWithFigErrorCode:];
-[AVAssetMakeReadyForInspectionLoader _dictionaryOfSpecialGettersForKeyValueStatus];
-[AVAssetMakeReadyForInspectionLoader _dictionaryOfSpecialLoadingMethodsForKeys];
-[AVAssetMakeReadyForInspectionLoader _getAndPruneCompletionsWhileMutexLocked];
-[AVAssetMakeReadyForInspectionLoader _inspectionRequiresAFormatReader];
-[AVAssetMakeReadyForInspectionLoader _loadValuesUsingDefaultLoadingMethodWhileMutexLockedForKeys:];
-[AVAssetMakeReadyForInspectionLoader _loadValuesWhileMutexLockedForKeys:];
-[AVAssetMakeReadyForInspectionLoader _playbackItem];
-[AVAssetMakeReadyForInspectionLoader _providesAccurateTiming];
-[AVAssetMakeReadyForInspectionLoader _serverHasDied];
-[AVAssetMakeReadyForInspectionLoader _setStatus:figErrorCode:];
-[AVAssetMakeReadyForInspectionLoader _statusOfValueForKeyThatIsAlwaysLoaded];
-[AVAssetMakeReadyForInspectionLoader _statusOfValueWhileMutexLockedForKey:error:];
-[AVAssetMakeReadyForInspectionLoader _statusOfValuesIsTerminalWhileMutexLockedForKeys:];
-[AVAssetMakeReadyForInspectionLoader _updateStatusWhileMutexLocked:figErrorCode:];
```
