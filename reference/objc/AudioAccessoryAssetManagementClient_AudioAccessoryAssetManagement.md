# `AudioAccessoryAssetManagementClient`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryAssetManagement.framework/AudioAccessoryAssetManagement`](../userland/System__Library__PrivateFrameworks__AudioAccessoryAssetManagement.framework__AudioAccessoryAssetManagement.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 11 instance variables, 4 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _invalidateCalled;
B _invalidateDone;
@"RBSAssertion" _processAssertion;
i _downloadTranslationAssetsPid;
@"NSXPCConnection" _xpcCnx;
@"NSXPCConnection" _xpcAADCnx;
@"NSArray" _translationAssets;
@? _interruptionHandler;
@? _invalidationHandler;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _translationAssetsInfoHandler;
```

## Properties

```
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_translationAssetsInfoHandler) translationAssetsInfoHandler;
```

## Class methods

```
+[AudioAccessoryAssetManagementClient supportsSecureCoding];
```

## Instance methods

```
-[AudioAccessoryAssetManagementClient dispatchQueue];
-[AudioAccessoryAssetManagementClient _ensureXPCStarted];
-[AudioAccessoryAssetManagementClient setInvalidationHandler:];
-[AudioAccessoryAssetManagementClient init];
-[AudioAccessoryAssetManagementClient interruptionHandler];
-[AudioAccessoryAssetManagementClient setDispatchQueue:];
-[AudioAccessoryAssetManagementClient invalidate];
-[AudioAccessoryAssetManagementClient _interrupted];
-[AudioAccessoryAssetManagementClient encodeWithCoder:];
-[AudioAccessoryAssetManagementClient setInterruptionHandler:];
-[AudioAccessoryAssetManagementClient initWithCoder:];
-[AudioAccessoryAssetManagementClient invalidationHandler];
-[AudioAccessoryAssetManagementClient _invalidated];
-[AudioAccessoryAssetManagementClient downloadTranslationAssets:useCellular:showDownloadCompleteNotification:completion:];
-[AudioAccessoryAssetManagementClient _ensureAADXPCStarted];
-[AudioAccessoryAssetManagementClient _invalidateXPCServiceAssertion];
-[AudioAccessoryAssetManagementClient _takeXPCServiceAssertion];
-[AudioAccessoryAssetManagementClient downloadTranslationAssets:useCellular:completion:];
-[AudioAccessoryAssetManagementClient getTranslationAssets];
-[AudioAccessoryAssetManagementClient getTranslationAssets:error:];
-[AudioAccessoryAssetManagementClient getTranslationAssetsDownloadSize:completion:];
-[AudioAccessoryAssetManagementClient pidOfDownloadTranslationAssetsXPCService:];
-[AudioAccessoryAssetManagementClient setTranslationAssetsInfoHandler:];
-[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:];
-[AudioAccessoryAssetManagementClient translationAssetsInfoHandler];
```
