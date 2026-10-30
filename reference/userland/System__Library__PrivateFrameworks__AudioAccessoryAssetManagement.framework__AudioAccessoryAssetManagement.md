# `/System/Library/PrivateFrameworks/AudioAccessoryAssetManagement.framework/AudioAccessoryAssetManagement`

iOS 27.2 dyld shared cache image. Version `41.7.0.0.0`. **[DSC]**

## Linked libraries (8)

- `/System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/Translation.framework/Translation`
- `/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices`

## Objective-C: 2 classes, 6 protocols, 109 methods, 9 properties

### Class pages

Every class and protocol, with its methods: [`AAServicesXPCClientInterface`](../objc/AAServicesXPCClientInterface_AudioAccessoryAssetManagement.protocol.md), [`AAServicesXPCDaemonInterface`](../objc/AAServicesXPCDaemonInterface_AudioAccessoryAssetManagement.protocol.md), [`AMTranslationAssetInfo`](../objc/AMTranslationAssetInfo_AudioAccessoryAssetManagement.md), [`AudioAccessoryAssetManagementClient`](../objc/AudioAccessoryAssetManagementClient_AudioAccessoryAssetManagement.md), [`AudioAccessoryAssetManagementXPCClientInterface`](../objc/AudioAccessoryAssetManagementXPCClientInterface_AudioAccessoryAssetManagement.protocol.md), [`AudioAccessoryAssetManagementXPCServiceInterface`](../objc/AudioAccessoryAssetManagementXPCServiceInterface_AudioAccessoryAssetManagement.protocol.md), [`NSCoding`](../objc/NSCoding_AudioAccessoryAssetManagement.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_AudioAccessoryAssetManagement.protocol.md)

### Classes

`AMTranslationAssetInfo`, `AudioAccessoryAssetManagementClient`

### Protocols

`AAServicesXPCClientInterface`, `AAServicesXPCDaemonInterface`, `AudioAccessoryAssetManagementXPCClientInterface`, `AudioAccessoryAssetManagementXPCServiceInterface`, `NSCoding`, `NSSecureCoding`

### Properties

```
@property (class, TB,R) supportsSecureCoding;
@property (T@"NSLocale",&,N,V_locale) locale;
@property (T@"NSString",&,N,V_displayName) displayName;
@property (TC,N,V_assetStatus) assetStatus;
@property (TB,N,V_isSuggested) isSuggested;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_translationAssetsInfoHandler) translationAssetsInfoHandler;
```

## Strings (68)

```
getting Show download languages notification WithCompletion
### XPC connection unexpectedly invalidated
dnam
Downloading Translation Assets localeIdentifiers %@, useCellular %s showDownloadCompleteNotification %s
yes
-[AudioAccessoryAssetManagementClient invalidate]_block_invoke
pidOfDownloadTranslationAssetsXPCService: %ld
AudioAccessoryAssetManagement
tast
lcal
AMTranslationAssetInfo: assetStatus %s, displayName %@, isSuggested %d locale %@
Failed acquiring the assertion with error %@
downloadTranslationAssets succeeded: %@
com.apple.audioAccessoryAssetManagement
-[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:]_block_invoke_2
com.apple.AudioAccessoryAssetManagementXPCService
### getTranslationAssetsDownloadSize failed
Show download languages notification returning with error %{error}
com.apple.AudioAccessoryServices
### Activate XPC error: %{error}
v16@?0@\"NSError\"8
-[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:]_block_invoke
### Interrupted
Invalidating
Assertion acquired successfully
-[AudioAccessoryAssetManagementClient showDownloadLanguagesNotification:]_block_invoke_3
com.apple.AudioAccessoryAssetManagement
Downloaded
InProgress
-[AudioAccessoryAssetManagementClient downloadTranslationAssets:useCellular:showDownloadCompleteNotification:completion:]_block_invoke_2
AudioAccessoryAssetManagementClient
NotDownloaded
Show download languages notification with error: %{error}
getTranslationAssetsWithCompletion succeeded: AMTranslationAssetInfo: assetStatus %s, displayName %@, isSuggested %d locale %@\n
### ### downloadTranslationAssets failed: %@, %@
### getTranslationAssetsWithCompletion failed
-[AudioAccessoryAssetManagementClient getTranslationAssets]_block_invoke_2
### Show download languages notification failed
v32@?0@\"AMTranslationAssetInfo\"8Q16^B24
?
Invalidated
-[AudioAccessoryAssetManagementClient _takeXPCServiceAssertion]
-[AudioAccessoryAssetManagementClient downloadTranslationAssets:useCellular:showDownloadCompleteNotification:completion:]_block_invoke
-[AudioAccessoryAssetManagementClient downloadTranslationAssets:useCellular:showDownloadCompleteNotification:completion:]_block_invoke_3
unknown
Giving runtime to XPCService
getting TranslationAssets WithCompletion
-[AudioAccessoryAssetManagementClient _interrupted]
### downloadTranslationAssets failed
no
downloadTranslationAssets: failed with %{error} 
_downloadTranslationAssetsPid is 0 returning
-[AudioAccessoryAssetManagementClient _invalidated]
-[AudioAccessoryAssetManagementClient getTranslationAssetsDownloadSize:completion:]_block_invoke_2
processIdentifier is nil returning
target is nil returning
### ### getTranslationAssetsDownloadSize failed: %@, %@
getTranslationAssetsDownloadSize localeIdentifiers %@
-[AudioAccessoryAssetManagementClient pidOfDownloadTranslationAssetsXPCService:]
-[AudioAccessoryAssetManagementClient getTranslationAssetsDownloadSize:completion:]_block_invoke
v8@?0
-[AudioAccessoryAssetManagementClient getTranslationAssets:error:]_block_invoke
isgt
Unknown
processHandle is nil returning with error %@
-[AudioAccessoryAssetManagementClient getTranslationAssets]_block_invoke
### ### getTranslationAssetsWithCompletion failed: %@, %@
### ### Show download languages notification failed: %@, %@
```
