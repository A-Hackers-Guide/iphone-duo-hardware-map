# `/usr/lib/libFDRDecode.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 179,552 bytes.

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
%s: propertyLength != implementation->digestInfo->digestOutputSize
%s: malformed FDR Trust Object, expected tag %c%c%c%c found tag %c%c%c%c
%s: malformed FDR Trust Object trusted, expected tag %c%c%c%c found tag %c%c%c%c
%s: failed to parse im4c: %d
%s: malformed FDR2 Format (DERFDRItemSpecs)
%s: sealingManifestCallback failed with error 0x%llX
%s: propertyLength != AMFDRDigestSize
%s: malformed DERFDRItem
%s: PKI: verify im4c cert was issued and signed by issuer (success)
AMFDRDecodeIterateTrustObjectSslRootBegin
AMFDRDecodeCreateCertificateChain
%s: fdrDecode is NULL
%s: kFDRTag_inst propertyValue != instValue
%s: Invalid data class length
%s: FDR failed to decode multi combined Data img4
%s: Expecting kAMFDRDecodeImplementationSha384 or kAMFDRDecodeImplementationOffline
%s: Img4DecodeGetPropertyData(0x%x) failed.
%s: failed to decode payload: 0x%llx!
%s: metadataRecordCallback failed with error 0x%llX
%s: manifest or object property length does not match
%s: kFDRTag_inst property != fdrDecode->manifestUniqueID
%s: Img4DecodeGetPropertyData(kFDRTag_SCDG) failed.
%s: failed to decode public key: %d
%s: failed to parse cert properties: %d
%s: sysconfig context is not initialized
%s: manifest or object missing required property '%c%c%c%c'
%s: kAMFDRDecodeOptionManifestOnly, kAMFDRDecodeOptionSubCCOnly, kAMFDRDecodeOptionDataDigestOnly needs to be exclusive to each other
%s: signed section has an unexpected tag
%s: version size is invalid: %lu
_AMFDRDecodeVerifySealingRequestInternal
%s: data instance cannot be missing without kAMFDRDecodeOptionAllowNoDataInstance specified
%s: subCC digest length mismatch
AMFDRDecodeEvaluateTrustInternal
%s: Evaluation returned code=0x%016llX, re-evaluate with FDR 1.0 format
_AMFDRDecodeGetPayloadSeqAndSetManifestFromMultiCombinedData
%s: AMFDRDecodeIterateProducerIDBegin failed with error 0x%016llX
%s: kFDRTag_inst propertyLength (%d) != instLength (%zu)
%s: Invalid property length of kFDRTag_SrvT
%s: cannot find data in multi combined format
%s: fail to decode certificate of offline signing
%s: FDR Trust Object digest mismatch.
%s: malformed FDR Metadata Record Format
%s: malformed FDR Trust Object SslRoot, expected tag %c%c%c%c found tag %c%c%c%c
%s: FDR Trust Object revoked certificate found
%s: property is NULL
%s: no uniqueID is specified, cannot verify kFDRTag_inst property
_AMFDRDecodeCombined
%s: malformed FDR Combined Format (trustObject)
%s: failed to allocate *multiCombinedDataIterator
%s: Inner DER did not terminate properly.
%s: FDR failed to decode manifestOverride
%s: end of trusted root sequence found root_cert=%d
_AMFDRDecodeMultiSealingResposeRecords
%s: uniqueIDInfo.content.length != uniqueIDLength
%s: failed to parse boolean: %d
%s: combinedData is required to be set
%s: revocation check failed
_AMFDRDecodeVerifyChainOffline
%s: malformed FDR Multi-Response Error Code Format
%s: FDR Trust Object is NULL
%s: Failed decoding next item in sealing manifest contents
%s: AMFDRDecodeIterateTrustObjectRevokedNext failed
AMFDRDecodeOfflineBlob
%s: unexpected tag 0x%llX in certificate properties
%s: propertyLength != kImg4TagSize
%s: malformed DERFDRItem, invalid tag length
%s: Skip verifying type info
%s: Img4DecodeEvaluateObjectProperties failed
%s: no uniqueID is specified, but this is allowed, skip comparing kFDRTag_inst object property
%s: kFDRTag_cptp property length != fdrDecode->componentType.length
%s: asid subCC data != fdrDecode->asidSubCCID
_AMFDRDecodeVerifyCertIssuerInternal
%s: _AMFDRDecodeIterateCertChainBegin failed
%s: PKI: verify cert was issued by trusted root %d
%s: AMFDRDecodeIterateTrustObjectTrustedNext failed
AMFDRDecodeCheckCertRevocation
%s: malformed metaProperty Format
_AMFDRDecodeVerifySealingManifestInternal
%s: %s: certificate chain validation failed
%s: propertyValue != kFDRTagStr_sreq
%s: fdrDecode->sealingRequestImg4.payload_hashed is false
%s: uniqueID is not specified, which is allowed, skip uniqueID mismatch errors
%s: asid subCC length != fdrDecode->asidSubCCID.length
%s: Failed to malloc fdrDecode
%s: failed to decode params
%s: invalid metadata tag: 0x%llx
%s: End of Outer Sequence found, before any valid DER.
%s: AMSupportDigestSha1 failed
%s: Img4DecodeGetPropertyData(kFDRTag_clas) failed.
%s: FDR failed to get payload type
%s: FDR data trust evaluation failed.
%s: Found subCC %c%c%c%c
%s: _AMFDRDecodeMultiSealingResposeRecords failed with error 0x%llX
AMFDRDecodeIterateSysconfigPayloadNext
%s: PKI: im4c cert signature validation with issuer pubkey failed
%s: malformed offline signing public key
%s: offline signing public key length mismatch
%s: malformed FDR Multi-Response Error Format
%s: failed to get attestation from offline blob
AMFDRDecodeEvaluateTrustOfflineInternal
%s: malformed FDR Combined Format (DERFDRItemSpecs)
_AMFDRDecodeVerifySignatureDataWithOid
%s: ctx->inData must be non NULL and ctx->inDataLength must be non 0
%s: invalid payload tag: 0x%llx
%s: multi combined payload type is not mcmb
_AMFDRDecodeTolerateErrorsForOptions
%s: ignoring offline signing verification error 0x%016llX
%s: ignoring no trustobject error 0x%016llX
_AMFDRDecodeVerifyChain
%s: PKI: verify cert was issued by trusted key %d (success)
%s: subCCName cannot be NULL when kAMFDRDecodeOptionSubCCOnly is set.
%s: trust evaluation on customized payload format requires a reStitchManifest
%s: Payload version mismatch
%s: subject: %s, issuer: %s
%s: _AMFDRDecodeIterateCertChainNext failed (second call)
%s: AMFDRDecodeIterateProducerIDNext(loop) failed with error 0x%016llX
%s: memcmp( uniqueIDInfo.content.data, uniqueID, uniqueIDLength) != 0
%s: Buffer contains %lu unused bytes
%s: failed to parse sysconfig sequence: %d
%s: Failed to malloc empty certificate
AMFDRDecodeCreateCertificate
%s: validation failed for property 0x%llX - tag present
_AMFDRDecodeVerifySealingManifestCallback
AMFDRDecodeTrustObject
%s: Sealing manifest is NULL or 0 length
%s: Certificate Properties extension not found
_AMFDRDecodeVerifyDataCallback
%s: Evaluation returned code=0x%016llX, re-evaluate with FDR 2.0 format
%s: FDR failed to get restitched manifest from multi combined data
%s: No restitch manifest, but allow unsealed, try to proceed with the data manifest...
%s: ignoring unsealed error 0x%016llX
%s: malformed FDR Trust Object Revoked, invalid trusted tag length
%s: FDR Trust Object revoked public key found
AMFDRDecodeParseDERLengthFromBuffer
%s: failed to decode FDR2 Format
%s: malformed FDR2 Format (manifest2), expected tag %c%c%c%c found tag %c%c%c%c
AMFDRDecodeIterateSysconfigBegin
%s: PKI: cert was not issued by issuer (subject != issuer)
%s: malformed FDR Trust Object SslRoot, invalid trusted tag length
%s: can't decode manifest from Img4DecodeInitManifest, but it might be multi-manifest
%s: failed to decode the signed section
%s: no data instance is specified when looking for data in multi combined format
_AMFDRDecodeVerifyImage4CertIssuer
_AMFDRDecodeVerifySignature
%s: Failed to find subCC %c%c%c%c
%s: MultiCombinedItem malformed for multi combined data
%s: malformed FDR2 Format (manifest2)
_AMFDRDecodeEvaluateCertificateProperties
%s: failed to find property tag 0x%llu
%s: Img4DecodeGetPropertyData(kFDRTag_SrvT) failed.
%s: failed to decode FDR Multi Combined Format
%s: FDR Multi Combined Format unexpected tag: %llu
%s: failed to parse public key of im4c: %d
%s: FDR failed to decode Data img4
%s: can't parse sealing manifest contents classItem
AMFDRDecodeCertificate
%s: unexpected signed section tag: 0x%llx
%s: kFDRTag_asid property != fdrDecode->assemblyID
%s: Invalid data digest input
%s: trustobject does not contain trusted key
%s: malformed FDR Trust Object trusted key, expected tag %c%c%c%c found tag %c%c%c%c
%s: FDR Sealing Request trust evaluation failed.
%s: kFDRTag_inst propertyValue (sik) != instValue
%s: subCC digest verified
%s: publicKey must be non NULL and publicKeyLength must be non 0
%s: Img4DecodeGetPropertyData(kFDRTag_faic) failed.
%s: malformed im4c tag: %c%c%c%c
%s: _AMFDRDecodeMultiResposeRecords failed with error 0x%llX
%s: Metadata must be SET Container
%s: failed to get CSR from offline blob
AMFDRDecodeManifestBodyNext
%s: failed to decode payload: %d
%s: validation failed for property 0x%llX
%s: inData must be non NULL and inDataLength must be non 0
AMFDRDecodeSealingRequest
%s: found an empty data class in multi combined data
%s: failed to certificate dictionary
%s: propertyValue != fdrDecode->sealingManifestImg4.payload.hash
_AMFDRDecodeDERFDRItem
%s: malformed DERFDRItem, expected tag %c%c%c%c found tag %c%c%c%c
%s: multiple entries for tag 0x%llu found, but no unique ID specified
%s: outData must be non NULL and outDataLength must be non 0
%s: malformed FDR Multi-Response actionCode Format
%s: Img4DecodeGetPropertyData(kImg4Tag_DGST) failed.
AMFDRDecodeVerifyTestStationManifest
%s: kFDRTag_inst propertyValue missing expected -
%s: kFDRTag_asid property length != fdrDecode->assemblyID.length
_AMFDRDecodeSearchEntryFromPropertyList
%s: Payload type mismatch
%s: can't parse FDR Trust Object trusted
%s: can't parse sealing manifest tag. Expected tag %d, found %llu
%s: outTrustObject must be non NULL and outTrustObjectLength must be non 0
%s: magic size is invalid: %lu
%s: propertyValue must be non NULL with a non-zero length (length=%u)
%s: Img4DecodeGetPropertyData(kFDRTag_asid) failed.
%s: not verifying subCC payload, skip checking subCC digest
%s: Img4DecodeGetPropertyData(kFDRTag_cptp) failed.
%s: can't parse FDR Producer ID sequence
%s: failed to decode sealing manifest tag
AMFDRDecodeMetadata
%s: FDR Sealing Manifest is missing
_AMFDRDecodeVerifyData
%s: malformed FDR Combined Format, invalid tag length
%s: malformed FDR Combined Format (trustObject), invalid tag length
%s: DERParseBitString(sig) failed
%s: can't parse FDR Trust Object Revoked
AMFDRDecodeFindSubCCAndReturnAsPayload
%s: failed to parse signed section of im4c: %d
%s: Failed to malloc empty certificate chain
%s: failed to init certificate sequence
%s: cannot decode to a multicombined data, proceed with combined format
%s: PKI: verify cert was issued by trusted key %d
%s: digest must be non NULL and digestLength must be non 0
%s: failed to decode sealing manifest body
%s: FDR Trust Object revoked client ID found
%s: _AMFDRDecodeManifestBodyNext failed
%s: FDR Sealing Request is missing
%s: Re-evaluation succeeded
IM4P
%s: PKI: verify cert %d was issued by cert %d
%s: signature must be non NULL and publicKeyLsignatureLengthength must be non 0
AMFDRDecodeIterateProducerIDBegin
%s: can't parse FDR Trust Object SslRoot
_AMFDRDecodeVerifyTestStationManifestInternal
%s: found data in multi combined format
%s: decoded IM4C signature is empty
%s: PKI: cert signature validation with issuer pubkey failed
%s: failed to init sequence
%s: malformed AttributeTypeAndValue format: %d
AMFDRDecodeIterateTrustObjectTrustedBegin
%s: malformed FDR2 Format, expected tag %c%c%c%c found tag %c%c%c%c
%s: AMFDRDecodeCheckProducerIDRevocation failed with error 0x%016llX
%s: failed to decode subCC digests sequence
%s: cannot find tag in property list
%s: data is unwrapped
%s: publicKeyParam is NULL!!
%s: malformed FDR Multi-Response Payload Record Format
AMFDRDecodeEvaluateTrustCombinedWithSik
%s: FDR2 Format unexpected tag: %llu
%s: unexepcted items in offline blob
%s: can't parse FDR property meta
%s: failed to decode sysconfig payload: %d
%s: fdrDecode->uniqueID is NULL or 0 size
%s: FDR Combined Format unexpected tag: %llu
%s: context is NULL
%s: malformed FDR Trust Object Format
%s: malformed FDR Trust Object, invalid tag length
%s: unsupported public key length: %lu
%s: minor version not supported: 0x%x
%s: kFDRTag_inst property != fdrDecode->uniqueID
%s: No SCDG in manifest, subCC digest missing
%s: failed to decode FDR Combined Format
%s: context must be non NULL
AMFDRDecodeMultiResponse
%s: metaPropertyCallback failed with error 0x%llX
%s: No need to verify subCC and asid
%s: can't parse FDR Multi-response payload
%s: malformed FDR Multi-Response value Format
AMFDRDecodeIterateTrustObjectTrustedKeyBegin
%s: outRawData and outRawDataLength must be non NULL
%s: pManifestBodyInfo is NULL
%s: End of Inner Sequence found, before any valid DER.
%s: PKI: verify cert was issued by trusted root %d (success)
%s: malformed offline signing public key tag
%s: digestLength is %zu, expecting %zu
%s: Records must be SET Container
AMFDRDecodeVerifySealingManifest
%s: FDR 3.0 Data can't be decoded!
%s: failed to parse certificate property
%s: failed to find subCC digest
%s: numUnused != 0
%s: FDR Trust Object digest is NULL
%s: can't parse FDR Trust Object trusted key sequence
%s: AMFDRDecodeIterateTrustObjectRevokedBegin failed
%s: can't parse sealing manifest top-level container
%s: can't parse sealing manifest top-level container. Expected tag %llu, found %llu
AMFDRDecodeFDR2Data
%s: ctx must be non NULL
%s: invalid key length: %lu
%s: AMFDRDecodeCheckProducerIDRevocation
%s: can't parse FDR Trust Object SslRoot sequence
AMFDRDecodeTrustEvaluation
%s
%s: No manifest found - not evaluated.
_AMFDRDecodeFilterDataInstanceCallback
%s: kFDRTag_inst property == fdrDecode->uniqueID, found corresponding Data Instance.
%s: kFDRTag_inst propertyLength (sik) (%d) <= instLength (%zu)
%s: can't parse FDR Trust Object trusted sequence
%s: failed to parse certificate dictionary
%s: evaluateCertificateProperties failed
%s: Img4DecodeGetPropertyData(kFDRTag_prid) failed.
%s: kFDRTag_asid doesn't exist, but this is allowed
%s: decoded IM4C signature OID is empty
%s: missing public key algorithm parameter OID
%s: end of trusted key sequence found root_key=%d
%s: can't parse FDR Multi-response Metadata
AMFDRDecodeCheckProducerIDRevocation
AMFDRDecodeGetImg4Manifest
_AMFDRDecodeGetExpectedManifestHash
%s: Invalid data digest length: %ld
_AMFDRDecodeVerifySubCC
%s: malformed FDR Combined Format, expected tag %c%c%c%c found tag %c%c%c%c
%s: offline signing public key mismatch
%s: Re-evaluation returned code=0x%016llX
%s: FDR failed to get payload type from multi combined data
%s: decodeAlgId failed
%s: PKI: verify cert was issued and signed by issuer (success)
%s: PKI: verify cert %d was issued by %d (success)
%s: PKI: check payload hash with signature (success)
%s: missing IM4C leaf public key OID
%s: Record value must be OCTET_STRING
%s: can't parse FDR Trust Object trusted key: %d
%s: AMFDRDecodeIterateProducerIDNext(first) failed with error 0x%016llX
AMFDRDecodeEvaluateTrustWithSik
%s: malformed FDR2 Format (manifest2), invalid tag length
AMFDRDecodeMetaProperty
%s: Re-evaluation succeeded but decode options require version2
%s: ignoring raw error 0x%016llX
AMFDRDecodeVerifyCertIssuerWithOptions
AMFDRDecodeMultiSealingResponse
%s: failed to find corresponding data instance
%s: Skip verifying assembly identifier
%s: subCC is not hashed
decode error
%s: implementation must be non NULL and signatureOid must be non NULL
%s: Img4DecodeGetPropertyData(kFDRTag_inst) failed.
%s: verifying subCC, skip comparing digest of the entire data
%s: payload sequence malformed for multi combined data
%s: malformed attribute: %d
%s: Record value is NULL
%s: Record value length is 0
%s: malformed FDR Trust Object Revoked, expected tag %c%c%c%c found tag %c%c%c%c
%s: malformed cert property key: %c%c%c%c
%s: malformed offline blob
%s: can't parse top-level container
%s: unexpected property type != kImg4ObjectProperty
_AMFDRDecodeInstPropertyMatching
%s: kFDRTag_cptp property != fdrDecode->componentType
%s: cannot find subCC digest for %u
%s: malformed FDR Trust Object trusted key, invalid trusted key tag length
%s: can't parse FDR Trust Object Revoked sequence
%s: FDR Sealing Manifest failed to decode sequence
AMFDRDecodeImage4Certificate
%s: malformed FDR Multi-Response Payload Format
%s: malformed FDR2 Format, invalid fdr2Data.tag.length
%s: Skipping revocation check (trustobject unset)
%s: subCC digest mismatch
AMFDRDecodePublicKey
%s: failed to parse property list
%s: found multiple entries that match, uniqueID is required in this case
%s: publicKeyParam is NULL
%s: buffer is NULL
%s: multiResponseCallback failed with error 0x%llX
_AMFDRDecodeGetDataInfoCallback
%s: ClientID extension not found
%s: MetadataRecord must be SEQUENCE Container
%s: can't parse DERDecodeSeqNext
_AMFDRDecodeVerifySealingRequestCallback
%s: Staged sealing is not allowed
%s: malformed FDR Combined Format (trustObject), expected tag %c%c%c%c found tag %c%c%c%c
%s: FDR failed to get payload from multi combined data
%s: ignoring trust object mismatch error 0x%016llX
AMFDRDecodeManifestBody
%s: sysconfig version not supported: 0x%x
%s: %s: signature validation failed
%s: fdrDecode->dataImg4.payload_hashed is false
_AMFDRDecodeVerifyMultiCombinedDataInternal
%s: PKI: decoding trusted root %d failed with error 0x%016llX
_AMFDRDecodeMultiResposeRecords
%s: outRawData must be non NULL and outRawDataLength must be non 0
%s: failed to decode offline blob Format
%s: kFDRTag_inst propertyLength (%d) != fdrDecode->manifestUniqueID.length (%zu)
_Img4DecodeInitDummyPayloadForDataDigest
%s: im4c revocation check failed
%s: PKI: verify cert was issued by trusted key %d failed with error 0x%016llX
_AMFDRDecodeVerifyTrustObject
%s: kFDRTag_inst propertyValue (sik) != sikValue
%s: ignoring incomplete subcc error 0x%016llX
%s: failed to decode all sequences: %d
%s: chain_blob must be non NULL and chain_blob_length must be non 0
%s: _AMFDRDecodeIterateCertChainNext failed (first call)
%s: PKI: decoding trusted key %d failed with error 0x%016llX
%s: AMFDRDecodeIterateTrustObjectTrustedBegin failed
AMFDRDecodeEvaluateTrustOffline
%s: Record must be SEQUENCE Container
%s: AMSupportDigestSha256 failed
%s: malformed FDR Multi-Response Format
AMFDRDecodeCombined
%s: Img4DecodeGetObjectPropertyData failed
%s: failed to find object properties
%s: failed to begin decoding trusted key
%s: PKI: verify cert %d was issued by cert %d failed with error 0x%016llX
%s: cannot begin with an already initialized iterator
AMFDRDecodeVerifyMultiCombinedDataIntegrity
%s: unsupported signature length: %lu
%s: FDR Sealing Manifest failed to decode sealing manifest
%s: kFDRTag_inst propertyValue != fdrDecode->manifestUniqueID.data
%s: failed to find matching inst object propery, returning a mismatched one
AMFDRDecodeIterateMultiCombinedDataBeginWithRawData
%s: malformed Img4 Manifest (version parse fail)
%s: Img4DecodeEvaluateManifestProperties failed
%s: Skipping trust root check (trustobject unset)
%s: PKI: verify cert was issued by trusted root %d failed with error 0x%016llX
%s: AMFDRDecodeVerifySealingManifest 0x%016llX
AMFDRDecodeIterateTrustObjectRevokedBegin
AMFDRDecodeVerifySealingRequest
%s: can't parse content of MinimalManifestMetaData
%s: DERMemcmp failed.
%s: failed to find MANP (manifest payload) tag
%s: FDR Trust Object digest size not supported. digest is of size %zu
_AMFDRDecodeSequenceString
%s: malformed im4c tag length: %lu
%s: malformed cert property key length: %lu
%s: failed to decode DER
%s: trustObject is NULL
%s: Attribute must be set container. Found unexpected tag 0x%llu, skipping
%s: outImg4Blob must be non NULL and outImg4BlobLength must be non 0
%s: invalid digest length
%s: failed to get CSR signature from offline blob
%s: can't parse MinimalManifestMetaData
%s: failed to decode sysconfig metadata: %d
%s: _AMFDRDecodeVerifyTrustObject failed (%llu), continuing.
%s: malformed FDR Trust Object trusted, invalid trusted tag length
%s: malformed FDR2 Format, invalid tag length
%s: FDR Sealing Request failed to decode img4
%s: kFDRTag_inst propertyLength (sik) (%d) != sikLength (%zu)
_AMFDRDecodeFindDataFromMultiCombined
%s: failed to parse signed section sequence: %d
%s: failed to find property in the manifest
%s: Payload version is wrong size. got %zu expected %d
%s: _AMFDRDecodeIterateCertChainNext failed (%d)
%s: Failed to get payload sequence and set manifest from multi combined data
AMFDRDecodeIterateMultiCombinedDataNext
%s: item is bigger on the inside
%s: unsupported meta property type
%s: DERImg4DecodePropertyWithItem failed
%s: failed to find corresponding component type
%s: could not parse sealing manifest
%s: Unsupported tag found in manifest '%c%c%c%c'
%s: Invalid out pointers
%s: public key OID is not EC
%s: failed to find MANB (manifest body) tag
AMFDRDecodeManifestBodyInfoNext
%s: failed to parse payload content: %d
%s: Outer DER did not terminate properly.
_AMFDRDecodePropertiesFilterCallback
```
