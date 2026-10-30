# `AVContentKeySession`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVIntegrityChecking`
- 1 instance variables, 13 properties, 78 instance methods, 8 class methods

## Instance variables

```
@"AVContentKeySessionInternal" _session;
```

## Properties

```
@property (TB,R,N,GisInternal) internal;
@property (T@"AVContentKeyReportGroup",R) defaultContentKeyGroup;
@property (TB,R,N,GisDefunct) defunct;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<AVContentKeySessionDelegate>",R,W) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R) delegateQueue;
@property (T@"NSURL",R) storageURL;
@property (T@"NSString",R) keySystem;
@property (TB) supportsAdvisoryKeys;
@property (T@"NSData",R) contentProtectionSessionIdentifier;
```

## Class methods

```
+[AVContentKeySession initialize];
+[AVContentKeySession contentKeySessionWithKeySystem:];
+[AVContentKeySession _uniqueIDForCyptorUUID:cryptorKeyRequestID:];
+[AVContentKeySession contentKeySessionWithKeySystem:storageDirectoryAtURL:];
+[AVContentKeySession contentKeySessionWithLegacyWebKitCompatibilityModeAndKeySystem:storageDirectoryAtURL:];
+[AVContentKeySession copyDefaultSecureStopManagerForAppIdentifier:storageDirectoryAtURL:];
+[AVContentKeySession pendingExpiredSessionReportsWithAppIdentifier:storageDirectoryAtURL:];
+[AVContentKeySession removePendingExpiredSessionReports:withAppIdentifier:storageDirectoryAtURL:];
```

## Instance methods

```
-[AVContentKeySession isInternal];
-[AVContentKeySession setDelegate:queue:];
-[AVContentKeySession _processContentKeyRequestWithIdentifier:encryptionMethod:supportedProtocolVersions:options:groupID:error:];
-[AVContentKeySession createAndInstallCustomURLHandlerForAsset:outHandler:];
-[AVContentKeySession initWithKeySystem:storageDirectoryAtURL:internal:];
-[AVContentKeySession _contentKeyRequestForCryptorUUID:cryptorKeyRequestID:];
-[AVContentKeySession setAppIdentifier:];
-[AVContentKeySession issueContentKeyRequestWithCustomURLHandler:identifier:requestInfo:requestID:providesPersistableKey:];
-[AVContentKeySession issueContentKeyRequests:forInitializationData:];
-[AVContentKeySession defaultGroupID];
-[AVContentKeySession _removeContentKeyRequestForCryptorUUID:cryptorKeyRequestID:];
-[AVContentKeySession makeContentKeyGroup];
-[AVContentKeySession setSupportsAdvisoryKeys:];
-[AVContentKeySession init];
-[AVContentKeySession contentKeyRecipients];
-[AVContentKeySession issueContentKeyRequestWithPreloadingRequestOptions:identifier:initializationData:providesPersistableKey:];
-[AVContentKeySession contentKeyRequestDidSucceedWithBoss:keySpecifier:requestID:cryptor:];
-[AVContentKeySession dealloc];
-[AVContentKeySession _processContentKeyRequestWithIdentifier:initializationData:options:groupID:];
-[AVContentKeySession _invokeDelegateCallbackWithBlock:synchronouslyWhenDelegateQueueIsNULL:];
-[AVContentKeySession issueRenewableContentKeyRequest:];
-[AVContentKeySession keyRequestByID:];
-[AVContentKeySession copyCryptorForCryptKeyAttributes:];
-[AVContentKeySession createCryptorIfNecessaryForInitializationData:formatDescription:error:];
-[AVContentKeySession processContentKeyRequestForPSSHEntries:initializationData:groupID:options:];
-[AVContentKeySession _internalQueue];
-[AVContentKeySession _contentKeyGroups];
-[AVContentKeySession isDefunct];
-[AVContentKeySession issueContentKeyRequest:toDelegateWithCallbackSelector:];
-[AVContentKeySession processContentKeyRequestForTransportStreamWithCodecType:initializationData:groupID:options:];
-[AVContentKeySession supportsAdvisoryKeys];
-[AVContentKeySession _handleSecureStopDidFinalizeRecordCallback];
-[AVContentKeySession setDelegate:];
-[AVContentKeySession keySystem];
-[AVContentKeySession trackRequest:byRequestID:];
-[AVContentKeySession _sendFinishLoadingForPreloadedKeyRequest:withRequestID:fromHandler:error:];
-[AVContentKeySession storageURL];
-[AVContentKeySession _weakReference];
-[AVContentKeySession initWithStorageDirectoryAtURL:];
-[AVContentKeySession removeResourcesForID:];
-[AVContentKeySession addContentKeyRecipient:];
-[AVContentKeySession clientCanReceivePersistableContentKeyRequest];
-[AVContentKeySession hasProtector];
-[AVContentKeySession issuePersistableContentKeyRequest:];
-[AVContentKeySession delegate];
-[AVContentKeySession _setWeakReferenceForContentKeyRequest:withCryptorUUID:];
-[AVContentKeySession issuePersistableContentKeyRequestForKeySpecifier:initializationData:keyIDFromInitializationData:contentIdentifier:requestID:preloadingRequestOptions:identifier:originatingRecipientIdentifier:];
-[AVContentKeySession didProvideKeyRequestWithBoss:keySpecifier:requestID:renewalRequest:supportsOfflineKey:originatingRecipientIdentifier:];
-[AVContentKeySession processContentKeyRequestWithIdentifier:initializationData:options:];
-[AVContentKeySession expire];
-[AVContentKeySession description];
-[AVContentKeySession copyCryptorForInitializationData:];
-[AVContentKeySession _makeContentKeyGroupWithIDOut:error:];
-[AVContentKeySession _setContentKeyRequest:forCryptorUUID:cryptorKeyRequestID:];
-[AVContentKeySession removeContentKeyRecipient:];
-[AVContentKeySession _handleUpdateToPersistentKey:forKeyIdentifier:];
-[AVContentKeySession _handleKeyResponseSuccessfullyProcessedForCryptorUUID:andCryptorKeyRequestID:];
-[AVContentKeySession processContentKeyRequestForSinf:initializationData:groupID:options:];
-[AVContentKeySession initWithKeySystem:storageDirectoryAtURL:legacyWebKitCompatibilityMode:];
-[AVContentKeySession contentProtectionSessionIdentifier];
-[AVContentKeySession externalProtectionStateChangedCallbackWithBoss:keySpecifier:];
-[AVContentKeySession delegateQueue];
-[AVContentKeySession contentKeyRequestDidProduceContentKey:];
-[AVContentKeySession renewExpiringResponseDataForContentKeyRequest:];
-[AVContentKeySession _getOriginatingRecipientForUniqueIdentifier:];
-[AVContentKeySession _handleExternalProtectionStateChangedCallbackForCryptKeyIdentifier:];
-[AVContentKeySession _handleRequest:withRequestID:fromHandler:willHandleRequest:];
-[AVContentKeySession _willDeallocOrFinalize];
-[AVContentKeySession _handleKeyResponseError:forCryptorUUID:andCryptorKeyRequestID:];
-[AVContentKeySession defaultContentKeyGroup];
-[AVContentKeySession makeSecureTokenForExpirationDateOfPersistableContentKey:completionHandler:];
-[AVContentKeySession _handleContentProtectionSessionIdentifierDidChange:];
-[AVContentKeySession copyCryptorForFormatDescription:cryptorOut:errorOut:];
-[AVContentKeySession invalidateAllPersistableContentKeysForApp:options:completionHandler:];
-[AVContentKeySession issueContentKeyRequestForInitializationData:];
-[AVContentKeySession invalidatePersistableContentKey:options:completionHandler:];
-[AVContentKeySession _renewKeyWithIdentifier:encryptionMethod:initializationData:contentIdentifier:keyIDFromInitializationData:options:error:];
-[AVContentKeySession issueContentKeyRequest:];
```
