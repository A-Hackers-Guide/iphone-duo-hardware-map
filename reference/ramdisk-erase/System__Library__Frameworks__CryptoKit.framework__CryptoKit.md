# `/System/Library/Frameworks/CryptoKit.framework/CryptoKit`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,110,400 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 33 (Size: 4944)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (15)

- `/System/Library/Frameworks/CryptoKit.framework/CryptoKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/CryptoKitCBridging (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit (compatibility version 0.0.0, current version 878.40.5)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3, weak)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (3 classes, 0 protocols)

Classes: `_TtC9CryptoKit12SequenceDrbg`, `_TtC9CryptoKit3Rng`, `_TtC9CryptoKit4Drbg`

## Strings (67)

```
publicKey
respondsToSelector:
drbgCtx
ccDigestInfo
exchangeKey:algorithms:parameters:error:
objectForObjectID:error:
objectID
randomBytesPtr
ccDigestCtx
custom
init
initWithToken:LAContext:parameters:error:
initWithTokenID:
sequenceState
sign:algorithms:parameters:error:
createObjectWithAttributes:error:
dataFromACL:
decapsulate:algorithms:parameters:error:
groupOrderByteCountForCP:
state
tokenIDs
boolValue
drbgInfo
ExportOnly should not return a key size.
CryptoKit/Ed25519Keys_cc.swift
CryptoKit/ECDSA_cc.swift
CryptoKit/SEP_P384.swift
CryptoKit/X25519Keys_cc.swift
CryptoKit/SEP_MLDSA.swift
CryptoKit/ECDH.swift
ECDHP256-mKEM-DEM-Key
generate() is not available on HPKE.DHKEM.PrivateKey, use generate(kem:) instead.
CryptoKit/SEP_P256.swift
CryptoKit/MLDSA_cc.swift
CryptoKit/ANSIx963.swift
Invalid parameter size
Fatal error
CryptoKit/AES-GCM.swift
CryptoKit/ChaChaPoly.swift
CryptoKit/X448Keys_cc.swift
CryptoKit/Ed448Keys_cc.swift
CryptoKit/Kyber.swift
CryptoKit/HPKE-AEAD.swift
ECDHP256-mKEM-KEM-Key
ECDHP256-mKEM-Authenticating-Data
CryptoKit/XWing_cc.swift
CryptoKit/ECDSA_ctk.swift
CryptoKit/KeyDiversificationNISTCurves.swift
SHA3_256 digest: 
SHA3_384 digest: 
ExportOnly should not return a nonce size.
CryptoKit/AES-CCM_cc.swift
u_SystemKeychainAlways
ASN1.ASN1ParserNode(identifier: 
SHA3_512 digest: 
CryptoKit/Nonces_ccm.swift
CryptoKit/SubjectPublicKeyInfo.swift
ExportOnly should not return a tag size.
CryptoKit/DHKEM.swift
CryptoKit/MLKEM_cc.swift
CryptoKit/ECDSA.swift
CryptoKit/SEP_MLKEM.swift
CryptoKit/SEP_Curve25519.swift
_TtCV9CryptoKit11SecureBytes7Backing
_TtC9CryptoKit3Rng
_TtC9CryptoKit4Drbg
_TtC9CryptoKit12SequenceDrbg
```
