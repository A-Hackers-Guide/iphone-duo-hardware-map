# `/usr/lib/libAppleSSE.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 206,240 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 3224)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/usr/lib/libAppleSSE.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (1 classes, 2 protocols)

Classes: `BAADelegateImpl`

Protocols: `BAASupportDelegate`, `NSObject`

## Strings (264)

```
CFDataGetLength(unsignedAPDU) <= sizeof(inData->varData)
mac
expirationDate
certificates
copied == dataSize
%s() -> %d
[cert length] <= (end - pos)
outData->data.confBlobSignatureSize <= (end - pos)
outData->data.assetACLRequestSize <= (end - pos)
nonce
service
pos <= end
err == 0 
outDataSize >= sizeof(outData->data)
(end - pos) >= dataSize
assetACLAttestation
operationMetadata
v8@?0
\tnoPasscodeCnt = %u\n
SSEGetActivationTimeout
retAssetACLRequest
retOperationApproval
sharingResult
 \t
SecureElement
hasSSE()
CFDataGetLength(acmContext) <= sizeof(inData->data.acmContext)
CFDataGetLength(hostChallenge) == sizeof(inData->data.hostChallenge)
CFDataGetLength(cardCryptogram) == sizeof(inData.data.cardCryptogram)
MGGetBoolAnswer
\tkeybag hash   = %016llx\n
unsignedAPDU
retAuthRandom
SSEEnableOffWristAuthorization
outData->data.attV2AuthKeySize == outDataSize - sizeof(outData->data)
/System/Library/Frameworks/Security.framework/Security
CFDataGetLength(acmContext) <= sizeof(inData.data.acmContext)
operationApprovalAttestation
outData->data.resultSignatureSize <= (end - pos)
\tauthRand hash = %016llx\n
CFDataGetLength(rSCl) <= 4294967295U
activationTimeout
manifest
dataSize <= sizeof(payloadHeader.seid)
userID
authRandom
size == sizeof(outData.data) + outData.data.signedDeviceDataSize
state
\tentropy hash  = %016llx\n
getSigKeyExpDate
size == sizeof(outData)
CFDataGetLength(seid) <= sizeof(inData.data.seid)
CFDataGetLength(cardChallenge) == sizeof(inData.data.cardChallenge)
\tsubcounter    = %llu\n
keyData
CFDataGetLength(cardCryptogram) == sizeof(inData->data.cardCryptogram)
isEnabled
rd=md0
%F %T (%z)
hostCryptogram
[keyData length] <= (end - pos)
signedAPDU
SSEUseEntangledAuthorizationRandom
_baaSupportClass
validationMechanism
sizeof(uint32_t) <= (end - pos)
SSEEffaceAuthorizationRandom
SSEIsOffWristAuthorizationEnabled
SSEGetSignedDeviceData
encryptedPIN
pubKey
outData.deviceVersion > 0
cardChallenge
SSEAuthorizeAndSignAPDU
IOGeneralInterest
AppleSSE Log Starts - System Version %s
BAASupport
seid
requestMetadata
assetACL
signedPairingInfo
CFDataGetLength(manifest) <= 4294967295U
getSigKeyCertificates
retMac
CFDataGetLength(nonce) <= sizeof(inData.data.nonce)
outData->data.resultSize <= (end - pos)
/usr/lib/libAppleSSEExt.dylib
authorize
outData->data.confBlobSize <= (end - pos)
sharingRequestSignature
sharingResultSignature
/var/mobile/Library/Logs/AppleSSE.log
pos
acmContext
retSignedAPDU
outData->data.assetACLRequestAttestationSize <= (end - pos)
retAttV2AuthKey
sePk
kern.bootargs
a
getBlessedUser
outDataSize <= sizeof(*outData)
*mac
dataSize <= sizeof(inData->data.seid)
sharingRequest
retSharingResult
\n
retConfirmationBlobSignature
size == sizeof(outData->data) + outData->data.keyDataSize + outData->data.attestationSize + outData->data.pubKeySize
assetACLRequestAttestation
operationApprovalVersion >= 1 && operationApprovalVersion <= 3
_notifyport
authorizeWithPIN
CFDataGetLength(rMCl) <= 4294967295U
retSignedPairingInfo
retKeyData
retAttestation
outData->data.macSize <= (end - pos)
acl
operation
operationApproval
%02x
SecTaskCreateFromSelf
retEncryptedPIN
[cert isKindOfClass:[NSData class]]
SSEAuthorizeAndSignECommerceBlob
SSEGetHostChallenge
CFDataGetLength(hostChallenge) == sizeof(inData.data.hostChallenge)
retAssetACLRequestAttestation
retSharingResultSignature
setSigKey
outData->data.authRandomSize <= (end - pos)
size >= sizeof(outData->data) + outData->data.confBlobSize + outData->data.confBlobSignatureSize
outData->data.signedPairingInfoSize == outDataSize - sizeof(outData->data)
size >= sizeof(outData->data)
confirmSigKey
cardCryptogram
outDataSize == sizeof(outData->data) + outData->data.signedAPDUSize
SSEGetAuthorizationRandom
keybagUUID
\tuserID        = %u\n
inData
acmContext || (authorizationType == kAuthorizationTypeUnlockedSinceBoot)
size >= sizeof(outData.data)
/usr/lib/libMobileGestalt.dylib
%s [%s]: 
\tsseKey hash   = %016llx\n
SecTaskCopyValueForEntitlement
com.apple.private.applesse.baa
CFDataGetLength(seid) <= sizeof(inData->data.seid)
CFDataGetLength(cardChallenge) == sizeof(inData->data.cardChallenge)
signedDeviceData
outData->data.operationApprovalSize <= (end - pos)
CFDataGetLength(sePk) <= 4294967295U
com.apple.private.applesse.allow
retHostCryptogram
confirmationBlob
outData->data.operationApprovalAttestationSize <= (end - pos)
retOperationApprovalAttestation
confirmationBlobSignature
retSignedDeviceData
InternalBuild
nfcd
generateSigKey
*hostChallenge
assetACLRequest
dataSize <= sizeof(inData->data.acmContext)
attV2AuthKey
payload.length <= 4294967295U
AppleSSE
retConfirmationBlob
hostChallenge
outData
SSEGetEntangledAuthorizationRandom
SSESetBlessedUser
SSESetEffacementNotificationHandler
\tseid          = 
certSize <= (end - pos)
CFDataGetLength(rcrt) <= 4294967295U
/Library/Caches/com.apple.xbs/FF83E7CC-A422-4417-A8D5-3AD7BBA47DD6/TemporaryDirectory.b4kgjH/Sources/AppleSSE/AppleSSElib/AppleSSElib.m
0
outData->data.signedAPDUSize <= (end - pos)
rcrt
handle
end
attestation
retPubKey
BAASupportDelegate
NSObject
BAADelegateImpl
confirmSigKey:status:
conformsToProtocol:
isEqualToString:
processName
setSigKey:expirationDate:keyData:certificates:
superclass
TQ,R
addObject:
getCertificates:
getSigKeyExpDate:expirationDate:
isInternal
length
prepareLazily
self
countByEnumeratingWithState:objects:count:
isKindOfClass:
setBlessedUser:keybagUUID:
setDelegate:
T@\"NSString\",?,R,C
T@\"NSString\",R,C
dataWithBytes:length:
getBytes:length:
getCertificateExpirationDate:
appendData:
array
class
debugDescription
getSigKeyCertificates:certificates:
processInfo
prepare
autorelease
boolValue
bytes
count
hash
performSelector:
respondsToSelector:
release
generateSigKey:keyData:attestation:pubKey:
isMemberOfClass:
performSelector:withObject:withObject:
retain
retainCount
zone
isProxy
T#,R
description
getBlessedUser:keybagUUID:
isEqual:
issueNewCertificate
performSelector:withObject:
i24@0:8I16i20
B24@0:8@16
@24@0:8:16
@32@0:8:16@24
@40@0:8:16@24@32
B16@0:8
i32@0:8^I16[16C]24
#16@0:8
Q16@0:8
@\"NSString\"16@0:8
i44@0:8I16^@20^@28^@36
i44@0:8I16Q20@28@36
i28@0:8I16^@20
@16@0:8
B24@0:8#16
Vv16@0:8
B24@0:8@\"Protocol\"16
i28@0:8I16^Q20
B24@0:8:16
^{_NSZone=}16@0:8
i44@0:8I16Q20@\"NSData\"28@\"NSArray\"36
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n
isEntitledForBAA(): entitled = %u
```
