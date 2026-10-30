# `/System/Library/PrivateFrameworks/EDPSecurity.framework/EDPSecurity`

iOS 27.2 dyld shared cache image. Version `18.0.1.0.0`. **[DSC]**

## Linked libraries (14)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/CryptoKit.framework/CryptoKit`
- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswiftos.dylib`

## Objective-C: 8 classes, 0 protocols, 14 methods, 5 properties

### Class pages

Every class and protocol, with its methods: [`EDPUtilities`](../objc/EDPUtilities_EDPSecurity.md), [`SignatureResponse`](../objc/SignatureResponse_EDPSecurity.md), [`ValidationResponse`](../objc/ValidationResponse_EDPSecurity.md), [`_TtC11EDPSecurity12FileMeasurer`](../objc/_TtC11EDPSecurity12FileMeasurer_EDPSecurity.md), [`_TtC11EDPSecurity13PackageSigner`](../objc/_TtC11EDPSecurity13PackageSigner_EDPSecurity.md), [`_TtC11EDPSecurity16PackageValidator`](../objc/_TtC11EDPSecurity16PackageValidator_EDPSecurity.md), [`_TtC11EDPSecurity16ResourceManifest`](../objc/_TtC11EDPSecurity16ResourceManifest_EDPSecurity.md), [`_TtC11EDPSecurity22PackageStaticValidator`](../objc/_TtC11EDPSecurity22PackageStaticValidator_EDPSecurity.md)

### Classes

`EDPUtilities`, `SignatureResponse`, `ValidationResponse`, `_TtC11EDPSecurity12FileMeasurer`, `_TtC11EDPSecurity13PackageSigner`, `_TtC11EDPSecurity16PackageValidator`, `_TtC11EDPSecurity16ResourceManifest`, `_TtC11EDPSecurity22PackageStaticValidator`

### Properties

```
@property (T@"NSData",&,N,Vsignature) signature;
@property (T@"NSError",&,N,Verror) error;
@property (T@"NSData",&,N,VvalidatedData) validatedData;
@property (TB,N,VisTrusted) isTrusted;
@property (T@"NSArray",&,N,VcertificateChain) certificateChain;
```

## Swift types (16)

`EDPSecurity.FileMeasurement`, `EDPSecurity.FileMeasurement.CodingKeys`, `EDPSecurity.FileMeasurementError`, `EDPSecurity.FileMeasurer`, `EDPSecurity.PackageSigner`, `EDPSecurity.PackageSignerError`, `EDPSecurity.PackageStaticValidator:`, `EDPSecurity.PackageValidator`, `EDPSecurity.PackageValidatorError`, `EDPSecurity.ResourceManifest`, `EDPSecurity.ResourceManifest.CodingKeys`, `EDPSecurity.ResourceManifestError`, `__C.NSURLResourceKey`, `__C.SecCSDigestAlgorithm`, `__C.SecCertificateRef`, `conformance`

## Strings (9)

```
Security
DigestAlgorithm
EDPSecurity.PackageStaticValidator
init(signatureData:requireTrust:)
hash2
hash5
<ResourceManifest: v
KeyType
MSErrorTrustDomain
```
