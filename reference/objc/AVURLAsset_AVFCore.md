# `AVURLAsset`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVAsset`
- Protocols: `AVContentKeyRecipientInternal`, `AVContentKeyRecipient`
- 1 instance variables, 15 properties, 66 instance methods, 34 class methods

## Instance variables

```
@"AVURLAssetInternal" _URLAsset;
```

## Properties

```
@property (TB,R,N) shouldMatchDataInCacheByURLPathComponentOnly;
@property (TB,R,N) shouldMatchDataInCacheByURLWithoutQueryComponent;
@property (T@"NSString",R,N) cacheKey;
@property (T@"NSArray",R,N) variants;
@property (T@"AVAssetResourceLoader",R,N) resourceLoader;
@property (TB,R,N) mayRequireContentKeysForMediaDataProcessing;
@property (T@"NSUUID",?,R,N) uniqueIdentifier;
@property (TB,?,R,N) disallowsLoggingURLs;
@property (TB,R,N) mayRequireContentKeysForMediaDataProcessing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSURL",R,C,N) URL;
@property (T@"NSUUID",R,N) httpSessionIdentifier;
```

## Class methods

```
+[AVURLAsset writableTypeIdentifiersForItemProvider];
+[AVURLAsset readableTypeIdentifiersForItemProvider];
+[AVURLAsset itemProviderVisibilityForRepresentationWithTypeIdentifier:];
+[AVURLAsset objectWithItemProviderData:typeIdentifier:error:];
+[AVURLAsset _objectWithItemProviderFileURL:typeIdentifier:isInPlace:error:];
+[AVURLAsset _preferredRepresentationForItemProviderReadableTypeIdentifier:];
+[AVURLAsset _preferredRepresentationForItemProviderWritableTypeIdentifier:];
+[AVURLAsset URLAssetWithURL:options:];
+[AVURLAsset assetForNSURLSessionWithURL:propertyList:];
+[AVURLAsset audiovisualTypes];
+[AVURLAsset UTTypeIDArrayFromUTTypeArray:];
+[AVURLAsset _UTTypes];
+[AVURLAsset _avfValidationPlist];
+[AVURLAsset _avfValidationPlistWithPlaylistMIMETypesTreatedAsISOBMFFMIMETypes];
+[AVURLAsset _figFileMIMETypes];
+[AVURLAsset _figFilePathExtensions];
+[AVURLAsset _figFileUTIs];
+[AVURLAsset _figHFSFileTypes];
+[AVURLAsset _figMIMETypes];
+[AVURLAsset _figStreamingMIMETypes];
+[AVURLAsset _figStreamingUTIs];
+[AVURLAsset _fileUTTypes];
+[AVURLAsset _getFigAssetCreationOptionsFromURLAssetInitializationOptions:assetLoggingIdentifier:figAssetCreationFlags:error:];
+[AVURLAsset _getFigAssetiTunesStoreContentInfoFromURLAssetiTunesStoreContentInfo:];
+[AVURLAsset _initializationOptionsClasses];
+[AVURLAsset _streamingUTTypes];
+[AVURLAsset audiovisualContentTypes];
+[AVURLAsset audiovisualMIMETypes];
+[AVURLAsset instanceIdentifierMapTable];
+[AVURLAsset isPlayableExtendedMIMEType:];
+[AVURLAsset isPlayableExtendedMIMEType:options:];
+[AVURLAsset setUserInfoObject:forURLAsset:];
+[AVURLAsset userInfoObjectForURLAsset:];
+[AVURLAsset userInfoObjectForURLAssetInstanceIdentifier:];
```

## Instance methods

```
-[AVURLAsset lyrics];
-[AVURLAsset allowsExpensiveNetworkAccess];
-[AVURLAsset cacheKey];
-[AVURLAsset _removeFigAssetNotifications];
-[AVURLAsset init];
-[AVURLAsset assetCache];
-[AVURLAsset initWithURL:options:];
-[AVURLAsset dealloc];
-[AVURLAsset allowsConstrainedNetworkAccess];
-[AVURLAsset creationOptions];
-[AVURLAsset _classForTrackInspectors];
-[AVURLAsset httpSessionIdentifier];
-[AVURLAsset uniqueIdentifier];
-[AVURLAsset variants];
-[AVURLAsset identifyingTag];
-[AVURLAsset downloadToken];
-[AVURLAsset resolvedURL];
-[AVURLAsset identifyingTagClass];
-[AVURLAsset originalNetworkContentURL];
-[AVURLAsset expire];
-[AVURLAsset description];
-[AVURLAsset resourceLoader];
-[AVURLAsset contentKeySession];
-[AVURLAsset loadDataWithTypeIdentifier:forItemProviderCompletionHandler:];
-[AVURLAsset tracks];
-[AVURLAsset contentKeySpecifiersEligibleForPreloading];
-[AVURLAsset _copyFormatReader];
-[AVURLAsset cancelLoading];
-[AVURLAsset URL];
-[AVURLAsset _addFigAssetNotifications];
-[AVURLAsset SHA1Digest];
-[AVURLAsset _loadFileRepresentationOfTypeIdentifier:forItemProviderCompletionHandler:];
-[AVURLAsset propertyListForNSURLSessionAssetReturningError:];
-[AVURLAsset _assetInspector];
-[AVURLAsset _absoluteURL];
-[AVURLAsset _assetInspectorLoader];
-[AVURLAsset _attachToContentKeySession:contentKeyBoss:failedSinceAlreadyAttachedToAnotherSession:];
-[AVURLAsset _attachedToExternalContentKeySession];
-[AVURLAsset _classForAssetTracks];
-[AVURLAsset _classForFigAssetInspectorLoader];
-[AVURLAsset _clientURLLoadingRepresentsAccurateNetworkStatistics];
-[AVURLAsset _doNotLogURLs];
-[AVURLAsset _ensureAssetDownloadCache];
-[AVURLAsset _errorForFigNotificationPayload:key:];
-[AVURLAsset _hasResourceLoaderDelegate];
-[AVURLAsset _installHandlerForNSURLSessionConfiguration:queue:];
-[AVURLAsset _managedAssetCache];
-[AVURLAsset _playbackItem];
-[AVURLAsset _removeUserInfoObject];
-[AVURLAsset _requiresInProcessOperation];
-[AVURLAsset _resourceLoaderWithRemoteHandlerContext:];
-[AVURLAsset _serializableCreationOptions];
-[AVURLAsset _setAssetInspectorLoader:];
-[AVURLAsset _setUserInfoObject:];
-[AVURLAsset _shouldOptimizeAccessForLinearMoviePlayback];
-[AVURLAsset _tracksDidChange];
-[AVURLAsset disallowsLoggingURLs];
-[AVURLAsset downloadDestinationURL];
-[AVURLAsset initWithFigCreationOptions:options:figAssetCreationOptions:figAssetCreationFlags:];
-[AVURLAsset initWithFileURL:offset:length:options:];
-[AVURLAsset initWithURL:offset:length:options:];
-[AVURLAsset mayRequireContentKeysForMediaDataProcessing];
-[AVURLAsset recommendedDestinationURLPathExtension];
-[AVURLAsset referenceRestrictions];
-[AVURLAsset shouldMatchDataInCacheByURLPathComponentOnly];
-[AVURLAsset shouldMatchDataInCacheByURLWithoutQueryComponent];
```
