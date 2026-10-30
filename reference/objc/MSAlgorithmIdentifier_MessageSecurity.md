# `MSAlgorithmIdentifier`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 17 instance methods, 3 class methods

## Instance variables

```
@"MSOID" _algorithm;
@"NSData" _parameters;
^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}} _asn1AlgId;
```

## Properties

```
@property (T^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}},R,V_asn1AlgId) asn1AlgId;
@property (T@"MSOID",R,V_algorithm) algorithm;
@property (T@"NSData",R,V_parameters) parameters;
```

## Class methods

```
+[MSAlgorithmIdentifier digestAlgorithmWithSignatureAlgorithm:error:];
+[MSAlgorithmIdentifier algorithmIdentifierWithAsn1AlgId:error:];
+[MSAlgorithmIdentifier algorithmIdentifierWithOID:];
```

## Instance methods

```
-[MSAlgorithmIdentifier parameters];
-[MSAlgorithmIdentifier dealloc];
-[MSAlgorithmIdentifier asn1AlgId];
-[MSAlgorithmIdentifier algorithm];
-[MSAlgorithmIdentifier ccMode:];
-[MSAlgorithmIdentifier initDigestAlgorithmWithSignatureAlgorithm:error:];
-[MSAlgorithmIdentifier signatureAlgorithmWithDigestAlgorithm:error:];
-[MSAlgorithmIdentifier keySize:];
-[MSAlgorithmIdentifier hash];
-[MSAlgorithmIdentifier initWithOID:parameters:];
-[MSAlgorithmIdentifier blockSize:];
-[MSAlgorithmIdentifier initWithOID:];
-[MSAlgorithmIdentifier encode];
-[MSAlgorithmIdentifier initWithAsn1AlgId:error:];
-[MSAlgorithmIdentifier decode:error:];
-[MSAlgorithmIdentifier isEqual:];
-[MSAlgorithmIdentifier ccAlgorithm:];
```
