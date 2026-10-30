# `/usr/lib/libFDR.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,348,768 bytes.

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
AMFDR
bagdemagus
AMFDRDataLocalMultiUpdateMetadataWithOptions
metadata  value #%ld is NULL
AMFDREncodeCertificateRequestAddAttribute
failed to find corresponding component type
validation failed for property 0x%llX
dataBlob is NULL
AMFDRSealingMapCopySubCCNameListWithAttributeForSealingMapEntry
statisticsArray is NULL
AMFDRDataMultiCopy got unexpected error
unsupported manifest version
info allocation failed
sealedData->dataArray length (%ld) does not match countToSeal (%ld)
Failed to delete unverified data instance %@ from local data store: %@
AMFDREncodeMultiRequestAddRecord
AMSupportX509CreateDerCertFromPEM failed %d
failed to convert chipID
TrustObject
Failed to load AP Ticket
_AMFDRDecodeVerifyChain
No data classes to seal over but AP ticket allows incomplete data
AMFDRSealingMapCopyManifestProperties
Failed to allocate dataClasses
AMFDRSealingManifestCopyLocalDataForClass
Could not send message size
CertifyCustomCommonName
en_US
fullKey is NULL
malformed FDR Multi-Response Error Code Format
Could not find tag '%@' in manifest properties
x-fdr-seal-version
AMFDRDataApTicketCopyObjectProperty
malformed cert property key length: %lu
Object of unexpectedtype '%@' for key '%@' in intraFactoryDataMapEntry
minimalSealingDataInstances is NULL/malformed
_AMFDRHttpRequestSendSync returned success but outError is not NULL
digest of provided ticket does not match boot manifest hash
AMFDRDataUpdateAsidMetadata
no data found for data class '%@-%@' skipping generate sealing request
manp
supmSealingManifestData has wrong type %@
Unable to create HTTP header extensiondictionary
organizationalUnitData is NULL
dataInstance is NULL. Sealing failed.
failed to encode metadata #%ld: %d
metaValueDict contains NULL value
valueLength is 0
componentType is invalid: %@
AMFDRSealedDataVerificationErrorIsBenign for PreSealing failed.
AMFDRSealedDataClearSealingManifest
metadataLength is not 0
memoryStoreDict is NULL
public key OID is not EC
_AMFDRSealingMapGetManifestPropertyEntriesForDevice_block_invoke
AMFDRDataHTTPChallengeClaim
Failed to allocate memory for digests
AMFDRDataGetMinimalManifestVersion
UnverifiedCombinedManifests
x-fdr-jmet-payload-dgst
v12@?0i8
AMFDRDataHTTPMultiMake
1.3.132.0.33
kIOReturnNotAligned
Could not combine '%@' and '%@'
RCAM
ExportLegacyDataClasses
Unable to create HTTP metadata Headers dictionary
populateAdditions is NULL
Failed to decode maxSizeNumber
%@ found in multi-response
can't get productType\n
grmr
end of trusted root sequence found root_cert=%d
AMFDRSealingMapCopyLocalDataForClass
AMFDRDataLocalExport
counterSign is NULL
permStr in amfdrRemote is NULL.
0
newGrmr %@ received from client doesn't equal oldGrmr %@
malformed offline signing public key tag
populate sealedData with sealing manifest, sealingManifestOverride : %@, forceSealing : %@, allowForbidden : %@, allowUnSeal : %d
Failed to compute digest for %s:%s
cannot create a separate amfdr object for data claiming
AMFDRDataLocalCopyDataStoragePath
RetryNumber
AMFDRSetOptions(amfdrRemote) failed.
Unverified combined data will be deleted
Unable to create internal HTTP header extension dictionary
malformed kAMFDRCertifyComponentAttributeComponentIndex, expected CFData.
aks_params_set_number failed : %d
Unable to get the sealing manifest
Failed to copy subcc list
kFDRTag_asid property != fdrDecode->assemblyID
property value needs to be CFNumber if attribute of StoreAsInteger was set
sealingMapEntry is malformed: %@
cannot allocate dataInstances array
CertifyNoClientID
AMSupportRsaCreateDataFromPem failed for permission cert
CertifyComponentAttributes
require remote data store
aks-client-queue
Failed to get cert data from SSL root
Unable to create SSL Root Data
keyData has wrong type %@
_AMFDRModuleCreateSignedCSR
AMFDRCryptoCreateSignatureCallback failed: %d
Matching
AMFDRSealingMapCopyDataInstanceForSealingMapEntry returned NULL
AMFDRSealingMapCopyLocalMultiCombinedDataAddDataClassWithMultiData
Could not create CFNumber for HTTP timeout.  Protocol default will be used.
Key is not required to seal
AMFDRDataLocalMultiCopyAsidMetadata is not implemented
asidSeparatedValues has wrong type %@
failed to extract sik from data instance
failed to created img4 for %@
fdrDecode->dataImg4.payload_hashed is false
_AMFDRDecodeGetDataInfoCallback
AMFDRSealingMapVerifySealing Failed to populate sealed data
unknown payload value type at #%ld: %lu
no uniqueID is specified, cannot verify kFDRTag_inst property
Overriding query for %@
_AMFDRSupportBase64Encode failed
failed to add record value
optionsArray isn't supported!!
failed to decode offline blob Format
Failed to recover required data from FDR DataStore with fatal error code: %ld
FDR-CM-SSL-ROOT
at least one data should be specified
AMFDREncodeSubCCDigestsBegin failed 0x%X
AMFDRSealingMapVerifyAsidMetadataWithPrimaryModule
ClientID extension not found
Could not get data instance for data class '%@'
No data instances to seal over but it's match attribute case
optionsFDR is NULL
AMFDRDecodeMetaProperty failed
numUnused != 0
PopulateSysCfg
AMFDRDataHTTPDelete
AMSupportPlatformWriteDataToFileURLUncached failed %d.
tag is 0
Record value is NULL
Failed to base64 encode
base64EncodedNonceSignature is NULL
Img4EncodeStitchManifest failed %d
_AMFDRDataMultiCopyInternal
options has invalid type
PopulateIORegistry
csrDerData has wrong type: %@
Failed to fetch intra factory data for instances %@\n
repairConfigurationContext sequenceEncoder is NULL
sealedDataInstance is NULL
%@ failed in attempt %ld, including for retry
%@: Property is required
decode error
Url
LocalInstance
unknown
amfdr->infoDict is NULL
AMFDRDataHTTPSign
AMFDRDataHTTPMultiExport
outContext->cryptoVersion is undefined
newGrmr is set, but mismatch schema is not allowed
SealingUpdateRepairConfigurationAsidMetadata
AMFDRCertificationRequest
_AMFDRHttpAuthenticateSendSync
failed to add metadata value
AMFDRSealingManifestCopyInstanceForClass
_AMFDRSealingMapInfoSetValue attribute failed
AMSupportHttpUriEscapeString(%@) failed
_buildReportWithKey failed for %@: %@
AMFDRSysconfigCopyValues
mutableOptionsDict is NULL
Failed to compute md5
AMFDRSealingMapCopyLocalData
AMFDRDataMultiCopy failed but multiRequestErrors is NULL
*outDigestSequenceData is NULL
outVersion is NULL
Could not createdataInstanceListString
x-fdr-client-id-sik
dataArrayToPut is NULL
RepairConfigurationAsidMetadata
MissingLiveData
failed to parse im4c: %d
kFDRTag_asid property length != fdrDecode->assemblyID.length
Re-evaluation succeeded but decode options require version2
Manifest
failed to get cstring from key
 pid=%@
Offline signing is not implemented in AMFDRDataLocalSignManifestForMultiData yet
AMFDRSealedDataCommit
unexpected subcclist array type
failed to allocate publicKeyInfoEncoder
property meta content is NULL
UseFDRProductType
tempURL is NULL
Failed to get trustObjData
AMFDRCryptoCreateLocalSignedFDRCertificateData
Missing SubCCData Instances: %@
AMFDRSetMemoryStore
Failed to convert sikPub to CFDataRef
kFDRTag_inst property == fdrDecode->uniqueID, found corresponding Data Instance.
failed to read cert from file
FDR failed to create SSO data.
AMFDRDataHTTPMake failed
failed to query chipID
Failed to get value for optional property '%@', skipping.
base64Attestation is NULL
outDataLength is NULL
Could not find key '%@' in sealing map.
AMFDRSetMemoryStore failed.
AMFDRSealingMapAutoChallengeClaim
sik AMFDRDataMultiUpdateMetaDataWithOptions failed
key is not a CFString
Found no live data match to sealed key '%@'
CLAIM
valueDataArray is NULL
additionToCommit is NULL
Trusted
com.apple.libFDR
Attribute must be set container. Found unexpected tag 0x%llu, skipping
EnableCookie
failed to encode signed section as set
Create minimalManifestPropertyItems failed
failed to certificate dictionary
not verifying subCC payload, skip checking subCC digest
_AMFDRDecodeVerifyData
FDR failed to get payload type
permissions is NULL
AMFDRSealingManifestCopyLocalMultiCombinedDataAddSubCCForClassWithMultiData
SigningURL not found in optionsDict
metadataDictArray is not supported for local patch
%lu
Station AMFDRDataHTTPPut with sik format is forbidden. %@-%@
count of separatedStrings is unexpected, metaDataValue is %@
manifestURL is NULL
inData is not CFData
cannot get data instances for %@, skip creating data blobs...
subCCLength is not 0
%@/%@:%@
failed to write manifest
invalid moduleChipName
CERTIFY
outChipIDNumber is NULL
TrustObjectURL
failed to read fdrProductType
dataClassStr is NULL
validation has invalid type
AMFDRSupportBase64Decode
malformed %@ in CSR format options
CFDictionaryCreate failed for '%@': %@
certificate data is invalid
Less than 1 SSL Roots found
dataClass create failed
FDR failed to get restitched manifest from multi combined data
subcc data %@ is not required for sealing, skip checking
AMFDRDiagnosticGenerateReport
intraDataInstances must be a CFArray
outSealingMapRepairConfiguration has wrong type %@
\n
kIOReturnError
_AMFDRDataLocalMultiPatchInternal
AssemblyID queried from sealing map is %@
x-fdr-csr-signature
bootManifestHash
localSubCCList is empty
cannot create a separate localDataStore for putting trust object.
GeneratedByRestore
populate sealedData with sealing map, sealingManifestOverride : %@, forceSealing : %@, allowForbidden : %@, allowUnSeal : %d
Revert
AMFDRSealedDataAddMinimalManifestClassInstance
IM4M %@ options.
AMFDRDataUtilitiesCreateStringWithBytesNoCopy
Could not split key string
failed to create filePath from %@, %@, %@
failed to obtain original digest
SysCfg
failed to create currDataInstance
keysToUpdate is NULL
callbackV2 is NULL
AMFDRDecodeIterateTrustObjectRevokedBegin failed
failed to compute digest for %@:%@
AMFDRDataLocalSignManifestForMultiData
AMFDRDecodeOfflineBlob
Put
 process=%@
metadata key #%u is NULL
AMFDRDataGetSigningVersion failed
subCC digest verified
SecurityDomain
_AMFDRSealingManifestSetSikOverride
mlb#
AMFDRDataMemoryRevert
failed to decode sysconfig metadata: %d
Data for %@:%@ missing, continuing.
HEAD
_AMFDRDataCopyImg4StrippedValue failed
keyNameData length is not 4
Cert rejected, attempting re-authentication.
kIOReturnNoDevice
Failed to verify offline blob
asid
failed to decode payload: 0x%llx!
propertyValue must be non NULL with a non-zero length (length=%u)
Invalid data digest length: %ld
AMFDRDataAppendPermissionUpdateAsidMetadata failed
Empty img4 base payload is set
digestLength is %zu, expecting %zu
assemblyInstanceArray is NULL
certificationCtx is NULL
csrSign callback produced NULL signature
unsignedManifestLength is 0
AMFDRSealedDataPopulateWithExistingData
Failed to delete data class and instance with error %@.
dataClassComponentType is NULL
Failed to get payload sequence and set manifest from multi combined data
Remote verification pass and unsealed data is allowed. Skip Auto Challenge Claim by Server, dataClass:%@, dataInstance: %@
dataClass is not CFStringRef
failed to convert versionOption
AMFDRSealingMapConfigSealedData
strArray is NULL
 tag=%@
MultiSealingMetadata
AMFDRDecodeIterateCertChainBegin failed %d
AMFDRSealingMapVerifyAndCommitSealedData
AMFDRSensorAuthCertification
failed to add signature
UseSikDataInstance
dataInstanceArray must be a CFArrayRef
grammarID:%@ is not same as grmrHashString:%@
failed to encode patched data
x-fdr-jmet-payload-dgst-expected
failed to add bmuIdentifierData attribute
CFNumberGetValue returned false.
Evaluation returned code=0x%016llX, re-evaluate with FDR 1.0 format
AMFDRDataHTTPMultiSign failed
_AMFDRHttpMultiResponseCallback
failed to add bmuIdentifierData value
dataInstance is NULL. MultiSealing failed.
clientId is NULL
Payload version mismatch
Could not create patchItemKeysString
kIOReturnNotPrivileged
kIOReturnIOError
failed to get data property from Img4 manifest, err %d
current
malformed FDR Trust Object, invalid tag length
No data was found for %@
CertifyRawPublicKey
failed to create dataClassStr
multiManifestData for %@:%@ missing, not commit this manifest
ForceAllowSchemaMismatch
failed to convert digest string
AMFDRDataLocalCopy
_AMFDRDataMemoryMultiCopyInternal
Failed to query product type
apTicket
blob is NULL
MemoryStoreURL
failed to create outputData
sealedData->sealedDataInstance is NULL
failed to add subCC %@ for %@:%@
AMFDRDataHTTPCopy failed: outValueData is NULL
_AMFDRSupportBase64Encode failed for permission cert
AMFDRSealedDataRecover
NeRD OS detected, digest mismatch is allowed
OrganizationalUnit
0123456789abcdef
primaryData for manp create failed
_AMFDRHttpMessageSendSync failed
kIOReturnNotWritable
amfdr->optionsDict is NULL
malformed properties
ioreg entry %@ is not a CFData
versionStr has wrong type %@
AMFDRDecodeManifestBodyInfoNext
optionsDict has wrong type %@
failed to create buffer from manifestEncoder.
ioreg entry %@ not found
can't parse FDR Trust Object Revoked sequence
_AMFDRDecodeFindDataFromMultiCombined
Failed to allocate subCCListDict
malformed data instance %@
AMFDRDeviceRefKey: %@
subCCDigestsContext is NULL
outDataSignature is NULL
no tags in tagArray, skipping...
Both '%@' and '%@' exist in sealing map entry 
AMFDRDataCopy
_AMFDRSealingManifestCopyDataClassesAndInstances
AMFDREncodeMetadataBegin failed 0x%X
EnableMultiRequest
metaSequenceEncoder is NULL
CopyAllowRawData
kFDRTag_cptp property length != fdrDecode->componentType.length
supm
SealingHeaders
ForceUpdate
DigestMismatchedDataInstances
AMFDRDecodeEvaluateTrustInternal
cannot create a separate amfdrRemote object for challenge claim
dataInstanceArray allocation failed
dataIndicesToRetry is NULL
topLevelSpec for payload is NULL
DeviceManifest
objTag is 0
failed to modify sysconfig
Invalid sealedData->multiSealingDataInstancesArray count
failed to generate base dict value to patch
cannot find tag in property list
AMFDRSealingMapCheckSubCCIntegrity
PersistIncompleteManifest
cannot create tagData
AMFDRSealingMapSetSikOverride failed
UseSOCKSPort
Failed to allocate dataClassesToCommit
multiRequestContext is NULL
_AMFDRSealingMapCopyAsidMetadataParameters
statisticsArray has %d requests
%@:%@ is missing but multiRequestError is NULL
*outCombinedData is NULL
grammarID has invalid type
System
adding %@ : %@ into array for multi instance
kAMFDROptionUpdateProperties is not array
AMFDRDataHTTPCreateMultiRequest
failed to copy patched digest and payload
AMFDRDataCreateCombined returned combinedValueData == NULL
Recovery/verify success. Local store has %d entries.
moduleDataInstanceStr has wrong type: %@
AMFDRAppendPermissionsString with ActionCLAIM failed
EnableDigest
Could not copy data instance for %@
RetryInterval
CertifyURL
*outDerData is NULL
Value of %@ #%d is NULL
Failed to allocate report
oldPerm is NULL
can't parse FDR Multi-response Metadata
_AMFDRDecodeSequenceString
failed to begin decoding trusted key
%@ manifest is missing but multiRequestError is NULL
HTTP server returned %d bytes of binary data. SHA256: %@
AMFDRSealedDataSetDataClassInstance
sealedData->sealingIM4M is not NULL
%@ is not in sealedData
AMFDRSealingMapCopyDataClassesAndInstancesWithAttribute failed
kIOReturnBadMessageID
failed to extract img4 data
AMFDRSealedDataRemoveMinimalManifestClassInstance
cannot create a separate amfdr object for data export
ca/authorize
pairedSoCArray cannot be allocated
failed to create data instancestring for minimal manifest
AMSupportDigestSha256 failed to calculate grmrData digest
failed to encode sysconfig
FDRSealingMapRecover
no data to verify digests
sik_pub_key_len is 0
missing data storage path
can't parse FDR Trust Object trusted sequence
httpStatus is negative
httpRequest allocation failed
moduleChipNameStr has wrong type: %@
Failed to allocate dataDictArray
sealingManifest is NULL
amfdrLocal options is NULL
asidMetadata: %@
moduleRawPublicKey has wrong type: %@
vvvvvvvvvvvvvvvvvvvvvvvvv BEGIN httpResponse vvvvvvvvvvvvvvvvvvvvvvvvv
failed to get value
buffer_len is 0
FDREncodeSealingRequest
ZhuGeCopyValue symbol is not supported
AMFDRDataHTTPCopy failed
AMFDRSealedDataMultiManifestPopulate failed
fail to add Sequence to manifestsSequenceEncoder
%@:%@
create manp failed
clientVersion is NULL
verificationDetails is NULL
FDREncodeExtendedProperties failed
ignoring trust object mismatch error 0x%016llX
2.5.4.3
Img4EncodeStitchManifest failed 0x%X
updateDataClasses is not an array
amfdr->cert is not a CFDataRef
Required apTrustObjectDigest from apTicket is NULL
iPhone17,2
AMFDREncodeMultiCombinedDataPayloadBegin failed 0x%X
Failed to malloc fdrDecode
_AMFDRSealingMapCopyMissingPropertyTags
no available property tags found
AMFDREncodeRepairConfigurationAddSequenceWithKey
amfdr and amfdrSource have different platform implementations
Put failed
failed to get value of asid %@
_AMFDRDataCopyImg4Manifest
VerifiedProperties
failed to convert value for %@-%@
PKI: decoding trusted key %d failed with error 0x%016llX
Sealing properties are empty.
copyCurrentDevice
\"
FCAM-RGB
GrammarHash
subCC %@ missing, skipping adding its digest
info is malformed
Failed to allocate subCCdataClasses
Unable to create CSR
1.3.132.0.34
can't parse DERDecodeSeqNext
digest must be non NULL and digestLength must be non 0
sealing map entry is NULL
Object of unexpected type '%@' in intraFactoryDataMap
Failed to get data instance for intra factory data class '%@', but incomplete or unsealed data entitlement is present
AMFDRDecodeCombined
Failed to get value for required property '%@' (ignored)
sealedData is NULL
AMFDRSealingMapCopyPropertyWithTag
valueDataDict  is NULL or unexpected
data is empty
failed to sign data to put
Could not copy data instance array for %@, array count is zero
OfflineBlobVerify
AMFDRDataHTTPRevert
cannot get multiResponseErrors
ZG:FDRProductType
failed to allocate dataToSign
AMFDRGetUnderlyingErrorCode
recordSetEncoder is NULL
Failed to create sealedData. Data Recovery failed.
;
Failed to allocate populateAdditions
AMFDRDataCopyPayloadKeysFromData
sdak
still missing device manifests: %@
AMFDRSealedDataSetRepairConfiguration failed.
encodedData is NULL
FDRCAFail
Setting memoryStore on top of existing store with %d items.
%@/*
separatedDataClass is NULL
urlStr is NULL
dataInstancesToVerify is NULL
Failed to get minimal manifest instance and data with error %@.
true
extraProperties is NULL
Missing data to seal and incomplete data is not allowed
sealingIM4M is NULL after call to AMFDRDataLocalSign. Sealing failed.
AMFDRDataCreateCombined
Unsupported tag found in manifest '%c%c%c%c'
fdrDecode is NULL
%@ is not allowed. returning kAMFDRServerErrorNotFound
AMFDRDataMultiPatchWithOptions
_AMFDRDecodeFilterDataInstanceCallback
x-fdr-internal-export-destination
OID of %@ #%d is empty
valueData is not NULL
encodedSealedDataLength is 0
AMFDRDataCopyExtraManifests
AMFDRDecodeIterateProducerIDNext(loop) failed with error 0x%016llX
MultiDelete
requestDict is NULL
dataClassArray must be a CFArray
Local FDR Data found and verified, but Update Property requested.
FDREncodeManifestObject failed
Failed to copy common name from certificate
outDecodedData is NULL
action is %d
_FDREncodeAddObjectProperties
UPDATEMETADATA
inOutHttpResponseData is NULL
AMFDRSealedDataHTTPSign
signatureDer is NULL
new grmr received from option is mismatched the grmr of data
AMFDRDataLocalMultiMake
Cannot verify subCC integrity for %@-%@
failed to create dataInstanceStr
invalid ECDSADerSignature: %@
%@ raw data's digest mismatch, verification failed.
valuesToUpdate is NULL
AMFDRDataLocalPatchCreatePayloadAndDigest
propertyTagValue has wrong type %@
AMFDRSealedData
failed to decode payload: %d
dm/revert
CertificateSigning
AMFDRSealedDataVerify
deviceRefKey is NULL
CombinedManifest
add type failed 0x%X
No data instances to seal over but AP ticket allows incomplete data
outData array count is zero
FDREncodeSealingRequest failed with manifest2
failed to add isCritical property
failed to restitch device manifest
Could not copy data for %@:%@
malformed im4c tag length: %lu
malformed dataClasses: %@, dataInstances:%@, componentTypes:%@
AMFDRSealingManifestCopyDataClassesInstancesPropertiesAndInfo
error %d found in multi-response for %@. no error message provided
Missing and/or unverified data instances in the local data store, but incomplete and/or unsealed data is allowed.
grmrHashString is NULL
AMFDRDataMultiCopyAsidMetadata failed
AMFDRDataHTTPCopyTrustObject failed: outValueData is NULL
sortedMinimalSealingDataInstances is NULL
failed to allocate encoded metadata #%ld
x-fdr-retry-backoff
SSO enabled for certification
AMFDRDataHTTPExport
AMFDRSealedDataGetSealingManifest
AppleKeyStore
FDREncodeCreateSignedData
SignData
property meta tag is NULL
AMFDRSealingMapCopyLocalDict
No cookie found
AMFDRDataLocalExport is not implemented
failed copy asidDict from amfdrRemote to amfdrLocal
AMFDROfflineBlobVerify
Invalid optionsArray or count
kIOReturnCannotLock
PATCH
_CFDataCreateFromData failed for *outManifest2
AsidSubCCIdOptionalVerifyList
_AMFDRSealingMapCopyLocalMultiCombinedDataCreateUnsealedManifest
outDerData is NULL
_AMFDRDiagnosticCopySealedFullKeysAndProperties
failed to add pubkey info
x-fdr-request-uuid
AMFDRHttpMessagePostAction failed
Invalid inputDataArray count
Failed to copy array
Unable to read AP Ticket
SealingManifestIsMinimal
AMFDRDataCopySslRoots
outProperty is null
ZhuGeCopyValueWithError symbol is not supported
CertifyChallengeSupport128b
_AMFDRPlatformDefaultCopyRefKeyPub
OtherData
AMFDRDeviceRefKeyGetPubKey returned NULL
failed copy componentTypeDict from amfdrRemote to amfdrLocal
failed to digest ticket, error %d, digestSize=%d
SecKeyCreateRSAPublicKey -> %p
invalid value of original item
AMFDRDecodeIterateTrustObjectTrustedBegin
malformed FDR Combined Format, expected tag %c%c%c%c found tag %c%c%c%c
could not verify the local sealing manifest, skipping
Failed to enumerate path: %@
validation failed for property 0x%llX - tag present
AMFDRSealingMapCopyMultiInstanceAndInfoForClass
_AMFDRSealingMapGetRepairConfigurationEntries failed
signatureDerLength is 0
kFDRTag_inst property != fdrDecode->manifestUniqueID
SikOverride
Primary module '%@' verification failed
FDRXFDRMessage
failed to decode as internal Sysconfig format
DSURL
multiSealingRequestErrors is NULL
AMFDRDataHTTPPut failed
failed to encode manifest tag
Failed to copy proxy information and proxy is enabled.
The digestValue length is not as expected.
AMFDRDataMemoryUpdateMetadataWithOptions
payloadValues is NULL
_AMFDRDiagnosticCreatePropertiesReport
subCCLength is 0
asidExceptionDict has wrong type %@
malformed format from AMFDRSealingMapCopyDataInstanceForSealingMapEntry, expecting CFArray or CFString
Unable to create offline blob
AMFDRDataHTTPMultiSign
:sik-
1.2.840.113635.100.6.16
AMFDRSetCopyMGOverrideCallback
Unable to get RefKey attestation
DeprecateV1
HTTPMaxAttempts
failed to create fullKey from %@, %@
_InsertHeader
AMFDREncodeMetaPropertyEnd failed 0x%X
FDREncodeSealingRequestEnd
inOutHttpResponseHeader is NULL
SubCC data class in %@ is: %@
partNumberStringData is NULL
AMFDRLoadMemoryStoreFromFile
%@:%@ is NULL
dataClasses has wrong type %@
Could not copy substring for data instance
Failed to allocate report.
Found intra factory data to download : %@
DumpHttpBodyLength
mismatched digest for %@:%@, discarding data
aks_params_get_der failed : %d
Invalid data class length
Failed to get value for property tag '%@' from FDR sealing property
fdrSuccess is NULL
_AMFDRSealedDataCreateMinimalSealingRequestPreCheck failed
en0
unexpected type sealingMapEntry: '%@'
DataFailedVerification
AMFDRSealedDataSetSikOverride
found multiple entries that match, uniqueID is required in this case
HardwareModel
1.2.840.113549.1.1.12
payload key #%u is NULL
%s
AMFDRDataDecodeAndSetSealingManifest
AMFDRDecodeTrustObject
FDR Trust Object digest mismatch.
AMFDRDataCopySealingManifestProperty failed for supm
failed to copy manifestOverride
dataClassesArray count is 0
exportLegacyData: kAMFDROptionExportLegacyDataClasses is not array
Evaluation returned code=0x%016llX, re-evaluate with FDR 2.0 format
missing required property %@
copied localData is NULL
!!!!!!!!!!!!!!!!!!!!!!!!!! Retries exhausted on attempt %d !!!!!!!!!!!!!!!!!!!!!!!!!!
AMFDRDataHTTPMultiDelete
discarded from
failed to encode payload #%ld: %d
AppendComponentType
x-fdr-paired-soc-chipid
_AMFDRDiagnosticCopyLocalFullKeys failed, error: %@
createCertificateCallback failed
dm/bulk/make
found, store in
deviceRefKey->attestation is NULL
dataToStripLength is 0
AMFDRDataVerifyInternal: AMFDRDecodeTrustEvaluation %@:%@ returned code=0x%016llX
kFDRTag_inst property != fdrDecode->uniqueID
no uniqueID is specified, but this is allowed, skip comparing kFDRTag_inst object property
_exportDataInstances
AMFDRDataLocalSign failed
failed to put patched data
chipIDNum is NULL
additionKeys or additionValues is NULL
AMFDREncodeMultiResponseAddRecord
%@:%@ get data failed - foundData is NULL
propertyTags is NULL
base64CsrGidSignature is NULL
CheckStoreSize
ccrsa_generate_key() -> %d
FDREncodeCreateOfflineSignedData failed
AMFDRSealingMapCreateAndPopulateSealedData
copyLocalMultiCombinedDataContext is not properly initialized, AMFDRSealingMapCopyLocalMultiCombinedDataBegin should be used
FailureProperties
verifying meta property
persisted in
AMSupportCopyURLWithAppendedComponent failed
dataClassInstanceWithoutSikPub create failed
aks_fdr_hmac_data
Cannot specify both %@ and %@ with value TRUE
Present
AMFDRDataGetManifestVersion
_AMFDRCopySealingManifestObjectTag failed
AMFDRSealingMapCopyLocalMinimalManifestForInstance
Malformed permStr '%@'
using custom CSR format
Sealing (force sealing or re-sealing) not allowed due to PR Doc setting, restore stopped as requested.
AMFDRDigestMd5
Failed to delete station manifest
Digest 
FDRSealingFail
Version2
EnableProxySsl
dataClass is not a CFString. Verification failed.
FDREncodeCreateOfflineSignedData
AMFDRSealingMapCopyAsidMetadataDataClassesAndInstancesWithPrimaryModule
x-fdr-manifest-prop-mpub-key
unsupported multi action: %d
callback is NULL
dataClassesOverride and dataInstancesOverride do not match
onDeviceDataClasses has wrong type %@
Missing SubCC for %@: required subCC: %@, existing subCC: %@, missing subCC: %@
HTTPBackoff
_AMFDRHttpMessagePreAction
AMFDRDataVerifyFDRProductTypeForDevice
salt is NULL
failed to strip set from im4m signed section (Next)
AMFDRDeviceRefKeySign
_AMFDRDataCreateUnsignedValue
CFStringCreateExternalRepresentation(dataInstanceData) failed
AMFDRSealedDataVerificationErrorIsBenign
FDREncodeSealedData: DEREncoderAddSequenceFromEncoder failed
MinimalManifestPropertyCheck
failed to convert value
Could not find sealing map entry for '%@'
_AMFDRCopyFormattingDescription
cam-connections-scheme
instance %@ has unsupported length
failed to created sealed data from input data store
sealingMapEntry is NULL
Unable to create HTTP header extension dictionary
AMFDRPermissionsRequest failed
got multiRequestErrors for %@
propertyValueLengths is NULL
failed to decode params
malformed FDR2 Format, invalid tag length
AMFDRSealingMapSetMGCopyAnswer: not supported on this platform
failed to allocate encoded payload data #%ld
AMFDRCopyDeviceKeys() returned error %d
FDREncodeCreateCombined: DEREncoderAddSequenceFromEncoder failed
The data instance %@ cannot be parsed
failed to create compAttrDict
AMFDRSealedDataPopulatedFromManifest
AMFDREncodeMetadataAddRecord
failed to copy #%ld to put
malformed FDR Trust Object Format
primaryDataInstance has wrong type %@
Waiting for response from FDR Service.
componentType is NULL\n
unexpected error code
entryName is NULL
Could not query MobileGestaltfor key '%@'
remoteDataStore is null
requiredDgstArray has invalid type
Record value must be OCTET_STRING
AMFDRAppendPermissionsString with ActionPUT sik instance for Claim failed
AMFDRAppendPermissionsString with %@ failed
Populate
AMFDRDataLocalMultiExport is not implemented
Could not find key '%@' in sealing manifest.
sealingMapRepairConfigurationURL has wrong type '%@'
AMFDRCertificateSigningRequest() failed: %@
payload key #%ld is NULL
missing unclaimed data %@
AMFDRDataCreateFDR2Data
lowercaseDigest is NULL
AMSupportDigestSha256 failed
missingDataIdentifiers allocation failed
outSignedValueDataDict is NULL
Patched keys are %@ 
Cannot convert versionOption
mandev
Failed to get data instance array for data class '%@', but it's a non-PoR data, simply ignoring it...
asid %@ missing but Allow Incomplete Data is set
x-fdr-minimal-seal
keyStr is NULL
AMFDRCryptoCreateLocalSignedCertificateData
_AMFDRCopyDataFromDeviceTree
signedCert is NULL
requestURL is NULL
invalid dataInstance
hash method is not sha384, using sha1
AMFDRDataApTicketIsTrusted returning true (Apple signed)
inputData is NULL
Unable to add sealing headers
using default clientId: %@
Verify property tag:%@ successfully
Could not load SealingMapRepairConfiguration from '%@'
nonce is NULL
sealedData->sealedDataInstance is not a CFStringRef
property %@ from sealing manifest has mismatched value %@, expected %@ (ignored)
kIOReturnUnsupported
Object of unexpected type '%@'
failed to copy optionsToSet
unexpected type for sealingMapSubCCList: %@
AMFDRDataHTTPMultiSign(amfdrRemote) failed.
allDict is NULL
failed to allocate attributeEncoder
rawData is NULL
_AMFDRSealingManifestTrustEvaluation
mutableValue is NULL
can't decode manifest from Img4DecodeInitManifest, but it might be multi-manifest
_AMFDRSealingMapVerifyAsidMetadata failed
Process
REVERT
_AMFDRDecodeSearchEntryFromPropertyList
AMFDREncodeMultiRequestBegin failed 0x%X
metaDataValue is malformed: %@
_getDataClassesAndInstances
AMFDRDataMemoryCommitPatch
Required data missing from FDR DataStore but neither 'Allow incomplete data' nor 'Allow unsealed data' is present in AP or Sealing Manifests.
AsidSubCCIdentifierList
failed to get CSR from offline blob
MobileGestalt returned non data or string for property key '%@'
MultiCopy
AMFDRDataCopyForPut failed
encodedItems for payload is NULL
dataClassArray length (%ld) does not match dataInstanceArray (%ld)
amfdr is not remote
data of productInfoKey allocation failed
MinimalManifestVersion2
Could not queryMobileGestalt for key '%@', expected CFArray
onDeviceFDRProductType query failed
URL connection error occurred: %@
AMFDRCryptoCopyRefKeyPub
clientID is NULL
exportDict is NULL
StationManifest
cannot create sysconfig from valueData
Failed to query manifest property entries
MissingMinimalManifests
sik instance %@ is too long
dictKeysBuffer allocation failed
cannot convert partialIm4mData to base64 string
AMFDRDataMemoryIterate
invalid encoding: %@
failed to copy dict value to put
FDR CA issuer is: %@
Unable to create amfdrRemote
Apple Inc.
metaDataDict is NULL
secondaryData create failed
CFNumberCreate returned false.
dataToClaim is NULL
Unable to extract trust object digest from AP Ticket
EarlyAccess
Failed to copy data classes with attribute %@
MultiUpdateMetaData
_
CertifySaltAttestationSignature
No implementation in AMFDRDataHTTP module
failed to allocate valueEncoder
sik
Failed to convert trust object digest to hex
PKI: verify cert was issued by trusted root %d failed with error 0x%016llX
sealingMapEntry for seal key is NULL
multiSealingMetadataKey is NULL
failed to query dataInstance
CFPropertyListCreateWithData returned NULL
UniqueDeviceID is NULL
kIOReturnExclusiveAccess
AMFDRDataAppendPermissionUpdateAsidMetadata
'%@' is missing
secondaryModule create failed
_AMFDRSealingMapCreatePermissions
metadataToRequest is NULL
_AMFDRDataHTTPPatchCreateImg4Callback
1.0
dataClassStr is of 0 length
_CreateComponentAttributeData
_AMFDRStringInstanceIsValid
subCC %@ is missing for %@:%@
_createManifestPropertyValueDict
sealedData->sealingManifest is NULL. Sealing failed.
manifest or object property length does not match
Could not get data instance string for dataInstanceIdentifier '%@'
Unable to create csrDERData
AMFDREncodeMultiRequestAddRecord failed 0x%X
AMFDRCryptoCreateCsrSignature
copyMGOverride failed
sealedData->dataArray is NULL
failed to query uniqueChipID
unexpected property type != kImg4ObjectProperty
UniqueDeviceID
trustobject
signed section has an unexpected tag
but is Apple signed.
AMFDRSealingMapVerifySealingManifestPropertiesInternal failed, adding to dataFailedToReport list
*repairConfigurationContext is NULL
dataInstancesChallengeClaim is NULL
malformed Img4 Manifest (version parse fail)
copyFDRProductType_block_invoke
unsignedManifest is NULL
failed to allocate pubKeyBlob
AMFDREncodeRepairConfigurationAddSetWithKey
AMFDRDecodeIterateSysconfigPayloadNext
v8@?0
got multiRequestErrors
Buffer contains %lu unused bytes
multi combined payload type is not mcmb
productType %@ does not have repair configuration
_getFDRSealingMapFromCache_block_invoke
_AMFDRHttpMultiSealingCallback
AMFDRSysconfig
stationManifest is NULL
malformed FDR Trust Object Revoked, expected tag %c%c%c%c found tag %c%c%c%c
can't parse FDR Producer ID sequence
propertyValue != fdrDecode->sealingManifestImg4.payload.hash
Staged sealing is not allowed
Skipping manifest check, missing required instances: %@
dataClassArray is NULL
Could not create dataInstanceListString
onDeviceMetadataArray has wrong type %@
Cookie
AMFDRDataLocalCopyDigest
Can't get C string from chipIDStr
permStringData is NULL
AMFDRPlatformSetImplementation
Failed to allocation digest buffer
offlineDataInstanceStr is NULL
patchedDataDict is NULL
failed to find matching inst object propery, returning a mismatched one
DEREncoderAddSetFromEncoder failed
AMFDRGetInfo
dataInstanceArray CFArrayCreateMutableCopy failed
kAMFDROptionUseSOCKSHost is NULL
Unexpected type for subCCListEntry: '%@'
AMFDRDecodeIterateCertChainNext failed %d
1.2.840.113549.1.1.5
KeepExistingData
instances is NULL
outSignedValueData is NULL.
CHIP
Skipping empty HTTP header
AMFDRDataDictCreateFromData
failed to create buffer from encoder.
Failed to allocate entitlements
error is NULL
APTicket
kFDRTag_asid doesn't exist, but this is allowed
encodedSysconfig is NULL
can't parse FDR Trust Object trusted key sequence
moduleChipName has wrong type: %@
FDRLocalDataMissing
missing public key algorithm parameter OID
Failed to allocate dataToReportArray
values is NULL
AssemblyID
AMFDRSealedDataVerify failed with unrecoverable errors
BoardId
com.apple.libfdr.customQueryProviderRegistryQueue
Missing value for key '%@' in sealing map entry 
AMFDRCreateTypeWithOptions
CFDictionaryCreateMutable failed for queryCache
AMFDRSealedDataPopulate with amfdrRemote failed with a fatal error
SealingPropertiesOverride
permissions allocation failed
failed to parse cert properties: %d
not allow unseal, shouldn't call this function
failed to read private key
AMFDREncodeMultiRequestEnd
lakeville
Unable to create apURL
AttemptToRecoverNonPoRData
Set-Cookie
SrvT
migrated %ld restore-time options
AMFDRDecodeMultiResponse
Failed to construct data instance for sealing map entry: %@\nContinuing anyway.
Failed to create sealing data class string from '%s'
repairConfigurationEntries has wrong type '%@'
local data dir enumerator is NULL
%@ is missing but multiRequestErrors is NULL
failed to set metaData
malformed FDR Trust Object SslRoot, expected tag %c%c%c%c found tag %c%c%c%c
failed to decode FDR2 Format
PKI: cert was not issued by issuer (subject != issuer)
_AMFDRDecodeVerifyChainOffline
_AMFDRSealingMapInfoSetValue componentType failed
Remote service returned error string: %@
unexpected type of innerHeaderValue
failed to add digest data
Img4DecodeGetPropertyData(kFDRTag_faic) failed.
copied dataInstance is NULL
Unexpected error for %@:%@: %ld
minimalSealingDataInstance is not a string
AMFDRDataLocalSign failed. Sealing failed.
Could not determine data directory URL
FDR failed to get payload from multi combined data
can't parse FDR Multi-response payload
AMFDRSealingMapRegisterCustomQueryProvider
metaDataArray is NULL
AMFDRCryptoCreateLocalSignedDataSignature
dataClass is NULL
dataClass:%@ already exists, callbackV2 is updated
Sending command dictionary to FDR Service.
kIOReturnNotReadable
sikLength is 0
primaryDataClass %@ instance query failed but Allow Incomplete Data is set
_Img4EncodeCreateUnsignedManifest failed
non-sik
failed to create currentAssemblyID
Could not get data instance for intra factory data class '%@'
_AMFDRSealingMapCopyLocalMultiCombinedDataCopyPayloadAndSaveLocalSignContext
AMFDRDataHTTPDelete failed
Failed to get data instance or assemblyID for data class '%@', but it is non-PoR, simply ignoring it...
sealedData->dataClassArray is not a CFArray
DEREncoderAddSequenceFromEncoder failed
failed to add csr version
LocalValidation
malformed FDR Combined Format (trustObject)
AMFDRDataCreateRepairConfigurationAsidMetadata failed
DEREncoderAddData failed for socChipIDECIDData
sealedDataClass must be a CFString
%@ raw data's digest match.
CFStringCreateExternalRepresentation(assemblyIDData) failed
AMFDREncodeSubCCDigestsEnd failed 0x%X
sock is -1
serviceStr is NULL
%@/%@
_AMFDRHttpRequestSendSync
AMFDRCryptoCreateDataSignature
CopyDigest
RequiredSubCCDgst
subCCKey has wrong type %@
_AMFDRDataMultiCopyCallbak
ManifestProperties
Primary module '%@:%@' verification failed
AMFDRSealingMapVerifyAsidMetadataForDevice
IODeviceTree:/arm-io/isp
_addSealingMapEntryKeyValueToCache
httpRequestData is NULL
%@ : %@
_AMFDRDataClaim failed
permissions request failed
sreq
AMFDRDataLocalCopyExtraManifestPath
failed to  create data instance string
AMFDREncodeMetaPropertyAddData failed 0x%X
metaDataKey is not a CFString
Object '%@' has unsupported type and cannot be formatted as identifier
Unexpected error and underlying error for %@: %ld
Img4DecodeGetPropertyData(kFDRTag_asid) failed.
_AMFDRDecodeCombined
Failed to find any of the subCCs: %@ from %@:%@
Failed to allocate currLiveFullKeys
metadataKeys is NULL
dataInstanceToClaim is NULL
allowSchemaMismatch has invalid type
dm/bulk/data
%@ is server signing only, skip claiming
malformed dataClassInstance
localDataDirURL is NULL
sealedData->dataClassArray length (%ld) does not match dataClassArray (%ld)
CertificateSecurityMode
digest still mismatched for %@:%@, discarding data
multiCombinedDataPayloadContext is NULL
%s failed to create DER file
AMFDRDataCopyRawAndFormatted
amfdr option is NULL
pHttpResponseHeader is invalid
signatureLength is 0
type != NULL
AMFDREncodeRepairConfigurationAddSequenceWithKey failed 0x%X
kAMFDROptionApTicketAllowUntrusted is TRUE, implicitly trusting ticket.
Cannnot store combined data to remote data store
add sequence with key %@ failed 0x%X
x-fdr-message
AMFDRDataHTTPCopy
Value of %@ #%d is malformed
Remote trust object digest still doesn't match apTicket.
CopyAsidMetadata
cannot get encode implementation
malformed skipDataClasses
failed to allocate rWithZero
AMSupportRsaCreatePrivateKeyFromPEMBuffer failed: %d
AMFDRDataAddDataClassesToClaim
failed to decode all sequences: %d
Records must be SET Container
multi-response error %d without an error message
AMFDRDataHTTPPrefetch failed
DEREncoderAddData failed for batteryVersionData
dataInstanceData is NULL
_AMFDRSealedDataLocalSign fail
PUT/%@:sik-%@-%@
_AMFDRHttpRequestSendSyncNoRetry
^^^^^^^^^^^^^^^^^^^^^^^^^ MultiRequest attempt %u failed, sleeping for %d seconds ^^^^^^^^^^^^^^^^^^^^^^^^^
1.2.840.113635.100.6.74.4
Entitlements
unknown data type for the subCC value
extraOptionsCopy is NULL
SealDate
failed to create subCCReportDetails
AMFDRDataMemoryDelete
_aks_operation
AMFDRDeviceRefKeyCopyKeyBlob
gHttpRequestStatisticsArray is NULL
minimalManifestInstances array count is not equal to sealedData->minimalSealingDataInstances
strippedData is NULL
AMFDREncodeMetadataEnd
asid subCC data != fdrDecode->asidSubCCID
Value in key %@ has wrong type
cryptoVersion is undefined
Remote
ctx->amfdr is NULL
failed to copy data for %@-%@
fdrData
failed to compute restitched digest for %@:%@
FDREncodeSealingRequest failed
AMFDRSealingMapCopyDataClassesWithAttributeInternal
Data
FDR Trust Object revoked certificate found
MinimalSealingManifest
Key '%@' length should be 4 for '%@' in manifest property entry
subCC is not hashed
onDeviceFDRProductType and serverFDRProductType are not the same: \"%@\", \"%@\"
inOutHttpStatus is NULL
metadataLength is 0
Ticket is not trusted.
dataClassArray must be a CFArrayRef
AMFDRDecodeImage4Certificate
SealingUpdateProperties
MultiExport
valueToRequest is NULL
AMFDRDataHTTPSign(amfdrRemote) failed.
dataClass has wrong type '%@
dataArray is NULL
AMFDREncodeRepairConfigurationAddSetWithKey failed 0x%X
outData from AMFDRSealingMapCopyDataInstanceForSealingMapEntry is NULL
realm
AMFDRDataHTTPCopyTrustObject failed: serverURL is NULL
failed to delete manifest: %@
_AMFDRSupportBase64Encode
escapedDataClassStr is NULL
Failed to get digest from rawDataToSign
failed to add NULL signatureOidParams
AMFDRSetOptions
dataInstances allocation failed
intraFactoryDataMap is NULL
sreqDataInstance is NULL
Cannot convert dataVersionOption
remote manifest decode and set minimalManifests: %@
FDR data trust evaluation failed.
failed to allocate data class/instance arrays
Both '%@' and '%@' exist in sealing map entry
errorCode is not NULL for successful record
com.apple.libFDR.persistent
AMFDRSealedDataGetMultiManifest
tempData is NULL, failed to convert tempCString to CFData
_AMFDRPlatformDefaultRefKeySign
Failed to get data class and instance to delete with error %@.
Remote FDR Data verification failed for %@.  (Data can be generated by restore, will not be recovered)
encodedMetadata is NULL
Memory
valueDataLength has size of 0
kIOReturnLockedWrite
malformed FDR Multi-Response Error Format
%@ is not entitled in AP ticket, derstat: %d entitled: %d
MissingLocalDataInstances
AMFDRDataLocalPutTrustObject
Failed to copy station local scrt
CertifyRawECDSASignature
adding apManifestTruncated to CSR
_AMFDRDataCopyForPutWithManifest
malformed FDR2 Format, expected tag %c%c%c%c found tag %c%c%c%c
x-fdr-jmet-product-type
_AMFDRPlatformGetPrivateKeyStation
AMFDREncodeSubCCDigestsAddData
MultiCombinedItem malformed for multi combined data
Unable to create localDataStore
send_message failed
AMFDRDataMemoryMultiDelete
_AMFDREncodeCreatePayload failed to return a payload
spub
Missing data to create multi sealing request and incomplete data is not allowed
AMFDREncodeManifestContextCreateSignedManifest
AMFDRDataSetApTicketAndGetNewestTrustObject
AMFDRDataMultiMake
failed to create innerHeaderKey
_CreateComponentAttributeData failed
contentStr is NULL
_AMFDRDataPrepareRepairConfigurationContextArrayData
No SCDG in manifest, subCC digest missing
amfdr is NULL
scrt
failed to HMAC sign (0x%.8x)
length of dataClasses and dataInstances are not the same
AMFDRError
CFStringCreateWithFormat returned key is NULL
_AMFDRCreateUrlWithKey
malformed export destination
sealedData->dataInstanceArray is NULL
AMFDRDataMemoryMake is not implemented
FDR Trust Object revoked client ID found
uri is NULL
_AMFDRSealedDataVerifyMinimalManifestProperty
remoteDataStore->optionsDict is null
'%@' sealing map entry does not have %@
AMFDRDecodeManifestBodyInfoGetDataClass failed
metadataDict is of incorrect type
Digest realm=\"%@\", nonce=\"%@\", salt=\"%@\", uri=\"%@\", response=\"%@\", qop=auth, cert=%@
AMFDREncodeMetaPropertyEnd
AMFDRGetComponentTypeForClassInstance
Unable convert %@ path to URL.
Unable to load memoryStore data from %@
faus
value is not NULL
failed to allocate dstEncoder
Stations
CookieFile
AMFDRSealedDataPopulate with amfdrRemote failed. Continuing since sealing is disabled.
failed to add pubkey algorithm
Could not create directory enumerator at '%@'
Previous AMFDRDataLocalPatch got errors
invalid payload tag: 0x%llx
nonce
metadataDictArray is NULL
failed to add data to certificationRequestInfo
amfdr->asidDict is NULL
AMFDRSealingMapGetEntriesForDeviceInternal
CopyTrustObject
failed to add attribute octet string value
No need to verify subCC and asid
currentDevice has wrong type %@
_createZhuGePreferences failed
AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance failed for %@:%@
asidExceptionList has wrong type %@
AMFDRDataLocalPrefetch is not implemented
Inner DER did not terminate properly.
queryCache is NULL
csrData byte length is 0
AMFDRDataLocalDecomposeFullKey failed for '%@'
AMFDRSetStat
kFDRTag_inst propertyValue (sik) != sikValue
productType has wrong type '%@'
esca
exportLegacyData: Remote FDR Data %@ exported successfully.
failed to verify test station signature, _checkVerificationError %@
optionsDict=%@
AMFDRPlatformCopyDefaultClientIdByInterface
multiUpdateMetadata allocation failed
_AMFDRDecodeEvaluateCertificateProperties
_AMFDRSealingMapCopyAsidMetadataParameters failed
AMFDRSealingManifestCopyMultiInstanceAndInfoForClass
FDR SSO function is NULL, SSO ticket fetching disabled.
DELETE
%@
intraDataClasses must be a CFArray
Failed to export data %@.
AMFDRDataGetSigningVersion
can't parse FDR Trust Object SslRoot sequence
malformed dataInstance
_AMFDRSealingMapCopyDataClassesAndInstances failed
sikPubDigest is NULL
dataInstanceStr is NULL.
AMFDRDecodeIterateSysconfigBegin
_AMFDRSealingMapCheckSubCCIntegrityInternal
_AMFDRCertificateSigningRequestInternal
MLBSerialNumber is required for sealing when allowSealingWithMLBSerialNumber is set
Data instances %@ missing.\nMulti-manifest %@ missing.\nDigest for %@ mismatched.\nCombined manifests %@ did not verify.\nData instances %@ did not verify.\nMinimal manifests %@ missing.\nMinimal manifests %@ did not verify. \nMinimalSealin
1.2.840.113549.1.1.11
_AMFDRSealedDataVerifyMinimalManifest
AMFDRDataLocalCommitPatch
malformed kAMFDRCertifyComponentAttributeBoardType, expected CFString.
AMFDRDataCreateSikInstanceStringInternal
dataInstanceStr is NULL
SealedProperty
Failed to populate extra device manifest
AMFDRSealingMapVerifySealingManifestPropertiesInternal
www-authenticate
failed to add SoCECID attribute
metaDataOptionsArray is NULL
Illegal use of PrivateKey
Unable to get trust object
AMFDRDataCreateRepairConfigurationAsidMetadata
_AMFDRHttpProxyIsEnabled
Remote FDR Data verification success, but Force Sealing requested.
AMFDRDataMemoryMultiCopyAsidMetadata is not implemented
outDataClasses is NULL
Could not create missingSubCCArray
com.apple.libFDR.httpRequestStatistic
arrayCount is 0
AMFDRDataHTTPPutWithOptions
failed to open userclient via %s: %d\n
-
x-fdr-chip-name
AMFDRDataHTTPChallengeClaim cannot find the callback funtion.
AMFDRSealingMapPopulateMinimalSealingManifest failed: %@
_AMFDRDataLocalSignContextToImg4Context
valueDict key is not a string
AMFDRDataLocalMultiPutWithOptions
newOptions is NULL
committed FDR data has larger size than estimated
failed to create properties
Failed to create csr
/System/Library/FDR/FDRSealingMap.plist
sealedData->sealingRequest is NULL. Sealing failed.
adapter_name is NULL
StripImg4
FusedByRestore
LocalSigning
INST
customCommonNameData is NULL
AMFDRDataStripExtraManifest failed
failed to copy dataInstance for %@
fetched from server for %@ 
AMFDRDataCopyDataForPatch
<AMFDRLocalDataSignContext: (null)>
publicKeyParam is NULL
AMFDRSealingManifestCopyLocalDictForClass
repairConfigurationContext is NULL
outCryptoVersion is NULL
Payload for data class '%@' is missing but is not required for sealing
AMFDRDataUpdateAsidMetadata failed
DataFailedToReport
AMFDRSealedDataGetSealingRequest
AMFDRDataErrorIsBenign
asidMetadataEntry has wrong type %@
Failed to copy station manifest
outRawData and outRawDataLength must be non NULL
subCCName cannot be NULL when kAMFDRDecodeOptionSubCCOnly is set.
queryCache allocation failed
errorString
AMFDRDecodeTrustEvaluation
FDR failed to decode multi combined Data img4
PKI: verify im4c cert was issued and signed by issuer (success)
Missing AllowIdentifierOverride entitlement
com.apple.libfdr.sealingMapRepairConfigurationCache
1.2.840.113635.100.6.17
failed to add attribute oid
failed to copy dict for %@-%@
invalid key length: %lu
Object of unexpected type '%@' for key dataInstance, expected CFString
assemblyID has invalid type
add item sequence failed 0x%X
Expecting kAMFDRDecodeImplementationSha384 or kAMFDRDecodeImplementationOffline
permStr must not be NULL
base64EncodedComponentSignature is NULL
_AMFDRDataHTTPMultiCopyInternal
FDREncodeCreateSignedManifest returned an empty manifest
signedValueData is NULL %@:%@
Instance %@ is too long
SOCKSPort
_CopyCsrGidSignature
metaValueDict key is not a string
AMFDRDataCreateInstanceString
%@ failed but did not return an error
failed to create PUT permission
%@-%@:%@
productType is NULL
All required subCC values are present in %@
escapedDataInstanceStr is NULL
SealingURL
AMFDRDataInstanceCopyNonSik
_AMFDRDataApTicketCopyURL
failed to allocate mutableComponentTypes arrays
failed to add BoardType attribute
img4.manifest.signed_section.length is 0
AMFDRDataDecodeMetaProperty
AMFDRDataMultiCopy local data missing %@
failed to decode DER
verifying subCC, skip comparing digest of the entire data
EnableProxy
 epochtime=%@
AMFDRSealedDataCreateSealingMetadata failed
_AMFDRFinalize
failed to allocate mutableDataClasses arrays
inData is NULL
CopyDefaultDataPath did not return a CFURL
dataInstancesOverride is not an array
Could not get value for identifier '%@'
Content-Length
authenticationStr is NULL
_createFullKeysForDataInstances
AMFDRDeviceKey.c
_CopyClientIdForAdapter
unsupported type for dataClasses
dataInstance is not a CFString. Verification failed.
failed to find %@-%@ from sealedData to delete
Failed to allocate amfdr->memoryStore.
Could not convert identifier '%@' to primitive
Failed to get data instance for data class '%@', but incomplete or unsealed data entitlement is present
missingDataIdentifiers
_isSealingClass
No intra factory data classes to download but AP ticket allows incomplete data
key has wrong type %@
AMFDRDecodeMultiSealingResponse failed
sikPubString is NULL
Failed to allocate infoOptions
AMFDRGetMemoryStore
AMFDRDataPopulate
there's something wrong with subCC digest for %@:%@, subCC check failing
Found '%@' not sealed
_checkVerificationError %@
amfdrSource optionsDict is NULL
Found local trust object
AMFDRDataVerifyInternal
failed to get attestation from offline blob
AssemblyIdentifierList
Allow unsealed, just return true...
multiErrors is NULL
Found sealing manifest: %@
AMFDRDataMemoryRevert is not implemented
dataClassToClaim is NULL
Metadata must be SET Container
Failed to create sealedData.
dm/bulk/metadata
newGrmr %@ is set by option, new base payload will be created.
AMSupportDigestSha384 failed 0x%X
could not populate the local sealing manifest, skipping
_AMFDRSealingMapCopyMinimalManifestClassesAndInstances failed
malformed componentType: %@
sealedData->dataClassArray is NULL
Local FDR Data missing, attempting to recover.
previous permissions request failed but supressed, not populating %@:%@ 
CFDictionaryCreateMutable failed for propertiesOverride
failed to get multi response for %@:%@
bdak
SrNm
primaryData for dcls create failed
Subjects
outContext->componentTypePostfix is NULL
AMFDRDataMemoryPatch is not implemented
failed to allocate outerSequenceEncoder
AMFDRDataCopyRawAndFormatted failed, can't copy original data
Img4DecodeGetPropertyData(0x%x) failed.
x-fdr-key-attestation
_Img4EncodeCreateUnsignedManifest
FDRSealedVerifyFail
Previous AMFDRDataMemoryCopy got errors
AMFDREncodeProducerIDAddDigest
VerifyAsidInSubCC
originalData is NULL
requiredSubCCs create failed
propertyValueTypes is NULL
x-fdr-seal-manifest-version
AMFDRDataMultiCopy failed(%@), but multiRequestError is NULL
valueDict contains NULL value
dataToSign must be non-NULL and non-0 length
keyBufferLength is 0
AMFDRDataUtilitiesCreateDataWithBytesNoCopy
Pid
Missing multi-manifest: %@
Failed to copy challenge callbacks
malformed FDR2 Format (manifest2), expected tag %c%c%c%c found tag %c%c%c%c
AMFDRSealedDataMultiManifestPopulate
AMFDREncodeRepairConfigurationBegin
Floating point identifier '%@' is not supported
AMFDRDecodeCheckProducerIDRevocation failed with error 0x%016llX
decode and copy payload keys for %@ failed
kIOReturnVMError
malloc failed
dataInstanceArray is NULL
_AMFDRDecodeVerifySubCC
_AMFDRSealingMapGetManifestPropertyEntriesForDevice failed
Failed to allocate prunedSealingMapCache
_AMFDRDataCopyFormattedRawAndImg4Internal
amfdrlocal permissions changed. Old permissions: %@ new permissions %@
PersistCookie
AMFDRDecodeOfflineBlob failed
csrDERData is NULL
outRawData must be non NULL and outRawDataLength must be non 0
Response commandDict is NULL
Unable to get sik
Int64 property value is not the size of uint64_t
keyValueData is NULL
StoreAsInteger
failed to create an encoded data blob for %@
AMFDREncodeSubCCDigestsEnd
failed to create repairConfigurationData
Could not find sealingMapAllProperties for '%@'
attestation is NULL
_AMFDRDataDictMultiCopyInternal
DataInstance
manifestProperties is NULL
Unable to create challengeDigest
failed to get FDR data version
not found, discard from
dataClassLength is %d, unexpected...
Skip verifying type info
ExportDestination
Invalid context, expected AMFDRRef
Img4EncodeCreatePayload failed 0x%X
CertifyClientId
%@ is missing but Allow Incomplete Data is set
AMFDRDataHTTPExport failed
failed to decode private key
cannot decode to a multicombined data, proceed with combined format
Record value length is 0
AMFDRDataMemoryMultiCopyAsidMetadata
amfdr->memoryStore failed allocation
httpResponseHeader is NULL
facf
UnverifiedDataInstances
AMFDRDataVerifyAndCopySubCCKeys
AMFDREncodeRepairConfigurationEnd failed 0x%X
_AMFDRDecodeMultiResposeRecords failed with error 0x%llX
permsStr is NULL. kAMFDROptionPermissions required in options.
AMFDRModuleCreateSignedCSR
Failed to convert CSR to PEM format
Unable to commit FDR memoryStore data to disk.  Error %d
AMFDRCreatePermissionsString
propertyLength != implementation->digestInfo->digestOutputSize
Failed to create amfdrLocal
_AMFDRDiagnosticCreateDataReport
Sealed key not found with live queries based on sealing map
Failed to compute digest of RSA Public Key
failed to read hardware model
FDRSealedVerifySuccess
*outSealedData is NULL
amfdr->componentTypeDict is NULL
Malformed key '%@'
Skipping revocation check (trustobject unset)
2.5.4.11
_deleteFromSealedData failed with error %@
No implementation in AMFDRDataMemory module
Unanble to create public key from private key
dstSequenceEncoder is NULL
Local
AMFDRPermissionsRequest
Failed to get proxy info for URL '%@'
1.2.840.113635.100.11.1
valueDict is NULL
outdataLength is NULL
amfdr->digestDict is NULL
apTicket is null
Required data missing from FDR DataStore but either 'Allow incomplete data' or 'Allow unsealed data' is present in AP or Sealing Manifests.
metadataRecordCallback failed with error 0x%llX
AMFDRDataPut(%@:%@) failed
valueData is NULL
dataClasses allocation failed
_AMFDRSealingMapInfoSetValue
_AMFDRDeviceRefKeyClassFinalize
Unable to create remoteDataStore
found data in multi combined format
mutableMinimalManifestInstances create failed
metadata has wrong type %@
1.2.840.113635.100.6.8
IODeviceTree:/chosen
Img4DecodeGetPropertyData(kImg4Tag_DGST) failed.
AMFDRHttpMessagePostAction failed: %@
failed to create csr data
signContextArray is empty
ccrsa_generate_key_deterministic() -> %d
Failed to allocate buffer
Flushed memoryStore to %@
Unable to create defaultPath
DiscardExtraManifests
iPhone17,4
options on amfdr are NULL
Failed to create trustobjectDigestData
malformed kAMFDRCertifyComponentAttributeBatteryVersion, batteryVersion = %@, batteryVersionValue = 0x%llx
FDREncodeCreateSignedManifest
FDREncodeCreateOfflineSignedManifest
strValue is NULL
dataClassArray create failed
/
%@ already in valueDataDict
FDR failed to create SSO data. (ssoData is NULL).
bmuIdentifierData is NULL
items is invalid
%s: failed to allocated digest data\n
Local verification pass. Skip Auto Challenge Claim by Server, dataClass:%@, dataInstance: %@
failed to query sealed data instance for minimal manifest and incomplete data is not allowed
Unexpected error and underlying error for %@:%@: %ld, %ld
failed to copy matching sealing properties
AMFDRDataMemoryMultiMake is not implemented
failed to encode data class
outSealingMap is NULL
failures is NULL
failed to create multiManifestDataClass
'%@' manifest populate
amfdrOptions is NULL
dm/bulk/export
fdrOptions is NULL
value is malformed
POST
metaDataDict is of incorrect type
VerifiedData
cannot find a way to decide board revision
%@ failed to report what data is missing
malformed kAMFDRCertifyComponentAttributeBatteryVersion, expected CFNumber.
_copySealingManifestProperty
Failed to allocate privateOptions.
Invalid patchDictArray count
minimalManifests create failed
failed to copy payload data for %@-%@
DataClassesOverride
certificationOptions has wrong type: %@
_AMFDRDataHTTPConvertMultiResponseKey
LiveInstance
minimalSealedDataInstances must be a CFArray
failed to read cert data from %@. error %d
trust verification error code=0x%016llX for %@:%@
dataInstance has wrong type '%@
infoValue allocation failed
apManifestTruncated is NULL
data %@-%@ is missing
signing failed: signature is NULL
values has wrong type %@
sysconfig version not supported: 0x%x
PKI: verify cert %d was issued by %d (success)
x-fdr-jmet-multi-seal
No digest and no data to compute it from
minor version not supported: 0x%x
failed to get instance of primary dataClass %@
_AMFDRPlatformGetPrivateKeyNative
AMSupportMakeDirectory failed
AllowSealingWithMLBSerialNumber
apManifest is NULL
SealIdentifiers
verifying sealing properties against sealing manifest
kIOReturnRLDError
failed to create keyData
currDataInstanceData is NULL
Unverified data instances: %@
dataLength is 0
kIOReturnNotOpen
asid subCC length != fdrDecode->asidSubCCID.length
Property tag '%@' in sealing map is not sealed.
failed to get process name
AMFDREncodeMultiCombinedDataPayloadAddData
failed to create valueData
AMFDRDataLocalMake
failed to create data instance string
_AMFDRCopyChallengeCallbacks
Failed to populate local data
Failed to allocate sealingMapEntryDict
AMFDRDataCopyAsidMetadataParameters failed
dataClassArrayToCopy is NULL
tag has wrong type %@
Set %@ to MSM version: %@
Nothing to compose multirequest
failed to add BatteryVersion attribute
Sign
kIOReturnStillOpen
_AMFDRSealingMapGetEntries
multiDataInstances is NULL
entitlement is missing
Failed to append permissions string with data class '%@', data instance '%@', action '%d'
metaOptions allocation failed
got http failures
trustObjectDigest is NULL
malformed FDR Metadata Record Format
LiveProperty
FDREncodeCreateCombinedFast
Could not get filename of URL '%@'
AMFDRSealingMapPopulateMinimalSealingManifest
%lu bytes data found in multi-response for %@
CFStringCreateCopy returned false.
Unable to create DER CSR (csrDER is NULL)
Failed to create csr, _AMFDRModuleCreateSignedCSR failed.
AMFDRGetCert
ComponentType/
Invalid dataInstancesArray count
TS2
AMFDRDataHTTPPrefetch
_AMFDRDataCopyImg4StrippedValue
AMFDREncodeMultiCombinedDataPayloadAddData failed 0x%X
AMFDRDecodeCheckCertRevocation
Invalid metadataDictArray count
_AMFDRSealedDataFinalize
NULL
AMFDRDataMemoryUpdateMetadataWithOptions is not implemented
failed to add data to attributeEncoder
failed to find corresponding data instance
%d %@
outSealingManifest is NULL
failed to load file %@, status %d
SkipManifest
APTicketAllowDigestMismatch
asidMetadata has wrong type %@
FDR 3.0 Data can't be decoded!
_HttpRequestStatisticCreateString failed
failed to convert certificate
failed to create sealedDataInstanceData
xcld
AMFDRGetOptions
AMFDRCreateDataSignature
Patch data can't pass grammar check
dataInstanceLength is not 0
AMFDREncodeSubCCDigestsBegin
FCAM-IR
AMFDRDataLocalMultiDelete
outImg4Blob must be non NULL and outImg4BlobLength must be non 0
sealNotIntended is true, skip to get minimal-manifest
moduleRawPublicKeyWithPrefix is NULL
1.2.840.113635.100.11.2
Failed to convert sealedDataInstance to CFDataRef
*outManifest is NULL
mansta
StoreMaxSize
failed to add subCC
copied localData is NULL for %@:%@
manifest
messageData is NULL
mutableKey is NULL
Failed to populate sealedData from local data store. Data recovery failed.
Invalid private key data type
failed to add %s data
kIOReturnBadArgument
CFErrorCreate failed.
sysconfig context is not initialized
BoardID
AMFDRSetOption
different length of dataClassesOverride and dataInstancesOverride
Value in sealing map has wrong type
Remote FDR Data verification success against test station signature.
AMFDRDataMemoryMultiCommitPatch is not implemented
clientIdSik is NULL
createSignedData failed
_AMFDRDataPermAllowed
_AMFDRSealingMapCopyDataClassesAndInstancesInternal for required to seal attribute failed
exportLegacyData: Failed to export legacy data %@.
Checking %@:%@ from sealing map...
failed to decode metadata #%u: 0x%llx
AMFDRDataCreatePermissionsString
failed to decode FDR Combined Format
aries
Object of unexpected type '%@' in manifest property entries
_AMFDRSealingMapCopyMinimalManifestClassesAndInstances
_AMFDRSealedDataCreateMinimalSealingRequestPreCheck
AMFDREncodeRepairConfigurationCollectionEnd failed 0x%X
malformed FDR Combined Format (DERFDRItemSpecs)
Use small manifest for '%@' for copy local data
Malformed requiredDataInstanceString '%@'
AMFDRDataHTTPCopyDigest
RefKeyBlob
Failed to allocate dataFailedToReport.
Failed to export sealedData
%@.offline
dictValuesBuffer allocation failed
_AMFDRPlatformDefaultCopyDeviceKeys
.
AMFDRRegisterModuleChallengeCallbackV2
localSignContext->dataInstanceData is NULL
OID of %@ #%d is not a string
IM4P
AMFDRSealingManifestCopyLocalMultiCombinedDataAddDataClassWithMultiData
failed to add csrSignature
outManifest is NULL.
AMFDRSetComponentTypeForClassInstance failed
AMFDRSealingMapCopyManifestPropertiesForDeviceInternal
failed to get signature from callbackSignature
Failed to allocate failureData/verifiedData
AMFDREncodeMetaPropertyBegin failed 0x%X
AMFDRSetModuleChallengeCallbackV2Context
AMFDRDataPutWithOptions
MultiPatch
cannot find matched camera sensor info: (%@)
no ticket in options
failed copy subCCDigestDict from amfdrRemote to amfdrLocal
SealedSubCCMissing
ExportAfterSealing
Claim is skipped because no data needs to be claimed
Unexpected type '%@' in subcc list
Unable to create CSR RefKey signature
AMFDRSealingMapConfigSealedData failed.
DERParseBitString(sig) failed
identifiers is NULL
AMFDRSealingMapCopyDataClassesAndInstancesWithAttribute
_AMFDRSealingMapCopyIdentifierListForClass
CertifyBase64
Found local data: '%@'
ctx must be non NULL
Skip copy data class '%@' with '%@' attribute
dataClassesArray is NULL
unexpected qop: %@
AMFDRSetOptions(amfdrLocal) failed.
_AMFDRDecodeMultiSealingResposeRecords failed with error 0x%llX
_AMFDRSealingMapGetManifestPropertyEntriesForDevice
DEREncoderAddData failed for boardTypeData
sik-
PKI: verify cert was issued by trusted root %d (success)
primaryDataDict has wrong type %@
unknown action type: %d
AMFDRDataAddSealingPropertiesOverride
_AMFDRDataDictPutInternal
failed to decode public key: %d
Components
ClientId
failed to preserve amfdr options
CryptoGenerateRSAKeys
failed to add attribute
VerifyData
_AMFDRDataPrepareRepairConfigurationContextSupmSetData
manifestPrefix is NULL
Using overridden data class and instance %@:%@
Skip data class '%@'
outManifestProperties is NULL
Failed to get value for property tag '%@', skipping.
failed to populate apticket, currently not fatal
subCCArray is NULL, please use AMFDRSealingMapCopyLocalMultiCombinedDataAddDataClass when adding the entire data
Failed to create outDataReport
outBlob is NULL
MissingSubCCDataInstances
propertyTag is NULL
AMFDRDataMemoryPopulate
aks
failed to allocate path
input data array is NULL
sik-%@-%@
dataInstanceStr is of 0 length
dataToStrip is NULL
dataClass is not a CFStringRef: %@
newGrmr %@ is set by option, but no Grmr in original data
could not verify minimal manifest from the local sealing manifest, skipping
copyLocalMultiCombinedDataContext is NULL
Attribute/
failed to add valueSequenceEncoder to keySequenceEncoder
libFDR-??
mix-n-match-prevention-status
UseSOCKSHost
metadata is NULL
not found %@ in sealedData
AMFDRDataMemoryMultiPatch
outSignature is NULL
Invalid dataArray count
sealedData->intraFactoryDataInstances is NULL
RepairConfigurationAsidExceptionList
_AMFDRHttpAuthenticationCallback
payload keys and values have different numbers
dataInstances is NULL
dataClassesOverride is not an array
;%@/Mothership
Payload type mismatch
No data to seal over or data verification is not required. Data verifies.
AMFDRDataMemoryMultiCopyManifest is not implemented
metaPropertyCallback failed with error 0x%llX
Force to check non-sik data
httpRequest is not a CFHTTPMessage
%@ is not in newMinimalSealingDataInstances
https://skl.apple.com
amfdrCopy is NULL
tempCString is NULL
MissingDataInstances
_AMFDRHttpLogResponse
_AMFDRSealedDataCreateSealingRequestInternal (MultiSealing) failed
Unverified minimal manifests: %@
https://ig.apple.com
AMFDRDataCommitWithPopulateAddition
permission is NULL
MultiPut
Failed to clear populated data from sealedData. Data Recovery failed.
Missing data instances.  Sealing manifest will be %@ AMFDRSealedDataRef.
AMFDRDataCopy failed, but ignoring verification failure.
AMFDRDataLocalDecomposeFullKey failed with %@
_AMFDRDataDictCopyInternal
dm/export
formattedInstanceStr is NULL
AMFDRDataLocalPatch
_AMFDRHttpHandleHeaderMessage
AMFDRDecodeEvaluateTrustOfflineInternal
Unexpected type '%@' in sealing map
failed to create boardTypeData
AMFDRSealedDataCreateSealingRequest
sreqDataInstanceStr is NULL
metadataContext is NULL
value has wrong type %@
AMFDRSealedDataVerify failed without returning outError
invalid challengeSupport128b: %@
dataClass is NULL. Sealing failed.
AMFDRSealedDataVerifyDigest
failed to add subject oid
AMFDRDecodeIterateTrustObjectSslRootBegin
AMFDRSealingMapCopyMultiInstanceWithIdentifiers
AMFDRSealingMapPropertyHasAttribute
AMFDRSealingMapPopulateSealingManifest failed on amfdr
x-fdr-patch-required-subcc-dgst
responseParts is NULL
cannot populate paired SoC if dataClassArray (%@) or dataInstanceArray (%@) is malformed
No restitch manifest, but allow unsealed, try to proceed with the data manifest...
_AMFDRDecodeVerifySignature
Invalid AMFDRDeviceRefKey
commandDict is NULL
metaData is malformed: %@
FDREncoderAddSequenceProperty
_FDREncodeAddManifestProperties
success
+
%@ already in multiRequestErrors
AMFDRDataVerifySealingManifest
malformed attribute: %d
AMFDRSealingMapCheckMultiSubCCIntegrityForClass
x-fdr-minimal-seal-version
^^^^^^^^^^^^^^^^^^^^^^^^^ END httpRequest ^^^^^^^^^^^^^^^^^^^^^^^^^
Failed to write extra station manifest
_AMFDRDataClaimInternal
_AMFDRHttpRequestSendSync returned error
manifest or object missing required property '%c%c%c%c'
AMFDRServicePreflightRecoveryCopyData
FDRTotalHTTPFailures
AMFDRSealedDataVerify with amfdrLocal failed after recovery. Data Recovery failed.
failed to allocate *outData
Failed to create FDR2 data
Invalid data digest input
SkipRecoverDataClasses
subCC values cannot be verified for %@-%@
AppleDeviceQueryFramework ZhuGeCopyValue is unavailable!
partialIm4mData is in malformed format
url is null
Must have a data instance for each data class to add to miniaml sealing array
contentType is NULL
payloadDict is NULL
_buildReportWithKey
encodedSealedData is NULL
NSString is not respond to initWithBytesNoCopy on this device, falling back to CFStringCreateWithBytes
mainManifest is NULL
failed to write data to %@
Skip the mimatched property %@ in ingoreProperties array
_AMFDRHttpNonceSign
dataClassToRequest is NULL
foundData is NULL
outPayloadKeys is NULL
FDR Trust Object revoked public key found
PKI: verify cert %d was issued by cert %d failed with error 0x%016llX
Mismatched properties: %@
<Sysconfig '%@'>{version=0x%08x}
%@ #%d has invalid length
Failed to store trust object in local data store
memoryStore is NULL
AMFDREncodeCertificateRequestBegin
AMFDRDataStripExtraManifest
manifest2 data is NULL
claimPermissions is NULL
Missing key '%@' in manifest property entry
Could not get assembly identifier
failed to encode manifest version
aks_ref_key_create_with_blob failed : %d
x-fdr-client-version
saltedNonce is NULL
dataInstance is not CFStringRef
AMFDRSysconfigCreateEncodedData
add data class failed 0x%X
length of gestaltKeyList is 0
query %@ failed, productInfoValue is %@, typeID is %lu
AMFDRDataGetMinimalManifestVersion failed
patchedPayloadDict is NULL
value is NULL
ingoreProperties is not a CFArray
httpXHeaders is not dictionary
bpub
Could not find sealingMapProperties for '%@'
failed to write cert data to %@
AMFDRDataMemoryMultiCommitPatch
AMFDRDataRecover
committed FDR data (%ld bytes) has larger size than estimated (%ld MB)
Failed to create certificate reference
User
_AMFDRHttpLogRequest
failed to encode metadata key #%ld
failed to add metadata record value
Invalid kAMFDRDataClaimOptionServerOnlySigningDataClasses option is set
privatekey
AMFDRSealedDataPopulate
AMFDREncodeMetadataBegin
_copyIdentifierListForSealingMapEntry
failed to add dataClass
TrustObjectDigest
pManifestBodyInfo is NULL
invalid digest length
_AMFDRDecodeMultiResposeRecords
Could not skip seal class '%@'
failed to allocate memory
UniqueChipID
asid metadata of %@ is removed because its super module %@ has missing parts
Failed to read data from %@
dcls
exceptionDataClass has wrong type %@
multiRequestErrors is NULL or unexpected
failed to allocate sWithZero
Required generated data missing from FDR DataStore, but may be generated at restore time.
AllowCSRForbidden
dm/make
Unable to create attestationData
AMFDRDecomposePermissionString failed
dataClassInstanceToRetry is NULL
failed to allocate minimalSealingData arrays
_AMFDRHttpCopyPurpleReverseProxyInformation
failed to copy sysconfig entries
DeprecateGIDSigning
Invalid value '%@' for option '%@' (must be a CFString)
_AMFDRSealingMapPrepareAMFDRForCopyLocalData failed
Failed to create an unsealed manifest for multiple data
___thr_AMFDRLoadPersistent
authorizationResponseStr is NULL
Failed to allocate verifiedProperties/failureProperties
FDRSealingSuccess
if_nameindex: skipping %s
Remote FDR Data verification failure, attempting to seal.
AMFDRDataLocalMultiMake is not implemented
Cannot specify both componentAttributesCritical and componentAttributesCriticalProductionMode at the same time
failed to allocate encoder
Only supports remote amfdr
_AMFDRDataMultiPatchCallback
AMFDRDecodeManifestBody failed
*outSealedDataLength is 0
errorLength is 0
cannot convert subCCsToVerifyDigest to uint32_t ptr
Failed to allocate fullKeys
AMSupportRemoveFile failed %d.
kAMFDROptionOfflineSigning
dataClassArray has invalid element #%ld
Cannot get entry at index %ld
property %@ from sealing manifest has mismatched data (required=%d, matching=%d)
en3
digest is invalid
AP is in non-default demotion state, ignore sik verification
can't parse MinimalManifestMetaData
failed to allocate data classes/instances/missingDataIdentifiers
Unable to create csrSigData
failed to create internalCertificationOptions
%@ not a valid 4cc
Local FDR Data found and verified, but Update dataClass requested.
data for %@ missing, but is not required for sealing.
Skip export missing data %@-%@
_AMFDRDecodeTolerateErrorsForOptions
propertyTag has wrong type %@
failed to copy data and save manifest for %@
missing data asid from metadata
minimalManifestData for %@:%@ missing, not commit this manifest
payload value #%u is NULL
AMFDRDataAppendPermissionsString
AMFDREncodeRepairConfigurationBegin for product info item failed 0x%X
SkipExtraManifests
AMFDRSealingMapCopySubCCDataClasses
clientIdData is NULL
FDRRecoveryFail
Failed to load sealing map
Missing key '%@' in sealing map entry
dataToEncode is NULL
originalData and expectedData are NULL
Certificate
%s: %@: code=%ld
*
target class is NULL but instance is non-NULL
EnableSslValidation
CertifyComponentAttributesCriticalProductionMode
AMFDRDataLocalCopyExtraManifest
Delete from sealedData %@-%@
SealingManifest
use sik option defined by sealingMap
*minimalManifestInstances malformed
can't parse top-level container
Unable to create outCert
kAMFDROptionSealingUpdateProperties is not array
malformed dataClass
Missing minimal manifests: %@
publicKey is NULL
CFStringCreateExternalRepresentation(dataClassData) failed
AMFDRDataHTTPIterate
topLevelSpec for metadata is NULL
failed to allocate outerSetEncoder
patchDict is NULL
%@ has been specified in override data class, skipping this entry
No data classes to seal over but it's match attribute case
Failed to load FDR keys %d
failed to add data to subjectEncoder
AMFDRDecodeIterateProducerIDBegin failed with error 0x%016llX
ComponentAttributeProductionMode
finalDataClassesToExport is NULL
instanceStr is NULL
AMFDREncodeRepairConfigurationBegin for Collection failed 0x%X
Encountered '%@' data class twice
___thr_AMFDRHttpRequestStatisticsRecord
missing value in pairedSoCs
%@%@
2.5.4.10
AMFDRSysconfigCreateEncodedKey
failed to allocate subjectEncoder
originalDataArray is NULL
failed to verify img4 data for %@-%@
failed to HMAC sign
/System/Library/Caches/com.apple.factorydata
resultData is NULL
subCCListWithDigest is malformed
%s returned status %d. x-fdr-message: '%@'
No data to seal over. Declaring data verified.
Unexpected type for property tag %ld
MultiRequestActionPut but valueDataArray is NULL, or other action code but valueDataArray has value
AMFDRDeviceRefKeyCreateWithData failed
metaKeysToUpdate is NULL
SubCCList
kAMFDROptionExportDataClasses is not array
multiSealingMetadata is malformed: %@
dataClassInstance has wrong size '%ld
 missingSupm: %@ 
1.2.840.10045.4.3.3
inst is NULL
failed to create uuid
failed to parse local sealing manifest for seal date
seal
Failed to load sealing map on device
Primary module '%@' verification pass
AMFDRDataHTTPLoadPersistent failed
AMFDRCryptoCopyAttestation
type has wrong type %@
refKey is NULL
img4 data is NULL
failed to copy combined data, returning uncombined data instead
AMFDRDataMemoryMake
FDREncodeCreateSignedManifest failed %d
PKI: im4c cert signature validation with issuer pubkey failed
PKI: check payload hash with signature (success)
x-fdr-user-metadata-
_AMFDRSealedDataExportExistingData
failed to allocate payloadEncoder
failed to create minimalSealingDataInstanceData
CFDataCreate failed to create md5 data
certificate
^^^^^^^^^^^^^^^^^^^^^^^^^ BEGIN httpRequest ^^^^^^^^^^^^^^^^^^^^^^^^^
AMFDRSysconfigSetMetaValues
valueDataDict is not NULL
CertifyPartNumber
dataClassesToVerify is NULL
AMFDRDataMemoryGetStore
no sealing manifest in options
primaryDataClassInstance create failed
amfdr/amfdr->optionsDict is NULL
CertifyHeaders
AMFDRDataHTTPMultiUpdateMetadataWithOptions
AMFDRDataMemoryMultiPatch is not implemented
sik_pub_key is NULL
AMFDRDataCopyPayloadKeysFromData failed
unexpected tag 0x%llX in certificate properties
AMFDRDeviceRefKeyCreateWithData
add productInfoValue of %@ failed 0x%X
AMFDRDataLocalDelete
populate sealedData with sealing manifest, sealingManifestOverride : %@, forceSealing : %@, allowForbidden : %@, allowUnSeal : %d, updateDataClasses : %@, updateProperties : %@
CFPropertyListCreateWithData returned %@
export destination has wrong type
failed to strip set from im4m signed section
key is NULL
failed to validate ticket (error %d)
failed to decode as sysconfig format
malformed FDR2 Format (manifest2), invalid tag length
AMFDRSealedDataCommit failed.
preflight
AMFDRDataHTTPSign failed
action is NULL
No sealing manifest in data store
localFullKeys is NULL
PropertyMismatched
AMFDRCopyDisposableKeys
Failed to read data
failed to decode metadata: %d
metaKeys is NULL
Img4EncodeCreateManifest returned an empty manifest
amfdrLocal is NULL
subCCs is NULL
failed to find MANB (manifest body) tag
Outer DER did not terminate properly.
implementation must be non NULL and signatureOid must be non NULL
Failed to append permissions string with data class '%@', data instance '%@',  action '%d'
AMFDRIncrementStat
AMFDRDataPatchWithOptions
_AMFDRDataPrepareRepairConfigurationContextPdct failed
_AMFDRSealingMapCopyPropertyTagsAndIdentifiersWithAttribute
permsStr is NULL
radomData is NULL
newNode is NULL
kFDRTag_inst propertyValue missing expected -
chain_blob must be non NULL and chain_blob_length must be non 0
_AMFDRHttpCopySOCKSInformation
dataInstanceArray must be a CFArray
Local FDR Data found and verified, but Force Update requested.
_AMFDRSealingMapGetRepairConfigurationEntryWithSealingMapEntry
sealingIM4M is NULL
AMFDRIsProtoDevice
_appendManifestProperties
amfdrRemote permissions changed. Old permissions: %@ new permissions %@
x-fdr-retry-timeout
IOAESAccelerator
PKI: verify cert was issued by trusted key %d (success)
sig_len is 0
AMFDRSealedDataSetMinimalManifestClassInstanceWithVersions
failed to find property tag 0x%llu
Failed to create tempMemoryStoreData
missing data hash from metadata
failed to add ComponentIndex attribute
property tag '%@' not found
failed to add subject sequence
dataClassData is NULL
formattedDict is uninitailized
invalid propertyTag '%@'
component
verifying minimal sealing manifests
AMFDRSealingMapPopulateMinimalSealingManifest failed on amfdr
Failed to find store max size for '%@'
unknown metadata value type at #%ld: %lu
failed to add attribute data
keyNameData is NULL
AMFDRDecodeMetaProperty
epochTimeNumber is null 
failed to create csr context
CertifyComponentAttributesCritical
AMFDRDecodePublicKey
_AMFDRDecodeIterateCertChainNext failed (%d)
AMFDRDataHTTPPresent
Failed to allocate str
failed to create img4 data: %d
time
invalid number of payload values
Permissions
malformed cert property key: %c%c%c%c
Not support for CFArray format in AMFDRSealingMapCopyInstanceWithIdentifiers
Using value %@ for key %@ from query cache
%s: failed to get data property from Img4 manifest\n
_AMFDRDataDictCopyForPut
outDerDataLength is NULL
failed to copy OID of %@ #%d
%@ must be a CFURL
updateAsidMetadataPermissions allocation failed
_CopyDevRefKeySignature
Failed to read memory data for key %@
AMFDRDataMemoryMultiUpdateMetadataWithOptions is not implemented
DIGEST
sealingManifestData is NULL. kAMFDROptionSealingManifest not set in options, not stitching im4m
Invalid originalDataArray count
_AMFDRDecodeGetExpectedManifestHash
statKey is NULL
rawManifestData is NULL
Cannot get amfdr version
repairConfiguration has wrong type %@
failed to add pubkeyOidParams
failed to copy data for %@-%@, but data is allowed to be missing since skip sealing is enabled
ComponentAttributeBoardType
failed to add signatureOid
%@-%@
3kmXfug8VcxLI5yEmsqQKw
PKI: verify cert was issued and signed by issuer (success)
No trust object present in amfdr object
failed to create encoder
1.2.840.113549.1.9.14
Skipping sealing property '%@' as specified.
_AMFDRSealingManifestSetSikOverride failed
sha2-384
EffectiveSecurityModeSEP
dataInstancesToReq is NULL
cannot allocate memory
AMFDRDecodeManifestBodyInfoGetDataInstance failed
failed to obtain valid patched digest and data
Found live instances '%@' for '%@'
AMFDRSealedDataDelete
refPubKey is NULL
Local FDR Data found and verified, but Update Repair Configuration Asid Metadata requested.
Failed to populate sealedData->sealingIM4M from local data store. Data Recovery failed.
AMFDRDataLocalIterate
kAMFDROptionUseSOCKSPort is not CFNumber
dataClassInstance is NULL
AMFDRDecodeIterateTrustObjectRevokedBegin
Primary
keyLength is 0
AMFDRDataInstanceUseSikFormat
signature must be non NULL and publicKeyLsignatureLengthength must be non 0
DEREncoderAddData failed for component index
_copyUnderlyingErrors
Could not query MobileGestalt for key '%@'
permissions has wrong type %@
propertyValues is NULL
AMFDRDecodeManifestBodyInfoGetComponentType failed
DEREncoderAddDataFromEncoder failed
AMFDRDataMultiPutWithOptions
clientCert is NULL
ticketHash
options is NULL
%s:%spid:%d,%s:%s%s%s%s%s%u:%s fail%s\n
userInfo is NULL
failed to allocate mutable copy of override data class/instance array
Using %@:%@ from sealing map
x-fdr-metadata-authuserid
x-fdr-certification-type
failed to allocate certificationRequestInfo
metadataDict allocation failed
fdrProductType is NULL
unsupported public key length: %lu
Skip optional data class '%@'
___thr_AMFDRSavePersistent
Failed to create batteryVersionData
dataClassArray allocation failed
Value in key '%@' or %@' or %@' has wrong type
AMFDRCertificateSigningRequest failed
outerSequenceEncoder is NULL
AMFDRModuleCameraSensorAuthIsValid
AMFDRModuleCertificationWithOptionsAndPermissions
_createFullKeysForDataInstances failed
verifiedData is NULL
AMFDRDeviceRefKeyCopyAttestation
Object of unexpected type '%@' for key dataClass, expected CFString
malformed dataInstanceArray
failed
failed to allocate sequence/octet encoder
Missing key '%@' in subcc list entry
verifyError is NULL
AMFDRAppendPermissionsString failed
AMFDRDataMultiUpdateMetadataWithOptions failed with error %@
kFDRTag_inst propertyValue != instValue
primaryDataClass has wrong type %@
_copyMGValuePropertyEntry
Error enumerating %@, error: %@
_AMFDRDataMultiPatchInternal
payloadData is NULL
AMFDRDataRevert return false
DataClassOverride and UpdateDataClasses contains same dataClass
AMFDREncodeSubCCDigestsAddData failed 0x%X
AMFDRDataLocalCommit
ignoring incomplete subcc error 0x%016llX
mismatched digest for %@:%@, retry fetching manifests
AMFDRDecodeCertificate
MissingSealingProperties
Missing value for currentDataInstance Array in sealing map entry 
Failed to get ApTicket
failed to get refkey
repairConfigurationContextSrc is invalid
MissingMultiManifests
_AMFDRDataCreateRepairConfigurationAsidMetadata
failed to parse AP ticket
AMFDRDataMultiUpdateMetadataWithOptions - %@
_AMFDRDecodeInstPropertyMatching
propertiesOverride is not a dictionary
AMFDREncodeRepairConfigurationAddData
_AMFDRSealingManifestCopyDataClassesAndInstances failed
AMFDRDecodeMetadata failed
failed to add attestation
malformed FDR Trust Object Revoked, invalid trusted tag length
propertiesToExclude is not an array
internalHttpXHeaders is NULL
%@%@%@%@%@%@
failed to decode hex string
EntitlementReadFailed
ForceCommit
sealingManifestData DataCopy failed
subject: %s, issuer: %s
end of trusted key sequence found root_key=%d
outSignedCsr is NULL
Expected data type in sealedData->dataArray
failed to create encoded buffer
CFArrayCreateMutable failed for dataClassesToClaim
ctx is NULL
if_nameindex: found clientid %@ for adapter %s
unescapedValue is NULL
SSL trust evaluation failed
%@:%@ get data failed - uncombinedData is NULL
_AMFDRDataMultiPatchCallback got errors
MultiRequestErrors
invalid createX509PublicKey: %@
%s:%spid:%d,%s:%s%s%s%s%s%u:%s bad 1%s\n
FDREncodeCreateCombinedFast length mismatch
AMFDRDecodeEvaluateTrustOffline
_AMFDRDiagnosticCopyEntitlementsFromAPTicket
_deleteUnverifiedDataInstance failed when deleting data %@-%@ with error 0x%016llX.
SSO enabled for data PUT
FDREncodeCreateSignedData failed
ignoring no trustobject error 0x%016llX
Failed to allocate privateOptions
AMFDREncodeProducerIDAddDigestFromData failed %d
AMFDRDataCreateFDR2Data failed
fail to decode certificate of offline signing
publicKey must be non NULL and publicKeyLength must be non 0
propertyEntry has wrong type %@
cookie
clearing expected kAMFDRServerErrorNotFound error
invalid createECDSADerSignature: %@
kIOReturnNoResources
kIOReturnIPCError
_AMFDRSetOptions failed
failed to read manifest: %@
Skipping trust root check (trustobject unset)
AMFDRSealingMapCreateRecoveryPermissionsWithOption
AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance
Malformed dataInstanceString '%@'
asidMetadataInternalBlob has wrong type %@
%d
FDR using SSO.
metaDataToRequest is NULL
metadata keys and values have different numbers
failed to add img4 data IM4M
Unexpected propertyValue type
AMFDRSealingMapCopyLocalMinimalManifestSubCCKeys
ComponentAttributeComponentIndex
AMFDRSealedDataGetSikOverride
AMFDRDeviceRefKey
failed to allocate recordEncoder
AMFDRDataVerifySealingManifestInternal
AMFDRDataCreateCombined failed
AMFDRHttpMessagePreAction failed
CertifyClassFKey
exportLegacyData: malformed dataClass
certificateRequestContext is NULL
AMFDRDataCreateMultiDataAsMultiResponse
AMFDRCryptoCreateCsr
failed to add csr
AMFDRDataVerifyImg4Integrity
dataBlobs is NULL
_AMFDRDecodeVerifySignatureDataWithOid
AMFDRSealingManifestCopyMultiInstanceForClass
pidNumber is null 
%@ %@
Tag
Img4DecodeInitManifest failed
_AMFDRDiagnosticCopyAndVerifySubCC
asidMetadata AMSupportBase64Encode failed
AMFDRDecodeIterateProducerIDBegin
Invalid property length of kFDRTag_SrvT
_AMFDRSealingMapCopyDataClassesAndInstancesInternal
MultiRequestBackoff
base64CsrSignature is NULL
sealedDataInstance must be a CFString
Local FDR Data found and verified, but Force Sealing requested.
-----END RSA PRIVATE KEY-----
Unknown
%@:%@ make data failed - foundData is NULL
AMFDRDataLocalCopyManifest
non-sik AMFDRDataAppendPermissionUpdateAsidMetadata failed
AMFDRSealedDataConfigureOptionsForRecover
AMFDRDataLocalMultiCommitPatch
AMFDREncodeMultiRequestBegin
AMFDRSealingMapSetSikOverride
Unable to create CSR GID signature
missingDataInstances has wrong type %@
failed to decode property
keysInPatchDict is NULL
AMFDRSetSsoCreateServiceTicketCallback
Cannot get property tag from entry %ld
dm/claim
find the exeNode, dataClass:%@
Skipping empty inner header
secondaryDataClassInstance has wrong type %@
_AMFDRSealedDataCopyAndCommitIntraFactoryData
Cannot add data class and instance from %@ to dictionary
failed to open connection to %s: %d\n
failed to add dataInstance
componentTypeData is NULL
malformed FDR2 Format (manifest2)
```
