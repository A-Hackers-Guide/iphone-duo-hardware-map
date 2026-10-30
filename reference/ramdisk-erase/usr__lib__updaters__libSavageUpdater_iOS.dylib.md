# `/usr/lib/updaters/libSavageUpdater_iOS.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 314,688 bytes.

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
length
dataWithLength:
UTF8String
URLWithString:
dictionaryWithDictionary:
setLength:
dictionary
dictionaryWithObjects:forKeys:count:
setObject:forKeyedSubscript:
appendData:
dataWithBytesNoCopy:length:freeWhenDone:
defaultManager
fileExistsAtPath:
removeItemAtPath:error:
stringWithFormat:
stringWithUTF8String:
stringByAppendingPathComponent:
bytes
createDirectoryAtPath:withIntermediateDirectories:attributes:error:
mutableBytes
writeToFile:atomically:
checkSavageProvisioning\n
prewarmCamera -> %d\n
pearlSeaCookieHandleMessage %d %p %zu %p %p\n
mapScheme3Object: fourcc:%.4s\n\n
getAttestationToBrunorCollectionKey\n
setDummyWrappedFDRDataEncryptionKey -> %d\n
encryptFDRDataForBrunor %p %zu %p %p %p %zu\n
getPDAK\n
getAttestationToBrunorCollectionKey -> %d\n
aneUnmapFunction:\t%s\n
JasmineIRLog: %s \n
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n
verifyFDRData -> %d\n
Reference frames info record written to %s\n
pearlSeaCookieHandleMessage, type=%d -> 0x%x\n
mapScheme3Object -> 0x%x\n
signDataWithBrunorCollectionKey -> %d\n
YonkersIRxLog: %s \n
Removed %@\n
getPearlSelfTestResult -> %d\n
simulateSelfTestFailure -> %d\n
mappedToSEP:\t\t%s\n
prepareFDRDataEncryptionKey\n
getAttestationToPDAK\n
Couldn't create OS Log for 'com.apple.BiometricKit.Library-PearlFactory'!\n
Generating reference frames files...\n
%s: PSPC data loaded to SEP.\n
objectSize:\t\t%d\n
unmappedFromISP:\t%s\n
allocateAndMapObjectS3C1 -> 0x%x\n
signDataWithBrunorPermanentKey -> %d\n
prepareFDRDataEncryptionKey -> %d\n
checkSavageProvisioning -> %d\n
unmappedFromSEP:\t%s\n
generateAndVerifyAriesHostAuthorization -> %d\n
YonkersLog: %s \n
SavageLog: %s \n
ReferenceFramesInfo setCount: %d\n
ReferenceFramesSetInfo, index: %d, type: %d, count: %d, size: %d\n
prewarmCamera (%u)\n
allocateAndMapObjectS3C1: fourcc:%.4s mapObj:%d unmapObj:%d\n\n
Results of Allocation and Mapping Object Scheme3 Context1:\n
mappedToANE:\t\t%s\n
Generating reference frames info record...\n
setEntitlementOverrideConfig -> %d\n
objectFound:\t\t%s\n
ispMapFunction:\t\t%s\n
getBrunorCollectionKey -> %d\n
setDummyWrappedFDRDataEncryptionKey\n
getPDAK -> %d\n
getDummy0PSDData -> %d\n
Reference set dictionary written to %s\n
dvaOffset:\t\t0x%X\n
getBrunorPermanentKey -> %d\n
encryptFDRData -> %d\n
%s: PSPC data found.\n
getPearlSelfTestResult\n
aneMapFunction:\t\t%s\n
encryptFDRDataInternal -> %d\n
ReferenceFramesSetInfo, index: %zu, type: %d, count: %d, size: %d\n
Reference frame (set=%d, frame=%d, size=%d, type=%d, temp=%f) written to %s\n
%s: Loading PSPC from FDR.\n
simulateSelfTestFailure\n
mappedToISP:\t\t%s\n
unmappedFromANE:\t%s\n
signDataWithBrunorCollectionKey\n
%s: Successfully got provisioning data.\n
checkSecureStreaming -> %d\n
checkSecureStreamingAndVerifySignatures -> %d\n
pearlSeaCookieHandleMessage, type=%d reply[%zu] %.*P\n
encryptFDRDataForBrunor -> %d\n
getDummy0PSDData\n
generateAndVerifyAriesHostAuthorization\n
setEntitlementOverrideConfig (0x%x)\n
ispUnmapFunction:\t%s\n
encryptFDRData %p %zu %p %p\n
encryptFDRDataInternal %p %zu %p %p %d\n
Verifying new reference frames info record...\n
checkSecureStreaming\n
checkSecureStreamingAndVerifySignatures (%u)\n
getBrunorPermanentKey\n
YonkersIRxDeviceLog: %s \n
getBrunorCollectionKey\n
signDataWithBrunorPermanentKey\n
SavageDeviceLog: target-type = %s; unallowedTarget = %s \n
verifyFDRData %p %zu\n
ReferenceFramesPath: %s\n
getAttestationToPDAK -> %d\n
SavageKCV
permanentKeyLength
pData
CertificationURL
%s: Begin Auth Flow \n
Yonkers: %s \n
_RightEcam
/SavageFullCertWrap.DER
(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || messageSize
%s: Finished pre-auth-flow \n
Yonkers: YonkersUpdateController::writeFilesToFileSystem: persoLoop=%d, isProd=%d, isYmgt=%d\n
BA
/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/PearlFactoryLib/PearlFactoryLib.m
YonkersIR/YonkersIR3Patch.DER
%s [error]: %s \n
Ngsk
%s Tried NGID Provisioning...look for valid KCV in the ioreg (NGIDProvStatus = %d) \n
SavageUpdaterExecCommand - no yonkers controller instance
%s: PSPC data loaded to SEP.\n
/SavageFirmwareSigCertification.DER
signedRefFramesInfoRecordData
AuthResponse
YonkersIR/YonkersIR3PatchAuthCertification.DAT
%s: %s (%d)\n
/SavagePatchWrap.DER
/SavageLeafCertWrap.DER
YonkersIR/YonkersIR4PatchProvCertification.DER
replySize == sizeof(cmd_get_brunor_collection_key_out_v1_t)
(outData->attestationLength > 0) && (outData->attestationLength <= (16 * 1024))
AppleH16CamIn
Yonkers: restoreOptions missing or not a dictionary\n
SavageAuthSalt
YonkersIRx: No yonkersIRxOptions \n
YonkersIR/YonkersIR3BinaryPlusHeaderPatchFusing.FW
/SavagePatchFusing.DER
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n
sparse
%s: Begin Personalization \n
YonkersIR/YonkersIR2PatchFusing.DAT
%s: Begin Wrapping \n
%s: VTPatchLen = %d; Number of patch toggle commands - %d; ysy%c; yvt%c \n
/SavagePatchCertification.DER
objectSize:\t\t%d\n
unmappedFromANE:\t%s\n
destroyInstance
AuthCSR
CertifyComponentAttributesCriticalProductionMode
/SavagePatch.DAT
/Library/Caches/com.apple.xbs/DC80B99A-71A7-45F7-A533-4926D6628DC9/TemporaryDirectory.RiHkKs/Sources/Pearl_Kernel/PearlSupport/PearlSupportUtils.m
CreateDeviceInfoDict
%s: Finished fusing with result = 0x%02X (tryAgain = %d) \n
%s: AMSupportWriteDataToFileURL failed with fileNameFS \n
LeafSignature (Pre-validation):--------------offset = %d (%d)\n
B3
SavageUpdaterCreate - failed to register kLibSavageUpdaterClass
sparseLP
kcvBuffer
JasmineIR1,FWPatch%X
YonkersIR2ChipID
v8@?0
SavageUpdaterIsDone - no yonkers controller instance
service
prf1Class && (prf1ClassSize > 0)
YonkersIR3AuthPubKeyHmac
%s [CSR]: %s (status = 0x%08X) \n
SavageNonce
YonkersIR1ECPubKeyHmac
YonkersIR1
YonkersIR/YonkersIR4Patch.DER
YonkersChipID
Dev
IODeviceTree:/
decryptedDataBuffer
 %02X 
YonkersIR/YonkersIR1Patch.DER
SavageAuthPubKeyHmac
SavageMacAlgo
FDRDataEncryptionKey
WrapOption
YonkersIR2UID
%s - %d bytes\n
YonkersIR/YonkersIR1PatchFusing.DER
/YonkersPatchFusing.DER
%s [input]: %s %s \n
YonkersIR/YonkersIR1PatchFusing.DAT
/YonkersPatchCertification.DAT
/SavageLeafCert%s%s.DER
YonkersIR1AuthPubKey
%s: restoreOptions missing or not a dictionary\n
/SavageFullCertCertification.DER
SavageUpdaterExecCommand - invalid input to SavageUpdaterExecCommand
SavageUpdaterIsDone - no jasmine ir controller instance
dataLength > 0
CheckProvisioningStatus
YonkersIR3AuthPubKey
%s: Input specified to the processing command\n
ProvPubKeyHmac
\n SavageUpdateController::validateSignatureLen -- s length = %d \n
%s/%@
/System/Library/Caches/com.apple.factorydata
YonkersIR1AuthResponse
YonkersIR/YonkersIR4BinaryPlusHeaderPatchFusing.FW
YonkersIR/YonkersIR2Patch.DER
SavagePubKeyHmac
%s - %p (%p) - UpdaterIsSupported = %d; JasmineIRIsPresent = %d \n
VerifyData
YonkersIR3UID
writeDataToFileURL
%s: Entering execCommand: command = %s, persoLoop = %d \n
refPath
ReferenceFramesSetInfo, index: %d, type: %d, count: %d, size: %d\n
FlipFusingState
YonkersIR/YonkersIR4BinaryPlusHeaderPatchCertification.FW
YonkersIR/YonkersIR4BinaryPlusHeaderPatchAuthCertification.FW
getSignedCertificate
pJasmineIRDevice->fdrDataEncryptionKeyPresent
/SavagePatch%s.DER
ReferenceFramesPath: %s\n
signatureLength
\n %s -- Padding the s value with %d zero bytes \n
/usr/standalone/firmware/Savage/
/SavagePatch.DER
LeafCertificate:--------------offset = %d (%d)\n
/SavageFirmwareSig%s%s.DER
SavageUpdaterCreate - no yonkersIRx controller instance
replySize == sizeof(status)
attestation && attestationLength
PostFDRSealing
ECPubKeyHmac
SavageChipID
SavageDeviceRev
/SavageFirmwareSigWrap.DER
pearldReady
replySize <= sizeof(reply)
performNextStage
YonkersIR/YonkersIR3PatchFusing.DAT
YonkersIRErrorDomain
SavageCFDictionarySetData
/SavageLeafCertCertification.DER
YonkersIR2ProvPubKeyHmac
YonkersIR3AuthSalt
YonkersIR1MacAlgo
fdrInput
YonkersIR1AuthPubKeyHmac
YonkersIR1Nonce
YonkersIRxUpdateController::writeFilesToFileSystem(): %s (%d)\n
SavageAuthResponse
signature
/SavagePatchAuthCertification.DAT
/SavagePatchAuthCertification.DER
/SavageFirmwareSigAuthCertification.DER
AppleH13CamIn
AuthPubKeyHmac
YonkersIRxUpdateController::formatAndStitchFiles() -  theCompletePatchFileLen=%d, signedCertificateLen=%d, firmwareDataLen=%d \n
YonkersIR/YonkersIR1BinaryPlusHeaderPatchAuthCertification.FW
SavageErrorDomain
JasmineIR1,FwPatch%X
mappedToISP:\t\t%s\n
YonkersIR/YonkersIR1PatchAuthCertification.DER
%s: Begin actual NGID Provisioning \n
%s: Savage firmware passed in as a data ref \n
Results of Allocation and Mapping Object Scheme3 Context1:\n
YonkersIR1FabRevision
%s -  certStartAddr=0x%08X, firmwareStartAddr=0x%08X, theCompletePatchFileLen=%d, signedCertificateLen=%d, firmwareDataLen=%d, 4cc=%s \n
/SavageFirmwareSig.DER
mappedToANE:\t\t%s\n
getFirmware
SavageUpdateController.cpp
YonkersIR2AuthSalt
RestoreSystemPartition
YonkersIsProvisioned
/YonkersPatchFusing.DAT
SavageUID
reference-info-record.DAT
YonkersIR1AuthSalt
%s: Finished pre-certification \n
\n SavageUpdateController::validateSignatureLen -- Padding the s value with %d zero bytes \n
savageUID
dvaOffset:\t\t0x%X\n
ispMapFunction:\t\t%s\n
permanentKey
No C string description available.
%s: KCV: \n
replySize <= sizeof(cmd_get_brunor_permanent_key_out_v1_t)
YonkersIR3FabRevision
%s: Begin actual Fusing \n
%s: This sensor doesn't support auth flow \n
_LeftBcam
SavagePrivateHelper.cpp
path
PSD2Length
PSD3
YonkersIRx: YonkersIRxUpdateController::eventCmdQueryInfoPreflighting: Finished Preflighting for sensor number %d (result = %d)\n
CertifyChallengeSupport128b
SavageUpdaterCreate - failed to create SavageUpdaterObj
ReferenceFramesInfo setCount: %d\n
com.apple.pearld.ready
YonkersIR1UID
YonkersIR2ECPubKeyHmac
YonkersIR3ProvPubKeyHmac
\n %s -- r length = %d \n
%s: Using dummy auth challenge key \n
getFirmwareDigest
validateSignatureLen
writeFWFilesToFileSystem
hostPubKeyBuffer
attestation
YonkersIR/YonkersIR2Patch.DAT
Yonkers: fwSigOffset = 0x%02X, fwSigEncapLen = 0x%02X, lfManifestStartOffset = 0x%02X, im4cSeqStartOffset = 0x%02X, im4cStartOffset = 0x%02X, lfSigOffset = 0x%02X, lfSigEncapLen = 0x%02X \n
%s: Finished pre NGID Provisioning \n
/SavageLeafSigFusing.DER
/SavageFirmwareSigFusing.DER
reference-%@__T_%@.bin
aneUnmapFunction:\t%s\n
FusingOption
%s: Extracting provenance certification data is done with result = 0x%02X (tryAgain = %d) \n
Yonkers: Signed Certificate:-------------- Length = %d \n
%s: Finished wrapping: 0x%02llx (result = 0x%02X; tryAgain = %d) \n
/SavagePatchCertification.DAT
target-type
*attestation
YonkersIR/YonkersIR1PatchAuthCertification.DAT
/SavagePatchFusing.DAT
SavageCFDictionarySetInteger32
aneMapFunction:\t\t%s\n
%s - %p (%p) - UpdaterIsSupported = %d; numInstances = %d; \n
%s: Begin Fusing \n
FirmwareData
/SavagePatch%s.DAT
SavageUpdaterExecCommand - no jasmine ir controller instance
%.6f
com.apple.BiometricKit
%s - Finding %s \n
YonkersIRx: restoreOptions missing or not a dictionary\n
eventCmdQueryInfo
outDataLength
clearBuffer
AuthPubKey
Yonkers: TSS Response:--------------Total Length = %d \n
JasmineIRErrorDomain
dense
unmappedFromSEP:\t%s\n
Options
YonkersIR/YonkersIR3Patch.DAT
YonkersIRxErrorDomain
SavageUpdaterCreate - no savage controller instance
denseLP
collectionKeyLength
%s%s
/YonkersPatchBinaryPlusHeader.FW
SavageUpdaterExecCommand - no yonkersIRx controller instance
PSD2
execCommand
getTSSResponse
YonkersIR/YonkersIR.Prod.fw
Yonkers: No YonkersOptions \n
\n %s -- Padding the r value with %d zero bytes \n
writeFilesToFileSystem
serviceName
IOService
SavageMNS
%s: No chipID from string instance \n
replySize == sizeof(outData)
pdak && pdakLength
%s: Finished pre-prov-certification \n
%@/reference-%@.plist
*signature
outPSD3Length
AppleH10CamIn
ECPubKey
numLenOctets <= MAX_LEN_OCTETS
brunor
%s Begin reading info needed for certification \n
SavageUpdateCreate - no jasmine ir controller instance
SavageUpdaterCreate - no yonkers controller instance
(type == kPearlFactorySeaCookieMessageS0) || (type == kPearlFactorySeaCookieGenerateNonce) || message
%s - %p (%p) - UpdaterIsSupported = %d; numInstances = %d; YonkersIRIsPresent[%d] = %d \n
YonkersIR/YonkersIR3PatchAuthCertification.DER
FirmwareCertificate:--------------offset = %d (%d)\n
data
encryptedDataBuffer
reply
YonkersIR3ChipID
%s: Including auth challenge key in the DAT file \n
/SavagePatchWrap.DAT
SavagePubKey
inData
callback
%s - numInstances = %d; updaterSupported = %d\n
%s: Unsupported command: %s\n
YonkersIR/YonkersIR1BinaryPlusHeaderPatchProvCertification.FW
furei
sigSLen >= MIN_SIG_LEN && sigSLen <= MAX_ACCEPTED_SIG_LEN
\n JasmineIR: %s \n
/SavageLeafSig.DER
requestData
development-cert
%s: Finished pre-fusing \n
YonkersIR/YonkersIR4PatchProvCertification.DAT
/YonkersPatch.DER
YonkersErrorDomain
\n SavageUpdateController::validateSignatureLen -- Padding the r value with %d zero bytes \n
/SavageFullCertFusing.DER
Reference frames info record written to %s\n
YonkersIRxDeviceOpen
Auth challenge received from libFDR:--------------\n
/YonkersPatch%s%s.DER
AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n
connect
pspc
%s: Successfully got provisioning data.\n
provisioningStatus
YonkersIR/YonkersIR2BinaryPlusHeaderPatch.FW
%s: Begin NGID Provisioning \n
ispUnmapFunction:\t%s\n
YonkersIR/YonkersIR3PatchFusing.DER
SavageFabRevision
tmpData
/SavageFullCertAuthCertification.DER
i
%@/%@
RestoreInternal
%s: Finished Personalization - %d \n
YonkersPubKeyHmac
v12@?0i8
YonkersIR2
ApplePearlSEPDriver
aries
Generating reference frames files...\n
/SavageLeafSigAuthCertification.DER
savageFWCert && savageFWCertLength
%s: Loading PSPC from FDR.\n
unmappedFromISP:\t%s\n
YonkersIR3ECPubKeyHmac
YonkersIR/YonkersIR2BinaryPlusHeaderPatchCertification.FW
YonkersIR/YonkersIR4BinaryPlusHeaderPatchProvCertification.FW
%s moduleDataInstanceStr: %s \n
FirmwareSignature (Pre-validation):--------------offset = %d (%d)\n
FormatDR
YonkersIR3MacAlgo
YonkersIR/YonkersIR1BinaryPlusHeaderPatch.FW
\n %s -- s length = %d \n
/YonkersPatch.DAT
ret > 0 && ret < sizeof(tempChar)
outResult
mappedToSEP:\t\t%s\n
YonkersIR1MNS
YonkersIR/YonkersIR4PatchAuthCertification.DER
CertifyRawPublicKey
%s: Missing FDRDataEncryptionKey in ioreg \n
AuthSalt
AuthCertOption
ApplePearlExclaveSEPDriver
dataInfo
%s: PSPC data found.\n
YonkersIR/YonkersIR3PatchProvCertification.DAT
%s: PearlStatus=%d, KCV=0x%x \n
collectionKey
YonkersIR2MacAlgo
YonkersIRx: YonkersIRxUpdateController::eventCmdQueryInfoPreflighting: Begin Preflighting for sensor number %d \n
JasmineIR: restoreOptions missing or not a dictionary\n
%s: Savage firmware passed in as a dictionary \n
size == sizeof(response)
dataLength
YonkersIR/YonkersIR4PatchCertification.DER
YonkersIR/YonkersIR2PatchProvCertification.DER
YonkersIR/YonkersIR3BinaryPlusHeaderPatch.FW
%s: Digest offset and length are correctly calculated \n
(*outLength > 0) && (*outLength >= dataLength)
getInstance
YonkersIR/YonkersIR2PatchAuthCertification.DER
YonkersIR/YonkersIR1Patch.DAT
SavageAuthCSR
YonkersIR%d,SysTopPatch%X
ProvenanceCertOption
YonkersIR/YonkersIR1BinaryPlusHeaderPatchFusing.FW
YonkersIR/YonkersIR3BinaryPlusHeaderPatchCertification.FW
%@-%@
/SavageLeafCertAuthCertification.DER
SavageUpdaterExecCommand - no savage controller instance
replySize >= sizeof(cmd_alloc_map_s3c1_out_v1_t)
%s: Begin reading info needed for certification - %d\n
CertifyRawECDSASignature
/SavagePatch%s%s.DAT
%@: %s
sensorType
PersonalizeOnlyThisInstance
%s: Begin Provenance Certification Flow \n
%s - %p (%p) - UpdaterIsSupported = %d; YonkersIsPresent = %d \n
outLength
Generating reference frames info record...\n
outHostPubKeyLength && (*outHostPubKeyLength >= (448 / 8))
YonkersIR2FabRevision
%sPubKey
/SavageLeafCert.DER
calibration && (calibrationSize > 0)
objectFound:\t\t%s\n
YonkersIR/YonkersIR.Dev.fw
/usr/standalone/firmware/Yonkers/
%@: Input Options: %@
/SavageLeafSigWrap.DER
libSavageUpdater
refFrame
tempString
Reference set dictionary written to %s\n
IODeviceTree:/chosen
Yonkers,SysTopPatch%X
/YonkersPatchCertification.DER
_LeftEcam
\n SavageUpdateController::validateSignatureLen -- r length = %d \n
SavageUpdaterIsDone - no savage controller instance
*outLength >= minimalOutputBufferLength
replySize >= sizeof(*outData)
\n YonkersIRx: %s \n
%s: isProvisioned=%d; isSocProdFused=%d; persoLoop = %d\n
JasmineIR1,VideoPatch%X
SavageUpdaterExecCommand - Preflighting - controller exec command error
setDictionary
encryptedBuffer
YonkersIR/YonkersIR4PatchFusing.DAT
/YonkersPatch%s%s.DAT
SavageWrapOutputKey
%s: Missing FDRDataEncryptionKey in ioreg - 0x%02X \n
sema
YonkersIR2MNS
/usr/standalone/firmware/
YonkersIRx: Signed Certificate (TSS Response):-------------- Length = %d \n
FirmwareSignature (Post-validation):--------------offset = %d (%d)\n
Yonkers: signedCertLen = 0x%02X, totalManifestLen = 0x%02X, lfManifestLen = 0x%02X, im4cSeqLen = 0x%02X \n
pSavageDevice->fdrDataEncryptionKeyPresent
/SavageLeafSigCertification.DER
outKCVLength && (*outKCVLength >= 3)
YonkersIR3
%s: Entering execCommand: command = %s, numPersoLoopForInstance[%d] = %d \n
YonkersIR1ProvPubKeyHmac
%s: isProvisioned=%d \n
ReferenceFramesSetInfo, index: %zu, type: %d, count: %d, size: %d\n
(type == kPearlFactorySeaCookieValidateTatsuTicket) || replySize
dataInfo->setCount > 0
__os_warn_unused(__builtin_add_overflow((dataLength), (2 * 16 + __builtin_offsetof(psd2_encrypted_t, encryptedData)), (&minimalOutputBufferLength))) == 0 
YonkersIR2AuthPubKey
%s: File does not exist\n
YonkersFabRevision
Ymgt
LeafSignature(Post-validation):--------------offset = %d (%d)\n
/SavageLeafSig%s%s.DER
SavageUpdaterExecCommand - No-preflight - controller exec command error
<libSavageUpdater %p [%p]>{} \n
queryInfo
%s: Begin reading info needed for auth flow \n
sensor-type
Complete Signed Savage Certificate:--------------Length = %d \n
%s
getSavageProvisioningData
pspcData
%s: Entering execCommand: command = %s, persoLoop = %d  \n
_connect != ((io_object_t) 0)
ProvPubKey
outConnect
Reference frame (set=%d, frame=%d, size=%d, type=%d, temp=%f) written to %s\n
PersonalizedFirmwareRootPath
YonkersIR/YonkersIR4PatchCertification.DAT
Prod
%s: Picked up FDRDataEncryptionKey as wrap input key \n
%s: AMSupportMakeDirectory failed with fileNameFS \n
YonkersIR/YonkersIR4PatchFusing.DER
YonkersIR/YonkersIR3BinaryPlusHeaderPatchAuthCertification.FW
/SavageFullCert%s%s.DER
(type == kPearlFactorySeaCookieValidateTatsuTicket) || reply
YonkersIR/YonkersIR1PatchProvCertification.DER
%s: isProvisioned=0x%llX; isNGIDProvisioned=0x%X \n
replySize == sizeof(*outData)
%s: Fetching digest during SeaCookie pairing\n
%s: persoLoop=%d, isProd=%d, isBalan=%d\n
YonkersIR/YonkersIR2BinaryPlusHeaderPatchProvCertification.FW
YonkersUID
JasmineIR: JasmineIRUpdateController::writeFilesToFileSystem: persoLoop=%d, isProd=%d
outData
YonkersIR4propNam
YonkersIRUpdateController::start: isProvisioned[%d]=0x%llX; numPersoLoopForInstance[%d]=%d \n
com.apple.pearld.check_secure_streaming
YonkersIR2Nonce
YonkersIRxUpdateController::writeFilesToFileSystem: numPersoLoopForInstance[%d]=%d, isProd=%d \n
YonkersMNS
bagdemagus
dictFileName
YonkersIR3Nonce
YonkersNonce
%s: Exiting execCommand: command = %s, result = 0x%X, persoLoop = %d \n
/SavagePatch.FW
outDataSize <= signedRefFramesInfoRecordData.length
GetCombined
%s: Finished pre-personalizing \n
lakeville
notifyResult == 0
%s: Add the results of the command processed to the output \n
YonkersIR/YonkersIR1PatchCertification.DER
outNGIDDELength && (*outNGIDDELength >= 16)
attestationLength
hamal
savagePubKey
YonkersIR/YonkersIR4Patch.DAT
output dictionary of execCommand
YonkersIR/YonkersIR3PatchCertification.DAT
num != NULL
/SavageLeafCertFusing.DER
YonkersIR/YonkersIR1PatchProvCertification.DAT
%s: Finished Personalization \n
%s: Extracting auth certification data is done with result = 0x%02X (authFlowLoop = %d, tryAgain = %d) \n
YonkersIR/YonkersIR2PatchCertification.DAT
/SavagePatch%s%s.DER
cmd
ngidDEBuffer
att
sigRLen >= MIN_SIG_LEN && sigRLen <= MAX_ACCEPTED_SIG_LEN
%s: NGID_d_e: \n
%x
YonkersIR/YonkersIR2PatchFusing.DER
getAuthChallenge
SavageUpdateController::eventCmdPerformNextStage: Begin actual wrapping live nonce boot \n
PSD3MACLength == (16)
%s: Finished eventCmdQueryInfo %d \n
formatAndStitchFiles
YonkersIR/YonkersIR4BinaryPlusHeaderPatch.FW
LeafSignature(Pre-validation):--------------offset = %d (%d)\n
Library-PearlFactory
YonkersIR1ChipID
start
eventCmdPerformNextStage
SavageAuthPubKey
_RightBcam
%s - YonkersIRxIsPresent[%d] = %d; chipID = 0x%04x\n
camChannel
%s: Begin reading info needed for provenance certification - %d\n
%s: Finished pre-wrapping \n
refFrameData
pathString
%s: Exiting execCommand: command = %s, result = 0x%X, numInstance = %d \n
%s: Extracting certification data is done with result = 0x%02X (tryAgain = %d) \n
YonkersIR/YonkersIR1BinaryPlusHeaderPatchCertification.FW
fileURL
YonkersIR/YonkersIR2BinaryPlusHeaderPatchFusing.FW
YonkersIR/YonkersIR2PatchAuthCertification.DAT
%s: Begin reading info needed for certification \n
JasmineIRIsProvisioned
JasmineIRUpdateController::eventCmdPerformNextStage: Begin actual wrapping live nonce boot \n
YonkersIR/YonkersIR2PatchProvCertification.DAT
%s: Send out the results in fOutput of the command processed\n
YonkersIR/YonkersIR4PatchAuthCertification.DAT
JasmineIR: Signed Certificate (TSS Response):-------------- Length = %d \n
YonkersIR2AuthPubKeyHmac
YonkersIR4
YonkersIR3MNS
%s [output]: %s %s \n
YonkersIR/YonkersIR2BinaryPlusHeaderPatchAuthCertification.FW
%s \n
%s: - result = 0x%08X (chipID = 0x%08X) \n
refFileName
YonkersIR/YonkersIR2PatchCertification.DER
YonkersIR/YonkersIR3PatchProvCertification.DER
YonkersIR/YonkersIR3BinaryPlusHeaderPatchProvCertification.FW
SavageUpdaterIsDone - no yonkersIRx controller instance
StripImg4
YonkersIR3AuthResponse
sensorIsProvisioned
numSensorInstance
JasmineIRUpdateController.cpp
%s - %p (%p) - UpdaterIsSupported = %d; SavageIsPresent = %d \n
%s: isProvisioned=0x%llX; isNGIDProvisioned=0x%X; isSocProdfused=%d; persoLoop = %d\n
err == 0 
DataDirectory
YonkersIR2AuthResponse
%sPubKeyHmac
YonkersIR/YonkersIR1PatchCertification.DAT
glenbrook
Verifying new reference frames info record...\n
replySize <= (16 * 1024)
AuthChallengeOption
YonkersIR/YonkersIR3PatchCertification.DER
YonkersIsYmgt
LeafSignature (Post-validation):--------------offset = %d (%d)\n
/SavageFullCert.DER
systemRootPath
dataInfo->setCount <= (4)
/System/Library/Pearl/ReferenceFrames
AppleCamera
%s: Begin Certification \n
YonkersUpdateController.cpp
```
