# `/System/Library/PrivateFrameworks/AppleRestoreUtils.framework/AppleRestoreUtils`

From the upgrade restore ramdisk (141-29011-104.dmg). 366,544 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 3696)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/System/Library/PrivateFrameworks/AppleRestoreUtils.framework/AppleRestoreUtils (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (2 classes, 3 protocols)

Classes: `ARUListener`, `ARUListenerBase`

Protocols: `ARUListenerProtocol`, `ARUServiceProtocol`, `NSObject`

## Strings (827)

```
unexpected type existingUUIDs
FDRCAURL
_ARUConstructTaskOptions
'0
/Library/DataAccess
reply
replySize <= sizeof(reply)
_connect != ((io_object_t) 0)
EnableSsl
/vm
/Library/Caches
ARUExecuteTask_block_invoke
ProvisionAce2Options
/Library/NFStorage
DataDirectory
unmappedFromANE:\t%s\n
com.apple.ARUListener.aruCtx.update
MinimalManifestPropertyCheck
/Library/UserNotifications
outHostPubKeyLength && (*outHostPubKeyLength >= (448 / 8))
requesting setting digest of DataClass: %@
/Library/Preferences
added statistics to httpStatistics
value has wrong type %@
aruCtx or httpStatistics is NULL
B16@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8
CFDictionaryCreate failed for aruTaskOptions
aruTaskOptions=%@
ARUContextSetProvisioningData
prpc
/Library/VoiceServices
decryptedDataBuffer
dense
callback
mappedToSEP:\t\t%s\n
v16@?0@\"NSError\"8
MergeFDRv3Options
EnableRunTaskConcurrently
_ARUPreSDcrtActions
copyProvisioningData
-[ARUListenerBase sendMinimalManifestPropertyCheckTag:andResponse:]
%s: AMFDRCreateDataSignature return false\n
EnableVerboseLogging
/iomfb_bics_daemon
/root/Library/MobileContainerManager
GetCombined
aneUnmapFunction:\t%s\n
ARUGetRestoreContext
ProvisionTristar
sendTristarEsn return result is %d
_ARUContextCopyFormattingDescription
_ARUSetTaskOptions
/Library/Carrier Bundles
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestRewrapEK failed with 0x%x%s\n
user allow list:
%s: Loading PSPC from FDR.\n
replySize == sizeof(status)
aruTaskOptions is NULL
com.apple.AppleRestoreUtils.task.async
/Library/DeviceRegistry
kcvBuffer
signatureLength
/wireless
could not create file: %s (%s)\n
outDataSize <= signedRefFramesInfoRecordData.length
attestationLength
%s
task:%@ execute failed with error code=%d.
/Library/CoreBrightness
/Library/ManagedAssets
ReferenceFramesInfo setCount: %d\n
signature
-[ARUListenerBase addDataClassForClaim:withDataInstance:andReponse:]
outAttestation is null
outstatistics is NULL
FDRSetMultiSealingMetaData
ProvisionVillanovaOptions
v16@?0^{_ftsent=^{_ftsent}^{_ftsent}^{_ftsent}q^v**iiSSQiSsSSS^{stat}[1c]}8
Generating reference frames files...\n
pspc
CFArrayCreateMutable failed for pendingTaskTableNums/failedTasks
/Library/ApplePushService
service
connect
outLength
AuthInstallSigningServerURL
EnableMultiLynxUpload
/Library/Logs/CoreDuet
IOService:/IOResources/AppleKeyStore
ReferenceFramesSetInfo, index: %d, type: %d, count: %d, size: %d\n
digestData is NULL
AMFDRSetDigest _aruCtx->fdrHttp return failure.
copySsoTicket return result is %d
check-vcrt-boardid
dictKeysBuffer or dictValuesBuffer is NULL
mobile
%s:%spid:%d,%s:%s%s%s%s%s%u:%s version mismatch: %llu%s\n
aneMapFunction:\t\t%s\n
/Library/Accounts
Free Blocks:%lld blocks of size:%d\n
UploadTcrt
newTaskOptions is NULL
refFrameData
attestation && attestationLength
(outData->attestationLength > 0) && (outData->attestationLength <= (16 * 1024))
copySsoTicket is null
ARUExecuteTask_block_invoke_2
FDREnableSso
/Library/IdentityServices
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 3)%s\n
addDataClassForClaim return result is %d
UploadPEidSubCCData
ProvisionLTHKey
CLASS NONE
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEKWK failed with 0x%x%s\n
Adding property str: %@
ARUSetLogHandler_block_invoke_2
ProvisionLTHKeyOptions
Failed to get data protection class for given path %s with errno %s (%d)\n
savageFWCert && savageFWCertLength
StripImg4
(type == kPearlFactorySeaCookieValidateTatsuTicket) || replySize
PED
CFNumberCreate failed for taskIndex: %d
all tasks are completed, wrapping up
pre task:%@ execute failed.
(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || messageSize
/root/Library/Preferences
/Library/Backup
ARUExecuteTask
/Library/Assistant
aks_fv_new_kek
i
reference-%@__T_%@.bin
permanentKey
ARUSetLogHandler_block_invoke
PrintHttpStatistics
aks_fs_supports_enhanced_apfs
EnableSso
ExtraCertOptions
timeout waiting for aru async tasks execution
akstest_rewrap_ek
replySize >= sizeof(*outData)
statistics is null
CertifySEK
RestoreOptions
not enable in PR option, skip task:%@
/backup
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unpack data failed%s\n
%s: Successfully got provisioning data.\n
_aruCtx->fdrHttp is NULL
CreateFactorySDcrt
ARUEnforceDigestCheck
/Library/Calendar
ARUContextSetTrustObjectData
daks
WrapPearlDataOptions
failed to convert currentTaskNum: %@ to an int
/Library/mad/activation_records
/Library/MobileBluetooth
fdrInput
size == sizeof(response)
prepareFDRDataEncryptionKey returen status is %d
/Library/SyncedPreferences
/Library/ConfigurationProfiles
akstest_new_ekwk
prf1Class && (prf1ClassSize > 0)
path
ARUListener
_ARUListenerCreateSignatureForPayload
Reference frames info record written to %s\n
outPolicy is null
set multiSealingMetadata to fdrHttp/fdrLocal
CLASS B
\tSize Distribution:
%s: PSPC data loaded to SEP.\n
signatureLen is 0\n
com.apple.ARUListener.sendFdrStatistics.serial.update
RunTaskConcurrently
/MobileDevice/ProvisioningProfiles
/Library/mad
outNGIDDELength && (*outNGIDDELength >= 16)
fdrLocal or fdrHttp is NULL
Connection to %@ invalidated, reason: %s
FDRTrustObjectURL
ARU CHECKPOINT START: %@
/run
/db/com.apple.xpc.launchd
/Library/NanoBackup
Generating reference frames info record...\n
AMFDRSetDigest _aruCtx->fdrLocal return failure.
FDRDataStoreURL
FDRExtraSslRoot
Dcrt failed to bump DAK: 0x%08x\n
/Library/CoreDuet
*attestation
/Library/Logs
/Library/Mail
CFArrayCreateMutable returned exportDataClasses is NULL
UploadTcrtOptions
%s: mode=%o, u/g=%i:%i class=%i%s\n
sparseLP
outPSD3Length
att
ARUAllowCertificateValidationFailed
/Managed Preferences/mobile
/Library/BackBoard
/Library/WebClips
mcrt
leftover task: %@ dispatched
/mobile
/Media/Downloads
ReferenceFramesSetInfo, index: %zu, type: %d, count: %d, size: %d\n
(type == kPearlFactorySeaCookieValidateTatsuTicket) || reply
-[ARUListenerBase createSignatureForPayload:andGetResponse:]
AuthInstallEnableSso
-[ARUListenerBase sendFdrStatistics:andResponse:]
MultiSealingMetadata
/db
akstest_last_user
 (skip)
%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n
Library-PearlFactory
tsid
AMFDRDataSetSealingPropertiesOverride fdrRemote return failure.
newSubCCdata is NULL
UploadWcrt
create-fdr-iCheck-markers
taskOptionKey is NULL
:
systemRootPath
ARUContextSetCallbackContext
UploadMcrt
aks_get_internal_info_for_key
ispMapFunction:\t\t%s\n
PSD2Length
UploadPEidOptions
CreateFactoryWiFiCertificate
outPolicy return result is %d
pspcData
ApplePearlSEPDriver
ARUCopyHttpStatistics
data
denseLP
prepareFDRDataEncryptionKey failed and erorr code is %d
CheckVcrtBoardID
ARUExtraCertOptions
/Library/Fonts
EscrowPasscodePeriod
%lld,%d\n
FDREnableMultiRequest
tristar-provision
aks_fv_rewrap_kek
aks_fv_unwrap_vek_with_acm
mappedToANE:\t\t%s\n
/networkd
/Library/CoreFollowUp
requestData
mappedToISP:\t\t%s\n
%s: fdrRemote is NULL\n
_ARUListenerAddOverrideProperties
/log
/Library/CallHistoryDB
ARUCreateContext
taskOptions is NULL
__thr_ARURunTaskConcurrently_block_invoke
/.overprovisioning_file
aks_internal_state
IOService:/IOResources/AppleKeyStoreTest
err == 0 
ARUSetCreateSsoServiceTicketCallback
TrustObjectData
ARUEnableMultiLynxUpload
-[ARUListenerBase sendTristarEsn:andResponse:]
aks-client-queue
ReferenceFramesPath: %s\n
objectSize:\t\t%d\n
CFArrayCreateMutable returned claimDataClasses is NULL
ARUContextSetPEidSubCCData
CaUrl
/Containers
%s:\n\tNum files:\t%u,\n\tNum hardlinks:\t%u,\n\tNum compressed:\t%u,\n\tTotal Size:\t%lld,\n\tMin File Size:\t%lld,\n\tMax File Size:\t%lld,\n
pearldReady
ispUnmapFunction:\t%s\n
ARUForceTrustedSubmission
task is NULL
wheel
%s%s
savageUID
clearBuffer
v8@?0
-[ARUListenerBase addLegacyDataClassForExport:andResponse:]
/Library/MedicalID
 dir: %s %i\n
dataLength
com.apple.BiometricKit
fdrRemote is NULL
requesting adding DataClass: %@
FDRPrintHttpStatistics
_ARUPostSDcrtActions
/root/Library/Caches
/Library/Logs/AppleSupport
/Library/adi
Reference frame (set=%d, frame=%d, size=%d, type=%d, temp=%f) written to %s\n
ARUContextSetLocalFDR
/Library/AggregateDictionary
__thr_ARUListenerAddStatistic
signature is NULL\n
AMFDRDataSetSealingPropertiesOverride fdrLocal return failure.
/.exclave
replySize <= sizeof(cmd_get_brunor_permanent_key_out_v1_t)
PSD2
-[ARUListenerBase copyRefKeyPubKeyAndAttestation:]
aruCtx is NULL
AllowCertificateValidationFailed
/root
/Library/CrashReporter
/Library/NanoTimeKit
%@ combinedTaskOptions is NULL
option '%s' has non-boolean value, using default\n
com.apple.pearld.check_secure_streaming
unmappedFromSEP:\t%s\n
CreateFactoryDcrt
ARUAllowMissingSyscfgData
_networkd
/Library/SMS
akstest_check_class
_aruCtx->fdrLocal is NULL
dispatch_semaphore_create failed
/log/com.apple.xpc.launchd
%i
dictFileName
hostPubKeyBuffer
%s: PSPC data found.\n
ARUContextSetApTicket
ARUExecuteInitTasks
IODeviceTree:/filesystems
failed to open userclient via %s: %d\n
%@/reference-%@.plist
not erase install, skip task:%@
dataInfo->setCount > 0
errorCode
/.ssh
/Library/AddressBook
<user>
refFileName
encryptedBuffer
ProvisionTristarOptions
_ARURunTaskConcurrently
com.apple.AppleRestoreUtils.task.serial.update
replySize <= (16 * 1024)
sek
aks_fv_set_protection
%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n
/Library
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewKey failed with 0x%x%s\n
calibration && (calibrationSize > 0)
outRequestCert is null
CreateFactoryMFiCertificates
MergeFDRv3
/Managed Preferences
ngidDEBuffer
failed to commit Sep SDAK: 0x%08x\n
esnData is NULL
ped
FDRDisableSSLValidation
ARU CHECKPOINT END: %@
/.fseventsd
/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m
/System/Library/Pearl/ReferenceFrames
PEid
restoreOptions is NULL
%s:%spid:%d,%s:%s%s%s%s%s%u:%s unexpected output count %u (expected: 1)%s\n
/System/Library/Caches/com.apple.factorydata
UUID
%s: payload is NULL\n
/Library/CountryBundles
%s%s\n
ApplePearlExclaveSEPDriver
-[ARUListenerBase copyRestoreLocalPolicy:]
factory-wificrt
aruCtx->aruTaskOptions is NULL
failed to commit DAK: 0x%08x\n
CLASS D
set provision data successfully
Can't create mutable httpStatistics 
pubKey is NULL\n
/root/Library
signedRefFramesInfoRecordData
CreateFactorySUCertificate
_wireless
EscrowTokenPeriod
provisioningStatus
ARUExecuteTasksInternal
outConnect
*outLength >= minimalOutputBufferLength
Verifying new reference frames info record...\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapEK failed with 0x%x%s\n
WrapPearlData
copySignProvisioningRequest return result is %d
_ARUListenerAddDataClassForClaim
aru_get_boolean_option
outKCVLength && (*outKCVLength >= 3)
/Library/Logs/CrashReporter
/Library/BulletinBoard
/Library/DoNotDisturb
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestCheckClass failed with 0x%x%s\n
dataInstance is NULL
unexpected type statistic
UploadPrpc
/Library/MobileInstallation
ARUContext
TrustObjectURL
/preferences
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestUnwrapKey failed with 0x%x%s\n
aks_get_convenience_bio_state
dataInfo
ARUSetLogHandler
tcrt
wcrt
/Library/TCC
/Media
_aruCtx is null
/installd
/Library/DeviceRegistry.state
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestNewEK failed with 0x%x%s\n
%s:%spid:%d,%s:%s%s%s%s%s%u:%s kAKSTestLastUser failed with 0x%x%s\n
%s/%@
/Library/NanoPreferencesSync
/Library/terminus
-apfs_shared_datavolume
sdcrt
/Library/DeviceRegistry.dontBackUp
/Library/Trial
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n
FormatDR
PSD3
-[ARUListenerBase sendLog:withReply:]
AMFDRDataAddLegacyDataClassesToExport return error
UploadPrpcOptions
UploadWcrtOptions
DsUrl
ARUVerboseLogging
/keybags
/Applications
_ARUListenerAddLegacyDataClassForExport
ProvisionVillanova
ARURestoreOptions
failed to allocate processedTasks
aks_kext_set_options
akstest_unwrap_ek
refFrame
addLegacyDataClassForExport return result is %d
merge-fdrv3
aks
/Documents/Pearl
savagePubKey
getSavageProvisioningData
PEDOptions
_ARUSetTaskOptionsFromRestoreOptions
/Media/iTunes_Control
kern.bootargs
Log connection to %@ invalidated, reason: %s
CreateFDRiCheckMarkers
could not open file: %s (%s)\n
Results of Allocation and Mapping Object Scheme3 Context1:\n
replySize == sizeof(*outData)
fdrRemote or fdrLocal is NULL
com.apple.ARUService
ARUContextSetRemoteFDR
/protected/trustd
ARUAddLegacyDataForExportAfterUpload
/MobileAsset
shared allow list:
_merge_dict_cb
cmd
VerifyData
dataClass is NULL
Failed to get log xpc proxy with error: %@
/Keychains
objectFound:\t\t%s\n
-[ARUListenerBase copyProvisioningData:]
Can't generate propertyStr
ret > 0 && ret < sizeof(tempChar)
tempString
%s:%spid:%d,%s:%s%s%s%s%s%u:%s aks connection failed%s\n
/Library/Passes
/Library/FrontBoard
%s/mobile
serviceName
unmappedFromISP:\t%s\n
APTicketData
/Library/ISP
collectionKeyLength
/containers
__os_warn_unused(__builtin_add_overflow((dataLength), (2 * 16 + __builtin_offsetof(psd2_encrypted_t, encryptedData)), (&minimalOutputBufferLength))) == 0 
_ARUListenerCopyRefKeyPublicKeyAndAttest return result is %d
outPublicKey is null
v16@?0@\"NSDictionary\"8
EnforceDigestCheck
CLASS C
(*outLength > 0) && (*outLength >= dataLength)
setDictionary
Reference set dictionary written to %s\n
ProvisionAce2
mfi
TrustedSubmission
/Library/ControlCenter
akstest_new_key
fileURL
inData
permanentKeyLength
IsPearlKeyReady
AuthInstallProvisioningServerURL
_ARUPreDcrtActions
SDcrt failed to bump Sep SDAK: 0x%08x\n
/Library/Cookies
aks_fv_new_vek
%s:%spid:%d,%s:%s%s%s%s%s%u:%s ioreg: %d, boot_arg: %d%s\n
-[ARUListenerBase sendMultiSealingMetadata:andResponse:]
provision-lth-key
pdak && pdakLength
sema
%s: CFDataCreate signature data return NULL\n
su
post task:%@ execute failed.
/Library/Voicemail
CLASS A
pathString
_ARUListenerCopyRefKeyPubKeyAndAttestation
/MobileSoftwareUpdate
/Library/MediaStream
outDataLength
UploadMcrtOptions
/Library/SoftwareUpdate
file: %s %i\n
dvaOffset:\t\t0x%X\n
PSD3MACLength == (16)
-[ARUListenerBase copySsoTicket:]
/Library/Keyboard
Can't allocate overrideProporties dict!!
/Library/SpringBoard
aks_delete_xart_leak
%s:%spid:%d,%s:%s%s%s%s%s%u:%s options value 0x%llx exceeds uint32_t%s\n
outResult
replySize == sizeof(cmd_get_brunor_collection_key_out_v1_t)
attestation
/logs/AppleSupport
/root/Library/Lockdown
/Library/MobileContainerManager
failed to write restore bag to disk %s\n
akstest_new_ek
encryptedDataBuffer
outSso is null
set minimalManifestPropertyCheckTag to fdrHttp/fdrLocal
%s: fdrHttp is NULL\n
ARUCreateContext failed
ace2-provision
villanova-provision
ExtraSslRoot
_ARUPostDcrtActions
attestation is NULL\n
dataLength > 0
notifyResult == 0
(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || message
AMFDRDataSetDataClassesToClaim return error
null XPC connection
copyRestoreLocalPolicy is null
logStr is NULL
decode_pfk_bulk_data
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n
%@/%@
*signature
type is NULL
IsInRestoreOS
AddLegacyDataForExportAfterUpload
<var>
%.6f
replySize >= sizeof(cmd_alloc_map_s3c1_out_v1_t)
/root/Library/Logs
/logs/BurnIn
AppleKeyStore
outSignature is null
Failed to create ARUContext
_aks_operation
root
/Library/UserConfigurationProfiles
%i,%u,%u,%u,%lld,%lld,%lld,
e-apfs
%s: outRequestCert is NULL\n
ARUContextSetRestoreOptions
EnableMultiRequest
/tmp
daemon
failed to open connection to %s: %d\n
decode_pfk_bulk_entry
collectionKey
Log connection to %@ interrupted
aks_kext_get_options
aks_run_internal_test
-[ARUListenerBase setDigest:withDataInstance:Digest:andReponse:]
key has wrong type %@
_ARURunTaskConcurrently_block_invoke
_securityd
akstest_unwrap_key
%s:%spid:%d,%s:%s%s%s%s%s%u:%s count %llu exceeds max %u%s\n
dataInfo->setCount <= (4)
reference-info-record.DAT
/logs
sparse
dcrt
AppleKeyStoreTest
stat failed: %s\n
/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/PearlSupport/PearlSupportUtils.m
v12@?0i8
ARUSetCreateLocalPolicyCallback
wrap-pearl-data
Connection to %@ interrupted
Failed to get xpc proxy with error: %@
UploadPEid
_ARURunTask
refPath
replySize == sizeof(outData)
outData
com.apple.pearld.ready
Reference frame (set=%d, frame=%d, size=%d, type=%d, temp=%f) written to %s\n
%s: PSPC data loaded to SEP.\n
checkSecureStreaming -> %d\n
pearlSeaCookieHandleMessage, type=%d -> 0x%x\n
objectSize:\t\t%d\n
encryptFDRData -> %d\n
verifyFDRData %p %zu\n
Verifying new reference frames info record...\n
prewarmCamera -> %d\n
setEntitlementOverrideConfig -> %d\n
Results of Allocation and Mapping Object Scheme3 Context1:\n
mappedToANE:\t\t%s\n
getBrunorCollectionKey\n
ReferenceFramesSetInfo, index: %zu, type: %d, count: %d, size: %d\n
Reference set dictionary written to %s\n
%s: Successfully got provisioning data.\n
simulateSelfTestFailure\n
setDummyWrappedFDRDataEncryptionKey\n
getPDAK\n
getPDAK -> %d\n
encryptFDRData %p %zu %p %p\n
mapScheme3Object: fourcc:%.4s\n\n
prepareFDRDataEncryptionKey\n
Couldn't create OS Log for 'com.apple.BiometricKit.Library-PearlFactory'!\n
Reference frames info record written to %s\n
ispMapFunction:\t\t%s\n
unmappedFromANE:\t%s\n
getAttestationToPDAK -> %d\n
getDummy0PSDData -> %d\n
encryptFDRDataInternal %p %zu %p %p %d\n
mapScheme3Object -> 0x%x\n
dvaOffset:\t\t0x%X\n
getAttestationToBrunorCollectionKey -> %d\n
setDummyWrappedFDRDataEncryptionKey -> %d\n
simulateSelfTestFailure -> %d\n
aneMapFunction:\t\t%s\n
getAttestationToPDAK\n
%s: PSPC data found.\n
generateAndVerifyAriesHostAuthorization\n
encryptFDRDataInternal -> %d\n
prewarmCamera (%u)\n
ispUnmapFunction:\t%s\n
getBrunorCollectionKey -> %d\n
signDataWithBrunorPermanentKey -> %d\n
generateAndVerifyAriesHostAuthorization -> %d\n
%s: Loading PSPC from FDR.\n
aneUnmapFunction:\t%s\n
getAttestationToBrunorCollectionKey\n
signDataWithBrunorCollectionKey\n
ReferenceFramesInfo setCount: %d\n
Generating reference frames info record...\n
ReferenceFramesSetInfo, index: %d, type: %d, count: %d, size: %d\n
getPearlSelfTestResult -> %d\n
checkSecureStreamingAndVerifySignatures (%u)\n
allocateAndMapObjectS3C1: fourcc:%.4s mapObj:%d unmapObj:%d\n\n
objectFound:\t\t%s\n
getBrunorPermanentKey\n
ReferenceFramesPath: %s\n
encryptFDRDataForBrunor %p %zu %p %p %p %zu\n
unmappedFromSEP:\t%s\n
checkSavageProvisioning -> %d\n
getPearlSelfTestResult\n
pearlSeaCookieHandleMessage %d %p %zu %p %p\n
mappedToSEP:\t\t%s\n
signDataWithBrunorCollectionKey -> %d\n
getBrunorPermanentKey -> %d\n
encryptFDRDataForBrunor -> %d\n
verifyFDRData -> %d\n
Generating reference frames files...\n
checkSavageProvisioning\n
setEntitlementOverrideConfig (0x%x)\n
allocateAndMapObjectS3C1 -> 0x%x\n
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n
Removed %@\n
checkSecureStreaming\n
checkSecureStreamingAndVerifySignatures -> %d\n
pearlSeaCookieHandleMessage, type=%d reply[%zu] %.*P\n
unmappedFromISP:\t%s\n
signDataWithBrunorPermanentKey\n
getDummy0PSDData\n
mappedToISP:\t\t%s\n
prepareFDRDataEncryptionKey -> %d\n
ARUListenerProtocol
NSObject
ARUListener
ARUServiceProtocol
ARUListenerBase
createDirectoryAtPath:withIntermediateDirectories:attributes:error:
dataWithBytesNoCopy:length:freeWhenDone:
retainCount
setDigest:withDataInstance:Digest:andReponse:
length
release
fileExistsAtPath:
init
containsObject:
createSignatureForPayload:andGetResponse:
description
hash
interfaceWithProtocol:
sendMinimalManifestPropertyCheckTag:andResponse:
setExportedObject:
stringByAppendingPathComponent:
stringWithFormat:
synchronousRemoteObjectProxyWithErrorHandler:
dataWithLength:
dictionary
initWithARUContextRef:
invalidate
readAruCtxAMFDRSafe:
retain
self
valueForKey:
T@\"NSString\",R,C
appendData:
intValue
performSelector:withObject:withObject:
sendFdrStatistics:andResponse:
TQ,R
addLegacyDataClassForExport:andResponse:
mutateAruCtxAMFDRSafe:
setObject:forKeyedSubscript:
isProxy
_xpcConnection
performSelector:withObject:
sendMultiSealingMetadata:andResponse:
T#,R
copyRefKeyPubKeyAndAttestation:
removeItemAtPath:error:
copyRestoreLocalPolicy:
countByEnumeratingWithState:objects:count:
defaultManager
dictionaryWithDictionary:
initWithServiceName:
isMemberOfClass:
sendTristarEsn:andResponse:
setInterruptionHandler:
bytes
isEqual:
setRemoteObjectInterface:
superclass
UTF8String
initWithFormat:
addDataClassForClaim:withDataInstance:andReponse:
class
executeARUTask:withOptions:getReply:
isKindOfClass:
sendLog:withReply:
setExportedInterface:
T@\"NSString\",?,R,C
dictionaryWithObjects:forKeys:count:
errorWithDomain:code:userInfo:
mutableBytes
respondsToSelector:
resume
writeToFile:atomically:
zone
autorelease
copySsoTicket:
setInvalidationHandler:
setLength:
URLWithString:
copyProvisioningData:
debugDescription
performSelector:
setLogHandlerConn:
stringWithUTF8String:
valueForKeyPath:
code
conformsToProtocol:
v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16
v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24
B24@0:8@16
B16@0:8
v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32
v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24
v48@0:8@\"NSString\"16@\"NSString\"24@\"NSData\"32@?<v@?@\"NSError\">40
#16@0:8
@16@0:8
B24@0:8#16
Vv16@0:8
Q16@0:8
v24@0:8@?16
v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">24
v32@0:8@\"NSData\"16@?<v@?@\"NSError\">24
v24@0:8@?<v@?@\"NSData\"@\"NSData\"@\"NSError\">16
@32@0:8:16@24
@24@0:8:16
B24@0:8:16
@24@0:8^{__ARUContext={__CFRuntimeBase=QAQ}^{__CFDictionary}^{__CFDictionary}^{__CFDictionary}^{__CFArray}^{__CFData}^{__CFData}^{__CFBoolean}^{__AMFDR}^{__AMFDR}^?^?^v}16
v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\">32
v24@0:8@?<v@?@\"NSDictionary\">16
@40@0:8:16@24@32
^{_NSZone=}16@0:8
v48@0:8@16@24@32@?40
v32@0:8@\"NSArray\"16@?<v@?@\"NSError\">24
v32@0:8@\"NSString\"16@?<v@?@\"NSNumber\">24
@\"NSString\"16@0:8
v40@0:8@16@24@?32
v24@0:8@?<v@?@\"NSData\"@\"NSError\">16
B24@0:8@\"Protocol\"16
v32@0:8@16@?24
```
