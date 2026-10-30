# `/usr/lib/libFDR.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 1,348,768 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 31 (Size: 3560)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (14)

- `/usr/lib/libFDR.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork (compatibility version 1.0.0, current version 3896.200.61)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libReverseProxyDevice.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/MSUDataAccessor.framework/MSUDataAccessor (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/AppleDeviceQuerySupport.framework/AppleDeviceQuerySupport (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (4,211)

First 2,500 of 4,211.
```
invalid implementation, impl->size is 0
AMFDRDataHTTPChallengeClaim failed
failed to write manifest
_AMFDRDecodeSearchEntryFromPropertyList
repairConfigurationEntries has wrong type '%@'
failed to load file %@, status %d
kAMFDRErrorMissingNonGeneratedData:Failed to fetch data for instances %@\nFailed to fetch multi-manifest for instances %@
amfdrCopy->optionsDict is NULL
signDataBool is required to true to sign base payload.
failed to init certificate sequence
Img4DecodeGetPropertyData(kFDRTag_SCDG) failed.
Skipping trust root check (trustobject unset)
_AMFDRDecodeVerifyChainOffline
implementation must be non NULL and signatureOid must be non NULL
Sign
entitlement is missing
sik-
_AMFDRSealingMapCopyAsidMetadataPrimaryModules failed
metadata is NULL
clientVersion is NULL
metaData is malformed: %@
oid too long
propertiesToExclude is not an array
supmSealingManifestData has wrong type %@
dataClassStr is not string
x-fdr-minimal-seal-version
Missing entitlement to allow server forbidden error
(NULL)
Failed to allocate dataClassesToCommit
_AMFDRSealedDataCreateSealingRequestInternal
AMFDRDataLocalMultiPatch
failed to decode metadata: %d
MissingMinimalManifests
0
AMFDRDataInstanceUseSikFormat
DataVersion
AssemblyID
Could not split key string
Primary module '%@' verification pass
AMFDRDataHTTPIterate
sikData is in malformed format
lakeville
CopyFromMappedFile
AMFDRRegisterModuleChallengeCallbackV2
ticket is not trusted
_AMFDRCopyChipIDNumberFromChipIDECIDDataInstance
No data instances to seal over but AP ticket allows incomplete data
AMFDRModuleCameraSensorAuthIsValid
manifest or object missing required property '%c%c%c%c'
AMFDRSealingMapCreateRepairConfigurationAsidMetadataInternalBlob
AMFDRPermissionsRequest
SealDate
failed to add subCC
AMFDRSetStat
Unable to load memoryStore data from %@
multiRequestErrors is NULL
seal
SrvT
PKI: verify cert was issued and signed by issuer (success)
Stations
payload valueData is NULL
AMFDRDataMemoryMultiMake is not implemented
AMFDRError
failed to allocate reStitchedManifest
AMFDRSealingMapCopyManifestProperties failed
failed to get instance of primary dataClass %@
metadataDict allocation failed
%@-%@ is missing but allowIncomplete is set, skip creating request of %@-%@ ...
optionsDict is not CFDictionary
UseFDRProductType
_AMFDRSealingManifestTrustEvaluation
data is empty
AMFDRDataVerifySealingManifest
failed to sign data %@:%@
AMFDRSealingMapCopyMultiInstanceAndInfoForClass
nonce
failed to verify test station signature, _checkVerificationError %@
sealNotIntended is true, skip to get minimal-manifest
apTicket is null
ignoring no trustobject error 0x%016llX
ChipID
AsidSubCCIdentifierList
Remote FDR Data verification failed.
kAMFDROptionMemoryStoreURL not set.
Unexpected error and underlying error for %@: %ld
propertyValueTypes is NULL
AMFDRDataLocalCreateDataWithManifestsInternal
outCryptoVersion is NULL
_Img4EncodeCreateUnsignedManifest
*outDigestSequenceDataLength is 0
options has invalid type
VerifiedProperties
failed to verify meta property
repairConfigurationContextSrc is invalid
Failed to allocate amfdr->memoryStore.
Failed to delete device manifest
cannot allocate dataClasses array
csrData is NULL
Failed to find adapter for clientid.
DeviceClass
FDR store size: committed %ld bytes, estimated %ld MB
Failed to allocation digest buffer
cannot get encode implementation
failed to decode all sequences: %d
Failed to allocate fullKeys
Failed to fetch trust object
dataArray is NULL
 tag=%@
___thr_AMFDRSavePersistent
Unsupported cryptoVersion %d to create CSR
_AMFDRSealedDataCreateSealingRequestInternal (Main) failed
AMFDREncodeMetaPropertyAddData failed 0x%X
AMFDRGetOptions
AMFDRDataLocalPatchCreateSignedData
_AMFDRSealingMapCopyMinimalManifestClassesAndInstances
dm/revert
Force commit is enabled, continue to commit data anyway
failed to query uniqueChipID
missing IM4C leaf public key OID
 pid=%@
AMFDRCryptoCopyAttestation
dataInstanceLength is not 0
https://skl.apple.com
Unable to extract trust object digest from AP Ticket
Could not get seal data instance
auth
AMFDRDataMemoryMultiExport
Could not find dataClass '%@' in sealing manifest, outDataInstance is NULL
dataClass or dataInstance is NULL
AMFDRSealedDataVerificationErrorIsBenign for PreSealing failed.
Img4EncodeCreateManifest returned an empty manifest
AMFDREncodeMultiResponseBegin
AMFDRSealedDataSign failed. Sealing failed.
Failed to convert %@ to a uint64.
callbackV2 is NULL
Local verification pass. Skip Auto Challenge Claim by Server, dataClass:%@, dataInstance: %@
_AMFDRSealingMapCreatePermissions
metadata key #%u is NULL
dataClass is NULL
outDataSignature is NULL
_AMFDRDataMultiPatchInternal
key is not a CFString
_AMFDRPlatformDefaultCopyRefKey
AMFDRSupportBase64Decode
certifyUrl is NULL
Failed to allocate sealedFullKeys
Could not query MobileGestalt for key '%@'
AMFDRSetComponentTypeForClassInstance failed
could not verify the local sealing manifest, skipping
malformed componentType: %@
_AMFDRIntraDataCopyAndCommitInternal failed but outError is NULL.
Could not send message size
amfdr->componentTypeDict is NULL
Could not get UniqueDeviceID
AMSupportCopyURLWithAppendedComponent failed
propertyValueLengths is NULL
<AMFDRLocalDataSignContext: dataClass: %@, dataInstance: %@, data: %@, assembly ID: %@, subCC digest list: %@>
decodeAlgId failed
DeprecateVersion1
AMFDRSealingManifestCopyMultiInstanceAndInfoForClass
BoardId
patchDict %ld is NULL
metaDataDict is of incorrect type
bytes not in binary range of data
Cannot convert versionOption
sikLength is 0
failed to allocate sequence/octet encoder
cannot convert subCCsToVerifyDigest to uint32_t ptr
failed to decode sysconfig payload: %d
Data
property %@ from sealing manifest has mismatched value %@, expected %@ (ignored)
SealedInstance
ignoring trust object mismatch error 0x%016llX
Remote FDR service returned %s
DEREncoderAddData failed for component index
Unable to read AP Ticket
trust verification error code=0x%016llX
malformed FDR Trust Object SslRoot, expected tag %c%c%c%c found tag %c%c%c%c
AMFDROfflineBlobCreate
Remote FDR Data verification success.
unsupported manifest version
malformed FDR Trust Object trusted, invalid trusted tag length
_AMFDRDecodeVerifySignatureDataWithOid
No trust object in options or in data store
AMFDRDataLocalCopyDataStoragePath
PKI: verify cert was issued by trusted key %d failed with error 0x%016llX
malformed dataInstance
PersistCookie
=
FDREncodeSealingRequest failed
failed to create csr context
Failed to export sealedData
discarded from
dictKeysBuffer allocation failed
AMFDRDataLocalPatchCreatePayloadAndDigest
AMFDRDataLocalDeleteExtraManifest
sikOverrideKey create failed
AMFDRDataLocalCopyManifest
propertyLength != implementation->digestInfo->digestOutputSize
Primary
Both '%@' and '%@' do not exist in sealing map entry
failed to convert PEM to DER: %d
bootManifestHash
AMFDREncodeMultiCombinedDataPayloadBegin failed 0x%X
AMFDREncodeMultiCombinedDataPayloadAddData failed 0x%X
Could not load sealing map
Failed to compute md5
subCC is not hashed
AMFDRSealingMapCopyMultiInstanceForClassWithOptions
Failed to allocate trust object digest data
CertifyRawECDSASignature
time
KeepExistingData
Img4EncodeCreateManifest failed %d
Skip verifying assembly identifier
Missing key '%@' in subcc list entry
_AMFDRSealingMapGetRepairConfigurationEntries failed
cannot determine paired SoC if sealedDataInstance is missing
MissingMultiManifests
AMFDRSealedDataSetDataClassInstance failed
non-sik
multiple entries for tag 0x%llu found, but no unique ID specified
trust object empty
AMFDRDecomposePermissionString
malformed kAMFDRCertifyComponentAttributeComponentIndex, expected CFData.
unexpected NULL dataValue
outerSequenceEncoder is NULL
_AMFDRDecodeInstPropertyMatching
Invalid data digest length: %ld
AMFDRSysconfigCreateFromData
mix-n-match not allowed
can't parse FDR Trust Object trusted key sequence
exeNode->dataClass is NULL
_stringTagToDERTag
Failed to fetch data for %@:%@.
unexpected property type != kImg4ObjectProperty
dataBlobs length does not match dataClasses
manifest
failed to allocate *outDataSignature
%@: Property is required
stationManifest is NULL
kFDRTag_asid doesn't exist, but this is allowed
ctx is NULL
Unable to create internal HTTP header extension dictionary
bagdemagus
AMFDRDataVerifyInternal
options is NULL
Failed to get value for property tag '%@', skipping.
primaryData for manp create failed
timeStr is NULL
AMFDRDataMemoryUpdateMetadataWithOptions is not implemented
amfdrRemote->optionsDict must be a CFDictionaryRef
AMFDRDataHTTPCreateMultiRequest failed
sealedData->dataArray is empty
3kmXfug8VcxLI5yEmsqQKw
assemblyID has invalid type
commandDict is NULL
UnverifiedCombinedManifests
AMFDRDecodeIterateTrustObjectTrustedBegin
Reading from Sealing Manifest
AMFDRDataMemoryMake
dataInstanceLength is 0
failed to add attestation
AMFDRDataCopyPayloadKeysFromData failed
%@:%@ make data failed - foundData is NULL
_AMFDRDataHTTPPatchInternal
Failed to allocate report
AMFDRSealedDataVerify failed but outError is NULL.
Library/Application Support/FDR
EffectiveSecurityModeSEP
_AMFDRDataPrepareRepairConfigurationContextSupmSetData for %@ failed 0x%X
FDREncodeCreateSignedData failed
AMFDRSealingMapCallMGCopyAnswer failed for %@, error=%@.
Unexpected type for property tag %ld
_AMFDRDiagnosticCopyComponentTypesInfoFromSealingManifest
metadata value #%u is NULL
failed to copy sysconfig entries
_AMFDRDataPrepareRepairConfigurationContextArrayData
AMFDREncodeRepairConfigurationBegin for Item failed 0x%X
malformed im4c tag: %c%c%c%c
Img4DecodeGetPropertyData(kFDRTag_SrvT) failed.
Illegal use of PrivateKey
can't parse FDR Trust Object SslRoot
malformed dataInstance, expected CFArray
asidExceptionDict has wrong type %@
dm/make
preflight
AMFDRCryptoCreateECDSADerData failed, status: %d
outVersion is NULL
failed to create boardTypeData
failed to create minimalSealingDataClassData
moduleDataInstanceStr is NULL
found clientid %@ for adapter %s
Img4DecodeGetPropertyData(kFDRTag_prid) failed.
failed to create currDataClassInstance string
separatedDataClassInstance is NULL
Local FDR Data found and verified, but Update Repair Configuration Asid Metadata requested.
FDREncodeCreateSignedManifest
cam-connections-scheme
publicKeyParam is NULL!!
Permissions request failed.
AMFDREncodeManifestContextCreateSignedManifest failed
AMFDRDataLocalPatch
Fail to export data %@-%@
outSignedValueDataDict is NULL
malformed dataClassInstance
AMFDRSealedDataRestoreOptions failed.
FDREncodeCreateSignedManifest failed %d
AMFDREncodeMetaPropertyAddData
SignData
failed to allocate mutableComponentTypes arrays
AMFDREncodeMetaPropertyBegin
memoryStoreDict is NULL
dataToStripLength is 0
inData must be non NULL and inDataLength must be non 0
failed to allocate data class/instance arrays
_AMFDRSealingMapCopyDataClassesAndInstancesInternal failed
discard %@:%@ from sealing manifest
x-fdr-message
en0
secondaryDataClass has wrong type %@
info allocation failed
DumpHttpBodyOnFailure
AMFDRDataHTTPPrefetch
MultiSealingMetadata
AMFDRDataMemoryMultiPatch
IODeviceTree:/arm-io/isp
publicKey must be non NULL and publicKeyLength must be non 0
AMFDRSealingMapCallMGCopyAnswer %@ for %@, error=%d.
Unable to create challengeDigest
failure
x-fdr-minimal-seal
statisticsArray is NULL
Invalid value '%@' (must be a CFString)
ForceUpdate
failed to encode payload #%ld: %d
AMFDRDataLocalMake
internalQueryCache allocation failed
metaDataToRequest is NULL
Primary module '%@:%@' verification failed
AMFDREncodeMultiRequestEnd failed 0x%X
amfdrRemote permissions changed. Old permissions: %@ new permissions %@
CertificateFile
+
gHttpRequestStatisticsArray is NULL
ExportAfterSealing
previous permissions request failed but supressed, not populating %@:%@ 
%@ is not in newMinimalSealingDataInstances
encodedManifest is NULL
encodedSysconfig is NULL
payloadValues is NULL
signedData is NULL
malformed format from AMFDRSealingMapCopyDataInstanceForSealingMapEntry, expecting CFArray or CFString
FDR failed to create SSO data. (ssoData is NULL).
_AMFDRSealingManifestSetSikOverride failed
invalid createECDSADerSignature: %@
malformed FDR Trust Object SslRoot, invalid trusted tag length
AMFDRSealingMapSetMGCopyAnswer
failed to add attribute value
failed to query chipID
failed to modify sysconfig
ComponentAttributeBatteryVersion
amfdrSource is NULL
kFDRTag_asid property != fdrDecode->assemblyID
failed to add SoCECID attribute
AMFDRDataMemoryCopy
_AMFDRDataCreateUnsignedValue
failed to encode sysconfig
Delete
Re-evaluation succeeded
AMFDRDataCopy failed, but ignoring verification failure.
magic size is invalid: %lu
valueDict key is not a string
dataClasses allocation failed
'%@' is missing
FDREncodeCreateOfflineSignedData failed
AMFDREncodeSubCCDigestsAddData failed 0x%X
malformed FDR2 Format (manifest2), expected tag %c%c%c%c found tag %c%c%c%c
dataClassesArray is NULL
primaryData for dcls create failed
_
AMFDREncodeProducerIDBegin failed %d
Create minimalManifestPropertyItems failed
onDeviceFDRProductType query failed
%@ %@
ClientId
bpub
failed to add data to subjectEncoder
*minimalManifestInstances malformed
PropertyIdentifier
UniqueDeviceID
TrustObjectDigest
minimalSealingDataInstances is NULL/malformed
mutableMetaDataDict is NULL
tagStr is NULL
Failed to enumerate path: %@
SOCKSProxy
Failed to create permissions string for data class '%@', data instance '%@', action '%d'
failed to verify img4 data for %@
-----END RSA PRIVATE KEY-----
Image4SecureBootCertificateFormat
iPhone17,4
failed to remove device manifest
StoreAsData
AMFDRSealingMapCopyLocalDataByPopulate
AMFDRSealedData.c
Unable to read AP Ticket but data verification is not requested
_AMFDRServiceCopySocketDict
ExportDataClasses
Failed to read memory data for key %@
failed to create payload digest
componentTypeStringData is NULL
AMFDRDataMemoryPut failed
metadataContext is NULL
Copy
_AMFDRDataDictMultiCopyInternal
failed to restitch device manifest
failed to sign data to put
valueToRequest is NULL
malformed kAMFDRCertifyComponentAttributeProductionMode, expected CFBoolean.
LiveInstance
remoteDataStore is null
System
x-fdr-client-id-sik
_addMetaDataRecord
exportLegacyData: kAMFDROptionExportLegacyDataClasses is not array
skip fetching all %d data classes
cannot create a separate amfdr object for data export
aks
PermissionsRequest
_AMFDRHttpMultiSealingCallback
SOCKSPort
mpub
AMFDRDataHTTPMultiSign(amfdrRemote) failed.
Failed to create permissions string for     data class '%@', data instance '%@', action '%d'
asidMetadata: %@
_AMFDRHttpMessagePreAction
failed to create internalCertificationOptions
Invalid amfdr object
ZhuGeCopyValue symbol is not supported
separatedAction is NULL
2.5.4.10
outReport is NULL
Invalid private key data type
AMFDRDataMultiMake got unexpected error
CryptoGenerateRSAKeys
can't parse content of MinimalManifestMetaData
Failed to create an unsealed manifest for multiple data
failed to extract sik from data instance
AMFDRDataHTTPRevert
AllowSealingWithMLBSerialNumber
Unexpected multi-sealing error from server: %@
_AMFDRDataPatchInternal
add version failed 0x%X
AMFDRDataCopySealingManifestProperty failed
subCC %@ is missing for %@:%@
AMFDRCryptoCopyRefKeyPub
AMFDRDataCreateSikInstanceString
unsignedManifestLength is 0
FDRSealedVerifyFail
Skipping scrt for %@
dataInstance has wrong type '%@
AMFDREncodeManifestContextAddImg4Context failed
can't parse FDR Producer ID sequence
AMFDRSealingManifestCopyMinimalManifestClassesAndInstancesVersions
No sealed key found and allowUnSeal is false
metadataKeys is NULL
Skipping file '%@'
action is NULL
sealedData->dataInstanceArray is NULL
AMFDRSetDigest
EnableStagedSealing
SealingUpdateRepairConfigurationAsidMetadata
%@ found in multi-response
MLBSerialNumber is required for sealing when allowSealingWithMLBSerialNumber is set
kIOReturnNotOpen
combinedData is NULL
subCCKey has wrong type %@
AMFDRDataCreateCombined failed
malformed FDR2 Format, expected tag %c%c%c%c found tag %c%c%c%c
CertifySignedCSR
keyBuffer is NULL
AMSupportDigestSha384 failed 0x%X
AMFDRSealedDataHTTPSign
FDREncodeCreateFDR2Data
missing multi request error
localSubCCList is empty
failed to decode FDR2 Format
_AMFDRPlatformDefaultCopyRefKeyAttest
version is undefined
Img4DecodeInitManifest failed
no uniqueID is specified, cannot verify kFDRTag_inst property
createSignedData failed
unexpected type for sealingMapSubCCList: %@
property %@ from sealing manifest has mismatched data (ignored)
%@:%@ get data failed - uncombinedData is NULL
AMFDRDataLocalPutExtraManifest
malformed FDR2 Format (manifest2), invalid tag length
Could not create patchItemKeysString
failed to parse property list
nonceSignatureBufferLength is 0
failed to obtain digests for patched data %@
AMFDRDataMemoryPutWithOptions
malformed kAMFDRCertifyComponentAttributeBoardType, expected CFString.
AMFDRDataMemoryCopy failed
Remote FDR Data sealing successful.
CLAIM
AMFDRDataLocalDelete failed
Failed to write extra station manifest
digestLength is %zu, expecting %zu
pidNumber is null 
sealing properties found : %@
AMFDREncodeMultiResponseEnd
AMFDREncodeRepairConfigurationAddData
partNumberStringData is NULL
topLevelSpec for payload is NULL
fail to add Sequence to manifestsSequenceEncoder
MissingDataInstances
AMFDREncodeSubCCDigestsBegin failed 0x%X
AMFDRSealingMapCopyLocalData returned error: %@
Could not create enforceDataInstanceString
AMFDRDataMemoryCopyDigest
SealedDataMissing
AMFDRDataCreateCombined returned combinedValueData == NULL
kFDRTag_cptp property != fdrDecode->componentType
MultiMake
_AMFDRHttpRequestSendSyncNoRetry_block_invoke
permissions request failed
Failed to allocate standaloneSealingMap
Unexpected populateInfo value
failed to add %s data
responseClaimData is NULL
<AMFDRLocalDataSignContext: (null)>
Img4DecodeGetPropertyData(kFDRTag_cptp) failed.
unexpected subcclist array type
refKey is NULL
trustObject is NULL
Cannot specify both %@ and %@ with value TRUE
missingDataIdentifiers allocation failed
EnableDigest
digest is invalid
failed to get CSR signature from offline blob
AMFDRDecodeIterateSysconfigBegin
com.apple.libFDR.persistent
outEncodedData is NULL
escapedDataClassStr is NULL
moduleRawPublicKeyWithPrefix is NULL
AMFDRDecodeIterateTrustObjectRevokedNext failed
version size is invalid: %lu
secondaryModules create failed
AMFDRCryptoCreateModuleSignedCsr
AMFDRSealedDataSetIntraFactoryDataClassInstance
asidMetadata updated successfully: %@
Missing data instances.  Sealing manifest will be %@ AMFDRSealedDataRef.
amfdr is not a remote store, skipped verifying digests
metaPropertyCallback failed with error 0x%llX
chipIDCString is NULL
digest still mismatched for %@:%@, discarding data
could not verify minimal manifest from the local sealing manifest, skipping
Invalid property length of kFDRTag_SrvT
context must be non NULL
%@:%@
AMFDRDataDecodeMetaProperty
secondaryDataClass %@ instance query failed but Allow Incomplete Data is set
_AMFDRSealedDataCreateSealingRequestInternal (MultiSealing) failed
AMFDRSealingMapCopyDataClassesAndInstancesWithAttribute
componentTypeDict queried from sealing map is %@
propertyTag has wrong type %@
FDR Product Type: %@
AMFDRDataHTTPCopy failed: outValueData is NULL
Failed to allocate dataDictArray
keyBufferLength is 0
Failed to verify offline blob
dataBlobs is NULL
CertifySikPub
AMFDRDataLocalCopy
InfoQueryOptionDataClassOnly
Found key %@ (trustError %@)
sock is -1
sealedData->dataClassArray does not match dataClassArray contents.
AMFDRDataMemoryPatch is not implemented
revocation check failed
/System/Library/FDR/FDRSealingMapRepairConfiguration.plist
_HttpRequestStatisticCreate
httpHeader is NULL
failed to encode data class
dataToSign must be non-NULL and non-0 length
Invalid kAMFDRDataClaimOptionDeviceOnlySigningDataClasses option is set
Empty img4 base payload is set
invalid inDataLength:%u
Required generated data missing from FDR DataStore, but may be generated at restore time.
AMFDRDataCopyRawAndFormatted failed, can't copy original data
failed to decode params
CertificateSigning
topLevelSpec for metadata is NULL
FDREncodeManifestObject failed
AMFDRDataMultiCopyDataForPatch failed for %@: %@
different length of dataClassesOverride and dataInstancesOverride
Attribute/
ChallengeClaim callback return NULL componentNonce
AMFDRSealingManifestCopyDataClassesInstancesAndProperties failed
AMFDREncodeRepairConfigurationAddSequenceWithKey
invalid optionsDict
invalid payload tag: 0x%llx
AMFDRSealingMapSetMGCopyAnswer: not supported on this platform
MultiPut
deviceRefKey->attestation is NULL
Invalid patchDictArray count
Could not get data instance for data class '%@'
attestation is NULL
cannot create a separate amfdrRemote object for challenge claim
failed to encode metadata key #%ld
dataClassesToReq is NULL
grammarID has invalid type
populateInfoDict is NULL
AMFDRDecodeImage4Certificate
counterSign is NULL
exportLegacyData: malformed dataClass
AMFDREncodeMetadataEnd failed 0x%X
Failed to fetch data for %@:%@, but it is not required for sealing
aks_ref_key_create failed : %d
failed to add attribute data
DeviceOnlySigning
Unexpected error and underlying error for %@: %ld, %ld
kIOReturnIOError
dataClass has wrong type '%@
context is NULL
AMFDRSealingMapAutoChallengeClaim
dataInstancesToRetry is NULL
AMFDRDecodeManifestBodyInfoNext
failed to get product type
AMFDRDataMemoryExport
failed to get cstring from key
kIOReturnNoResources
ComponentType/
requestDict is NULL
optionsDict is NULL
failed to parse ticket
Encountered '%@' data class twice
valueDict is NULL
kIOReturnNotAligned
Failed to get data instance or assemblyID for data class '%@', but unfused hardware is allowed
missingDataIdentifiers
array count is not equal to first dataInstanceArrayCount: %ld
ExtraSslRoots
AMFDRSealingMapPopulateSealingManifest failed: %@
localDataDirURL is NULL
PopulateIORegistry
metadata key #%ld is NULL
sealingIM4M is NULL
_AMFDRSealedDataCreateMinimalSealingRequestPreCheck failed
AMFDRDataMemoryMake is not implemented
<Sysconfig '%@'>{version=0x%08x}
ForceAllowSchemaMismatch
productInfoKey has wrong type %@
refPubKey is NULL
_AMFDRDecodeMultiSealingResposeRecords
failed to get digests from server
failed to allocate recordValueEncoder
originalData is NULL
Img4DecodeGetObjectPropertyData failed
AMFDRSealingMapSetSikOverride
Trusted
Found no data to seal over
failed to encode payload key #%ld
libFDR-??
key has wrong type %@
fdrDecode->uniqueID is NULL or 0 size
PrivateKeyFile
AMFDRDataHTTPPrefetch failed
en2
failed to copy payload data for %@-%@
Unable to create CSR RefKey signature
PermissionsRequestHeaders
organizationUnit is NULL
AMFDRSealedDataCreateSealingRequest failed. Sealing failed.
Invalid sealedData->multiSealingDataInstancesArray count
UpdateMetaData
AMFDRDataHTTPCopyManifest is not implemented
%lu
mutableMultiSealingDataInstances is NULL
AMFDRSealingMapCallMGCopyAnswerInternal
com.apple.libfdr.sealingMapRepairConfigurationCache
_CopyDevRefKeySignature
url is null
failed to create buffer from manifestEncoder.
Unit is not sealed
AMFDRDataLocalMultiCommitPatch
failed to find matching inst object propery, returning a mismatched one
data is unwrapped
No sealing map for this device
_AMFDRSealingMapCopyLocalMultiCombinedDataCopyPayloadAndSaveLocalSignContext
AMFDRSealedDataClearMultiManifest
invalid oid sub-identifier %s
outData array count is zero
dataInstanceToReq is NULL
mutableValue is NULL
AMFDRSealingMapPopulateMinimalSealingManifest failed: %@
kAMFDROptionSealingUpdateProperties is not array
Allow unsealed, just return true...
dataInstanceArray must be a CFArrayRef
AMFDRDataCopyPayloadKeysFromData
productInfoValue has wrong type %@
AMFDRDataLocalMultiPutWithOptions
_AMFDRDecodeFindDataFromMultiCombined
queryCache is NULL
success
_AMFDRDecodeTolerateErrorsForOptions
Could not get Sealed Data Instance
Properties
AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance failed for %@:%@
failed to restore amfdr options
_deleteUnverifiedDataInstance failed when deleting data %@-%@ with error 0x%016llX.
multiRequestContext is NULL
foundDataLength is 0
requiredSubCCs create failed
AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClass
failed to allocate sWithZero
AMFDREncodeSubCCDigestsEnd
AMSupportDigestSha384 failed to calculate subCCValue digest
Failed to copy subcc list
AMFDRDecodeMetadata
AMFDRSealedDataCreateSealingMetadata
unknown payload value type at #%ld: %lu
outBlob is NULL
AMFDREncodeMultiResponseAddRecord
failed to create outputData
failed to create repairConfigurationData
_AMFDRSealingMapCopyIntraFactoryClassesAndInstances failed
_AMFDRSealingMapCheckSubCCIntegrityInternal
AMFDRSensorAuthCertification
keyStr is NULL
Unable to create defaultPath
trustobject
AMFDREncodeProducerIDEnd
Cannot convert productInfoValue
Could not find key '%@' in sealing map.
createDataSignatureCallback is NULL
%@-%@:%@
Invalid dataInstanceArray count
metaDataKey is not supported: %@
GET
%@/%@/%@
minimalSealingDataInstance is not a string
Could not decode trust object (decodestatus=%llu)
productType has wrong type '%@'
%@ #%d is malformed
DisallowSealing
AMFDRSealedData
Failed to allocate memory for digests
invalid moduleChipName
manifest2 data is NULL
grammar hash mismatched, check the grammar ID
_AMFDRDataCopyUnCombinedValue
sealing map entry is NULL
dataInstanceArray allocation failed
certificate
AMFDRDeviceKey.c
Create mergeTags failed
Object of unexpected type '%@' for key '%@' in manifest property entry
saltWtihAttestationSignature has wrong type: %@
_AMFDRSavePersistentData
Remote FDR Data verification success against test station signature.
Failed to convert sealedDataInstance to CFDataRef
fullKeyStr is NULL
failed to parse local sealing manifest for seal date
Failed to get live data for '%@'
sealedData->sealingIM4M is NULL
moduleRawPublicKey is NULL
radomData is NULL
failed to create fullKey from %@, %@
Object of unexpected type '%@' for key '%@' in sealing map entry
AMFDRSealingManifestCopyInstanceForClass
/usr/lib/FDRSealingMap.plist
MultiRequestErrors not in userInfo
AMFDRDataMultiUpdateMetadataWithOptions - %@
_AMFDRDecodeVerifyData
failed to allocate outData
dataInstancesToReq is NULL
AMFDRDataMultiExport failed
failed to get property %@ from sealing manifest (ignored)
https://gg.apple.com
AMFDRDataLocalSign failed
trustObjectData is NULL
failed to get multi response for %@:%@
dataToEncode is NULL
failed to encode patch data %@
failed to encode manifest version
currentDevice has wrong type '%@'
x-fdr-metadata-authuserid
Failed to load FDR keys %d
_HttpRequestStatisticCreateString
kAMFDROptionApTicketAllowUntrusted is TRUE, implicitly trusting ticket.
%@:%@ is missing but multiRequestErrors is NULL
failed to allocate payloadEncoder
_AMFDRSealingMapVerifyAsidMetadata
Station AMFDRDataHTTPPut with sik format is forbidden. %@-%@
Remote FDR Data verification failure, attempting to seal.
permStr in amfdrRemote is NULL.
failed to create sealedDataInstanceData
%d %@
AMFDRDecodeIterateProducerIDBegin
MinimalManifestVersion2
ForceSealing
primaryDataClasses create failed
_AMFDRHttpRequestSendSync returned success but outError is not NULL
AMFDRSealingMapVerifySealingManifestPropertiesInternal reported error: %@
minor version not supported: 0x%x
optionsFDR is NULL
facf
AMFDRSealingMapCopyPropertyWithTag failed, %@
Failed to export data %@.
Verify success %@:%@
cannot find matched camera sensor info: (%@)
Remote trust object digest still doesn't match apTicket.
Skip optional data class '%@'
outSignedCsr is NULL
b64Metadata has wrong type %@
_AMFDRAPTicketHasBooleanEntitlement
Failed to delete unverified minimal manifests with error %@.
failed to convert value
failed to parse certificate property
_CopyCsrGidSignature
amfdr option is NULL
valueDictArray size is invalid
failed to create valueData
dataClass create failed
AMFDRDataLocalUpdateMetadataWithOptions is not implemented
_AMFDRHttpNonceSign
AMFDRDataMemoryCommitPatch is not implemented
invalid value of original item
Failed to get data instance array for data class '%@', but it's a non-PoR data, simply ignoring it...
clientID is NULL
Missing data to seal and incomplete data is not allowed
AMFDRDataCreateString
_AMFDRDataLocalPatchInternal failed
signatureLength is 0
AMFDRDataHTTPChallengeClaim cannot find the callback funtion.
CertifyComponentAttributesCriticalProductionMode
Failed to allocate privateOptions.
failed to allocate certificationRequestInfo
outProperty is null
failed to allocate sikOverrideDict
failed to copy optionsToSet
Could not get data instance for intra factory data class '%@'
PKI: verify cert %d was issued by cert %d failed with error 0x%016llX
AMFDRDataDecodeAndSetSealingManifest failed
; Domain=%@ Description=%@ code=%ld
got multiRequestErrors for %@
MismatchedProperties
value is NULL
RequiredSubCCDgst
_AMFDRApTicketPropertyCallback
add data class failed 0x%X
AMFDRDataLocalCreateFullKey failed for dataClass: %@, dataInstance: %@
CAURL
ExportLegacyDataClasses
primaryDataInstance: %@
vvvvvvvvvvvvvvvvvvvvvvvvv BEGIN httpResponse vvvvvvvvvvvvvvvvvvvvvvvvv
AMFDRSealedDataSetDataClassInstance
failed to add attribute octet string value
AMFDRCreatePermissionsString
failed to set metaData
internalError is NULL
x-fdr-retry-backoff
inData is NULL
Failed to allocate dataInstancesToCommit
dataArrayToPut is NULL
failed to parse manifest from combined format
signature must be non NULL and publicKeyLsignatureLengthength must be non 0
Cannot get property tag from entry %ld
failed to decode original data
failed to get instance of dataClass %@
unsupported multi action: %d
Unable to create HTTP metadata Headers dictionary
encodedSealedData is NULL
AMFDRSetOptions
failed to get data property from Img4 manifest, err %d
Img4DecodeGetPropertyData(kFDRTag_faic) failed.
_CFDictionaryAddDictionary
not verifying subCC payload, skip checking subCC digest
Object of unexpectedtype '%@' for key '%@' in intraFactoryDataMapEntry
failed to add CSR attribute (error %d)
Remote
malformed dataInstanceArray
subCC digest encoding failed for %@
CertificationCtx is NULL
%s: failed to parse AP ticket as Img4 manifest\n
dataInstanceArray is NULL
originalDataArray is NULL
com.apple.libFDR.httpRequestStatistic
Could not get data instance string for identifier '%@'
CFPropertyListCreateWithData returned NULL
x-fdr-csr-DataClassRequest
Remote FDR Data verification failed for %@.  (Data can be generated by restore, will not be recovered)
additionToCommit is NULL
malformed FDR Trust Object trusted, expected tag %c%c%c%c found tag %c%c%c%c
vvvvvvvvvvvvvvvvvvvvvvvvv END httpResponse vvvvvvvvvvvvvvvvvvvvvvvvv
AMFDRDataMemoryMultiCopyManifest is not implemented
failed to decode offline blob Format
unexepcted items in offline blob
found multiple entries that match, uniqueID is required in this case
1.3.132.0.34
AMFDRSealingMapPopulateSealingManifest failed on amfdrRemote
malformed kAMFDRCertifyComponentAttributeBatteryPackIdentifier, expected CFString or CFData.
_AMFDRSealedDataLocalSign
PopulateSysCfg
onServerAsidMetaDataDict has wrong type %@
dataClass should be *
BoardID
failed to create encoder
failed to add pubkeyOid
failed to add attribute data to set
data is missing but multiRequestErrors is NULL
valueDictArray is NULL
failed to certificate dictionary
Skip verifying type info
Object of unexpected type '%@' in sealing map
_AMFDRSealingMapCopyDataClassesAndInstances
rawDict is NULL
_AMFDRDataMultiPatchCallback
pidStr is NULL
SigningURL not found in optionsDict
intraDataClasses length (%ld) does not match intraDataInstances (%ld)
Failed to copy array
Img4EncodeStitchManifest failed 0x%X
count of separatedStrings is unexpected, metaDataValue is %@
FCAM-RGB
failed to convert uniqueChipID
OrganizationalUnit
invalid dataInstance
sikDigest is NULL
APTicket
malformed FDR Multi-Response Payload Format
failed to decode FDR Multi Combined Format
StoreMaxSize
AMFDRDecodeManifestBody failed
VerifiedData
extraProperties is NULL
AMFDREntitlementIsEntitled
Failed to populate local data
Buffer contains %lu unused bytes
_AMFDRDecodeSequenceString
failed copy subCCDigestDict from amfdrRemote to amfdrLocal
malformed dataClassInstance %@, cannot find sik prefix
permStringData is NULL
UniqueDeviceID is NULL
inOutHttpStatus is NULL
:sik-
Apple Inc.
failed to allocate missingSubCCList
base64EncodedNonceSignature is NULL
AMFDRDataMemoryRevert
metadataLength is 0
dataClassArray is NULL
failed to create outSignedValueData
Re-evaluation returned code=0x%016llX
Failed to allocate subCCListDict
moduleRawPublicKey has wrong type: %@
_AMFDRDataHTTPMultiCopyInternal
Unexpected error for %@:%@: %ld
dataLength is 0
kIOReturnCannotLock
CFNumberGetValue returned false.
_isLocalSign
signed section has an unexpected tag
FDR data trust evaluation failed.
cannot find subCC digest for %u
Failed to load sealing map on device
Failed to get data instance for intra factory data class '%@', but incomplete or unsealed data entitlement is present
CertifyHeaders
CertifyBase64
AMFDRDataHTTPExport failed
malformed kAMFDRCertifyComponentAttributeBatteryVersion, expected CFNumber.
FDRLocalVerifyFail
dataClass is NULL. Verification failed.
dataInstancesToVerify is NULL
amfdr->asidDict is NULL
failed to query dataInstance
ManifestVersion2
certificationCtx is NULL
Unverified data instances will be deleted
sortedMinimalSealingDataInstances is NULL
%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n
AMFDRCopyDeviceKeys() returned error %d
AMFDRDecodeIterateCertChainNext failed %d
AMFDRSealingMapCopyLocalMinimalManifestSubCCKeys
verifying meta property
AMFDRDataMemoryMultiCopyDigest
failed to allocate outerSequenceEncoder
AMFDRCreateWithImplementation
_AMFDRCopyFormattingDescription
verifyError is NULL
Verification success: '%@' = '%@'
x-fdr-retry-timeout
deviceRefKey->refKey is NULL
_AMFDRDataCopyUnCombinedValue failed
assemblyIDData is NULL
*pRepairConfigurationCollectionContext is NULL
errorCodeLength is not 1
dd/MM/yyyy HH:mm:ss zzz
AMFDRDeviceRefKey: %@
objTag is 0
currDataInstance is NULL
AMFDRDataLocalRevert
dm/updateMetadata
FDRTotalHTTPFailures
AMFDRSysconfig
trust evaluation on customized payload format requires a reStitchManifest
failed to add img4 data IM4M
AMFDRCreateDataSignature
Value in manifest property entry has wrong type
nonce is NULL
UnverifiedDataInstances
Unable to create apURL
2.5.4.11
_buildReportWithKey
AMFDREncodeMetadataBegin
2
AMFDRSealingMapPopulateMinimalSealingManifest failed on amfdr
cannot convert partialIm4mData to base64 string
multiSealingMetadataKey is NULL
RestoreOSBuild
Metadata must be SET Container
x-fdr-request-uuid
AMFDRDataHTTPPresent
exportDict is NULL
failed to add record key
INST
Using value %@ for key %@ from query cache
PREFETCH
AMFDRDataCreateFDR2Data
newGrmr %@ is set by option, new base payload will be created.
Evaluation returned code=0x%016llX, re-evaluate with FDR 1.0 format
x-fdr-paired-soc-chipid
AMFDREncodeMetaPropertyBegin failed 0x%X
failed to decode payload data as sysconfig format
create dcls failed
AMFDRDecodeIterateSysconfigPayloadNext
failed to HMAC sign
This device is not FDR supported
RSA Public Key SHA1
Permissions
amfdr options is NULL
FDR Trust Object digest mismatch.
malformed FDR Multi-Response Error Code Format
timed out waiting
sealedData->sealingManifest is NULL. Sealing failed.
failed to compute digest for %@:%@
AMFDRSetComponentTypeForClassInstance
AllowIncompleteData
AMFDRSealingManifestCopyLocalDictForClass
sealingMapEntry is NULL
and is NOT Apple signed.
_AMFDRSealingMapCopyIntraFactoryClassesAndInstances
AMFDRLoadMemoryStoreFromFile
malformed offline blob
DataClass
RequiredToPerformManifestCheck
failed to copy data for %@-%@, but data is allowed to be missing since skip sealing is enabled
malformed FDR2 Format, invalid tag length
AMFDRSealingMapCreateAndPopulateSealedData
___thr_AMFDRLoadPersistent
AMFDRDataHTTPPut failed
AMFDRSealingMapPopulateMinimalSealingManifest
x-fdr-partial-im4m
AMFDRDataCreateSikInstanceStringInternal
add type failed 0x%X
sealedData->sealingIM4M is not NULL
sealing manifest has expected property %@:%@
AMFDRDataMemoryExport is not implemented
AMFDRDataAppendPermissionUpdateAsidMetadata failed
sealedData->dataArray is not a CFArray
AMFDRSealingMapGetEntriesForDeviceInternal_block_invoke
local data dir enumerator is NULL
Failed to allocate verifiedProperties/failureProperties
AMFDRSetSubCCDigestsToVerify
_AMFDRDataLocalMultiCopyInternal
PKI: decoding trusted root %d failed with error 0x%016llX
outSealingManifest is NULL
kIOReturnNotWritable
AMFDREncodeCertificateRequestCreateUnsginedData
Record must be SEQUENCE Container
SysCfg
ssoData base64 conversion failed
AMFDRDataMemoryMultiCopyDigest is not implemented
failed to add metadata record value
Flushed memoryStore to %@
dcls
Failed to create tempMemoryStoreData
asid %@ missing but Allow Incomplete Data is set
Required Subcc data missing from FDR DataStore but Neither 'Allow incomplete data' nor 'Allow unsealed data' is present.
AMFDRDataApTicketCopyObjectProperty
CopyDigest
failed to copy #%ld to put
CertifySaltAttestationSignature
_AMFDRHttpAuthenticateSendSync
failed to copy patched digest and payload
%@: ApTicket is NOT trusted, %@
metaDataValue is malformed: %@
signedValueData is NULL %@:%@
subCC values cannot be verified for %@-%@
invalid fdrVersion: %d
AMSupportHttpUriEscapeString(%@) failed
No data found for asid metadata but faic is set. Skipping update asid metadata
AMFDRDataPopulate
tag is 0
values is NULL
FDR CA issuer is: %@
dataDict has wrong type %@
outRawData must be non NULL and outRawDataLength must be non 0
DERParseBitString(sig) failed
valueDict contains NULL value
AMFDRSealingMapCreateRecoveryPermissionsWithOption
%@ already in multiRequestErrors
invalid encoding: %@
Both '%@' and '%@' exist in sealing map entry 
AMFDREncodeMultiRequestBegin
property meta tag is NULL
failed to remove station manifest
DEREncoderAddSetFromEncoder failed
AMFDREncodeCertificateRequestAddSubject
Certificate Properties extension not found
%s returned status %d. ResponseBody: '%@'
Invalid metadataDictArray count
invalid challengeSupport128b: %@
%s failed to create DER file
DataStore
validation has invalid type
CertifyRawPublicKey
failed to create socECIDData
MinimalSealingManifests
failed to create dataClassStr
httpXHeaders is not dictionary
PKI: verify cert was issued by trusted root %d (success)
EarlyAccessConsistencyRequired
failed to add bmuIdentifierData value
_AMFDRDeviceRefKeyClassFinalize
Attribute must be set container. Found unexpected tag 0x%llu, skipping
AMFDRSealingMapCopyRequiredIdentifiers
fsca
deviceRefKey is NULL
supm data mismatched
_AMFDRSealingMapGetManifestPropertyEntriesForDevice_block_invoke
%@ : %@
FDREncodeSealedDataEnd failed
Payload version mismatch
failed to create dataInstanceStr
AMFDRDataHTTPCreateMultiRequest
CertifyNoClientID
LocalInstance
Failed to create outDataReport
dataInstanceArray is not a CFArray
kIOReturnNoMemory
repairConfigurationContext is NULL
amfdr->digestDict is NULL
FDR 3.0 Data can't be decoded!
urlStr is NULL
metaDataOptionsArray is NULL
Failed to populate raw data
subCCs is NULL
PKI: verify cert %d was issued by %d (success)
_AMFDRHttpAuthenticateSign failed
RefKeyBlob
cannot populate paired SoC if dataClassArray (%@) or dataInstanceArray (%@) is malformed
no available property tags found
AMFDRCryptoCreateCsrSignature
permissions request failed but supressed, mark %@:%@ as missing
Unexpected propertyTag type
FDR failed to get payload from multi combined data
mainManifest is NULL
Unable to create SSL Root Data
_checkVerification
_AMFDRDataHTTPPatchCreateImg4Callback
AMFDRSealedDataClearSealingManifest
AMFDRSealedDataConfigureOptionsForRecover failed.
metaValueDict key is not a string
failed to add actionCode
No FDR SSL root found
cannot create sysconfig from valueData
AMFDRDataLocalPutTrustObject
failed to decode sysconfig metadata: %d
found data in multi combined format
failed to decode payload: 0x%llx!
_AMFDRDecodeGetDataInfoCallback
en1
Ticket is not trusted.
_AMFDRSealingMapCopyDataClassesAndInstancesInternal
csrSign callback produced NULL signature
Cannot convert CFNumber %@
bdak
AMFDRDataMultiCopy failed but multiRequestErrors is NULL
AMFDRSetCopyMGOverrideCallback
AMFDRDataCreateInstanceString
payloadData is NULL
ZG:FDRProductType
_AMFDRHttpCopyPurpleReverseProxyInformation
AMFDRDataMemoryMultiCommitPatch is not implemented
failed to find MANB (manifest body) tag
failed to parse boolean: %d
will populate sealedData with sealing map since we have data class and instance override
Digest realm=\"%@\", nonce=\"%@\", salt=\"%@\", uri=\"%@\", response=\"%@\", qop=auth, cert=%@, componentSig=%@, componentNonce=%@
AMFDRDataHTTPLoadPersistent failed: %@
DEREncoderAddData failed for s
failed to get FDR data version
outAsidMetadata create failed
keyNameData length is not 4
_buildReportWithKey failed for %@: %@
FDREncodeCreateSignedManifest returned an empty manifest
componentType is invalid: %@
amfdrCopy is NULL
FDR failed to get restitched manifest from multi combined data
Force to check non-sik data
_AMFDRSealingMapGetManifestPropertiesEntries
Failed to allocate populateAdditions
mismatched digest for %@:%@, discarding data
_AMFDREncodeCreateProducerIDFromPEMCert
_AMFDRDataLocalSignContextToImg4Context
x-fdr-hardware-model
serviceStr is NULL
organizationalUnitData is NULL
AMFDRSealedDataCommit with amfdrLocal failed. Data Recovery failed.
%@ is missing but multiRequestErrors is NULL
metaValueDict is NULL
PKI: decoding trusted key %d failed with error 0x%016llX
amfdr/amfdr->optionsDict is NULL
failed to read cert from file
claimOptions is NULL
can't parse FDR property meta
invalid key length: %lu
sealedDataClass=%@ sealedDataInstance=%@ dataClassArray=%@ dataInstanceArray=%@ dataArray=%@
AMFDRSysconfigCreateEncodedKey
failed to add signatureOidParams
multiCombinedDataPayloadContext is NULL
unknown action type: %d
Matching
Unable to create localDataStore
x-fdr-retry-attempts
AMFDRDataHTTPMultiSign failed
_CreateComponentAttributeData
Failed to copy challenge callbacks
_AMFDRPlatformDefaultCopyDisposableKeys
failed to add data to pubkeyOid
Failed to malloc fdrDecode
manifestInfo is NULL
FailureReason
Failed to populate local data with manifests
Failed to allocate subCCdataClasses
application/x-pem-file
Malformed dataInstanceString '%@'
_getDataClassesAndInstances
DeviceManifest
Required data missing from FDR DataStore but either 'Allow incomplete data' or 'Allow unsealed data' is present in AP or Sealing Manifests.
MetadataRecord must be SEQUENCE Container
failed to compute digest %d
AMFDRDataMultiPatchWithOptions
dataInstancesOverride is not an array
_AMFDRHttpLogRequest
perform aes => %d (%s)
SEAL
_AMFDRCopyDataFromDeviceTree
patchDict is NULL
_AMFDRStringInstanceIsValid
RepairConfigurationAsidExceptionList
cannot allocate dataInstances array
_AMFDRDiagnosticCreateDataReport
x-fdr-libFDR-tag
MultiRequestBackoff
1.2.840.113549.1.1.11
_AMFDRDataCreateRepairConfigurationAsidMetadata
EnableSslValidation
AMFDRDataMemoryMultiPutWithOptions
metaValueDict contains NULL value
_AMFDRDataDictCopyInternal
Force commit is enabled, continue to populate data anyway
_AMFDRSealingMapVerifyAsidMetadataWithPrimaryModule
CreateRepairConfigurationAsidMetadata
dataClass %d is NULL
dataInstances allocation failed
Remote FDR Data verification success, but Force Sealing requested.
Floating point identifier '%@' is not supported
Failed to create amfdrMemory
primaryDataClassInstance create failed
failed to add pubkey data
APTicketAllowUntrusted
outImg4Blob must be non NULL and outImg4BlobLength must be non 0
failed to create multiManifestDataClass
metadata  value #%ld is NULL
dataClassData is NULL
Failed to create trustobjectDigestData
Failed to create AMFDRSealedData object
tempCString is NULL
_AMFDRDataHTTPMultiPatchInternal
FDREncodeCreateCombined: DEREncoderAddSequenceFromEncoder failed
no data instance is specified when looking for data in multi combined format
data size is 0, file %@
CFDataCreate failed for permCertDerData
Found sealing manifest: %@
DataFailedVerification
AMFDRSealedDataCommit failed.
FDR failed to create SSO data.
httpRequestData is NULL
MinimalManifestPropertyCheck
LocalValidation
_AMFDRSupportBase64Decode failed
AMFDRDataHTTPExport
AMFDRDataPutForRestore
_AMFDRDecodeVerifyCertIssuerInternal
fail to decode certificate of offline signing
AMFDRSealingMapCopySubCCNameListWithAttributeForSealingMapEntry
add productInfoKey %@ failed 0x%X
failed to allocate mutableDataInstances arrays
AMFDRDataGetSigningVersion failed
AMFDRDataMultiCopyDataForPatch
repairConfigurationMap has wrong type %@
Checking %@:%@ from sealing map...
currentDevice has wrong type %@
^^^^^^^^^^^^^^^^^^^^^^^^^ BEGIN httpRequest ^^^^^^^^^^^^^^^^^^^^^^^^^
valueData is NULL
malformed AttributeTypeAndValue format: %d
AMFDRSealingMapCopyManifestPropertiesForDeviceInternal
malformed export destination
FailureData
sealedData->dataClassArray is NULL
AMFDREncodeProducerIDAddDigest
FDREncoderAddSequenceProperty
create manp failed
Failed to commit local data
FDR failed to decode multi combined Data img4
No data instances to seal over but it's match attribute case
dm/bulk/data
_AMFDRHttpHandleHeaderMessage
malformed FDR Trust Object Format
AMFDRDecodeManifestBodyNext
SSL trust evaluation failed
Reading from FDR local data path
_AMFDRDiagnosticCopyComponentTypesInfoFromSealingMap
AMFDRDigestMd5
AMFDRClearMemoryStore
not allow unseal, shouldn't call this function
certificationOptions has wrong type: %@
1.2.840.10045.4.3.2
_AMFDREncodeCreateProducerIDFromPEMCert failed %d
multiDict is NULL
failed to convert digest string
Failed to populate extra device manifest
using custom CSR format
AMFDRDataCreateRepairConfigurationSupmdata failed
amfdr is null
oldPerm is NULL
AMFDRDataLocalDecomposeFullKey failed for '%@'
buffer_len is 0
optionsDict has wrong type %@
furei
malformed attribute: %d
Multi sealing require FDR 2.0
httpRequest is NULL
AMFDRDataMemoryCommitPatch
AMFDRDataMemoryMultiCopyAsidMetadata
mix-n-match-prevention-status
failed to init sequence
AMFDRSealingMapCopyDataClassesInstancesAndInfo
unescapedValue is NULL
outDerData is NULL
malformed kAMFDRCertifyComponentAttributeSoCChipIDECID, expected CFData.
sealingMapEntry malformed:'%@'
sealedData->dataClassArray length (%ld) does not match dataClassArray (%ld)
failed to add subject value
_AMFDRSealingManifestSetSikOverride
unsupported minimal sealing version
Unsupported tag found in manifest '%c%c%c%c'
'%@', '%@', '%@', '%@', '%@' not exists in sealing map entry
_AMFDRDataPermAllowed
OtherData
_AMFDRDataCopyFormatted failed with %@
kFDRTag_inst property != fdrDecode->uniqueID
_AMFDRSealingMapPrepareAMFDRForCopyLocalData
Missing multi-manifest: %@
AMFDRDataLocalDecomposeFullKey failed with %@
AMFDRSealingMapCallMGCopyAnswerDefault
AMFDRCryptoCreateFDRCsrContext
Data for %@:%@ missing, continuing.
AMFDRDataMemoryMultiUpdateMetadataWithOptions is not implemented
newOptions is NULL
AMFDRDataHTTPDelete failed
dataClassesToExport is NULL
AMFDRSysconfigCopyValues
%@.offline
AMFDRSealingMapCopyLocalMinimalManifestForInstance
malformed kAMFDRCertifyComponentAttributeSoCECID, expected CFString.
com.apple.libFDR.AllowIdentifierOverride
FDR failed to get payload type from multi combined data
sealedData->sealedDataInstance is NULL
ChallengeClaim callback return NULL componentSignature
AMFDRGetMemoryStore
FailureProperties
minimalManifestVersions must be a CFArray
DIGEST
add pdct inner sequence failed 0x%X
propertyTag '%@' length should be 4
keyLength is 0
offline signing public key length mismatch
AMFDRDataHTTPCopyTrustObject
_checkVerificationError %@
copyFDRSealingMapFromFilesystem
UseSOCKSPort
villanova
CombinedManifest
aks_params_get_der failed : %d
failed to decode property
dataClassArray has invalid element #%ld
ca/authorize
dataArray is not a CFArray
AMFDRDataLocalMultiExport
Failed to allocate %lu byte message buffer
_AMFDRDiagnosticCreateDataReport fail, error: %@
PKI: verify cert was issued by trusted root %d
CopyAllowOfflineSigning
AMFDRSealingMapGetEntriesForDeviceInternal
Sealing properties are empty.
serverURL is NULL
sealedData->dataInstanceArray length (%ld) does not match dataInstanceArray (%ld)
failed to parse im4c: %d
SealingUpdateDataClasses
Unable to create remoteDataStore
CertifyClassFKey
mutableOptionsDict is NULL
AP is in non-default demotion state, ignore sik verification
Failed to SikPub for data class instance '%@-%@', but SikPub is allowed to be missing if no sealing is intended
failed to decode hex string
mismatched digest for %@:%@, retry fetching manifests
AMFDRDataMultiMake
Failed to fetch intra factory data for instances %@\n
AMFDREncodeRepairConfigurationBegin for collection failed 0x%X
ProductType
SealingManifest
Could not skip data class '%@' without unsealed data entitlement
unknown repairConfigurationDataType %d
AMFDRGetSikOverride
failed to strip data for %@-%@
target class is NULL but instance is non-NULL
payload is not CFDataRef
ioreg entry %@ is not a CFData
_AMFDRDecodeIterateCertChainNext failed (first call)
RequireSubCCDigest
multi-response error %d without an error message
Domain=%@ Description=%@ code=%ld
failed to query local store max size: %@
localOptions allocation. Sealing failed.
_FDREncodeCreateDataFromOid
CopyManifest
AMFDRDataGetMinimalManifestVersion
dataClass length is invalid
ignoring raw error 0x%016llX
Error to create string from property data for %@
failed to add img4 data
recordSetEncoder is NULL
metadataOptions has wrong type %@
AMFDRDataLocalPopulate
x-fdr-client-id
HTTPMaxAttempts
malformed data instance %@
metadataLength is not 0
AMFDRGetInfo
amfdrRemote options is NULL
Recovery/verify success. Local store has %d entries.
_AMFDRDiagnosticCopySealedFullKeysAndProperties
sik_pub_key_len is 0
AMFDRDataLocalMultiExport is not implemented
The data instance %@ cannot be parsed
Missing key '%@' in sealing map entry
_AMFDRSealingMapGetRepairConfigurationEntries
sealingMapEntry for seal key is NULL
true
Failed to allocate entitlements
No SCDG in manifest, subCC digest missing
FDR error: %@
AMFDRSealingMapCopyAsidMetadataData failed
Could not find sealing map entry for '%@'
%@ is not entitled in AP ticket, derstat: %d entitled: %d
AMFDRSealedDataPopulate with amfdrRemote failed. Data Recovery failed.
DataClassesOverride
1.2.840.113635.100.6.8
payload value #%u is NULL
customCommonNameData is NULL
_AMFDRDataDictPutInternal
%@ data source took %lu ms to initialize.
internalHeaders is not dictionary
Failed to allocate localFullKeysToVerify/sealedFullKeysToVerify
memoryStoreDictURL is NULL
AMFDREncodeRepairConfigurationBegin for product info item failed 0x%X
yyMMddHHmmss'Z'
AMFDRIncrementStat
dataInstances is NULL
AMFDRDataMemoryMultiCopyManifest
AMFDRDeviceRefKeyCopyKeyBlob
_AMFDRDataCopyImg4Manifest failed
chipIDNum is NULL
outDataLength is NULL
valueLength is 0
MobileGestalt returned NULL for image4CryptoHashMethod
error %d found in multi-response for %@. no error message provided
AMFDRPlatformSetImplementation
Delete unverified data instance : %@-%@
MultiRequestErrors
SecurityDomain
subCC check failed for %@: %@
Intra factory data download and committed to local success.
Setting memoryStore on top of existing store with %d items.
%02x:%02x:%02x:%02x:%02x:%02x/%u.%u.%u.%u
formattedDict is uninitailized
AMFDREncodeMultiCombinedDataPayloadBegin
x-fdr-key-attestation
_FDREncodeCreateRandomNumber
missing public key algorithm parameter OID
httpStatus is negative
failed to allocate privateOptions
_AMFDRFinalize
AMFDREncodeProducerIDAddDigestFromData failed %d
failed to create componentTypeStr
Patched keys are %@ 
Invalid metaDataArray count
hasPKA is NULL
GrammarID
_AMFDRDataCreatePtrFromTagStringCFArray
Remote verification pass and unsealed data is allowed. Skip Auto Challenge Claim by Server, dataClass:%@, dataInstance: %@
AMFDRSealedDataSetSikOverride
Img4EncodeCreatePayload failed %d
sealedDataInstance is NULL
Failed to allocate dataClasses
asidMetadataInternalBlob create failed
productType %@ does not have repair configuration
x-fdr-chip-name
AMFDRSealingMapConfigSealedData failed.
version has wrong type %@
type != NULL
Failed to get data instance or assemblyID for data class '%@', but incomplete is allowed
No data classes to seal over but it's match attribute case
AMFDRSealingMapCopyDataClassesAndInstancesWithAttribute failed
OfflineBlobVerify
AMFDREncodeRepairConfigurationAddSequence
dataClassesChallengeClaim is NULL
AMFDRSealingManifestCopyDataClassesInstancesAndProperties
Failed to copy station manifest
_AMFDRSealingMapGetEntries
FDR Trust Object revoked public key found
kFDRTag_inst propertyValue (sik) != sikValue
AMFDRSealingMapCopyLocalDict
still missing device manifests: %@
permissionsStr is NULL
grmrData is NULL
SDOM
Malformed permStr '%@'
failed to copy original digest
data for %@ missing, but is not required for sealing.
;%@/%@:%@
payload value #%ld is NULL
failed to add %s string
actionCode returned is %d
assemblyID in option not equals asid in patchDict
Put
%@%@%@%@%@%@
amfdr->cert is NULL
Failed to compute digest of raw data.
Could not get value for identifier '%@'
failed to create data class instance data
Unexpected type for subCCDataClass: %@
aksStatus is %d
AMFDRDataAppendPermissionsString
subCC digest encoding failed for %@:%@
failed to add record value
Object '%@' has unsupported type and cannot be formatted as identifier
Successfully read %d bytes for AP Ticket
AMFDRWriteDataToFileURL
digestData is NULL
Failed to allocate manifestProperties 
intraFactoryDataMap is NULL
dataInstanceStr is of 0 length
kFDRTag_inst propertyValue missing expected -
_AMFDRDecodeVerifyDataCallback
verifying subCC, skip comparing digest of the entire data
AMFDRHttpRequestPrintGlobalStatistics
sikPubString is NULL
UserMetadata
outDerDataLength is NULL
multiResponseContext is NULL
AMFDRDataVerifyAndCopySubCCKeys
AMFDRDataLocalSignManifestForMultiData
malformed FDR Multi-Response Error Format
xcld
Failed to get digest from trust object
Failed to get proxy info for URL '%@'
ForceCommit
v12@?0i8
cannot set implementation for the duplicated amfdr object
Unable to populate apTicket for amfdrRemote
dataInstance is NULL
AMFDRDataPutWithOptions
multiResponseCallback failed with error 0x%llX
www-authenticate
dataClassStr %ld is NULL
Object of unexpected type '%@' for key dataClass, expected CFString
PATCH
signContextArray is empty
Missing data instances: %@
_AMFDRDecodeIterateCertChainNext failed (second call)
Failed to get digest from rawDataToSign
_CreateTruncatedTicket
FDREncodeCreateOfflineSignedManifest
Failed to get cert data from SSL root
subject: %s, issuer: %s
Failed to put data to memory datastore
uuidStr is NULL
No URL in request
FDR local data verification failed or sealedData is empty. Recovering from remote.
Failed to store remote trust object in local data store
Unverified minimal manifests will be deleted
'%@' manifest populate
DEREncoderCreateEncodedBuffer failed
outSignedValueData is NULL.
no subCC found
cannot create subCCData
Station AMFDRDataHTTPUpdateMeta with sik format is forbidden. %@-%@
AMFDREncodeMultiCombinedDataPayloadEnd failed 0x%X
malformed Img4 Manifest (version parse fail)
dataClassInstanceWithoutSikPub create failed
permission is NULL
cannot find a way to decide board revision
sik_digest is NULL
AMFDRDataLocalPresent
dataClassesOverride and dataInstancesOverride do not match
dataBlob is NULL
ComponentAttributeSoCChipIDECID
tag has wrong type %@
failed to delete data at %@
failed to initialize options
unsignedManifest is NULL
Invalid dataClassArray count
values has wrong type %@
queryCache allocation failed
CFStringCreateWithBytes failed for rawSealDate
metaValues is NULL
Failed to convert CSR to PEM format
dataInstancesChallengeClaim is NULL
AMFDRDecodeIterateProducerIDNext(first) failed with error 0x%016llX
outSealingMapRepairConfiguration has wrong type %@
http://gg.apple.com/fdrtrustobject
%@ #%d has invalid length
_Img4EncodeCreateUnsignedManifest failed
Sealing is not allowed if FDRAllowUnsealedData is enabled
dataClassInstance has wrong size '%ld
Missing SubCCData Instances, but incomplete and/or unsealed data is allowed.
AMFDRCopyDisposableKeys
failed to add key
malformed FDR Combined Format (DERFDRItemSpecs)
AMFDRSealingMapCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData
rawManifestData is NULL
metadata has wrong type %@
Failed to get data instance for data class '%@', but incomplete or unsealed data entitlement is present
keySuffix is malformed
Failed to load AP Ticket
Patch data can't pass grammar check
ptr is NULL
Payload type mismatch
Could not get sealingManifestData
AMFDRDecodeManifestBodyInfoGetComponentType failed
spub
failed to create currDataInstance
failed to copy dict for %@-%@
could not parse sealing manifest
_AMFDRDataLocalSignContextToImg4Context failed
failed to set patch data %@
dataClass is NULL. Sealing failed.
dataClass is not a CFStringRef: %@
Local data not sealed
Only supports remote amfdr
No data instances to recover
populate sealedData with sealing map, sealingManifestOverride : %@, forceSealing : %@, allowForbidden : %@, allowUnSeal : %d
DEREncoderAddSequenceFromEncoder failed
dataStoreType is NULL
strValue is NULL
Invalid type for '%@'. Expected CFBoolean.
cannot convert tag to CFData
propertyValue != fdrDecode->sealingManifestImg4.payload.hash
ExportDestination
dataToPatch is NULL
use default primaryDataInstance
AMFDRSealingMapRegisterCustomQueryProvider
AMFDRSealingMapPopulateSealingManifest
failed to allocate mutableDataClasses arrays
sdak
1.2.840.113549.1.1.1
WarningMessage
_AMFDRDataCopyImg4StrippedValue failed
AMFDRDecodeIterateProducerIDBegin failed with error 0x%016llX
AMFDRDataHTTPCopyTrustObject failed: outValueData is NULL
dataInstance is NULL. Sealing failed.
copyCurrentDevice
AMFDREncodeCreatePayloadAndDigest
_AMFDRDataCopyFormattedRawAndImg4 failed
Unable to load FDR trustObject data
fdrDecode is NULL
Both '%@' and '%@' exist in sealing map entry
CertifyPartNumber
1.2.840.113549.1.1.12
malformed dataClass
versionStr has wrong type %@
AMFDRDataAppendPermissionsString failed for seal
AMFDRSealingMapCopyLocalMultiCombinedDataAddDataClassWithMultiData
x-fdr-manifest-prop-mpub-key
innerHeaderKey is NULL
AMFDRDataCopy
failed to strip set from im4m signed section
versionOption is NULL
failed to add public key
brunor
manifestBodyInfo is NULL
AMFDRPermissionsRequest failed
*outDerDataLength is 0
AMFDRDataPut(%@:%@) failed.
key to encode is NULL
failed to encode patched data
kFDRTag_inst propertyLength (%d) != instLength (%zu)
kFDRTag_inst propertyValue != instValue
type
Could not find sealingMapProperties for '%@'
base64EncodedSalt is NULL
pdct
outSealingMap is NULL
internalHttpXHeaders is NULL
arrayCount is 0
Failed to allocate report.
AMFDRGetUnderlyingErrorCode
asidSeparatedValues has wrong type %@
base64Attestation is NULL
clearing expected kAMFDRServerErrorNotFound error
failed to obtain original digest
AMFDRSysconfigSetValues
AMFDRDataLocalPut failed
Mismatched properties: %@
dataClassInstanceToRetry is NULL
_AMFDRPlatformDefaultRefKeySign
_exportDataInstances
payloadKeys is NULL
_AMFDRDeviceRefKeyCopyFormattingDescription
FDREncodeSealingRequestEnd
Object of unexpected type '%@'
AMFDRSealingMapCopyPropertyWithTag
AMFDRDataMultiCopyAsidMetadata failed
separatedDataClass is NULL
_checkVerificationError
AMFDREncodeMultiCombinedDataPayloadAddData
data instance cannot be missing without kAMFDRDecodeOptionAllowNoDataInstance specified
manpCount cannot be zero
ClientCredential
Failed to copy station local scrt
Unable to get the sealing manifest
Failed to delete station manifest
failed to decode payload: %d
Auto Challenge Claim by Server, dataClass:%@, dataInstance: %@
_AMFDRSealingMapCopyIdentifierListForClass
'%@' manifest populate failed with error %@
_AMFDRSealedDataVerifyMinimalManifest
metadataValues is NULL
AMFDRPlatformCopyDefaultClientIdByECID
_AMFDRDecodeMultiResposeRecords failed with error 0x%llX
fdrSuccess is NULL
Found no live data match to sealed key '%@'
Unable to get trust object
Failed to allocate sealingMapEntryDict
_AMFDRHttpLogResponse
MetadataType
Station AMFDRDataHTTPMultiPut with sik format is forbidden. %@-%@
metaDataArray is NULL
AMFDRDiagnosticGenerateReport
%@ must be a CFURL
AMFDRDecodeCombined
AMFDRDataHTTPMultiDelete
bmuIdentifierData is NULL
_createFullKeysForDataInstances for required to seal ones failed
payload keys and values have different numbers
scrt
AMFDRCertificateSigningRequest
unexpected type of innerHeaderValue
uniqueChipID mismatched
Both callback and callbackV2 are NULL
_AMFDRSealingMapInfoSetValue
proxyInfo is NULL
populateAdditions is NULL
signing failed: signature is NULL
Skipping sealing property '%@' as specified.
outData is NULL
Img4DecodeInit failed %d
_CFDataCreateFromData failed for *outImg4Data
sealedData is NULL
AMFDRDataLocalCopyDigest
failed to query %@
kIOReturnNotReadable
AMFDRDataLocalCommit
payload sequence malformed for multi combined data
_AMFDRSealingMapGetRepairConfigurationEntryWithSealingMapEntry
%d
AMFDRDataApTicketIsTrusted
MinimalManifestVersion
asid
permStr is NULL
DEREncoderAddData failed for r
no data found for data class '%@-%@' skipping generate sealing request
kIOReturnLockedWrite
No SSL Root found in trust object
GrammarHash
AMFDRDataLocalMultiUpdateMetadataWithOptions is not implemented
cannot allocate action array
no sealing manifest in options
AMFDRDataLocalCreateMultiCombinedData
Not support for CFArray format in AMFDRSealingMapCopyInstanceWithIdentifiers
data for %@ is not optional if it exists in the manifest.
payload is invalid
_AMFDRSealingMapVerifyAsidMetadataWithPrimaryModule failed
committed FDR data (%ld bytes) has larger size than estimated (%ld MB)
remoteOptions allocation. Sealing failed.
failed to add csrSignature
failed to add pubkey algorithm
%@ is server signing only, skip claiming
failed to add subCC %@ for %@:%@
exportDestination is NULL
sysconfigRef is NULL
im4c
epochTimeNumber is null 
_AMFDRSealedDataExportExistingData
propertyDataArray is NULL
outData must be non NULL and outDataLength must be non 0
AMFDRHttpMessagePostAction failed: %@
CertifyClientId
AMFDRDataCreateFDR2Data failed
PutCombined
chipID mismatched
patchedDataDict is NULL
_AMFDRDecodeIterateCertChainBegin failed
AMFDRSealingMapCopyLocalSubCCKeys
AMFDRDataRevert return false
combinedData has size of 0
Failed to allocate privateOptions
CertifyURL
AMFDRCertificateSigningRequest() failed: %@
AMFDRSealingMapVerifySealingManifestPropertiesInternal failed, adding to dataFailedToReport list
Missing SubCCData Instances: %@
sealingDataInstance is not a string
kIOReturnInternalError
failed to add error value
AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo
message is NULL
ticketHash
SkipVerifySik
failed to read fdrProductType
AMFDREncodeRepairConfigurationBegin failed 0x%X
localSignContext->_subCCDigestObjPData is NULL
failed to delete manifest: %@
No data classes to seal over but AP ticket allows incomplete data
can't parse FDR Multi-response Metadata
/System/Library/FDR/FDRSealingMap.plist
x-fdr-metadata-
URL connection error occurred: %@
unexpected invalid hash
_AMFDRDecodeVerifyChain
AMFDRModuleCreateSignedCSR
failed to allocate path
failed to generate base dict value to patch
Failed to get value for property tag '%@' from FDR sealing property
Failed to compute digest of RSA Public Key
AMFDRDataLocalDecomposeFullKeyInternal
x-fdr-jmet-payload-dgst-expected
failed to add SocChipIDECID attribute
AMFDRDataMemoryCopyManifest
pManifestBodyInfo is NULL
multiRequestErrors is NULL or unexpected
%@ is not allowed. returning kAMFDRServerErrorNotFound
AMFDRSealedDataPopulate
AMFDRSealedDataRestoreOptions
PrivateKey
Could not get chipid string for identifier '%@'
Record value is NULL
EarlyAccess
failed to query sealed data instance for minimal manifest and incomplete data is not allowed
amfdr->challengeCallbacks is NULL
Failed to delete data class and instance with error %@.
1
This is a proto device that needs more permissive decode options...
data of kAMFDRSealingMapRepairConfigurationPdct has wrong type %@
FDRCAFail
dataInstanceToRequest is NULL
AMFDREncodeCertificateRequestAddAttribute
dataClassArray length (%ld) does not match dataInstanceArray (%ld)
failed to patch data for %@-%@
outManifest is NULL.
/mnt1/System/Library/Caches/com.apple.factorydata
failed to create img4 data: %d
sealedData->dataArray length (%ld) does not match countToSeal (%ld)
ChallengeClaim
failed to encode sysconfig sequence: %d
*outSealedDataLength is 0
%@-%@
metadataDict create failed
_AMFDRDataCopyImg4StrippedValue
%s returned status %d. x-fdr-message: '%@'
AMFDRSealedDataVerify with amfdrLocal failed after recovery. Data Recovery failed.
not found %@ in sealedData
FDREncodeCreateCombined failed
originalOptions is NULL
dataInstance is NULL. minimalSealing failed.
_AMFDRSealedDataCopyAndCommitIntraFactoryData
AppleKeyStore
failed to decode subCC digests sequence
FDREncodeSealedData: DEREncoderAddSequenceFromEncoder failed
multiUpdateMetadataOptions allocation failed
could not parse manifest
Failed to get trustObjData
asidMetadataInternalBlob has wrong type %@
_AMFDRSealingManifestCopyMinimalManifestClassesAndInstances
CopyTrustObject
failed to add isCritical property
Int64 property value is not the size of uint64_t
Set-Cookie
length of dataClasses and dataInstances are not the same
failed to compute restitched digest for %@:%@
dataClass cannot be empty
_AMFDRApTicketIsAppleSigned
AMFDRDataCopyAsidMetadataParameters
Will attempt to recover non-PoR data class '%@'
dataClass:%@ already exists, callbackV2 is updated
updateDataClasses is not an array
kAMFDROptionUseSikDataInstance is set to false
_createZhuGePreferences
^^^^^^^^^^^^^^^^^^^^^^^^^ END httpRequest ^^^^^^^^^^^^^^^^^^^^^^^^^
signatureDer is NULL
AMFDRDataHTTPMultiUpdateMetadataWithOptions
keyData has wrong type %@
ComponentAttributeProductionMode
sreqDataInstanceStr is NULL
outSignatureLength is NULL
no key to register
failed to decode sysconfig data: 0x%llx
SecKeyCreateRSAPrivateKey -> %p
unsupported encode type
FDRSealingMapRecover
sealedData->dataInstanceArray is not a CFArray
AMFDRGetCert
Primary module '%@' verification failed
AMFDROfflineBlobVerify
patchDict key is not a string
AMFDRCryptoCreateLocalSignedFDRCertificateData
failed to allocate sequenceEncoder
Img4EncodeCreatePayload returned an empty payload
failed to add value to collection sequenceEncoder for type %d
CFDictionaryCreateMutable failed for propertiesOverride
%@/%@
AMFDRSealedDataSign failed, but unsealed data is allowed. Sealing succeeded.
boolean entitlement query error, result: %@, error: %@
_isSealingClass
x-fdr-attestation
certifyHeaders is NULL
encodedItems for metadata is NULL
Failed to write extra device manifest
propertyInfo is NULL
_AMFDRHttpRequestSendSyncNoRetry
_AMFDRHttpMultiResponseCallback
_AMFDRDiagnosticCopySealDate
data is NULL
aries
%@:%@ get data failed - foundData is NULL
FDR Trust Object revoked client ID found
cannot allocate memory
outComponentType is NULL
infoKey allocation failed
failed to create innerHeaderValue
PropertyMismatched
sik is NULL
AMFDRDecodeMultiResponse failed
contentStr is NULL
AMFDRSealingMapCopyLocalMultiCombinedDataAddDataClass
_getMinimalSealingManifestDataInstances
.
APTicketAllowDigestMismatch
cannot find tag in property list
Failed to get data instance array for data class '%@', but incomplete or unsealed data entitlement is present
AMFDRSealingMapRecoverCurrentDeviceWithMemoryStore
manifestInstance is NULL
HardwareModel
failed to add data to attributeEncoder
failed to allocate publicKeyInfoEncoder
AMFDRDataLocalIterate
MinimalSealingManifest
deviceRepairConfigurationEntry has wrong type '%@'
send_message failed
_AMFDRHttpRequestSendSync failed
DEREncoderAddDataFromEncoder failed
CopyAllowRawData
failed to add signatureOid
AMFDRDataLocalPutWithOptions
FDR failed to get payload type
AMFDRSealedDataVerify failed without returning unverifiedDataInstances in outError
AMFDRDataHTTPMultiSign
failed to obtain valid patched digest and data
csrValueData is NULL
Found '%@' not sealed
MultiExport
failed to encode manifest tag
httpRequest allocation failed
_copySealingManifestProperty
unknown
AMFDRDataAppendPermissionsString failed
Less than 1 SSL Roots found
using default clientId: %@
;%@/Mothership
asidPatchDict create failed
permissions is NULL
AMFDRSealingMapVerifyAsidMetadataForDevice
TrustObjectURL
ALLOW
Required data missing from FDR DataStore but neither 'Allow incomplete data' nor 'Allow unsealed data' is present in AP or Sealing Manifests.
Outer DER did not terminate properly.
httpValue is NULL after _AMFDRSupportBase64Encode
AMFDRDataMemoryMultiPatch is not implemented
FDREncodeExtendedProperties failed
manifest or object property length does not match
_AMFDRDecodeVerifySubCC
fdrVersionNumber is NULL
Entitlements
failed to decode manifest: %d
secondaryData create failed
AMFDRDataHTTPCommit
Missing properties : %@
failed to create octet string data
dataToStrip is NULL
claimPermissions is NULL
fdrOptions is NULL
AMFDRSealedDataVerify failed with unrecoverable errors
AMFDRSealedDataGetSealingRequest
Cert rejected, attempting re-authentication.
failed to read cert data from %@. error %d
amfdr->infoDict is NULL
Unexpected type '%@' in sealing map
failed to allocate memory for AMFDRSealingMapCopyLocalMultiCombinedDataContext
Unable to get sik
failed to create separatedStrings
%@ failed to report what data is missing
dataClasses must be a CFArrayRef
use sik option defined by sealingMap
AppleDeviceQueryFramework ZhuGeCopyValue is unavailable!
Failed to get minimal manifest instance and data with error %@.
_AMFDRDiagnosticCopyLocalFullKeys failed, error: %@
kIOReturnBadMessageID
_getFDRSealingMapFromCache_block_invoke
failed to encode top-level metadata set: %d
AMFDRDecodeIterateTrustObjectRevokedBegin failed
Instance %@ is too long
IM4M %@ options.
dataToClaim is NULL
failed to get value of asid %@
primaryDataInstances create failed
_AMFDRSealingMapVerifyAsidMetadata failed
Failed to fetch data for %@:%@, but it may be generated by the restore
%@ raw data's digest mismatch, verification failed.
malformed metaProperty Format
Could not skip seal class '%@'
AMFDRDecodeManifestBodyInfoGetDataInstance failed
AMFDRDataHTTPMultiPutWithOptions
propertyTag is NULL
AMFDRDecodeIterateTrustObjectRevokedBegin
pairedSoCArray cannot be allocated
AMFDRGetSubCCDigestsToVerify
AMFDRAppendPermissionsString with ActionPUT sik instance for Claim failed
dataInstanceEntries count mismatch
FDRMissingDataInstance
AMFDRSetOptions(amfdrRemote) failed.
failed to create metaPropertyData
AMFDRDeviceRefKeyCopyAttestation
_AMFDREncodeCreatePayload failed to return a payload
valueDictArray has invalid element #%ld
Could not copy data for %@:%@
additionKeys or additionValues is NULL
valueDataDict is not NULL
Failed to locate new trust object
_InsertHeader
Invalid public key data type
AMFDRCryptoCreateDataSignature failed
failed to create minimalSealingDataInstanceData
AMFDRDataLocalEncodeImplementatation
malformed FDR Multi-Response value Format
AMFDRSealingMapVerifyAndCommitSealedData
\"
Skipping empty inner header
public key OID is not EC
No data to seal over. Declaring data verified.
HTTP request failed (status=%d)
AMFDRSealedDataCreateSealingMetadata failed
repairConfigurationContextDst is invalid
Erasing memorystore with %d items.
WriteUncached
_AMFDRDecodeVerifySignature
productType is NULL
primaryDataClass has wrong type %@
incomplete asidMetadata
result
_exportDataInstances failed with error %@
MissingSealingProperties
RequiredToSeal
Property tag '%@' in sealing map is not sealed.
metaDict is NULL
Local FDR Data verification failure, attempting to recover.
kFDRTag_inst propertyValue (sik) != instValue
Using %@:%@ from sealing map
keysToUpdate is NULL
AMSupportRsaCreatePrivateKeyFromPEMBuffer failed: %d
outContext->cryptoVersion is undefined
CFErrorCreate failed.
failed to decode public key: %d
failed to get attestation from offline blob
kFDRTag_inst property != fdrDecode->manifestUniqueID
%@:%@ is NULL
missing data storage path
AMFDRCreateError
dataClasses has wrong type %@
tagData length is not 4
Tag
User
sreq
lowercaseDigest is NULL
_AMFDRDataLocalMultiPatchInternal
queryCache has wrong type %@
repairConfiguration has wrong type '%@'
optionName is NULL
Unable to create outCert
Components
productInfoDict has wrong type %@
_AMFDRSealingMapCopyAsidMetadataPrimaryModules
mutableKey is NULL
Unable to create CSR GID signature
multiResponse is NULL
failed to parse AP ticket
_AMFDRDiagnosticCopyAndVerifySubCC
AMFDRSealedDataClear
repairConfigurationContext is invalid
items is invalid
FCAM IR
patchedPayloadDict is NULL
AMFDRDecodeCheckProducerIDRevocation failed with error 0x%016llX
malformed data instance for key '%@' in sealing map.
_AMFDRServiceSendSocketDict about to send %lu bytes.
_CFDictionaryAddDictionary fail to add dictionary
Failed to allocate dataIntanceToDelete.
Failed to allocate buffer
%@/Mothership
AMFDRCryptoCreateGenericCsrContext
aks_sik_attest failed : %d
sha2-384
AMSupportPlatformWriteDataToFileURLUncached failed %d.
Payload version is wrong size. got %zu expected %d
failed to create currentAssemblyID
AMFDRDataHTTPCopyTrustObject failed
newGrmr is set, but mismatch schema is not allowed
failed to allocate mutable copy of override data class/instance array
amfdrlocal permissions changed. Old permissions: %@ new permissions %@
SubCC data class in %@ is: %@
strippedDataLength is 0
dataclasses has wrong type %@
copied localData is NULL
Failed to populate sealedData from local data store. Data recovery failed.
AMFDRDataMemoryPatch
propertyTagValue has wrong type %@
AMFDRDataCopyTrustObject failed
failed to write data file %@, status %d
Img4DecodeGetObjectPropertyData failed for '%@'
instanceStr is NULL
LocalSigning
dataClassArray must be a CFArrayRef
_AMFDRSealingMapCopyAsidMetadataParameters failed
Value in key '%@' has wrong type
Failed to verify trustObject Digest
item is bigger on the inside
malformed FDR2 Format (manifest2)
CheckStoreSize
_AMFDRDecodeMultiResposeRecords
SkipRecoverDataClasses
_AMFDRSealedDataSealingPropertyCheck
sealingManifestData is NULL. kAMFDROptionSealingManifest not set in options, not stitching im4m
expectedDataArray is NULL
AMFDRDataUtilitiesCreateStringWithBytesNoCopy
amfdrLocal options is NULL
escapedDataInstanceStr is NULL
__AMFDRSealedDataPopulatePrivate
Verify property tag:%@ successfully
_CopyClientIdForAdapter
can't parse FDR Trust Object Revoked sequence
malformed cert property key length: %lu
AMSupportDigestSha256 failed
propertyValue must be non NULL with a non-zero length (length=%u)
x-fdr-metadata-ChipID
AMFDRDataVerifyImg4Integrity with %@:%@ failed
failed to create data instancestring for minimal manifest
AMFDRDecodeGetImg4Manifest
kAMFDRDecodeOptionManifestOnly, kAMFDRDecodeOptionSubCCOnly, kAMFDRDecodeOptionDataDigestOnly needs to be exclusive to each other
_AMFDRSealingMapEntrySetSikOverride failed
CFDictionaryCreate failed for '%@': %@
strippedData is NULL
FDR-CM-SSL-ROOT
AMFDRSealingMapCheckSubCCIntegrity
manifestDataDict is NULL
FDR Multi Combined Format unexpected tag: %llu
AMFDRSealingMapCopySubCCDataClasses
AMFDRDataHTTPMultiSign error [%ld] for %@: %ld
Error occured when populating AP ticket
SealingExcludeProperties
_isZhuGeLegacyAvailable_block_invoke
_AMFDRSealingMapCopyMinimalManifestClassesAndInstances failed
committed FDR data has larger size than estimated
non-sik AMFDRDataAppendPermissionUpdateAsidMetadata failed
aks_fdr_hmac_data
failed to add subject sequence
repairConfiguration has wrong type %@
AMFDRDecodeManifestBodyInfoGetDataClass failed
DEREncoderAddData failed for boardTypeData
Invalid context, expected AMFDRRef
AMFDRDataLocalDelete
malformed cert property key: %c%c%c%c
sig byte pointer is NULL
_AMFDRModuleCreateSignedCSR
exportLegacyData: Remote FDR Data %@ exported successfully.
AMFDREncodeRepairConfigurationBegin
_AMFDRDataMultiCopyCallbak
Img4DecodeGetPropertyData(kFDRTag_clas) failed.
Create amfdr failed
Could not find key '%@' in sealing manifest.
1.2.840.113635.100.11.2
CreateRepairConfigurationSupmData
AMFDRDataMemoryDelete failed
failed to add dataInstance
tmpDataClassInstance allocation failed
decode and copy payload keys for %@ failed
encodedMetadata is NULL
%@/%@:%@
ApTicket in amfdr->optionsDict is NULL
cannot get multiResponseErrors
AMFDRDecodeMultiResponse
can't parse MinimalManifestMetaData
DataInstanceIdentifier
Failed to store trustobject-current in local data store
CopyDefaultDataPath did not return a CFURL
invalid propertyTag '%@'
SrNm
amfdrLocal is NULL
malformed %@ in CSR format options
exportLegacyData: Failed to export legacy data %@.
failed to parse signed section sequence: %d
AMFDRDecodeIterateSysconfigMetadataNext
AMFDRDataMemoryMultiCommitPatch
AMFDRMigrateCredentials
failed to copy extra manifests
AMFDRDataMultiClaimWithOptions
unknown data type for the subCC value
Unable to clear localDataStore
dm/bulk/metadata
Reading AP ticket for entitlements
_AMFDRDiagnosticCreatePropertiesReport fail, error: %@
AMFDRDataLocalSign failed. Sealing failed.
AMFDRDataLocalMultiCopyAsidMetadata is not implemented
outData from AMFDRSealingMapCopyDataInstanceForSealingMapEntry is NULL
AMFDRSetMemoryStore failed.
EpochTime
failed to create buffer from encoder.
data for %@ does not verify, but is not required for sealing. Removing from local data store.
Img4EncodeCreatePayload failed 0x%X
failed to parse certificate dictionary
Waiting for response from FDR Service.
Could not determine if data directory %@ exists
inputData is NULL
unsupported public key length: %lu
_AMFDRDiagnosticCopyMinimalSealingManifestFullKeysForSealingMapEntry
AMFDRSealedDataPopulatePairedSoCs
AMFDRDataLocalCopyExtraManifest
kFDRTag_inst propertyLength (sik) (%d) <= instLength (%zu)
AMFDRSealedDataDelete
%s
AMFDRSealingMapCopyMinimalManifestDataInstancesWithAttribute
/
non-sik AMFDRDataMultiUpdateMetaDataWithOptions failed
failed to add data to certificationRequestInfo
com.apple.libFDR
_AMFDRDataPrepareRepairConfigurationContextPdct
FDR failed to decode manifestOverride
aks_ref_key_sign failed: %d
CFArrayGetCount(dataClasses) (%ld) != CFArrayGetCount(dataInstances) (%ld)
FDR Trust Object revoked certificate found
AttemptToRecoverNonPoRData
Unable to create csrDERData
Key is not required to seal
publicKeyParam is NULL
failed to allocate dstEncoder
malformed kAMFDRCertifyComponentAttributeBatteryVersion, batteryVersion = %@, batteryVersionValue = 0x%llx
grmr
Failed to get digest sha256 from trustObject data
AMFDRSealingMapVerifySealing returned success.  Local store has %d entries.
failed to allocate minimalSealedData arrays
StripImg4
base64CsrGidSignature is NULL
Failed to allocate currLiveFullKeys
Expected data type in sealedData->dataArray
FDREncodeCreateCombinedFast
dataClass:%@ already exists, callback is updated
%@:%@ Invalid type for rawValueData. Expected CFData.
unsupported meta property type
MultiSealing
EnableCookie
_AMFDRDeviceRefKeyCreateInternal
AMFDRAppendPermissionsString with ActionGET non-sik instance for Claim failed
failed to create dataVersion
Unexpected error=%ld to handle
grammarID:%@ is not same as grmrHashString:%@
_merge_dict_cb
AMFDRDataCommitWithPopulateAddition
End of Inner Sequence found, before any valid DER.
malformed FDR Combined Format (trustObject), invalid tag length
failed to copy data and save manifest for %@
failed to create compAttrDict
_AMFDRSealedDataCopyFormattingDescription
AMFDRCryptoCreateLocalSignedCertificateData
failed to add NULL pubkeyOidParams
value has wrong type %@
valueData is not NULL
CFStringCreateExternalRepresentation(assemblyID) failed
apTicket
dataToDecode is NULL
failed to add BoardType attribute
valueDataLength has size of 0
SSO enabled for data PUT
AMFDRDataLocalCopyTrustObject
Local FDR Data found and verified, but Update Property requested.
minimalManifestInstances array count is not equal to sealedData->minimalSealingDataInstances
_AMFDRSealingMapCopyMissingPropertyTags
Content-Type
Authorization
application/octet-stream
valueDataDict  is NULL or unexpected
AMFDRDataLocalUpdateMetadataWithOptions
Object of unexpected type '%@' in intraFactoryDataMap
img4.manifest.signed_section.length is 0
requiredDgstArray has invalid type
Failed to create FDR2 data
Could not get sealing map
clientIdSik is NULL
AMFDRDataMemoryMultiUpdateMetadataWithOptions
_AMFDRDataLocalCreateSubCCDigestObjP
mandev
use minimal set of FDR support, deviceSealingMap is '%@'\n
%lu bytes data found in multi-response for %@
clientId is NULL
malloc failed
invalid multi-request error code: %ld
LocalCopyForceBootedOSTrustObject
AMFDRDataHTTPPutWithOptions
validation failed for property 0x%llX
failed to find property tag 0x%llu
Skip copy data class '%@' with '%@' attribute
_CreateComponentAttributeData failed
verifying sealing properties against sealing manifest
error is NULL
failed to decode payload #%u: 0x%llx
AMFDRDataCopySslRoots
fdrProductType is NULL
originalData and expectedData are NULL
AMFDRDataStripExtraManifest
EarlyAccessMultiData
_AMFDRSealingMapInfoSetValue componentType failed
Digest realm=\"%@\", nonce=\"%@\", salt=\"%@\", uri=\"%@\", response=\"%@\", qop=auth, cert=%@
Missing minimal sealing instances: %@
FDREncodeSealingRequest
dataClassInstance is NULL
malformed skipDataClasses
AMFDRDeviceRefKeyGetPubKey returned NULL
Img4EncodeStitchManifest returned empty data
malformed FDR Combined Format, invalid tag length
AMFDRDataHTTPDelete
Failed to create csr, AMFDRCryptoCreateModuleSignedCsr failed.
AMFDRDataHTTPSign(amfdrRemote) failed.
instances is NULL
Attributes
EnableProxy
No cookie found
AMFDRDataMemoryDelete
RepairConfigurationAsidMetadata
AMFDRCryptoCreateSignedCsr
Local FDR Data found and verified, but data export requested (sealing skipped).
AMFDRCryptoCreateCsr
AppendComponentType
AMFDRDataGetSigningVersion
SealingPropertiesOverride
newGrmr %@ is set by option, but no Grmr in original data
_AMFDRDataMultiCopyInternal
_AMFDRDataCopyForPutWithManifest
x-fdr-patch-base-payload
https://ig.apple.com
Re-evaluation succeeded but decode options require version2
Opt to skip co-processor scrt
CertifyComponentAttributes
statisticsArray has %d requests
failed to created sealed data from input data store
AMFDRCertificationRequest
metadata key is NULL
rfcg
kIOReturnError
FDREncodeCreateSignedData
permissions allocation failed
ctx->amfdr is NULL
add productInfoValue of %@ failed 0x%X
_AMFDRVerificationErrorRemoteDataIsSealed
sealedDataClass is NULL
entryName is NULL
Cannot specify both componentAttributesCritical and componentAttributesCriticalProductionMode at the same time
minimalSealingDataInstance is malformed: %@
Missing key '%@' in manifest property entry
productInfoDict create failed
AMFDRDataHTTPSign
amfdr is NULL
failed to fetch trust object
basePayload is NULL
mutableMultiSealingDataClasses is NULL
_AMFDRSealingMapGetManifestPropertyEntriesForDevice failed
OID of %@ #%d is empty
_AMFDRCopySealingManifestObjectTag failed
got multiRequestErrors
command
_FDREncodeAddObjectProperties
no options in amfdr
Img4DecodeGetPropertyData(kFDRTag_inst) failed.
MultiDataInstanceIdentifierList
Value in key %@ has wrong type
FDR SSO function is NULL, SSO ticket fetching disabled.
_AMFDRPlatformDefaultHMACSign
sealedData->sealingRequest is NULL. Sealing failed.
minimalSealedDataInstances must be a CFArray
verifying minimal sealing manifests
dataInstance is not CFStringRef
failed to add attribute
multiErrors is NULL
Img4DecodeGetPropertyData(kFDRTag_asid) failed.
AMFDRSealingMapRevertCurrentDevice
Content-Length
metadataValue is NULL
_AMFDRDiagnosticCopyEntitlementsFromAPTicket
AMFDRSealedDataPopulate with amfdrRemote failed. Continuing since sealing is disabled.
multiSealingRequestErrors is NULL
responseParts is NULL
failed to preserve amfdr options
primaryModule create failed
metadataToRequest is NULL
MissingSubCCDataInstances
asidMetadata has wrong type %@
Unverified data instances: %@
kIOReturnNoDevice
failed to convert versionOption
Required
%@:%@ populate data failed - foundData is NULL
_AMFDRHttpRequestSendSyncNoRetry failed
ignoring incomplete subcc error 0x%016llX
serviceKeyStr is NULL
AMFDRSealedDataPopulatedFromManifest
metadata valueData is NULL
_AMFDRSetOptions failed
property is NULL
assemblyInstanceArray is NULL
Failed to set options on amfdr
apManifest is NULL
FDREncodeReStitchManifest
invalid items key or value found
dataInstanceArray CFArrayCreateMutableCopy failed
failed to allocate data classes/instances/missingDataIdentifiers
Failed to copy proxy information and proxy is enabled.
AMFDRSealedDataSetMinimalManifestClassInstanceWithVersions
AMFDRSealedDataVerify
Key '%@' length should be 4 for '%@' in manifest property entry
manifestProperties is NULL
Failed to copy data classes with attribute %@
fullKey is NULL
formattedDict is NULL
Invalid originalDataArray count
chain_blob must be non NULL and chain_blob_length must be non 0
AMFDRSealingMapPopulateSealingManifest failed
No data found for %@
Cannot convert dataVersionOption
AMFDRDecodeCheckCertRevocation
Img4DecodeGetPropertyData(kImg4Tag_DGST) failed.
Cannot verify subCC integrity for %@-%@
Export
AMFDRDataMemoryMultiDelete
failed to allocate *outData
TS2
AMFDRDeviceRefKeySign
Invalid kAMFDRDataClaimOptionServerOnlySigningDataClasses option is set
primaryDataDict has wrong type %@
AMFDRSealingMapCopyLocalMultiCombinedDataEnd
```
