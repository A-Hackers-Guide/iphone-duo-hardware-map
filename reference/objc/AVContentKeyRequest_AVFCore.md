# `AVContentKeyRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 10 properties, 57 instance methods, 8 class methods

## Instance variables

```
@"AVContentKeyRequestInternal" _contentKeyRequest;
```

## Properties

```
@property (Tq,R) status;
@property (T@"NSError",R) error;
@property (T@,R) identifier;
@property (T@"NSData",R,N) initializationData;
@property (T@"NSDictionary",R,C) options;
@property (TB,R) canProvidePersistableContentKey;
@property (T@"AVContentKeySpecifier",R) contentKeySpecifier;
@property (T@"AVContentKey",R) contentKey;
@property (T@"<AVContentKeyRecipient>",R,W) originatingRecipient;
@property (TB,R) canBeFulfilledWithAdvisoryKey;
```

## Class methods

```
+[AVContentKeyRequest _mergeDictionary:withItemsFrom:];
+[AVContentKeyRequest _createKeyRequestDictionaryForApp:persistentKey:serverChallenge:cryptorKeyRequestID:purpose:];
+[AVContentKeyRequest _ensureProtocolVersionList:];
+[AVContentKeyRequest _mergeDictionary:withMissingItemsFrom:];
+[AVContentKeyRequest _prepareCryptor:forRenewal:andReturnKeyRequestID:isInchargeOfKeyRequest:error:];
+[AVContentKeyRequest _validateHLSEncryptionMethod:];
+[AVContentKeyRequest _validateProtocolVersionList:];
+[AVContentKeyRequest _validateServerChallenge:];
```

## Instance methods

```
-[AVContentKeyRequest contentKey];
-[AVContentKeyRequest _requestID];
-[AVContentKeyRequest identifier];
-[AVContentKeyRequest _setError:];
-[AVContentKeyRequest dealloc];
-[AVContentKeyRequest status];
-[AVContentKeyRequest error];
-[AVContentKeyRequest contentIdentifier];
-[AVContentKeyRequest description];
-[AVContentKeyRequest options];
-[AVContentKeyRequest session];
-[AVContentKeyRequest _setStatus:];
-[AVContentKeyRequest _clearContext];
-[AVContentKeyRequest externalContentProtectionStatus];
-[AVContentKeyRequest canProvidePersistableContentKey];
-[AVContentKeyRequest processContentKeyResponseError:];
-[AVContentKeyRequest setReportGroup:];
-[AVContentKeyRequest _canRespondByRequestingPersistableContentKeyRequest];
-[AVContentKeyRequest _copyAndStoreCryptorUUID];
-[AVContentKeyRequest _copyContentKeyBoss];
-[AVContentKeyRequest _encryptionMethod];
-[AVContentKeyRequest _finishLoadingCustomURLRequestWithError:];
-[AVContentKeyRequest _finishLoadingCustomURLRequestWithResponseData:renewalDate:];
-[AVContentKeyRequest _getRetryReasonForError:];
-[AVContentKeyRequest _handleKeyResponseError:];
-[AVContentKeyRequest _handleKeyResponseSuccessWithCryptor:];
-[AVContentKeyRequest _keySystem];
-[AVContentKeyRequest _makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:error:];
-[AVContentKeyRequest _performStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:];
-[AVContentKeyRequest _prepareForKeyRenewalReturningError:];
-[AVContentKeyRequest _processContentKeyResponse:renewalDate:initializationVector:error:];
-[AVContentKeyRequest _processContentKeyResponseError:];
-[AVContentKeyRequest _sendResponseInfoToCustomURLHandlerWithRenewalDate:];
-[AVContentKeyRequest canBeFulfilledWithAdvisoryKey];
-[AVContentKeyRequest contentKeyRequestDataForApp:contentIdentifier:options:error:];
-[AVContentKeyRequest contentKeySpecifier];
-[AVContentKeyRequest disallowsLoggingURLs];
-[AVContentKeyRequest ensureCryptorWithFormatDescription:error:];
-[AVContentKeyRequest figCryptor];
-[AVContentKeyRequest identifierForLogging];
-[AVContentKeyRequest identifierString];
-[AVContentKeyRequest initWithContentKeySession:contentKeyBoss:useContentKeyBoss:keySpecifier:initializationData:keyIDFromInitializationData:contentIdentifier:isRenewalRequest:requestID:providesPersistableKey:preloadingRequestOptions:identifier:supportsOfflineKey:originatingRecipientIdentifier:];
-[AVContentKeyRequest initWithContentKeySession:reportGroup:customURLHandler:identifier:requestInfo:requestID:providesPersistableKey:isRenewalRequest:];
-[AVContentKeyRequest initWithContentKeySession:reportGroup:identifier:contentIdentifier:keyIDFromInitializationData:initializationData:preloadingRequestOptions:providesPersistableKey:];
-[AVContentKeyRequest initializationData];
-[AVContentKeyRequest keyIDFromInitializationData];
-[AVContentKeyRequest makeOptionalStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:];
-[AVContentKeyRequest makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:];
-[AVContentKeyRequest originatingRecipient];
-[AVContentKeyRequest processContentKeyResponse:];
-[AVContentKeyRequest processContentKeyResponseData:];
-[AVContentKeyRequest processContentKeyResponseData:renewalDate:error:];
-[AVContentKeyRequest renewExpiringContentKeyResponseData];
-[AVContentKeyRequest renewsExpiringResponseData];
-[AVContentKeyRequest respondByRequestingPersistableContentKeyRequest];
-[AVContentKeyRequest respondByRequestingPersistableContentKeyRequestAndReturnError:];
-[AVContentKeyRequest willOutputBeObscuredDueToInsufficientExternalProtectionForDisplays:];
```
