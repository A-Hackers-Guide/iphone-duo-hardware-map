# `AVFigAssetInspectorLoader`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAssetInspectorLoader`
- 13 instance variables, 0 properties, 45 instance methods, 5 class methods

## Instance variables

```
^{OpaqueFigAsset=} _figAsset;
i _figAssetCreationStatus;
@"AVWeakReference" _weakReferenceToAsset;
@"AVAssetInspector" _assetInspector;
@"AVDispatchOnce" _assetInspectorOnce;
@"NSObject<OS_dispatch_queue>" _completionHandlerQueue;
^{OpaqueFigSimpleMutex=} _loadingMutex;
@"NSMutableArray" _loadingBatches;
B _loadingCanceled;
B _registeredForFigAssetNotifications;
B _prefersNominalDurations;
q _fragmentMinderAssociationCount;
@"NSURL" _URL;
```

## Class methods

```
+[AVFigAssetInspectorLoader _mapAssetKeys:toFigAssetPropertySet:figAssetTrackPropertySet:callerName:];
+[AVFigAssetInspectorLoader _figAssetTrackPropertiesForKeys];
+[AVFigAssetInspectorLoader _figAssetTrackMediaSelectionPropertiesArray];
+[AVFigAssetInspectorLoader _figAssetMediaSelectionPropertiesArray];
+[AVFigAssetInspectorLoader _figAssetPropertiesForKeys];
```

## Instance methods

```
-[AVFigAssetInspectorLoader lyrics];
-[AVFigAssetInspectorLoader isPlayable];
-[AVFigAssetInspectorLoader isAssociatedWithFragmentMinder];
-[AVFigAssetInspectorLoader asset];
-[AVFigAssetInspectorLoader initWithFigAsset:forAsset:];
-[AVFigAssetInspectorLoader _statusOfValueForKey:error:firstNonLoadedDependencyKey:];
-[AVFigAssetInspectorLoader _removeFigAssetNotifications];
-[AVFigAssetInspectorLoader statusOfValueForKey:error:];
-[AVFigAssetInspectorLoader hasProtectedContent];
-[AVFigAssetInspectorLoader _completionHandlerQueue];
-[AVFigAssetInspectorLoader dealloc];
-[AVFigAssetInspectorLoader isComposable];
-[AVFigAssetInspectorLoader _prefersNominalDurations];
-[AVFigAssetInspectorLoader _classForTrackInspectors];
-[AVFigAssetInspectorLoader _invokeCompletionHandlerForLoadingBatches:];
-[AVFigAssetInspectorLoader variants];
-[AVFigAssetInspectorLoader _isStreaming];
-[AVFigAssetInspectorLoader _loadingBatches];
-[AVFigAssetInspectorLoader duration];
-[AVFigAssetInspectorLoader isCompatibleWithSavedPhotosAlbum];
-[AVFigAssetInspectorLoader figChapters];
-[AVFigAssetInspectorLoader loadValuesAsynchronouslyForKeys:keysForCollectionKeys:completionHandler:];
-[AVFigAssetInspectorLoader fragmentCount];
-[AVFigAssetInspectorLoader downloadToken];
-[AVFigAssetInspectorLoader _loadStatusForProperty:figAsset:error:];
-[AVFigAssetInspectorLoader resolvedURL];
-[AVFigAssetInspectorLoader _loadingMutex];
-[AVFigAssetInspectorLoader isExportable];
-[AVFigAssetInspectorLoader _setFragmentMindingInterval:];
-[AVFigAssetInspectorLoader _figAsset];
-[AVFigAssetInspectorLoader originalNetworkContentURL];
-[AVFigAssetInspectorLoader _fragmentMindingInterval];
-[AVFigAssetInspectorLoader _setIsAssociatedWithFragmentMinder:];
-[AVFigAssetInspectorLoader _ensureAllDependenciesOfKeyAreLoaded:];
-[AVFigAssetInspectorLoader initWithURL:figAssetCreationFlags:figAssetCreationOptions:avAssetInitializationOptions:forAsset:figErr:];
-[AVFigAssetInspectorLoader firstFragmentSequenceNumber];
-[AVFigAssetInspectorLoader assetInspector];
-[AVFigAssetInspectorLoader contentKeySpecifiersEligibleForPreloading];
-[AVFigAssetInspectorLoader _copyFormatReader];
-[AVFigAssetInspectorLoader figChapterGroupInfo];
-[AVFigAssetInspectorLoader cancelLoading];
-[AVFigAssetInspectorLoader URL];
-[AVFigAssetInspectorLoader _addFigAssetNotifications];
-[AVFigAssetInspectorLoader loadValuesAsynchronouslyForKeys:completionHandler:];
-[AVFigAssetInspectorLoader isReadable];
```
