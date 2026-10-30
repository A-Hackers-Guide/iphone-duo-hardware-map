# `/usr/lib/libFDRDecode.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 179,552 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 19 (Size: 1680)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (3)

- `/usr/lib/libFDRDecode.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`

## Entitlements

```xml
  - no entitlements
```

## Strings (446)

```
%s: Re-evaluation succeeded but decode options require version2
%s: publicKeyParam is NULL!!
%s: PKI: verify cert was issued by trusted root %d (success)
AMFDRDecodeGetImg4Manifest
%s: malformed FDR2 Format, invalid tag length
%s: metaPropertyCallback failed with error 0x%llX
%s: failed to decode the signed section
_AMFDRDecodeVerifyTestStationManifestInternal
%s: Skip verifying assembly identifier
%s: fdrDecode->dataImg4.payload_hashed is false
%s: asid subCC data != fdrDecode->asidSubCCID
%s: can't parse FDR Trust Object Revoked sequence
%s: malformed FDR Metadata Record Format
%s: Img4DecodeEvaluateManifestProperties failed
%s: found data in multi combined format
AMFDRDecodeVerifyCertIssuerWithOptions
%s: decoded IM4C signature is empty
%s: trustobject does not contain trusted key
_AMFDRDecodeGetDataInfoCallback
%s: malformed FDR Trust Object Format
%s: malformed FDR Trust Object trusted key, invalid trusted key tag length
%s: outTrustObject must be non NULL and outTrustObjectLength must be non 0
%s: AMSupportDigestSha1 failed
_AMFDRDecodeVerifyTrustObject
%s: kFDRTag_asid property length != fdrDecode->assemblyID.length
%s: AMFDRDecodeIterateTrustObjectTrustedBegin failed
%s: item is bigger on the inside
AMFDRDecodeMetaProperty
%s: failed to parse payload content: %d
%s: multiple entries for tag 0x%llu found, but no unique ID specified
%s: cannot find tag in property list
%s: PKI: verify cert was issued and signed by issuer (success)
%s: AMFDRDecodeIterateTrustObjectTrustedNext failed
_AMFDRDecodeMultiSealingResposeRecords
AMFDRDecodeFindSubCCAndReturnAsPayload
%s: fdrDecode is NULL
%s: Img4DecodeGetPropertyData(kFDRTag_cptp) failed.
%s: Unsupported tag found in manifest '%c%c%c%c'
%s: malformed DERFDRItem, invalid tag length
%s: end of trusted root sequence found root_cert=%d
%s: Sealing manifest is NULL or 0 length
%s: failed to decode FDR2 Format
%s: offline signing public key length mismatch
%s: malformed FDR Multi-Response Error Format
AMFDRDecodeMultiSealingResponse
%s: malformed FDR2 Format, expected tag %c%c%c%c found tag %c%c%c%c
%s: FDR Trust Object digest size not supported. digest is of size %zu
%s: asid subCC length != fdrDecode->asidSubCCID.length
%s: malformed FDR Combined Format (trustObject)
%s: found multiple entries that match, uniqueID is required in this case
%s: malformed AttributeTypeAndValue format: %d
%s: Record must be SEQUENCE Container
%s: failed to allocate *multiCombinedDataIterator
%s: version size is invalid: %lu
%s: FDR Trust Object digest mismatch.
%s: kFDRTag_inst property == fdrDecode->uniqueID, found corresponding Data Instance.
%s: FDR data trust evaluation failed.
%s: ignoring unsealed error 0x%016llX
%s: publicKeyParam is NULL
%s: unexepcted items in offline blob
%s: invalid key length: %lu
%s: kFDRTag_cptp property != fdrDecode->componentType
%s: no data instance is specified when looking for data in multi combined format
%s: PKI: decoding trusted root %d failed with error 0x%016llX
%s: malformed FDR Trust Object Revoked, expected tag %c%c%c%c found tag %c%c%c%c
AMFDRDecodePublicKey
%s: malformed FDR2 Format (DERFDRItemSpecs)
%s: DERImg4DecodePropertyWithItem failed
%s: malformed FDR Combined Format, invalid tag length
%s: cannot find data in multi combined format
%s: Failed to get payload sequence and set manifest from multi combined data
%s: malformed im4c tag: %c%c%c%c
%s: malformed FDR2 Format, invalid fdr2Data.tag.length
%s: Img4DecodeGetPropertyData(kFDRTag_SCDG) failed.
%s: malformed FDR Combined Format (trustObject), invalid tag length
%s: FDR failed to get restitched manifest from multi combined data
%s: PKI: verify im4c cert was issued and signed by issuer (success)
%s: missing public key algorithm parameter OID
%s: _AMFDRDecodeMultiSealingResposeRecords failed with error 0x%llX
AMFDRDecodeIterateSysconfigBegin
%s: kFDRTag_inst propertyValue (sik) != sikValue
%s: PKI: verify cert was issued by trusted key %d (success)
%s: publicKey must be non NULL and publicKeyLength must be non 0
%s: Expecting kAMFDRDecodeImplementationSha384 or kAMFDRDecodeImplementationOffline
%s: malformed FDR Trust Object, expected tag %c%c%c%c found tag %c%c%c%c
%s: failed to decode sealing manifest tag
%s: inData must be non NULL and inDataLength must be non 0
%s: MetadataRecord must be SEQUENCE Container
AMFDRDecodeFDR2Data
AMFDRDecodeCreateCertificate
%s: FDR Sealing Manifest failed to decode sealing manifest
_AMFDRDecodeGetExpectedManifestHash
AMFDRDecodeIterateTrustObjectTrustedBegin
%s: propertyValue != kFDRTagStr_sreq
%s: propertyValue != fdrDecode->sealingManifestImg4.payload.hash
AMFDRDecodeEvaluateTrustInternal
%s: kAMFDRDecodeOptionManifestOnly, kAMFDRDecodeOptionSubCCOnly, kAMFDRDecodeOptionDataDigestOnly needs to be exclusive to each other
%s: trust evaluation on customized payload format requires a reStitchManifest
%s: Evaluation returned code=0x%016llX, re-evaluate with FDR 2.0 format
%s: Re-evaluation returned code=0x%016llX
%s: malformed FDR Trust Object trusted key, expected tag %c%c%c%c found tag %c%c%c%c
%s: can't parse FDR Trust Object SslRoot
AMFDRDecodeVerifyMultiCombinedDataIntegrity
%s: unexpected signed section tag: 0x%llx
%s: failed to parse public key of im4c: %d
%s: DERMemcmp failed.
_AMFDRDecodeInstPropertyMatching
%s: kFDRTag_inst propertyLength (sik) (%d) != sikLength (%zu)
%s: ctx->inData must be non NULL and ctx->inDataLength must be non 0
%s: failed to find object properties
_AMFDRDecodeVerifySealingRequestInternal
%s: propertyLength != kImg4TagSize
%s: kFDRTag_inst propertyLength (sik) (%d) <= instLength (%zu)
%s: subCC digest mismatch
%s: Invalid data digest input
%s: failed to decode all sequences: %d
%s: malformed FDR Trust Object Revoked, invalid trusted tag length
%s: Metadata must be SET Container
%s: No need to verify subCC and asid
%s: No SCDG in manifest, subCC digest missing
%s: cannot decode to a multicombined data, proceed with combined format
%s: _AMFDRDecodeIterateCertChainBegin failed
%s: PKI: decoding trusted key %d failed with error 0x%016llX
AMFDRDecodeIterateTrustObjectRevokedBegin
%s: Failed decoding next item in sealing manifest contents
%s: could not parse sealing manifest
%s: subCC is not hashed
%s: revocation check failed
%s: Skipping trust root check (trustobject unset)
_AMFDRDecodeMultiResposeRecords
%s: public key OID is not EC
%s: invalid payload tag: 0x%llx
_AMFDRDecodeVerifyData
decode error
%s: malformed FDR Multi-Response value Format
%s: Failed to malloc fdrDecode
%s: memcmp( uniqueIDInfo.content.data, uniqueID, uniqueIDLength) != 0
%s: failed to decode DER
AMFDRDecodeMetadata
%s: FDR Sealing Request is missing
%s: subCC digest length mismatch
%s: failed to decode FDR Multi Combined Format
%s: ignoring trust object mismatch error 0x%016llX
%s: failed to decode sysconfig payload: %d
%s: failed to find property in the manifest
%s: %s: signature validation failed
%s: ignoring raw error 0x%016llX
%s: outImg4Blob must be non NULL and outImg4BlobLength must be non 0
%s: malformed offline signing public key
%s: can't parse FDR Multi-response payload
%s: can't parse FDR Trust Object Revoked
%s: can't decode manifest from Img4DecodeInitManifest, but it might be multi-manifest
%s: Outer DER did not terminate properly.
%s: Img4DecodeGetPropertyData(0x%x) failed.
%s: malformed FDR Trust Object trusted, expected tag %c%c%c%c found tag %c%c%c%c
%s: FDR Sealing Manifest failed to decode sequence
%s: failed to decode sysconfig metadata: %d
%s: data instance cannot be missing without kAMFDRDecodeOptionAllowNoDataInstance specified
%s: failed to parse property list
%s: PKI: verify cert %d was issued by %d (success)
_AMFDRDecodeVerifyChainOffline
%s: Records must be SET Container
%s: Certificate Properties extension not found
AMFDRDecodeImage4Certificate
AMFDRDecodeManifestBodyNext
%s: Img4DecodeEvaluateObjectProperties failed
%s: sealingManifestCallback failed with error 0x%llX
%s: failed to decode subCC digests sequence
%s: PKI: verify cert %d was issued by cert %d
%s: unsupported meta property type
%s: Img4DecodeGetPropertyData(kFDRTag_inst) failed.
%s: FDR Sealing Request trust evaluation failed.
_AMFDRDecodeVerifySubCC
%s: malformed attribute: %d
%s: AMFDRDecodeIterateTrustObjectRevokedBegin failed
%s: failed to decode payload: %d
AMFDRDecodeCreateCertificateChain
%s: multi combined payload type is not mcmb
%s: payload sequence malformed for multi combined data
%s: _AMFDRDecodeIterateCertChainNext failed (first call)
AMFDRDecodeTrustObject
AMFDRDecodeCheckCertRevocation
%s: failed to decode offline blob Format
AMFDRDecodeOfflineBlob
%s: failed to find MANB (manifest body) tag
%s: invalid metadata tag: 0x%llx
%s: unexpected property type != kImg4ObjectProperty
%s: PKI: cert was not issued by issuer (subject != issuer)
%s: can't parse FDR Producer ID sequence
AMFDRDecodeVerifySealingRequest
%s: outData must be non NULL and outDataLength must be non 0
%s: magic size is invalid: %lu
%s: Img4DecodeGetPropertyData(kFDRTag_prid) failed.
%s: Record value is NULL
%s: failed to init certificate sequence
%s: failed to find property tag 0x%llu
%s: kFDRTag_inst property != fdrDecode->uniqueID
%s: verifying subCC, skip comparing digest of the entire data
%s: AMFDRDecodeCheckProducerIDRevocation
%s: outRawData must be non NULL and outRawDataLength must be non 0
%s: failed to decode public key: %d
%s: malformed cert property key: %c%c%c%c
%s: FDR Trust Object revoked public key found
%s: FDR Trust Object revoked client ID found
%s: malformed FDR Multi-Response Payload Format
%s: failed to get CSR signature from offline blob
%s: failed to decode sealing manifest body
%s: malformed offline blob
%s: pManifestBodyInfo is NULL
%s: Inner DER did not terminate properly.
%s: kFDRTag_inst propertyValue != fdrDecode->manifestUniqueID.data
%s: Payload version mismatch
%s: Invalid data class length
_AMFDRDecodeVerifySignatureDataWithOid
%s: malformed FDR Multi-Response actionCode Format
_AMFDRDecodeVerifySealingManifestInternal
%s: evaluateCertificateProperties failed
%s: fdrDecode->uniqueID is NULL or 0 size
_AMFDRDecodeVerifySignature
%s: End of Inner Sequence found, before any valid DER.
%s: failed to find MANP (manifest payload) tag
%s: Img4DecodeGetPropertyData(kImg4Tag_DGST) failed.
%s: malformed FDR Combined Format, expected tag %c%c%c%c found tag %c%c%c%c
%s: FDR Multi Combined Format unexpected tag: %llu
_AMFDRDecodeTolerateErrorsForOptions
%s: end of trusted key sequence found root_key=%d
%s: PKI: verify cert was issued by trusted root %d failed with error 0x%016llX
%s: AMFDRDecodeIterateProducerIDBegin failed with error 0x%016llX
%s: malformed FDR2 Format (manifest2), invalid tag length
%s: malformed Img4 Manifest (version parse fail)
%s: minor version not supported: 0x%x
%s: Failed to malloc empty certificate chain
%s: validation failed for property 0x%llX - tag present
%s: kFDRTag_inst property != fdrDecode->manifestUniqueID
_AMFDRDecodeSearchEntryFromPropertyList
%s: can't parse FDR Trust Object trusted sequence
AMFDRDecodeIterateTrustObjectSslRootBegin
AMFDRDecodeEvaluateTrustCombinedWithSik
%s: failed to parse im4c: %d
AMFDRDecodeManifestBody
%s: End of Outer Sequence found, before any valid DER.
%s: malformed DERFDRItem, expected tag %c%c%c%c found tag %c%c%c%c
%s: kFDRTag_inst propertyLength (%d) != instLength (%zu)
%s: malformed FDR Trust Object SslRoot, expected tag %c%c%c%c found tag %c%c%c%c
%s: can't parse sealing manifest contents classItem
%s: malformed metaProperty Format
_AMFDRDecodeVerifyDataCallback
%s: Payload version is wrong size. got %zu expected %d
%s: PKI: verify cert was issued by trusted key %d
%s: PKI: check payload hash with signature (success)
%s: offline signing public key mismatch
%s: Skip verifying type info
%s: FDR failed to get payload type
%s: malformed FDR Combined Format (DERFDRItemSpecs)
%s: PKI: verify cert %d was issued by cert %d failed with error 0x%016llX
%s: Record value must be OCTET_STRING
AMFDRDecodeSealingRequest
%s: Invalid out pointers
%s: failed to find corresponding component type
%s: failed to parse certificate dictionary
_AMFDRDecodeVerifySealingRequestCallback
_AMFDRDecodeFilterDataInstanceCallback
%s: cannot find subCC digest for %u
%s: buffer is NULL
%s: can't parse FDR property meta
%s: manifest or object property length does not match
%s: %s: certificate chain validation failed
%s: kFDRTag_inst propertyValue != instValue
IM4P
%s: FDR failed to get payload type from multi combined data
%s: failed to begin decoding trusted key
%s: fail to decode certificate of offline signing
AMFDRDecodeIterateTrustObjectTrustedKeyBegin
AMFDRDecodeVerifyTestStationManifest
%s: subCCName cannot be NULL when kAMFDRDecodeOptionSubCCOnly is set.
%s: digestLength is %zu, expecting %zu
%s: malformed FDR Multi-Response Error Code Format
%s: context is NULL
%s: can't parse FDR Trust Object trusted key: %d
%s: unsupported public key length: %lu
%s: failed to get attestation from offline blob
%s: sysconfig context is not initialized
%s: kFDRTag_inst propertyLength (%d) != fdrDecode->manifestUniqueID.length (%zu)
%s: property is NULL
%s: Staged sealing is not allowed
%s: signature must be non NULL and publicKeyLsignatureLengthength must be non 0
%s: Found subCC %c%c%c%c
%s: malformed FDR Multi-Response Format
%s: Buffer contains %lu unused bytes
%s: failed to find matching inst object propery, returning a mismatched one
%s: kFDRTag_inst propertyValue (sik) != instValue
_AMFDRDecodeCombined
%s: FDR failed to decode multi combined Data img4
%s: FDR failed to get payload from multi combined data
%s: can't parse sealing manifest top-level container
%s: can't parse sealing manifest top-level container. Expected tag %llu, found %llu
%s: failed to decode params
AMFDRDecodeMultiResponse
%s: failed to parse sysconfig sequence: %d
%s: Evaluation returned code=0x%016llX, re-evaluate with FDR 1.0 format
%s: PKI: im4c cert signature validation with issuer pubkey failed
%s: decodeAlgId failed
%s: FDR Trust Object revoked certificate found
%s: Failed to find subCC %c%c%c%c
%s: Img4DecodeGetObjectPropertyData failed
%s: validation failed for property 0x%llX
%s: FDR Trust Object is NULL
%s: PKI: verify cert was issued by trusted root %d
%s: digest must be non NULL and digestLength must be non 0
%s: invalid digest length
%s: can't parse FDR Trust Object trusted
%s: MultiCombinedItem malformed for multi combined data
AMFDRDecodeCombined
%s: FDR2 Format unexpected tag: %llu
%s: can't parse top-level container
%s: kFDRTag_cptp property length != fdrDecode->componentType.length
%s: Payload type mismatch
%s: ignoring incomplete subcc error 0x%016llX
AMFDRDecodeCheckProducerIDRevocation
AMFDRDecodeEvaluateTrustOffline
AMFDRDecodeParseDERLengthFromBuffer
%s: malformed FDR2 Format (manifest2), expected tag %c%c%c%c found tag %c%c%c%c
%s: propertyLength != AMFDRDigestSize
%s: uniqueID is not specified, which is allowed, skip uniqueID mismatch errors
%s: Img4DecodeGetPropertyData(kFDRTag_asid) failed.
%s: FDR failed to decode manifestOverride
%s: cannot begin with an already initialized iterator
%s: failed to find corresponding data instance
%s: _AMFDRDecodeManifestBodyNext failed
%s: Failed to malloc empty certificate
_AMFDRDecodeEvaluateCertificateProperties
%s: Img4DecodeGetPropertyData(kFDRTag_SrvT) failed.
_AMFDRDecodeFindDataFromMultiCombined
_AMFDRDecodeVerifyMultiCombinedDataInternal
AMFDRDecodeVerifySealingManifest
%s: can't parse sealing manifest tag. Expected tag %d, found %llu
%s: FDR 3.0 Data can't be decoded!
%s: failed to parse cert properties: %d
%s: malformed FDR2 Format (manifest2)
%s: can't parse content of MinimalManifestMetaData
%s: can't parse DERDecodeSeqNext
AMFDRDecodeIterateSysconfigPayloadNext
%s: _AMFDRDecodeMultiResposeRecords failed with error 0x%llX
%s: unexpected tag 0x%llX in certificate properties
%s: AMFDRDecodeCheckProducerIDRevocation failed with error 0x%016llX
_AMFDRDecodeDERFDRItem
_AMFDRDecodePropertiesFilterCallback
%s: kFDRTag_asid property != fdrDecode->assemblyID
%s: subCC digest verified
%s: data is unwrapped
%s: malformed FDR Trust Object SslRoot, invalid trusted tag length
%s: FDR Sealing Manifest is missing
%s: FDR Sealing Request failed to decode img4
%s: Re-evaluation succeeded
%s: malformed FDR Combined Format (trustObject), expected tag %c%c%c%c found tag %c%c%c%c
%s: im4c revocation check failed
%s: context must be non NULL
%s: malformed FDR Multi-Response Payload Record Format
%s: ClientID extension not found
%s: malformed DERFDRItem
%s: failed to decode FDR Combined Format
%s: malformed offline signing public key tag
%s: Record value length is 0
%s: multiResponseCallback failed with error 0x%llX
%s: AMFDRDecodeIterateTrustObjectRevokedNext failed
%s: AMFDRDecodeVerifySealingManifest 0x%016llX
%s: fdrDecode->sealingRequestImg4.payload_hashed is false
%s: FDR Combined Format unexpected tag: %llu
%s: trustObject is NULL
%s: numUnused != 0
%s: _AMFDRDecodeIterateCertChainNext failed (%d)
%s: implementation must be non NULL and signatureOid must be non NULL
AMFDRDecodeIterateProducerIDBegin
AMFDRDecodeIterateMultiCombinedDataBeginWithRawData
%s
%s: propertyValue must be non NULL with a non-zero length (length=%u)
_Img4DecodeInitDummyPayloadForDataDigest
%s: combinedData is required to be set
%s: subject: %s, issuer: %s
_AMFDRDecodeSequenceString
%s: can't parse FDR Trust Object SslRoot sequence
%s: malformed FDR Trust Object, invalid tag length
%s: can't parse FDR Multi-response Metadata
AMFDRDecodeManifestBodyInfoNext
%s: Skipping revocation check (trustobject unset)
%s: kFDRTag_asid doesn't exist, but this is allowed
%s: No restitch manifest, but allow unsealed, try to proceed with the data manifest...
%s: failed to init sequence
%s: AMFDRDecodeIterateProducerIDNext(loop) failed with error 0x%016llX
AMFDRDecodeEvaluateTrustWithSik
%s: failed to parse signed section sequence: %d
%s: AMSupportDigestSha256 failed
%s: Img4DecodeGetPropertyData(kFDRTag_clas) failed.
%s: _AMFDRDecodeVerifyTrustObject failed (%llu), continuing.
%s: no uniqueID is specified, but this is allowed, skip comparing kFDRTag_inst object property
%s: ignoring no trustobject error 0x%016llX
%s: No manifest found - not evaluated.
_AMFDRDecodeVerifySealingManifestCallback
%s: can't parse FDR Trust Object trusted key sequence
%s: ctx must be non NULL
%s: can't parse MinimalManifestMetaData
%s: failed to parse boolean: %d
%s: failed to parse certificate property
%s: uniqueIDInfo.content.length != uniqueIDLength
%s: failed to decode payload: 0x%llx!
%s: failed to parse signed section of im4c: %d
%s: FDR failed to decode Data img4
%s: failed to get CSR from offline blob
%s: decoded IM4C signature OID is empty
_AMFDRDecodeVerifyChain
%s: PKI: verify cert was issued by trusted key %d failed with error 0x%016llX
AMFDRDecodeCertificate
%s: malformed im4c tag length: %lu
%s: outRawData and outRawDataLength must be non NULL
%s: sysconfig version not supported: 0x%x
%s: FDR Trust Object digest is NULL
%s: Invalid data digest length: %ld
_AMFDRDecodeGetPayloadSeqAndSetManifestFromMultiCombinedData
%s: DERParseBitString(sig) failed
%s: AMFDRDecodeIterateProducerIDNext(first) failed with error 0x%016llX
%s: malformed cert property key length: %lu
AMFDRDecodeTrustEvaluation
%s: Img4DecodeGetPropertyData(kFDRTag_faic) failed.
%s: propertyLength != implementation->digestInfo->digestOutputSize
%s: failed to find subCC digest
%s: ignoring offline signing verification error 0x%016llX
%s: PKI: cert signature validation with issuer pubkey failed
%s: signed section has an unexpected tag
%s: failed to certificate dictionary
%s: no uniqueID is specified, cannot verify kFDRTag_inst property
%s: Invalid property length of kFDRTag_SrvT
AMFDRDecodeEvaluateTrustOfflineInternal
_AMFDRDecodeVerifyCertIssuerInternal
%s: chain_blob must be non NULL and chain_blob_length must be non 0
%s: _AMFDRDecodeIterateCertChainNext failed (second call)
AMFDRDecodeIterateMultiCombinedDataNext
%s: unsupported signature length: %lu
%s: metadataRecordCallback failed with error 0x%llX
%s: kFDRTag_inst propertyValue missing expected -
%s: not verifying subCC payload, skip checking subCC digest
%s: Attribute must be set container. Found unexpected tag 0x%llu, skipping
%s: missing IM4C leaf public key OID
%s: malformed FDR Trust Object trusted, invalid trusted tag length
%s: found an empty data class in multi combined data
%s: manifest or object missing required property '%c%c%c%c'
_AMFDRDecodeVerifyImage4CertIssuer
```
