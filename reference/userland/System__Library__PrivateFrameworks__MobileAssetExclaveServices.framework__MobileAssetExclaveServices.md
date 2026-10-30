# `/System/Library/PrivateFrameworks/MobileAssetExclaveServices.framework/MobileAssetExclaveServices`

iOS 27.2 dyld shared cache image. Version `2215.52.1.0.0`. **[DSC]**

## Linked libraries (13)

- `/System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CryptoKit.framework/CryptoKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libMobileGestalt.dylib`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswiftos.dylib`

## Objective-C: 5 classes, 3 protocols, 35 methods, 4 properties

### Class pages

Every class and protocol, with its methods: [`MAExclaveManifestStorageServiceBaseProtocol`](../objc/MAExclaveManifestStorageServiceBaseProtocol_MobileAssetExclaveServices.protocol.md), [`MAExclaveManifestStorageServiceProtocol2`](../objc/MAExclaveManifestStorageServiceProtocol2_MobileAssetExclaveServices.protocol.md), [`NSObject`](../objc/NSObject_MobileAssetExclaveServices.protocol.md), [`SecureMobileAssetExclaveManager`](../objc/SecureMobileAssetExclaveManager_MobileAssetExclaveServices.md), [`_TtC24SecureMobileAssetExclave31MAExclaveManifestStorageService`](../objc/_TtC24SecureMobileAssetExclave31MAExclaveManifestStorageService_MobileAssetExclaveServices.md), [`_TtC24SecureMobileAssetExclave33MobileAssetExclaveServicesManager`](../objc/_TtC24SecureMobileAssetExclave33MobileAssetExclaveServicesManager_MobileAssetExclaveServices.md), [`_TtCC24SecureMobileAssetExclave31MAExclaveManifestStorageService6Server`](../objc/_TtCC24SecureMobileAssetExclave31MAExclaveManifestStorageService6Server_MobileAssetExclaveServices.md), [`_TtCC24SecureMobileAssetExclave31MAExclaveManifestStorageService7Service`](../objc/_TtCC24SecureMobileAssetExclave31MAExclaveManifestStorageService7Service_MobileAssetExclaveServices.md)

### Classes

`SecureMobileAssetExclaveManager`, `_TtC24SecureMobileAssetExclave31MAExclaveManifestStorageService`, `_TtC24SecureMobileAssetExclave33MobileAssetExclaveServicesManager`, `_TtCC24SecureMobileAssetExclave31MAExclaveManifestStorageService6Server`, `_TtCC24SecureMobileAssetExclave31MAExclaveManifestStorageService7Service`

### Protocols

`MAExclaveManifestStorageServiceBaseProtocol`, `MAExclaveManifestStorageServiceProtocol2`, `NSObject`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Swift types (13)

`SecureMobileAssetExclave.MAExclaveManifestStorageService`, `SecureMobileAssetExclave.MAExclaveManifestStorageService.Server`, `SecureMobileAssetExclave.MAExclaveManifestStorageService.Service`, `SecureMobileAssetExclave.MAExclaveManifestStorageServiceHandler`, `SecureMobileAssetExclave.MAStorageError`, `SecureMobileAssetExclave.MobileAssetExclaveServicesManager:`, `SecureMobileAssetExclave.SecureMobileAssetManifestObjectDigestsSHA256`, `SecureMobileAssetExclave.SecureMobileAssetManifestObjects`, `SecureMobileAssetExclave.SecureMobileAssetNonce`, `SecureMobileAssetExclave.SecureMobileAssetSelector`, `__C.SecureMobileAssetManifestStateEnum`, `__C.tb_error_t`, `conformance`

## Strings (45)

```
Invalid key value while decoding result type for checkManifestForSelector
Invalid key value while decoding result type for proposeNonce
init()
SecureMobileAssetExclave/MobileAssetExclaveServices_Swift.swift
: incorrect fixed-sized array length, expected 32, got 
Invalid key value while decoding result type for invalidateManifestForSelector
invalid rawValue for MAStorageError: 
Invalid key value while decoding result type for stageManifestForSelector
com.apple.mobileassetd
SecureMobileAssetExclave.MobileAssetExclaveServicesManager
com.apple.mobileassetd.service
Fatal error
Invalid key value while decoding result type for activateCommittedManifestForSelector
Invalid key value while decoding result type for commitStagedManifestForSelectors
%s invalidateManifestForSelector request succeeded.
%s could not convert string \"%s\" to UTF-8 data
%s Sending stageManifestForSelector request...
%s stageManifestForSelector request succeeded.
%s commitStagedManifestForSelectors:\nfsTags=%s\nspecifiers=%s
%s Starting conclave failed with transport error: %u
%s proposeNonce request succeeded.
%s Sending proposeNonce request...
%s checkState=%s is invalid
%s checkManifestForSelector request succeeded.
%s Successfully started com.apple.mobileasset.conclave
%s Starting com.apple.mobileasset.conclave...
%s catalogHash=%s
%s infoPlistHash=%s
%s specifierDigest=%s (%s)
%s stageManifestForSelector request failed: %@
%s commitStagedManifestForSelectors request failed: %@
%s Sending commitStagedManifestForSelectors request...
proposeNonce returning: %s
%s activateCommittedManifestForSelector request succeeded.
%s Exclaves not supported
%s proposeNonce request failed: %@
%s Sending checkManifestForSelector request...
%s commitStagedManifestForSelectors request succeeded.
%s activateCommittedManifestForSelector request failed: %@
%s Sending activateCommittedManifestForSelector request...
%s commitStagedManifestForSelectors: fsTags and specifiers have unequal count
%s manifestHash=%s
%s invalidateManifestForSelector request failed: %@
%s checkManifestForSelector request failed: %@
%s Sending invalidateManifestForSelector request...
```
