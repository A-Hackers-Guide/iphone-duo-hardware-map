# `/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`

iOS 27.2 dyld shared cache image. Version `341.40.12.0.0`. **[DSC]**

## Linked libraries (14)

- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/Security.framework/Security`
- `/usr/lib/libheimdal-asn1.dylib`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`
- `/usr/lib/swift/libswiftos.dylib`

## Objective-C: 34 classes, 6 protocols, 688 methods, 192 properties

### Class pages

Every class and protocol, with its methods: [`MSAlgorithmIdentifier`](../objc/MSAlgorithmIdentifier_MessageSecurity.md), [`MSCMSAppleExpirationTimeAttribute`](../objc/MSCMSAppleExpirationTimeAttribute_MessageSecurity.md), [`MSCMSAppleHashAgilityAttribute`](../objc/MSCMSAppleHashAgilityAttribute_MessageSecurity.md), [`MSCMSAppleHashAgilityV2Attribute`](../objc/MSCMSAppleHashAgilityV2Attribute_MessageSecurity.md), [`MSCMSAppleTimestampAttribute`](../objc/MSCMSAppleTimestampAttribute_MessageSecurity.md), [`MSCMSAttribute`](../objc/MSCMSAttribute_MessageSecurity.md), [`MSCMSAttributeCoder`](../objc/MSCMSAttributeCoder_MessageSecurity.protocol.md), [`MSCMSAuthEnvelopedData`](../objc/MSCMSAuthEnvelopedData_MessageSecurity.md), [`MSCMSCompressedData`](../objc/MSCMSCompressedData_MessageSecurity.md), [`MSCMSContentInfo`](../objc/MSCMSContentInfo_MessageSecurity.md), [`MSCMSContentTypeAttribute`](../objc/MSCMSContentTypeAttribute_MessageSecurity.md), [`MSCMSCounterSignerInfo`](../objc/MSCMSCounterSignerInfo_MessageSecurity.md), [`MSCMSCountersignatureAttribute`](../objc/MSCMSCountersignatureAttribute_MessageSecurity.md), [`MSCMSEncryptionKeyPreferenceAttribute`](../objc/MSCMSEncryptionKeyPreferenceAttribute_MessageSecurity.md), [`MSCMSEnvelopedData`](../objc/MSCMSEnvelopedData_MessageSecurity.md), [`MSCMSEnvelopedDataInternal`](../objc/MSCMSEnvelopedDataInternal_MessageSecurity.md), [`MSCMSIdentifier`](../objc/MSCMSIdentifier_MessageSecurity.md), [`MSCMSMessage`](../objc/MSCMSMessage_MessageSecurity.protocol.md), [`MSCMSMessageDigestAttribute`](../objc/MSCMSMessageDigestAttribute_MessageSecurity.md), [`MSCMSMultipleSignaturesAttribute`](../objc/MSCMSMultipleSignaturesAttribute_MessageSecurity.md), [`MSCMSMutableAttributeArray`](../objc/MSCMSMutableAttributeArray_MessageSecurity.md), [`MSCMSRecipientInfo`](../objc/MSCMSRecipientInfo_MessageSecurity.md), [`MSCMSSMIMECapabilitiesAttribute`](../objc/MSCMSSMIMECapabilitiesAttribute_MessageSecurity.md), [`MSCMSSignedData`](../objc/MSCMSSignedData_MessageSecurity.md), [`MSCMSSignerInfo`](../objc/MSCMSSignerInfo_MessageSecurity.md), [`MSCMSSigningTimeAttribute`](../objc/MSCMSSigningTimeAttribute_MessageSecurity.md), [`MSCMSTimestampAttribute`](../objc/MSCMSTimestampAttribute_MessageSecurity.md), [`MSCMSTimestampAttributeInternal`](../objc/MSCMSTimestampAttributeInternal_MessageSecurity.md), [`MSDecodeOptions`](../objc/MSDecodeOptions_MessageSecurity.md), [`MSError`](../objc/MSError_MessageSecurity.md), [`MSMessageImprint`](../objc/MSMessageImprint_MessageSecurity.md), [`MSOID`](../objc/MSOID_MessageSecurity.md), [`MSPKIStatusInfo`](../objc/MSPKIStatusInfo_MessageSecurity.md), [`MSTimestampRequest`](../objc/MSTimestampRequest_MessageSecurity.md), [`MSTimestampResponse`](../objc/MSTimestampResponse_MessageSecurity.md), [`MessageSecurityMessage`](../objc/MessageSecurityMessage_MessageSecurity.protocol.md), [`NSCoding`](../objc/NSCoding_MessageSecurity.protocol.md), [`NSObject`](../objc/NSObject_MessageSecurity.protocol.md), [`NSSecureCoding`](../objc/NSSecureCoding_MessageSecurity.protocol.md)

### Classes

`MSAlgorithmIdentifier`, `MSCMSAppleExpirationTimeAttribute`, `MSCMSAppleHashAgilityAttribute`, `MSCMSAppleHashAgilityV2Attribute`, `MSCMSAppleTimestampAttribute`, `MSCMSAttribute`, `MSCMSAuthEnvelopedData`, `MSCMSCompressedData`, `MSCMSContentInfo`, `MSCMSContentTypeAttribute`, `MSCMSCounterSignerInfo`, `MSCMSCountersignatureAttribute`, `MSCMSEncryptionKeyPreferenceAttribute`, `MSCMSEnvelopedData`, `MSCMSEnvelopedDataInternal`, `MSCMSIdentifier`, `MSCMSMessageDigestAttribute`, `MSCMSMultipleSignaturesAttribute`, `MSCMSMutableAttributeArray`, `MSCMSRecipientInfo`, `MSCMSSMIMECapabilitiesAttribute`, `MSCMSSignedData`, `MSCMSSignerInfo`, `MSCMSSigningTimeAttribute`, `MSCMSTimestampAttribute`, `MSCMSTimestampAttributeInternal`, `MSDecodeOptions`, `MSError`, `MSMessageImprint`, `MSOID`, `MSPKIStatusInfo`, `MSTimestampRequest`, `MSTimestampResponse`, `NSData`

### Protocols

`MSCMSAttributeCoder`, `MSCMSMessage`, `MessageSecurityMessage`, `NSCoding`, `NSObject`, `NSSecureCoding`

### Properties

```
@property (T@"MSOID",R,&) attributeType;
@property (T@"MSOID",R) type;
@property (T@"NSData",&,N) dataContent;
@property (T@"<MSCMSMessage>",&) embeddedContent;
@property (T@"MSOID",&) contentType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (class, TB,R) supportsSecureCoding;
@property (T^{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}},R,V_asn1AlgId) asn1AlgId;
@property (T@"MSOID",R,V_algorithm) algorithm;
@property (T@"NSData",R,V_parameters) parameters;
@property (T@"NSDate",R,&,V_expirationTime) expirationTime;
@property (T@"MSOID",R,&) attributeType;
@property (T@"NSData",R,&,V_hashAgilityValue) hashAgilityValue;
@property (T@"MSOID",R,&) attributeType;
@property (T@"NSDictionary",R,&,V_hashAgilityValues) hashAgilityValues;
@property (T@"MSOID",R,&) attributeType;
@property (T@"NSData",&,N,V_rawTimestampTokenData) rawTimestampTokenData;
@property (T@"MSTimestampResponse",R) timestampResponse;
@property (T@"NSData",&,V_attributeDERData) attributeDERData;
@property (T^{Attribute={heim_oid=Q^I}{Attribute_value=I^{heim_base_data}}},V_encodedAttribute) encodedAttribute;
@property (T@"MSOID",R,&,V_attributeType) attributeType;
@property (T@"NSArray",R,&,V_attributeValues) attributeValues;
@property (T@"MSOID",N,&,Vtype) type;
@property (T@"NSData",N,C) dataContent;
@property (T@"NSArray",N,C) recipients;
@property (T@"MSOID",N,&,VencryptionAlgorithm) encryptionAlgorithm;
@property (T@"NSArray",N,C) protectedAttributes;
@property (T@"NSArray",N,C) unprotectedAttributes;
@property (T@"NSArray",N,C) originatorCertificates;
@property (T@"MSOID",N,&,VcontentType) contentType;
@property (T@"<MSCMSMessage>",N,&,VembeddedContent) embeddedContent;
@property (T@"MSOID",N,&,Vtype) type;
@property (T@"NSData",N,C) dataContent;
@property (T@"<MSCMSMessage>",N,&,VembeddedContent) embeddedContent;
@property (T@"MSOID",N,&,VcontentType) contentType;
@property (T@"NSData",&,V_content) content;
@property (T@"<MSCMSMessage>",&,V_embeddedContent) embeddedContent;
@property (T@"MSOID",&,V_contentType) contentType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"MSOID",&,V_contentType) contentType;
@property (T@"MSOID",R,&) attributeType;
@property (T@"MSCMSSignerInfo",W,N,V_containingSignerInfo) containingSignerInfo;
@property (TQ,V_chainMode) chainMode;
@property (T@"NSArray",&,V_additionalCertificates) additionalCertificates;
@property (T@"MSCMSSignerInfo",W,N,V_containingSignerInfo) containingSignerInfo;
@property (T@"NSArray",R,V_signers) signers;
@property (T@"MSOID",R,&) attributeType;
@property (T^{__SecCertificate=},R,V_encryptionCertificate) encryptionCertificate;
@property (TB,V_legacyASN1Encoding) legacyASN1Encoding;
@property (T@"MSOID",R,&) attributeType;
@property (T@"NSArray",&,V_recipients) recipients;
@property (T@"NSData",&,V_encryptedContent) encryptedContent;
@property (TB,V_contentChanged) contentChanged;
@property (T@"NSNumber",R,V_version) version;
@property (T@"MSAlgorithmIdentifier",&,V_encryptionAlgorithm) encryptionAlgorithm;
@property (T@"NSData",&,V_encryptionKey) encryptionKey;
@property (T@"NSMutableArray",&,V_unprotectedAttributes) unprotectedAttributes;
@property (T@"NSMutableArray",&,V_originatorCertificates) originatorCertificates;
@property (TB,V_legacyASN1Encoding) legacyASN1Encoding;
@property (T@"MSOID",R,V_type) type;
@property (T@"NSData",&,N,V_dataContent) dataContent;
@property (T@"<MSCMSMessage>",&,V_embeddedContent) embeddedContent;
@property (T@"MSOID",&,V_contentType) contentType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Ti,V_type) type;
@property (T^{IssuerAndSerialNumber={heim_base_data=Q^v}{heim_integer=Q^vi}},V_issuerAndSerialNumber) issuerAndSerialNumber;
@property (T^{heim_base_data=Q^v},V_subjectKeyId) subjectKeyId;
@property (T@"NSData",&,V_skidData) skidData;
@property (T@"NSData",&,V_serialNumberData) serialNumberData;
@property (T@"NSData",&,V_issuerNameData) issuerNameData;
@property (T@"NSData",&,V_messageDigest) messageDigest;
@property (T@"MSOID",R,&) attributeType;
@property (T@"MSCMSSignerInfo",W,N,V_containingSignerInfo) containingSignerInfo;
@property (T@"MSAlgorithmIdentifier",&,N,V_bodyHashAlgorithm) bodyHashAlgorithm;
@property (T@"MSAlgorithmIdentifier",&,N,V_signatureAlgorithm) signatureAlgorithm;
@property (T@"MSAlgorithmIdentifier",&,N,V_signedAttrsHashAlgorithm) signedAttrsHashAlgorithm;
@property (T@"NSData",W,N,V_signedAttrsHash) signedAttrsHash;
@property (T@"MSOID",R,&) attributeType;
@property (T@"NSMutableArray",&,V_attributes) attributes;
@property (T@"NSMutableArray",&,V_genericAttributes) genericAttributes;
@property (T@"NSData",&,V_encodedAttributeSet) encodedAttributeSet;
@property (T@"NSNumber",&,V_version) version;
@property (T@"NSArray",&,V_encryptedKeys) encryptedKeys;
@property (T@"NSData",&,V_userKeyingMaterial) userKeyingMaterial;
@property (T@"NSArray",&,V_algorithmCapabilities) algorithmCapabilities;
@property (T@"MSAlgorithmIdentifier",&,V_keyEncryptionAlgorithm) keyEncryptionAlgorithm;
@property (T^{__SecCertificate=},N,V_recipientCertificate) recipientCertificate;
@property (T@"NSArray",&,V_recipientCertificates) recipientCertificates;
@property (T^{__SecCertificate=},N,V_originator) originator;
@property (T^{__SecIdentity=},N,V_originatorIdentity) originatorIdentity;
@property (T@"NSData",&,V_originatorPubKey) originatorPubKey;
@property (T@"NSSet",R,V_capabilities) capabilities;
@property (T@"MSOID",R,&) attributeType;
@property (T@"NSNumber",&,V_version) version;
@property (T@"NSArray",&,V_signers) signers;
@property (T@"NSSet",&,V_digestAlgorithms) digestAlgorithms;
@property (T@"MSDecodeOptions",&,V_options) options;
@property (TB,V_contentChanged) contentChanged;
@property (TB,V_detached) detached;
@property (T@"NSMutableSet",&,V_certificates) certificates;
@property (T@"MSOID",R) type;
@property (T@"NSData",&,N,V_dataContent) dataContent;
@property (T@"<MSCMSMessage>",&,V_embeddedContent) embeddedContent;
@property (T@"MSOID",&,V_contentType) contentType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T^{__SecKey={__CFRuntimeBase=QAQ}^{__SecKeyDescriptor}^v},V_signerPrivKey) signerPrivKey;
@property (T^{SignerInfo=i{heim_base_data=Q^v}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}^{heim_base_data}{AlgorithmIdentifier={heim_oid=Q^I}^{heim_base_data}}{heim_base_data=Q^v}^{heim_base_data}},V_encodedSignerInfo) encodedSignerInfo;
@property (T^{__SecCertificate=},V_signerCertificate) signerCertificate;
@property (TB,V_useIssuerAndSerialNumber) useIssuerAndSerialNumber;
@property (T@"MSAlgorithmIdentifier",&,V_signatureAlgorithm) signatureAlgorithm;
@property (T@"NSData",&,V_signedAttrsData) signedAttrsData;
@property (T@"NSData",&,V_unsignedAttrsData) unsignedAttrsData;
@property (T@"NSData",&,V_identifierData) identifierData;
@property (T@"NSNumber",&,V_version) version;
@property (T@"MSCMSSignedData",W,V_containingSignedData) containingSignedData;
@property (T@"MSAlgorithmIdentifier",&,V_digestAlgorithm) digestAlgorithm;
@property (T@"NSArray",R) certificates;
@property (TB,V_contentChanged) contentChanged;
@property (TB,R,V_signatureCalculated) signatureCalculated;
@property (T@"MSCMSMutableAttributeArray",&,V_protectedAttributes) protectedAttributes;
@property (T@"NSData",&,N,V_signature) signature;
@property (T@"MSCMSMutableAttributeArray",&,V_unprotectedAttributes) unprotectedAttributes;
@property (T@"NSData",&,V_LAContext) LAContext;
@property (T@"NSDate",R,&,V_signingTime) signingTime;
@property (T@"MSOID",R,&) attributeType;
@property (T@"MSCMSTimestampAttributeInternal",&,V_timestampAttribute) timestampAttribute;
@property (T@"NSURL",&,V_serverURL) serverURL;
@property (TB,V_certChainRequested) certChainRequested;
@property (T@"MSCMSSignerInfo",R,V_signerInfo) signerInfo;
@property (T@"NSArray",R,V_certificates) certificates;
@property (T@"MSOID",R,V_digestAlgorithm) digestAlgorithm;
@property (T@"NSDate",R) timestampTime;
@property (T@"MSOID",R,&) attributeType;
@property (T@"MSOID",N,&,VattributeType) attributeType;
@property (TB,V_verifySignatures) verifySignatures;
@property (TB,V_verifySigners) verifySigners;
@property (TB,V_verifyTimestamps) verifyTimestamps;
@property (T@"NSArray",&,V_signerPolicies) signerPolicies;
@property (T@"NSDate",&,V_verifyTime) verifyTime;
@property (T^{__SecIdentity=},V_identity) identity;
@property (T@"NSData",&,V_key) key;
@property (T@"NSData",&,V_LAContext) LAContext;
@property (T@"NSArray",&,V_additionalCertificates) additionalCertificates;
@property (T@"NSArray",&,V_anchorCertificates) anchorCertificates;
@property (T@"MSAlgorithmIdentifier",&,V_algorithmIdentifier) algorithmIdentifier;
@property (T@"NSData",&,V_hashedMessage) hashedMessage;
@property (T{heim_oid=Q^I},R,V_Asn1OID) Asn1OID;
@property (Tr^{ccdigest_info=QQQQ*^v^?^?i^?},R) ccdigest;
@property (T@"NSData",R,V_OIDBytes) OIDBytes;
@property (T@"NSString",R,V_OIDString) OIDString;
@property (T^{__CFString=},R) secKeyAlgorithm;
@property (Tq,R,V_status) status;
@property (T@"NSString",R,V_statusString) statusString;
@property (Tq,R,V_failInfo) failInfo;
@property (TB,R,V_hasFailInfo) hasFailInfo;
@property (T@"NSData",&,V_nonce) nonce;
@property (TB,V_certReq) certReq;
@property (T@"MSOID",&,V_reqPolicyID) reqPolicyID;
@property (Tq,V_version) version;
@property (T@"MSMessageImprint",&,V_messageImprint) messageImprint;
@property (T@"NSObject<OS_dispatch_queue>",&,V_xpcQueue) xpcQueue;
@property (T@"NSObject<OS_xpc_session>",&,V_xpcSession) xpcSession;
@property (T@"NSData",&,V_timestampRequest) timestampRequest;
@property (Tq,V_retryCount) retryCount;
@property (Tq,V_firstRetryErrorCode) firstRetryErrorCode;
@property (T@"NSDate",&,V_fetchStartTime) fetchStartTime;
@property (T@"NSURL",&,V_timestampServer) timestampServer;
@property (Tq,V_maxRetryAttempts) maxRetryAttempts;
@property (T@"MSMessageImprint",&,V_messageImprint) messageImprint;
@property (T@"NSData",&,V_serialNumber) serialNumber;
@property (T@"NSString",&,V_tsa) tsa;
@property (T@"MSOID",&,V_tsaPolicyID) tsaPolicyID;
@property (Tq,V_version) version;
@property (T@"MSPKIStatusInfo",&,V_status) status;
@property (T@"NSDate",&,V_timestamp) timestamp;
@property (T@"NSData",&,V_nonce) nonce;
@property (T@"MSCMSSignedData",&,V_timeStampToken) timeStampToken;
@property (T@"NSData",&,V_timeStampTokenData) timeStampTokenData;
@property (T@"NSData",&,V_timestampResponse) timestampResponse;
@property (T@"NSArray",&,V_certificates) certificates;
```

## Swift types (27)

`MessageSecurity.MSCMSAuthEnvelopedData:`, `MessageSecurity.MSCMSCompressedData:`, `MessageSecurity.MSCMSContentError`, `MessageSecurity.MSCMSContentTypeError`, `MessageSecurity.MSCMSEnvelopedDataInternal:`, `MessageSecurity.MSCMSError`, `MessageSecurity.MSCMSTimestampAttributeInternal.decodedAttribute`, `MessageSecurity.MSCMSTimestampAttributeInternal:`, `__C.Accuracy`, `__C.AlgorithmIdentifier`, `__C.Attribute`, `__C.Attribute_value`, `__C.Extension`, `__C.Extensions`, `__C.GeneralName`, `__C.GeneralName.__Unnamed_union_u`, `__C.GeneralName_enum`, `__C.MessageImprint`, `__C.RecipientInfo`, `__C.RecipientInfo.__Unnamed_union_u`, `__C.RecipientInfo_enum`, `__C.SecCertificateRef`, `__C.TSTInfo`, `__C.heim_base_data`, `__C.heim_integer`, `__C.heim_oid`, `conformance`

## Strings (612)

```
Missing algorithm OID
Content-type attribute must not be present in Countersignature
NOT_NULL
CommonCrypto error 
2.16.840.1.101.3.4.1.21
2.16.840.1.101.3.4.1.27
TimeStampToken is not SignedData
ASN1 success
underlyingErrorCode
ASN1_BAD_LENGTH
could not parse OID into parts %@
B32@?0@\"MSCMSSignerInfo\"8Q16^B24
unable to create timestamp attribute for timestamp %lu
2.16.840.1.101.3.4.1.46
2.16.840.1.101.3.4.1.47
unable to decode MessageDigest
1.2.840.113549.1.9.16.3.6
first_error_code
--- Basic Info ---\n
unable to build chain according to mode; could not evaluate trust
v24@?0@\"MSOID\"8^B16
Apple Hash Agility V2 Attribute must have one value
Self message imprint has nil parameter
1.2.840.113549.1.9.16.2.14
B32@?0@\"<MSCMSAttributeCoder>\"8Q16^B24
1.2.840.113635.100.9.2
trust evaluation of signer failed
QuerySN
No certificate for identity 
com.apple.messagesecurity.mstimestamp.fetchTimestampWithCompletionBlock_success
Other timestamp request cannot be nil
Failed encoding type SMIMECapabilities
0123456789.
Failed encoding type ContentInfo
Failed encoding type CMSIdentifier
decode failed due to signature verification failure
timeStampTokenData
Granted
MessageSecurity.MSCMSAuthEnvelopedData
Other timestamp request has nil parameter
unable to verify timestamp signature for timestamp %lu
retry_count
Status string mismatch
signer verification failed for signer %lu
Expiration Time Attribute MUST have a single signed attribute value
ASN1_OVERFLOW
ASN1_EXACT_CONSTRAINT
1.2.840.10045.2.1
Unable to encode signedData: missing digest algorithms
unable to find any certificates with email address %@
com.apple.messagesecurity.MSCMSContentTypeError
timestampResponse
Missing value for Multiple Signatures attribute
unable to decode Apple Hash Agility Attribute
Invalid content type
<MSTimestampResponse:\n
Version mismatch
Unable to encode signedData: id-data content type and no data content
MSErrorKeychainDomain
Unable to decode OriginatorInfo
1.3.6.1.5.5.7.6.52
Unknown error
  Message Imprint: %@\n
TimeStampToken data is nil
SHA-1
Failed encoding type SMIMEEncryptionKeyPreference
2.16.840.1.101.3.4.2.4
errorDescription
  Policy OID: %@\n
Hashed messages do not match
Unable to encode signedData: no signers and not certs-only message
unable to find certificate by identifier; invalid choice in encoding
Missing or too many message-digest attribute(s)
  Algorithm OID: %@
0x%02x,
algorithmOIDString
Other message imprint has unsupported hash algorithm
unable to decode data content (%ld bytes)
responseObject
Status %ld
Self message imprint has unsupported hash algorithm
MSErrorCryptoDomain
MSErrorTrustDomain
com.apple.HeimASN1
UTC
1.2.840.113549.1.9.16.2.11
Failed encoding type AppleHashAgilityValue
UnknownContentTypeOID
1.2.840.113549.1.1.4
1.2.840.10045.4.3.4
.
unable to get certificate from provided identity
unable to find any certificates in keychain
%d
decode failed for recipientInfo (rid vs encryptedKey count)
NO
Unable to encode signedData: content is not detached and no content specified
2.16.840.1.101.3.4.1.6
algorithmParameters
MSCMSAppleTimestampAttribute: no timestamp token data to encode
unable to decode signerInfo in countersignature
2.16.840.1.101.3.4.1.7
  Request Size: %lu bytes\n
1.2.840.113549.1.9.15
MSErrorCMSDomain
unable to access the content encryption key
Message-digest attribute failed to verify
CMSIdentifier has inconsistent type and stored values: expected issuerAndSerialNumber
MSErrorAllocationDomain
ASN1_MIN_CONSTRAINT
-[MSCMSRecipientInfo initWithCertificate:keyEncryptionAlgorithm:keyWrapAlgorithm:originator:]
could not parse OID into string
(nil)
3
signedData contains content but has no signers
%@ is not a supported digest algorithm
Not an Expiration Time attribute according to AttributeType
No digest algorithm specified
decode failed for recipientInfo due to RFC 5652 violation (version)
unable to find a certificate matching the recipient
2.16.840.1.101.3.4.1.42
errorCode
countersignature verification failed for signer %lu
unable to copy Attribute
logCMSDecodingFailures
unable to find a certificate matching the signer
1.2.840.113549.1.1.1
<MSTimestampRequest: %p>\n
invalid Time choice in Signing Time
SMIME Capabilities Attribute should only have one value
com.apple.MessageSecurity
Unable to encode
2.16.840.1.101.3.4.1.5
  Server URL: %@
TSTInfo data is nil
  TimeStampToken: (nil)\n
unable to allocate Attribute
unable to decode Signing Time value
QuerySKID
ASN1_MISSING_FIELD
Unable to encode RecipientInfo: missing destination address
error_code
com.apple.MessageSecurity.MSTimestampXPCService
version
  Version: %ld\n
Failed to decode TimeStampToken as ContentInfo
unable to get contentType from envelopedData.encryptedContentnInfo
1.2.840.113549.1.7.2
MessageImprint pointer cannot be NULL
Timestamp response data mismatch
unable to get contentType from signedData
Failed to create message imprint for timestamp verification
Unable to verify
Unable to decode
Timestamp request cannot be nil
ContentInfo
1.3.14.3.2.7
  Policy: (none)\n
findIdentityByCertificate
unknown ccAlg -- unexpected encryption algorithm: %@
unknown ccMode -- unexpected encryption algorithm: %@
counter signer has no reference to a signer with a signature
findCertificateBySubjectKeyID
v32@?0@\"NSSet\"8Q16^B24
2.16.840.1.101.3.4.2.1
ASN1_INVALID_CHOICE
1.2.840.113549.1.1.7
unable to decode CMS Identifier tag
en_US_POSIX
ASN1_GOT_INDEFINITE
Unknown content type
http://timestamp.apple.com/ts-ec
com.apple.MSTimestampXPCService.queue
TSA mismatch
<MSMessageImprint: %p>\n
Unable to decode comrpessed data
MessageSecurity.MSCMSCompressedData
!
invalid CMS Identifier choice
Error Unavailable
  Gen Time: %@ UTC\n
  Serial Number: (none)\n
musr
\n--- Additional Debug Info ---\n
Nonce values do not match
  Hash: (empty)
unable to decode Expiration Time value
BundledSN
ASN1_MISPLACED_FIELD
DataContent
Nonce mismatch
Self timestamp response has nil parameter
signature verification failed for signer %lu
1.2.840.10045.4.3.3
1.3.6.1.5.5.7.3.8
SignedData does not contain encapsulated content (TSTInfo)
Failed to decode TSTInfo: ASN.1 error %d
Timestamp request was not granted. Status: %ld
unable to decode envelopedData.originatorInfo
RecipientInfo not found
1.2.840.113549.2.5
1.2.840.113549.1.9.5
default
v32@?0@\"MSOID\"8Q16^B24
\n
v32@?0@\"MSCMSSignerInfo\"8Q16^B24
Failed encoding type SignerInfo
%s did not find SubjectKeyIdentifier %@
MessageSecurity.MSCMSEnvelopedDataInternal
1.2.840.113549.1.9.16.1.4
could allocate OID components
  Hash: %@ (%lu bytes)
Failed encoding type CMSCBCParameter
init()
1.2.840.10045.4.3.2
statusString
no signer with input certificate hash
decode failed due to signer verification failure
ASN1_BAD_FORMAT
1.2.840.113549.1.1.12
Unable to allocate attribute array
ASN1_GOT_BER
valueForBooleanDefault
Unknown
unable to decode CMS Identifier
Encryption Key Preference Attribute should only have one value
unable to find any identities with email address %@
success
CMSIdentifer has unknown type: %d
Failed encoding type CMSRC2CBCParameter
unable to copy OID
fetch
Revocation warning
Not a Signing Time attribute according to AttributeType
Unknown ASN1 error
| 
MSErrorASN1Domain
1.2.840.113549.1.1.5
2.16.840.1.101.3.4.1.2
reqPolicyOIDString
Timestamp token SignedData not available for verification
Waiting
hashedMessage
Failed encoding type CMSAttributes
Failed encoding type OriginatorInfo
1.2.840.113549.1.7.6
Timestamp mismatch
>
unable to decode SMIME Capabilities Attribute
unable to set verify date on trust object
unable to encrypt/decrypt the content
2.16.840.1.101.3.4.1.45
messageType
certReq
<MSTimestampRequest:\n
could not parse OID into data
unable to encode signed attributes
unable to decode content info (%ld bytes)
MSTimestampHTTPErrorDomain
unable to build chain according to mode; missing signer info or signer certificate missing from signer info
QueryIssuer
ASN1_INDEF_UNDERRUN
Could not sign data: no private key
SHA-384
v32@?0@\"NSData\"8Q16^B24
decode failed for recipientInfo (keyEncryptionAlgorithm)
Not a ContentType attribute according to AttributeType
Failed encoding type AppleAgileHash
Could not sign data: no signature algorithm
InvalidContentTypeOID
Unable to encode compressed data
Underlying ASN1 error 
INVALID_ISSUER
underlyingErrorDomain
  Failure Info: %ld\n
1.2.840.113635.100.9.1
ASN1_MAX_CONSTRAINT
unable to verify countersigner %lu
2.16.840.1.101.3.4.1.25
underlying_error_code
  Gen Time: (none)\n
  Response Size: %lu bytes
SHA-256
v24@?0@\"MSAlgorithmIdentifier\"8^B16
<MSMessageImprint:\n
failed to set verification time
Could not sign data: no digest
No response object in XPC reply
Failed to unarchive timestamp response
unable to add signer cert to certificates; missing signer info or signer certificate missing from signer info
Unable to encode signedData: unable to allocate digest algorithm array
Timestamp response is missing message imprint or algorithm
1.2.840.113549.1.9.16.3.7
Failed to allocate memory for OID components
SignedData error
unable to copy Algorithm Identifier
  Message Imprint: (none)\n
  Status: %@\n
TSA policy OID mismatch
Could not decode message-digest attribute
Unable to encode signedData: embedded content type specified and no embedded content
decode failed due to timestamp verification failure
findCertificateByIssuerAndSerialNumber
%@
EnvelopedData
unable to decode envelopedData.recipientInfos
com.apple.messagesecurity
CMSSignedData
%@:%@ 
ASN1 encoding error
MessageSecurity/MSCMSAttribute.swift
internal asn1 error
1.2.840.10045.4.3.1
<MSTimestampResponse: %p>\n
Other message imprint cannot be nil
2.16.840.1.101.3.4.1.1
Unable to decode AuthEnvelopedData
http://timestamp.apple.com/ts01
nonce
; 
Other message imprint has nil parameter
failed to set anchor certificates
  Request Certificates: %@\n
  Algorithm: %@\n
yyyyMMddHHmmss'Z'
MSOID %@ does not indicate a digest algorithm
No timestamp request data available
v24@?0@\"NSObject<OS_xpc_object>\"8@\"NSObject<OS_xpc_object>\"16
  Serial Number: %@ (%lu bytes)\n
Fail info mismatch
unknown type for Encryption Key Preference Attribute
1.2.840.113549.3.2
2.16.840.1.101.3.4.1.41
%u.%u
1.3.14.3.2.26
SHA-512
countersigner verification failed for signer %lu
1.2.840.113549.1.9.4
invalid Time choice in Expiration Time
system-keychain
Invalid MessageImprint data
failInfo
Status mismatch
Unable to decode the content encryption key
MessageSecurity.MSCMSTimestampAttributeInternal
2.16.840.1.101.3.4.1.22
underlying_error_domain
  Nonce: %@ (%lu bytes)\n
hasFailInfo
Failed to extract TSTInfo from SignedData
1.2.840.113549.1.9.6
v32@?0@\"MSCMSCounterSignerInfo\"8Q16^B24
Signed content-type attribute does not match content-type in signedData
2.16.840.1.101.3.4.2.3
  Policy: %@\n
failed to create signerInfo object for signer %u
Failed encoding type TimeStampReq
Timestamp request data does not match
unable to create trust object due to security error
\xd1
Failed encoding type DataContent
Invalid OID component at index %lu: value %ld is out of valid range [0, %u]
ASN1_INDEF_OVERRUN
Missing or too many content-type attribute(s)
Signer has no signature algorithm
timestampServer
INVALID_OID
v32@?0@8Q16^B24
Version numbers do not match
status
Failed to decode TimeStampResp: ASN.1 error %d
B32@?0@\"NSString\"8Q16^B24
decode failed for signerInfo due to RFC 5652 violation (version)
Algorithm Identifier %@ does not indicate a public key algorithm
  Status String: %@\n
Unable to encode signedData: unable to allocate signerInfos array
decode failed for signedData due to RFC 5652 violation
Unable to encode SignerInfo: missing signer certificate
Certificate request flags do not match
unknown blockSize -- unexpected encryption algorithm: %@
ASN1_BAD_CHARACTER
Not a Multiple Signatures attribute according to AttributeType
timestamp_server
Timestamp response does not contain a message imprint
unable to decode envelopedData (%ld bytes)
1.2.840.113549.1.7.1
1.2.840.113549.3.7
Failed to create XPC session
requestObject
Algorithm identifiers do not match
Not a MessageDigest attribute according to AttributeType
Failed to decode timestamp token as MSTimestampResponse
Unable to get serial number from certificate
1.2.840.113549.1.7.5
unable to verify countersignature(s) for countersigner %lu
Failed encoding type AlgorithmIdentifier
timestamp.apple.com
unable to decode Algorithm Identifier
unable to allocate Algorithm Identifier
Timestamp token signature and certificate verification failed
v32@?0@\"<MSCMSAttributeCoder>\"8Q16^B24
BundledIssuer
ASN1_BAD_ID
unable to decode envelopedData.unprotectedAttrs
1.2.840.113549.1.9.16.1.2
elapsed_ms
Unable to encode signedData: missing content type
Not a Countersignature attribute according to AttributeType
ASN1_OVERRUN
Invalid OID string format
TSA policy OIDs do not match
  TSA: %@\n
Not an Encryption Key Preference attribute according to AttributeType
Request contained nonce but response does not
Other timestamp response has nil parameter
Failed encoding type MultipleSignatures
unable to get private key from provided identity
unable to compute digest for signature
Unable to encode SignerInfo: missing destination address
1.2.840.113549.1.7.3
Failed to create XPC session: %s
signer is missing signature
1.3.14.3.2.6
Failed to create Apple timestamp policy
Message imprint presence mismatch
unable to create trust object
AuthEnvelopedData
v8@?0
decode failed for recipientInfo (rid)
Revocation notification
1.2.840.113549.1.1.11
Fail info presence mismatch
Unable to get issuer sequence from certificate
1.2.840.113549.1.1.14
1.2.840.10045.4.1
SecKeyAlgorithm %@ does not indicate a signature algorithm
Serial number mismatch
unable to find any identities in keychain
no certificates found in signerInfo for trust evaluation
com.apple.messagesecurity.mstimestamp.fetchTimestampWithError_success
MSDecryptGCM error: %d
1.2.840.113549.1.1.13
unable to decode CMSAttributes
yyMMddHHmmss'Z'
%02X
1.3.133.16.840.63.0.2
unknown keySize -- unexpected encryption algorithm: %@
ContentType attribute contains more than one value
unable to decode Multiple Signatures attribute
com.apple.messagesecurity.MSCMSContentError
No timestamp server URL specified
Not an SMIMECapabilities attribute according to AttributeType
ASN1_PARSE_ERROR
decode failed for recipientInfo (originator)
  Nonce Length: %lu bytes
No timestamp response data to parse
signer has no signature algorithm
Unable to encode enveloepd data
ASN1_TYPE_MISMATCH
MessageSecurity/MSCMSAuthEnvelopedData.swift
BundledSKID
ASN1_EXTRA_DATA
(not set)
Rejection
2.16.840.1.101.3.4.2.2
MSOID %@ does not indicate a signature algorithm
UNEXPECTED_VALUE
Could not decode content-type attribute
signer has no reference to a signedData with content
%@ is not a supported signature algorithm
unable to verify timestamp signature because there are no timestamps
Self timestamp request has nil parameter
unable to decode SKID Identifier
failed to get public key from certificate
MSTimestampErrorDomain
timestamp verification failed for signer %lu
Failed encoding type CMSOrderedAttributes
Failed encoding type MessageDigest
NULL
https://timestamp.apple.com/tsa-mldsa87-rsa3072-pss-sha512
signer index, %lu, out of range of signer count, %lu
Unable to encode signedData: unable to allocate certificates array
Apple Hash Agility Attribute should only have one value
1.2.840.113635.100.9.3
unable to add recipient
Invalid parameter
2.16.840.1.101.3.4.1.26
Server URL mismatch
Message imprint cannot be nil
Other timestamp response cannot be nil
Unable to encode signedData: failed to encode a SignerInfo
1.2.840.113549.1.9.3
1.2.840.113549.1.9.2.51
ASN1_BAD_TIMEFORMAT
2.16.840.1.114027.80.9.1.15
1.2.840.113635.100.9.4.1
the Encryption Key Preference Attribute did not match any certificates
unable to decode Apple Hash Agility V2 Agile Hash
Unable to encode content info: missing content type or content
unable to find identity matching %@
unable to create countersignature attribute for countersigner %lu
Could not sign data: no identity in keychain for certificate
1.2.840.113549.1.9.16.1.9
.%u
@\"NSObject<OS_xpc_object>\"8@?0
Unable to encode signedData: missing digest algorithm and not certs-only message
Cannot encode signed attributes: no SignedData
messageImprint
YES
  TimeStampToken: Present\n
MessageDigest attribute contains more than one value
Could not sign data: no key or certificate specified
No key for identity 
missing or invalid OID string %@
Request policy OID mismatch
Granted with modifications
CMSIdentifier has inconsistent type and stored values: expected subjectKeyId
MD5 is not supported for signing
Failed encoding type CMSSignedData
unable to decode signedData (%ld bytes)
Failed encoding type SecCMS_SMIMEEncryptionKeyPreference
1.2.840.113549.1.9.16.1.23
XPC communication error: %s
  Nonce: (none)\n
Signing Time Attribute MUST have a single signed attribute value
unable to decode Encryption Key Preference Attribute
id-aa-timeStampToken attribute has %lu values, expected 1
TimeStampToken error
Unable to encrypt
ASN1_INDEF_EXTRA_DATA
unable to decode ContentType
Failed encoding type ContentType
-[MSCMSTimestampAttribute initWithTimestampToken:]
%s did not find IssuerAndSerialNumber %@ %@
Failed to encode TimeStampReq: %@
MSCMSChainMode with chain specified, but could not build chain beyond leaf, continuing with single certificate
found %lu candidate certs from keychain with matching email addresses
Unable to generate nonce underlying crypto error %d
Error decrypting underlying crypto error %d
MSCMSRecipientInfo init encryption algorithm %@ not permitted for certificate key type %ld
MSTimestampResponse: Failed to parse timestamp response: %@
unable to parse certificate at %u
BundledSKID = %{mask.hash}@
failed to set credential reference on signer public key: %@
recipientInfo violates RFC 5652 (key usage)
Failed to parse hash algorithm OID: %@
%s %s isInternal: %d val: %s isForced: %d appVal: %s result: %d
Invalid data - error decoding AuthEnvelopedData
MSCMSRecipientInfo requires an originator identity for an EC recipient. Encode will fail if not set.
No certificate with id-kp-timeStamping EKU found in certificate chain
Found unsupported content type: AuthenticatedData
failed to add recipient. No shared encryption algorithm with the rest of the recipients
no countersignatures, returning successful verification
no timestamps, returning successful verification
Unable to generate key underlying crypto error %d
MSTimestampResponse initWithTimestampToken: failed to parse token: %@
QueryIssuer = %{mask.hash}@
logging %s 0x%zx [%ld-%ld)/%ld %s
Invalid data - Error encoding GCM parameters
Error encrypting underlying crypto error %d
MSCMSChainMode with chain specified, but no trusted chain found (%@), continuing with untrusted chain
%s failed with %@
found %lu candidate email certs from keychain
MSCMSRecipientInfo %s: Unsupported certificate key type
MSTimestampRequest: Completion block is required
%{public}@
Found unimplemented contented type: EncryptedData
Invalid data - no certificate in originatorCertificates
Invalid data - no recipients found
Invalid data - originatorInfo has no certificates
Invalid data - error decoding OriginatorInfo
TimeStampToken has multiple signers (%lu), RFC 3161 requires exactly one
signedData contains embedded content but signer %lu does not have signed attributes.
Found unknown content type: %@
BundledIssuer = %{mask.hash}@
QuerySKID = %{mask.hash}@
Bad signature algorithm %@. Trying to compose signature algorithm from %@ and digest %@
No recipient found
Invalid data - error decoding GCMParameters
Failed to encode TimeStampToken: %@
Digest length %lu is not a supported length
QuerySN = %{mask.hash}@
Invalid input data/embedded data
Invalid AES-GCM tag length %ld, RFC 5084 requires 12 to 16 octets
Failed to archive MSTimestampRequest: %@
Found unsupported content type: DigestedData
Error decrypting encoded content
Invalid data - aes-ICVlen is negative or too large
Invalid input algorithm %u
MSTimestampRequest: Retryable error (attempt %ld/%ld): %@
Failed to build MessageImprint for TimeStampReq: %@
MSCMSSignerInfo init signature aglorithm %@ not permitted for certificate key type %ld
Invalid encryption algorithm %u
MSTimestampResponse: Cannot initialize with nil timestamp response data
TimeStampToken has no signers
No certificates in SignedData
found %lu valid email candidate certs
Error: SignedData contentType is %@ (expected %@)
Failed to parse TSA policy OID: %@
failed to set credential reference on signer private key: %@
skipping non-certificate CertificateChoice at %u
MSCMSAppleTimestampAttribute: failed to create MSTimestampResponse from token data
Invalid data - error encoding AuthEnvelopedData
MSTimestampRequest: Failed to unarchive response: %@
MSTimestampRequest: Queue is required
MSTimestampResponse initWithTimestampToken: Cannot initialize with nil token data
BundledSN = %{mask.hash}@
failed to decode recipient %u: %@
aes-ICVlen %ld does not match mac length %ld
Invalid data - AES-GCM algorithm identifier carries no parameters
Error extracting MAC
Invalid AES-GCM nonce length %ld, expected 12 to 16 octets
```
