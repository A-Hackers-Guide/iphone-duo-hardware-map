# `/usr/lib/libAppleSSE.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 206,240 bytes.

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
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n
isEntitledForBAA(): entitled = %u
assetACLRequest
com.apple.private.applesse.allow
com.apple.private.applesse.baa
end
size == sizeof(outData->data) + outData->data.keyDataSize + outData->data.attestationSize + outData->data.pubKeySize
[keyData length] <= (end - pos)
*hostChallenge
acmContext || (authorizationType == kAuthorizationTypeUnlockedSinceBoot)
keybagUUID
expirationDate
signedPairingInfo
sePk
setSigKey
size == sizeof(outData)
hostChallenge
outData->data.confBlobSize <= (end - pos)
outData->data.assetACLRequestAttestationSize <= (end - pos)
dataSize <= sizeof(payloadHeader.seid)
v8@?0
AppleSSE Log Starts - System Version %s
authorize
CFDataGetLength(hostChallenge) == sizeof(inData.data.hostChallenge)
operationApprovalAttestation
IOGeneralInterest
a
%F %T (%z)
authorizeWithPIN
pos <= end
retSignedAPDU
acl
outData->data.attV2AuthKeySize == outDataSize - sizeof(outData->data)
outDataSize == sizeof(outData->data) + outData->data.signedAPDUSize
outData->data.confBlobSignatureSize <= (end - pos)
SSEEffaceAuthorizationRandom
(end - pos) >= dataSize
operationApproval
\tsseKey hash   = %016llx\n
getBlessedUser
unsignedAPDU
CFDataGetLength(cardCryptogram) == sizeof(inData->data.cardCryptogram)
confirmationBlob
SSEGetSignedDeviceData
manifest
/usr/lib/libAppleSSEExt.dylib
/System/Library/Frameworks/Security.framework/Security
err == 0 
acmContext
requestMetadata
operationMetadata
rd=md0
\n
hostCryptogram
retAttestation
outData
outDataSize <= sizeof(*outData)
isEnabled
retAttV2AuthKey
sharingRequestSignature
kern.bootargs
\tsubcounter    = %llu\n
attestation
activationTimeout
retAuthRandom
retMac
sharingRequest
outData->data.authRandomSize <= (end - pos)
CFDataGetLength(nonce) <= sizeof(inData.data.nonce)
state
BAASupport
CFDataGetLength(rMCl) <= 4294967295U
/Library/Caches/com.apple.xbs/FF83E7CC-A422-4417-A8D5-3AD7BBA47DD6/TemporaryDirectory.b4kgjH/Sources/AppleSSE/AppleSSElib/AppleSSElib.m
CFDataGetLength(acmContext) <= sizeof(inData.data.acmContext)
outData->data.signedPairingInfoSize == outDataSize - sizeof(outData->data)
signedAPDU
SSESetEffacementNotificationHandler
retAssetACLRequestAttestation
pubKey
generateSigKey
userID
CFDataGetLength(cardChallenge) == sizeof(inData->data.cardChallenge)
outData->data.signedAPDUSize <= (end - pos)
nonce
retHostCryptogram
operationApprovalVersion >= 1 && operationApprovalVersion <= 3
\tnoPasscodeCnt = %u\n
CFDataGetLength(rSCl) <= 4294967295U
retSignedPairingInfo
getSigKeyCertificates
outData.deviceVersion > 0
SSEAuthorizeAndSignAPDU
SSEGetEntangledAuthorizationRandom
payload.length <= 4294967295U
 \t
/usr/lib/libMobileGestalt.dylib
size >= sizeof(outData->data) + outData->data.confBlobSize + outData->data.confBlobSignatureSize
retConfirmationBlob
CFDataGetLength(unsignedAPDU) <= sizeof(inData->varData)
signedDeviceData
CFDataGetLength(sePk) <= 4294967295U
retSharingResultSignature
sizeof(uint32_t) <= (end - pos)
size >= sizeof(outData->data)
SSEGetAuthorizationRandom
retSignedDeviceData
encryptedPIN
getSigKeyExpDate
CFDataGetLength(cardCryptogram) == sizeof(inData.data.cardCryptogram)
SSEUseEntangledAuthorizationRandom
certificates
outData->data.operationApprovalSize <= (end - pos)
_notifyport
seid
inData
SSEGetActivationTimeout
\tuserID        = %u\n
%02x
_baaSupportClass
validationMechanism
keyData
0
dataSize <= sizeof(inData->data.seid)
attV2AuthKey
MGGetBoolAnswer
retConfirmationBlobSignature
pos
CFDataGetLength(rcrt) <= 4294967295U
CFDataGetLength(acmContext) <= sizeof(inData->data.acmContext)
outDataSize >= sizeof(outData->data)
mac
outData->data.operationApprovalAttestationSize <= (end - pos)
retOperationApprovalAttestation
sharingResultSignature
outData->data.resultSignatureSize <= (end - pos)
SecTaskCopyValueForEntitlement
SSEAuthorizeAndSignECommerceBlob
outData->data.macSize <= (end - pos)
copied == dataSize
rcrt
/var/mobile/Library/Logs/AppleSSE.log
\tkeybag hash   = %016llx\n
%s() -> %d
certSize <= (end - pos)
hasSSE()
SSEGetHostChallenge
dataSize <= sizeof(inData->data.acmContext)
retPubKey
CFDataGetLength(hostChallenge) == sizeof(inData->data.hostChallenge)
confirmationBlobSignature
CFDataGetLength(seid) <= sizeof(inData.data.seid)
SSEEnableOffWristAuthorization
size == sizeof(outData.data) + outData.data.signedDeviceDataSize
outData->data.assetACLRequestSize <= (end - pos)
service
\tauthRand hash = %016llx\n
CFDataGetLength(seid) <= sizeof(inData->data.seid)
handle
nfcd
SecTaskCreateFromSelf
cardChallenge
operation
SecureElement
%s [%s]: 
\tseid          = 
\tentropy hash  = %016llx\n
CFDataGetLength(cardChallenge) == sizeof(inData.data.cardChallenge)
assetACL
outData->data.resultSize <= (end - pos)
retKeyData
authRandom
retSharingResult
AppleSSE
InternalBuild
retEncryptedPIN
confirmSigKey
retAssetACLRequest
retOperationApproval
sharingResult
CFDataGetLength(manifest) <= 4294967295U
*mac
SSEIsOffWristAuthorizationEnabled
size >= sizeof(outData.data)
assetACLRequestAttestation
assetACLAttestation
[cert isKindOfClass:[NSData class]]
[cert length] <= (end - pos)
cardCryptogram
SSESetBlessedUser
BAADelegateImpl
BAASupportDelegate
NSObject
self
setBlessedUser:keybagUUID:
setSigKey:expirationDate:keyData:certificates:
getSigKeyExpDate:expirationDate:
prepareLazily
retainCount
bytes
generateSigKey:keyData:attestation:pubKey:
isEqualToString:
T@\"NSString\",?,R,C
TQ,R
array
class
isMemberOfClass:
setDelegate:
zone
T@\"NSString\",R,C
boolValue
count
getBlessedUser:keybagUUID:
isKindOfClass:
performSelector:
performSelector:withObject:withObject:
superclass
confirmSigKey:status:
dataWithBytes:length:
debugDescription
getCertificates:
issueNewCertificate
length
performSelector:withObject:
retain
addObject:
countByEnumeratingWithState:objects:count:
description
getSigKeyCertificates:certificates:
isInternal
processInfo
processName
respondsToSelector:
release
T#,R
appendData:
autorelease
conformsToProtocol:
isEqual:
getCertificateExpirationDate:
isProxy
prepare
getBytes:length:
hash
i32@0:8^I16[16C]24
Q16@0:8
B16@0:8
i44@0:8I16^@20^@28^@36
i44@0:8I16Q20@28@36
B24@0:8@16
#16@0:8
Vv16@0:8
^{_NSZone=}16@0:8
B24@0:8@\"Protocol\"16
i28@0:8I16^Q20
i28@0:8I16^@20
@24@0:8:16
@32@0:8:16@24
B24@0:8:16
@\"NSString\"16@0:8
i44@0:8I16Q20@\"NSData\"28@\"NSArray\"36
@16@0:8
@40@0:8:16@24@32
B24@0:8#16
i24@0:8I16i20
```
