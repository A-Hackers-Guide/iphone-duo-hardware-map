# `/System/Library/PrivateFrameworks/AppleRestoreUtils.framework/XPCServices/ARUService.xpc/ARUService`

From the upgrade restore ramdisk (141-29011-104.dmg). 949,360 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 32 (Size: 4288)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (15)

- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication (compatibility version 1.0.0, current version 64578.104.1, weak)`
- `/usr/lib/libauthinstall.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libVinylNonUpdater.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork (compatibility version 1.0.0, current version 3896.200.61)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>com.apple.AppleNVMeEAN.allow</key>
	<true/>
	<key>com.apple.cyrus.allow</key>
	<true/>
	<key>com.apple.driver.AirshipDaleBasebandControlInterface.user-access</key>
	<true/>
	<key>com.apple.driver.AppleAuthCP.i2c.user-access</key>
	<true/>
	<key>com.apple.driver.AppleAuthCP.user-access</key>
	<true/>
	<key>com.apple.driver.AppleBasebandPCI.user-access</key>
	<true/>
	<key>com.apple.driver.AppleConvergedIPCICEBB.user-access</key>
	<true/>
	<key>com.apple.driver.I2C.device.user-access</key>
	<true/>
	<key>com.apple.keystore.class.wku</key>
	<true/>
	<key>com.apple.keystore.fdr-access</key>
	<true/>
	<key>com.apple.keystore.sik.access</key>
	<true/>
	<key>com.apple.nfcd.hwmanager</key>
	<true/>
	<key>com.apple.private.AppleKMPEndpoint.user-access</key>
	<true/>
	<key>com.apple.private.AppleRepairSEPDriver.allow</key>
	<true/>
	<key>com.apple.private.AppleSSMAEndpoint.user-access</key>
	<true/>
	<key>com.apple.private.AppleSSMAService.user-access</key>
	<true/>
	<key>com.apple.private.IOAESAccelerator.fdr-key-handle</key>
	<true/>
	<key>com.apple.private.IOPortTransportAIDBusUserClient.access</key>
	<true/>
	<key>com.apple.private.PurpleReverseProxy.allowed</key>
	<true/>
	<key>com.apple.private.ZhuGeSupport.CopyValue</key>
	<true/>
	<key>com.apple.private.applepearl.allow</key>
	<true/>
	<key>com.apple.private.applesepmanager.allow</key>
	<true/>
	<key>com.apple.private.factorysupportd.reverseproxy</key>
	<true/>
	<key>com.apple.private.security.bootpolicy</key>
	<true/>
	<key>com.apple.rootless.volume.iSCHardware</key>
	<true/>
	<key>com.apple.security.iokit-user-client-class</key>
	<array>
		<string>AppleNVMeUpdateUC</string>
		<string>AppleAPFSUserClient</string>
		<string>AppleHPMUserClient</string>
		<string>AppleSEPUserClient</string>
		<string>AppleARMIICUserClient</string>
		<string>AppleNVMeEANUC</string>
		<string>IOAESAcceleratorUserClient</string>
		<string>AppleOysterUserClient</string>
		<string>AppleCyrusUserClient</string>
		<string>AppleKMPEndpointUserClient</string>
		<string>AppleSSMAEndpointUserClient</string>
		<string>AppleSSMAServicesUserClient</string>
		<string>IOPortTransportAIDBusUserClient</string>
		<string>AppleAuthCPUserClient</string>
		<string>ApplePearlUserClient</string>
		<string>AppleBasebandPCIUserClient</string>
		<string>AppleBasebandUserClient</string>
		<string>IOAppleConvergedIPCBBUserClient</string>
		<string>AppleStockholmControlUserClient</string>
	</array>
	<key>com.apple.security.network.client</key>
	<true/>
	<key>com.apple.stockholm.kext.entitlement</key>
	<true/>
</dict>
</plist>
```

## Objective-C (9 classes, 4 protocols)

Classes: `ARUProvController`, `ARUProvSequencer`, `ARUService`, `ARUTreeckoManager`, `Ace2ARUProvController`, `Ace2ARUTreeckoManager`, `Ace2HPMInterface`, `NSString`, `ServiceDelegate`

Protocols: `ARUListenerProtocol`, `ARUServiceProtocol`, `NSObject`, `NSXPCListenerDelegate`

## Strings (4,166)

First 2,500 of 4,166.
```
ARUProvSequencer
ARUServiceProtocol
ARUListenerProtocol
NSXPCListenerDelegate
Ace2ARUTreeckoManager
MGExtra
ARUService
NSObject
ServiceDelegate
ARUProvController
Ace2HPMInterface
ARUTreeckoManager
Ace2ARUProvController
v20@0:8I16
i36@0:8i16@20r^^{__CFDictionary}28
B24@0:8:16
Vv16@0:8
v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16
^{__CFData=}16@0:8
Q20@0:8I16
i32@0:8@16@24
B24@0:8@\"Protocol\"16
v24@0:8@?<v@?@\"NSData\"@\"NSError\">16
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32
v24@0:8@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">16
i24@0:8^{__CFString=}16
@24@0:8I16I20
Q36@0:8I16I20I24I28I32
Q28@0:8I16I20I24
{?=*Q}16@0:8
@24@0:8@16
v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\">24
I
i40@0:8^{__CFData=}16^{__CFData=}24Q32
i28@0:8@16i24
v24@0:8^{__CFBoolean=}16
I16@0:8
v24@0:8@?16
B24@0:8@16
@40@0:8:16@24@32
B32@0:8@16@24
B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24
i24@0:8^{__CFDictionary=}16
v40@0:8@16@24@?32
@24@0:8:16
B16@0:8
@16@0:8
B32@0:8^{__CFData=}16Q24
^{__CFString=}16@0:8
^{__CFData=}
Q48@0:8C16^v20Q28I36^Q40
v24@0:8@16
{?=\"data\"*\"length\"Q}
@32@0:8:16@24
i48@0:8^{__CFData=}16^{__CFData=}24^{__CFData=}32Q40
i48@0:8^{__CFString=}16^{__CFString=}24^{__CFDictionary=}32Q40
@\"NSString\"16@0:8
v32@0:8@16@?24
v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24
v24@0:8^{__CFData=}16
Q40@0:8C16^v20Q28I36
v48@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32@?<v@?@\"NSError\">40
^{__CFString=}
v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\">32
B24@0:8#16
^{_NSZone=}16@0:8
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24
^{__CFBoolean=}
@\"NSArray\"
v20@0:8i16
Q24@0:8^@16
v24@0:8@?<v@?@\"NSDictionary\">16
v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24
v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">24
v16@0:8
i24@0:8@16
^{__CFBoolean=}16@0:8
Q16@0:8
v32@0:8{?=*Q}16
i
v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24
i16@0:8
B48@0:8^{__CFData=}16Q24r^^{__CFData}32^Q40
#16@0:8
v48@0:8@16@24@32@?40
v24@0:8^{__CFString=}16
@\"NSXPCConnection\"
checkSavageProvisioning -> %d\n
prewarmCamera -> %d\n
objectSize:\t\t%d\n
setDummyWrappedFDRDataEncryptionKey\n
objectFound:\t\t%s\n
unmappedFromANE:\t%s\n
getAttestationToBrunorCollectionKey\n
encryptFDRDataForBrunor -> %d\n
getPDAK\n
getDummy0PSDData -> %d\n
generateAndVerifyAriesHostAuthorization\n
dvaOffset:\t\t0x%X\n
Reference frame (set=%d, frame=%d, size=%d, type=%d, temp=%f) written to %s\n
getPearlSelfTestResult -> %d\n
allocateAndMapObjectS3C1 -> 0x%x\n
getBrunorPermanentKey\n
getPDAK -> %d\n
getAttestationToPDAK -> %d\n
encryptFDRData %p %zu %p %p\n
Generating reference frames files...\n
pearlSeaCookieHandleMessage %d %p %zu %p %p\n
mapScheme3Object: fourcc:%.4s\n\n
signDataWithBrunorPermanentKey -> %d\n
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n
Reference set dictionary written to %s\n
getAttestationToBrunorCollectionKey -> %d\n
ispMapFunction:\t\t%s\n
ispUnmapFunction:\t%s\n
generateAndVerifyAriesHostAuthorization -> %d\n
mappedToANE:\t\t%s\n
Couldn't create OS Log for 'com.apple.BiometricKit.Library-PearlFactory'!\n
aneUnmapFunction:\t%s\n
Verifying new reference frames info record...\n
%s: Loading PSPC from FDR.\n
getPearlSelfTestResult\n
checkSecureStreamingAndVerifySignatures (%u)\n
checkSecureStreamingAndVerifySignatures -> %d\n
ReferenceFramesPath: %s\n
ReferenceFramesSetInfo, index: %zu, type: %d, count: %d, size: %d\n
%s: PSPC data loaded to SEP.\n
simulateSelfTestFailure\n
setEntitlementOverrideConfig (0x%x)\n
signDataWithBrunorCollectionKey -> %d\n
encryptFDRDataInternal %p %zu %p %p %d\n
Removed %@\n
Generating reference frames info record...\n
Results of Allocation and Mapping Object Scheme3 Context1:\n
mappedToISP:\t\t%s\n
unmappedFromISP:\t%s\n
encryptFDRData -> %d\n
checkSecureStreaming\n
pearlSeaCookieHandleMessage, type=%d -> 0x%x\n
getAttestationToPDAK\n
verifyFDRData -> %d\n
setEntitlementOverrideConfig -> %d\n
getBrunorCollectionKey\n
setDummyWrappedFDRDataEncryptionKey -> %d\n
aneMapFunction:\t\t%s\n
encryptFDRDataForBrunor %p %zu %p %p %p %zu\n
ReferenceFramesSetInfo, index: %d, type: %d, count: %d, size: %d\n
simulateSelfTestFailure -> %d\n
prewarmCamera (%u)\n
pearlSeaCookieHandleMessage, type=%d reply[%zu] %.*P\n
mappedToSEP:\t\t%s\n
unmappedFromSEP:\t%s\n
signDataWithBrunorCollectionKey\n
getDummy0PSDData\n
checkSavageProvisioning\n
mapScheme3Object -> 0x%x\n
getBrunorCollectionKey -> %d\n
getBrunorPermanentKey -> %d\n
signDataWithBrunorPermanentKey\n
ReferenceFramesInfo setCount: %d\n
Reference frames info record written to %s\n
%s: PSPC data found.\n
%s: Successfully got provisioning data.\n
checkSecureStreaming -> %d\n
allocateAndMapObjectS3C1: fourcc:%.4s mapObj:%d unmapObj:%d\n\n
prepareFDRDataEncryptionKey\n
prepareFDRDataEncryptionKey -> %d\n
libCyrusFDR unit_is_j126 = %{public}d
verifyFDRData %p %zu\n
encryptFDRDataInternal -> %d\n
createExistingCertificateFromServer
%s: kFDRTag_asid property length != fdrDecode->assemblyID.length
Buttons1,ECID
origDataPtr is NULL
libCyrusFDR_is_multilynx_present: %d, answer: %d, count: %d\n
%s: Evaluation returned code=0x%016llX, re-evaluate with FDR 1.0 format
tempAuthlistables has wrong type %@
testdummy
@Timer10,Ticket
amfdrRemote is NULL
Unable to extract trust object digest from AP Ticket
can't read Mogul memory zone
sysconfig returns all err 100, skip uploading process
CLASS B
Free Blocks:%lld blocks of size:%d\n
No crash thread in report\n
AMFDRDecodeImage4Certificate
dataInfo->setCount > 0
%s: offline signing public key mismatch
marker path is NULL
_AMFDRSupportBase64Encode
failed to parse mfiProductPlanUID
failed to encode MFiAccessoryData (error %d)
can't get the lock status for zone %d
===== local cert not equal to the cert inside mogul chip =====
mogulChipIdEcidData is NULL
@PCON2,Ticket
FDR is not supported
sikDataArrayToPut is NULL
i
preFusingOutput is NULL.
/Library/AggregateDictionary
%s: PKI: im4c cert signature validation with issuer pubkey failed
AMFDRCertificateSigningRequest returned no fusing data
Failed to get pointer of data
Yonkers - Factory
%s invalid argument. sysconfig and etnry cannot be NULL
000t
000E
B64_BOARDID
failed to generate MFi CSR format
kAppleNVMeIsEANFormatted failed, kernResult = 0x%x
fail to lock memory zone %d, retVal: %x
-[Ace2ARUProvController verifyAllKeys:]
isProdPart is NULL
cert data length not match
SIGEMT
%s: kFDRTag_inst propertyLength (%d) != instLength (%zu)
0012
Download and compare successfully - \n%@\n%@
lcrt doesn't exist in FDR data store, start collecting
_ARUReadApTicketFromEAN
B64_CHIPID
iPad Display
No valid OID specified, skip checking
dense
%s: Failed to get payload sequence and set manifest from multi combined data
@YonkersIR4,Ticket
failed to add value %@
Force migrate sik data class: %@
PED,Ticket
urlSkeyReqEncodeData is Null
failed to decode lynx blob sequence item %d
value is not in CFNumberRef
_ARUCheckAPTickets
collectionKey
AMFDRDecodeCheckCertRevocation
fusing output: %@
_formatChipId
fdrContext->mountpoint is required
UploadWcrtOptions
DataClassesToWrap
%s: unsupported public key length: %lu
provisionInfoDict is NULL
syscfgPropertyTags is not array
AMFDRDataDictCopy got error
Content-Type
ARU0CfgHandleTypeVerifySealing
%s Failed to validate HMAC.
ARUTristatReadProvisioningStatus failed
fail to allocate space for outCtx
can't get idsn data
GetErrorCodeI2C
0x%016llx - 0x%016llx %s %s <%s> %s\n
AMFDRDecodeIterateCertChainNext failed for inter cert 0x%016llX
failed to lock Area51 Manufacturer NVM
reference-%@__T_%@.bin
x-fdr-key-attestation
Failed to read frame from addr(0x%016llx): %d(%s)
HardwareMountpoint
IOService:/IOResources/AppleCyrus
%s: FDR failed to get payload type
%s: Records must be SET Container
CameraAP1,ECID
ARUFDRCopyMergedFDRv3LocalDataWithDict
sysctl.proc_cputype
property has wrong type %@
iAP2ControlSession cmd cannot be NULL
ApplePearlExclaveSEPDriver
%s: propertyValue != kFDRTagStr_sreq
CFUUIDCreateString failed for %@
failed to base64 encode attestation
pSavage is NULL after successful open
failed to allocate *mogulServiceIter
outKCVLength && (*outKCVLength >= 3)
%s: propertyValue != fdrDecode->sealingManifestImg4.payload.hash
@Acdcuc1,Ticket
Acdcuc1,ECID
failed to allocate dictKeysBuffer
outLeafCertDigest is NULL
Failed to create chipId string
EnableSsl
libCyrusFDR: entered libCyrusFDR_get_public_key%s
failed to compute digest: %d
failed to create combinedDataClasses
libCyrusFDR: ERROR: [%s:%u:%s] invalid lynx num %d%s
_Bool sysConfig3ManifestGetMetadataHMAC(struct __SysConfig3ManifestEntry *__single, SysConfigData *__single)
unable to read apticket
/Library/SoftwareUpdate
/Library/ConfigurationProfiles
AMFDRCertificateSigningRequest failed, error: %@
/root/Library
AudioAP1,ECID
ExecAIDCmdI2C
aks_attest_context_get_header_version
IODeviceTree:/filesystems
%s This SysConfig version (0x%X) does not support HMAC.
Failed to create connection options dictionary\n
pipe failed while preparing to execute %s: %s
could not open file: %s (%s)\n
%s: End of Outer Sequence found, before any valid DER.
_formatUdid
Incorrect key read, expecting 0x%04X, get 0x%02X%02X
/Library/Accounts
%s: Record value must be OCTET_STRING
Disabling SSL validation
CFStringGetCString failed
/Library/mad/activation_records
%s: can't parse sealing manifest tag. Expected tag %d, found %llu
Failed to create fusingInput dictionary
invalid hash from libCyrusFDR_get_imm_hash_for_sandcat
libCyrusFDR: libCyrusFDR_is_multilynx_present(%d): device is not not multilinx?%s
%s Failed to allocate sysconfig.
send request result = %d\n
%s: Invalid out pointers
@YonkersVisible1,Ticket
Baobab2,ECID
Start Auth Read Failed
akstest_new_key
%s: kFDRTag_cptp property != fdrDecode->componentType
%s %d is not a CFData
iPad MLB
createSignatureFromMogul
%s: invalid digest length
Select Fifo Failed
failed to parse key %d
_cliReadData
0018
ARUMogulReadCertFromMemoryZoneImpl
ExtraCertOptions
/Media
/Library/terminus
chipIDUIDStr is NULL
outAccessoryData is NULL
Can't read register successfully
Failed to get proc path: %d(%s)
replySize <= sizeof(reply)
ARUArea51RequestProvisionAppleComponentCertificate
failed to allocate certChainEncoder
%s: can't parse FDR Multi-response payload
%s: Record value length is 0
allowCertificateValidationFailed = %@
%s: No manifest found - not evaluated.
@Acdcuc6,Ticket
Error Mtp Retries Exceeded
%s: subCCName cannot be NULL when kAMFDRDecodeOptionSubCCOnly is set.
Verify EsmLock Status Read Failed
cert #%d is too long (%ld)
AllowIncompleteData
Skipped ServerOnlySigning data class: %@
xpc sendFdrStatistics error code is %d
multilynx got sn (%d):
Error setting esn string.
_wireless
AMFDRDecodeIterateProducerIDBegin
Failed to get data protection class for given path %s with errno %s (%d)\n
missing fsca in previous apticket, skipping sysconfig upload.
%s: Img4DecodeGetPropertyData(kFDRTag_inst) failed.
Final - release failed %d 
failed to create public key data
Mountpoint
wheel
000k
getDummy0PSDData failed, error code = %d
chipIDECIDCtx check failed
_Bool sysConfig3CreateFullHMAC(struct __SysConfig3 *__single, SysConfigData *__single)
Cryptex1,UDID
PRODUCT type is nil
CTParseKey failed
%s: cannot find tag in property list
mismatched ticketApFusesDigest, fatal error!
EXC_RESOURCE
AMFDRDecodeEvaluateTrustCombinedWithSik
iterate_matching
eUICC
dataClasses is NULL
Skip adding %s to eCfg since it is not overridable for engineer
could get manifest property CPID
leafRawCertItem is NULL
failed to read the certificate chain to Area51
%s: failed to decode sealing manifest tag
iPad
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n
No existing metadata
https://skl.apple.com
sealMetaDataDic failed to create
mfiProperty is too long
PrivateKey
crash_signal_handler
%s: malformed FDR Multi-Response actionCode Format
preFusingOutput is NULL
ARUPEDRequestSendSync
processData
PRODUCT
_constructRequestPacket
ForHttps
Lock Customer SMASN Zone succeeded
arm_thread_backtrace_from_fp
param length overflow: %u, remaining length
failed to parse oid: %s
leafCertOrig is NULL
%y%m%d%H%M%SZ
*
x-fdr-certification-type
%s: Unsupported tag found in manifest '%c%c%c%c'
provisioning URL is NULL or none-String type: %@
Devices - Stations
encryptedDataBuffer
%s: Skip verifying assembly identifier
%s: FDR Sealing Manifest is missing
%s: Img4DecodeGetPropertyData(kFDRTag_SrvT) failed.
PCON1,ECID
First AuthCtrl Read Failed
Stations
failed to get der params: 0x%08x
addLegacyDataClassForExport for lcrt failed
%s: can't parse content of MinimalManifestMetaData
\nseputil --pair LYNX output:
BT_MAC2
prf1Class && (prf1ClassSize > 0)
%s: invalid metadata tag: 0x%llx
_Bool sysConfig3PayloadEntryGetData(struct __SysConfig3PayloadEntry *__single, SysConfigData *__single)
lakeville
AMFDRCertificateSigningRequest failed: %@
ispUnmapFunction:\t%s\n
%s: kFDRTag_asid doesn't exist, but this is allowed
created iCheck marker for %@
Ace2HPMInterface::locatedDevices...
Content-Length : %lu\n
SIGHUP
x-fdr-manifest-prop-edak-cert
tcrtUploadRecertified
tcrt
seputil --pair LYNX output
decodeCertData return error = %lx
failed to create dataStorePath
akstest_unwrap_key
decodeCertData failed, attestation is malformed
ARUMogulGenerateSignatureImplI2C
fail to create lynxSerialNumber, lynxSerialNumber is NULL
RegionCode
ARU0CfgHandleTypeMissingCurrentAPTicket
ReferenceFramesSetInfo, index: %d, type: %d, count: %d, size: %d\n
%s sysconfig (0x%p) or manifest (0x%p) argument was null
x-fdr-sensor-auth-key-certification
salt has wrong type: %@
ARUTristarParseSecData failed
cert is NULL
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapKey failed with 0x%x%s\n
replySize == sizeof(cmd_get_brunor_collection_key_out_v1_t)
%s: fail to decode certificate of offline signing
Failed to Base64 decode fusing data, error: %d
ARUMogulCertificationGetComponentType
_addNumberEntryIntoSysConfig
_ARUCreateCStr
AMSupportBase64Encode valueStr returned %d
0019
Unable to create dakContext->manifestProps
pdak
Get the flag number is : %@
CCECCryptorExportKey returned %d
tbsSubjectItem is NULL
failed to apply restore options to fCfg.
@Timer9,Ticket
Ace2DerDecodePrivateBody error %d \n
AuthCSR
FDRCAURL
DcrtRequireSpecificBAAOID
Response:%@
%s: item is bigger on the inside
unwrappedDataPtr or outLength is 0
Final - failed %d\n
libCyrusFDR: ERROR: [%s:%u:%s] kAppleCyrusFDRCollection -> %x%s
AMFDRDecodeIterateSysconfigMetadataNext
no prpc found, error:%@
Failed to create mogul service iterator
Skip generating sysconfig data, continue with adding restore option related keys
Failed to calloc config
akstest_new_ek
attestation
%s: Failed to malloc empty certificate
PED,ApFusesDigest,A
AMFDRDataMultiCopy unexpected error (code %d) on %@
IECS locatedDevices - done.  Objects located: %lu
EkAppleNVMeEANErase failed, kernResult = 0x%x
get SocChipIdEcid failed
%s: %s: certificate chain validation failed
%s: propertyLength != kImg4TagSize
Failed to create crash thread
/containers
Failed to encode payload entry sequence with return: %d
x-fdr-chip-name
reply
%s: Found subCC %c%c%c%c
%s: No need to verify subCC and asid
ProvisioningMAC
ARUPEDVerifyTagInt
dataClassArray is not an array
SIGBUS
fdrInput
%s: failed to find matching inst object propery, returning a mismatched one
%@-%@
000v
multiDataInstance is not an array
%s: failed to decode DER
requested cert is NULL
ARUFDRCreateFactoryWiFiFIKCsrSignature
Can't read enough data from register
echo failed
Required information cannot be queried
%s: failed to find property tag 0x%llu
Failed to allocate ARUVillanovaCtxRef
tcrtData is NULL
OrganizationalUnit
failed to create requestDict
encryptFDRDataForBrunor failed with no space, try again with memory size = %d
_getProvisioningStatus
Error setting status code string
failed to modify sysconfig, error: %@
0001
failed to create key(%@) or value (%@)
Write Key To Test Failed
Can't generate signature for CSR!!
EnableRunTaskConcurrently
UploadPrpcOptions
%s: failed to parse property list
macTypeStr is NULL
WcrtCertifyURL
_AMFDRDecodeInstPropertyMatching
Metadata
AppleNVMeEAN
AMSupportBase64Encode verifyKey returned %d
DsUrl
001a
Lock mtpProgram Failed
sikPub is NULL
...Unable to open IECS service.  err = 0x%X
%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n
ARUFDRRequestSubFactoryCerts_block_invoke
start to encryptFDRDataForBrunor
000q
000L
mtpProgram Failed
%s: verifying subCC, skip comparing digest of the entire data
%s: cannot find data in multi combined format
%s: PKI: verify cert was issued and signed by issuer (success)
000U
ARUFDRMultiDataInstanceDownload
TRUE
outDataLength
 string
%@/%s
AppleCyrus
ARUFDRRequestFactoryCertIndividual
v24@?0@\"NSData\"8@\"NSError\"16
could not create httpRequest\n
Failed to create currentDigest
outputData is NULL
failed to create certifyOptions
can't parse mainInfo sequence
Successfully verified that all subCC values are present for %@
McrtCertifyURL
Error: %@ is in 0Cfg but not in sealing manifest
treekoM is not a Ace2ARUTreeckoManager class \n
Failed to get lock status
%s: PKI: verify cert was issued by trusted root %d (success)
tmpTags is NULL
BoardID
ETHER_MAC2
struct __SysConfig3 *__singleallocSysConfig3(SysConfig3Magic, SysConfig3Version)
RearCameraAuthICSignedCSR
PutCombined
SIGIO
statistics is NULL
_AMFDRDecodeVerifyData
failed creating %s
YonkersIR3,ECID
can't get kMGQHWModelStr %d
ClientId
createSignatureFromEUicc
IsPearlKeyReady
/Library/Mail
creatSsoTicket failed
ARUFDRUpload %@ failed
ARUMogulCreateMogulService
%s: FDR2 Format unexpected tag: %llu
ARUPEDVerifyTagBool
AMSupportHttpCreatePostBody error is %d
*outLength >= minimalOutputBufferLength
Unable to allocate sysconfig3vX object. Likely due to an unsupported magic: 0x%X or version: 0x%X
_createToBeCertifiedBlob
SoftwareBehavior
DEREncoderAddSequenceFromEncoder failed
_initializeContextInfo
Unable to create propsStr
failed to read key 0x%04X
/logs
%s: context is NULL
hexdump
@Baobab2,Ticket
_formatClientId
entering ARUFDRSetDAKCerts
ARUFDRDownload
ComponentFunction
RID
failed to allocate encoder
options->dakContex is NULL
Aries
Unsupported cryptoVersion to create CSR
pspcData
%s: Failed to malloc fdrDecode
ARUSensorAuthCertificationUpload
AMFDRDataMultiCopy got NULL return
CLASS C
lcrt
no data collected in PEidSubCCOutput
the respons length is %x and %x
ARUProvisionVillanova
Invalid MAC address length: %lu, expected %d or %d.\n
send Ack To Server failed
AMFDRDecodeMetaProperty
/mnt5/lynx.dat
can't get B64ChipId string
can't write cmd to set target
LCfg
3Bg3
/.fseventsd
Offline signing verification passed.
We can't decide which Mogul it is if IDSN is missing
SIGTERM
failed to convert path to cstring
-[Ace2ARUTreeckoManager decodeProvisioningData:]
_ARUFDRMergeDict
ARUUtilsParseCertExtension failed, error = 0x%llx
device BOARDID is nil
type of dictKeysBuffer[%d] is not supported: %@
Remote
%s:%spid:%d,%s:%s%s%s%s%s%u:%s self has no sig%s\n
ARUFDRToolsCheckSubCC
failed to generate %@ CSR format
Task: %d, fetching DAK cert got error
%s: failed to find MANP (manifest payload) tag
%s sysconfig metadata entry cannot have both string and data fields populated!
Verify LockStatus Read Failed
x-fdr-device-certificate-version
outWrapData is NULL
Failed to create FDR options dictionary
Failed to read the current cert chain key from Area51
kern.bootargs
libCyrusFDR_get_public_key
Reference set dictionary written to %s\n
AccessoryCertificate
ARUFDRCreateAMFDRWithOption
@Golay,Ticket
signature is mismatched 
SIGSYS
decode error
Failed to create httpHeaders dictionary
ARUUtilsVerifyCertChain returned a NULL leafCert
Thread %d crashed with Thread State:\n
authentication challenge not received
Start Auth Write Failed
-
ARU0CfgHandleTypeDoNothing
000s
Upload wcrt failed!!
@Acdcuc5,Ticket
auth,mlb
device ECID is nil
ARUTristarTreeckoManagerSendRequest
iPhone
B64_OTPV2
Already Provisioned, attempting to lock...
create log string failed: %s
%s:%spid:%d,%s:%s%s%s%s%s%u:%s incorrect attestation data%s\n
e-apfs
lynx-count
cfString or cStr is NULL
SIGWINCH
refFrame
type of %@:%@ is not supported
dataStoreUrl is NULL
vKey and cKey from server are vKey=%@ cKey=%@ 
/root/Library/Preferences
can't get kMGQBoardId %d
FDR Data does not match
can't get cert data from Area51
%s either data or string must be non-null
SIGPIPE
tid<%d>, %s
libCyrusFDR_get_imm_hash_for_sandcat
failed to append PUT permission
x-fdr-manifest-prop-pdak-cert
local data verification passed with expected trust errors.
Try to generate 0Cfg
Missing required OID %s (decode error 0x%llx)
%s: failed to parse metadata content: %d
Unable to retrieve lock esmStatus failed.
Failed to efface USB Zone
syscfg
/Library/ApplePushService
Configuration cleanup failed
Write Challenge Data Failed
failed to put dummy data to local
ProvisioningResponse ID is wrong, expecting 0x%04X, getting 0x%02X%02X
failed to convert data Oid
_createProcess
decode_pfk_bulk_data
@Acdcuc4,Ticket
akstest_rewrap_ek
_createBaseFusingInput
x-fdr-manifest-prop-sdak-cert
AuthSalt
tristar
,
Invalid crash thread in report\n
struct __SysConfig3MetadataEntry *__singlesysConfig3GetMetadataEntryForKey(struct __SysConfig3 *__single, const char *__single __terminated_by(0))
USBPortController7,ECID
invalid param length, got %u, expecting %u
/System/Library/Pearl/ReferenceFrames
%@/factory/%@.created
signing public key is NULL
can't write cmd to AID pass-thru register
%s: ctx->inData must be non NULL and ctx->inDataLength must be non 0
failed to allocate accessoryDataArray
cmdStr is NULL
ComponentAttributeSoCChipIDECID
/Library/Keyboard
failed to allocate mergeValueDict
AMSupportBase64Encode maniStr returned %d
ProvisionSerialNumber
failed to add key %@
eeid
ARUFDRCreateDummyCsrSignature
EscrowTokenPeriod
@YonkersIR3,Ticket
SourceDSURL
%s: FDR data trust evaluation failed.
SEPAttestQA
%02x
permanentKeyLength
%s: %s
0004
unexpected path. Neither DAK certs nor certs been downloaded from FDR server
Failed to write 0Cfg to EAN with error %d
CLASS D
AuthPubKeyHmac
chipIDStr is NULL
-[Ace2ARUProvController programOTPKey:forSlot:]
%s: malformed metaProperty Format
%s: Img4DecodeEvaluateManifestProperties failed
@Timer12,Ticket
mgRet isn't a class
ARUFDRCreateDummyCsrSignatureWithCryptoVersion
1.2.840.113635.100.8.7
mappedToISP:\t\t%s\n
%s: kFDRTag_inst propertyValue != instValue
PEidSubCCInput has wrong type %@
manifestData is NULL
PED tss Request
2
@JasmineIR1,Ticket
outDataSignature is NULL
ARUMogulCertificationInternal
/protected/trustd
migratedSikDataClassInstances is NULL
encryptFDRDataForBrunor failed, error code = %d
ecdh public key convert fail \n
%s: failed to decode sealing manifest body
decodeOutData allocation failed
called with a NULL matching dictionary
Mogul device is not ready
memory zone check failed
fdrContext is required
the battery version inside vcrt doesn't match to the expected one
AMAuthInstallCreate failed
Error: No current AP ticket
Invalid response length %u
area51
AMAuthInstallAddTrustedSSLCACert failed for %d, %@
myURL is Null
AMFDRDataMultiPut with SIK failed
UseSikFormat
%s:%spid:%d,%s:%s%s%s%s%s%u:%s dumping attestation info:%s\n
%s invalid argument. sysconfig and key cannot be NULL
Devices
x-fdr-client-id-sik
DAKs/EDAK.der
%s: Certificate Properties extension not found
return value is not number
dataRef is Null
dataClass is NULL
systemDataStorePath is required
aks_fv_new_kek
Buttons2,ECID
Key Select Write Failed
can't convert to base64 string\n
sikStr is NULL\n
aneUnmapFunction:\t%s\n
service is NULL
failed to fetch existing certificate from server
%s: Skipping trust root check (trustobject unset)
_ARUTristarGetRsaPublicKey_block_invoke
ARUVillanovaCreateAuthCertificationDict
chipName has wrong type: %@
%d: %@/%lx
failed to get error code via AID, retVal: %x
@SE2,Ticket
-[Ace2ARUTreeckoManager Ace2DerDecodePublicBody]
wrong cert number (%d) returned from server
%s: kFDRTag_inst propertyLength (%d) != fdrDecode->manifestUniqueID.length (%zu)
cert
addSysConfigEntry
Area51 is not using the cert in 0x5102. Read value: 0x%02X%02X
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestRewrapEK failed with 0x%x%s\n
subCCOutputKeysBuffer is NULL
derChainData is NULL
failed to add key and value into sequence
ARUEANWriteImage
%s: malformed offline signing public key
ARUVillanovaCreate
fdrContext->apticketData is required
/iomfb_bics_daemon
Unsupported AID mogul type
%s: failed to decode subCC digests sequence
_Bool _sysConfig3AddMetadataEntry(struct __SysConfig3 *__single, struct __SysConfig3MetadataEntry *__single)
%s sysconfig is NULL.
x-refkey-certificate
Can't allocate memory for tristar service
%s: end of trusted root sequence found root_cert=%d
%@/factory/mfi/mfi%d-%s.der
iCheck marker path is NULL
eCfg data creation failed
Failed to decode old eCfg data
ARUUtilsCreatePkcs7CertFromCertChain
libCyrusFDR: unit_is_j126 %d%s
=
MACH_HEADER
%Y%m%d%H%M%SZ
chipName is NULL
authPollDone timeout 
unsupported mogul type, exit...
Fail to generate ccrng !\n
Final Pre-fusing output: %@
Unable to create minimalManifestPropertyCheckTag
Apple Inc.
Found AppleNVMeEAN object
===== remote cert equal to the cert inside mogul chip(digest not compared) =====
invalid parameter
YonkersVisible2,ECID
publicKey is NULL
lcrt is successfully claimed
Skip 0Cfg write because no sealing property was found for this product
%s: Metadata must be SET Container
AMAuthInstallSetSOCKSProxyDict failed: %d
AMFDRDataDelete got error
x-fdr-euicc-certs
vKey base data%@ fail 
pearl key is not ready, encryption isn't started
-[ARUService setLogHandlerConn:]
/Library/MedicalID
innerHeaderKey failed to create
OTP key2 verification fail
_formatProductName
Get data successfully from server
attestationData is NULL
failed to encode attestation to base64 format
libCyrusFDR: entered libCyrusFDR_is_multilynx_present%s
can't create commandCode string.
SerialNumber
Multi lynx certificate collection finished
appv
Couldn't find AppleNVMeEAN object
outPolicy is NULL
failed to allocate command
bdak
%s: PSPC data found.\n
mappedToSEP:\t\t%s\n
dataClassesToMerge is NULL or malformed
Tag was not the expected Payload tag %llX
could not split parameter: %@
%s DERPayload is NULL
000x
unknown component type, exit...
USB_ETHER_MAC
Acdcuc3,ECID
000a
BOARDID
AppleHPM
/MobileSoftwareUpdate
0016
Final - failed %d 
eumCertificate
csrAttributes is NULL
-[Ace2ARUProvController provisionKey:chanllgeKey:verifyKey:forSlot:]
failed to add to certChainEncoder
AMFDRDecodeParseDERLengthFromBuffer
failed to allocate outerSetEncoder
ETH_MAC
hasFausInOldTicket = %d
%s: malformed AttributeTypeAndValue format: %d
No XPC log: %s
_Bool sysConfig3ManifestGetFullHMAC(struct __SysConfig3ManifestEntry *__single, SysConfigData *__single)
collectAuthlistable failed
ARUFDRClaimAndDownload
Cannot verify that all subCC values are present for %@.
MLBNumber
pathString
mismatched SecureStorageSCFDigest of dev-fused, ignored!
Key 0x%02X%02X is not written
valid response id, returned: 0x%02X%02X, expected: 0x%X
failed to add data content
Failed to write FDR data to EAN with error %d
lynx
ispMapFunction:\t\t%s\n
000n
Tristar Provisioning Verify Auth Interrupted
ARUFDRUpload
failed to get manifest from ticket
CertifyURL
malformed dataInstance
omitting constant prefix for pub key comparison
EXC_CRASH
libCyrusFDR: ERROR: [%s:%u:%s] cant allocate mem%s
_Bool sysConfig3UpdateHMAC(struct __SysConfig3 *__single)
pub key mismatch
--sourceFDRPath
replySize <= (16 * 1024)
AMFDRDecodeVerifySealingRequest
%s: offline signing public key length mismatch
None PED feature supported for SoC 0x%x
prpc
/Library/SyncedPreferences
Key Parity Not Odd
Lock USB Zone failed!!
AMFDRSealingMapCopyInstanceForClass %@ failed
sendProvisioningRequestCmd error %d \n
2006-05-31
soc-fingerprint
-apfs_shared_datavolume
AMFDRDataAppendPermissionsString failed
Ignoring AMFDRDataMultiCopy trust error on %@.
Input data is NULL
DAKs/MDAK.der
pubKeyDigestString is NULL
Product str isn't in correct format
Verify function return error %d\n
failed to retrieve chipID
fdrOptions is NULL
failed to create dakCertsTags/propCertsTags 
ComponentAttributeComponentIndex
Tag %@ (0x%x) is in 0Cfg but not in sealing map
%s: FDR Trust Object digest mismatch.
Can't decode C1 from response\n
/Library/SMS
subCCVal has wrong type %@
Caught a signal %d sent to aru, possibly a crash!
Apticket is NULL
/keybags
AMFDRDecodeIterateTrustObjectTrustedBegin
%s: malformed FDR Trust Object SslRoot, invalid trusted tag length
%s: kFDRTag_inst propertyValue != fdrDecode->manifestUniqueID.data
_Bool sysConfig3DeleteMetadataEntryForKey(struct __SysConfig3 *__single, const char *__single __terminated_by(0))
_formatSerialNumber
return value is not cfstring
HWModelStr
failed to create eidValueHexStr
%s: context must be non NULL
v8@?0
Can't alloc memory for mDecryptionBody\n
decode length = %d is too long
%s Full HMAC does not match.
pubKeyDigestStringData is NULL
failed to create a buffer for reversed cert chain...
dataToSign is NULL
_find_sealed_data_hash
%s: inData must be non NULL and inDataLength must be non 0
Failed to copy options dictionary
arrayCount is 0
ARUFDRLocalCopy
/db/com.apple.xpc.launchd
mergedDict is empty but PEidAllowMissingData is set
expected BatteryVersion
Unknown auth chip
unescapedValue is NULL
path is NULL
respLength is wrong
config is NULL or empty, skip
%s: malformed FDR Combined Format (trustObject), invalid tag length
Unable to decode payload with error %d
IECS createUserClient - status = 0x%lX, self.service = %u, self.connection = %u (prior to IOServiceOpen)
generate ecdh key pair error result = %d\n
logCallback
write-0cfg
/Library/AddressBook
%s: PKI: verify im4c cert was issued and signed by issuer (success)
AMFDRDataDictPut failed
read cert digest (%d bytes) from mogul memory zone and passed after comparison
%s (%s)
libCyrusFDR: ERROR: [%s:%u:%s] kAppleCyrusMLTestDelete -> %x%s
_AMFDRDecodeVerifyDataCallback
_Bool sysConfig3AddMetadataEntry(struct __SysConfig3 *__single, struct __SysConfig3MetadataEntry *__single)
ReadReg returns erroCode =  %x
cannot get multiResponseErrors
effaceMemoryZone
UUID
statusString:%@
ARUTristarTreeckoManagerSendRequest failed.
sdcrt/sdcrt.der
%s: malformed offline blob
ARUParseDERLengthFromBuffer failed
output is NULL
bCfg
%s: PKI: verify cert was issued by trusted root %d
ARU0CfgHandleTypeGenerate0CfgAllowFailure
/Managed Preferences
%s: malformed FDR Trust Object SslRoot, expected tag %c%c%c%c found tag %c%c%c%c
USBPortController1,ECID
USBPortController9,ECID
DAKs/PDAK.der
unexpected size, attestation length: %lu, supportedModule = %x
x-fdr-sensor-operation-context
AMFDRDecodeIterateSysconfigPayloadNext
AMFDRDecodeCreateCertificateChain
x-fdr-sensor-mac-type
@Timer1,Ticket
EnableSslValidation
AppleRestoreUtils-
can't encode Cert data
aks_run_internal_test
AppleKeyStore
000N
@JasmineAP1,Ticket
 TristarRsaKey is = %d, not ccRSAKeyPublic
Failed to query BMUBoardID.
ARUArea51WriteKeyValuePairs
/Library/UserNotifications
collectionKeyLength
Baobab,ECID
aks_fv_rewrap_kek
libCyrusFDR: ERROR: [%s:%u:%s] cant determine multlilynx presence%s
%s: Attribute must be set container. Found unexpected tag 0x%llu, skipping
DAKString is NULL
v32@?0@\"NSData\"8@\"NSData\"16@\"NSError\"24
memory zone is locked, no need more certification
000j
ARUTristarTreeckoManagerParseSecData
malformed subjectPubKey %d
Failed to decode old appv data
ARUPEDLogBase64Dict
%s: failed to init certificate sequence
euicceumCertificate
ZG:BMUExpectedBoardID
AMSupportCommonCopyHexStringFromData failed %d
/log
%s: failed to parse cert properties: %d
Permissions
unexpected size, signatureLength: %lu
CertifyComponentType
%s Requested version (0x%X) does not support HMAC.
set multiSealingMetadata failed
attestation is null
Failed to allocate payloadEntry
/mobile
Decode sequence error: %d
ped mismatched %s: 0x%llx vs 0x%llx
Library-PearlFactory
Tag was not the expected manifest tag %llX
BMU,UniqueID
outPkcs7Cert is NULL
Can't allocate memeory for public body 
%s: malformed FDR Multi-Response Format
lock zone error code is %d !!
--lynx_get_app_hash
B64_OTPC2
EXC_BREAKPOINT
verify-0cfg
%i,%u,%u,%u,%lld,%lld,%lld,
_ARURead0CfgFromEAN
%s invalid argument. sysconfig and entry cannot be NULL
IDSN not found for Mogul I2C service, skipping
Error status %d\n
%F
%s: implementation must be non NULL and signatureOid must be non NULL
failed to create ticketData
RID is NULL
Generating reference frames info record...\n
signatureLength
%@%@
@USBPortController3,Ticket
failed to get SecureStorageSCFDigest
@YonkersIR2,Ticket
dict has wrong type %@
Tag
SignData
fuse: %@
dump_bytes_internal
%s: can't parse FDR Trust Object SslRoot sequence
GetErrorCodeRawAID
ARUMultiLynxUpload
_AMFDRDecodeDERFDRItem
ARUParseDERLengthFromBuffer return incorrect DER length
can't get signatureData
attestation is NULL\n
ARUTristarTreeckoManagerSetOption
failed to find needed OIDs
_ARUDelete0CfgFromEAN
failed to program the certificate chain to Area51
/backup
%s: kFDRTag_inst property == fdrDecode->uniqueID, found corresponding Data Instance.
@CameraISP1,Ticket
keyData has wrong type %@
kToBeSignedPayload
failed to fetch trust object
Lock Customer ASN Zone succeeded
Task %@ failed
_connect != ((io_object_t) 0)
%s: outRawData and outRawDataLength must be non NULL
can't allocate headerOptions
eUiccString is NULL
%s: failed to parse certificate dictionary
ARUFDRToolsMergeFDRv3Data
failed to sign with keyType: 0x%08x
can't write data to memory zone %d, line: %d
Failed to create string from fusing data
ProvisionTristarOptions
/Library/NFStorage
can't create cert chain from PEM 
mergedDataClassArray is NULL or malformed
000z
MultiRequestErrors
failed to malloc buffer
%s: DERParseBitString(sig) failed
Upload mcrt failed!!
Unable to parse response data from provisioning server 
failed to create Pkcs7 cert from remote cert chain
%s: malformed offline signing public key tag
0002
_formatBoardId
MPN
Error setting status code string.
acss
/Library/TCC
aks_kext_get_options
PED,SecurityDomain
_mtpProgram
Area51 certification finished, attempting to lock...
ARULynxCopyMultiSecureStorageSCFDigest
ARUWcrtUpload
AP
ARUFDRWriteFDRiCheckMarkers
Did NOT build matching dict
Mac Display
restoreos
failed to chown parent directory as mobile
failed to attest ref key: 0x%08x
apticket has both rfcg and esca
(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || messageSize
%s: AMFDRDecodeIterateTrustObjectRevokedNext failed
can't get boardid string
AMFDRSealingMapCopyInstanceForClass failed
%s: subCC is not hashed
%s: FDR Combined Format unexpected tag: %llu
serverUrlStr is NULL
publicKeyData is NULL
AMFDRDecodeVerifyCertIssuerNoRevocation failed for leaf cert 0x%016llX
000l
/System/Library/Caches/com.apple.factorydata
signedCSR has wrong type: %@
USBPortController5,ECID
BMU,BoardID
wrapData is NULL
ARU0CfgVerify
CCRSACryptorEncrypt failed = %d
failed to allocate dataInstancesToWrap
DAKs/BDAK.der
signature is NULL
replySize >= sizeof(*outData)
keyHashStr is Null
su
DcrtRequireBAAOID
ARUArea51LockManufacturerNVM
ARUArea51IsProdPart
ARUArea51Provision
%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n
failed to get publicKeyHexStr
SIGTSTP
_FDREncodeCreateDataFromOid
%s: fdrDecode is NULL
PEidSubCCOutput is NULL
Timer,ECID,2
failed to write apticket
_ARUCompareTagsInSyscfgAndManifest
ARUUtilsChangePathOwner
libCyrusFDR: ERROR: [%s:%u:%s] kAppleCyrusFDRCollectionConfirm -> %x%s
--dataClasses
libCyrusFDR: ERROR: [%s:%u:%s] kAppleCyrusMLDiagnostic -> %x%s
%s key was invalid
currAuthlistables has wrong type %@
either CA or Trustobject URL is missing
createEUiccSignatureDict start
EXC_BAD_ACCESS
/Library/NanoTimeKit
%s: FDR failed to decode multi combined Data img4
_AMFDRDecodeSequenceString
failed to CFDataCreate digestData
failed to create data store directory
keyData is nil
Failed writing command
aks_attest_context_dump
AMFDRDecodeFDR2Data
encodedOutput has wrong type %@
can't parse next sequence of mainSeq
_createFDROptions
EnableProxySsl
/root/Library/MobileContainerManager
%s: decodeAlgId failed
struct __SysConfig3ManifestEntry *__singleallocSysConfig3Manifest(SysConfig3Version, const SysConfigData *__single, const SysConfigData *__single, const SysConfigData *__single)
_formatSessionKey
fail to create multi lynxData: %d
versionNum is NULL
ChipID ECID inside mogul doesn't match to the SoC
attestation key cannot be read
000W
AppleAuthCP
decode nonce is Null
/Applications
%s: data instance cannot be missing without kAMFDRDecodeOptionAllowNoDataInstance specified
_AMFDRDecodeGetDataInfoCallback
@USBPortController5,Ticket
failed to create metadata dictionary
       expected: '%c%c%c%c'
Failed to allocate out_buffer
_get_oid_property_value
NONE ApFusesDigest matched!
_formatB64BoardId
Mac
can't get cert data from Mogul
EXC_EMULATION
First AuthCtrl Write Failed 
aks_attest_context_get_blob
Error Final Mtp Write Failed
Request for fusing data failed.
Component
Repair UCRT
ARUPEDTask
failed to add crls
MergedDataClassArray
com.apple.pearld.check_secure_streaming
objectSize:\t\t%d\n
%s: asid subCC data != fdrDecode->asidSubCCID
cannot begin with an already initialized iterator
can't write cmd to start challenge
%s: malformed DERFDRItem, expected tag %c%c%c%c found tag %c%c%c%c
Clear Auth Status Failed
ARULynxCopySecureStorageSCFDigest
libCyrusFDR_get_imm_hash_for_sandcat failed: %d
aks_fs_supports_enhanced_apfs
%s: malformed cert property key: %c%c%c%c
statusString:%@ and responseStatus is %d
Provisioning state not valid.
T_MAC
Failed to get thread exception state: %d(%s)
ARUAllowMissingSyscfgData
v12@?0i8
@CameraAP2,Ticket
libCyrusFDR: cert(%d) len %jd%s
size == sizeof(response)
mpub
scrt
EnableVerboseLogging
%s: subCC digest length mismatch
%s: malformed FDR Multi-Response Payload Record Format
could not create cert from PEM buffer %d
Not found keys in keyDict
APTicketData
skeyDataRef is Null
Unable to create CSR RefKey signature
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n
getSavageProvisioningData
IODeviceTree:/chosen
RearCameraAuthIC
malformed lynxData
keyDict is nil 
derCert is NULL
SysconfigStage
%s: trustobject does not contain trusted key
cKey is nil \n
keys required cannot be read: %@
%s: FDR Trust Object revoked client ID found
outCtx is NULL
strExtRepData is NULL
Invalid value length %u
%s: FDR Multi Combined Format unexpected tag: %llu
ARUServiceMsgCopyRefKeyPubKeyAndAttestation return %d
euiccCtx is null or not cfdata!!
MarketingBehaviorHardware
pemData is NULL
/Library/SpringBoard
ARUFDRCreateEUiccCert failed, but allow incomplete data is set in FDR option, continue
%s: can't parse top-level container
%s: Img4DecodeGetPropertyData(kFDRTag_prid) failed.
migratedDataClassInstances is NULL
AMSupportBase64Encode challengeKey returned %d
%s: Img4DecodeGetObjectPropertyData failed
__os_warn_unused(__builtin_add_overflow((dataLength), (2 * 16 + __builtin_offsetof(psd2_encrypted_t, encryptedData)), (&minimalOutputBufferLength))) == 0 
%s: trustObject is NULL
ARUPEDCreateAuthInstallRequest
USBPortController3,ECID
BasebandUpdater
failed to decode base64 string: %d
%s key must be non-NULL
@AVISP1,Ticket
ARUMogulIsMemoryZoneLockedImpl
failed to get attestation
maniStr is nil !\n
sparse
%s: PKI: verify cert %d was issued by cert %d failed with error 0x%016llX
%s data cannot be length zero
creatSsoTicket required
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestCheckClass failed with 0x%x%s\n
*signature
void _freeDEREncodeSysConfigPayloadEntries(DEREncodeSysConfig3Payload_t *__single)
CAURL
xpc minimalManifestPropertyCheckTag error code is %d
xpc setDigest error code is %d
Unexpected sysconfig key type
v16@?0@\"NSNumber\"8
failed to allocate buffer to fill string
sema
%s: failed to decode metadata: %d
%s: malformed FDR Multi-Response value Format
@Cellular1,Ticket
ARUFDRCreateMFiCSRFormatForNapoli
SIGABRT
/Library/Logs/AppleSupport
%s: publicKey must be non NULL and publicKeyLength must be non 0
can't create uuid string for current session
%d: %@/%lx : %@
arm_thread_backtrace
%s: failed to decode payload: %d
Ace2DerDecodePublicBody error %d \n
restore options is NULL
attestation is NULL
can't parse next sequence of mainDerSeq
Unable to open IECS service.  err = 0x%X
Not waiting for response for IECS command '%c%c%c%c'
Create Certificate Chain failed
mcrt
!1.2.840.113635.100.6.71.1
ARU0CfgHandleTypeGenerate0Cfg
-[ARUProvSequencer provisioningAck:ackCmdType:]
ARUServiceMsgSendFdrStatistics finished
_AMFDRDecodeVerifyChain
DEREncoderAddSetFromEncoder failed
rsaPublicKey is NULL
AppleAuthCPAID
PROV
return value is not a number
failed to query os version
Attributes
optionsDict is NULL
mountPoint is NULL
failed to create aks params
%@.%@
AuthInstallProvisioningServerURL
PED tss Response
AVISP1,ECID
Error formatting key for string.
can't parse mainItemInfo sequence
ARUFDRCreateMFiAccessoryData
maniStr is NULL
task options is NULL
dictFileName
Apple Accessory Host Attestations
2.5.4.3
Content-Length
Can't decode C2 from response\n
/Library/Preferences
%s: can't parse FDR Trust Object Revoked
@YonkersVisible2,Ticket
copyMacToBinary
%s: invalid payload tag: 0x%llx
Subjects
/MobileAsset
AMFDRDecodeFindSubCCAndReturnAsPayload
tristar-provision
libCyrusFDR: ERROR: [%s:%u:%s] kAppleCyrusMLTestWrite -> %x%s
Tag is %@ and value is %@
failed to allocate *outDataSignature
Write memory zone failed %x and %x
0014
ProvisionVillanovaOptions
%s: can't parse FDR property meta
PersistCertificate
base64CaString is NULL\n
%s: FDR Sealing Request trust evaluation failed.
%s Payloads with the deleted flag are only supported on version 0x%08X or higher.
Acdcuc4,ECID
Tristar Provisioning Verify Miscompare %x != %x at %d
The key is not existed
%s Payload HMAC does not match.
PCON4,ECID
Polaris,ID
dcrt/dcrt.der
%@ file doesn't exist at local.
failed to add cert chain
%.6f
Failed to get UID or Nonce or Chipid or productionMode from pre-fusing output
DMC,ECID
iPhone OS
provisioning failed: retVal: 0x%x
/Library/ISP
libCyrusFDR: ERROR: [%s:%u:%s] kAppleCyrusFDRVerify(reset) -> %x%s
%s: outImg4Blob must be non NULL and outImg4BlobLength must be non 0
failed to decode DER
/Library/Logs/CoreDuet
%s: AMFDRDecodeIterateTrustObjectRevokedBegin failed
%s: ignoring offline signing verification error 0x%016llX
can't parse next sequence of tempinDerSeq
Memory
The Battery Version inside vcrt matches to the one actually installed
ARUFDRRequestAndSaveMFICerts
arm
0009
can't generate dummy pearl data
refKeyBlob is NULL
RestoreOptions
x-fdr-manifest-prop-%@-key
SaveLeafDAKCertOnly
osk digest
Unable to retrieve provisioning state.
can't decode public data\n
tempString
amfdr is NULL
subCCInputKeysBuffer is NULL
/Library/NanoPreferencesSync
_AMFDRDecodeVerifyCertIssuerInternal
Failed to create base fusing input
currDataInstance is NULL
malloc mBodyDerDecoder.buffer fail \n
ETHER_MAC3
Can not get old AP ticket from EAN
task is NULL
Decode inData error
failed to lock Area51 Vendor NVM
(type == kPearlFactorySeaCookieValidateTatsuTicket) || reply
RearCameraAuthICProductionMode
subCCInputValuesBuffer is NULL
Decode manifest tag is 0x%lx 
key
vDecodeData verify data: %@ len: %d
EnableSso
/Library/CoreDuet
0000
failed to query lynx from device
ARUArea51WriteAppleComponentCertChain
Memcpy algorithmIDData error! \n
outCert is NULL
sendEchoAckToServer failed
001b
failed to write marker (error %d)
ARUVillanovaCreate failed.
decodeIfAttestationIsOriginal
%s: minor version not supported: 0x%x
_startAuthentication
invalid subTaskIndex
Devices - eUICC
getRequestInfo
/Library/ControlCenter
Dotara provision type!
sendRequestSync return error
instanceArray in NULL
no leaf cert parsed out
aks_attest_context_verify
unmappedFromISP:\t%s\n
%s: missing public key algorithm parameter OID
psd3
ARUServiceMsgSetDigest
The option for using the existing certificate is not specified
failed to convert signed data Oid
%s: failed to allocate *multiCombinedDataIterator
Lock Customer IMSN Zone failed!!
origRawCertItem is NULL\n
EXC_RPC_ALERT
%s: memcmp( uniqueIDInfo.content.data, uniqueID, uniqueIDLength) != 0
%s: magic size is invalid: %lu
requestDict is NULL
dict is NULL
Validate %@ failed
Unable to create metaDataKey
refFrameData
Found OID: %s
failed to create station amfdr
ARUServiceMsgCopySsoTicket
MarketingPartNumber
pdak && pdakLength
%s: ClientID extension not found
000Q
ARUFDRClaim
can't read cert length
Efface and lock Mogul memory zones failed!!
ARUApticketGetChipIDUniqueChipID
failed to get 0x%llx from manifest
@USBPortController10,Ticket
_setCommandCodeOption
B64_C1
libCyrusFDR_get_diagnostic
0015
https://gg.apple.com
Failed to get registry properties
Found tags in 0Cfg but not in sealing map
EXC_SOFTWARE
%s: failed to get CSR signature from offline blob
Failed to create sensorTypeNum
claim permsStr is NULL
Unable to create propCertKey
%s invalid arguments. entry and data cannot be null
@Timer4,Ticket
000d
Unable to read configuration status.
get a proper attestation cert from mogul successfully: %@
failed to create PKCS7 signed data
%s: Img4DecodeGetPropertyData(0x%x) failed.
multilynx cert_len (%d): %zu
aa digest
%s: invalid key length: %lu
%s: FDR Trust Object digest is NULL
Multi-claim and Multi-download successfully - \n%@\n%@
generate new session key failed 
local appv found and sync to fCfg
SavageCamInterfaceSensorPreFusing failed with error: 0x%x
subCCOutputValuesBuffer is NULL
Failed to compute digest of core data 
UseSOCKSHost
410
 (skip)
%s: Sealing manifest is NULL or 0 length
%s: FDR failed to get payload from multi combined data
%s: kFDRTag_inst property != fdrDecode->uniqueID
%s data was zero length
@USBPortController1,Ticket
1.2.840.113635.100.6.71.3
@USBPortController8,Ticket
MFiProductPlanUID
AMFDRDecodeVerifyMultiCombinedDataIntegrity
failed to create marker for MFi
ARUFDRCreateEUiccCert failed and no incomplete data set
310
failed to create CS symbolicator
@DCV,Ticket
0007
Unable to get DER data 
userInfo is NULL
dataClassesToMergeArray and mergedDataClassArray count mismatch
eUiccCert is NULL
%s: cannot begin with an already initialized iterator
%s: buffer is NULL
@Timer11,Ticket
edak,ecrt
failed to create remotePolicyNonceDigestData
Did NOT find service(s) matching AppleHPM
ProvisionURL
%s: can't parse FDR Multi-response Metadata
%@ - ARUFDRSetDAKCertsInternal failed
ARUFDRRequestSubFactoryCerts failed for task %d
unexpected size, permanent public key length: %lu, supportedModule = %x
(*outRespCtx)->keysNotFound is NULL
_ARUSensorAuthCertificationUpload for %@:%@ failed
ExeciAP2ControlSessionCmdI2C
%u
@Acdcuc2,Ticket
collectAuthlistable
Timer,ECID,9
VerifyData
%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n
000Z
Cellular2,ECID
kAppleNVMeEANRead failed, kernResult = 0x%x
ackStr  %@ \n
prpcSensorCtx is NULL
000X
SkipFGSN
ComponentType
read cert (%d bytes) from mogul memory zone and passed after comparison
verification return lenth is %d
PrintHttpStatistics
/Library/DeviceRegistry
/Library/Trial
Wireless1,ECID
YonkersVisible1,ECID
UseSOCKSPort
mfiCertPath is NULL
failed to parse mfiProperty
%s: failed to parse boolean: %d
%s sourceData was 0 length
tcrt FDR upload failed
auth,display
00000915
IOServiceOpen on AppleNVMeEAN failed, kernResult = 0x%x, fConnection = 0x%x
DEREncodeSysConfig3Payload_t *__single_createDEREncodeSysConfigPayloadEntries(struct __SysConfig3PayloadEntry *__single)
mismatched %@ of dev-fused, ignored!
@Baobab,Ticket
000b
Unable to create dakCertKey
outErrorCode cannot be NULL
can't allocate memory for atte cert
AMFDRDecodeMultiSealingResponse
%s: Img4DecodeGetPropertyData(kFDRTag_cptp) failed.
camChannel
@USBPortController2,Ticket
copyTcrtDataByServiceName_block_invoke
@USBPortController12,Ticket
AMFDRDataMultiCopy got NULL return, but wrapDataCheck isn't needed, skip wrap data
failed to copy data classes and instances
Allow missing data class %@.
%s was stopped by signal %d
Failed to efface Qi Zone
aks_attest_context_get_uint64
%s: ignoring incomplete subcc error 0x%016llX
PEidSubCCInput is empty
failed to allocate outerSequenceEncoder
sek
AMFDRPermissionsRequest failed
minimal-manifest
CFArrayCreateMutable failed for digests
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %swarning parsing an unverified attestation%s\n
CLASS NONE
count of dakCertsTags/propCertsTags mismatched
sysctl.proc_translated
ARU Tristar Provisioning failed
Submiting appv...
%s: FDR failed to get payload type from multi combined data
FDRDataStoreURL
_aesDecrypt
_ARUArea51RequestProvisionCertChain
Can't get mgRef from MGCopyAnswer %d
error write register %d
MetadataDict
mcrtOptions is NULL
&
dataClassInstance is NULL
Lock Apple Zone succeeded
Unable to handle apticket in EAN
Invalid response id, returned: 0x%02X%02X, expected: 0x%04X
%s: pManifestBodyInfo is NULL
undefinedBag
AMFDRDataMultiClaim failed
keyType is not aks_system_key_fik
Unable to create propTags
Failure code: 0x%08lX
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unpack data failed%s\n
%s: asid subCC length != fdrDecode->asidSubCCID.length
AMFDRDecodeVerifyCertIssuerWithOptions
allDataClasses is NULL
failed to allocate csrSignature
FDR local copy failed.
 rsaPublicKey is NULL, can't verify signature 
AuthCtrl KeyState Read Failed
_AMFDRDecodeVerifySignature
AMFDRDecodeIterateTrustObjectSslRootBegin
Area51 seems dead
%s invalid magic provided 0x%08X
%@/ca/certify
unsupported public key size: %d
%s the refcon arg was NULL
start challenge fail
failed to create directory for iCheck marker (error %d)
ARUKeysProvisioningCopyResponse
%s: no uniqueID is specified, but this is allowed, skip comparing kFDRTag_inst object property
x-fdr-metadata-ChipID
dataClassArrayToCopy is NULL
provisioningAck end\n
Failed to create moduleSNStr
%s: FDR Trust Object revoked public key found
digestLength is 0
failed to create Pkcs7 cert from local cert chain
EXC_GUARD
%s: DERImg4DecodePropertyWithItem failed
%s sysconfig payload entry must have exactly one of data/string/deleted set. data: %p string: %p deleted: %d
AuthInstallSigningServerURL
000P
%s invalid version provided 0x%08X
csrDerData has wrong type: %@
AMFDRDataMultiClaim missing data to claim %@
sik--
%@ already exist in mergedDict, not allow to be overridden
Final fusing step failed.
refPath
%s: failed to get CSR from offline blob
struct __SysConfig3MetadataEntry *__singleallocSysConfig3MetadataEntry(const char *__single __terminated_by(0), const uint8_t *__single __counted_by(dataLength), uint32_t, const char *__single __terminated_by(0))
can't get control session message response, err: 0x%x
Villanova provisioning completed successfully.
/Managed Preferences/mobile
%s: malformed FDR Trust Object trusted, expected tag %c%c%c%c found tag %c%c%c%c
YonkersIR2,ECID
Fetching DAK cert got error
ARUServiceMsgSendTristarEsn
MarketingBehaviorSoftware
bufferLength is 0
UploadPEidOptions
Found %@ in 0Cfg, checking sealing manifest
Can't create CLIENT_ID for current session
%s (%s)\n
B64_MANIFEST
AllowMissingUnwrappedData
AMFDRDecodeSealingRequest
AMAuthInstallHTTPCopyDefaultTrustedSSLCACerts failed
failed to add root
@BMUTicket
TrustObject
------------------------------ \nRequest Content: \n%@\n ------------------------------ \n
lcrt-%@ from MG, not the same as lcrt-%@ read from Cyrus
failed to certify Area51
%s: combinedData is required to be set
USBPortController12,ECID
create baseSequencer error!
Failed to create area51 attestation certificate
verify cert chain successfully
libCyrusFDR: ERROR: [%s:%u:%s] cert doesnt fit %d%s
ApplePearlSEPDriver
clientId is NULL
Failed to get cpu type for pid(%d): %d(%s)\n
unknown parameter ID: %u
aks
%s: can't parse FDR Producer ID sequence
%s: Expecting kAMFDRDecodeImplementationSha384 or kAMFDRDecodeImplementationOffline
ARUFDRCreateAMFDRWithOption failed
skip to validate %@, always return true
%s: malformed FDR Trust Object, expected tag %c%c%c%c found tag %c%c%c%c
CLIENT_ID
unknown or unsupported cert request
unsupported EcP384 key, fallback to EcP256
signatureDer is NULL
outAttestation is NULL
Verifiy return nil \n
BoardId
AMAuthInstallRequestSendSync failed: %d
AMFDRSealingMapCopyDataClassesWithAttribute failed with error %@
ECID
mountedUrl is NULL
ARUFDRCreateEUiccCert
Failed to delete 0Cfg from EAN with error %d
(type == kPearlFactorySeaCookieValidateTatsuTicket) || replySize
Unable to create metaDataValue
ARUArea51ReadNVM
failed to allocate *outLeafCertDigest
%s: failed to parse payload content: %d
UID
failed to copy keys
Lock Customer Info Zone succeeded
/MobileDevice/ProvisioningProfiles
000B
Failed command
w
AMFDRDecodeIterateCertChainNext failed for leaf cert 0x%016llX
getPermanentKey: err is %d, supportedModule = %x
-[Ace2ARUProvController programAllKeys:]
%s: failed to init sequence
%s: missing IM4C leaf public key OID
options is NULL
The following data classes failed to migrate: %@
===== remote cert not equal to the cert inside mogul chip =====
ARUGenerateMcrt
Failed write command
can't get the lock status
Failed to get C string from OID: %@
aries
P1 - Tried to move %d - failed retval = %d\n
invalid oid sub-identifier %s
Failed to create base fusingInput
ARUPEDVerifyTagData
start to generate dummy pearl data
otpvKey is Null
chipID is NULL
UniqueDeviceID
AppleARMIICDevice
value is not in CFDataRef
x-fdr-attestation
ARUFDRToolsStringToTag failed to convert data class to tag
pedOptions is NULL
mergedDict is empty
failed to create dakContext for dak certification
Memory zone %d is locked
libCyrusFDR_cert_collect fail: %d
osk pub
%s: malformed im4c tag length: %lu
%s: data is unwrapped
Bad parameters --ctx
outSignature is NULL
TrustedSubmission
(outData->attestationLength > 0) && (outData->attestationLength <= (16 * 1024))
_Bool sysConfig3AddPayloadEntry(struct __SysConfig3 *__single, struct __SysConfig3PayloadEntry *__single)
BMU2,UniqueID
1.2.840.113635.100.6.71.2
ARUEANIsEANSupported
IDSN
xpc copySsoTicket error code is %d
apticketPath is NULL
%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n
%s: malformed attribute: %d
ARUFDRUploadDict failed
failed to create iCheck marker for %@
failed to get public key (%d): 0x%08x
apticket is NULL
SikDataClasses
_AMFDRDecodeMultiSealingResposeRecords
char *__single __terminated_by(0)_allocAndCopyString(const char *__single __terminated_by(0), size_t)
AMFDRSealingMapPopulateSealingManifest failed
Lynx FDR upload successfully
000T
DataStore
SIGALRM
_AMFDRDecodeVerifyTrustObject
0010
Data length is 0
Request factory cert(task = %d) failed
kAppleNVMeIsEANFormatted return isFormatted = 0x%x
unable to get device info\n
derCertArray is invalid
/Library/MobileContainerManager
%s: fdrDecode->dataImg4.payload_hashed is false
_copyIORegistryServiceProperty
000C
_AMFDRSupportBase64Encode failed
Invalid UID data size: %ld
CHIPID
------- SERVER RESPONSE -------\n%.*s------- END SERVER RESPONSE -------\n
-[ARUService executeARUTask:withOptions:getReply:]_block_invoke
%s: PKI: verify cert was issued by trusted key %d (success)
Savage,UID
AMFDRCertificateSigningRequest() failed: %@
_ARUCreateCStr failed to create cstring from destinationPath
0001957
ARUFDRSetDAKCertsInternal
hasFausInNewTicket = %d
%s:%spid:%d,%s:%s%s%s%s%s%u:%s %s%s%s[%04zu,%04zu): %s%s%s%s\n
_AMFDRDecodeVerifySealingManifestInternal
%s: Skipping revocation check (trustobject unset)
SIGUSR2
xpcProxy receive error %@
RequireMFiAuth
TrustObjectDigest
failed to add csr version
Native
verificationwithInfo end\n
Failed to malloc oidBuf for %@
permStr is NULL
ARUFDRRequestMFiCert
Failed to read nvm 0x%04X
REQUIRE_func
%s: can't parse FDR Trust Object SslRoot
%s: publicKeyParam is NULL
Thread %d:\n
failed to validate %@ with ucrt root, aksError: 0x%x. trying to validate with scrt
/Library/DeviceRegistry.dontBackUp
JasmineIR1,ECID
DCRT-X
outCsrFormat is NULL
%s: No restitch manifest, but allow unsealed, try to proceed with the data manifest...
posix_spawn %s success: %s
replySize <= sizeof(cmd_get_brunor_permanent_key_out_v1_t)
YonkersIR3
%s: can't parse FDR Trust Object trusted key: %d
%s: manifest or object property length does not match
@Timer6,Ticket
_ARUCreateCStr failed to create cstring from stage
aks_attest_context_get_sealed_hash
provisioningStatus
%s: unexpected property type != kImg4ObjectProperty
000K
startAuthentication failed
base64CsrSignature is NULL
x-fdr-minimal-seal-manifest-inst-prop
pkcs7Data is NULL
merge-fdrv3
%s: failed to parse sysconfig sequence: %d
BuildVersion
addLegacyDataClassForExport is NULL
_decodePrivateBody
executing %s
%s: validation failed for property 0x%llX
ARUVillanovaPerformInitialPreFusing
@USBPortController11,Ticket
AMSupportDigestSha256 failed
signDataWithBrunorPermanentKey: err is %d
.
ARUTristarReadProvisioningStatus failed
%s: can't parse sealing manifest top-level container
000g
_ARUFDRDumpNestedError
send cmd %x
ARUPrpcVillanovaAuthCertificationCreateSensorCtx
'%@' is not EAN data class
libCyrusFDR: ERROR: [%s:%u:%s] kAppleCyrusMLGetSN -> %x%s
RearCameraAuthICPubKey
ARUFDRCreateBrunorSignature
Efface Qi Zone succeeded
OTP key2 provisioning fail
EscrowPasscodePeriod
000p
entering ARUFDRSetDAKCertsInternal
mergedDataClass is NULL or malformed
_AMFDRDecodeFilterDataInstanceCallback
apticket.der
???
000e
xpc addLegacyDataClassForExport error code is %d
No data received from server.
_ARUFDRCertificateOIDCheckSingle
request digest
converted mfiProductPlanUID is too long
US
reqSkeyEncodedData is Null
ARUUtilsParseCertExtension
Unable to decode manifest with error %d
invalid count of data class array
Not all keys in 0Cfg were sealed
No crash thread from context
ARUPEDVerifyTicket failed
ProvisionAce2ServerURL
failed to populate sealingManifest
outDigests is NULL
/Library/DeviceRegistry.state
%s: malformed FDR Combined Format (trustObject), expected tag %c%c%c%c found tag %c%c%c%c
Cannot verify that all subCC values are present for %@-%@.
SIGQUIT
outPreFusingOutput is NULL
SkipFGSN is %@, VerifyOnly is %@ !
CertifyNoClientID
-[ARUService executeARUTask:withOptions:getReply:]
systemRootPath
/logs/AppleSupport
Savage
PEid
Mimosa,ECID
Successfully migrated data classes: %@\nand data classes using SIK: %@
SIGUSR1
%s: malformed FDR Trust Object trusted key, invalid trusted key tag length
RearCameraAuthICNonce
ARUVillanovaPerformProvisioningFusing
CFDictionaryCreateMutableCopy failed for %@
eidValue
Tag is not a string
failed to allocate missingDataClassesInstances
failed to create maxAttempt number
_copySoCChipIdEcidData
ARUFDRMultiClaimAndDownload
Failed to convert chipId
arm_thread_set_registers
ARUTristarChallengeVerify failed at slot %d
%s: failed to find object properties
socksHost is set, disableReverseProxy is automatically set to true
aks_attest_context_get
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEK failed with 0x%x%s\n
/Library/mad
aks_kext_set_options
%s: _AMFDRDecodeMultiSealingResposeRecords failed with error 0x%llX
%s: failed to begin decoding trusted key
%s: PKI: verify cert was issued by trusted root %d failed with error 0x%016llX
...Unable to open IO connection.  err = 0x%X, %s
error code is %d !!
found mogul I2C service
provision return %@
provision failed
PEidAllowMissingData
xpc copyProvisioningData error code is %d
AMFDRDataCopy return NULL data
TcrtCertifyURL
signedRefFramesInfoRecordData
https://gs.apple.com:443
asidMetadata
x86
SanityCheck
can't decode private data\n
%s: unexepcted items in offline blob
0003
failed to allocate dictValuesBuffer
===== local cert equal to the cert inside mogul chip(digest not compared) =====
invalid cstring path
%s: MultiCombinedItem malformed for multi combined data
000A
AMSupportBase64Encode dataRef returned %d
PSD2
%s: No SCDG in manifest, subCC digest missing
x-fdr-RemotePolicyExtension
CFDataCreateWithBytesNoCopy return NULL
response data= %x is wrong
version is NULL
failed to set aks option: 0x%08x
derCertArray is NULL
WIFI_MAC2
SIGINT
Ticket
@PCON1,Ticket
ARUParseDERLengthFromBuffer
chipID has wrong type: %@
000y
Cryptor Create Failed\n
EnforceDigestCheck
%s: Img4DecodeEvaluateObjectProperties failed
property %@ cannot be found
jCfg
_ARUCreateCStr failed to create cstring from systemDataStorePath
%s Unsupported sysconfig version: 0x%X
CFDictionaryCreateMutable failed for pedRequest
Verification failed !!verifyKey from ace2 is data=%@ len=%d
CaUrl
000m
could get manifest property ECID
%s: AMFDRDecodeIterateProducerIDBegin failed with error 0x%016llX
ChipID ECID inside mogul match to the SoC, no need more certification
+[NSString(MGExtra) stringFromMG:]
%s: metadataRecordCallback failed with error 0x%llX
Lock Esm Status Already Locked
Found local seal file in file system, that means sealing was successful
Binary Images:\n
_AMFDRDecodeVerifySealingRequestInternal
_AMFDRDecodeVerifyChainOffline
PED,ChipID
dataInstances is NULL
Failed to obtain a data instance
_AMFDRDecodeCombined
isMogulService
return data is NULL
/Documents/Pearl
libCyrusFDR.c
Unable to decode DER data \n
write-ean
struct __SysConfig3 *__singleallocSysConfig3WithHMACKey(SysConfig3Magic, SysConfig3Version, SysConfigData)
ARUPEDRequestSendSync failed!
000G
0017
AMFDRDataCopy failed, ignoring verification failure.
ExtraSslRoots
Cannot create mogul service context
requestKey is NULL
CFDataCreate failed
MultiRequestMaxAttempts
iCheck marker url is NULL
can't write data to challenge data address
%s:\n\tNum files:\t%u,\n\tNum hardlinks:\t%u,\n\tNum compressed:\t%u,\n\tTotal Size:\t%lld,\n\tMin File Size:\t%lld,\n\tMax File Size:\t%lld,\n
ngidDEBuffer
malformed kAMFDRCertifyComponentAttributeBatteryVersion, batteryVersion = %@, batteryVersionValue = 0x%llx
Error is empty
/mnt1
-[Ace2ARUProvController verifyByChallenge:verifies:inDict:forSlot:]
/Library/MobileInstallation
replySize == sizeof(outData)
%s: malformed FDR Trust Object Format
AMFDRDecodeCombined
challenge is nil
correct key read, expecting 0x%04X, get 0x%02X%02X
_securityd
%s: uniqueIDInfo.content.length != uniqueIDLength
%s: signature must be non NULL and publicKeyLsignatureLengthength must be non 0
macType is invalid: %@
com.apple.ARUService.sealingMetadataUpdate
addStringMetadataIntoSysConfig
AMFDRDecodeCertificate
%s: unexpected tag 0x%llX in certificate properties
%s: PKI: verify cert %d was issued by %d (success)
returnData is NULL
pubKeyDigest is NULL
Tag was not the expected metadata tag %llX
%s sysconfig metadata entry must have EITHER string OR data fields populated!
ExtraSslRoot
/Library/DataAccess
application/x-www-form-urlencoded
prepare
ARUPEDConfigurePEDAMAI failed
CertifyBase64
-l 0xFFFFFFFF -v 99
value is not in MAC type
refFileName
%s: failed to find corresponding component type
%s: malformed FDR Combined Format (trustObject)
instance is NULL
dictToMerge is NULL
Don't need to generate 0Cfg now, but will save content from 0Cfg to manifest after FDR sealing
aneMapFunction:\t\t%s\n
00005066
ARUVillanovaCreateAuthCertificationDict failed
0011
invalid multiLynx actual count: %d vs maximum count: %d
CertifyPartNumber
AMFDRDataCopy failed
%@
AuthDbg,ECID
B64_BB_CHIPID
kAMFDROptionOfflineSigning
dcrt
%@ local get from device data store failed
Both provisioningData and originalAppvData are NULL, Skipping appv submission
_networkd
'%@' is not supported
===== local cert equal to remote cert =====
AppleKeyStoreTest
@CameraAP1,Ticket
AMFDRDataMultiCopy failed with unknown error
copyIDSNFromMogulService
_parseEchoResponse
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapEK failed with 0x%x%s\n
libCyrusFDR: ERROR: [%s:%u:%s] unexpected length of lynx-count: %u%s
%s: Img4DecodeGetPropertyData(kFDRTag_clas) failed.
%s: Re-evaluation returned code=0x%016llX
PED,SecureStorageSCFDigest
AMFDRDecodeIterateSysconfigBegin
%s: FDR Sealing Request failed to decode img4
%s: decoded IM4C signature OID is empty
RearCameraAuthICPubKeyHmac
CFURLCreateWithString failed for %@
Timer,ECID,7
failed to complete CSR against server
Golay,ECID
ARUFDRUploadDict
aks_fv_new_vek
ARUPEDCreateAuthInstallRequest failed
can't parse subItemInfo sequence
malformed tbs %d
failed to calloc write command
/db
can't allocate memory for localData
failed to copy provisioning data
%s: Inner DER did not terminate properly.
000i
ARUAppvUpload
AMFDRDecodeTrustObject
%s: cannot decode to a multicombined data, proceed with combined format
%s: AMFDRDecodeVerifySealingManifest 0x%016llX
%s: propertyValue must be non NULL with a non-zero length (length=%u)
Timer,ECID,10
UDID
ARUMogulChallengeCheck
set target fail
missingKeyCFNum is NULL
can't parse mDecryptionBody sequence
set %@ with metaDataDict:%@
certLength is wrong
WrapPearlDataOptions
mdak
%s: malformed FDR Multi-Response Error Format
ARUFDRDownloadManifestForProperties
euiccSignature
xpcProxy is NULL
Ace2HPMInterface is nil
%s: propertyLength != implementation->digestInfo->digestOutputSize
Didn't copy IDSN from IOService, currently not fatal
report_crash
McrtLockqQi
%s: failed to decode payload: 0x%llx!
2.5.4.10
AppleRestoreUtils-??
certName is NULL
/Library/Passes
circular_queue_init
_AMFDRDecodeVerifySubCC
@Polaris,UniversalTicket
000h
%@ verification did not pass, skipping iCheck marker
failed to get euicceumCertificate
can't get Mogul signature, retVal: %x
ARUServiceMsgCopyRefKeyPubKeyAndAttestation
_Bool sysConfig3ManifestGetPayloadHMAC(struct __SysConfig3ManifestEntry *__single, SysConfigData *__single)
Can't allocate memeory for decryption body 
marker data is NULL
ARUMogulEffaceAndLockMemoryZones
%@-%@ is uploaded successfully, enforceDigestCheck = %d
buffer is null
DataClass
CameraISP1,ECID
LYNX
/Library/ManagedAssets
permissions is NULL
cannot execute AID command, retVal: %x
Watch MLB
wrote cert digest (%d bytes) to mogul memory zone
ARUUtilsParseCertExtensionField failed, error = 0x%llx
ARUTristarGetESN
%@, FDR Data does not match in download data
outVerifyKey verifiy return nil \n
%s: failed to find subCC digest
failed to create eUiccRawCert
Lock Apple Zone failed!!
SIGPROF
/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/PearlSupport/PearlSupportUtils.m
%s hmac is NULL
Start claim
appv data creation failed
_createFCfgDataBlob
_AMFDRDecodeVerifyMultiCombinedDataInternal
failed to create device info dictionary
sessDataRef is Null
converted mfiProperty is too long
failed to get sealing manifest properties for sysconfig, %@
_ARUWrite0CfgToEAN
ARUApticketHasEntitlement
failed to chown path as mobile
can't get write component properties to Area51
Invalid HMAC key. sysconfig->hmacKey.data = %p, sysconfig->hmacKey.length = %d. Did you register HMAC key?
USBPortController8,ECID
can't find OUName in subject
UploadTcrtOptions
aks_internal_state
%s: Invalid data digest input
PED,Nonce
euiccCertificate
failed to request %@
sendRequestSyncWithHeaders
decodePrivateBody allocation failed
AMFDRDecodeIterateTrustObjectRevokedBegin
AMFDRDecodeCheckProducerIDRevocation
_Bool sysConfig3CreateMetadataHMAC(struct __SysConfig3 *__single, SysConfigData *__single)
_AMFDRDecodeGetExpectedManifestHash
%s: Evaluation returned code=0x%016llX, re-evaluate with FDR 2.0 format
ChipID
BbSNUM
ARUFDRRequestFactoryCertIndividual task:%d failed but allow incomplete data is set in FDR option, continue...
/Library
@DMC,Ticket
getAttestationToCollectionKey: err is %d, supportedModule = %x
SEK
getAttestationToMDAK: err is %d
Invalid Arguments\n 
/Library/WebClips
mergedDict is NULL
Timer,ECID,11
failed to create marker for %@
csr does not have correct common name
can't write cmd to Area51 I2C register, err: 0x%x
outLength
Populate keyBuffer Failed
Efface USB Zone succeeded
SN
set %@ to main metadata dict
ctx cannot be NULL
Verifiy function return error %d\n
rawLeafCert->length %u larger than bufferLength %u
unsupported action!
failed to write restore bag to disk %s\n
%s: cannot find subCC digest for %u
%s: found data in multi combined format
failed to encode sysconfig, error: %@
ARUServiceMsgSendMultiSealingMetadata
SOCKSPort
McrtSkipCheckChipIdEcid
001c
DEREncoderCreateEncodedBuffer failed
generate dummy pearl data
Watch
device CHIPID is nil
/logs/BurnIn
unmappedFromANE:\t%s\n
the error code is %d !!
--pair
Unsupported ARM state
sepClassFKey
/usr/local/bin/sysconfig
provisioningWithInfo start\n
/Library/FrontBoard
ARUPEidUpload
PCON3,ECID
partNum is NULL
ARUMogulCreateAttestationCertImplI2C
failed to download original eCfg data
@InductivePower1,Ticket
Mtp PrgCtrl Status Poll Failed
current_command: '%c%c%c%c'
keys are NULL
Did not get the new AP ticket from restored
AMFDRDecodeTrustEvaluation
%s: AMFDRDecodeCheckProducerIDRevocation failed with error 0x%016llX
_AMFDRDecodeTolerateErrorsForOptions
_openIoService
ARUMogulServiceIteratorBeginWithMogulType
decode vNonce is nil
ARUTristarProvision failed
failed to validate %@ with scrt, aksError: 0x%x, but sepAttestQA enabled, validation failure is allowed
can't get attestation cert, retVal: %x
not PKCS7 signed data! \n
%s was terminated by signal %d
%s: AMSupportDigestSha256 failed
%s: unexpected signed section tag: 0x%llx
villanova
CertifySaltAttestationSignature
dataClassToClaim is NULL
/Library/Carrier Bundles
%s source string was NULL
_ARUEANReadImage
eCfg
libCyrusFDR: success%s
%@/FactoryData/System/Library/Caches/com.apple.factorydata/%@
Thread %d Crashed:\n
__TEXT
libCyrusFDR: ERROR: [%s:%u:%s] kAppleCyrusMLGetPub -> %x%s
%s: subCC digest mismatch
Failed to efface zone
SysCfg tags for this product: %@
Failed to copy FDR data
%s/mobile
%s: sysconfig version not supported: 0x%x
SavageCamInterfaceSensorFusing failed with error: 0x%x
malloc decryptionKey fail \n
1.2.840.113635.100.11.3
Reference frame (set=%d, frame=%d, size=%d, type=%d, temp=%f) written to %s\n
mappedToANE:\t\t%s\n
MLBSerialNumber
ARUPrpcAuthCertificationCreateSensorCtx
%s: Invalid data digest length: %ld
%s: malformed FDR Combined Format, expected tag %c%c%c%c found tag %c%c%c%c
_provDerDecode
CertifyCustomCommonName
SIGURG
%s: unsupported signature length: %lu
RTMU1,ECID
Get the flag number is : %@ \n
inboxsu
failed to allocate rawEncoder
SIGTTOU
%s: malformed FDR Trust Object Revoked, invalid trusted tag length
%s: %s: signature validation failed
%s: evaluateCertificateProperties failed
testDummyDataInstance is NULL
cCfg
ace2HPMReadForAddress %d read error
objectFound:\t\t%s\n
_AMFDRDecodeVerifySealingManifestCallback
Acdcuc5,ECID
CameraAP4,ECID
-[ARUProvSequencer verificationwithInfo:treekoManager:]
Savage - Factory
AMSupportBase64Encode sessDataRef returned %d
failed to query build version
failed to encode MFI Accessory Data
output FDR data length is %d
AID service currently only supported on Mogul
1.2.840.113549.1.7.1
UniqueChipID
000R
ComponentAttributeDict
decodeCertData
can't check authentication
%s: malformed im4c tag: %c%c%c%c
IODeviceTree:/defaults
ARUMogulServiceIteratorNext
Invalid mogulIOServiceTypeImplMapIndex
can't allocate memory for idsn
%s:%spid:%d,%s:%s%s%s%s%s%u:%s failed REQUIRE condition (%s:%d)\n%s\n
%s: AMFDRDecodeIterateProducerIDNext(first) failed with error 0x%016llX
%s: failed to find MANB (manifest body) tag
sik-
Not in restoreOS
AMFDRSealingMapCopyMinimalManifestDataInstancesWithAttribute failed, %@
requested fcrt is NULL
memcmp skey hash fail \n
failed to get lynx serial number
Failed to create mogul service
mfi
_ARUShouldSkipGenerateSyscfgData
_AMFDRDecodeSearchEntryFromPropertyList
 deleted
chipIDData has wrong type: %@
No expected value is cached by key=%@
libCyrusFDR_test_delete
failed to create default FDRContext for lynx submission
failed to allocate sigOidSequenceEncoder
path
AMFDRDecodeVerifyTestStationManifest
ARUSensorAuthCertificationCopyCameraIORegValue
tmpProperties is NULL
CoreSymbolication framework is not available
\n
StripImg4
@USBPortController9,Ticket
propertyData is NULL
lockStatus is NULL
Lock Customer ID Zone succeeded
ProvisionAce2Options
TrustObjectURL
Failed to init mogulServiceIterator
/networkd
/Library/DoNotDisturb
%s: outRawData must be non NULL and outRawDataLength must be non 0
sealDataInstance is NULL
Task: %d, fetching %d cert got error
ARUEANIsEANFormatted
Trying service = 0x%X...
-[ARUTreeckoManager decodeProvisioningData:]
/Library/CallHistoryDB
urlSessReqEncodeData is Null
%s: malformed DERFDRItem, invalid tag length
%s: not verifying subCC payload, skip checking subCC digest
sealDataClassInstance create failed
MFiAccessoryData
%s: fdrDecode->uniqueID is NULL or 0 size
sourceDSURL is not a string
can't verify cert chain
_addMacEntryIntoSysConfig
Nothing to update, Skipping appv/eCfg submission
inTags is NULL
AMFDRDataCopySealingManifestProperty failed
dataClassSet is NULL
ARUFDRUpload failed for %@
outProperties is NULL
New Product Experience Attestation
key %d is not a string
failed to create entry for OID %@
No I2C callback specified
Translated
%s: uniqueID is not specified, which is allowed, skip uniqueID mismatch errors
_AMFDRDecodeFindDataFromMultiCombined
PED,ECID
value is NULL
AMSupportHttpUriEscapeString base64SkeyStr returned %d
failed to convert to DER format
McrtIsAce3
%s: can't parse sealing manifest top-level container. Expected tag %llu, found %llu
%s sysconfig version (0X%08X) did not match manifest version (0X%08X
ean-storage-present
aks_get_convenience_bio_state
Failed to create camChannelNum
@PCON4,Ticket
failed to add %s into context
/Library/CoreFollowUp
%s: malformed FDR2 Format, invalid tag length
validate %@ pass
com.apple.pearld.ready
%s: failed to parse signed section sequence: %d
ssoData is NULL
2.5.4.8
failedToMigrate is NULL
AMFDRSupportBase64Encode eUICCString failed
Reference frames info record written to %s\n
savageFWCert && savageFWCertLength
%s: ctx must be non NULL
%s: manifest or object missing required property '%c%c%c%c'
SCfT
pub key length mismatch, cert : %lu, der : %lu
--destinationFDRPath
failed to open userclient via %s: %d\n
ARUServiceMsgSendFdrStatistics
%s data and string are mutually exclusive
AMFDRSupportBase64Encode failed
Failed to get thread state: %d(%s)
FA
could not parse manifest
AddLegacyDataForExportAfterUpload
@AudioAP1,Ticket
@CameraAP4,Ticket
SOCKSHost
_Bool sysConfig3CreatePayloadHMAC(struct __SysConfig3 *__single, SysConfigData *__single)
@AuthDbg,Ticket
EUICCCSN
failed to add %s
otpcKey is Null
no apTicket in options
DataVersion
failed to decode public key: 0x%016llX
akstest_unwrap_ek
510
%s Invalid HAMC key. sysconfig->hmacKey.data = %p, sysconfig->hmacKey.length = %u
@Timer8,Ticket
AMFDRDecodePublicKey
DERReturn _DERDecodeSysConfig3ParseAndPopulateMetadataSequence(DERDecodedInfo *__single, _Bool *__single, void *__single)
encodeSubccData failed: %u
ARUTristarLock
AMFDRDataPut failed
failed to create directory for %@
The product doesn't support EAN
%s service not found!
Failed to get localCert: %@
parent is NULL
ARUFDRToolsWrapPearlData
ESN buffer is NULL
Not Pass PrgMtp Bit Clear Failed
failed to append GET permission
libCyrusFDR: entered lynx_index_to_slave_pos%s
AMSupportHttpCopyProxySettings failed for %@
Mtp Init PrgCtrl Read Failed
AMFDRDataMultiCopy MultiRequest error, but no details error info.
Failed to get arm thread state: %d(%s)
Failed to write appv to EAN with error %d
Failed to query ChipID or UniqueChipID from device
provisioningAck start\n
provision-lth-key
*attestation
USBPortController10,ECID
_formatEcid
malformed dataClass
Brunor
Lock Customer ID Zone failed!!
Failed to create timeout\n
arm64
failed to download original appv data
PED,BoardID
encodeSubccData
STATUS is NULL\n
vcrt BatteryVersion
1.2.840.113635.100.8.4
restoreOptions is NULL
```
