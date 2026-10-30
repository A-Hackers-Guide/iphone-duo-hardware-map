# `/usr/lib/updaters/libSavageUpdater_iOS.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 314,688 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 27 (Size: 3192)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (11)

- `/usr/lib/updaters/libSavageUpdater_iOS.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/updaters/libSavageRestoreInfo_iOS.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (697)

```
dataWithLength:
URLWithString:
appendData:
dictionaryWithDictionary:
dictionaryWithObjects:forKeys:count:
stringWithFormat:
writeToFile:atomically:
stringByAppendingPathComponent:
createDirectoryAtPath:withIntermediateDirectories:attributes:error:
dataWithBytesNoCopy:length:freeWhenDone:
fileExistsAtPath:
mutableBytes
removeItemAtPath:error:
length
UTF8String
bytes
defaultManager
setObject:forKeyedSubscript:
dictionary
setLength:
stringWithUTF8String:
Verifying new reference frames info record...\n
%s: PSPC data loaded to SEP.\n
checkSecureStreaming -> %d\n
checkSecureStreamingAndVerifySignatures -> %d\n
setEntitlementOverrideConfig -> %d\n
allocateAndMapObjectS3C1: fourcc:%.4s mapObj:%d unmapObj:%d\n\n
Results of Allocation and Mapping Object Scheme3 Context1:\n
getBrunorPermanentKey -> %d\n
aneUnmapFunction:\t%s\n
Reference frame (set=%d, frame=%d, size=%d, type=%d, temp=%f) written to %s\n
ReferenceFramesSetInfo, index: %zu, type: %d, count: %d, size: %d\n
getAttestationToBrunorCollectionKey\n
getAttestationToPDAK -> %d\n
generateAndVerifyAriesHostAuthorization\n
SavageDeviceLog: target-type = %s; unallowedTarget = %s \n
%s: Loading PSPC from FDR.\n
getPearlSelfTestResult -> %d\n
allocateAndMapObjectS3C1 -> 0x%x\n
prepareFDRDataEncryptionKey\n
setDummyWrappedFDRDataEncryptionKey -> %d\n
getDummy0PSDData\n
generateAndVerifyAriesHostAuthorization -> %d\n
ReferenceFramesInfo setCount: %d\n
JasmineIRLog: %s \n
SavageLog: %s \n
%s: PSPC data found.\n
dvaOffset:\t\t0x%X\n
getBrunorCollectionKey\n
encryptFDRDataForBrunor %p %zu %p %p %p %zu\n
getDummy0PSDData -> %d\n
encryptFDRDataInternal %p %zu %p %p %d\n
Generating reference frames files...\n
setDummyWrappedFDRDataEncryptionKey\n
encryptFDRData %p %zu %p %p\n
pearlSeaCookieHandleMessage, type=%d -> 0x%x\n
mapScheme3Object: fourcc:%.4s\n\n
prepareFDRDataEncryptionKey -> %d\n
YonkersIRxDeviceLog: %s \n
getPearlSelfTestResult\n
simulateSelfTestFailure -> %d\n
checkSecureStreamingAndVerifySignatures (%u)\n
pearlSeaCookieHandleMessage %d %p %zu %p %p\n
ispUnmapFunction:\t%s\n
mappedToSEP:\t\t%s\n
unmappedFromANE:\t%s\n
checkSavageProvisioning\n
prewarmCamera (%u)\n
mapScheme3Object -> 0x%x\n
objectFound:\t\t%s\n
mappedToISP:\t\t%s\n
signDataWithBrunorCollectionKey\n
signDataWithBrunorCollectionKey -> %d\n
getPDAK\n
verifyFDRData -> %d\n
checkSecureStreaming\n
aneMapFunction:\t\t%s\n
mappedToANE:\t\t%s\n
unmappedFromSEP:\t%s\n
getBrunorPermanentKey\n
signDataWithBrunorPermanentKey -> %d\n
Couldn't create OS Log for 'com.apple.BiometricKit.Library-PearlFactory'!\n
YonkersLog: %s \n
verifyFDRData %p %zu\n
Generating reference frames info record...\n
setEntitlementOverrideConfig (0x%x)\n
signDataWithBrunorPermanentKey\n
getPDAK -> %d\n
ReferenceFramesSetInfo, index: %d, type: %d, count: %d, size: %d\n
simulateSelfTestFailure\n
getBrunorCollectionKey -> %d\n
Removed %@\n
Reference set dictionary written to %s\n
prewarmCamera -> %d\n
encryptFDRDataForBrunor -> %d\n
getAttestationToPDAK\n
%s: Successfully got provisioning data.\n
checkSavageProvisioning -> %d\n
pearlSeaCookieHandleMessage, type=%d reply[%zu] %.*P\n
unmappedFromISP:\t%s\n
YonkersIRxLog: %s \n
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n
encryptFDRData -> %d\n
ispMapFunction:\t\t%s\n
ReferenceFramesPath: %s\n
objectSize:\t\t%d\n
encryptFDRDataInternal -> %d\n
Reference frames info record written to %s\n
getAttestationToBrunorCollectionKey -> %d\n
%s: Finished pre-personalizing \n
YonkersIR/YonkersIR1PatchAuthCertification.DAT
Yonkers: YonkersUpdateController::writeFilesToFileSystem: persoLoop=%d, isProd=%d, isYmgt=%d\n
/SavagePatch.DER
%s: Begin actual NGID Provisioning \n
%s/%@
YonkersIR1MacAlgo
FirmwareSignature (Pre-validation):--------------offset = %d (%d)\n
/SavagePatch.FW
%s: Savage firmware passed in as a dictionary \n
SavageUpdaterCreate - failed to register kLibSavageUpdaterClass
outHostPubKeyLength && (*outHostPubKeyLength >= (448 / 8))
PSD3
%s: AMSupportWriteDataToFileURL failed with fileNameFS \n
/SavageLeafCert%s%s.DER
inData
_connect != ((io_object_t) 0)
YonkersIR/YonkersIR3BinaryPlusHeaderPatchProvCertification.FW
/SavageFirmwareSigAuthCertification.DER
/SavageLeafSigWrap.DER
_LeftEcam
SavageUpdaterIsDone - no yonkers controller instance
outDataSize <= signedRefFramesInfoRecordData.length
SavageUpdaterExecCommand - Preflighting - controller exec command error
YonkersIR/YonkersIR3PatchAuthCertification.DER
%s: - result = 0x%08X (chipID = 0x%08X) \n
\n SavageUpdateController::validateSignatureLen -- s length = %d \n
/SavageFullCertAuthCertification.DER
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n
YonkersIR/YonkersIR4PatchAuthCertification.DAT
/YonkersPatch%s%s.DAT
%s: VTPatchLen = %d; Number of patch toggle commands - %d; ysy%c; yvt%c \n
/SavageLeafSigCertification.DER
/SavageLeafCertWrap.DER
ReferenceFramesSetInfo, index: %zu, type: %d, count: %d, size: %d\n
denseLP
IODeviceTree:/chosen
AuthPubKey
YonkersIR/YonkersIR2BinaryPlusHeaderPatchCertification.FW
Reference set dictionary written to %s\n
encryptedBuffer
%s [output]: %s %s \n
YonkersIR/YonkersIR4PatchProvCertification.DER
/YonkersPatchFusing.DER
decryptedDataBuffer
ReferenceFramesSetInfo, index: %d, type: %d, count: %d, size: %d\n
YonkersIR1ChipID
CertificationURL
YonkersIR/YonkersIR.Dev.fw
YonkersIR3ECPubKeyHmac
validateSignatureLen
getFirmware
%s: Digest offset and length are correctly calculated \n
AuthResponse
YonkersIR/YonkersIR2PatchFusing.DER
signedRefFramesInfoRecordData
/SavageFirmwareSigWrap.DER
DataDirectory
eventCmdPerformNextStage
YonkersIR/YonkersIR4BinaryPlusHeaderPatchFusing.FW
YonkersIR/YonkersIR3BinaryPlusHeaderPatch.FW
/SavagePatchWrap.DER
ApplePearlExclaveSEPDriver
%@/%@
fileURL
%s: Add the results of the command processed to the output \n
/YonkersPatchBinaryPlusHeader.FW
LeafSignature(Post-validation):--------------offset = %d (%d)\n
/SavageFirmwareSig.DER
SavageUpdaterCreate - no yonkersIRx controller instance
No C string description available.
ProvenanceCertOption
glenbrook
sensor-type
JasmineIRUpdateController::eventCmdPerformNextStage: Begin actual wrapping live nonce boot \n
refFrameData
YonkersIR4
start
/SavagePatchFusing.DAT
/SavageFullCert%s%s.DER
/SavageFullCert.DER
ECPubKey
ProvPubKey
%s: Extracting provenance certification data is done with result = 0x%02X (tryAgain = %d) \n
furei
SavagePubKeyHmac
WrapOption
SavageUpdaterCreate - no yonkers controller instance
connect
CreateDeviceInfoDict
%s: AMSupportMakeDirectory failed with fileNameFS \n
num != NULL
replySize == sizeof(status)
callback
mappedToISP:\t\t%s\n
dataLength
YonkersIRx: restoreOptions missing or not a dictionary\n
%s: Exiting execCommand: command = %s, result = 0x%X, numInstance = %d \n
YonkersUpdateController.cpp
YonkersIRx: No yonkersIRxOptions \n
Prod
/YonkersPatch%s%s.DER
%s: Entering execCommand: command = %s, numPersoLoopForInstance[%d] = %d \n
%s: Begin Auth Flow \n
YonkersIR/YonkersIR2PatchAuthCertification.DER
\n %s -- r length = %d \n
/YonkersPatch.DER
savageFWCert && savageFWCertLength
YonkersIR/YonkersIR1PatchFusing.DER
%s [CSR]: %s (status = 0x%08X) \n
SavageUID
%s: Finished pre-wrapping \n
%s: Missing FDRDataEncryptionKey in ioreg \n
com.apple.pearld.check_secure_streaming
Results of Allocation and Mapping Object Scheme3 Context1:\n
FlipFusingState
aries
ReferenceFramesPath: %s\n
Reference frames info record written to %s\n
savagePubKey
pspcData
attestationLength
YonkersIR2MNS
YonkersIR/YonkersIR4BinaryPlusHeaderPatchProvCertification.FW
lakeville
%s: Entering execCommand: command = %s, persoLoop = %d \n
JasmineIR: JasmineIRUpdateController::writeFilesToFileSystem: persoLoop=%d, isProd=%d
%@: %s
/SavageFullCertCertification.DER
notifyResult == 0
YonkersIR1ProvPubKeyHmac
PersonalizeOnlyThisInstance
%s: Begin Provenance Certification Flow \n
Yonkers,SysTopPatch%X
SavageUpdaterCreate - no savage controller instance
SavageUpdaterIsDone - no savage controller instance
outConnect
dataInfo
YonkersIR/YonkersIR1BinaryPlusHeaderPatchFusing.FW
\n SavageUpdateController::validateSignatureLen -- Padding the r value with %d zero bytes \n
(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || messageSize
dvaOffset:\t\t0x%X\n
PersonalizedFirmwareRootPath
%s: Begin reading info needed for certification - %d\n
LeafSignature(Pre-validation):--------------offset = %d (%d)\n
YonkersIR/YonkersIR3BinaryPlusHeaderPatchCertification.FW
LeafSignature (Pre-validation):--------------offset = %d (%d)\n
YonkersIR1FabRevision
YonkersIR2ChipID
%s - %d bytes\n
Yonkers: fwSigOffset = 0x%02X, fwSigEncapLen = 0x%02X, lfManifestStartOffset = 0x%02X, im4cSeqStartOffset = 0x%02X, im4cStartOffset = 0x%02X, lfSigOffset = 0x%02X, lfSigEncapLen = 0x%02X \n
%s: Begin NGID Provisioning \n
%s: NGID_d_e: \n
/SavageLeafCertFusing.DER
v8@?0
YonkersIR2Nonce
YonkersIR/YonkersIR3PatchFusing.DER
CertifyRawPublicKey
Ngsk
%.6f
%s: PSPC data loaded to SEP.\n
pearldReady
objectSize:\t\t%d\n
YonkersPubKeyHmac
%s: Begin reading info needed for certification \n
SavageUpdaterExecCommand - invalid input to SavageUpdaterExecCommand
dictFileName
att
%s: Finished Personalization \n
FirmwareSignature (Post-validation):--------------offset = %d (%d)\n
/SavagePatchCertification.DAT
SavageUpdaterExecCommand - No-preflight - controller exec command error
fdrInput
Options
tmpData
YonkersIR1UID
%s: Begin actual Fusing \n
JasmineIR1,FWPatch%X
BA
*outLength >= minimalOutputBufferLength
SavageAuthCSR
%s: Savage firmware passed in as a data ref \n
unmappedFromSEP:\t%s\n
replySize <= sizeof(cmd_get_brunor_permanent_key_out_v1_t)
YonkersIR3AuthPubKeyHmac
YonkersIR1AuthSalt
FusingOption
 %02X 
CertifyChallengeSupport128b
ispMapFunction:\t\t%s\n
aneUnmapFunction:\t%s\n
replySize == sizeof(*outData)
sensorIsProvisioned
IODeviceTree:/
/SavageLeafSig%s%s.DER
path
replySize <= (16 * 1024)
JasmineIR: Signed Certificate (TSS Response):-------------- Length = %d \n
attestation && attestationLength
formatAndStitchFiles
YonkersUID
RestoreSystemPartition
YonkersIR/YonkersIR2PatchProvCertification.DAT
%s: Exiting execCommand: command = %s, result = 0x%X, persoLoop = %d \n
signature
YonkersIR3ProvPubKeyHmac
YonkersIR/YonkersIR3PatchAuthCertification.DAT
YonkersIR/YonkersIR1BinaryPlusHeaderPatchProvCertification.FW
%s: Finished pre NGID Provisioning \n
systemRootPath
YonkersIR/YonkersIR4BinaryPlusHeaderPatchCertification.FW
YonkersFabRevision
target-type
getFirmwareDigest
YonkersIR1AuthPubKey
YonkersIR2AuthResponse
%s: Send out the results in fOutput of the command processed\n
hamal
bagdemagus
%s: PearlStatus=%d, KCV=0x%x \n
<libSavageUpdater %p [%p]>{} \n
PostFDRSealing
YonkersIR/YonkersIR1Patch.DER
sigSLen >= MIN_SIG_LEN && sigSLen <= MAX_ACCEPTED_SIG_LEN
%s: %s (%d)\n
__os_warn_unused(__builtin_add_overflow((dataLength), (2 * 16 + __builtin_offsetof(psd2_encrypted_t, encryptedData)), (&minimalOutputBufferLength))) == 0 
Verifying new reference frames info record...\n
YonkersIR2UID
YonkersIR2FabRevision
%s: Begin Fusing \n
YonkersIR/YonkersIR2BinaryPlusHeaderPatchAuthCertification.FW
YonkersChipID
%s: Finished wrapping: 0x%02llx (result = 0x%02X; tryAgain = %d) \n
tempString
reference-%@__T_%@.bin
YonkersIR3ChipID
YonkersIR/YonkersIR4PatchProvCertification.DAT
/YonkersPatchCertification.DER
SavageAuthPubKeyHmac
%s: Picked up FDRDataEncryptionKey as wrap input key \n
i
VerifyData
%s: Loading PSPC from FDR.\n
ECPubKeyHmac
SavageWrapOutputKey
PSD2
CheckProvisioningStatus
\n YonkersIRx: %s \n
YonkersIR/YonkersIR4PatchAuthCertification.DER
Yonkers: signedCertLen = 0x%02X, totalManifestLen = 0x%02X, lfManifestLen = 0x%02X, im4cSeqLen = 0x%02X \n
%s - %p (%p) - UpdaterIsSupported = %d; JasmineIRIsPresent = %d \n
ret > 0 && ret < sizeof(tempChar)
YonkersIR/YonkersIR1PatchProvCertification.DAT
YonkersIR/YonkersIR4Patch.DAT
getSignedCertificate
SavageKCV
%@: Input Options: %@
SavageUpdaterCreate - failed to create SavageUpdaterObj
YonkersIR2AuthSalt
%s - %p (%p) - UpdaterIsSupported = %d; numInstances = %d; YonkersIRIsPresent[%d] = %d \n
Yonkers: TSS Response:--------------Total Length = %d \n
%s: Unsupported command: %s\n
YonkersIR/YonkersIR4PatchCertification.DAT
SavageAuthPubKey
/SavagePatchWrap.DAT
SavageCFDictionarySetData
AppleH16CamIn
%@-%@
YonkersIsYmgt
%s: PSPC data found.\n
permanentKeyLength
YonkersIR/YonkersIR3BinaryPlusHeaderPatchFusing.FW
/YonkersPatchFusing.DAT
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n
YonkersIRx: YonkersIRxUpdateController::eventCmdQueryInfoPreflighting: Finished Preflighting for sensor number %d (result = %d)\n
YonkersIR/YonkersIR4PatchFusing.DAT
YonkersIR/YonkersIR4BinaryPlusHeaderPatch.FW
Auth challenge received from libFDR:--------------\n
%s: isProvisioned=%d \n
libSavageUpdater
YonkersIR3AuthSalt
ProvPubKeyHmac
YonkersIR/YonkersIR1PatchCertification.DER
/SavagePatchAuthCertification.DER
YonkersErrorDomain
YonkersIR/YonkersIR1PatchAuthCertification.DER
YonkersIR/YonkersIR1BinaryPlusHeaderPatch.FW
/usr/standalone/firmware/Yonkers/
*attestation
outDataLength
sensorType
SavagePrivateHelper.cpp
/SavageFirmwareSig%s%s.DER
cmd
data
YonkersIR/YonkersIR3PatchProvCertification.DAT
%s Tried NGID Provisioning...look for valid KCV in the ioreg (NGIDProvStatus = %d) \n
(*outLength > 0) && (*outLength >= dataLength)
outKCVLength && (*outKCVLength >= 3)
execCommand
%s: Finished pre-auth-flow \n
CertifyRawECDSASignature
%s: This sensor doesn't support auth flow \n
JasmineIRUpdateController.cpp
/SavagePatchCertification.DER
*signature
YonkersIR1AuthResponse
writeFilesToFileSystem
SavageNonce
FDRDataEncryptionKey
/System/Library/Caches/com.apple.factorydata
(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || message
replySize <= sizeof(reply)
AppleH13CamIn
/usr/standalone/firmware/
dataLength > 0
YonkersIR3MacAlgo
destroyInstance
/SavageFullCertFusing.DER
%s [input]: %s %s \n
/SavageFirmwareSigCertification.DER
SavageUpdaterExecCommand - no yonkersIRx controller instance
/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m
YonkersIR/YonkersIR2PatchCertification.DAT
/SavageLeafSigAuthCertification.DER
outResult
pdak && pdakLength
YonkersIR3MNS
YonkersIR/YonkersIR3PatchFusing.DAT
YonkersIR/YonkersIR3Patch.DER
getSavageProvisioningData
YonkersIR1Nonce
eventCmdQueryInfo
\n %s -- Padding the s value with %d zero bytes \n
_RightBcam
outLength
outPSD3Length
YonkersIR3Nonce
AuthCertOption
YonkersNonce
YonkersMNS
numLenOctets <= MAX_LEN_OCTETS
SavageAuthSalt
encryptedDataBuffer
GetCombined
replySize == sizeof(outData)
(type == kPearlFactorySeaCookieValidateTatsuTicket) || replySize
objectFound:\t\t%s\n
%s: Begin reading info needed for auth flow \n
YonkersIR/YonkersIR2BinaryPlusHeaderPatchFusing.FW
/SavagePatch%s%s.DAT
PSD2Length
com.apple.BiometricKit
YonkersIR2AuthPubKeyHmac
getInstance
YonkersIR/YonkersIR2PatchFusing.DAT
Reference frame (set=%d, frame=%d, size=%d, type=%d, temp=%f) written to %s\n
YonkersIR/YonkersIR3BinaryPlusHeaderPatchAuthCertification.FW
YonkersIR/YonkersIR4Patch.DER
SavageChipID
%s Begin reading info needed for certification \n
ReferenceFramesInfo setCount: %d\n
YonkersIR/YonkersIR3PatchCertification.DER
%s: Fetching digest during SeaCookie pairing\n
%@/reference-%@.plist
(outData->attestationLength > 0) && (outData->attestationLength <= (16 * 1024))
YonkersIsProvisioned
%s -  certStartAddr=0x%08X, firmwareStartAddr=0x%08X, theCompletePatchFileLen=%d, signedCertificateLen=%d, firmwareDataLen=%d, 4cc=%s \n
SavageUpdateController::eventCmdPerformNextStage: Begin actual wrapping live nonce boot \n
FormatDR
collectionKeyLength
%sPubKey
/YonkersPatchCertification.DAT
JasmineIRIsProvisioned
_LeftBcam
SavageUpdaterExecCommand - no savage controller instance
mappedToSEP:\t\t%s\n
%sPubKeyHmac
sigRLen >= MIN_SIG_LEN && sigRLen <= MAX_ACCEPTED_SIG_LEN
SavageMacAlgo
%s - %p (%p) - UpdaterIsSupported = %d; SavageIsPresent = %d \n
outNGIDDELength && (*outNGIDDELength >= 16)
YonkersIRxDeviceOpen
YonkersIR/YonkersIR2PatchProvCertification.DER
Yonkers: Signed Certificate:-------------- Length = %d \n
SavageAuthResponse
B3
/SavagePatch%s%s.DER
YonkersIR4propNam
YonkersIR2
SavageMNS
dataInfo->setCount > 0
refFrame
YonkersIR/YonkersIR4BinaryPlusHeaderPatchAuthCertification.FW
_RightEcam
SavageErrorDomain
SavageCFDictionarySetInteger32
savageUID
%x
%s: Input specified to the processing command\n
Complete Signed Savage Certificate:--------------Length = %d \n
%s: persoLoop=%d, isProd=%d, isBalan=%d\n
YonkersIRUpdateController::start: isProvisioned[%d]=0x%llX; numPersoLoopForInstance[%d]=%d \n
%s: Begin Personalization \n
YonkersIR/YonkersIR1PatchCertification.DAT
AppleCamera
YonkersIR2ProvPubKeyHmac
\n %s -- Padding the r value with %d zero bytes \n
\n JasmineIR: %s \n
SavageUpdateCreate - no jasmine ir controller instance
dense
sparse
YonkersIR1ECPubKeyHmac
getTSSResponse
sema
YonkersIR2MacAlgo
%s: Extracting auth certification data is done with result = 0x%02X (authFlowLoop = %d, tryAgain = %d) \n
YonkersIR/YonkersIR4PatchCertification.DER
getAuthChallenge
\n SavageUpdateController::validateSignatureLen -- Padding the s value with %d zero bytes \n
SavageUpdaterIsDone - no yonkersIRx controller instance
refPath
%s: Including auth challenge key in the DAT file \n
%s: isProvisioned=%d; isSocProdFused=%d; persoLoop = %d\n
pspc
YonkersIR/YonkersIR.Prod.fw
LeafCertificate:--------------offset = %d (%d)\n
%s
sparseLP
size == sizeof(response)
YonkersIR1MNS
%s: Begin Wrapping \n
YonkersIR%d,SysTopPatch%X
PSD3MACLength == (16)
YonkersIR2AuthPubKey
%s: Extracting certification data is done with result = 0x%02X (tryAgain = %d) \n
FirmwareData
YonkersIR/YonkersIR2PatchAuthCertification.DAT
/SavageLeafSigFusing.DER
provisioningStatus
YonkersIR/YonkersIR2PatchCertification.DER
JasmineIR1,FwPatch%X
setDictionary
v12@?0i8
Dev
/SavagePatchAuthCertification.DAT
reply
attestation
output dictionary of execCommand
/SavageLeafSig.DER
JasmineIR: restoreOptions missing or not a dictionary\n
replySize >= sizeof(cmd_alloc_map_s3c1_out_v1_t)
replySize == sizeof(cmd_get_brunor_collection_key_out_v1_t)
/SavagePatchFusing.DER
SavageUpdateController.cpp
YonkersIR1AuthPubKeyHmac
performNextStage
%s moduleDataInstanceStr: %s \n
%s: isProvisioned=0x%llX; isNGIDProvisioned=0x%X; isSocProdfused=%d; persoLoop = %d\n
numSensorInstance
%s - %p (%p) - UpdaterIsSupported = %d; numInstances = %d; \n
YonkersIRx: Signed Certificate (TSS Response):-------------- Length = %d \n
\n %s -- s length = %d \n
YonkersIRxErrorDomain
kcvBuffer
AuthSalt
RestoreInternal
pJasmineIRDevice->fdrDataEncryptionKeyPresent
pathString
%s: Successfully got provisioning data.\n
(type == kPearlFactorySeaCookieValidateTatsuTicket) || reply
signatureLength
%s%s
pData
YonkersIR/YonkersIR3PatchCertification.DAT
%s [error]: %s \n
%s - %p (%p) - UpdaterIsSupported = %d; YonkersIsPresent = %d \n
ApplePearlSEPDriver
serviceName
dataInfo->setCount <= (4)
/SavagePatch%s.DER
Library-PearlFactory
%s - YonkersIRxIsPresent[%d] = %d; chipID = 0x%04x\n
YonkersIRx: YonkersIRxUpdateController::eventCmdQueryInfoPreflighting: Begin Preflighting for sensor number %d \n
%s: Finished eventCmdQueryInfo %d \n
replySize >= sizeof(*outData)
queryInfo
%s: Finished pre-certification \n
IOService
/usr/standalone/firmware/Savage/
%s: Using dummy auth challenge key \n
SavageUpdaterExecCommand - no jasmine ir controller instance
mappedToANE:\t\t%s\n
YonkersIRxUpdateController::writeFilesToFileSystem(): %s (%d)\n
%s - numInstances = %d; updaterSupported = %d\n
%s: Begin Certification \n
writeDataToFileURL
Yonkers: %s \n
FirmwareCertificate:--------------offset = %d (%d)\n
YonkersIR1
%s: File does not exist\n
SavageDeviceRev
com.apple.pearld.ready
development-cert
YonkersIRxUpdateController::formatAndStitchFiles() -  theCompletePatchFileLen=%d, signedCertificateLen=%d, firmwareDataLen=%d \n
LeafSignature (Post-validation):--------------offset = %d (%d)\n
SavagePubKey
\n SavageUpdateController::validateSignatureLen -- r length = %d \n
/SavageLeafCertCertification.DER
SavageUpdaterExecCommand - no yonkers controller instance
/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/PearlSupport/PearlSupportUtils.m
YonkersIR3UID
AuthPubKeyHmac
requestData
YonkersIR/YonkersIR1BinaryPlusHeaderPatchCertification.FW
YonkersIR/YonkersIR1Patch.DAT
YonkersIR/YonkersIR2Patch.DER
Generating reference frames info record...\n
permanentKey
YonkersIR3AuthPubKey
%s \n
/SavagePatch.DAT
/SavageLeafCert.DER
err == 0 
%s: Finished pre-fusing \n
Yonkers: restoreOptions missing or not a dictionary\n
%s: No chipID from string instance \n
collectionKey
YonkersIR2ECPubKeyHmac
%s: Finished pre-prov-certification \n
calibration && (calibrationSize > 0)
%s: Finished Personalization - %d \n
%s: Missing FDRDataEncryptionKey in ioreg - 0x%02X \n
SavageFabRevision
YonkersIR/YonkersIR2BinaryPlusHeaderPatch.FW
/YonkersPatch.DAT
%s: Entering execCommand: command = %s, persoLoop = %d  \n
service
/System/Library/Pearl/ReferenceFrames
camChannel
JasmineIRErrorDomain
/SavageFullCertWrap.DER
SavageUpdaterIsDone - no jasmine ir controller instance
aneMapFunction:\t\t%s\n
YonkersIR/YonkersIR1BinaryPlusHeaderPatchAuthCertification.FW
Yonkers: No YonkersOptions \n
writeFWFilesToFileSystem
JasmineIR1,VideoPatch%X
pSavageDevice->fdrDataEncryptionKeyPresent
clearBuffer
AppleH10CamIn
YonkersIR3AuthResponse
%s: Begin reading info needed for provenance certification - %d\n
YonkersIR/YonkersIR3PatchProvCertification.DER
/SavageFirmwareSigFusing.DER
ispUnmapFunction:\t%s\n
YonkersIR/YonkersIR2Patch.DAT
YonkersIR3FabRevision
AuthCSR
brunor
StripImg4
YonkersIR/YonkersIR2BinaryPlusHeaderPatchProvCertification.FW
CertifyComponentAttributesCriticalProductionMode
Generating reference frames files...\n
%s: Finished fusing with result = 0x%02X (tryAgain = %d) \n
YonkersIRxUpdateController::writeFilesToFileSystem: numPersoLoopForInstance[%d]=%d, isProd=%d \n
YonkersIR/YonkersIR4PatchFusing.DER
%s: KCV: \n
refFileName
YonkersIR3
Ymgt
unmappedFromISP:\t%s\n
unmappedFromANE:\t%s\n
outData
YonkersIR/YonkersIR1PatchFusing.DAT
/SavageLeafCertAuthCertification.DER
prf1Class && (prf1ClassSize > 0)
reference-info-record.DAT
%s - Finding %s \n
%s: restoreOptions missing or not a dictionary\n
%s: isProvisioned=0x%llX; isNGIDProvisioned=0x%X \n
AuthChallengeOption
YonkersIR/YonkersIR3Patch.DAT
/SavagePatch%s.DAT
hostPubKeyBuffer
YonkersIR/YonkersIR1PatchProvCertification.DER
YonkersIRErrorDomain
ngidDEBuffer
```
