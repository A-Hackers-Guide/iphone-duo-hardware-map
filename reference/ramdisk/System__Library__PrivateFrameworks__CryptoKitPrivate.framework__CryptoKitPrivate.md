# `/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,251,136 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 34 (Size: 5328)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (17)

- `/System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/CryptoKitCBridging.framework/CryptoKitCBridging (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CryptoKit.framework/CryptoKit (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit (compatibility version 0.0.0, current version 878.40.5)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf (compatibility version 1.0.0, current version 1.0.0)`
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

## Objective-C (39 classes, 0 protocols)

Classes: `ARCAwaitingActivation`, `ARCCredential`, `ARCPresentation`, `ARCResponse`, `ARCTestServer`, `ATHMAwaitingActivation`, `ATHMPresentation`, `ATHMTestServer`, `CKPATKeyBlinding`, `RSABSSATokenBlinder`, `RSABSSATokenIssuer`, `RSABSSATokenReady`, `RSABSSATokenWaitingActivation`, `TDMEvaluation`, `TDMTestServer`, `TDMToken`, `_TtC16CryptoKitPrivate10ATHMClient`, `_TtC16CryptoKitPrivate10ATHMServer`, `_TtC16CryptoKitPrivate12SequenceDrbg`, `_TtC16CryptoKitPrivate18ATHMKeyCommitments`, `_TtC16CryptoKitPrivate18AlishaSPAKE2Prover`, `_TtC16CryptoKitPrivate18CKPIETFKeyBlinding`, `_TtC16CryptoKitPrivate19RSAPSSSPKI_Bridging`, `_TtC16CryptoKitPrivate19TDMServerEvaluation`, `_TtC16CryptoKitPrivate20ARCCredentialWrapper`, `_TtC16CryptoKitPrivate22ARCPresentationWrapper`, `_TtC16CryptoKitPrivate27AlishaSPAKE2ProverConfirmed`, `_TtC16CryptoKitPrivate28ARCAwaitingActivationWrapper`, `_TtC16CryptoKitPrivate3Rng`, `_TtC16CryptoKitPrivate4Drbg`, `_TtC16CryptoKitPrivate6Scrypt`, `_TtC16CryptoKitPrivate9ARCServer`, `_TtC16CryptoKitPrivate9TDMClient`, `_TtC16CryptoKitPrivate9TDMServer`, `_TtCO16CryptoKitPrivate15CKSecretSharing32CKShamirShareSharedInternalState`, `_TtCO16CryptoKitPrivate15CKSecretSharingP33_CE506D4359C10354E8EAAF853DBEE0AA32CKHybridSecretShareInternalState`, `_TtCO16CryptoKitPrivate2HE12ParamContext`, `_TtCO16CryptoKitPrivate2HE13ObjectStorage`, `_TtCO16CryptoKitPrivate2HE24ObjectStorageWithZeroize`

## Strings (485)

```
Serialized Share not large enough
includeThreshold
insecureToChangeIncludeMessageEntropy
Shares numbers (not necessarily indexes) 
recoverHybridSecretKeyFromShamirShares(shareArray:)
n_4096_logq_27_28_28_logt_7
 vs. expected (state.cSuiteParams.gcmKeyByteCount)
 Serialized sealed box nonce length does not match provided ciphersuite parameters 
 in the array are inconsistent
ARC.error
Failed in ccss_shamir_share_bag_recover_secret with error 
CryptoKitPrivate/TDMOPRFBridging.swift
Unsupported ciphersuite in Protobuf Deserialized HybridSecretSharingSharedState. Must be .aesGcm256128
\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0
Share index must be greater than 0 and less than 
CredentialResponse
n_4096_logq_27_28_28_logt_5
 Serialized nonce length does not match provided ciphersuite parameters 
recoverSecret(shares:)
Unsupported H2G ciphersuite.
Unexpected error: Shamir Share Generator failed to generate share
Only Protobuf version 1 is supported, provided version 
CryptoKitPrivate.ARCAwaitingActivationWrapper
CredentialRequest
threshold
quantum128
n_8192_logq_3x55_logt_42
com.apple.cryptokit.ATHM.error
init(threshold:secret:supportedPrime:)
CryptoKitPrivate.ARCCredentialWrapper
CryptoKitPrivate/ARCBridging.swift
TokenResponseProof
TDM: Serialization of scalar s unexpectedly failed.
Failed in ccss_shamir_parameters_init with error 
CryptoKitPrivate.TDMServerEvaluation
n_4096_logq_27_28_28_logt_16
CoreCrypto Error in call to underlying CryptoKit calls with error 
CryptoKitPrivate/CKPIETFKeyBlinding.swift
The scrypt derivation did not return a result of the expected length, or failed.
iv
insecure_n_16_logq_60_logt_15
n_8192_logq_29_60_60_logt_15
Serialized share's version is not supported
CryptoKitPrivate/UnlinkableTokenAPI.swift
CryptoKitSecretSharing.SecretShare
n_4096_logq_27_28_28_logt_13
n_8192_logq_3x55_logt_30
init(threshold:secret:associatedData:includeADInShares:includeThresholdInShares:ciphersuite:insecureToChangeIncludeMessageEntropy:)
Underlying CryptoKit call had incorrect parameter size in recoverSecret?
init(threshold:authenticatedData:includeADInShares:includeThresholdInShares:ciphersuite:insecureToChangeIncludeMessageEntropy:)
Failed in ccss_shamir_share_bag_add_share with error 
CryptoKitPrivate.ATHMServer
ciphersuite
AES_GCM_256_128
associated_data
 and a sealedBox 
AESGCMNonceForCKHybridSecretSharing
tag
TDM: Serialization of scalar c unexpectedly failed.
\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0r
Addition unexpectedly failed in corecrypto with error code: 
 Serialized sealed box tag length does not match provided ciphersuite parameters 
numberOfShares must be greater than threshold
Share Index must be greater than 0
Unsupported prime and associated parameters in Protobuf Deserialized ShamirSecretSharingSharedState. Must be .p2E128M159
Multiplication unexpectedly failed in corecrypto with error code: 
BGV
includeAuthenticatedData
shamirGeneratorState
Unimplemented arbitrary exponentiation
BFV
Failed in ccss_shamir_parameters_init_bridge (ccss_shamir_parameters_init) with error 
CryptoKitPrivate/ATHMBridging.swift
CryptoKitSecretSharing.HybridSecretSharingGeneratorSerialization
Recomputed GCM Ciphertext does not match the one embedded in shares
numberOfShares must be at least the threshold
Failed in ccss_sizeof_shamir_share_generator_serialization
insecure_n_512_logq_4x60_logt_20
corecrypto_error
Failed in ccss_shamir_share_generator_init secret is not smaller than prime
u_SystemKeychainAlways
CryptoKitPrivate/ECToolbox_cc.swift
CryptoKitSecretSharing.ShamirShareGeneratorSerialization
n_4096_logq_27_28_28_logt_4
Fatal error
Negation unexpectedly failed in corecrypto with error code: 
CryptoKitSecretSharing.HybridSecretSharingSharedState
Unsupported Version in Protobuf Deserialized HybridSecretSharingSharedState
recoverSecretFromShamirShares(shares:)
Threshold must be in [
CryptoKitPrivate.AlishaSPAKE2Prover
keyToBeShared
/Library/Caches/com.apple.xbs/0DCA9824-EBA5-4B95-8B83-17A07ADAAF15/TemporaryDirectory.JX3ggf/Sources/CryptoKit/CryptoKitPrivate/Secret Sharing/CKHybridSecretSharing.swift
 in recoverSecret
generateBaseShareofHybridKey(shareIndex:)
Failed in ccss_shamir_share_generator_init with error 
sharedState
share_y
CryptoKitPrivate/OPRF.swift
ccss_shamir_share_generator_serialize failed with error 
n_8192_logq_28_60_60_logt_20
 Serialized key length does not match provided ciphersuite parameters 
M Z 
generateShare(shareIndex:)
init(threshold:supportedPrime:)
CryptoKitPrivate.ATHMClient
sealedBox
ciphertext
n_4096_logq_27_28_28_logt_6
Error with Authentication in opening  GCM sealed box contained in ciphertext in recoverSecret
C D 
Failed in ccss_shamir_share_generator_deserialize with error 
init()
n_8192_logq_40_60_60_logt_26
 Failure creating nonce from serialized data
AESGCMKeyForCKHybridSecretSharing
 in generateShares
Substraction unexpectedly failed in corecrypto with error code: 
authenticatedData
prime
CryptoKitPrivate/Kyber.swift
n_4096_logq_27_28_28_logt_17
n_8192_logq_3x55_logt_24
Unexpectedly failed serializing the scalar.
generateShares(_:)
version
nonce
insecure_n_8_logq_5x18_logt_5
n_8192_logq_3x55_logt_29
 Serialization must contain sharedState 
Share Index must be greater than 0 and <= 
generateShamirShare(shareIndex:)
CredentialPresentation
share_x
 Only support version 1 serializations, this is version 
CryptoKitPrivate/AesPrg.swift
Underlying CryptoKit call had incorrect parameter size in generateShares?
Subtraction unexpectedly failed in corecrypto with error code: 
CryptoKitPrivate.AlishaSPAKE2ProverConfirmed
CryptoKitPrivate.TDMClient
com.apple.cryptokit.rsabssa
/Library/Caches/com.apple.xbs/0DCA9824-EBA5-4B95-8B83-17A07ADAAF15/TemporaryDirectory.JX3ggf/Sources/CryptoKit/CryptoKitPrivate/Secret Sharing/CKRawShamirSecretSharing.swift
CryptoKitPrivate.ARCPresentationWrapper
CryptoKitPrivate.RSAPSSSPKI_Bridging
n_4096_logq_16_33_33_logt_4
unchecked
_TtC16CryptoKitPrivate9ARCServer
_TtC16CryptoKitPrivate18CKPIETFKeyBlinding
_TtCO16CryptoKitPrivate2HE13ObjectStorage
_TtCO16CryptoKitPrivate2HE12ParamContext
_TtC16CryptoKitPrivate10ATHMClient
CKPATKeyBlinding
RSABSSATokenReady
_TtC16CryptoKitPrivate19RSAPSSSPKI_Bridging
_TtC16CryptoKitPrivate18ATHMKeyCommitments
_TtC16CryptoKitPrivate6Scrypt
_TtC16CryptoKitPrivate19TDMServerEvaluation
_TtC16CryptoKitPrivate9TDMServer
_TtCO16CryptoKitPrivate2HE24ObjectStorageWithZeroize
ARCResponse
RSABSSATokenWaitingActivation
TDMEvaluation
_TtC16CryptoKitPrivate27AlishaSPAKE2ProverConfirmed
_TtC16CryptoKitPrivate12SequenceDrbg
ATHMAwaitingActivation
ATHMPresentation
ARCPresentation
ARCTestServer
RSABSSATokenBlinder
TDMToken
TDMTestServer
_TtCV16CryptoKitPrivate11SecureBytes7Backing
_TtC16CryptoKitPrivate20ARCCredentialWrapper
_TtC16CryptoKitPrivate10ATHMServer
_TtC16CryptoKitPrivate18AlishaSPAKE2Prover
_TtC16CryptoKitPrivate9TDMClient
_TtCO16CryptoKitPrivate15CKSecretSharingP33_CE506D4359C10354E8EAAF853DBEE0AA32CKHybridSecretShareInternalState
ARCAwaitingActivation
RSABSSATokenIssuer
_TtCO16CryptoKitPrivate15CKSecretSharing32CKShamirShareSharedInternalState
_TtC16CryptoKitPrivate28ARCAwaitingActivationWrapper
_TtC16CryptoKitPrivate3Rng
ATHMTestServer
ARCCredential
_TtC16CryptoKitPrivate22ARCPresentationWrapper
_TtC16CryptoKitPrivate4Drbg
T@\"NSData\",&,N,V_publicKey
_tokenBlinder
ciphersuite
initWithKeyByteCount:
input
verifyWithKeyCommitmentsData:numBuckets:deploymentID:
_keyId
getRemainingPresentationCountWithPresentationContext:presentationLimit:error:
isValidWithSignature:for:with:context:
tokenBlinder
_nbuckets
numBuckets
sub:corecryptoError:
credential
initFromPublicKeyBytes:inGroup:compressed:corecryptoError:
keyId
T@\"NSData\",R,&,N,V_keyCommitmentsData
blindedMessage
y
ccShamirState
getRemainingPresentationCountWithPresentationContext:presentationLimit:
subdataWithRange:
Kble_intro
T@\"NSString\",R,N,V_deploymentID
_presentation
keyIDFromSPKI:
nbuckets
responseData
oprfServer
verifyTokenWithOutput:TID:FSR:
T@\"NSData\",N,R,VM2
.cxx_destruct
_presentationData
getCredentialDataError:
_nonce
presentationData
share
KEnc
T@\"_TtC16CryptoKitPrivate9ARCServer\",R,N,V_server
blindSign:blindedBy:with:context:error:
drbgInfo
initWithGeneratorForCP:
makeCredentialWithResponseData:error:
precredential
T@\"_TtC16CryptoKitPrivate9TDMServer\",R,N,V_tdmServer
dictionaryWithObjects:forKeys:count:
finalizeWithFSR:evaluatedElement:proof:publicKey:error:
respondWithRequestData:metadata:error:
T@\"NSData\",R,&,N,V_responseData
blindedElement
threshold
multiply:corecryptoError:
activateWithResponseData:error:
_rsaPrivateKey
blindPublicKeyWithPublicKey:with:context:error:
keyCommitmentsData
T@\"NSData\",R,&,N,V_blindedMessage
T@\"_TtC16CryptoKitPrivate9TDMClient\",R,N,V_tdmClient
serializeWithKeyBytes:error:
initWithLength:
SymmetricLTS
initWithCredentialResponseData:precredential:error:
nonce
verifyFullyParsedASN1:end:error:
T@\"_TtC16CryptoKitPrivate10ATHMClient\",R,N,V_client
finalizeWithEvaluatedElement:proof:publicKey:fsr:error:
finalizeWithResponseData:nbuckets:error:
getNonce
groupOrderByteCountForCP:
initWithRequestContext:serverPublicKey:error:
params
sequenceState
associatedData
x963Representation
T@\"NSData\",N,R,VKMac
inverseModOrder
_ciphersuite
oprfClient
readMetadataWithPresentationData:nbuckets:error:
T@\"NSData\",R,&,N,V_signature
_proof
tdmServer
M2
T@\"NSData\",N,R,VSymmetricLTS
_ciphersuiteModulusByteCount
includeAccessStructureInShare
length
presentWithPresentationContext:presentationLimit:error:
setParamsForSize:params:error:
spakeCtxData
getKeyIDWithKeyCommitmentsData:
_tdmServer
_client
x
cSuiteParams
dataUsingEncoding:
getCredentialDataAndReturnError:
X
initWithCredential:presentationContext:presentationLimit:error:
blind
highEntropySecrets
client
initWithParams:share:
dataWithLength:
TQ,R,N,V_nonce
T@\"NSData\",N,R,VKRMac
T@\"_TtC16CryptoKitPrivate10ATHMServer\",R,N,V_server
respondWithRequestData:error:
T@\"NSData\",N,R,ValishaKey
T@\"_TtC16CryptoKitPrivate22ARCPresentationWrapper\",R,&,N,V_presentation
_requestData
blindSign:error:
errorWithDomain:code:userInfo:
info
initWithClient:responseData:nbuckets:error:
unblindPublicKey:with:context:error:
verifyAndGetKeyIDFromKeyCommitmentsData:numBuckets:deploymentID:
_keyCommitmentsData
encryptionParams
includeADInShares
ccXOFCtx
mutableBytes
boolValue
cipherSuite
init
isEqual:
requestData
T@\"NSData\",R,&,N,V_presentationData
z1_self
T@\"NSData\",N,R,VKble_intro
initWithResponseData:
custom
drbgCtx
_tokenContent
alishaKey
initWithPublicKey:error:
_signature
getPresentationData
getX
initWithPresentationData:nonce:error:
KRMac
TQ,R,N,V_nbuckets
_credential
_precredential
initWithKeyCommitmentsData:nbuckets:deploymentID:error:
_deploymentID
mapToCurve_SSWU_RandomOracle
respondWithRequestData:metadata:nbuckets:error:
request
T@\"NSData\",N,R
be
initWithData:error:
initWithx963Representation:group:
secret
aad
_responseData
deploymentID
publicKeyBytes
T@\"NSData\",R,&,N,V_blindingInverse
blindSignMessage:blindedBy:withKey:context:error:
compressedx962PointByteCountForCurveParameters:
isValidSignature:forMessage:signedBy:context:
signature
tokenWaitingActivationWithContent:error:
_blindingInverse
initWithNumBuckets:deploymentID:
tokenContent
evaluate:error:
randomBytesPtr
T@\"NSData\",R,&,N,V_proof
activateTokenWithServerResponse:error:
exportKeyCommitmentsAndReturnError:
initWithRequestContext:serverPublicKeyData:error:
Kble_oob_master
z0_self
serializedBigEndianScalar
validateOutput:TID:
_publicKey
evaluateWithBlindedElement:error:
proof
blindingInverse
_server
T@\"NSData\",R,&,N,V_evaluatedElement
compressedRepresentationFromSecKey:
dealloc
T@\"_TtC16CryptoKitPrivate28ARCAwaitingActivationWrapper\",R,N,V_precredential
serializedPublicKey:
state
tdmClient
initWithCredentialData:error:
makeRequest
deriveKeyWithPassword:salt:outputSize:cost:blockSize:parallelization:
initWithBytes:length:
numberWithInteger:
presentation
prime
publicKey
T@\"RSABSSATokenBlinder\",R,&,N,V_tokenBlinder
KMac
T@\"NSData\",R,&,N,V_keyId
blindPublicKey:withPrivateKey:context:error:
initWithData:inGroup:reduction:corecryptoError:
initWithTID:
respondsToSelector:
server
T@\"NSData\",R,&,N,V_requestData
T@\"_TtC16CryptoKitPrivate20ARCCredentialWrapper\",R,&,N,V_credential
initWithRandomScalarInGroup:
privateScalarFromSecKey:
unblindPublicKey:withPrivateKey:context:error:
_blindedMessage
processResponseWithY:M1:
initWithKeyCommitmentsData:numBuckets:deploymentID:error:
initWithPassword:salt:authenticatedData:keyDerivationCost:
tempShare
add:corecryptoError:
getServerPublicKey
initWithBlindingInverse:blindedMessage:tokenContent:tokenBlinder:ciphersuite:
initWithParams:x:y:
paramContext
T@\"NSData\",N,R,VKble_oob_master
T@\"NSData\",R,&,N,V_tokenContent
_evaluatedElement
backingStruct
readMetadataWithPresentationData:nbuckets:
initWithEvaluatedElement:proof:
makePresentationWithPresentationContext:presentationLimit:error:
FSR
T@\"NSData\",N,R,VKEnc
evaluatedElement
secKeyFromCompressedRepresentation:
_tdmClient
verifyWithPresentationData:nonce:requestContext:presentationContext:presentationLimit:
bytes
setPublicKey:
initWithNumBuckets:deploymentID:error:
initWithTokenContent:tokenSignature:keyId:
statePointer
q40@0:8@16Q24^@32
@\"_TtC16CryptoKitPrivate22ARCPresentationWrapper\"
@56@0:8@16^{__SecKey=}24^{__SecKey=}32@40^@48
@48@0:8@16q24@32^@40
@48@0:8@16Q24@32^@40
^{__SecKey=}48@0:8^{__SecKey=}16^{__SecKey=}24@32^@40
B48@0:8@16@24^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32@40
@16@0:8
@32@0:8@16@24
@\"NSData\"
Q16@0:8
B40@0:8r*16r*24^@32
[385{ccrsa_pub_ctx=\"pb_n\"Q\"pb_bitlen\"Q\"pb_funcs\"^{cczp_funcs}\"pb_ccn\"[1Q]}]
^{__SecKey=}24@0:8@16
q16@0:8
@32@0:8q16@24
v16@0:8
@48@0:8@16q24q32^@40
r^{ccrsabssa_ciphersuite=}
@40@0:8@16@24@32
B48@0:8@16@24^{__SecKey=}32@40
@\"_TtC16CryptoKitPrivate9TDMClient\"
@24@0:8^@16
q32@0:8@16q24
@\"NSString\"
B40@0:8Q16@24^@32
B56@0:8@16q24@32@40q48
@56@0:8@16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}32@40^@48
@40@0:8@16Q24@32
@40@0:8Q16@24^@32
@\"RSABSSATokenBlinder\"
@\"_TtC16CryptoKitPrivate9TDMServer\"
@40@0:8@16q24^@32
^{ccrsa_pub_ctx=QQ^{cczp_funcs}[1Q]}16@0:8
@56@0:8@16@24@32@40r^{ccrsabssa_ciphersuite=}48
@48@0:8@16@24Q32^@40
@40@0:8@16@24^@32
B40@0:8@16@24@32
Q
[125{ccrsa_full_ctx=\"pb_n\"Q\"pb_bitlen\"Q\"pb_funcs\"^{cczp_funcs}\"pb_ccn\"[1Q]}]
?
@24@0:8Q16
@32@0:8@16^@24
B40@0:8@16q24@32
@56@0:8@16@24q32Q40I48I52
@48@0:8@16@24@32Q40
@\"_TtC16CryptoKitPrivate10ATHMClient\"
@\"_TtC16CryptoKitPrivate9ARCServer\"
v24@0:8@16
@24@0:8^{__SecKey=}16
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}48@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@32^@40
@\"_TtC16CryptoKitPrivate10ATHMServer\"
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}24@0:8@16
@24@0:8@16
@56@0:8@16@24@32@40^@48
@40@0:8@16Q24^@32
@\"_TtC16CryptoKitPrivate28ARCAwaitingActivationWrapper\"
@\"_TtC16CryptoKitPrivate20ARCCredentialWrapper\"
B56@0:8@16Q24@32@40Q48
B32@0:8@16@24
@24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16
```
