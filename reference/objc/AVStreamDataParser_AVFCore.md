# `AVStreamDataParser`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVIntegrityChecking`, `AVContentKeyRecipient`, `AVContentKeySessionDelegate`
- 1 instance variables, 19 properties, 55 instance methods, 5 class methods

## Instance variables

```
@"AVStreamDataParserInternal" _parser;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSData",R) contentProtectionSessionIdentifier;
@property (TB,R,N) mayRequireContentKeysForMediaDataProcessing;
@property (TB,N) preferSandboxedParsing;
@property (TB,R,N,GisDefunct) defunct;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<AVStreamDataParserOutputHandling>",R,N) delegate;
@property (Tq,R) status;
@property (Tq,R) status2;
@property (T@"NSError",R) error;
@property (T@"NSArray",C,N) allowableMIMETypes;
@property (T@"NSArray",R,N) fullListOfAllowableMIMETypes;
@property (T@"AVAsset",R,N) asset;
```

## Class methods

```
+[AVStreamDataParser _createBlockBufferUsingNSData:withOffset:withLength:];
+[AVStreamDataParser _createNSDataWithBlockBuffer:];
+[AVStreamDataParser audiovisualMIMETypes];
+[AVStreamDataParser canParseExtendedMIMEType:];
+[AVStreamDataParser outputMIMECodecParameterForInputMIMECodecParameter:];
```

## Instance methods

```
-[AVStreamDataParser asset];
-[AVStreamDataParser init];
-[AVStreamDataParser _setError:];
-[AVStreamDataParser dealloc];
-[AVStreamDataParser status];
-[AVStreamDataParser error];
-[AVStreamDataParser isDefunct];
-[AVStreamDataParser setSession:];
-[AVStreamDataParser setDelegate:];
-[AVStreamDataParser hasProtector];
-[AVStreamDataParser delegate];
-[AVStreamDataParser expire];
-[AVStreamDataParser contentKeySession];
-[AVStreamDataParser setStatus:];
-[AVStreamDataParser contentProtectionSessionIdentifier];
-[AVStreamDataParser _willDeallocOrFinalize];
-[AVStreamDataParser _figManifold:formatDescription:orDecryptorDidChange:forTrackID:];
-[AVStreamDataParser status2];
-[AVStreamDataParser _ICYIsAllowed];
-[AVStreamDataParser _MPEG2TSIsAllowed];
-[AVStreamDataParser _MovieFragmentStreamIsAllowed];
-[AVStreamDataParser _WebVTTIsAllowed];
-[AVStreamDataParser _appendStreamData:withFlags:];
-[AVStreamDataParser _attachToContentKeySession:contentKeyBoss:failedSinceAlreadyAttachedToAnotherSession:];
-[AVStreamDataParser _attachedToExternalContentKeySession];
-[AVStreamDataParser _configureInternal];
-[AVStreamDataParser _createAssetIfNecessary];
-[AVStreamDataParser _createFigManifold:manifold:];
-[AVStreamDataParser _createFigManifoldRemote:manifold:];
-[AVStreamDataParser _createFigManifoldWithBlockBuffer:manifold:];
-[AVStreamDataParser _figManifold:discoveredNewTrackID:mediaType:];
-[AVStreamDataParser _figManifold:pushedSampleBuffer:trackID:flags:];
-[AVStreamDataParser _figManifold:trackDidEnd:];
-[AVStreamDataParser _figManifoldAllNewTracksReady:];
-[AVStreamDataParser _fullListOfAllowableMIMETypes];
-[AVStreamDataParser _registerForFigManifoldCallbacksForTrackID:];
-[AVStreamDataParser _unregisterForFigManifoldCallbacksForTrackID:];
-[AVStreamDataParser allowableMIMETypes];
-[AVStreamDataParser appendStreamData:];
-[AVStreamDataParser appendStreamData:withFlags:];
-[AVStreamDataParser contentKeySession:didProvideContentKeyRenewalRequest:];
-[AVStreamDataParser contentKeySession:didProvideContentKeyRequest:];
-[AVStreamDataParser contentKeySessionContentProtectionSessionIdentifierDidChange:];
-[AVStreamDataParser fullListOfAllowableMIMETypes];
-[AVStreamDataParser mayRequireContentKeysForMediaDataProcessing];
-[AVStreamDataParser preferSandboxedParsing];
-[AVStreamDataParser processContentKeyResponseData:forTrackID:];
-[AVStreamDataParser processContentKeyResponseError:forTrackID:];
-[AVStreamDataParser providePendingMediaData];
-[AVStreamDataParser renewExpiringContentKeyResponseDataForTrackID:];
-[AVStreamDataParser setAllowableMIMETypes:];
-[AVStreamDataParser setPreferSandboxedParsing:];
-[AVStreamDataParser setShouldProvideMediaData:forTrackID:];
-[AVStreamDataParser shouldProvideMediaDataForTrackID:];
-[AVStreamDataParser streamingContentKeyRequestDataForApp:contentIdentifier:trackID:options:error:];
```
