# `AVAssetInspectorLoader`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `AVAsynchronousKeyValueLoading`
- 1 instance variables, 26 properties, 40 instance methods, 1 class methods

## Instance variables

```
@"AVWeakReference" _weakReference;
```

## Properties

```
@property (T@"AVWeakReference",R,N,G_weakReference) weakReference;
@property (T@"NSURL",R,N) URL;
@property (T^{OpaqueFigAsset=},R,N,G_figAsset) figAsset;
@property (T^{OpaqueFigPlaybackItem=},R,N,G_playbackItem) playbackItem;
@property (T#,R,N,G_classForTrackInspectors) classForTrackInspectors;
@property (T{?=qiIq},R,N) duration;
@property (T@"NSArray",R,N) variants;
@property (T@"NSString",R,N) lyrics;
@property (TB,R,N,GisPlayable) playable;
@property (TB,R,N,GisExportable) exportable;
@property (TB,R,N,GisReadable) readable;
@property (TB,R,N,GisComposable) composable;
@property (TB,R,N,GisCompatibleWithSavedPhotosAlbum) compatibleWithSavedPhotosAlbum;
@property (T@"NSArray",R,N) figChapterGroupInfo;
@property (T@"NSArray",R,N) figChapters;
@property (T@"NSURL",R,N) resolvedURL;
@property (T@"NSURL",R,N) originalNetworkContentURL;
@property (TQ,R,N) downloadToken;
@property (T@"NSArray",R,N) contentKeySpecifiersEligibleForPreloading;
@property (TB,R,N) hasProtectedContent;
@property (TB,R,N,G_isStreaming) streaming;
@property (TB,R,N,G_prefersNominalDurations) prefersNominalDurations;
@property (Tq,R,N) firstFragmentSequenceNumber;
@property (Tq,R,N) fragmentCount;
@property (TB,R,N,GisAssociatedWithFragmentMinder) associatedWithFragmentMinder;
@property (Td,N,G_fragmentMindingInterval,S_setFragmentMindingInterval:) fragmentMindingInterval;
```

## Class methods

```
+[AVAssetInspectorLoader initialize];
```

## Instance methods

```
-[AVAssetInspectorLoader lyrics];
-[AVAssetInspectorLoader isPlayable];
-[AVAssetInspectorLoader isAssociatedWithFragmentMinder];
-[AVAssetInspectorLoader statusOfValueForKey:error:];
-[AVAssetInspectorLoader hasProtectedContent];
-[AVAssetInspectorLoader init];
-[AVAssetInspectorLoader dealloc];
-[AVAssetInspectorLoader isComposable];
-[AVAssetInspectorLoader _prefersNominalDurations];
-[AVAssetInspectorLoader _classForTrackInspectors];
-[AVAssetInspectorLoader variants];
-[AVAssetInspectorLoader _isStreaming];
-[AVAssetInspectorLoader duration];
-[AVAssetInspectorLoader isCompatibleWithSavedPhotosAlbum];
-[AVAssetInspectorLoader figChapters];
-[AVAssetInspectorLoader loadValuesAsynchronouslyForKeys:keysForCollectionKeys:completionHandler:];
-[AVAssetInspectorLoader fragmentCount];
-[AVAssetInspectorLoader _weakReference];
-[AVAssetInspectorLoader downloadToken];
-[AVAssetInspectorLoader resolvedURL];
-[AVAssetInspectorLoader isExportable];
-[AVAssetInspectorLoader _setFragmentMindingInterval:];
-[AVAssetInspectorLoader _figAsset];
-[AVAssetInspectorLoader originalNetworkContentURL];
-[AVAssetInspectorLoader _fragmentMindingInterval];
-[AVAssetInspectorLoader _setIsAssociatedWithFragmentMinder:];
-[AVAssetInspectorLoader _ensureAllDependenciesOfKeyAreLoaded:];
-[AVAssetInspectorLoader copyWithZone:];
-[AVAssetInspectorLoader firstFragmentSequenceNumber];
-[AVAssetInspectorLoader assetInspector];
-[AVAssetInspectorLoader contentKeySpecifiersEligibleForPreloading];
-[AVAssetInspectorLoader _copyFormatReader];
-[AVAssetInspectorLoader figChapterGroupInfo];
-[AVAssetInspectorLoader cancelLoading];
-[AVAssetInspectorLoader URL];
-[AVAssetInspectorLoader loadValuesAsynchronouslyForKeys:completionHandler:];
-[AVAssetInspectorLoader isReadable];
-[AVAssetInspectorLoader _createAVErrorForError:andFigErrorCode:];
-[AVAssetInspectorLoader _playbackItem];
-[AVAssetInspectorLoader _serverHasDied];
```
