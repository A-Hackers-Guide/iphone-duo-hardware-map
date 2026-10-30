# `/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`

From the upgrade restore ramdisk (141-29011-104.dmg). 948,160 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 32 (Size: 5312)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe, NlistOutofsyncWithDyldinfo
```

## Linked libraries (15)

- `/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/usr/lib/libheimdal-asn1.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/swift/libswiftCore.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/swift/libswiftCoreFoundation.dylib (compatibility version 1.0.0, current version 120.100.0)`
- `/usr/lib/swift/libswiftDispatch.dylib (compatibility version 1.0.0, current version 1605.40.4, weak)`
- `/usr/lib/swift/libswiftObjectiveC.dylib (compatibility version 1.0.0, current version 973.1.0)`
- `/usr/lib/swift/libswiftXPC.dylib (compatibility version 1.0.0, current version 167.0.2, weak)`
- `/usr/lib/swift/libswift_Builtin_float.dylib (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/usr/lib/swift/libswiftos.dylib (compatibility version 1.0.0, current version 1090.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (34 classes, 6 protocols)

Classes: `MSAlgorithmIdentifier`, `MSCMSAppleExpirationTimeAttribute`, `MSCMSAppleHashAgilityAttribute`, `MSCMSAppleHashAgilityV2Attribute`, `MSCMSAppleTimestampAttribute`, `MSCMSAttribute`, `MSCMSAuthEnvelopedData`, `MSCMSCompressedData`, `MSCMSContentInfo`, `MSCMSContentTypeAttribute`, `MSCMSCounterSignerInfo`, `MSCMSCountersignatureAttribute`, `MSCMSEncryptionKeyPreferenceAttribute`, `MSCMSEnvelopedData`, `MSCMSEnvelopedDataInternal`, `MSCMSIdentifier`, `MSCMSMessageDigestAttribute`, `MSCMSMultipleSignaturesAttribute`, `MSCMSMutableAttributeArray`, `MSCMSRecipientInfo`, `MSCMSSMIMECapabilitiesAttribute`, `MSCMSSignedData`, `MSCMSSignerInfo`, `MSCMSSigningTimeAttribute`, `MSCMSTimestampAttribute`, `MSCMSTimestampAttributeInternal`, `MSDecodeOptions`, `MSError`, `MSMessageImprint`, `MSOID`, `MSPKIStatusInfo`, `MSTimestampRequest`, `MSTimestampResponse`, `NSData`

Protocols: `MSCMSAttributeCoder`, `MSCMSMessage`, `MessageSecurityMessage`, `NSCoding`, `NSObject`, `NSSecureCoding`

## Strings (1,668)

```
Failed to build MessageImprint for TimeStampReq: %@
MSTimestampResponse: Cannot initialize with nil timestamp response data
found %lu candidate certs from keychain with matching email addresses
Invalid data - AES-GCM algorithm identifier carries no parameters
Invalid data - aes-ICVlen is negative or too large
BundledSN = %{mask.hash}@
QuerySKID = %{mask.hash}@
Bad signature algorithm %@. Trying to compose signature algorithm from %@ and digest %@
No recipient found
MSCMSRecipientInfo requires an originator identity for an EC recipient. Encode will fail if not set.
unable to parse certificate at %u
BundledIssuer = %{mask.hash}@
Invalid data - no recipients found
Error decrypting encoded content
MSCMSRecipientInfo init encryption algorithm %@ not permitted for certificate key type %ld
MSTimestampRequest: Failed to unarchive response: %@
Failed to parse hash algorithm OID: %@
Found unimplemented contented type: EncryptedData
BundledSKID = %{mask.hash}@
Invalid data - no certificate in originatorCertificates
Digest length %lu is not a supported length
Found unsupported content type: AuthenticatedData
QueryIssuer = %{mask.hash}@
failed to decode recipient %u: %@
Invalid data - Error encoding GCM parameters
Failed to encode TimeStampToken: %@
TimeStampToken has no signers
skipping non-certificate CertificateChoice at %u
%{public}@
Unable to generate nonce underlying crypto error %d
Failed to encode TimeStampReq: %@
Failed to archive MSTimestampRequest: %@
failed to add recipient. No shared encryption algorithm with the rest of the recipients
failed to set credential reference on signer public key: %@
Invalid data - error encoding AuthEnvelopedData
Error encrypting underlying crypto error %d
Error decrypting underlying crypto error %d
MSTimestampResponse initWithTimestampToken: Cannot initialize with nil token data
Found unsupported content type: DigestedData
found %lu valid email candidate certs
Invalid encryption algorithm %u
Invalid data - error decoding AuthEnvelopedData
Invalid data - error decoding OriginatorInfo
Invalid AES-GCM tag length %ld, RFC 5084 requires 12 to 16 octets
MSCMSRecipientInfo %s: Unsupported certificate key type
recipientInfo violates RFC 5652 (key usage)
No certificates in SignedData
MSCMSAppleTimestampAttribute: failed to create MSTimestampResponse from token data
no countersignatures, returning successful verification
Invalid input algorithm %u
MSTimestampRequest: Retryable error (attempt %ld/%ld): %@
MSTimestampResponse initWithTimestampToken: failed to parse token: %@
MSCMSChainMode with chain specified, but no trusted chain found (%@), continuing with untrusted chain
Found unknown content type: %@
QuerySN = %{mask.hash}@
Invalid data - originatorInfo has no certificates
MSTimestampRequest: Queue is required
MSCMSChainMode with chain specified, but could not build chain beyond leaf, continuing with single certificate
no timestamps, returning successful verification
Invalid data - error decoding GCMParameters
aes-ICVlen %ld does not match mac length %ld
Error: SignedData contentType is %@ (expected %@)
found %lu candidate email certs from keychain
failed to set credential reference on signer private key: %@
No certificate with id-kp-timeStamping EKU found in certificate chain
signedData contains embedded content but signer %lu does not have signed attributes.
Invalid input data/embedded data
Invalid AES-GCM nonce length %ld, expected 12 to 16 octets
Unable to generate key underlying crypto error %d
MSTimestampResponse: Failed to parse timestamp response: %@
Failed to parse TSA policy OID: %@
%s failed with %@
logging %s 0x%zx [%ld-%ld)/%ld %s
MSCMSSignerInfo init signature aglorithm %@ not permitted for certificate key type %ld
MSTimestampRequest: Completion block is required
TimeStampToken has multiple signers (%lu), RFC 3161 requires exactly one
%s %s isInternal: %d val: %s isForced: %d appVal: %s result: %d
Error extracting MAC
MSCMSSigningTimeAttribute
MSCMSMultipleSignaturesAttribute
MSCMSEncryptionKeyPreferenceAttribute
MSCMSAppleHashAgilityAttribute
MSCMSAppleHashAgilityV2Attribute
MSError
MSCMSContentInfo
MSCMSAuthEnvelopedData
MSCMSAppleTimestampAttribute
MSCMSCountersignatureAttribute
MSCMSCompressedData
MSCMSMessage
MSCMSMutableAttributeArray
MSCMSCounterSignerInfo
MessageSecurityMessage
NSCoding
MSPKIStatusInfo
MSCMSTimestampAttribute
MSCMSEnvelopedData
MSMessageImprint
MSCMSIdentifier
MSCMSSignerInfo
MSCMSEnvelopedDataInternal
MSCMSTimestampAttributeInternal
MSCMSRecipientInfo
MSTimestampRequest
NSSecureCoding
MSTimestampResponse
MSDecodeOptions
MSCMSSMIMECapabilitiesAttribute
MSCMSAppleExpirationTimeAttribute
MSAlgorithmIdentifier
MSCMSContentTypeAttribute
MSCMSMessageDigestAttribute
MessageSecurityHexRepresentation
NSObject
MSCMSAttributeCoder
MSOID
MSCMSSignedData
MSCMSAttribute
isEqualToData:
keyEncryptionAlgorithm
setCertificates:
T@\"MSOID\",N,&,VattributeType
array
reqPolicyID
setTimeStampTokenData:
setXpcQueue:
timestampAttribute
_bodyHashAlgorithm
initWithSignerInfo:additionalCertificates:
objectAtIndex:
setSignerCertificate:
setSignerPrivKey:
sign:
T#,R
containsObject:
T@\"MSTimestampResponse\",R
_OIDString
_xpcSession
date
initSignatureOIDWithSecKeyAlgorithm:error:
isEqualToTimestampResponse:error:
release
attributeType
initWithIdentity:signatureAlgorithm:useIssuerAndSerialNumber:error:
setGenericAttributes:
signerPolicies
signingCertificate
T@\"MSAlgorithmIdentifier\",&,V_keyEncryptionAlgorithm
T@\"NSArray\",R,V_certificates
T@\"NSData\",&,V_messageDigest
T@\"NSDate\",R,&,V_signingTime
_recipientCertificates
addDigestAlgorithmFromSigner:
appendBytes:length:
containingSignedData
algorithmIdentifier
init:hashedMessage:
initWithEmbeddedContent:signer:signerChainMode:error:
localizedDescription
supportsSecureCoding
embeddedContent
setDataContent:
T@\"NSData\",R,V_OIDBytes
initWithIdentity:recipientsAlgorithmCapabilities:error:
length
timeIntervalSinceDate:
verifyTimestamp:error:
T@\"MSOID\",R,&,V_attributeType
contentTypeAttributeWithOID:
invertedSet
parseTSTInfo:error:
removeSignersWithCertificate:error:
setNonce:
setVerifySigners:
xpcQueue
T@\"NSArray\",R
T@\"NSData\",&,N,V_signature
T@\"NSData\",&,V_timeStampTokenData
_userKeyingMaterial
decodeIdentifier:error:
keyEncryptionKey:forEncryption:secCMSCompatibility:
setLAContext:
sleepForTimeInterval:
TB,V_verifySignatures
createXPCMessageForTimestampFetch
setSignedAttrsHashAlgorithm:
verifyWithMessageImprint:policies:error:
_subjectKeyId
_type
createTrustObjectWithPolicies:error:
initWithString:error:
T@\"NSArray\",&,V_signers
RSASignatureOIDWithDigestAlgorithm:error:
TB,V_certReq
TB,V_verifySigners
_encryptedContent
_version
createAttributeArrayFromAttributeSetRaw:error:
createTrustObjectWithPolicies:verifyTime:anchorCertificates:error:
T@\"MSAlgorithmIdentifier\",&,N,V_signatureAlgorithm
T^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}},V_encodedSignerInfo
decodeKeyTransRecipientInfo:certificates:LAContext:error:
encodeKeyTransRecipientInfo:recipientInfo:error:
failInfo
originatorPubKey
_verifySignatures
algorithm
timeStampToken
verifySignatures:
tsa
_signerInfo
asn1AlgId
bytes
integerValue
parseTSAFromGeneralName:
setOptions:
T@\"NSData\",&,V_skidData
T@\"NSDate\",&,V_fetchStartTime
TB,R
createSharedInfo:
encodedAttributeSet
hasFailInfo
hashedMessage
init:server:nonce:
arrayWithArray:
certReq
envelopedData
numberWithInteger:
setEncryptionAlgorithm:
_xpcQueue
addCertificatesForSigner:mode:error:
Asn1OID
_attributeValues
_digestAlgorithm
_serialNumber
addSigner:withCertificates:
autorelease
code
encode
TB,R,V_hasFailInfo
_reqPolicyID
ccAlgorithm:
compare:
decimalDigitCharacterSet
encodeKeyAgreeRecipientInfo:recipientInfo:error:
initWithCertificate:recipientsAlgorithmCapabilities:error:
initWithDecryptionKey:
T^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}},V_issuerAndSerialNumber
_additionalCertificates
encodeObject:forKey:
ensureXPCSessionExists:
initWithDictionary:
replaceObjectAtIndex:withObject:
stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:
T@\"MSOID\",R,V_type
getCharacters:range:
initWithCertificate:signatureAlgorithm:useIssuerAndSerialNumber:error:
initWithMessageImprint:
initWithUTF8String:
isEqualToDate:
numberWithInt:
setChainMode:
T@\"MSOID\",N,&,VencryptionAlgorithm
setTsaPolicyID:
getAttributesWithType:
initWithStatus:statusString:failInfo:hasFailInfo:
setEmbeddedContent:
setOriginatorCertificates:
unsignedAttrsData
validateTimestampRequestData:
T@\"MSAlgorithmIdentifier\",&,V_digestAlgorithm
dealloc
T^{__CFString=},R
_issuerAndSerialNumber
encodeRecipientInfo:recipientInfo:error:
initWithTimeIntervalSince1970:
messageDigestAttributeWithDigest:
zone
MSErrorWithDomain:code:errorLevel:underlyingError:description:
_encodedAttributeSet
bulkEncryptDecrypt:algorithm:mode:key:iv:error:
removeAttributes:
signature
calculateSignatureDigestWithAlgorithm:error:
setIdentifierData:
removeSignersWithIndexes:error:
T@\"NSData\",&,V_serialNumber
T@\"NSData\",&,V_timestampResponse
T@\"NSMutableArray\",&,V_genericAttributes
TB,V_certChainRequested
T^{__SecIdentity=},V_identity
T@\"NSSet\",R,V_capabilities
_legacyASN1Encoding
_options
_signatureCalculated
originatorIdentity
setIssuerNameData:
T@\"MSAlgorithmIdentifier\",&,V_signatureAlgorithm
_genericAttributes
initWithDataContent:isDetached:signer:signerChainMode:error:
setTimeStampToken:
verifyTime
LAContext
T@\"MSOID\",N,&,Vtype
_Asn1OID
_signers
encodeBool:forKey:
encryptDecryptContent:ccOperation:error:
isKindOfClass:
keySize:
T@\"NSData\",&,V_key
_signerCertificate
initWithServerURL:chainRequested:
setAttributeDERData:
setEncryptedContent:
setIssuerAndSerialNumber:
setTimestamp:
setUnprotectedAttributes:
OIDBytes
signers
_serialNumberData
bodyHashAlgorithm
domain
initECSignatureOIDWithDigestAlgorithm:error:
setMessageImprint:
secKeyAlgorithm
getAttributesWithType:protectedAttributes:
recipients
setXpcSession:
verifyCountersignaturesAndCountersignersWithPolicies:verifyTime:anchorCertificates:signature:error:
setReqPolicyID:
T@\"MSCMSSignerInfo\",R,V_signerInfo
_identity
_tsaPolicyID
digestOIDWithSignatureAlgorithm:error:
encodeWithCoder:
finishAsyncFetch:error:onQueue:completion:
verifyTimestamps:error:
T@\"MSOID\",N,&,VcontentType
UTF8String
_signatureAlgorithm
_timestamp
recipientCertificate
cString
T@\"NSArray\",&,V_signerPolicies
Tr^{ccdigest_info=QQQQ*^v^?^?i^?},R
_unprotectedAttributes
_verifyTime
anchorCertificates
initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:
initWithDomain:code:userInfo:
dataWithLength:
Tq,V_firstRetryErrorCode
_chainMode
copyAttributeData:
parseFailureInfo:
removeRecipientWithEmailAddress:error:
retryCount
setAnchorCertificates:
_signerPolicies
T@\"NSData\",&,N,V_rawTimestampTokenData
T@\"NSData\",&,V_LAContext
T@\"NSDictionary\",R,&,V_hashAgilityValues
_algorithmIdentifier
initWithAttribute:LAContext:error:
setAlgorithmIdentifier:
Tq,R,V_status
_content
_skidData
addObjectsFromArray:
initWithHashAgilityValue:
setDateFormat:
setDigestAlgorithms:
setRecipientCertificates:
T@\"NSData\",&,V_serialNumberData
_hashAgilityValue
errorWithDomain:code:userInfo:
setContent:
timestampRequest
T@\"NSURL\",&,V_serverURL
calculateContentDigestWithAlgorithm:error:
dictionary
initWithBytes:length:encoding:
initWithEnvelopedData:
intValue
setSignedAttrsHash:
tsaPolicyID
_parameters
fetchTimestampWithError:
_fetchStartTime
T@\"MSCMSSignedData\",&,V_timeStampToken
T@\"NSData\",&,V_unsignedAttrsData
T@\"NSObject<OS_dispatch_queue>\",&,V_xpcQueue
_digestAlgorithms
decodeObjectOfClass:forKey:
encryptionCertificate
initWithAttributeStruct:error:
T^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}},V_encodedAttribute
_keyEncryptionAlgorithm
buildTimestampRequest
initWithEmailAddress:
initWithEmbeddedContent:recipient:encryptionAlgorithm:
setStatus:
setUseIssuerAndSerialNumber:
stringByAppendingFormat:
hash
identity
subjectKeyId
useIssuerAndSerialNumber
_useIssuerAndSerialNumber
algorithmCapabilities
certificateHasTimeStampingEKU:
checkSignedPerRFC5652:
createRequiredAttributes:
decodeMessageSecurityObject:options:error:
removeObjectsAtIndexes:
stringWithString:
_timeStampToken
T@\"NSArray\",R,&,V_attributeValues
T@\"NSData\",N,C
T@\"NSNumber\",R,V_version
_algorithmCapabilities
addIndex:
getRecipients
key:
timestampServer
.cxx_destruct
_identifierData
_signerPrivKey
decode:error:
description
initCertsOnlyWithCertificates:error:
recipientCertificates
setKey:
attributeDERData
encryptionAlgorithm
init:
initWithCertificate:legacyKeyWrapAlgorithm:
verifyWithRequest:policies:error:
MSErrorWithDomain:code:errorLevel:underlyingError:description:arguments:
Tq,V_retryCount
TB,V_legacyASN1Encoding
_verifySigners
removeSignerCertificatesWithIndexes:
setAttributeType:
setLocale:
setObject:forKeyedSubscript:
T@\"MSOID\",&,V_reqPolicyID
T@\"NSString\",&,V_tsa
initWithFormat:
_originatorPubKey
componentsSeparatedByString:
removeObject:
statusString
userInfo
_messageImprint
T@\"MSOID\",R,&
URLWithString:
_algorithm
_certChainRequested
_timestampRequest
generateEncryptionKey:
initWithAttribute:error:
_encodedSignerInfo
_encryptionAlgorithm
appendFormat:
decodeIntegerForKey:
initWithBytes:length:
initWithDataContent:
retain
setEncodedAttribute:
_timestampResponse
blockSize:
initWithIssuerName:serialNumber:
initWithSignerInfo:signerChainMode:
retainCount
localeWithLocaleIdentifier:
serverURL
signedAttrsHash
_embeddedContent
_signedAttrsData
dataWithBytes:length:
encodeImplicitAttributesWithError:
initWithDataContent:recipient:encryptionAlgorithm:
messageDigest
setServerURL:
HybridSignatureOIDWithDigestAlgorithm:error:
T@\"NSData\",&,V_encryptionKey
initWithEmbeddedContent:error:
verifyContentTypeAttribute:
xpcSession
_serverURL
cleanupMessageImprint:
initWithEmbeddedContent:
retryDelayForAttempt:
timestamp
setTsa:
T@\"NSArray\",R,V_signers
TB,V_contentChanged
_messageDigest
getAttributesWithOID:
rangeOfCharacterFromSet:
setTimeZone:
T@\"NSData\",&,V_signedAttrsData
T^{__SecIdentity=},N,V_originatorIdentity
_dataContent
conformsToProtocol:
contentChanged
decryptContent:error:
initWithDataContent:error:
setMaxRetryAttempts:
addCounterSignerCertificates:mode:error:
addSigner:withChainMode:error:
ccdigest
setContainingSignerInfo:
setProtectedAttributes:
setRawTimestampTokenData:
signatureAlgorithmOIDWithSecKeyAlgorithm:error:
verifySignatures
T@\"MSAlgorithmIdentifier\",&,V_algorithmIdentifier
T@\"NSArray\",&,V_recipientCertificates
T^{__SecCertificate=},N,V_originator
initWithEmail:algorithmCapabilities:
objectForKeyedSubscript:
setEncodedSignerInfo:
verifySignaturesAndSignersWithPolicies:verifyTime:error:
verifyWithRequest:error:
T@\"NSData\",&,V_nonce
T@\"NSData\",&,V_userKeyingMaterial
_hashedMessage
initWithEmail:LAContext:error:
nonce
numberWithUnsignedInt:
reset
signerCertificate
encryptBulkKey:
_recipientCertificate
addMultipleSignaturesAttribute
arrayWithCapacity:
firstRetryErrorCode
getSignerCertificate:error:
initWithCertificate:error:
originator
T@\"NSData\",&,V_timestampRequest
TB,V_detached
dataUsingEncoding:
encodeAttributeWithError:
encodeInteger:forKey:
initRSASignatureOIDWithDigestAlgorithm:error:
initWithOID:
mutableCopy
algorithmIdentifierWithOID:
dictionaryWithObjects:forKeys:count:
digestAlgorithmWithSignatureAlgorithm:error:
initWithAttribute:certificates:LAContext:containingSignerInfo:error:
initWithIssuerName:serialNumber:negativeNumber:
parseTimeStampToken:error:
T@\"NSData\",&,V_hashedMessage
T@\"NSData\",R,&,V_hashAgilityValue
T^{__SecCertificate=},N,V_recipientCertificate
_maxRetryAttempts
maxRetryAttempts
objectForKey:
parseMSTimestampResponseFromReply:error:
performAsyncFetchAttempt:maxAttempts:onQueue:completion:
T@\"NSArray\",&,V_encryptedKeys
T@\"NSData\",&,V_content
_protectedAttributes
enumerateObjectsAtIndexes:options:usingBlock:
initWithTimestampToken:error:
signerPrivKey
timeStampTokenData
encodedSignerInfo
Ti,V_type
countByEnumeratingWithState:objects:count:
init:server:
invalidateXPCSession
setSigners:
encodedAttribute
indexesOfObjectsPassingTest:
initWithDataContent:isDetached:signer:error:
setFetchStartTime:
setSignedAttrsData:
setType:
verifySignaturesAndSignersWithPolicies:verifyTime:anchorCertificates:error:
Tq,R,V_failInfo
T@\"NSString\",R,V_OIDString
asMessageSecurityHexString
copy
setAdditionalCertificates:
options
T@\"NSDate\",&,V_timestamp
addSMIMECapabilitiesAttribute:
checkDecryptionResult:
encryptionKey
initWithIdentity:
setSignature:
addRecipient:
initWithDataContent:isDetached:signer:additionalCertificates:error:
initWithEncryptionAlgorithm:
messageImprint
setContainingSignedData:
setTimestampServer:
unarchivedObjectOfClass:fromData:error:
verifyTimestamps:
OIDWithString:error:
T@\"MSPKIStatusInfo\",&,V_status
setRecipientCertificate:
superclass
T@\"NSString\",R,V_statusString
addProtectedAttribute:
firstObject
isMemberOfClass:
setUserKeyingMaterial:
verifySignature:
T@\"MSMessageImprint\",&,V_messageImprint
_encodedAttribute
encodeAttributesWithError:
freeRecipientInfo:
indexOfObjectPassingTest:
initWithEmbeddedContent:signer:additionalCertificates:error:
setEncodedAttributeSet:
signedAttrsHashAlgorithm
_cachedTimestampResponse
algorithmIdentifierWithAsn1AlgId:error:
arrayWithObjects:count:
componentsJoinedByString:
count
hashAgilityValues
removeLastObject
removeSignersWithIdentity:error:
T@\"NSArray\",&,V_recipients
T@\"NSDate\",R,&,V_expirationTime
Tq,V_version
_containingSignedData
data
initWithSigningTime:
removeRecipientWithCertificate:error:
setEncryptedKeys:
T@\"MSCMSMutableAttributeArray\",&,V_unprotectedAttributes
_encryptedKeys
_signedAttrsHash
buildMessageImprintForASN1:error:
enumerateObjectsUsingBlock:
setOriginator:
setSignatureAlgorithm:
userKeyingMaterial
isProxy
T@\"<MSCMSMessage>\",&,V_embeddedContent
T@\"MSAlgorithmIdentifier\",&,V_encryptionAlgorithm
T@\"NSString\",R,C
_LAContext
_signature
issuerAndSerialNumber
objectAtIndexedSubscript:
T@\"NSData\",&,V_identifierData
decodeBoolForKey:
initWithDecryptionIdentity:
setOriginatorIdentity:
setTimestampResponse:
skidData
verifyCountersignatures:
T@\"MSCMSMutableAttributeArray\",&,V_protectedAttributes
content
verifyWithMessageImprint:error:
_contentType
appendData:
isImplementedInObjectiveC
T@\"NSMutableArray\",&,V_attributes
T@\"NSMutableArray\",&,V_originatorCertificates
class
indexSet
initWithAttribute:certificates:LAContext:error:
setDigestAlgorithm:
timeZoneWithName:
stringFromDate:
TB,V_useIssuerAndSerialNumber
setSubjectKeyId:
T@\"NSArray\",&,V_additionalCertificates
Tq,V_maxRetryAttempts
_hashAgilityValues
setCertChainRequested:
T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_signerPrivKey
_hasFailInfo
_signedAttrsHashAlgorithm
dateWithTimeIntervalSince1970:
initWithEmail:keyEncryptionAlgorithm:
setWithSet:
setContentType:
_expirationTime
_anchorCertificates
_asn1AlgId
allObjects
attributes
dataWithData:
generateAttributeStruct
T@\"NSObject<OS_xpc_session>\",&,V_xpcSession
_originatorCertificates
detached
initDigestOIDWithSignatureAlgorithm:error:
initWithEmail:signatureAlgorithm:LAContext:error:
performSingleSyncFetchAttempt:
serialNumberData
timestampResponse
T@\"NSArray\",&,V_anchorCertificates
setDateStyle:
setWithArray:
timeZoneForSecondsFromGMT:
timestampTime
verifySigners
_rawTimestampTokenData
initWithSignerInfo:
setFirstRetryErrorCode:
setWithCapacity:
stringWithUTF8String:
verifyCountersignaturesAndCountersignersWithPolicies:verifyTime:anchorCertificates:error:
verifySignatureAndSignerWithPolicies:verifyTime:anchorCertificates:error:
_OIDBytes
dateWithTimeIntervalSinceReferenceDate:
initWithAsn1AlgId:error:
initWithEmail:
initWithSkid:
attributeValues
T@\"NSData\",&,V_attributeDERData
T@\"MSOID\",&,V_tsaPolicyID
T@\"NSData\",&,N
setEncryptionKey:
setSkidData:
setVersion:
T@\"NSData\",&,N,V_dataContent
T@\"NSNumber\",&,V_version
TQ,R
T^{__SecCertificate=},V_signerCertificate
T@\"NSDate\",R
_attributeDERData
_timestampResponseParsed
unprotectedAttributes
tstinfo
dictionaryWithCapacity:
isEqualToMessageImprint:error:
setHashedMessage:
setIdentity:
setSerialNumberData:
signatureAlgorithm
unsignedIntValue
OIDWithAsn1OID:error:
addSMIMEEncryptionKeyPreferenceAttribute:
init
initWithAttributeType:values:
performSelector:withObject:
performSelector:withObject:withObject:
setDetached:
OIDString
OIDWithData:error:
_certReq
archivedDataWithRootObject:requiringSecureCoding:error:
initHybridSignatureOIDWithDigestAlgorithm:error:
setAsn1OidFromOIDString:error:
ECSignatureOIDWithDigestAlgorithm:error:
T@\"NSData\",&,V_issuerNameData
initWithCapabilities:
initWithServerURL:
_contentChanged
initWithLength:
T@\"NSArray\",N,C
T@\"<MSCMSMessage>\",N,&,VembeddedContent
T@\"MSCMSSignedData\",W,V_containingSignedData
certChainRequested
decodeKeyAgreeRecipientInfo:certificates:LAContext:error:
setContentTypeWithType:
_status
addCounterSignerAttribute:
sendTimestampFetchAnalyticsEvent:success:error:samplingRate:
signedData
timestampToken
type
digestAlgorithm
T@\"MSCMSSignerInfo\",W,N,V_containingSignerInfo
TB,V_verifyTimestamps
_retryCount
_tsa
addObject:
characterSetWithCharactersInString:
debugDescription
T@\"NSString\",?,R,C
T@\"NSURL\",&,V_timestampServer
fetchStartTime
fetchTimestampWithCompletionBlock:queue:
hashAgilityValue
initWithAsn1OID:error:
initWithFormat:arguments:
initWithOID:parameters:
boolValue
createSecCMSSharedInfo:
encodeSignerInfo:error:
initWithSignerInfo:signerChainMode:additionalCertificates:
isEqualToString:
performSelector:
stringWithFormat:
T@\"MSOID\",&,V_contentType
_nonce
setMessageDigest:
setSignerPolicies:
verifyMessageDigestAttribute:error:
T@\"NSSet\",&,V_digestAlgorithms
initWithCertificate:algorithmCapabilities:originator:
initWithCoder:
issuerNameData
setTimestampAttribute:
set
T@\"NSArray\",&,V_certificates
_detached
calculateSignedAttributesDigest:
calculateSignerInfoDigest:
freeKeyTransRecipientInfo:
initWithDER:
originatorCertificates
dictionaryWithObject:forKey:
initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:
parameters
removeSignersWithEmailAddress:error:
setAttributes:
setBodyHashAlgorithm:
setOriginatorPubKey:
ccMode:
initWithDigest:
_attributeType
additionalCertificates
findBestEncryptionAlgorithmForNewRecipient:
setLength:
T@\"NSData\",R,V_parameters
_unsignedAttrsData
appendString:
decodeSignerInfo:certificates:LAContext:error:
genericAttributes
initWithEmail:recipientsAlgorithmCapabilities:LAContext:error:
isEqualToTimestampRequest:error:
setCertReq:
T@\"MSCMSTimestampAttributeInternal\",&,V_timestampAttribute
T@\"NSMutableArray\",&,V_unprotectedAttributes
dictionaryWithDictionary:
serialNumber
signerInfo
T@\"NSData\",&,V_encodedAttributeSet
_encryptionKey
_key
containingSignerInfo
contentType
initWithData:error:
initWithExpirationTime:
setSerialNumber:
TB,R,V_signatureCalculated
_certificates
_signingTime
setVerifyTimestamps:
status
verifyTimestamps
T@\"NSDate\",&,V_verifyTime
T^{__SecCertificate=},R,V_encryptionCertificate
initWithCertificate:
objectsAtIndexes:
setAlgorithmCapabilities:
setRetryCount:
setTimestampRequest:
setVerifySignatures:
TQ,V_chainMode
_timestampServer
_verifyTimestamps
certificates
initWithDataContent:recipient:
initWithIdentity:error:
setObject:forKey:
setTimeStyle:
T@\"NSData\",&,V_originatorPubKey
MSErrorWithDomain:code:underlyingError:description:
T@\"<MSCMSMessage>\",&
encryptContent:
T@\"NSMutableSet\",&,V_certificates
T{heim_oid=Q^I},R,V_Asn1OID
arrayWithObject:
parseTimestampResponse:
T@\"MSAlgorithmIdentifier\",&,N,V_signedAttrsHashAlgorithm
_originatorIdentity
_statusString
encodeEncryptionParameters:
encryptedKeys
identifierData
legacyASN1Encoding
signatureAlgorithmWithDigestAlgorithm:error:
_timestampAttribute
addRecipient:error:
calculateAttributesWithDigest:error:
chainMode
removeAllObjects
setRecipients:
setWithObject:
verifyCountersignatures:error:
addUnprotectedAttribute:
initDigestAlgorithmWithSignatureAlgorithm:error:
initWithIdentity:signatureAlgorithm:error:
setKeyEncryptionAlgorithm:
setVerifyTime:
signingTime
T@\"MSAlgorithmIdentifier\",&,N,V_bodyHashAlgorithm
T@\"MSOID\",R
signedAttrsData
_capabilities
_failInfo
_firstRetryErrorCode
addSigner:
capabilities
T@\"MSOID\",R,V_digestAlgorithm
version
T@\"MSOID\",R,V_algorithm
caseInsensitiveCompare:
decodeRecipientInfo:certificates:LAContext:error:
decryptWrappedKey:kek:iv:
insertObject:atIndex:
mutableBytes
_attributes
_recipients
dataContent
initWithTimestampToken:
isSupportedHashAlgorithm:
removeObjectAtIndex:
verifyTime:
verifyWithSignerInfo:policies:error:
T@\"MSDecodeOptions\",&,V_options
_issuerNameData
_containingSignerInfo
encodeOriginatorInfoCertificates:error:
expirationTime
initWithEmbeddedContent:signer:error:
rawTimestampTokenData
self
key
T@\"NSData\",&,V_encryptedContent
T^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}},R,V_asn1AlgId
_encryptionCertificate
absoluteString
encryptedContent
expectedHashLength:
isEqual:
T@\"NSData\",W,N,V_signedAttrsHash
T^{heim_base_data=Q^v},V_subjectKeyId
initWithCertificate:signatureAlgorithm:error:
initWithEmbeddedContent:recipient:
isRetryableError:
protectedAttributes
setUnsignedAttrsData:
signatureCalculated
T@\"NSArray\",&,V_algorithmCapabilities
_originator
encodeMessageSecurityObject:
initWithCertificate:algorithmCapabilities:
initWithHashAgilityValues:
respondsToSelector:
setContentChanged:
setLegacyASN1Encoding:
T@\"MSOID\",&
_timeStampTokenData
decodeAttribute:error:
digestAlgorithms
initWithCapacity:
#16@0:8
@\"NSNumber\"
@24@0:8^{GeneralName=i(?={GeneralName_otherName={heim_oid=Q^I}{heim_base_data=Q^v}}{heim_base_data=Q^v}{heim_base_data=Q^v}{GeneralName_directoryName=i(?={RDNSequence=I^{RelativeDistinguishedName}})}{heim_base_data=Q^v}{heim_base_data=Q^v}{
@24@0:8^{MessageImprint={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}16
@36@0:8@16@24B32
B40@0:8@16Q24^@32
@32@0:8:16@24
@32@0:8^{heim_oid=Q^I}16^@24
B40@0:8@16^{RecipientInfo=i(?={KeyTransRecipientInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}{KeyAgreeRecipientInfo=i{OriginatorIdentifierOrKey=i(?={IssuerAndSerialNumber={heim_base_dat
@\"MSCMSTimestampAttributeInternal\"
@32@0:8@16Q24
@56@0:8@16q24Q32@40@48
v48@0:8@16@24@32@?40
@40@0:8@16Q24@32
Q
@\"NSObject<OS_dispatch_queue>\"
B48@0:8@16@24@32^@40
@\"NSSet\"
@\"<MSCMSAttributeCoder>\"32@0:8@\"MSCMSAttribute\"16^@24
@\"MSCMSMutableAttributeArray\"
v24@0:8@\"MSOID\"16
@\"NSData\"24@0:8^@16
B24@0:8^@16
@\"MSTimestampResponse\"
@52@0:8I16I20I24@28@36^@44
@44@0:8^{__SecIdentity=}16@24B32^@36
@40@0:8^{__SecIdentity=}16@24^@32
@40@0:8^{__SecCertificate=}16@24@32
^{__CFData=}32@0:8@16B24B28
@40@0:8@16@24^{heim_base_data=Q^v}32
^{__SecIdentity=}
v32@0:8^{__SecCertificate=}16^@24
@\"MSDecodeOptions\"
@44@0:8^{__SecCertificate=}16@24B32^@36
B32@0:8^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}16^@24
v24@0:8^{__SecCertificate=}16
@\"MSAlgorithmIdentifier\"
Q24@0:8^@16
v32@0:8@?16@24
B56@0:8@16@24@32@40^@48
v24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16
@\"MSOID\"16@0:8
B24@0:8@16
v48@0:8q16q24@32@?40
i
^{__SecCertificate=}32@0:8Q16^@24
v24@0:8^{MessageImprint={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}16
@\"NSDate\"
@52@0:8@16B24@28Q36^@44
@24@0:8^{__SecIdentity=}16
@16@0:8
B24@0:8@\"Protocol\"16
v24@0:8@\"NSData\"16
@20@0:8B16
^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}}
@32@0:8^{__SecIdentity=}16^@24
@48@0:8^{RecipientInfo=i(?={KeyTransRecipientInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}{KeyAgreeRecipientInfo=i{OriginatorIdentifierOrKey=i(?={IssuerAndSerialNumber={heim_base_data=Q
@24@0:8@\"NSCoder\"16
@52@0:8@16B24@28@36^@44
^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}16@0:8
^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}
v32@0:8Q16@24
^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}
@32@0:8@16@24
v24@0:8^{__SecIdentity=}16
@24@0:8@16
@\"NSMutableArray\"
@64@0:8@16q24Q32@40@48*56
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@0:8
B24@0:8:16
@\"NSURL\"
@44@0:8q16@24q32B40
v24@0:8^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}}16
Q16@0:8
@32@0:8@16^@24
q16@0:8
v24@0:8q16
@48@0:8@16@24@32^@40
@\"MSCMSAttribute\"24@0:8^@16
@56@0:8@16@24@32@40^@48
@\"<MSCMSMessage>\"16@0:8
@24@0:8:16
i16@0:8
@44@0:8@16B24@28^@36
B24@0:8#16
Vv16@0:8
^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}}16@0:8
^{__SecTrust=}32@0:8@16^@24
^{__SecTrust=}48@0:8@16@24@32^@40
v24@0:8@\"NSCoder\"16
v20@0:8B16
@\"MSPKIStatusInfo\"
@28@0:8@16B24
v24@0:8@\"<MSCMSMessage>\"16
B16@0:8
@28@0:8^{__SecCertificate=}16B24
^{__SecIdentity=}16@0:8
B32@0:8@16^@24
I24@0:8^@16
v32@0:8@16@24
@40@0:8:16@24@32
^{__SecCertificate=}
@\"NSObject<OS_xpc_session>\"
B24@0:8^{__SecCertificate=}16
v32@0:8@16Q24
@\"MSCMSSignerInfo\"
@48@0:8@16q24@32@40
@48@0:8^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}16@24@32^@40
@\"NSArray\"
@32@0:8^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}16^@24
@\"MSMessageImprint\"
@\"MSCMSSignedData\"
@\"NSDictionary\"
@40@0:8^{__SecCertificate=}16@24^@32
d24@0:8q16
v44@0:8@16B24@28d36
B32@0:8^{MessageImprint={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}16^@24
B40@0:8@16@24^@32
v24@0:8^{heim_base_data=Q^v}16
v32@0:8@16^@24
@24@0:8Q16
@40@0:8@16@24^@32
@24@0:8^{__SecCertificate=}16
v24@0:8r^{RecipientInfo=i(?={KeyTransRecipientInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}{KeyAgreeRecipientInfo=i{OriginatorIdentifierOrKey=i(?={IssuerAndSerialNumber={heim_base_data=
^{heim_base_data=Q^v}
@40@0:8@16@24@32
@\"MSOID\"
@32@0:8^{__SecCertificate=}16@24
@40@0:8^{__SecCertificate=}16@24^{__SecIdentity=}32
q
@32@0:8^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}}16^@24
@\"NSData\"16@0:8
B
^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}}
v40@0:8@16Q24^@32
v32@0:8^{__SecIdentity=}16^@24
@\"<MSCMSMessage>\"
@\"NSString\"16@0:8
@48@0:8^{__SecCertificate=}16@24@32^{__SecIdentity=}40
@\"NSData\"
r^{ccdigest_info=QQQQ*^v^?^?i^?}16@0:8
^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}}16@0:8
^{_NSZone=}16@0:8
@32@0:8^{__CFString=}16^@24
v24@0:8^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}}16
v24@0:8@16
^{__CFData=}24@0:8@16
@\"NSString\"
^{__CFString=}16@0:8
Q24@0:8@16
v20@0:8i16
@36@0:8@16I24^@28
q24@0:8^{PKIFailureInfo=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16
@32@0:8^{heim_base_data=Q^v}16^@24
^{heim_base_data=Q^v}16@0:8
@\"NSMutableSet\"
^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}16@0:8
v24@0:8^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}16
@40@0:8@\"NSData\"16@\"MSDecodeOptions\"24^@32
^{__SecCertificate=}16@0:8
{heim_oid=Q^I}16@0:8
{heim_oid=\"length\"Q\"components\"^I}
v24@0:8Q16
B28@0:8B16^@20
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}
?
@24@0:8^@16
@48@0:8@16@24Q32^@40
@32@0:8^{__SecCertificate=}16^@24
v16@0:8
ASN1_OVERRUN
1.3.6.1.5.5.7.3.8
underlying_error_code
SHA-384
unable to encode signed attributes
unable to decode SMIME Capabilities Attribute
trust evaluation of signer failed
v8@?0
Other timestamp response cannot be nil
algorithmParameters
unable to copy OID
Unable to encode signedData: no signers and not certs-only message
MSErrorCryptoDomain
SHA-256
unable to decode CMSAttributes
Unknown ASN1 error
v32@?0@8Q16^B24
first_error_code
Timestamp response does not contain a message imprint
  Policy: %@\n
<MSMessageImprint: %p>\n
Failed encoding type CMSIdentifier
3
Unable to encode signedData: failed to encode a SignerInfo
underlyingErrorDomain
Not a Signing Time attribute according to AttributeType
Failed encoding type MultipleSignatures
1.2.840.113549.1.9.16.2.14
id-aa-timeStampToken attribute has %lu values, expected 1
unable to create trust object
unable to find any certificates in keychain
Could not sign data: no identity in keychain for certificate
1.2.840.113549.1.1.12
unable to verify timestamp signature because there are no timestamps
1.3.14.3.2.6
unable to decode Encryption Key Preference Attribute
unable to find any identities with email address %@
signer is missing signature
1.2.840.10045.4.3.4
com.apple.messagesecurity.mstimestamp.fetchTimestampWithError_success
\n
  Request Size: %lu bytes\n
unable to decode Apple Hash Agility Attribute
Failed encoding type AppleAgileHash
unable to decode envelopedData.originatorInfo
Self message imprint has nil parameter
unable to decode MessageDigest
unable to find any certificates with email address %@
com.apple.messagesecurity.MSCMSContentTypeError
Unable to encrypt
!
Failed to create Apple timestamp policy
unable to build chain according to mode; missing signer info or signer certificate missing from signer info
UnknownContentTypeOID
1.2.840.113549.1.1.13
Failed encoding type ContentType
Invalid parameter
1.2.840.113549.1.9.4
MessageSecurity/MSCMSAttribute.swift
timestamp.apple.com
unable to build chain according to mode; could not evaluate trust
1.2.840.113549.1.9.5
Failed encoding type SMIMECapabilities
MSCMSAppleTimestampAttribute: no timestamp token data to encode
NULL
Failed to create XPC session
Unable to allocate attribute array
v32@?0@\"MSCMSCounterSignerInfo\"8Q16^B24
ASN1_INDEF_EXTRA_DATA
Unable to verify
YES
signedData contains content but has no signers
unable to get certificate from provided identity
2.16.840.1.101.3.4.1.42
timestampServer
Status string mismatch
Failed encoding type CMSAttributes
Not a ContentType attribute according to AttributeType
ASN1_MAX_CONSTRAINT
unable to compute digest for signature
MSDecryptGCM error: %d
1.2.840.113549.1.7.5
1.2.840.113549.1.9.16.1.23
Failed to unarchive timestamp response
timestamp verification failed for signer %lu
1.2.840.113549.1.9.6
unable to set verify date on trust object
decode failed due to signer verification failure
Failed to create message imprint for timestamp verification
Could not sign data: no digest
unknown ccMode -- unexpected encryption algorithm: %@
  Status: %@\n
Status mismatch
TSA policy OID mismatch
1.2.840.113549.1.9.3
| 
com.apple.messagesecurity
1.3.6.1.5.5.7.6.52
http://timestamp.apple.com/ts-ec
timeStampTokenData
  Hash: (empty)
  Algorithm OID: %@
BundledSN
-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:]
MessageImprint pointer cannot be NULL
fetch
(nil)
Signing Time Attribute MUST have a single signed attribute value
ASN1_INDEF_OVERRUN
Signer has no signature algorithm
TSTInfo data is nil
  Serial Number: (none)\n
decode failed due to signature verification failure
unable to copy Attribute
unable to decode ContentType
the Encryption Key Preference Attribute did not match any certificates
2.16.840.1.101.3.4.1.22
could allocate OID components
decode failed due to timestamp verification failure
1.2.840.113549.1.1.4
MSOID %@ does not indicate a signature algorithm
Failed encoding type OriginatorInfo
Invalid MessageImprint data
Invalid OID string format
responseObject
Unable to get serial number from certificate
unable to find a certificate matching the signer
Unknown error
; 
Request contained nonce but response does not
Serial number mismatch
B32@?0@\"<MSCMSAttributeCoder>\"8Q16^B24
\xd1
Other timestamp request cannot be nil
Granted with modifications
Other message imprint has unsupported hash algorithm
ASN1_BAD_ID
  Response Size: %lu bytes
1.2.840.113549.1.1.5
1.2.840.10045.2.1
%u.%u
Unable to encode signedData: unable to allocate certificates array
Not an SMIMECapabilities attribute according to AttributeType
SMIME Capabilities Attribute should only have one value
unable to verify countersignature(s) for countersigner %lu
decode failed for recipientInfo (keyEncryptionAlgorithm)
2.16.840.1.101.3.4.1.45
1.2.840.113549.3.7
unable to decode SKID Identifier
unable to get private key from provided identity
MessageSecurity.MSCMSAuthEnvelopedData
Failed encoding type CMSCBCParameter
No timestamp request data available
statusString
Waiting
Hashed messages do not match
-[MSCMSTimestampAttribute initWithTimestampToken:]
ASN1_GOT_BER
1.3.14.3.2.26
ASN1_BAD_CHARACTER
no certificates found in signerInfo for trust evaluation
2.16.840.1.101.3.4.2.2
Invalid OID component at index %lu: value %ld is out of valid range [0, %u]
  TSA: %@\n
ASN1_BAD_TIMEFORMAT
  Request Certificates: %@\n
Timestamp response data mismatch
unable to decode Apple Hash Agility V2 Agile Hash
ASN1_MIN_CONSTRAINT
Invalid content type
Underlying ASN1 error 
1.2.840.113549.1.9.2.51
%@
unable to decode data content (%ld bytes)
Failed encoding type CMSRC2CBCParameter
SecKeyAlgorithm %@ does not indicate a signature algorithm
unknown ccAlg -- unexpected encryption algorithm: %@
Failed to allocate memory for OID components
  Nonce: %@ (%lu bytes)\n
Revocation warning
BundledSKID
ContentType attribute contains more than one value
Could not decode message-digest attribute
1.2.840.113549.1.7.2
counter signer has no reference to a signer with a signature
system-keychain
unable to find any identities in keychain
2.16.840.1.101.3.4.1.26
Self timestamp response has nil parameter
Failed encoding type SignerInfo
MSErrorCMSDomain
decode failed for recipientInfo (rid)
Message imprint cannot be nil
  Gen Time: %@ UTC\n
ASN1_BAD_FORMAT
Message-digest attribute failed to verify
Could not sign data: no key or certificate specified
2.16.840.1.101.3.4.1.7
Nonce mismatch
Apple Hash Agility V2 Attribute must have one value
MSTimestampHTTPErrorDomain
1.2.840.113549.1.9.16.1.9
Unable to decode AuthEnvelopedData
timestamp_server
Failed encoding type SMIMEEncryptionKeyPreference
com.apple.messagesecurity.MSCMSContentError
com.apple.MSTimestampXPCService.queue
<MSTimestampResponse: %p>\n
v32@?0@\"NSSet\"8Q16^B24
Failed to create XPC session: %s
<MSTimestampRequest:\n
Unable to encode signedData: missing digest algorithm and not certs-only message
invalid Time choice in Signing Time
invalid Time choice in Expiration Time
Failed to decode timestamp token as MSTimestampResponse
ASN1_EXTRA_DATA
com.apple.HeimASN1
Revocation notification
signer index, %lu, out of range of signer count, %lu
2.16.840.1.101.3.4.1.47
.
  Policy OID: %@\n
Status %ld
ASN1_TYPE_MISMATCH
1.3.133.16.840.63.0.2
\n--- Additional Debug Info ---\n
No key for identity 
Algorithm identifiers do not match
MessageSecurity.MSCMSTimestampAttributeInternal
1.2.840.113549.1.7.6
Missing algorithm OID
MSErrorASN1Domain
2.16.840.1.101.3.4.1.25
2.16.840.1.101.3.4.1.27
Self timestamp request has nil parameter
Expiration Time Attribute MUST have a single signed attribute value
MSErrorAllocationDomain
Signed content-type attribute does not match content-type in signedData
unable to create countersignature attribute for countersigner %lu
MessageSecurity/MSCMSAuthEnvelopedData.swift
B32@?0@\"NSString\"8Q16^B24
unable to decode envelopedData.recipientInfos
Failed to extract TSTInfo from SignedData
unable to allocate Attribute
Version numbers do not match
v24@?0@\"MSAlgorithmIdentifier\"8^B16
  TimeStampToken: (nil)\n
Unable to encode RecipientInfo: missing destination address
certReq
Failed to decode TimeStampResp: ASN.1 error %d
unable to find identity matching %@
Failed encoding type AlgorithmIdentifier
signer verification failed for signer %lu
logCMSDecodingFailures
Failed encoding type DataContent
1.2.840.113549.1.9.16.1.2
unable to decode CMS Identifier tag
QuerySN
ASN1_MISSING_FIELD
ASN1_INDEF_UNDERRUN
1.2.840.113549.1.7.3
unable to copy Algorithm Identifier
reqPolicyOIDString
v32@?0@\"NSData\"8Q16^B24
2.16.840.1.101.3.4.1.5
unable to decode signedData (%ld bytes)
MSErrorKeychainDomain
%s did not find SubjectKeyIdentifier %@
ASN1_INVALID_CHOICE
<MSTimestampRequest: %p>\n
unable to find certificate by identifier; invalid choice in encoding
Unable to decode
errorCode
Granted
SHA-512
Not an Encryption Key Preference attribute according to AttributeType
Self message imprint has unsupported hash algorithm
failed to create signerInfo object for signer %u
unable to get contentType from envelopedData.encryptedContentnInfo
Cannot encode signed attributes: no SignedData
decode failed for signerInfo due to RFC 5652 violation (version)
messageType
<MSMessageImprint:\n
SHA-1
%s did not find IssuerAndSerialNumber %@ %@
INVALID_ISSUER
2.16.840.1.101.3.4.1.46
--- Basic Info ---\n
requestObject
Fail info presence mismatch
Fail info mismatch
decode failed for recipientInfo (originator)
version
  Hash: %@ (%lu bytes)
%@ is not a supported digest algorithm
EnvelopedData
Unable to encode compressed data
2.16.840.1.101.3.4.1.21
  Nonce: (none)\n
NO
Unable to encode signedData: unable to allocate signerInfos array
decode failed for signedData due to RFC 5652 violation
Unknown content type
No certificate for identity 
2.16.840.1.101.3.4.2.3
Timestamp request data does not match
Request policy OID mismatch
ASN1_MISPLACED_FIELD
com.apple.MessageSecurity.MSTimestampXPCService
Other message imprint cannot be nil
MessageSecurity.MSCMSCompressedData
underlying_error_domain
hashedMessage
unable to verify countersigner %lu
MD5 is not supported for signing
@\"NSObject<OS_xpc_object>\"8@?0
  Message Imprint: %@\n
Failed encoding type MessageDigest
1.3.14.3.2.7
unable to decode Algorithm Identifier
Unable to encode SignerInfo: missing signer certificate
SignedData error
1.2.840.10045.4.3.3
1.2.840.113549.3.2
2.16.840.1.101.3.4.1.6
Other timestamp request has nil parameter
0x%02x,
%d
could not parse OID into data
Unable to encode enveloepd data
timestampResponse
no signer with input certificate hash
Not a Multiple Signatures attribute according to AttributeType
Apple Hash Agility Attribute should only have one value
AuthEnvelopedData
Server URL mismatch
Timestamp request was not granted. Status: %ld
TSA mismatch
countersigner verification failed for signer %lu
unable to decode signerInfo in countersignature
unable to decode Signing Time value
failed to set verification time
1.2.840.10045.4.3.1
XPC communication error: %s
Rejection
Message imprint presence mismatch
Failed encoding type CMSSignedData
Timestamp response is missing message imprint or algorithm
2.16.840.1.114027.80.9.1.15
v24@?0@\"NSObject<OS_xpc_object>\"8@\"NSObject<OS_xpc_object>\"16
Timestamp token signature and certificate verification failed
Error Unavailable
Not a MessageDigest attribute according to AttributeType
Failed encoding type TimeStampReq
invalid CMS Identifier choice
Failed encoding type AppleHashAgilityValue
BundledIssuer
Algorithm Identifier %@ does not indicate a public key algorithm
http://timestamp.apple.com/ts01
No response object in XPC reply
Failed encoding type ContentInfo
Failed encoding type CMSOrderedAttributes
2.16.840.1.101.3.4.1.2
Other message imprint has nil parameter
findIdentityByCertificate
NOT_NULL
unable to access the content encryption key
hasFailInfo
signer has no signature algorithm
valueForBooleanDefault
Could not sign data: no private key
Unable to encode
Unable to decode comrpessed data
2.16.840.1.101.3.4.1.1
Nonce values do not match
Unable to get issuer sequence from certificate
failed to get public key from certificate
Certificate request flags do not match
signature verification failed for signer %lu
en_US_POSIX
MessageSecurity.MSCMSEnvelopedDataInternal
  Algorithm: %@\n
Unable to encode signedData: unable to allocate digest algorithm array
errorDescription
DataContent
internal asn1 error
2.16.840.1.101.3.4.2.1
missing or invalid OID string %@
status
CMSSignedData
No digest algorithm specified
ASN1_BAD_LENGTH
ASN1 success
TimeStampToken data is nil
<MSTimestampResponse:\n
unknown type for Encryption Key Preference Attribute
.%u
  TimeStampToken: Present\n
unable to create trust object due to security error
  Policy: (none)\n
Other timestamp response has nil parameter
countersignature verification failed for signer %lu
1.2.840.113549.1.9.16.2.11
MSErrorTrustDomain
default
Unable to encode signedData: content is not detached and no content specified
B32@?0@\"MSCMSSignerInfo\"8Q16^B24
Not a Countersignature attribute according to AttributeType
1.2.840.10045.4.1
success
Unable to encode signedData: id-data content type and no data content
QueryIssuer
2.16.840.1.101.3.4.1.41
retry_count
(not set)
MessageDigest attribute contains more than one value
unable to create timestamp attribute for timestamp %lu
error_code
elapsed_ms
1.2.840.113635.100.9.2
No timestamp server URL specified
  Serial Number: %@ (%lu bytes)\n
Version mismatch
CMSIdentifier has inconsistent type and stored values: expected issuerAndSerialNumber
unable to decode Expiration Time value
unable to decode envelopedData.unprotectedAttrs
Missing or too many content-type attribute(s)
v32@?0@\"MSOID\"8Q16^B24
%02X
Could not sign data: no signature algorithm
2.16.840.1.101.3.4.2.4
  Gen Time: (none)\n
1.2.840.113635.100.9.1
findCertificateBySubjectKeyID
init()
could not parse OID into string
QuerySKID
decode failed for recipientInfo (rid vs encryptedKey count)
unknown keySize -- unexpected encryption algorithm: %@
TimeStampToken is not SignedData
unable to add signer cert to certificates; missing signer info or signer certificate missing from signer info
Not an Expiration Time attribute according to AttributeType
ASN1_PARSE_ERROR
ASN1_EXACT_CONSTRAINT
UNEXPECTED_VALUE
TimeStampToken error
RecipientInfo not found
Unable to decode the content encryption key
1.2.840.113549.1.9.16.3.6
nonce
Unable to encode signedData: embedded content type specified and no embedded content
INVALID_OID
unable to encrypt/decrypt the content
signer has no reference to a signedData with content
MSOID %@ does not indicate a digest algorithm
0123456789.
unable to get contentType from signedData
Unable to encode content info: missing content type or content
InvalidContentTypeOID
1.2.840.113549.1.7.1
1.2.840.113549.1.9.16.1.4
1.2.840.10045.4.3.2
underlyingErrorCode
ASN1 encoding error
unable to find a certificate matching the recipient
>
TSA policy OIDs do not match
  Failure Info: %ld\n
1.2.840.113635.100.9.3
unable to add recipient
com.apple.MessageSecurity
com.apple.messagesecurity.mstimestamp.fetchTimestampWithCompletionBlock_success
  Version: %ld\n
  Message Imprint: (none)\n
could not parse OID into parts %@
  Nonce Length: %lu bytes
CMSIdentifer has unknown type: %d
ASN1_GOT_INDEFINITE
%@:%@ 
CommonCrypto error 
Unable to decode OriginatorInfo
unable to allocate Algorithm Identifier
unknown blockSize -- unexpected encryption algorithm: %@
Failed to decode TSTInfo: ASN.1 error %d
1.2.840.113549.1.9.15
unable to decode envelopedData (%ld bytes)
failInfo
Timestamp token SignedData not available for verification
UTC
v24@?0@\"MSOID\"8^B16
yyyyMMddHHmmss'Z'
MSTimestampErrorDomain
decode failed for recipientInfo due to RFC 5652 violation (version)
1.2.840.113549.1.1.11
Failed to decode TimeStampToken as ContentInfo
SignedData does not contain encapsulated content (TSTInfo)
Encryption Key Preference Attribute should only have one value
unable to verify timestamp signature for timestamp %lu
Unable to encode signedData: missing digest algorithms
Content-type attribute must not be present in Countersignature
%@ is not a supported signature algorithm
1.2.840.113549.1.1.7
https://timestamp.apple.com/tsa-mldsa87-rsa3072-pss-sha512
Timestamp request cannot be nil
algorithmOIDString
unable to decode Multiple Signatures attribute
  Status String: %@\n
ASN1_OVERFLOW
unable to decode content info (%ld bytes)
Missing or too many message-digest attribute(s)
messageImprint
Missing value for Multiple Signatures attribute
Failed encoding type SecCMS_SMIMEEncryptionKeyPreference
yyMMddHHmmss'Z'
1.2.840.113635.100.9.4.1
Timestamp mismatch
v32@?0@\"<MSCMSAttributeCoder>\"8Q16^B24
ContentInfo
Could not decode content-type attribute
1.2.840.113549.2.5
1.2.840.113549.1.1.1
Unknown
unable to decode CMS Identifier
v32@?0@\"MSCMSSignerInfo\"8Q16^B24
1.2.840.113549.1.1.14
1.2.840.113549.1.9.16.3.7
Unable to encode signedData: missing content type
musr
findCertificateByIssuerAndSerialNumber
  Server URL: %@
No timestamp response data to parse
CMSIdentifier has inconsistent type and stored values: expected subjectKeyId
failed to set anchor certificates
Unable to encode SignerInfo: missing destination address
```
