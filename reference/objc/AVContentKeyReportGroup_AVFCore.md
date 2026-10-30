# `AVContentKeyReportGroup`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 1 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" _contentKeySessionWeakReference;
^{OpaqueFigContentKeySession=} _figContentKeySession;
@"NSData" _protectorSessionIdentifier;
@"NSMutableArray" _cryptorsList;
@"NSObject<OS_dispatch_queue>" _serialQueue;
@"NSString" _keySystem;
Q _groupID;
B _isExpired;
^{OpaqueFigCFWeakReferenceHolder=} _weakContentKeyBoss;
B _useContentKeyBoss;
```

## Properties

```
@property (T@"NSData",R) contentProtectionSessionIdentifier;
```

## Instance methods

```
-[AVContentKeyReportGroup dealloc];
-[AVContentKeyReportGroup copyCryptorForCryptKeyAttributes:];
-[AVContentKeyReportGroup hasProtector];
-[AVContentKeyReportGroup processContentKeyRequestWithIdentifier:initializationData:options:];
-[AVContentKeyReportGroup expire];
-[AVContentKeyReportGroup contentProtectionSessionIdentifier];
-[AVContentKeyReportGroup _contentKeyBoss];
-[AVContentKeyReportGroup _associateRequestWithGroupWithRequestID:error:];
-[AVContentKeyReportGroup _contentKeySession];
-[AVContentKeyReportGroup _destroyContentKeyGroupWithError:];
-[AVContentKeyReportGroup _figContentKeySession];
-[AVContentKeyReportGroup _processContentKeyRequestWithIdentifier:contentIdentifier:keyIDFromInitializationData:initializationData:options:];
-[AVContentKeyReportGroup _processContentKeyRequestWithKeyRequestFromPSSH:decryptFormatType:initializationData:options:];
-[AVContentKeyReportGroup _setAuthorizationToken:forIdentifier:error:];
-[AVContentKeyReportGroup associateContentKeyRequest:];
-[AVContentKeyReportGroup configureAppIdentifier:];
-[AVContentKeyReportGroup copyCryptorForIdentifier:initializationData:];
-[AVContentKeyReportGroup createCryptorIfNecessaryForIdentifier:initializationData:formatDescription:hlsMethod:error:];
-[AVContentKeyReportGroup createProtectorSessionIdentifierIfNecessary];
-[AVContentKeyReportGroup cryptorOptionsForIdentifier:initializationData:formatDescription:hlsMethod:];
-[AVContentKeyReportGroup externalProtectionStatusForCryptor:withDisplays:];
-[AVContentKeyReportGroup failProcessingContentKeyRequestWithIdentifier:initializationData:error:];
-[AVContentKeyReportGroup initWithKeySystem:keySession:contentKeyBoss:useContentKeyBoss:groupID:storageDirectoryAtURL:];
```
