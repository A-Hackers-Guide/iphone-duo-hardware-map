# `_TtC24SecureMobileAssetExclave33MobileAssetExclaveServicesManager`

- Image: [`/System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/MobileAssetExclaveServices`](../userland/System__Library__PrivateFrameworks__MobileAssetExclaveServices.framework__MobileAssetExclaveServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MAExclaveManifestStorageServiceProtocol2`
- 3 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
os.Logger log;
_$sSo6NSLockC lock;
SecureMobileAssetExclave.MAExclaveManifestStorageService.Service tbClient;
```

## Instance methods

```
-[_TtC24SecureMobileAssetExclave33MobileAssetExclaveServicesManager init];
-[_TtC24SecureMobileAssetExclave33MobileAssetExclaveServicesManager activateCommittedManifestForFSTag:specifier:error:];
-[_TtC24SecureMobileAssetExclave33MobileAssetExclaveServicesManager checkManifestForFSTag:specifier:state:manifest:infoPlist:catalog:isValid:error:];
-[_TtC24SecureMobileAssetExclave33MobileAssetExclaveServicesManager commitStagedManifestForFSTags:specifiers:error:];
-[_TtC24SecureMobileAssetExclave33MobileAssetExclaveServicesManager invalidateManifestForFSTag:specifier:error:];
-[_TtC24SecureMobileAssetExclave33MobileAssetExclaveServicesManager proposeNonce:];
-[_TtC24SecureMobileAssetExclave33MobileAssetExclaveServicesManager stageManifestForFSTag:specifier:manifest:infoPlist:catalog:error:];
-[_TtC24SecureMobileAssetExclave33MobileAssetExclaveServicesManager initWithConclave:];
```
