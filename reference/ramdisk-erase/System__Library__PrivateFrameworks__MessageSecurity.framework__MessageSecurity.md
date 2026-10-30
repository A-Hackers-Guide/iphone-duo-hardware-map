# `/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 948,160 bytes.

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
MSTimestampRequest
MSMessageImprint
MSCMSIdentifier
MSCMSAppleExpirationTimeAttribute
MSCMSAppleTimestampAttribute
MSError
MSCMSContentInfo
MSCMSEncryptionKeyPreferenceAttribute
MSCMSTimestampAttribute
MSCMSMessage
MSCMSEnvelopedDataInternal
NSSecureCoding
MSCMSAppleHashAgilityAttribute
MessageSecurityMessage
NSObject
MSCMSAttributeCoder
MSOID
NSCoding
MSDecodeOptions
MSCMSMessageDigestAttribute
MSCMSSMIMECapabilitiesAttribute
MSCMSMutableAttributeArray
MSCMSTimestampAttributeInternal
MSCMSRecipientInfo
MSPKIStatusInfo
MSCMSContentTypeAttribute
MSCMSMultipleSignaturesAttribute
MSCMSCountersignatureAttribute
MessageSecurityHexRepresentation
MSTimestampResponse
MSCMSSignedData
MSCMSSigningTimeAttribute
MSCMSAppleHashAgilityV2Attribute
MSCMSCounterSignerInfo
MSCMSAuthEnvelopedData
MSAlgorithmIdentifier
MSCMSAttribute
MSCMSEnvelopedData
MSCMSSignerInfo
MSCMSCompressedData
_status
T@\"NSData\",&,V_timeStampTokenData
_maxRetryAttempts
addRecipient:
createAttributeArrayFromAttributeSetRaw:error:
signerPrivKey
signedAttrsData
encodeMessageSecurityObject:
encodedAttributeSet
indexOfObjectPassingTest:
tstinfo
T{heim_oid=Q^I},R,V_Asn1OID
parameters
stringWithFormat:
OIDBytes
_messageImprint
blockSize:
ccdigest
performSingleSyncFetchAttempt:
recipientCertificates
signedData
T@\"NSArray\",&,V_algorithmCapabilities
_encryptionCertificate
_skidData
decodeBoolForKey:
encryptionKey
setLegacyASN1Encoding:
TB,V_verifyTimestamps
addSigner:withCertificates:
array
dataWithData:
initWithData:error:
isEqualToData:
performAsyncFetchAttempt:maxAttempts:onQueue:completion:
verifySignatureAndSignerWithPolicies:verifyTime:anchorCertificates:error:
isProxy
_digestAlgorithms
containingSignerInfo
encryptedKeys
initWithDataContent:
T@\"NSArray\",R
T@\"NSData\",&,V_serialNumber
encryptionCertificate
performSelector:
timestampToken
verifyContentTypeAttribute:
asn1AlgId
encodeImplicitAttributesWithError:
hasFailInfo
initWithEmail:LAContext:error:
isEqualToTimestampResponse:error:
setSignedAttrsHashAlgorithm:
unsignedAttrsData
T@\"NSArray\",&,V_anchorCertificates
cString
options
algorithmIdentifierWithOID:
initWithEmbeddedContent:recipient:encryptionAlgorithm:
parseTimestampResponse:
setAsn1OidFromOIDString:error:
setFirstRetryErrorCode:
OIDWithString:error:
T@\"NSData\",&,N
T^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}},V_encodedSignerInfo
copyAttributeData:
setTimestampResponse:
setUnprotectedAttributes:
verifyCountersignaturesAndCountersignersWithPolicies:verifyTime:anchorCertificates:signature:error:
version
T@\"NSNumber\",&,V_version
_timestampRequest
finishAsyncFetch:error:onQueue:completion:
identifierData
identity
initWithCapacity:
objectForKey:
_attributeDERData
_hashAgilityValue
bytes
encodeKeyAgreeRecipientInfo:recipientInfo:error:
enumerateObjectsUsingBlock:
initWithIdentity:signatureAlgorithm:error:
respondsToSelector:
setVerifyTime:
verifyWithMessageImprint:error:
T@\"NSDate\",&,V_verifyTime
createTrustObjectWithPolicies:error:
encodeRecipientInfo:recipientInfo:error:
encodeWithCoder:
freeRecipientInfo:
initDigestAlgorithmWithSignatureAlgorithm:error:
setAdditionalCertificates:
certificates
cleanupMessageImprint:
decodeSignerInfo:certificates:LAContext:error:
performSelector:withObject:withObject:
removeObjectAtIndex:
setEncryptedKeys:
setTimeStampToken:
verifyMessageDigestAttribute:error:
T@\"MSCMSSignerInfo\",W,N,V_containingSignerInfo
_attributeType
_unprotectedAttributes
initWithDecryptionKey:
messageImprint
verifySignature:
T@\"MSCMSSignedData\",&,V_timeStampToken
T@\"NSDate\",R
T^{__SecIdentity=},V_identity
bodyHashAlgorithm
buildMessageImprintForASN1:error:
indexSet
initWithEmailAddress:
removeSignersWithEmailAddress:error:
T@\"NSMutableArray\",&,V_genericAttributes
_detached
removeSignersWithIdentity:error:
retainCount
setHashedMessage:
verifyWithSignerInfo:policies:error:
T@\"NSString\",R,V_OIDString
_messageDigest
hash
initWithDecryptionIdentity:
isEqual:
isMemberOfClass:
keyEncryptionKey:forEncryption:secCMSCompatibility:
T@\"MSCMSTimestampAttributeInternal\",&,V_timestampAttribute
signedAttrsHash
T@\"NSMutableSet\",&,V_certificates
T@\"NSNumber\",R,V_version
createXPCMessageForTimestampFetch
initWithBytes:length:
initWithSignerInfo:
isSupportedHashAlgorithm:
T@\"NSArray\",N,C
_tsa
certificateHasTimeStampingEKU:
dateWithTimeIntervalSinceReferenceDate:
init:
initWithDataContent:isDetached:signer:additionalCertificates:error:
mutableCopy
setContent:
_additionalCertificates
_rawTimestampTokenData
_signatureAlgorithm
addSMIMEEncryptionKeyPreferenceAttribute:
initWithBytes:length:encoding:
removeObject:
setSignerCertificate:
setXpcQueue:
_LAContext
_options
dataContent
setMaxRetryAttempts:
verifyTimestamps:error:
_signerCertificate
removeAllObjects
setVersion:
stringWithUTF8String:
stringFromDate:
attributeValues
ccMode:
T@\"NSArray\",R,&,V_attributeValues
T@\"NSData\",&,V_messageDigest
_dataContent
_hashAgilityValues
addUnprotectedAttribute:
checkSignedPerRFC5652:
decodeAttribute:error:
date
initWithCertificate:recipientsAlgorithmCapabilities:error:
retryCount
setSignerPrivKey:
setTimestampAttribute:
stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:
containsObject:
algorithmCapabilities
hashAgilityValues
initCertsOnlyWithCertificates:error:
initWithCertificate:
initWithSignerInfo:signerChainMode:additionalCertificates:
setLAContext:
RSASignatureOIDWithDigestAlgorithm:error:
T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_signerPrivKey
_keyEncryptionAlgorithm
_timeStampTokenData
copy
indexesOfObjectsPassingTest:
setEncodedAttributeSet:
encryptBulkKey:
MSErrorWithDomain:code:errorLevel:underlyingError:description:
OIDString
T@\"NSData\",N,C
_signatureCalculated
absoluteString
setDigestAlgorithms:
invalidateXPCSession
setContainingSignedData:
setEncodedAttribute:
verifySignatures:
T@\"MSTimestampResponse\",R
Tq,V_maxRetryAttempts
Tr^{ccdigest_info=QQQQ*^v^?^?i^?},R
UTF8String
_failInfo
addSigner:
dictionary
initWithAsn1AlgId:error:
T@\"MSOID\",R,V_digestAlgorithm
T@\"NSURL\",&,V_timestampServer
_certChainRequested
replaceObjectAtIndex:withObject:
setAttributes:
tsaPolicyID
verifySignaturesAndSignersWithPolicies:verifyTime:anchorCertificates:error:
T@\"NSDate\",R,&,V_expirationTime
TB,V_verifySignatures
_signerInfo
decodeKeyAgreeRecipientInfo:certificates:LAContext:error:
setAnchorCertificates:
verifyCountersignatures:error:
verifySignatures
TB,R,V_hasFailInfo
_certificates
count
initRSASignatureOIDWithDigestAlgorithm:error:
initWithDataContent:isDetached:signer:signerChainMode:error:
numberWithUnsignedInt:
_asn1AlgId
setSignature:
signature
attributes
envelopedData
removeLastObject
addDigestAlgorithmFromSigner:
isEqualToString:
removeRecipientWithEmailAddress:error:
_OIDBytes
_reqPolicyID
_timestampResponseParsed
algorithmIdentifier
allObjects
issuerAndSerialNumber
setCertChainRequested:
setSignedAttrsData:
T@\"NSString\",R,C
T^{__SecCertificate=},R,V_encryptionCertificate
_encryptionAlgorithm
isRetryableError:
timeIntervalSinceDate:
TB,R,V_signatureCalculated
_encryptedKeys
decodeMessageSecurityObject:options:error:
initWithDataContent:recipient:encryptionAlgorithm:
messageDigest
T@\"NSMutableArray\",&,V_originatorCertificates
Tq,R,V_status
initWithEmbeddedContent:recipient:
isEqualToTimestampRequest:error:
setTimeStyle:
verifyWithRequest:error:
initWithFormat:
T@\"NSData\",&,V_issuerNameData
_anchorCertificates
_firstRetryErrorCode
addCounterSignerAttribute:
initWithEmbeddedContent:signer:signerChainMode:error:
setTsa:
_key
_protectedAttributes
initWithIdentity:error:
reqPolicyID
setEncryptionAlgorithm:
setSerialNumber:
verifyTimestamps
T@\"MSAlgorithmIdentifier\",&,N,V_signatureAlgorithm
T@\"MSAlgorithmIdentifier\",&,V_encryptionAlgorithm
T@\"NSData\",&,V_hashedMessage
T@\"NSData\",W,N,V_signedAttrsHash
TB,R
appendData:
encryptionAlgorithm
setAlgorithmCapabilities:
_signingTime
calculateContentDigestWithAlgorithm:error:
createTrustObjectWithPolicies:verifyTime:anchorCertificates:error:
dataUsingEncoding:
initWithAttribute:certificates:LAContext:error:
initWithIssuerName:serialNumber:negativeNumber:
initWithStatus:statusString:failInfo:hasFailInfo:
insertObject:atIndex:
T@\"MSPKIStatusInfo\",&,V_status
timestampServer
decryptContent:error:
initECSignatureOIDWithDigestAlgorithm:error:
initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:
key:
setTimeZone:
xpcSession
T@\"NSDate\",&,V_timestamp
_bodyHashAlgorithm
_serverURL
initWithAttribute:certificates:LAContext:containingSignerInfo:error:
initWithAttribute:error:
setEncryptionKey:
setSkidData:
timestampRequest
encodeKeyTransRecipientInfo:recipientInfo:error:
encodeObject:forKey:
T@\"MSCMSMutableAttributeArray\",&,V_protectedAttributes
_serialNumber
detached
encodeAttributeWithError:
encodedSignerInfo
maxRetryAttempts
_encodedAttributeSet
digestAlgorithms
hashAgilityValue
init:server:
initWithEmbeddedContent:signer:additionalCertificates:error:
setContentChanged:
setEmbeddedContent:
T@\"NSSet\",&,V_digestAlgorithms
sign:
supportsSecureCoding
timeStampTokenData
unprotectedAttributes
verifyTimestamps:
T@\"MSAlgorithmIdentifier\",&,N,V_signedAttrsHashAlgorithm
T@\"NSArray\",&,V_recipients
HybridSignatureOIDWithDigestAlgorithm:error:
T@\"NSArray\",R,V_certificates
addRecipient:error:
contentChanged
initWithSigningTime:
isEqualToDate:
digestAlgorithm
initWithAsn1OID:error:
initWithDictionary:
initWithEmail:algorithmCapabilities:
initWithSignerInfo:additionalCertificates:
performSelector:withObject:
setDetached:
signerCertificate
_Asn1OID
getCharacters:range:
setRetryCount:
timestampAttribute
signers
_signature
encodeAttributesWithError:
initWithTimeIntervalSince1970:
T@\"NSData\",&,V_key
TQ,R
_timestampAttribute
archivedDataWithRootObject:requiringSecureCoding:error:
getAttributesWithOID:
localizedDescription
objectForKeyedSubscript:
setWithObject:
Tq,R,V_failInfo
_timestamp
arrayWithObjects:count:
initSignatureOIDWithSecKeyAlgorithm:error:
initWithOID:parameters:
legacyASN1Encoding
removeSignerCertificatesWithIndexes:
retain
compare:
setRecipients:
setWithSet:
signatureAlgorithmOIDWithSecKeyAlgorithm:error:
verifySignaturesAndSignersWithPolicies:verifyTime:error:
setReqPolicyID:
T@\"MSOID\",R,V_type
_attributeValues
chainMode
issuerNameData
originatorIdentity
setObject:forKeyedSubscript:
setOriginatorIdentity:
initWithDigest:
arrayWithArray:
_containingSignerInfo
dictionaryWithObject:forKey:
initWithSignerInfo:signerChainMode:
setTimestampServer:
setUseIssuerAndSerialNumber:
T@\"NSData\",&,V_serialNumberData
T^{heim_base_data=Q^v},V_subjectKeyId
addObjectsFromArray:
length
setKeyEncryptionAlgorithm:
setRawTimestampTokenData:
stringWithString:
type
set
_contentChanged
T@\"MSOID\",&,V_reqPolicyID
encryptContent:
T@\"MSOID\",R,&
timeStampToken
T@\"NSData\",R,&,V_hashAgilityValue
T@\"NSObject<OS_xpc_session>\",&,V_xpcSession
T@\"NSString\",&,V_tsa
T@\"NSString\",R,V_statusString
_contentType
debugDescription
encodeOriginatorInfoCertificates:error:
initWithEmbeddedContent:
_OIDString
_serialNumberData
_xpcSession
addProtectedAttribute:
init:server:nonce:
initWithCertificate:legacyKeyWrapAlgorithm:
initWithString:error:
objectAtIndexedSubscript:
T@\"MSMessageImprint\",&,V_messageImprint
T@\"NSDate\",R,&,V_signingTime
_originatorPubKey
_useIssuerAndSerialNumber
decodeIntegerForKey:
fetchStartTime
getRecipients
reset
setBodyHashAlgorithm:
setObject:forKey:
setSigners:
setWithCapacity:
subjectKeyId
T@\"MSOID\",&,V_contentType
_signerPrivKey
dictionaryWithDictionary:
findBestEncryptionAlgorithmForNewRecipient:
freeKeyTransRecipientInfo:
setAttributeType:
T@\"NSArray\",&,V_additionalCertificates
T@\"NSData\",&,N,V_signature
T@\"NSURL\",&,V_serverURL
TB,V_certReq
addSMIMECapabilitiesAttribute:
data
decryptWrappedKey:kek:iv:
failInfo
T@\"<MSCMSMessage>\",N,&,VembeddedContent
T@\"MSAlgorithmIdentifier\",&,V_signatureAlgorithm
TB,V_certChainRequested
_identity
initWithDER:
initWithTimestampToken:
parseMSTimestampResponseFromReply:error:
verifyWithMessageImprint:policies:error:
_encodedAttribute
_statusString
errorWithDomain:code:userInfo:
recipientCertificate
setStatus:
certChainRequested
countByEnumeratingWithState:objects:count:
decode:error:
setDateFormat:
_issuerAndSerialNumber
_verifyTime
algorithm
createRequiredAttributes:
nonce
sleepForTimeInterval:
T@\"MSAlgorithmIdentifier\",&,V_algorithmIdentifier
_timestampServer
_verifyTimestamps
initWithUTF8String:
integerValue
setRecipientCertificates:
MSErrorWithDomain:code:underlyingError:description:
arrayWithCapacity:
decodeObjectOfClass:forKey:
domain
encryptedContent
.cxx_destruct
Tq,V_retryCount
T@\"NSData\",&,V_encodedAttributeSet
_content
_encodedSignerInfo
_recipientCertificates
initWithEnvelopedData:
initWithIssuerName:serialNumber:
_embeddedContent
decimalDigitCharacterSet
digestAlgorithmWithSignatureAlgorithm:error:
expirationTime
initWithDataContent:recipient:
parseFailureInfo:
setCertificates:
setDigestAlgorithm:
setTsaPolicyID:
caseInsensitiveCompare:
createSharedInfo:
removeObjectsAtIndexes:
setTimestampRequest:
T@\"<MSCMSMessage>\",&
T@\"NSArray\",&,V_signerPolicies
T^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}},V_issuerAndSerialNumber
_algorithm
appendFormat:
componentsSeparatedByString:
dictionaryWithObjects:forKeys:count:
setEncryptedContent:
T@\"NSData\",&,V_identifierData
T@\"NSData\",&,V_timestampResponse
addObject:
ccAlgorithm:
encodeEncryptionParameters:
signatureAlgorithmWithDigestAlgorithm:error:
xpcQueue
T@\"NSData\",&,V_originatorPubKey
addIndex:
serialNumberData
MSErrorWithDomain:code:errorLevel:underlyingError:description:arguments:
T@\"NSSet\",R,V_capabilities
Tq,V_version
_algorithmIdentifier
generateAttributeStruct
generateEncryptionKey:
initWithCapabilities:
initWithEmbeddedContent:error:
content
removeSignersWithIndexes:error:
TB,V_legacyASN1Encoding
contentType
initWithEmbeddedContent:signer:error:
initWithSkid:
rangeOfCharacterFromSet:
unarchivedObjectOfClass:fromData:error:
T@\"NSMutableArray\",&,V_attributes
_certReq
_nonce
encodeInteger:forKey:
initWithAttribute:LAContext:error:
initWithEmail:
removeAttributes:
setWithArray:
T@\"MSAlgorithmIdentifier\",&,V_digestAlgorithm
T@\"NSArray\",&,V_signers
T@\"NSData\",&,V_content
calculateAttributesWithDigest:error:
contentTypeAttributeWithOID:
initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:
setContentTypeWithType:
setEncodedSignerInfo:
enumerateObjectsAtIndexes:options:usingBlock:
setIssuerAndSerialNumber:
setProtectedAttributes:
setType:
setVerifyTimestamps:
signerPolicies
verifyCountersignatures:
setDataContent:
_hasFailInfo
characterSetWithCharactersInString:
encodedAttribute
initWithEmail:recipientsAlgorithmCapabilities:LAContext:error:
isKindOfClass:
setGenericAttributes:
verifyTime
OIDWithAsn1OID:error:
T@\"MSOID\",N,&,VencryptionAlgorithm
addCertificatesForSigner:mode:error:
algorithmIdentifierWithAsn1AlgId:error:
checkDecryptionResult:
release
getSignerCertificate:error:
originator
parseTSTInfo:error:
T@\"MSOID\",&
_retryCount
anchorCertificates
setCertReq:
setFetchStartTime:
setLocale:
_legacyASN1Encoding
_originator
_subjectKeyId
calculateSignatureDigestWithAlgorithm:error:
protectedAttributes
removeRecipientWithCertificate:error:
setServerURL:
useIssuerAndSerialNumber
T@\"NSData\",&,V_attributeDERData
Ti,V_type
componentsJoinedByString:
conformsToProtocol:
init:hashedMessage:
setRecipientCertificate:
T@\"MSCMSSignerInfo\",R,V_signerInfo
dealloc
T^{__CFString=},R
_originatorCertificates
objectAtIndex:
skidData
timestampResponse
TB,V_contentChanged
T^{__SecCertificate=},V_signerCertificate
_hashedMessage
digestOIDWithSignatureAlgorithm:error:
parseTimeStampToken:error:
setSignatureAlgorithm:
timestampTime
T@\"MSOID\",R
T@\"NSArray\",R,V_signers
T@\"NSData\",&,V_nonce
containingSignedData
getAttributesWithType:protectedAttributes:
initWithIdentity:signatureAlgorithm:useIssuerAndSerialNumber:error:
statusString
userInfo
T@\"MSOID\",R,&,V_attributeType
T@\"NSData\",&,V_signedAttrsData
addMultipleSignaturesAttribute
keyEncryptionAlgorithm
setAlgorithmIdentifier:
setIdentifierData:
setMessageDigest:
setOriginatorCertificates:
dataWithLength:
T@\"MSAlgorithmIdentifier\",&,V_keyEncryptionAlgorithm
_identifierData
T@\"NSArray\",&,V_recipientCertificates
T@\"NSData\",&,V_unsignedAttrsData
_algorithmCapabilities
dateWithTimeIntervalSince1970:
initWithExpirationTime:
setContentType:
T@\"NSData\",&,V_encryptionKey
TB,V_useIssuerAndSerialNumber
bulkEncryptDecrypt:algorithm:mode:key:iv:error:
initWithCoder:
initWithEmail:keyEncryptionAlgorithm:
initWithServerURL:chainRequested:
intValue
initWithLength:
key
T@\"NSData\",&,V_userKeyingMaterial
decodeIdentifier:error:
description
isEqualToMessageImprint:error:
sendTimestampFetchAnalyticsEvent:success:error:samplingRate:
setSerialNumberData:
Asn1OID
T@\"NSArray\",&,V_certificates
_chainMode
_type
capabilities
initWithEncryptionAlgorithm:
isImplementedInObjectiveC
setXpcSession:
_encryptionKey
encodeSignerInfo:error:
initHybridSignatureOIDWithDigestAlgorithm:error:
initWithHashAgilityValues:
originatorPubKey
parseTSAFromGeneralName:
setVerifySignatures:
timeZoneWithName:
T@\"MSCMSSignedData\",W,V_containingSignedData
initWithTimestampToken:error:
setSignedAttrsHash:
setTimestamp:
setUnsignedAttrsData:
setVerifySigners:
superclass
verifyTime:
tsa
TB,V_verifySigners
appendString:
initWithIdentity:
initWithMessageImprint:
signatureCalculated
stringByAppendingFormat:
_expirationTime
initWithCertificate:error:
initWithCertificate:signatureAlgorithm:useIssuerAndSerialNumber:error:
initWithDataContent:error:
status
validateTimestampRequestData:
T@\"MSAlgorithmIdentifier\",&,N,V_bodyHashAlgorithm
_parameters
addCounterSignerCertificates:mode:error:
initWithOID:
invertedSet
removeSignersWithCertificate:error:
setMessageImprint:
setNonce:
T@\"NSData\",R,V_parameters
T@\"NSDate\",&,V_fetchStartTime
numberWithInt:
setIssuerNameData:
timeZoneForSecondsFromGMT:
_timeStampToken
_tsaPolicyID
initWithAttributeStruct:error:
initWithDomain:code:userInfo:
recipients
self
serialNumber
setUserKeyingMaterial:
_originatorIdentity
buildTimestampRequest
calculateSignerInfoDigest:
setContainingSignerInfo:
signingCertificate
T@\"NSArray\",&,V_encryptedKeys
T@\"MSOID\",N,&,VcontentType
TQ,V_chainMode
_digestAlgorithm
_encryptedContent
addSigner:withChainMode:error:
setOriginatorPubKey:
ECSignatureOIDWithDigestAlgorithm:error:
URLWithString:
_unsignedAttrsData
additionalCertificates
appendBytes:length:
arrayWithObject:
localeWithLocaleIdentifier:
originatorCertificates
T@\"MSOID\",N,&,Vtype
encryptDecryptContent:ccOperation:error:
initWithDataContent:isDetached:signer:error:
signerInfo
verifyTimestamp:error:
T@\"MSOID\",N,&,VattributeType
setKey:
_timestampResponse
_userKeyingMaterial
dataWithBytes:length:
initWithFormat:arguments:
_fetchStartTime
TB,V_detached
_cachedTimestampResponse
_verifySigners
boolValue
hashedMessage
initWithCertificate:algorithmCapabilities:originator:
initWithHashAgilityValue:
_attributes
T@\"MSOID\",R,V_algorithm
T@\"MSDecodeOptions\",&,V_options
_signedAttrsData
_signedAttrsHash
createSecCMSSharedInfo:
dictionaryWithCapacity:
ensureXPCSessionExists:
OIDWithData:error:
initWithServerURL:
setIdentity:
signedAttrsHashAlgorithm
signingTime
certReq
firstObject
objectsAtIndexes:
verifySigners
_capabilities
_containingSignedData
_version
encodeBool:forKey:
keySize:
zone
LAContext
T@\"NSData\",&,V_skidData
fetchTimestampWithError:
setOriginator:
timestamp
unsignedIntValue
T@\"NSData\",&,N,V_dataContent
T@\"NSString\",?,R,C
T^{__SecCertificate=},N,V_recipientCertificate
class
encode
expectedHashLength:
initWithIdentity:recipientsAlgorithmCapabilities:error:
T@\"NSData\",&,V_timestampRequest
T@\"NSData\",&,N,V_rawTimestampTokenData
T@\"NSData\",R,V_OIDBytes
calculateSignedAttributesDigest:
code
initWithEmail:signatureAlgorithm:LAContext:error:
T#,R
T@\"NSObject<OS_dispatch_queue>\",&,V_xpcQueue
_verifySignatures
decodeKeyTransRecipientInfo:certificates:LAContext:error:
genericAttributes
initWithAttributeType:values:
numberWithInteger:
retryDelayForAttempt:
T@\"MSCMSMutableAttributeArray\",&,V_unprotectedAttributes
Tq,V_firstRetryErrorCode
setTimeStampTokenData:
verifyCountersignaturesAndCountersignersWithPolicies:verifyTime:anchorCertificates:error:
_issuerNameData
embeddedContent
T@\"MSOID\",&,V_tsaPolicyID
init
rawTimestampTokenData
setLength:
_genericAttributes
_signers
serverURL
setDateStyle:
T^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}},V_encodedAttribute
_signedAttrsHashAlgorithm
autorelease
decodeRecipientInfo:certificates:LAContext:error:
initWithCertificate:signatureAlgorithm:error:
messageDigestAttributeWithDigest:
signatureAlgorithm
verifyWithRequest:policies:error:
T@\"NSMutableArray\",&,V_unprotectedAttributes
T^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}},R,V_asn1AlgId
asMessageSecurityHexString
initWithCertificate:algorithmCapabilities:
mutableBytes
setAttributeDERData:
_signerPolicies
_recipients
_xpcQueue
attributeDERData
attributeType
fetchTimestampWithCompletionBlock:queue:
setChainMode:
setSignerPolicies:
T@\"NSDictionary\",R,&,V_hashAgilityValues
T^{__SecIdentity=},N,V_originatorIdentity
setOptions:
secKeyAlgorithm
T@\"NSData\",&,V_encryptedContent
T@\"NSData\",&,V_LAContext
firstRetryErrorCode
getAttributesWithType:
userKeyingMaterial
T@\"<MSCMSMessage>\",&,V_embeddedContent
T^{__SecCertificate=},N,V_originator
_recipientCertificate
initDigestOIDWithSignatureAlgorithm:error:
setSubjectKeyId:
@48@0:8^{__SecCertificate=}16@24@32^{__SecIdentity=}40
@32@0:8^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}}16^@24
@\"NSDictionary\"
@40@0:8@16@24@32
@\"<MSCMSMessage>\"16@0:8
B24@0:8@16
@\"MSDecodeOptions\"
@16@0:8
B32@0:8@16^@24
v32@0:8Q16@24
B28@0:8B16^@20
@\"<MSCMSMessage>\"
@32@0:8^{__SecCertificate=}16@24
@32@0:8@16^@24
d24@0:8q16
@\"NSObject<OS_dispatch_queue>\"
@28@0:8@16B24
^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}
v16@0:8
@24@0:8@16
@20@0:8B16
Q24@0:8^@16
v40@0:8@16Q24^@32
^{__SecCertificate=}
?
@\"MSAlgorithmIdentifier\"
{heim_oid=Q^I}16@0:8
@\"NSDate\"
^{heim_base_data=Q^v}
^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}}16@0:8
B56@0:8@16@24@32@40^@48
^{_NSZone=}16@0:8
v24@0:8@\"NSData\"16
v24@0:8^{__SecIdentity=}16
@\"NSNumber\"
@32@0:8^{__CFString=}16^@24
^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}
B32@0:8^{MessageImprint={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}16^@24
@44@0:8^{__SecCertificate=}16@24B32^@36
v24@0:8r^{RecipientInfo=i(?={KeyTransRecipientInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}{KeyAgreeRecipientInfo=i{OriginatorIdentifierOrKey=i(?={IssuerAndSerialNumber={heim_base_data=
^{__CFData=}32@0:8@16B24B28
@48@0:8@16q24@32@40
v24@0:8^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}16
@\"NSData\"16@0:8
Vv16@0:8
@\"NSSet\"
^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}}
v20@0:8B16
q
B40@0:8@16@24^@32
v20@0:8i16
@52@0:8@16B24@28Q36^@44
@40@0:8@\"NSData\"16@\"MSDecodeOptions\"24^@32
v24@0:8^{__SecCertificate=}16
^{__CFData=}24@0:8@16
{heim_oid=\"length\"Q\"components\"^I}
I24@0:8^@16
@64@0:8@16q24Q32@40@48*56
B24@0:8:16
@40@0:8^{__SecCertificate=}16@24@32
@44@0:8^{__SecIdentity=}16@24B32^@36
@\"<MSCMSAttributeCoder>\"32@0:8@\"MSCMSAttribute\"16^@24
@\"MSCMSTimestampAttributeInternal\"
@32@0:8^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}16^@24
@24@0:8^{GeneralName=i(?={GeneralName_otherName={heim_oid=Q^I}{heim_base_data=Q^v}}{heim_base_data=Q^v}{heim_base_data=Q^v}{GeneralName_directoryName=i(?={RDNSequence=I^{RelativeDistinguishedName}})}{heim_base_data=Q^v}{heim_base_data=Q^v}{
@52@0:8@16B24@28@36^@44
Q
@40@0:8@16@24^{heim_base_data=Q^v}32
q24@0:8^{PKIFailureInfo=b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1}16
^{__SecCertificate=}32@0:8Q16^@24
@56@0:8@16q24Q32@40@48
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16@0:8
@40@0:8:16@24@32
@\"NSString\"16@0:8
B
@40@0:8@16Q24@32
v24@0:8@16
v24@0:8q16
^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}}
@\"MSCMSAttribute\"24@0:8^@16
@40@0:8^{__SecIdentity=}16@24^@32
v44@0:8@16B24@28d36
B24@0:8^@16
v32@0:8@16Q24
@24@0:8^@16
@24@0:8@\"NSCoder\"16
v24@0:8^{MessageImprint={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}16
@\"MSMessageImprint\"
@\"MSPKIStatusInfo\"
i16@0:8
v24@0:8^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}}16
@48@0:8@16@24Q32^@40
v32@0:8^{__SecCertificate=}16^@24
B24@0:8^{__SecCertificate=}16
v32@0:8@16^@24
B16@0:8
@24@0:8^{__SecCertificate=}16
v32@0:8^{__SecIdentity=}16^@24
@32@0:8^{__SecCertificate=}16^@24
@32@0:8@16@24
@\"MSOID\"16@0:8
Q16@0:8
v24@0:8@\"MSOID\"16
@32@0:8^{heim_base_data=Q^v}16^@24
@24@0:8^{__SecIdentity=}16
v24@0:8^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}}16
^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}16@0:8
@\"MSOID\"
@24@0:8:16
@48@0:8^{RecipientInfo=i(?={KeyTransRecipientInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}{KeyAgreeRecipientInfo=i{OriginatorIdentifierOrKey=i(?={IssuerAndSerialNumber={heim_base_data=Q
@28@0:8^{__SecCertificate=}16B24
r^{ccdigest_info=QQQQ*^v^?^?i^?}16@0:8
@\"NSURL\"
@\"NSMutableSet\"
B32@0:8^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}16^@24
@56@0:8@16@24@32@40^@48
@32@0:8@16Q24
@40@0:8^{__SecCertificate=}16@24^@32
^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}
@\"NSArray\"
@24@0:8^{MessageImprint={AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}16
@24@0:8Q16
@\"MSTimestampResponse\"
#16@0:8
^{__CFString=}16@0:8
v24@0:8@\"NSCoder\"16
v24@0:8^{heim_base_data=Q^v}16
@48@0:8^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}}16@24@32^@40
@32@0:8:16@24
@\"NSString\"
@44@0:8q16@24q32B40
B40@0:8@16Q24^@32
@44@0:8@16B24@28^@36
@48@0:8@16@24@32^@40
^{__SecTrust=}32@0:8@16^@24
^{__SecTrust=}48@0:8@16@24@32^@40
v24@0:8^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v}16
^{__SecIdentity=}16@0:8
@\"NSData\"
q16@0:8
@\"NSObject<OS_xpc_session>\"
@\"MSCMSMutableAttributeArray\"
v24@0:8@\"<MSCMSMessage>\"16
B24@0:8@\"Protocol\"16
@40@0:8^{__SecCertificate=}16@24^{__SecIdentity=}32
^{__SecIdentity=}
Q24@0:8@16
@\"MSCMSSignerInfo\"
v32@0:8@?16@24
@36@0:8@16@24B32
v32@0:8@16@24
B24@0:8#16
B40@0:8@16^{RecipientInfo=i(?={KeyTransRecipientInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}}{KeyAgreeRecipientInfo=i{OriginatorIdentifierOrKey=i(?={IssuerAndSerialNumber={heim_base_dat
v48@0:8q16q24@32@?40
^{heim_base_data=Q^v}16@0:8
B48@0:8@16@24@32^@40
@\"NSMutableArray\"
@52@0:8I16I20I24@28@36^@44
@32@0:8^{__SecIdentity=}16^@24
@40@0:8@16@24^@32
^{__SecCertificate=}16@0:8
^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}16@0:8
v48@0:8@16@24@32@?40
v24@0:8Q16
@36@0:8@16I24^@28
@32@0:8^{heim_oid=Q^I}16^@24
@\"MSCMSSignedData\"
^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}}16@0:8
i
@\"NSData\"24@0:8^@16
invalid CMS Identifier choice
unable to find identity matching %@
Timestamp request data does not match
Self timestamp response has nil parameter
default
SignedData does not contain encapsulated content (TSTInfo)
  TimeStampToken: (nil)\n
MSErrorTrustDomain
2.16.840.1.101.3.4.1.6
missing or invalid OID string %@
<MSTimestampRequest:\n
Version mismatch
reqPolicyOIDString
Failed to decode TSTInfo: ASN.1 error %d
unable to access the content encryption key
unable to create trust object due to security error
https://timestamp.apple.com/tsa-mldsa87-rsa3072-pss-sha512
MessageImprint pointer cannot be NULL
<MSTimestampRequest: %p>\n
unable to decode data content (%ld bytes)
1.2.840.10045.4.3.4
2.16.840.1.101.3.4.1.45
Fail info presence mismatch
invalid Time choice in Signing Time
trust evaluation of signer failed
system-keychain
Could not sign data: no signature algorithm
1.3.6.1.5.5.7.6.52
XPC communication error: %s
Revocation warning
hashedMessage
Failed to decode timestamp token as MSTimestampResponse
Timestamp token signature and certificate verification failed
unable to decode ContentType
unable to decode signerInfo in countersignature
1.2.840.113549.1.7.5
Status %ld
BundledSKID
%s did not find IssuerAndSerialNumber %@ %@
(not set)
TSA policy OID mismatch
Other message imprint has nil parameter
unable to build chain according to mode; could not evaluate trust
Unable to allocate attribute array
v24@?0@\"MSOID\"8^B16
yyyyMMddHHmmss'Z'
MSErrorCMSDomain
valueForBooleanDefault
  Nonce Length: %lu bytes
Not a Countersignature attribute according to AttributeType
unable to get contentType from envelopedData.encryptedContentnInfo
failed to get public key from certificate
internal asn1 error
-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:]
decode failed for recipientInfo (rid vs encryptedKey count)
1.2.840.113549.1.1.11
1.2.840.113549.3.2
http://timestamp.apple.com/ts-ec
TimeStampToken is not SignedData
unable to add signer cert to certificates; missing signer info or signer certificate missing from signer info
2.16.840.1.101.3.4.2.1
@\"NSObject<OS_xpc_object>\"8@?0
  Status String: %@\n
  Serial Number: %@ (%lu bytes)\n
unable to decode Signing Time value
ASN1_BAD_FORMAT
Cannot encode signed attributes: no SignedData
MessageSecurity/MSCMSAuthEnvelopedData.swift
2.16.840.1.101.3.4.1.47
Unable to encode signedData: no signers and not certs-only message
com.apple.messagesecurity
decode failed for recipientInfo (originator)
NO
unable to decode CMS Identifier tag
1.2.840.113549.1.7.2
http://timestamp.apple.com/ts01
fetch
errorCode
timestampResponse
v32@?0@\"MSCMSSignerInfo\"8Q16^B24
Failed encoding type SMIMEEncryptionKeyPreference
ASN1_MISPLACED_FIELD
Encryption Key Preference Attribute should only have one value
Failed encoding type AppleAgileHash
unable to decode envelopedData.originatorInfo
failed to set verification time
com.apple.messagesecurity.MSCMSContentError
InvalidContentTypeOID
2.16.840.1.101.3.4.1.1
  Nonce: %@ (%lu bytes)\n
Failed encoding type AppleHashAgilityValue
counter signer has no reference to a signer with a signature
INVALID_OID
Could not sign data: no key or certificate specified
Signer has no signature algorithm
Invalid OID string format
1.2.840.113549.1.9.4
%d
Could not decode message-digest attribute
AuthEnvelopedData
timestamp.apple.com
2.16.840.1.101.3.4.1.46
Other message imprint has unsupported hash algorithm
CMSIdentifer has unknown type: %d
unable to encode signed attributes
ASN1_INDEF_EXTRA_DATA
unable to find a certificate matching the signer
SecKeyAlgorithm %@ does not indicate a signature algorithm
Certificate request flags do not match
Unable to decode
1.2.840.113549.1.9.16.1.4
unable to verify countersigner %lu
unable to verify timestamp signature because there are no timestamps
1.2.840.113549.1.1.12
2.16.840.1.101.3.4.1.26
Failed to create Apple timestamp policy
Message-digest attribute failed to verify
ASN1_TYPE_MISMATCH
ASN1_OVERFLOW
1.2.840.10045.4.3.1
1.2.840.113549.1.1.7
could not parse OID into string
Unable to encode signedData: unable to allocate digest algorithm array
MSOID %@ does not indicate a digest algorithm
hasFailInfo
timeStampTokenData
v32@?0@8Q16^B24
Algorithm identifiers do not match
  Hash: %@ (%lu bytes)
unable to decode CMS Identifier
signer index, %lu, out of range of signer count, %lu
Unable to encode signedData: missing digest algorithm and not certs-only message
MSErrorCryptoDomain
com.apple.messagesecurity.MSCMSContentTypeError
Granted with modifications
CMSIdentifier has inconsistent type and stored values: expected issuerAndSerialNumber
decode failed for signedData due to RFC 5652 violation
1.2.840.113549.1.9.6
BundledSN
Missing algorithm OID
com.apple.MessageSecurity.MSTimestampXPCService
Failed to create XPC session: %s
Request contained nonce but response does not
the Encryption Key Preference Attribute did not match any certificates
RecipientInfo not found
MessageSecurity.MSCMSTimestampAttributeInternal
2.16.840.1.101.3.4.2.2
elapsed_ms
Revocation notification
SHA-384
ASN1_INDEF_OVERRUN
ASN1 success
ASN1 encoding error
Timestamp response does not contain a message imprint
Granted
ContentType attribute contains more than one value
unable to add recipient
Could not sign data: no private key
Unable to encode SignerInfo: missing signer certificate
Failed to decode TimeStampResp: ASN.1 error %d
Failed encoding type OriginatorInfo
Unable to encode compressed data
Other message imprint cannot be nil
CMSIdentifier has inconsistent type and stored values: expected subjectKeyId
%@:%@ 
unable to find a certificate matching the recipient
1.2.840.113549.1.9.16.3.7
  Request Certificates: %@\n
v24@?0@\"MSAlgorithmIdentifier\"8^B16
Unable to encode signedData: failed to encode a SignerInfo
decode failed due to signer verification failure
unknown keySize -- unexpected encryption algorithm: %@
version
certReq
ASN1_OVERRUN
Unable to encode enveloepd data
Unable to decode the content encryption key
1.2.840.10045.4.3.2
2.16.840.1.101.3.4.1.41
Self timestamp request has nil parameter
unable to decode SKID Identifier
Unable to encode signedData: id-data content type and no data content
Failed encoding type CMSSignedData
Failed encoding type MessageDigest
ASN1_BAD_LENGTH
decode failed for recipientInfo (keyEncryptionAlgorithm)
2.16.840.1.101.3.4.1.25
Timestamp request was not granted. Status: %ld
%@ is not a supported digest algorithm
NOT_NULL
INVALID_ISSUER
Could not decode content-type attribute
Unable to verify
  Nonce: (none)\n
Not a MessageDigest attribute according to AttributeType
Missing value for Multiple Signatures attribute
yyMMddHHmmss'Z'
Signed content-type attribute does not match content-type in signedData
2.16.840.1.101.3.4.1.27
Not a ContentType attribute according to AttributeType
ASN1_INDEF_UNDERRUN
unable to compute digest for signature
Unable to encode
Unknown error
  Response Size: %lu bytes
Unable to encode signedData: content is not detached and no content specified
v32@?0@\"MSCMSCounterSignerInfo\"8Q16^B24
unable to create timestamp attribute for timestamp %lu
Failed encoding type AlgorithmIdentifier
2.16.840.1.114027.80.9.1.15
%@
Failed to create XPC session
  TimeStampToken: Present\n
MSCMSAppleTimestampAttribute: no timestamp token data to encode
ASN1_BAD_ID
1.2.840.113549.1.1.4
1.3.14.3.2.6
responseObject
ContentInfo
MD5 is not supported for signing
Other timestamp request has nil parameter
  Failure Info: %ld\n
Unknown ASN1 error
Invalid parameter
1.2.840.113549.1.1.14
retry_count
Message imprint cannot be nil
timestamp verification failed for signer %lu
<MSMessageImprint: %p>\n
Failed encoding type SignerInfo
.
unable to copy OID
Not an Expiration Time attribute according to AttributeType
Unable to get serial number from certificate
\xd1
unable to decode CMSAttributes
1.2.840.113549.1.9.16.2.11
unable to find any certificates in keychain
ASN1_PARSE_ERROR
ASN1_MAX_CONSTRAINT
EnvelopedData
Algorithm Identifier %@ does not indicate a public key algorithm
v32@?0@\"<MSCMSAttributeCoder>\"8Q16^B24
v32@?0@\"NSData\"8Q16^B24
decode failed for recipientInfo due to RFC 5652 violation (version)
decode failed for recipientInfo (rid)
TSA policy OIDs do not match
signedData contains content but has no signers
unable to decode Encryption Key Preference Attribute
QueryIssuer
unable to decode envelopedData.unprotectedAttrs
Invalid content type
Failed encoding type ContentInfo
Not an SMIMECapabilities attribute according to AttributeType
unable to get certificate from provided identity
MessageSecurity.MSCMSCompressedData
.%u
Failed encoding type TimeStampReq
\n--- Additional Debug Info ---\n
musr
1.2.840.113549.2.5
first_error_code
  Status: %@\n
unable to decode signedData (%ld bytes)
1.2.840.113549.1.9.15
Apple Hash Agility V2 Attribute must have one value
unknown ccAlg -- unexpected encryption algorithm: %@
1.3.6.1.5.5.7.3.8
  Message Imprint: (none)\n
Not an Encryption Key Preference attribute according to AttributeType
ASN1_BAD_CHARACTER
no certificates found in signerInfo for trust evaluation
1.2.840.113635.100.9.3
Unable to encode SignerInfo: missing destination address
init()
com.apple.messagesecurity.mstimestamp.fetchTimestampWithError_success
1.2.840.113549.1.9.16.3.6
  Policy OID: %@\n
unable to decode Apple Hash Agility V2 Agile Hash
No certificate for identity 
requestObject
Signing Time Attribute MUST have a single signed attribute value
TSTInfo data is nil
  Policy: (none)\n
Other timestamp response has nil parameter
  Hash: (empty)
MSTimestampErrorDomain
UnknownContentTypeOID
underlying_error_domain
No timestamp server URL specified
2.16.840.1.101.3.4.1.22
TimeStampToken data is nil
Waiting
unable to decode Multiple Signatures attribute
ASN1_GOT_BER
%@ is not a supported signature algorithm
unable to decode envelopedData (%ld bytes)
Not a Signing Time attribute according to AttributeType
logCMSDecodingFailures
Failed encoding type CMSRC2CBCParameter
1.2.840.113549.1.1.5
2.16.840.1.101.3.4.1.21
  Request Size: %lu bytes\n
TSA mismatch
Invalid MessageImprint data
Failed encoding type CMSIdentifier
Apple Hash Agility Attribute should only have one value
Missing or too many content-type attribute(s)
B32@?0@\"<MSCMSAttributeCoder>\"8Q16^B24
unable to get private key from provided identity
v32@?0@\"NSSet\"8Q16^B24
Failed encoding type DataContent
unable to build chain according to mode; missing signer info or signer certificate missing from signer info
signer has no reference to a signedData with content
ASN1_GOT_INDEFINITE
1.2.840.113549.1.9.16.1.23
nonce
unable to find any identities in keychain
ASN1_INVALID_CHOICE
com.apple.messagesecurity.mstimestamp.fetchTimestampWithCompletionBlock_success
unable to decode Apple Hash Agility Attribute
2.16.840.1.101.3.4.2.3
  Algorithm OID: %@
id-aa-timeStampToken attribute has %lu values, expected 1
QuerySKID
; 
Nonce values do not match
QuerySN
Unable to get issuer sequence from certificate
2.16.840.1.101.3.4.1.42
success
Failed to allocate memory for OID components
errorDescription
findCertificateBySubjectKeyID
Other timestamp request cannot be nil
  TSA: %@\n
unknown type for Encryption Key Preference Attribute
Request policy OID mismatch
  Gen Time: %@ UTC\n
signer verification failed for signer %lu
MSErrorKeychainDomain
Failed to decode TimeStampToken as ContentInfo
Self message imprint has nil parameter
  Serial Number: (none)\n
MessageDigest attribute contains more than one value
Failed encoding type ContentType
0x%02x,
1.2.840.113549.1.7.1
B32@?0@\"NSString\"8Q16^B24
signer is missing signature
Could not sign data: no digest
underlying_error_code
failed to set anchor certificates
underlyingErrorCode
Unable to encode signedData: embedded content type specified and no embedded content
Unable to encode signedData: unable to allocate certificates array
unable to set verify date on trust object
Could not sign data: no identity in keychain for certificate
1.2.840.113549.1.7.3
2.16.840.1.101.3.4.2.4
Server URL mismatch
failInfo
Self message imprint has unsupported hash algorithm
<MSMessageImprint:\n
Not a Multiple Signatures attribute according to AttributeType
TimeStampToken error
algorithmParameters
3
Unable to encode signedData: missing digest algorithms
unknown ccMode -- unexpected encryption algorithm: %@
could not parse OID into parts %@
YES
Unknown
unable to get contentType from signedData
Failed encoding type CMSOrderedAttributes
Expiration Time Attribute MUST have a single signed attribute value
com.apple.HeimASN1
1.3.14.3.2.26
decode failed due to signature verification failure
Failed encoding type MultipleSignatures
signer has no signature algorithm
MessageSecurity.MSCMSEnvelopedDataInternal
DataContent
Underlying ASN1 error 
Status mismatch
Status string mismatch
Message imprint presence mismatch
unable to allocate Attribute
invalid Time choice in Expiration Time
MSErrorAllocationDomain
MSErrorASN1Domain
%02X
1.2.840.113549.1.1.1
Timestamp mismatch
<MSTimestampResponse: %p>\n
Missing or too many message-digest attribute(s)
unable to verify countersignature(s) for countersigner %lu
MSDecryptGCM error: %d
Rejection
Failed encoding type CMSAttributes
unable to copy Attribute
1.2.840.10045.4.1
could allocate OID components
Version numbers do not match
Timestamp response data mismatch
Unable to encode content info: missing content type or content
-[MSCMSTimestampAttribute initWithTimestampToken:]
1.3.14.3.2.7
could not parse OID into data
0123456789.
  Policy: %@\n
1.2.840.113549.1.9.2.51
Failed encoding type SecCMS_SMIMEEncryptionKeyPreference
  Server URL: %@
  Gen Time: (none)\n
com.apple.MessageSecurity
SHA-512
Timestamp response is missing message imprint or algorithm
No timestamp request data available
!
UTC
NULL
decode failed for signerInfo due to RFC 5652 violation (version)
Unable to encode RecipientInfo: missing destination address
en_US_POSIX
BundledIssuer
unable to find certificate by identifier; invalid choice in encoding
unable to decode envelopedData.recipientInfos
MessageSecurity.MSCMSAuthEnvelopedData
SMIME Capabilities Attribute should only have one value
unable to find any identities with email address %@
| 
SignedData error
Unable to decode comrpessed data
unknown blockSize -- unexpected encryption algorithm: %@
v8@?0
1.2.840.113549.1.9.3
unable to create countersignature attribute for countersigner %lu
unable to create trust object
Nonce mismatch
unable to encrypt/decrypt the content
2.16.840.1.101.3.4.1.7
ASN1_EXACT_CONSTRAINT
--- Basic Info ---\n
No timestamp response data to parse
unable to decode Expiration Time value
No digest algorithm specified
findCertificateByIssuerAndSerialNumber
ASN1_EXTRA_DATA
error_code
no signer with input certificate hash
Unknown content type
unable to decode Algorithm Identifier
com.apple.MSTimestampXPCService.queue
statusString
1.2.840.113635.100.9.1
unable to find any certificates with email address %@
UNEXPECTED_VALUE
MessageSecurity/MSCMSAttribute.swift
Fail info mismatch
countersignature verification failed for signer %lu
Failed encoding type SMIMECapabilities
MSTimestampHTTPErrorDomain
Unable to decode AuthEnvelopedData
timestamp_server
SHA-1
  Algorithm: %@\n
Unable to encrypt
v32@?0@\"MSOID\"8Q16^B24
Failed to unarchive timestamp response
Timestamp request cannot be nil
algorithmOIDString
B32@?0@\"MSCMSSignerInfo\"8Q16^B24
%s did not find SubjectKeyIdentifier %@
underlyingErrorDomain
1.2.840.113549.3.7
SHA-256
1.2.840.113549.1.7.6
failed to create signerInfo object for signer %u
ASN1_MISSING_FIELD
countersigner verification failed for signer %lu
unable to decode MessageDigest
1.2.840.113635.100.9.2
unable to verify timestamp signature for timestamp %lu
decode failed due to timestamp verification failure
unable to decode SMIME Capabilities Attribute
findIdentityByCertificate
messageImprint
(nil)
Unable to encode signedData: missing content type
Unable to encode signedData: unable to allocate signerInfos array
Unable to decode OriginatorInfo
1.2.840.113549.1.9.16.1.9
1.3.133.16.840.63.0.2
No key for identity 
v24@?0@\"NSObject<OS_xpc_object>\"8@\"NSObject<OS_xpc_object>\"16
status
Failed to extract TSTInfo from SignedData
CMSSignedData
1.2.840.113549.1.9.16.2.14
Failed to create message imprint for timestamp verification
Failed encoding type CMSCBCParameter
1.2.840.113549.1.1.13
2.16.840.1.101.3.4.1.5
unable to allocate Algorithm Identifier
  Version: %ld\n
Other timestamp response cannot be nil
2.16.840.1.101.3.4.1.2
MSOID %@ does not indicate a signature algorithm
messageType
timestampServer
>
<MSTimestampResponse:\n
%u.%u
unable to copy Algorithm Identifier
  Message Imprint: %@\n
ASN1_BAD_TIMEFORMAT
1.2.840.10045.2.1
Invalid OID component at index %lu: value %ld is out of valid range [0, %u]
No response object in XPC reply
Error Unavailable
Content-type attribute must not be present in Countersignature
unable to decode content info (%ld bytes)
CommonCrypto error 
1.2.840.10045.4.3.3
signature verification failed for signer %lu
ASN1_MIN_CONSTRAINT
Timestamp token SignedData not available for verification
1.2.840.113549.1.9.5
1.2.840.113549.1.9.16.1.2
1.2.840.113635.100.9.4.1
\n
Serial number mismatch
Hashed messages do not match
%{public}@
QuerySKID = %{mask.hash}@
BundledSKID = %{mask.hash}@
failed to set credential reference on signer public key: %@
Invalid data - aes-ICVlen is negative or too large
Failed to encode TimeStampReq: %@
signedData contains embedded content but signer %lu does not have signed attributes.
MSCMSAppleTimestampAttribute: failed to create MSTimestampResponse from token data
Found unimplemented contented type: EncryptedData
Invalid data - AES-GCM algorithm identifier carries no parameters
Error encrypting underlying crypto error %d
MSTimestampRequest: Retryable error (attempt %ld/%ld): %@
Failed to parse hash algorithm OID: %@
MSTimestampRequest: Completion block is required
no countersignatures, returning successful verification
Invalid data - error decoding AuthEnvelopedData
No certificates in SignedData
BundledSN = %{mask.hash}@
found %lu valid email candidate certs
Invalid data - Error encoding GCM parameters
aes-ICVlen %ld does not match mac length %ld
MSCMSRecipientInfo requires an originator identity for an EC recipient. Encode will fail if not set.
MSCMSChainMode with chain specified, but no trusted chain found (%@), continuing with untrusted chain
Found unsupported content type: DigestedData
QuerySN = %{mask.hash}@
BundledIssuer = %{mask.hash}@
failed to add recipient. No shared encryption algorithm with the rest of the recipients
no timestamps, returning successful verification
No recipient found
MSTimestampResponse initWithTimestampToken: failed to parse token: %@
Invalid input data/embedded data
Invalid data - error encoding AuthEnvelopedData
Unable to generate key underlying crypto error %d
failed to set credential reference on signer private key: %@
MSCMSRecipientInfo init encryption algorithm %@ not permitted for certificate key type %ld
Failed to build MessageImprint for TimeStampReq: %@
MSTimestampResponse initWithTimestampToken: Cannot initialize with nil token data
Failed to encode TimeStampToken: %@
Digest length %lu is not a supported length
found %lu candidate email certs from keychain
%s %s isInternal: %d val: %s isForced: %d appVal: %s result: %d
recipientInfo violates RFC 5652 (key usage)
QueryIssuer = %{mask.hash}@
Unable to generate nonce underlying crypto error %d
Invalid AES-GCM tag length %ld, RFC 5084 requires 12 to 16 octets
MSTimestampRequest: Failed to unarchive response: %@
Invalid encryption algorithm %u
Error decrypting encoded content
Invalid data - error decoding OriginatorInfo
Error decrypting underlying crypto error %d
MSCMSChainMode with chain specified, but could not build chain beyond leaf, continuing with single certificate
skipping non-certificate CertificateChoice at %u
Error extracting MAC
Invalid input algorithm %u
TimeStampToken has no signers
TimeStampToken has multiple signers (%lu), RFC 3161 requires exactly one
No certificate with id-kp-timeStamping EKU found in certificate chain
unable to parse certificate at %u
MSTimestampResponse: Failed to parse timestamp response: %@
Failed to archive MSTimestampRequest: %@
found %lu candidate certs from keychain with matching email addresses
logging %s 0x%zx [%ld-%ld)/%ld %s
Found unknown content type: %@
failed to decode recipient %u: %@
Bad signature algorithm %@. Trying to compose signature algorithm from %@ and digest %@
Invalid data - no certificate in originatorCertificates
Invalid data - error decoding GCMParameters
Invalid data - originatorInfo has no certificates
Invalid AES-GCM nonce length %ld, expected 12 to 16 octets
MSTimestampRequest: Queue is required
Found unsupported content type: AuthenticatedData
Invalid data - no recipients found
MSCMSRecipientInfo %s: Unsupported certificate key type
%s failed with %@
MSCMSSignerInfo init signature aglorithm %@ not permitted for certificate key type %ld
Error: SignedData contentType is %@ (expected %@)
MSTimestampResponse: Cannot initialize with nil timestamp response data
Failed to parse TSA policy OID: %@
```
