# `/System/Library/Frameworks/Security.framework/Security`

From the upgrade restore ramdisk (141-29011-104.dmg). 3,869,744 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 44 (Size: 6576)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (25)

- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore (compatibility version 0.0.0, current version 0.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8, upward)`
- `/usr/lib/libCoreEntitlements.dylib (compatibility version 1.0.0, current version 1.0.0, upward)`
- `/usr/lib/libTLE.dylib (compatibility version 1.0.0, current version 1.0.0, upward)`
- `/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity (compatibility version 0.0.0, current version 0.0.0, upward)`
- `/System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer (compatibility version 1.0.0, current version 326.31.9, upward)`
- `/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter (compatibility version 1.0.0, current version 0.0.0, weak)`
- `/System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport (compatibility version 1.0.0, current version 1.0.0, upward)`
- `/System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics (compatibility version 1.0.0, current version 1.0.0, upward)`
- `/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag (compatibility version 1.0.0, current version 1.0.0, upward)`
- `/System/Library/Frameworks/MobileCoreServices.framework/MobileCoreServices (compatibility version 1.0.0, current version 1226.0.0, upward)`
- `/System/Library/Frameworks/CoreServices.framework/CoreServices (compatibility version 1.0.0, current version 1226.0.0, upward)`
- `/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime (compatibility version 1.0.0, current version 340.0.14, weak)`
- `/usr/lib/libsqlite3.dylib (compatibility version 9.0.0, current version 408.0.0)`
- `/usr/lib/libcoretls.dylib (compatibility version 1.0.0, current version 189.40.2)`
- `/usr/lib/libcoretls_cfhelpers.dylib (compatibility version 1.0.0, current version 189.40.2)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libbsm.0.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (109 classes, 32 protocols)

Classes: `AcmeCertRequest`, `CKKSControl`, `CKKSCurrentItemQuery`, `CKKSCurrentItemQueryResult`, `CKKSExternalKey`, `CKKSExternalTLKShare`, `CKKSPCSIdentityQuery`, `CKKSPCSIdentityQueryResult`, `DefaultCollectionActions`, `DetachedCertificateEntry`, `DetachedCertificatesFile`, `DetachedCertificatesLookup`, `ExternalPreSharedKey`, `FakeSecuritydXPCClient`, `KCSharingDaemonConnection`, `KCSharingGroup`, `KCSharingGroupCreateRequest`, `KCSharingGroupDeleteRequest`, `KCSharingGroupFetchRequest`, `KCSharingGroupInvite`, `KCSharingGroupLeaveRequest`, `KCSharingGroupManager`, `KCSharingGroupUpdateInfo`, `KCSharingGroupUpdateRequest`, `KCSharingMessagingdConnection`, `KCSharingParticipant`, `LKAUpgradeOutcomeReport`, `LocalKeychainAnalytics`, `NSData`, `NSDate`, `NSObject`, `OTBottleIDs`, `OTClique`, `OTConfigurationContext`, `OTControl`, `OTControlArguments`, `OTJoiningConfiguration`, `OTMetricsSessionData`, `OTOperationConfiguration`, `OTSerializedPlistEscrowRecord`, `OfferedEPSK`, `SECSFAAction`, `SECSFAActionAutomaticBugCapture`, `SECSFAActionDropEvent`, `SECSFAActionTapToRadar`, `SECSFAEventFilter`, `SECSFAEventRule`, `SECSFAMatchProperty`, `SECSFAPropertyValue`, `SECSFARule`, `SECSFARules`, `SECSFAVersion`, `SECSFAVersionMatch`, `SFAnalytics`, `SFAnalyticsActivityTracker`, `SFAnalyticsCollection`, `SFAnalyticsEvent`, `SFAnalyticsMatchingRule`, `SFAnalyticsMultiSampler`, `SFAnalyticsSQLiteStore`, `SFAnalyticsSampler`, `SFObjCType`, `SFSQLite`, `SFSQLiteStatement`, `SOSAnalytics`, `SOSCachedNotification`, `SecABC`, `SecAsyncPiper`, `SecCBORArray`, `SecCBORData`, `SecCBORMap`, `SecCBORNegative`, `SecCBORString`, `SecCBORUnsigned`, `SecCBORValue`, `SecCTKKey`, `SecConcrete_sec_array`, `SecConcrete_sec_certificate`, `SecConcrete_sec_identity`, `SecConcrete_sec_protocol_configuration`, `SecConcrete_sec_protocol_configuration_builder`, `SecConcrete_sec_trust`, `SecCoreAnalytics`, `SecEscrowRequest`, `SecExpConcrete_sec_experiment`, `SecExperiment`, `SecExperimentConfig`, `SecExternalPreSharedKey`, `SecItemCurrentItemData`, `SecItemRateLimit`, `SecJWSDecoder`, `SecJWSEncoder`, `SecKeyProxy`, `SecKeyProxyTarget`, `SecLaunchEvent`, `SecLaunchSequence`, `SecOfferedEPSK`, `SecOfferedPAKEIdentity`, `SecSFAParsedCollection`, `SecSOSStatus`, `SecSessionInfo`, `SecTapToRadar`, `SecXPCHelper`, `SecXPCUtils`, `SecuritydXPCCallback`, `SecuritydXPCClient`, `SharedCredentialController`, `TPMIDStableTrustedDeviceID`, `TPStableTrustedDeviceID`

Protocols: `ASAuthorizationControllerDelegate`, `ASAuthorizationControllerPresentationContextProviding`, `CKKSControlProtocol`, `EscrowRequestXPCProtocol`, `KCSharingGroupManagerSubscriberProtocol`, `KCSharingInvitationNotificationProtocol`, `KCSharingMessagingdXPCServerProtocol`, `KCSharingXPCClientProtocol`, `KCSharingXPCServerProtocol`, `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`, `NSXPCListenerDelegate`, `OS_sec_array`, `OS_sec_certificate`, `OS_sec_experiment`, `OS_sec_identity`, `OS_sec_protocol_configuration`, `OS_sec_protocol_configuration_builder`, `OS_sec_trust`, `OTControlProtocol`, `SFAnalyticsCollectionAction`, `SFAnalyticsProtocol`, `SFSQLiteRow`, `SOSControlProtocol`, `SecEscrowRequestable`, `SecKeyProxyProtocol`, `SecuritydXPCCallbackProtocol`, `SecuritydXPCClientInterface`, `SecuritydXPCProtocol`, `TrustdFileHelper_protocol`

## Strings (8,655)

First 2,500 of 8,655.
```
softlink:r:path:/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle
softlink:r:path:/System/Library/PrivateFrameworks/SecurityFoundation.framework/SecurityFoundation
rfc822Name
1973
Failed to export ML-DSA pubkey
RevocationInfo
spid-
Could not create SecuritydXPCClient
TLS_CHACHA20_POLY1305_SHA256
|
kSecKeyWrapPGPFingerprint
v24@?0@\"NSData\"8@\"NSError\"16
DemoUnit CA
object for key %s not set but %@
ProdMarker
invalid tag
{%O = %d,%O = %d,%O = %d}
versions key missing
PKCS #9 Extended Certificate Attributes
ECDSA With SHA-384
com.apple.security.cloudkeychainproxy3
r_Data
SecKeyCopyExternalRepresentation
Class getTKClientTokenSessionClass(void)_block_invoke
{+%O,%O=%u}
quic_use_legacy_codepoint
B40@?0@\"NSObject<OS_dispatch_data>\"8Q16r^v24Q32
mdat
2222
789456
verify
RDN
failed to get subjectAltName value bytes
Need an array of character sets, password must have at least 1 character from each set
yyyy-MM-dd'T'HH:mm:ss.SSSZZZZ
Class
symKeySize
com.apple.remotemanagementd
OTClique.m
info
getOSEnvironment
u_SystemKeychainAlways
algid:keyexchange:ECDH:KDFX963:SHA256
auditToken
CKDKVS-incomingMessages
1.2.840.113635.100.1.116
1.2.840.113635.100.1.129
{current=%d,total=%d}
select %@ from %@
circleChange
}
iCloudIdentity-tomb
RSA public key creation from data failed
algid:sign:RSA:digest-PKCS1v15:SHA224
SecRequirementSyntax
f
GIF
asen
malformed mach-o file, LC_CODE_SIGNATURE offset + size overflows\n
CodeSignature2
validation-category
AccountDSID
disabledViews
) or (
neg_curve
secp521r1
explicit detached
resumption_attempted
ocsp_enabled
TLS_DHE_RSA_WITH_AES_256_CBC_SHA256
SynchronizeAndWait
spwd
1999
1.2.840.113635.100.1.25
nw_protocol_options_access_handle
Bad user public signature
AppleESCertificates
http
1.2.840.113635.100.12.4
{+%O,%O=%O}
spid-%@
minimum_rsa_key_size
Netscape says this cert is OK
CreditCards
1.2.840.113635.100.6.59.1
token based item data does not have OID
bin3
hw.osenvironment
Certificate Basic Constraints
Permitted Subtree Maximum
NumberOfRequiredRandomCharacters
BasicCertificateProcessing
Siri
kSecAttrIsExtractable
^CodeResources$
float
bitfield
PublicSigningKey
1.2.840.113635.100.1.107
no data for key %s
kSecAttrAccessControl
SecStaticCode
MISSI KEA Algorithm
keyid
Unsupported symmetric key type: %@
algid:encrypt:ECIES:ECDH:KDFX963:SHA256:AESGCM-KDFIV
1.2.840.113635.100.6.2.33
cdpContextTypeFinishPasscodeChange
SOSCCCopyConcurringPeerPeerInfo
Access Method
m_Policy
0111
ExtendedValidation
failed to request authorization
{rules={'^version.plist$' = #T'^.*' = #T'^.*\\.lproj/' = {optional=#T, weight=1000}'^Base\\.lproj/' = {weight=1010}'^.*\\.lproj/locversion.plist$' = {omit=#T, weight=1100}},rules2={'^.*' = #T'.*\\.dSYM($|/)' = {weight=11}'^(.*/)?\\.DS_Store
v24@?0@\"<SFSQLiteRow>\"8^B16
 AND 
account_id
kSecCMSSignDigest
unsupported kSecValueRef in query
algid:sign:ECDSA:digest-RFC4754:SHA1
1.2.840.113635.100.1.125
SecCode
com.apple.security.syspolicy
%@%@%@%@%@
algid:sign:RSA:message-PSS:SHA224:SHA224:24
/System/AppleInternal/Library/Frameworks/CryptoTokenKit.framework/CryptoTokenKit
LAErrorDomain
com.apple.security.XPCAcmeService
Medium Type
%@\n%@\nRelated radar: rdar://%@\nRequest triggered at: %@
negotiated_protocol
set user credentials unimplemented
PKIX CRMF Registration Control, PKI Archive Options
kSecKeyWrapPGPECWrapDigestSHA512KekAES256
can't open output file for writing: %s, errno=%d\n
octagon-checkinheritancekey
Bit string
algid:sign:RSA:message-PKCS1v15:SHA1
 or 
permissionLevel
1.2.840.113635.100.1.68
rsa_pub_crypt failed, ccerr=%d
PermitLocalIssuer
iPhone OS
1122
index %lu
 required rules
^(\\d+)([A-Z])(\\d+)
1.2.840.113635.100.1.67
Certificate is revoked
invalid CFDataRef
com.apple.security.cert-request
lockassertions
123321
QWAC
v16@?0^v8
%@
%@: X962 signing failed (ccerr %d)
algid:sign:RSA:raw
SystemTrustedWeakKey
timestamp-url
new architecture offset is too large
counter
TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256
clique-status
defaultTestflightLWCR
SerialNumber
encoded extensions must be a data type
Allocation mismatch
Exception thrown trying to format object
 where %@
version
%@ has no wrapped key in %@
ApplePCSEscrowServiceIdKeySigning
push-reset-circle-to-kvs
S/MIME
algid:keyexchange:ECDHC:KDFX963:SHA256
PolicyConstraints
csutilities
CSFlags
errorCode
basicConstraintsCA
ValidHTTPS
com.apple.cs.
SecItemUpdate: %d
Invalid key
PPQ
LibraryConstraint
Inflating octagon peer signing persistent ref
Missing project-specific extension OID
<C: gen:'%@' %@>\n
kAppleIDAuthSupportProtocolSRPGROUP2048SHA256PBKDF
dspk
\"%@\"
xpc_path value is not an array
Failed to decode akid
2006-05-31
sos-compatibility-mode-cached
CMSDigestHashType
vacuum
codesign
domain
:
1.2.840.113635.100.1.91
policyOptions
return=%d
v24@?0q8@\"NSError\"16
v16@?0^{ccec_full_ctx=^{ccec_cp}[0{ccec_projective_point=[1Q]}]}8
code
structure
Number too large
run-unsigned-code
ssh 
TrustEvaluationDate
TrustCertificateTransparency
B24@?0r^{fat_arch=iiIII}8r^{fat_arch=iiIII}16
default-designated-lwcr
TransportType
HSADictionary
1112
CliqueStatusError
RFC1274 E-mail Address
1.2.840.113635.100.1.9
{+%O'^(Frameworks|SharedFrameworks|PlugIns|Plug-ins|XPCServices|Helpers|MacOS|Library/(Automator|Spotlight|LoginItems))/' = {nested=#T, weight=0}}
long
null trust input
digest
AppAttest_DeviceAttestation_AttestKey
^{__OpaqueSOSPeerInfo=}8@?0
ECIES: Failed to aes-gcm encrypt data (err %d)
Resending reveal signature
<SOSFullPeerInfo@%p: \"%@\">
Qualified Certificate
EC
P-256
failed to decode v1 otr session: %d
SecCSResourceAltered
select name from sqlite_master where type = 'table'
npn_used
nullkey
JOSE
1.2.840.113635.100.1.35
1.2.840.113635.100.6.27.11.2
eventClass
rockwell
alert_type
kcsharing-logger
1.2.840.113635.100.6.1.25.2
SecTrust
verifySignatureEmbeddedPolicy: CTGetSKIDAmfiCMS failed (V1 SignerInfo or error)
Synchronize
com.apple.security.secureobjectsync.circlechanged
viewCheck
signaturefile
SecCSResourceMissing
stapled-ticket
/System/Library/Frameworks/Security.framework
Certificate Extension Base URL
PKIX CRMF Registration Control, Registration Token
No public signature to match current user key
SOSCCCopyPeerPeerInfo
rpaa
cdhashes-full
scep
acmeLocalIssuer
create table if not exists Properties (\n    key    text primary key,\n    value  text\n);\n
eventRules
\n\t\t
ftp 
X25519 public key creation from data failed
Signing failed, err=%d
keybag
clique-findbottle
number
Private Key Usage Period
Excluded Subtree Maximum
1.2.840.113635.100.6.60
FDRProvisioning
3
idMSTDLNotificationFlowID
EnableAppTransportSecurityAppleBundleException
Compatibility version mismatch: self=%llu, other=%llu
timeoutWaitForCKAccount
Deleting signing key while purging
iPhoneProfileApplicationSigning
1.2.840.113635.100.1.40
^Versions/Current$
SecCodeSigner
requested validation for first signature slot, but it doesn't exist
compareLeafCertOIDs: OID mismatch for %s (1.2.840.113635.100.6.1.x)
Unable to build chain to root certificate.
never
failed to encode public key
7465
malformed mach-o file, LC_CODE_SIGNATURE wraps around\n
SecOTRFullIdentity
Device Characteristics
OS X Shared Library Cache (%s @ 0x%llx)
mach-port
end
oldschema
Unable to get public
Not f
Invalid certificate chain linkage.
omit-adhoc-flag
rules2
waitfortlkupload
TLS_RSA_WITH_AES_128_GCM_SHA256
LeafMarkersProdAndQA
exceptions
PCS-Notes
1.2.840.113635.100.12.17
Unable to find class %s
X.501 Name
algid:encrypt:RSA:OAEP:SHA384
ABCDEFGHJKLMNPQRSTUVWXYZ23456789
policy xpc array count < 2
Cannot request admission when already a peer
cfset
,
ats_non_pfs_ciphersuite_allowed
pref
UUID
Class getTKClientTokenClass(void)_block_invoke
1.2.840.113635.100.1.81
FCP_v2.1
PKCS #12 Enveloping IDs
edat
v_PersistentRef
SecKeyCopyAttributes
Action
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256
dropRate
B8@?0
IP Address
BUG IN CLIENT OF SECITEM: too many reads. See https://at.apple.com/secitemratelimit
accc
321654
X520 Country Name
X448 private key creation from data failed
algid:sign:ECDSA:digest-X962:SHA384
bundle with 
\\%c
No detached certificates found for executable: %@
QAMarker
ComponentName
Invalid private key size
CodeResources
/System/Library/Security/DetachedCertificates.der
<=
Digital Signature
%@: X25519 DH failed (ccerr %d)
trailing junk after add
ValidCMS
setting default value
TLS_RSA_WITH_AES_256_CBC_SHA
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA
AES-192-CBC
CoderDump
1.2.840.113635.100.6.50
overflow calculating output size (%u + %d + 15)
KEM decapsulation failed: expecting input data of size %dbytes
keychain
1.3.6.1.5.5.7.3.8
unsigned long long
com.apple.protectedcloudstorage.protectedcloudkeysyncing
algid:encrypt:RSA:OAEP:SHA256
epoch
SFSQLiteStatement.m
B24@?0r*8^v16
DeviceID
WiFi-tomb
certificates xpc value is not an array
/System/Library/Frameworks/UIKit.framework/UIKit
algid:sign:RSA:raw-cc
Date Formatting
object for key %s is NULL
unsigned char
certificateExtensionsEncoded
hard_failures
icloud-identity
atag
One or more certificates is using a weak key size.
uniqueDeviceID
tomb
PasswordNumberOfGroups
issuerIdentity
non-
RevocationDbIgnoredForAppleCodeSignChain
SecStaticCode::detachedCertificates(): Empty certificate data at index %ld
unknown eventclass: %@
X500 RSA Encryption
NULL
failed to find persistent ref for key: %d
Multiple extensions with the same extension ID
Remote error not dictionary!: %@
<OTConfigurationContext %@, %@, %@>
CRL Number
Failed to create authentication context
pagesize
CMSEncoder
No Memory
pcss
SecKeyCopyPublicBytes
SecKeyCreateMLDSASignature() called with NULL dataToSign
Sending reveal signature
otrsess
clientIdentifier
ConfigData
apple.com
CliqueStatusIn
MetricSessionInfo
<TPStableTrustedDeviceID: sdid=%@, lduid=%@, idMSTrustTimestamp=%@>
verifySignatureEmbeddedPolicy: verification failed, attempting auto-lookup of detached certificates
Developer ID
clique
B16@?0i8B12
SecErrorMessages
Yes
LAMPS13-MLDSARSA
Failed to create CFObject from XPC policy
1956
policy
%@-%@
AppleLegacyPushService
com.apple.mail
0123456789ABCDEF:
Ed25519PrivateKey
memory
 \t\n\r\f
Classification
%@%@%@%@
2147483680
subject
ccder failed to encode
__info_plist
predicate
No key wrap supported for key %@
algid:encrypt:RSA:OAEP:SHA224:AESGCM
TrustEvaluationID
TrustTopic
TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256
geo.apple.com
1111
Apple Worldwide Developer Relations CA - G2
ApplePPQSigning
H\"
v24@?0r^v8Q16
configVersion not understood %@, this tool knows about %d
com.apple.mobilemail
CMS 3DES Key Wrap
policies
(%d:%d)
drop table %@
SHA256:
<CKKSCurrentItemQuery(%@-%@): %@>
algid:keyexchange:ECDH:KDFX963:SHA512
Bad requested kSecKeyEncryptionParameterSymmetricKeySizeInBits: %@
no-macho
DataMessage (0x03)
SubjectCommonName
iPhoneApplicationSigning
Failed to encode [1] EXPLICIT tag
NSDictionary
1.2.840.113635.100.6.36
com.apple.networkextensionsharing
ttr
TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384
bskb
1.2.840.113635.100.6.2.10
AppAttest_DeviceAttestation_IsSupported
BUG IN CLIENT OF SECITEM: too many writes. See https://at.apple.com/secitemratelimit
1995
limitMinutes
Null CFType
SOSCCSetCompatibilityMode
ProductionEscrowKey
Data
Qualified Certificate Statements
i24@?0r^^{__CFArray}8^^{__CFError}16
algid:sign:RSA:message-PSS:SHA512:SHA512:64
InvalidMessage (0xFF)
Expected number type to be either integer or floating point
TLSv1_RC4_fallback
failed to encode certificate
{%O=%d,%O=%d}
DetachedCertificates.der
cipher_name
CKPackage
adaptive_proportion_reset_count
identifier
Authority Key Identifier
2012
SE-PTA
hard_failure_count
SecKeyCreateRandomKey
URLBag
<SecKeyRef %@ algorithm id: %lu, key type: %s, version: %d, bytes: %@, addr: %p>
Unsupported private key type: %@
NameConstraints
Base\\.lproj/
alert_code
char*
AllowAllMetrics
DES-EDE3-CBC
Public Key Info
Unknown CoreEntitlements encoding
Failed to decode certificate sequence: %d
Leaf certificate does not have an AKID
os-environment
Unable to get trust store content digest
1.2.840.113635.100.1.53
ParakeetService
processName
^AccountChanged
Inhibit Policy Mapping
\"payload\":\"%@\",
omit
This certificate has expired
X448PublicKey
ECDHKeyExchange wrong sharedInfo type (must be CFData/NSData)
{(
Invalid requirement
rules type invalid
void
^Required
enabledViews
LKAEventStashLoad
NetworkingTopic
kSecECCurveNone
inet
Certificate Transparency validation required for this use
source
_
isCurrentUser
legacy_DHE
key class
algid:encrypt:RSA:OAEP:SHA384:AESGCM
Validity
q24@?0@\"SecLaunchEvent\"8@\"SecLaunchEvent\"16
Missing project-specific Certificate Policy OID
cfarray
timestamp-authentication
 %@%@
%s: %s - %s
TLS_RSA_WITH_AES_256_GCM_SHA384
^OfficialDSID
smb 
1.2.840.113635.100.6.2.31
v24@?0@\"NSArray\"8@\"NSError\"16
senderHandle
JPEG
bool_and_error_request_returns_bool
Failed to get externalized context from LAContext
TKTokenNotFoundAndRegistered
CLLocation
SignatureDigestSHA1
endpoint
dynamicCode
Default
Anchor does not match pinned fingerprint
Public Key isn't available. The iCloud Password must be provided to keychain syncing subsystem to repair this.
HybridSigLAMPS13MLDSARSAPrivateKey
2147483679
1.2.840.113635.100.12.55
AppleOSXProvisioningProfileSigning
ApplePayIssuerEncryption
ATS
EDI Party Name
algid:sign:RSA:message-PKCS1v15:SHA512
policy identifier is not a string
repeatAfterSeconds
PKCS #12 OIDs
@\"SFAnalyticsEvent\"16@?0@\"<SFSQLiteRow>\"8
algid:encrypt:RSA:PKCS1
algid:keyexchange:ECDHC
1.2.840.113635.100.4.8
Missing issuer-specific extension OID
label
p
wrong value type for EKU
snrc
42
2002
 = 
Signature didn't verify for %@
SignatureDigestSHA224
type
<SecAccessControlRef: %@>
kSecCMSHashingAlgorithmSHA256
EC signature verification failed, no match
wrap
algid:sign:ECDSA:message-X962:SHA384
The password's allowed characters must be a CFStringRef
TLS_DHE_RSA_WITH_AES_256_CBC_SHA
Apple iPhone Certification Authority
Excluded Subtree Minimum
TEST %@ TEST
TEST
tls_ticket_request_count
Authority Information Access
SOSCCCopyMyPeerInfo
SOSCCRegisterSingleRecoverySecret
RSA-WRAP too short input data
anchors
1.2.840.113583.1.1.5
trailing garbage after plist item
not displayed (tag = %ld; length %ld)
101471
v32@?0@\"NSString\"8@\"SecLaunchSequence\"16^B24
RC4
DES-EDE
eventName
cannot mmap file %s\n
staticCode
build
Ed25519 signature verification failed (invalid signature length)
1.2.840.113635.100.1.64
root
PeerID
EvaluationID
NSURL
RSA signature verification failed, no match
clique-disable-walrus
failed to encode keyUsage
The dictionary parameter 'Identical Consecutive Characters' is either null or not a number
Certificate violates issuer name constraints
CodeOffset
Expected SEQUENCE for certificate list
ViewNotMember
520520
device-attest-01
0123
kSecACMEDirectoryURL
606179
X520 Organizational Unit Name
Certificate Renewal Time
AppleIssued
S
CKDKVS-synchronizeFailures
Unable to create LAContext from externalizedContext
KeyUsage
ocsp_received
join after restore unimplemented
DES-CBC
system
com.apple.security.egoIdentities
octagon-removecustodianrecoverykey
Bad Blob DER
revocation
%02x
rscan
kSOSCCViewEnable
agrp
SecKeyCopyKeyExchangeResult() called with NULL publicKey
1.2.840.113635.100.1.106
yyyy-MM-dd HH:mm
cdpContextTypeRecoveryKeyGenerate
SOSCCAccountHasPublicKey
Invalid parameters
codedirectory-hash
kern.entropy.health.repetition_count_test.max_observation_count
Unexpected Null Set to encode
v16@?0^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}8
m_CaseInsensitive
smtp
peer-infos
CloudServicesTopic
failed to encode notBefore
apls
v_Data
RequiredCharacterSets
failed to convert xpc policy[0]=%@ to CFString
expires
%s[%d]/%d#%d LF=%d
CKAsset
com.apple.security.codesigning
type = ? AND name = ?
backupLastSuccess
wrappedTLK
cdpContextTypeConfirmPasscodeCyrus
MD4
algid:sign:RSA:message-PSS:SHA1:SHA1:20
SSLHostname
SubjectOrganizationalUnit
 is NULL
%ld
inviteData
sos_analytics.db-shm
octagon-generateinheritancekey
 %u]
ECpriv sharedsecret: bad public key
<SecKeyRef algorithm id: %lu, key type: %s, version: %d, %d bits (block size: %zu), exponent: {hex: %llx, decimal: %lld}, modulus: %@, addr: %p>
dflt
Certificate Transparency validation required but missing
KCSharingGroup(%@, name: %@ shareURL: %@ participants:\n
/usr/lib/libnetwork.dylib
v
user_label=%@
algid:encrypt:ECIES:ECDH:KDFX963:SHA512:AESGCM
v24@?0Q8*16
/Versions/Current
isOlderGeneration proposed_circle
Issuer Unique ID
ProvoloneProcessedSigning
SOSCCRejectApplicants
failed to decode v3 otr session: %d
/System/Library/PrivateFrameworks/AppAttestInternal.framework/AppAttestInternal
com.apple.private.octagon.escrow-content
ircs
_rsae
cdhashes
v32@?0@\"NSString\"8@\"SFAnalyticsSampler\"16^B24
Algorithm
unsupported kSecMatchPolicy in query
algid:encrypt:ECIES:ECDH:SHA256:2PubKeys
algid:kem:ML-KEM
NTLMSSP
Netscape Nickname
applicants=%@
ECpriv failed to compute shared secret (err %d)
^_CodeSignature$
    '%@' %s %@\n
SignatureDigestUnknown
1986
Not direct bag
only one logical operation can be set
failed to decode keybag
policy xpc value is not an array
^_MASReceipt$
Apple Internal
ISO SHA with RSA Signature
OCSP Response Types Extension
com.apple.security.cfder.error
^Versions/[^/]+$
unsupported key algorithmId
SSL hostname does not match name(s) in certificate
Bad Circle DER
v32@?0@\"NSData\"8Q16^B24
SOSCCCopyRecoveryPublicKey
Validity Period
dku
DHKeyMessage (0x0A)
kSecECCurveSecp521r1
Kyber-768-privKey
1.2.840.113635.100.12.47
Apple Accessories Provisioning Authority - 
 <= 
altDSID
Superseded
swcagent
m_ItemList
kSecX25519
%s called with NULL SecKeyRef
Hybrid signature private key creation from data failed
r
1.2.840.113635.100.1.42
1.2.840.113635.100.1.51
Invalid size: %zu
(no error details)
TLS_DHE_RSA_WITH_AES_256_GCM_SHA384
No PeerInfo to encode
SOSCCCopyCircleJoiningBlob
m_TrustedOnly
AnchorAppleTestRoots
newOrder
unknown exception in CSAPI
Trying to remove db at: %@ while it is open
wait for initial sync unimplemented
SecKeyCreateEncryptedData() called with NULL plaintext
5683
1.2.840.113635.100.1.16
1.2.840.113635.100.1.32
1.2.840.113635.100.6.1.2
_privateKey
api
Key encapsulation failed, err=%d for key %@
X448 public key creation from data failed
1.2.840.113635.100.1.100
Alisha
CodeEntitlementDER
2004
v16@?0^{__CFDateFormatter=}8
Distribution
TLS_RSA_WITH_AES_128_CBC_SHA256
Certificate Renewal URL
PKCS12 V2 PBE With SHA1 And 128 Bit RC4
PCS-Sharing
algid:keyexchange:ECDH:KDFX963:SHA384
KeySize
com.apple.security.escrow-update
remote %@ 
is-main-binary
^{__CFArray=}8@?0
typ
min_version
enable_ocsp
SignatureAlgorithmUnknown
CircleAbsent
%llu
cdat
vrfy
AppleMobileStore
com.apple.security.trustedpeers.RecoveryKeySetError
groupID
CKKS4A
failed to read event body
PackageSigning
AppleQuartzTimeStamping
peers have views enabled unimplemented
Cert Sign
1.2.840.113635.100.6.1.13
Root is not temporally valid
 false /* opcode %d */
=?
drop
SecOTRPublicDHKey
1958
backup
/System/Library/Frameworks/CloudKit.framework/CloudKit
c:%@-%@
nw_protocol_metadata_access_handle
kSecurityRTCEventNameCliqueMemberIdentifier
CodeTopDirectory
osgn
ipc
notAfterDate
CFBundleVisibleComponentName
PKCS #12 Safe Contents ID
NotCA
abc
void *KeychainCircleLibrary(void)
Bad generation - proposed circle gencount is older than known circle gencount
7667
legacy_list
Signature verification failed.
BackupBagV0-tomb
SOSCCRegisterRecoveryPublicKey
%lld
Mac App Store
View bag allocation failed
KyberPrivateKey
flags
tlk-piggy
Engram
failed to get custom extension string bytes
value not present for token item
peer_public_key_type
CKDKVS-synchronize
waitfortlkcreation
cusi
algid:encrypt:ECIES:ECDHC:KDFX963:SHA256:AESGCM-KDFIV
1.2.840.113635
lookupDetachedCerts: CTGetSKIDAmfiCMS failed (V1 SignerInfo or error)
Unsupported DER Type
meetsDevleoperIDLegacyAllowedPolicy
Bad Circle Version
/System/Library/PrivateFrameworks/AppleIDAuthSupport.framework/AppleIDAuthSupport
Valid from
signer
defaultAdhocLWCR
PKCS #7 Signed Data
SigningCertNotFound
iMac
kSecEd448
syna
policy \"%@\" is unsupported or requires additional inputs
AppleTestMobileStore
RC5-CBCPad
Description length failed
syncableLive
Warsaw
IOService
Failed to load existing DetachedCertificates.der at %s: %s
NSExceptionRequiresForwardSecrecy
E
void *LocalAuthenticationLibrary(void)
1.2.840.113635.100.6.2.20
1.2.840.113635.100.6.2.22
SecCSPattern
Missing some required field
SOS Disabled for this platform
algid:sign:ECDSA:digest-X962:SHA224
Not Applicable
[name: %-20@] [%c%c%c%c%c%c%c%c%c%c] [type: %-20@] [spid: %8@] [os: %10@] [mid: %10@] [serial: %12@]
akpu
htps
kSecCMSSignDate
too many extensions
algid:sign:HybridSig:digest
 [leaf
failed to deallocate memory\n
q
PKCS #7
i24@?0^{?=Q{?=*Q}}8^B16
srvr
KCSharingGroup(%@, name: %@, participants: %@)
match
watchOS
SecAccessControl: invalid protection
genp
object for key %s failed to convert %s to CFString
%02X%02X:%02X%02X:%02X%02X:%02X%02X:%02X%02X:%02X%02X:%02X%02X:%02X%02X
1.2.840.113635.100.1.11
analyze
<SecOTRPublicDHKeyRef@%p: x: %@ y: %@ [%@]>
1.2.840.113635.100.1.56
DeveloperIDPlusTicket
tls_compliance_policy
CloudIdentity
kSecCMSEncryptionAlgorithmAESCBC
algid:sign:ECDSA:message-X962:SHA224
bundleversion
insert or replace into 
c:%@
PKCS #1 MD4 With RSA Encryption
1.2.840.113635.100.1.39
HomeAppClipUploadService
{requirement=%SO,?optional=%B}
try user credentials unimplemented
Ephemeral-Static Diffie-Hellman
trailing garbage at end of SecAccessControl data
algid:encrypt:ECIES:ECDHC:KDFX963:SHA1:AESGCM
Unable to get public key from generated ECkey
iAPAuthV4
soft_failure_count
escrow
Kyber-768-pubKey
EAPTrustedServerNames
MLDSAPublicKey
{hash=%O}
SignatureDigestSHA512
6666
unknown
All
 union all 
AES-128-ECB
ClientAttestationPublicKey
v24@?0r*8Q16
Properties
PKCS #12 V1 CRL Bag
PKCS #9 X509 Certificate
com.apple.security.sos.off
ldps
/System/Library/PrivateFrameworks/CryptoTokenKit.framework/CryptoTokenKit
1983
dryrun
view
com.apple.PrintKit.PrinterTool
NSCIDRExceptions
PKCS #9 Counter Signature
sosops
Not Valid Before
OU
Ed25519 signature verification failed (ccerr %d)
errors
clique-fetchescrow
iPAddress value is not a string
failed to create EKU data
recryptCert
CodeSigning
SecCodeSignerRemote
malformed fat file, slice %d extends past end of file\n
File does not exist at path: %@
SinglePurposeChainEKU
Q
PKCS #9 Unstructured Name
^(Frameworks/[^/]+\\.framework/|PlugIns/[^/]+\\.appex/|())SC_Info/[^/]+\\.(supf|supp)$
findAntlrPlugin
{?optional=%B}
 set %@
public
JSON
algid:sign:ECDSA:digest-X962:SHA256
kSecKeyKeyExchangeParameterRequestedSize is missing
SystemTrustValidityPeriod
name
Created
l
ML-KEM-1024-privKey
1989
has
/_CodeSignature
^(\\./)?(\\.\\.[^/]+|\\.?[^\\./][^/]*)$
SecDetachedCertificates
BasicConstraints
CodeEntitlements
Time Stamping Certifcate
%@; %d %@; data = %@
ProvoloneFDRSigning
noCACheck
NSAllowsArbitraryLoads
PKCS #7 Digested Data
CreditCards-tomb
Custom CFAllocator for sensitive data that zeroizes on deallocate
unsupported EC curve
<SecKeyRef algorithm id: %lu, key type: %s, version: %d, %d bits (block size: %zu), addr: %p>
owner
defaultPlatformLWCR
unsupported subjectAltName key type
dsid
kill
htsx
1.2.840.113635.100.6.92
dynamicCodeInfoPlist
samples
musr
y
RSA-WRAP bad ciphertext, unexpected session key size
Failed to get version element
short
SecPolicyTeamIdentifier
DetachedCertificatesLookupErrorDomain
com.apple.icdp.record.
CPS URI
Disallowed Characters dictionary parameter is either null or not a string
hasDateConstraints
<%@: [name: %20@] [%c%c%c%c%c%c%c%c] [type: %-20@] [spid: %8@] [os: %10@] [devid: %10@] [serial: %12@]
SecAccessControl data does not encode a dictionary
fclose
0505
BAA-UCRT
alert
TLS_AES_256_GCM_SHA384
atlk
Ed25519 private key creation from data failed
3PMobileAsset
componentVersion
PKCS #9 Signing Time
Views
Non-Repudiation
SecPolicyContext
TrustResultDetails
char
SOSPeerInfo
OTR Signing Key
designated
abcdefghijklmnopqrstuvwxyz1234567890
MarkRepresentation
1.2.840.113635.100.1.70
1.2.840.113635.100.6.1.25.1
apple
omissions
CTGetAKIDFromCertificate failed for %@: %d
SOSCCAcceptApplicants
SecTrustPinningRequired
security.mac.amfi.qa_root_certs_allowed
ticket_lifetime
SecPolicyName
Apple System Integration 2 Certification Authority
AppleXROSApplicationSigning
nsurlsessiond
SFAnalyticsActivityTracker user called stop w/o calling start
KCPairingChannel
bin1
Manatee
Public Key isn't available, this peer is in the circle, but invalid. The iCloud Password must be provided to keychain syncing subsystem to repair this.
SSLMinProtocolVersion
SecKeyVerifySignature() called with NULL signedData
OCSPSigner
/.
SOSCCFetchCompatibilityModeCachedValue
algid:sign:RSA:digest-PSS:SHA224:SHA224:24
entitlement[
SecDetachedCertificatesLookup: lookupDetachedCertificatesFileForExecutable not available
data
EC signature verification failed (ccerr %d)
jwk
com.apple.security.secureobjectsync.viewschanged
afps
algid:encrypt:RSA:raw-cc
TrustResultNotAfter
{requirement=%s,cdhash=%O}
events type invalid
com.apple.security.keychain
SOSFullPeerInfo.m
fresh
action
SecKeyVerifySignature
algid:keyexchange:ECDHC:KDFX963:SHA384
UnparseableExtension
responses
UseXPC
AcmeError
permanent-identifier
pending
on-system-volume
SOSCCCopyGenerationPeerInfo
u_TokenRawItems
1.2.840.113635.100.1.65
remotesigner
softfail
Photos
GrayListedKey
TrustQWACValidation
lookupDetachedCerts: file lookup failed: %s
soft_failures
PKCS #9 Friendly Name
TKUserSecretTriesLeftErrorKey
certificateSerial
0404
IssuerNameConstraints
map::at:  key not found
<cert(%p) s: %@ i: %@>
failed to create identity (check input values)
Unable to get number from data
kSecCMSAllCerts
SFA: %@ - %@
EscrowRecord
'permanent-identifier' type not supported by this server
notarized
AnchorTrusted
Failed to encode intermediate certificate entry
PKCS #1 MD2 With RSA Encryption
PCS-MasterKey
sox 
107
handle
kern.boottime
PKCS #9 X509 CRL
PCS-Maildrop
iPhoneProvisioningProfileSigning
Execution has encountered an unexpected state
SFAExclude
Code Signing Certificate
volm
algid:encrypt:RSA:OAEP:SHA256:AESGCM
1004
Hybrid Composite ML-DSA-87 RSA-3072 With SHA-512 (draft-13)
tLastKVSKeyCleanup
 [%@]
password
{symlink=%SO,?optional=%B}
unexpected system key type %d
ValidityPeriodMaximums
validateResource
Mach-O thin (
SOSCCCopyValidPeerPeerInfo
account was empty or not a CFString
guest
events
PKIX User Notice Qualifier
SecKeyCreateDecapsulatedKey
com.apple.security.analytics
Lost Password URL
Failed to create public key from data %@
wkey
kSecAttrApplicationTag
Failed to parse version integer
com.apple.security.trustedpeers.container
hasPendingKey
This certificate is not yet valid
kSecKeyWrapPGPECWrapDigestSHA256KekAES128
algid:sign:ECDSA:digest-X962
MDLTerminalAuth
  Chain1 anchor is %s
Invalid parameters: executablePath and cmsData are required
SFAnalyticsActivityTracker user called start twice
1.2.840.113635.100.6.1.29.3
KT
?,
PKIX CRMF Registration Control, PKI Publication Info
SOSCCRequestToJoinCircleAfterRestore
code signing internal problem: diskRep returned no allowedResourceOmissions
TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384
NSAllowsLocalNetworking
B24@?0^{__OpaqueSOSPeerInfo={__CFRuntimeBase=QAQ}^{__CFDictionary}^{__CFData}^{__CFDictionary}^{__CFString}^{__CFString}q^{__CFString}BB^{__CFDictionary}}8^^{__CFError}16
com.apple.cloudd
SecKeyCreateEncapsulatedKey() requires sharedKey output parameter
algid:encrypt:RSA:OAEP:SHA512:AESGCM
algid:keyexchange:ECDH
algid:kem:kyber
com.apple.ProtectedCloudStorage
Unsupported %@: %@ (converted value: %@
algid:sign:ECDSA:digest-RFC4754
/System/Library/Security/PQCCertificates.der
\\%02X
TrustExpirationDate
Invalid datetime character
Mach-O (unrecognized format)
radarNumber
versions not parsing: %@
@
apple-internal
kSecKeyWrapPGPSymAlg
kSecKeyWrapPGPWrapAlg
<%@: oid: %@ name: %@ options %@
SecSystemKeychainAlwaysSupported
NSString *getTKClientTokenParameterForceSystemSession(void)
Ignoring DHKey message
ML-KEM-768-pubKey
Failed to encode root SEQUENCE
com.apple.managedconfiguration.profiled
includeV0
TrustExtendedValidation
] = 
 < 
Explicit Text
iTunes Store URL Bag
new architecture offset underflows
leaf at index %lu
Leaf AKID does not match intermediate SKID for leaf at index %lu
normal
 (
NSNumber
PKIX CRMF Registration Control, Old Certificate ID
Netscape S/MIME KEA
algid:sign:ECDSA:digest-RFC4754:SHA224
 order by %@
SOSSetNewPublicBackupKey
u_TokenSession
114
1.2.840.113635.100.6.51
Certificate User Picture
o
Email Address
Unable to create public key bytes
1992
ExceptionResetCount
SFSQLite.m
thread-local-client-debug
enable_false_start
<SSLContext(%p) { ... }>
publicKey
cannot open file %s, errno=%d\n
lookupDetachedCerts: successfully looked up %ld certificates
dynamic-codesigning
Security
tlks
CTKKey
failed to create data
Error adding shared password
Unknown data encoding, expected CCDER_CONSTRUCTED_SET
{%O=%d}
Unable to get public key
Signature cryptographic verification failed
aku
v24@?0^{__CFString=}8^{__CFString=}16
1.2.840.113635.100.1.10
1.2.840.113635.100.6.55.1
AllowAccessoryUpdateSigningBeta
AcmeLocation
exists
Extra space in sequence
ATV value is not a Printable or UTF8 string
WeakKeySize
1.2.840.113635.100.6.29
xpc_path array count == 0
GET
termsOfServiceAgreed
com.apple.security.sfanalytics.samplers
SecCertificate
failed to get basic constraints path length value
_CFHostIsDomainTopLevelForCertificatePolicy
com.apple.trustd
qualityOfService
JSON:%@
failed to der encode certificate
HybridSig-%@-privKey
binn
1.2.840.113635.100.6.49
1.2.840.113635.100.14.3
<SecKeyRef:('%@') %p>
com.apple.secelemtoken
AppleEscrowService
TrustResultNotBefore
newNonce
SecStaticCode::addDetachedCertificatesFromData(): Failed to parse
componentName
WeakSignature
-wal
SSLSessionConfig
failed to encode NTPrincipalName
htpx
kSecClientIdentifier
com.apple.CalendarAgent
rejection_rate
PKCS #9 S/MIME Capabilities
SOSCCLoggedIntoAccount
CompanyName
NotarizationDate
on-authorized-authapfs-volume
algid:sign:ECDSA:digest-RFC4754:SHA256
algid:encrypt:ECIES:ECDH:KDFX963:SHA512:AESGCM-KDFIV
/*@0x%x*/
com.apple.security.padding
PKCS #12 RSA Encryption with 128 Bit RC4
foo
Excluded Subtree General Name
1976
1.2.840.113635.100.1.21
SOSViewResultCode=%d
Not Valid After
1.2.840.113635.100.11.3
pid
Failed to decode certificate
PKCS #9 Local Key ID
section
algid:encrypt:ECIES:ECDH:KDFX963:SHA256:AESGCM
Certificate Authority CRL Download URL
No
MacAppStoreInstaller
Failed to encode [2] EXPLICIT tag
$in
Development
circleOp
CFSecRecoveryKey
operation: %@ acl:%@\n
algid:sign:ML-DSA:message
otr
TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256
Certificate Subject Logo
SOSCCCopyInitialSyncData
Name constraints violated
I16@?0i8i12
count(*) as n
Certificate Homepage URL
uniformResourceIdentifier
CoreFoundation error
eventType missing
PKCS #9 SDSI Certificate
SecKeyCreateMLDSASignature
void *SecurityFoundationLibrary(void)
vwht
IPA_
installer package bundle
v24@?0Q8@\"NSString\"16
TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA
ST
truststore
{cdhashes=%O}
clique-legacy
loggedout
ats_required
allocate memory for SecAccessControl
ECPublicKey
visionOS
iPhone
ManifestHash
oid
v24@?0@\"SecItemCurrentItemData\"8@\"NSError\"16
anchorHash
Description
max_version
%@: X448 DH failed (ccerr %d)
Developer
NSParsedCIDRMaskKey
EDPSigning
architecture
enabled
appleCodesigningHashAgilityAttribute
SOSCCCopyViewUnawarePeerInfo
1.2.840.113635.100.1.34
PKCS #5 Password Based Encryption with SHA1 and DES CBC
SOSCCPushResetCircle
Failed to create dictionary
not 
com.apple.security.LegacyAPICounts
Class getAAFAnalyticsEventSecurityClass(void)_block_invoke
ML-KEM public key creation from data failed
.app
areCertChainsSimilar: Organizational unit (Team ID) mismatch in leaf certificate
/
kern.entropy.health.adaptive_proportion_test.max_observation_count
attestation not supported by key %@
SecIdentity
PasswordDisallowedCharacters
1967
cert_request_type
v24@?0@\"OTCustodianRecoveryKey\"8@\"NSError\"16
policy \"%@\" requires a string value for the %@ property
platform = %d
host
unsigned short
views
HybridSig LAMPS13-MLDSARSA private key creation from data failed
eapClient
failed to create xpc_object from policy oid
{basic_string<char, std::char_traits<char>, std::allocator<char>>={?=(__rep={__short=[23c]b7b1}{__long=*Qb63b1})}}24@?0r^v8r^v16
re-launch
disableSampling
Cannot reject non-applicant
InCircle
u_AuthUI
macOSProfileApplicationSigning
allowedBuilds
SFA-LastMatchRule-%@-
defaultAppStoreLWCR
Contacts
esiz
ClientAttestationData
Failed to encode [0] EXPLICIT tag
n
1.3.6.1.5.5.7.3.4
algid:encrypt:ECIES:ECDHC:KDFX963:SHA224:AESGCM-KDFIV
MissingIntermediate
1.2.840.113635.100.6.30
SecPinningDb
DisabledForCAs
2011
SoftFailure
NSString *getkSecurityRTCEventNameCliqueMemberIdentifier(void)
DES-MAC
OSStatus returned in error code
PasswordMinLength
1969
fmt
Invalid date: %i, %i, %i, %i, %i, %i, %i
Numeric string allocation failed
matched 
SOSCCCopyNotValidPeerPeerInfo
1.2.840.113635.100.1.72
viewactioncode
anchorreq
minimum_signature_algorithm
C
SFAnalytics
AES-256 Key Wrap
Hybrid Composite ML-DSA-87 RSA-3072 With SHA-512 (draft-07+)
CertificatePolicy
internal
AES-256-CBC
m_Limit
1110
Key is listed as untrusted
requested signature size is too long for slice: %d\n
Failed to sign peerinfo for peer
3333
The dictionary parameter 'characters' is either null or not a number
pinningQA
PKCS #12 RSA Encryption with 40 Bit RC4
failed to encode iPAddress
kSecKeyWrapPGPECFlags
 [ca%ld
SHA-384
m_LimitOne
RSApubkey wrong size of buffer to encrypt
policyConstraints
com.apple.securityd.ckks
sct_enabled
Null BackupSliceKeyBag
kSecCMSHashAgilityV2
Escrow
reference is nil
v24@?0^v8{Architecture=ii}16
TLSProbeExperiment
Watch OS
OctagonPublicEncryptionKey
sens
Failed to create certificate from auto-looked-up certificate data at index %ld
algid:sign:ECDSA:message-X962:SHA1
ML-DSA signature verification failed (invalid data inputs)
subarchitecture
.cstemp
KeychainV0
algid:sign:EdDSA:message-Curve448:SHAKE256
KEM Key decapsulation failed, err=%d for key %@
uniqueClientID
receiverPeerID
ticket_received
algid:sign:RSA:message-PSS:SHA256:SHA256:32
MMCS
symbol %s is missing
/module\\.map$
LaunchConstraints-responsible
Error iterating sequence: %d
\n\t\t<A:[
subj
fetchFailed
BSD Major
SecDetachedCertificatesLookup: %s
Note
enable_fallback_attempt
], A:[
com.apple.security.seckey.setoken.attestation-nonce
trailing junk after complete
RSAsign wrong input data length
1.2.840.113635.100.1.62
^(Versions/)?\\.DS_Store$
eventTime
B40@?0^{dispatch_data_s=}8Q16r^v24Q32
ANSI X9.57 DSA Signature
failed to decode encoded certificate
code signing internal error: trying to write Mach-O component directly
Failed to allocate encoding buffer
status_returns
Hybrid signature public key creation from data failed
RevealSignatureMessage (0x11)
OtherSyncable-tomb
Certificate missing a name
q24@?0@\"DetachedCertificateEntry\"8@\"DetachedCertificateEntry\"16
com.apple.security.keychain.sharing
PCS-CloudKit
failed to copy encryption public key bytes
subject input incorrect: 2 values required in ATV array
1.2.840.113635.100.12.44
AKS Lock Assertion Queue
/AppleInternal/
Failed to extract SKID from CMS blob: %d
versions on rule
csparser.bundle
SOSCCGetLastDepartureReason
runtime-version
plist encode failed
u_NoAuthUI
FactoryDeviceCertificate
errorDomain
return=%@
Certificate Policies
PKCS #12 PBE With Sha1 and 128 Bit RC2 CBC
com.apple.security.sos.transport.error
standard
2003
hardfail
CliqueStatusPending
OCSP Service Locator Extension
object %@ is not a data
Peer not signed to encode
Mail
kSecAttestationIdentity
PasswordCantStartWithChars
debug
RetirementDate
stableTrustedDeviceIDStatus
SOSCCCopyEngineState
algid:encrypt:RSA:OAEP:SHA512
1202
1.2.840.113635.100.6.27.11.1
IODeviceTree:/options
E-Mail Protection Certificate
Leaf certificate is a CA
requested signature size is too long for slice
RingState
bundle
TransparencyTopic
kSecCMSEncryptionAlgorithmDESCBC
msna
defaultDeveloperIDLWCR
afp 
Failed to create policy
do not 
Failed to decode root DER: %d
Verisign User Notices
SOSCopyECWrappedData
SOSCCCopyApplicantPeerInfo
Object Signing CA
nntp
DES-OFB
invalid constraint
EC public key creation from data failed
Bad Format of Peer Info DER
SecKeyIsAlgorithmSupported
delete from %@ where %@
EnableSecureObjectSync
force
m_HostOrSubdomainOfHost
HybridSig LAMPS8-15 private key creation from data failed
.lproj
CKReference
clique-leaveClique
clique-recovery
Health
SSLContext
0606
Country or Region does not match expected name
AccessoryPairing
Unexpected type
ldap
1968
{rules={'^version.plist$' = #T%s = #T%s = {optional=#T, weight=1000}%s = {omit=#T, weight=1100}}}
.framework
Failed to load nested DetachedCertificates.der at %s: %s
AppleTV
Passwords-tomb
CriticalExtensions
Generation Count for new circle is too old
%02X
1.3.6.1.5.5.7.3.2
eventFilter
eventType
SecPolicyRootDigest
SecCSResourceAdded
d
NSExceptionMinimumTLSVersion
ECDSA Public Key
certtkid
com.apple.setoken
%@R: %@
Other Name
SecPolicyIntermediateMarkerOid
QWACValidation
too large data for key %s
have_prerecord
v24@?0^{__CFString=}8^v16
Failed to encode X962 signature
ATV OID of unsupported type
1.2.840.113635.100.1.101
1.2.840.113635.100.15.3
AssetReceipt
SubjectOrganization
1.2.840.113635.100.1.50
result block
VersionPlatform
SWTransparencyTopic
ContinuityUnlock
algid:sign:RSA:digest-PKCS1v15:SHA256
1.3.6.1.5.5.7.3.31
com.apple.dataaccess.dataaccessd
NSSet
Statement not reset after last use: \"%@\"
long long
Class get_SFECKeyPairClass(void)_block_invoke
kern.entropy.health.repetition_count_test.failure_count
com.apple.email
EC private key creation from data failed
Unable to build chain to root (possible missing intermediate)
Launch-%@
1.2.840.113635.100.1.103
FMiP
Policy constraints violated
String allocation failed
{symlink=%s}
odel
SOSCCRequestToJoinCircle
LaunchConstraintResponsible
$self.identifier
Failed to sign public key hash for peer
Unknown 
TKErrorDomain
SecCSGuestAttributes
PKCS #12 RSA Encryption with Triple DES
ModelName
SignatureDigestSHA284
1.2.840.113635.100.6.2.26
iTunesStoreURLBag
%@, %@
PPMAggregatorConfigSigning
Encipher Only
Failed to encode leaf certificates SEQUENCE
(null)
SPKI-SHA256-BASE64
areCertChainsSimilar: Anchor type mismatch (Apple CA vs non-Apple CA)
errorDescription
X520 Common Name
Cannot accept non-applicant
PICache
TLSv1_3DES_fallback
1.2.840.113635.100.6.59.4
ghostbust
algid:sign:RSA:digest-PKCS1v15:SHA512
Pinning required but not used
files
The dictionary parameter 'At Most N Characters' is either null or not a string
{rules={'^.*' = #T%s = {optional=#T, weight=1000}'^.*/.*\\.pkg/' = {omit=#T, weight=10000}}}
action invalid type
IFMajorVersion
com.apple.security.securityd
%
CRL Issuer
anchor
-
Certificate Policy Constraints
ECDHKeyExchange wrong input (%d)
ValidLeaf
ValdateUpdate
filediskrep
PKCS #5 Password Based Encryption with MD5 and DES CBC
OctagonPublicSigningKey
hsa2PB
MLKEMPublicKey
SecTTR
mediaplaybackd
%@ asc
ViewNotQualified
1977
Failed to wrap key
failed to establish account
OctagonRKTLKOwnershipProof
SOSCCCopyRetirementPeerInfo
SOSCCViewSet
<%s>
ProcessingError
otrtimer
1.2.840.113635.100.4.1.2
^{__CFArray=}16@?0^{__CFDictionary=}8
user_label is nil
Invalid data pointers
Encoding failed
Error copying shared password
com.apple.keychainsharingmessagingd
warning
imps
AppleSSLService
SOSCopyECUnwrappedData
key
idnt
0707
double
com.apple.KCSharingMessagingdConnection.xpcConnection
PKCS #12 Cert And CRL Bag ID
no recovery key found in %@
failed to encode TBS
Got certificate: %@
DiskRepInfo
flowID
CliqueStatusAbsent
Certificate Scope-of-Use Extension
scrp
HybridSig LAMPS13-MLDSARSA public key creation from data failed
1.2.840.113635.100.1.86
Failed to allocate key data
accessGroups
CTGetSKIDFromCertificate failed for %@: %d
PasswordMaxLength
sha256
SecOTRFullDHKey
lookupDetachedCerts: SKID lookup failed or chain incomplete: %s
OctagonPairing
kSecAccessControlUserPresence can be combined only with kSecAccessControlApplicationPassword and kSecAccessControlPrivateKeyUsage
algid:sign:ECDSA:digest-X962:SHA1
csinterp
lastUploadTime
Analytics/%@.db-wal
1.2.840.113635.100.6.1.12
Unexpected error detail
cdpContextTypeRecoveryKeyNew
1.0.18013.5.1.6
Leaf certificate's AKID does not match intermediate certificate's SKID
machineID
enable_raw_external_pre_shared_keys
*24@?0Q8*16
0123456789.
OTRSession
1.2.840.113635.100.1.115
Apple iPhone Device CA
PKCS #12 Mode IDs
lookupDetachedCerts: no signature available
csresource
session_renewed
C%p F%p
...(%db)
_rsam
input file too large: %lld bytes\n
insert or replace into Properties (key, value) values (?,?)
Trusted EAP hostname does not match name(s) in certificate
fraction without digits
Constraint too large
Intermediate AKID does not match root SKID for leaf at index %lu
v24@?0@\"NSDictionary\"8@\"NSError\"16
octagon-cdp-status
Signature Data
addr
1.2.840.113635.100.6.1.30
abcdefghkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789
v16@?0^{__OpaqueSOSPeerInfo=}8
keys
AppleIDAuthority
SoftwareSigning
ML-DSA signature verification failed (invalid signature length)
Kern return error
SecTask
com.apple.private.octagon.secureelement
Key Identifier
Ed448 private key creation from data failed
intermediate
Rockwell
NULL certificate
invalid
algid:encrypt:RSA:OAEP:SHA224
1959
verifySignatureEmbeddedPolicy: verification succeeded with auto-looked-up certificates
NSParsedCIDRAddressKey
.
%04d%02d%02d%02d%02d%02dZ
kSecCMSSignDetached
1988
1964
2.23.146.2.1.6
SigningCertNotTrusted
cert
algid:encrypt:ECIES:ECDH:KDFX963:SHA1:AESGCM
The password's length parameters make no sense ( is max < min ?)
2
failed to submit order
Failed to encode root certificate entry
sslClient
MacSoftwareUpdate
OCSP Archive Cutoff Extension
NonEmptySubject
^Contents$
B16@?0^{sec_protocol_metadata_content=^v^?^v^?SS***[16C]^{sec_array}^{sec_array}^v^{dispatch_data_s}^v^{dispatch_data_s}^{sec_array}^{sec_array}^{sec_array}^{dispatch_data_s}^{sec_identity}^{sec_trust}***QQQQQQQSQQQQQQQS*b1b1b1b1b1b1b1b1b1b
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384
AutoUnlock
RSAencrypt wrong input size (err %d)
1.2.840.113635.100.12.12
SubjectKeyID/AuthorityKeyID mismatch in chain
<Changes: {\n
QCSCompliance
code signing internal problem: unknown exception thrown by validation
Failed to encode version
SHA-256
subjectAltName
bin2
PasswordCharacters
1.2.840.113635.100.1.55
Common Name does not match expected name
kSecUseHardwareBoundKey
updateType
failed to encode extensions
bin0
Invalid universal time year between 50 and 70
Failed to encode date.
com.apple.utilities.sqlite3
Certificate Private Key Usage Period
=
-journal
gs.apple.com
sos_analytics
CRL Sign
Potluck
UCRT
One or more unsupported critical extensions found.
iPhone Developer
Legacy
1963
Password type does not exist.
timestamp
eppc
UTCTimeNoSeconds
1.2.840.113635.100.14.2
_attestationCRKey
com.apple.installer.osinstallersetupd
TLSv1_fallback
O
%@: algorithm not supported by the key %@
trustedKeys
CFBundleDisplayName
kSecECCurveSecp256r1
SMIME
%@-shm
No aks bag to load
PKIX CPS Pointer Qualifier
ECpriv sharedsecret: bad public key (err %d)
DeveloperIDInstaller
Mac App Distribution
versions
peer_authentication_optional
event_type
acmeServerURL
canonical
enable_resumption
1.2.840.113635.100.1.113
v32@?0@\"NSString\"8@\"NSNumber\"16^B24
NSString
Apple TVOS
copy peer peer info unimplemented
Kyber public key creation from data failed
algid:sign:RSA:digest-PKCS1v15
sync
developer-mode
iPhone Distribution
notes
enable_ech
1994
1.2.840.113635.100.1.98
UniversalFileOffset
PKCS #1 MD5 With RSA Encryption
UnknownMessage
attestationChain
FleetSampleRate
NO
Unused
Skipjack CBC64
ID for %@-%@
1.2.840.113635.100.1.121
attribution
%F
SE-PTC
trailing junk after keybag
++
newPublicBackupKey
attr: %@: %@
cdhash
bskb-backup
Found unknown critical extensions
yMdHms
KCSharingGroupUpdateInfo(%@, name: \"%@\", new participants: %@)
certificateExtensions
Attempting to create SecKeyRef with NULL key_class
preserve-afsc
non-Apple CA
SignatureDigestMD4
csrChallengePassword
algid:sign:EdDSA:message-Curve25519:SHA512
weight
octagon-setrecoverykey
1.2.840.113635.100.1.63
1.2.840.113635.100.6.22
requirement-data
Mac Developer
prp
k
One or more certificates have been revoked.
UNIX error exception: %d
ExpName
v32@?0@\"NSString\"8@\"SFAnalyticsMultiSampler\"16^B24
Inflating persistent ref
-----BEGIN %s-----\n
The dictionary parameter 'number of groupds' is either null or not a number
unable to create trust ref
/*legacy*/
com.apple.security.experiment
SecKey
RevocationValidUntil
enable_tickets
ATV OID encode failed for %@
<SecOTRFullDHKeyRef@%p: x: %@ y: %@ [%@]>
ValidRoot
Certificate Policy Mappings
Qualifier
sign
identifier 
all
accepted
uptime
Peer is not retired
<CKKSPCSIdentityQuery(%@): %@>
Ed448 signature verification failed (invalid signature length)
desc
1.2.840.113635.100.6.1.29.2
pragma synchronous = %@
106
lwcr-responsible
SecSoftLink.h
en_US_POSIX
malformed mach-o file, LC_CODE_SIGNATURE does not point to end of file\n
PKCS #12 Cert Bag IDs
requestEnsurePeerRegistration
1.2.840.113635.100.1.31
kSecAttrIsPermanent
General Name
1.2.840.113635.100.1.105
TrustQCStatements
timestamp-omit-certificates
files2
Mac OS
CIRCLE:    [%20@] UserSigned: %c
WiFi
^{__CFData=}8@?0
65
enforcement
SecItemAdd: %d
ccpbkdf2_hmac failed: %d
\"signature\":\"%@\"
v16@?0Q8
2008
1.2.840.113635.100.6.1.5
3456789
Certificate Revocation URL
SOSCCSetUserCredentialsAndDSID
crle
SecPolicy
1.2.840.113635.100.4.13
MISSI DSS Algorithm
com.apple.security.secureobjectsync.recoverykeychanged
repeatAfterSeconds not number
Failed to create hash for peer applicant
%@: Failed to get public key from private key
 %d
title
v32@?0@\"NSDictionary\"8@\"NSArray\"16@\"NSError\"24
/System/Library/Frameworks/CFNetwork.framework/CFNetwork
waitforunlock
basic_string
com.apple.managedclient.pds.Certificate
1.2.840.113635.100.1.9.1
csreq
ticket_offered
lifetimecontrol not supported for key %@
failed get public key
1.2.840.113635.100.1.120
tag/length decode failed
requirements
Root element is not a SEQUENCE, tag=0x%llx
pdmn
algid:sign:RSA:digest-PSS:SHA384:SHA384:48
algid:sign:ECDSA:message-RFC4754:SHA384
aks_load_bag failed: %d
Signature Algorithm
PKCS #12 PBE With Sha1 and 40 Bit RC4
1982
SecCSResourceHasSidebandData
session_resumed
cfdata_error_request_returns_cfdata
sdat
testsEnabled
Unexpected floating point number type: %@
repetition_failure_count
id-aa-timeStampToken
chain
notarization
Failed to decode skid
parentKeyUUID
UseTokens
is.autonavi.com
Ed448 public key creation from data failed
Failed to get key out of trust ref, was it evaluated?
SecuritydXPCClient
Byte string
algid:sign:ECDSA:digest-RFC4754:SHA512
AST2
Anchor is not an Apple root
ASAuthorizationPasswordProvider
TrustResultValue
Property
kern.entropy.filter.total_sample_count
HomeKit
This certificate is valid
non-CA cert does not support path len
algid:keyexchange:ECDH:KDFX963:SHA224
requireCT
and
MISSI DSS Algorithm (Old)
Critical
Attempt to create remote identity from key-only proxy
backupKeybagPath
entitlements-DER
CK
PBUNSET
HybridSigLAMPS8_15PublicKey
PasswordDefaultForType
ChainLength
begin exclusive
NSAllowsArbitraryLoadsInWebContent
failed to add key to keychain: %@
kOddCompactDataMessage (0x31)
 >= 
AMFITrustedKeys
Expected INTEGER for compatibility_version, tag=0x%llx
SecDebugErrorMessages
JSONObject
kpid
trustRefTime
details
AcmeStatus
v20@?0I8^{DynamicHash=^^?i}12
MachineIDKey
ViewUndefined
LocalAuthentication is not available
/Library/
com.apple.private.amfi.can-load-cdhash
entitlements
Key Compromise
TKClientTokenSession
1972
PKCS12 V2 PBE With SHA1 And 40 Bit RC4
m_SubjectContains
com.apple.mediaplaybackd
HybridSigLAMPS13MLDSARSAPublicKey
Failed to extract public key from private key
1.2.840.113635.100.12.48
CodeRequirements-1
yyyy-MM-dd'T'HH:mm:ssZZZZZ
1.3.6.1.5.5.7.3.3
failed to encode extension data
skid
1.2.840.113635.100.1.44
AppleSMPEncryption
RollIdentityOnMIDRotation
v32@?0@\"NSData\"8@\"NSDate\"16@\"NSError\"24
DES-ECB
DigestMismatch
1212
1.2.840.113635.100.1.102
AppleServerAuthenticationNoPinning%@
eventType not a string
kSecurityRTCEventNameOctagonTrustLost
%@: Unable to get public key
admin
{+%O, %O = 'OS X SDK version before 10.9 does not support Library Validation'}
Expected [1] EXPLICIT tag, got 0x%llx
hardwareBound
 NOT
updatedGroup
Signature doesn't validate
algid:sign:ECDSA:message-RFC4754:SHA512
Blob failed to decode
shareURL
1.2.840.113635.100.1.30
intermediate of leaf at index %lu
secttr
rules config format version %d because %@
v40@?0@\"NSData\"8@\"NSString\"16@\"NSData\"24@\"NSError\"32
AES-192-ECB
No iCloud identity PeerInfo found in circle
Invalid key operation %d
ntPrincipalName
Failed to encode compatibility_version
wrapppedTLK
sentTime
octagon-createcustodianrecoverykey
Privilege Withdrawn
ApplePayQRCodeEncryption
sysb
ocsp
event
error
CertificateTransparency
unable to create trust plist
total-signatures
Failed to create certificate from detached chain data
ApplePay
1.2.840.113549.1.9.1
110
1234
DuplicateExtension
challenges
failed to encode extension string
%@.%@
NoNetworkAccess
1.2.840.113635.100.1.46
B16@?0^{sec_protocol_metadata_content=^v^?^v^?SS***[16C]@@@@@@@@@@@@***QQQQQQQSQQQQQQQS*b1b1b1b1b1b1b1b1b1b1b1b1b1b1^?^?^v^vb1b1b1^{__CFSet}{os_unfair_lock_s=I}}8
radarnumber
Unsupported unboxing type: %@
Cessation Of Operation
1.2.840.113635.100.1.114
1.3.6.1.5.5.7.3.1
1.2.840.113635.100.1.73
%c:%@ 
{%s=%d,%s=%d}
%02.2x
info-plist-hash
supported
kTCCServiceSystemPolicyAllFiles
\\[]{}().+*?^$|
Apple Developer
appleCodesigningHashAgilityAttributeV2
General Names
123654
 /* exists */
kern.entropy.health.adaptive_proportion_test.failure_count
]>
cenc
1.2.840.113635.100.1.57
accessGroup
unsupported subjectAltName value type
requestedSize
ComponentVersion
ENTER
componentID
configVersion missing
1.2.840.113635.100.6.1.6
blob
DeveloperID Date parsing: extension not found
Ed448PrivateKey
sharedInfo
PENDING
retryafter
TPStableTrustedDeviceID
slnr
failed to create xpc_array of certificates
v16@?0@\"NSObject<OS_xpc_object>\"8
 absent 
get-task-allow
Tap-To-Radar
com.apple.WebKit
1
Unsupported %@: %@
<SecKeyRef remoteKey: %@>
NoMessage
x5c
/tmp/AcmeAtt_%@
security.mac.amfi.developer_mode_status
startup_done
<SecKeyRef %@ algorithm id: %lu, key type: %s, version: %d, addr: %p>
2013
Unknown string encoding
^Versions$
CodeRequirements-5
linker-signed
HTML
data required for wrapping
Kyber-1024-privKey
<SecKeyRef 
1.2.840.113635.100.6.57.1
SecStaticCode::addDetachedCertificatesFromData(): Failed to merge
)
CFBundleName
NIAPRemovesBuiltinATSExceptions
(select %@, %@ from (%@) order by %@ desc limit %lu)
out of memory
0123456789ABCDEF
algid:encrypt:ECIES:ECDH:KDFX963:SHA224:AESGCM-KDFIV
Need a string of characters; password must only contain characters in this string
com.apple.WebKit.Networking
c
SecRandom falied!
Class getLAContextClass(void)_block_invoke
RCSEncryption
NSExceptionRequiresNIAPTLSPackageVersion
Unable to decode public key: %@
SOSCCTryUserCredentialsAndDSID_internal
algid:encrypt:ECIES:ECDHC:KDFX963:SHA224:AESGCM
030379
VersionMin
1123
SignatureHashAlgorithms
OS X Shared Library Cache (unknown type)
PKCS #1 SHA-1 With RSA Encryption
failed to create xpc_array
basicConstraints
identifiers
v56@?0@\"NSString\"8@\"NSData\"16@\"NSData\"24@\"NSData\"32@\"NSData\"40@\"NSError\"48
Ed448PublicKey
Organizational Unit does not match expected name
preserve-metadata
digest-algorithms
group
Reached maximum count of authentication attempts\n %@
SecOTRPublicIdentity
1010
Apple iPhone OS Provisioning Profile Signing
Certificate violates issuer policy constraints
appID
teamidentifier
i8@?0
Null Public Key
logging
can't write to output file (len: %d): %s, errno=%d\n
/DetachedCertificates.der
\n
Failed to provide key data to SecKeyCreateWithData
com.apple.AddressBookSourceSync
id-aa-signing-certificate
SOSCCProcessSyncWithPeers
nextUpdate
-shm
xpc_dictionary_create returned NULL
I36@?0@\"NSString\"8q16@\"NSDictionary\"24I32
1.2.840.113635.100.6.1.33
2000
Mach-O universal (
Title
CRL Distribution Points
nega
0101
1.2.840.113635.100.12.18
v20@?0I8^{__CFError=}12
MD2
pending-check
K
Certificate exceeds maximum temporal validity period
{rules={'^version.plist$' = #T%s = #T%s = {optional=#T, weight=1000}%s = {weight=1010}%s = {omit=#T, weight=1100}},rules2={'^.*' = #T'^[^/]+$' = {nested=#T, weight=10}'^(Frameworks|SharedFrameworks|PlugIns|Plug-ins|XPCServices|Helpers|MacOS
1.2.840.113635.100.1.110
newschema
AcctUUID
ML-KEM private key creation from data failed
1957
nameConstraints
Unknown boolean encoding
daysSinceSuccess
CRL
ccecies_encrypt_gcm failed %d
anchorsOnly
leaf
defaultDevelopmentLWCR
u_CredRef
Internal error (XPC failure)
<CKKSExternalTLKShare(%@): recv:%@ send:%@@>
no error pointer provided
Unknown data encoding, expected CCDER_CONSTRUCTED_CFSET
bound
Key Encipherment
B48@?0@\"TKClientTokenSession\"8^{__CFDictionary=}16^{__CFDictionary=}24^{__CFDictionary=}32^^{__CFError}40
v20@?0i8@\"NSError\"12
policy \"%@\" could not be created from the given properties
backupPeerIDList
failed to encode basic constraints extension
algid:sign:RSA:message-PSS:SHA384:SHA384:48
1103
1.2.840.113635.100.6.1.14
magic
%@-wal
Subject Key Identifier
v16@?0q8
1.2.840.113635.100.1.130
/System/AppleInternal/
ats_trust_policy
TLS_RSA_WITH_AES_128_CBC_SHA
PKCS #12 Secret Bag ID
DeviceOwnerAuthentication
%@: Ed25519 signing failed (ccerr %d)
AwaitingSignature
1.2.840.113635.100.1.47
teamid
code-signing-flags
kSecCMSSignedAttributes
+
108
1970
RecoveryPublicKey
0123456789abcdef
tls_delegated_credentials_enabled
failed to create xpc_array for policy
Strong Crypto Export Approved
SOSCCSendToPeerIsPending
kSecEd25519
2010
StatusCodes
finalize
attribute invalid type
Our GX is bigger, resending DH
challengeToken
dbg-
bsiz
ipp 
5252
thisUpdate
LeafSPKISHA256
events key missing
com.apple.SecureTransport.early_fail.%ld
1.2.840.113635.100.12.9
/tmp/AcmeCsr_%@
B24@?0^v8^^{__CFError}16
PKCS #1 SHA-384 With RSA Encryption
0
X25519PrivateKey
algid:encrypt:ECIES:ECDHC:KDFX963:SHA384:AESGCM-KDFIV
Unable to parse known extension
leaf-certificate-skid
Caller-specified eContentType
com.apple.mobilesafari
Policy Qualifier #%d
atyp
securityd
AES-128 Key Wrap
Chain exceeded constrained path length
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 '()+,-./:=?@
TrustRevocationChecked
SecRequestClientIdentity: subject array has missing value or wrong type for %s key
pop3
0909
1979
1.2.840.113635.100.1.60
1.2.840.113635.100.1.82
TKErrorCode getTKTokenNotFoundAndRegistered(void)
B12@?0I8
success
first-launch
pool allocation failure
x
1.2.840.113635.100.6.1.7
macho
PKCS12 V2 PBE With SHA1 And 128 Bit RC2 CBC
SSL server
OSStatus
SubjectPublicKeyInfoHash
CKArchivedAnchoredPackage
%s CFData allocation failed
RSA private key creation from data failed
alg
rsa_priv_crypt failed, ccerr=%d
v16@?0r^v8
No wrapped key to parse
tlkUUID
Peer is not an applicant
AA Compromise
invi
u_Tomb
^v40@?0^{__CFData=}8^{__CFData=}16^{?=qq}24^^{__CFError}32
2006
Description encode failed
SyncSet
Unknown Status
DeveloperID Date parsing: extension value wrong tag
TKClientToken
1.2.840.113635.100.1.90
issuerHash
>KeyParameters
SecKeyCopyKeyExchangeResult
ucrt
Failed to create utc date
key type
com.apple.runtime-issues
action unknown: %@
com.apple.
SFAnalyticsSampler
InternalError
fdopen
Description alloc failed
failed to encode SubjectAltName
Failed to copy XPC policy
algid:sign:RSA:digest-PKCS1v15:SHA384
realloc buf failed
IdLinkage
CodeRequirements-3
PKCS #9 Unstructured Address
cpo
subjectAltName value is not a string
ggrp
Unable to export key parameters
kOddCompactDataMessage (0x21)
SOSBackupSliceKeyBag
SOSCCView
SOSCCMessageFromPeerIsPending
%u.%u.%u.%u
0103
fqdn was NULL, and no associated domains found
result
operation
Missing handle for open cache db
Go away
Certificate Authority Revocation URL
passphrase
failed to get directory info
entitlements-dict
validated
excludeCount
Diffie-Helman Public Key
Permitted Subtree Minimum
1.2.840.113635.100.1.92
MATCH OPCODE %d NOT UNDERSTOOD
\"
Unknown view(%@) (ViewResultCode=%d)
Certificate Authority
ProvoloneProcessedSigningQA
NSString *getkSecurityRTCEventNameOctagonTrustLost(void)
PKCS #12 V1 Key Bag
salt
kSecECCurveSecp384r1
lseek
{
R
com.apple.trustdFileHelper
QCSTypeWeb
1.2.840.113635.100.1.69
data for key %s is NULL
lwcr-library
false_start_used
NSNull
NSURLError
WatchMigration
dk
com.apple.private.skip-library-validation
v32@?0@\"NSString\"8Q16^B24
user signature of public key hash fails to verify
unexpected end of event file %zu of %zu bytes read
The dictionary parameter 'EndWith' is either null or not a string
trailing garbage at end of datetime
base version
Analytics/%@.db
com.apple.security.sosoctagonbitschanged
Organization
MacDistributionInstaller
signing-time
NotInCircle
p12Decode
1201
select %@, %@ from %@
SSLDisableRecordSplitting
NSPinnedDomains
OrderBundleSigner
canSendMetrics
CKDKVS-synchronizeWithCompletionHandler
Retirement date is after current date
Reasons
failed to make EKU extension
algid:sign:RSA:message-PKCS1v15:SHA224
com.apple.security.otr.error
ipsecServer
recryptParams
DCAttestation
ZuluCalendar
continuing
CodeDirectory
select value from Properties where key = ?
kEvenCompactDatamessage (0x30)
failed to create xpc_object from policy options
format
Key size is not permitted for this use
/usr/local/
sos_analytics.db-wal
sealedhashesbound
u_AuthUIS
TemporalValidity
Non-CA certificate used as a CA
Certificate has extensions but is not version 3
idMSTrustTimestamp
B
OCSP Nonce Extension
147258
LeafMarkerOidWithoutValueCheck
Failed to create set
Failed to encode root certificates SEQUENCE
okd
NSUnbufferedIO
NSArray
clique-removefriends
RequestPending
```
