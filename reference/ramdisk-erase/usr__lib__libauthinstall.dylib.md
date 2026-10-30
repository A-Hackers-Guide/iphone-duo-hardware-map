# `/usr/lib/libauthinstall.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 1,912,368 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 37 (Size: 5408)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, HasTLVDescriptors, AppExtensionSafe
```

## Linked libraries (19)

- `/usr/lib/libauthinstall.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork (compatibility version 1.0.0, current version 3896.200.61)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit (compatibility version 1.0.0, current version 275.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity (compatibility version 0.0.0, current version 0.0.0, weak)`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking (compatibility version 1.0.0, current version 72.0.0)`
- `/usr/lib/libMobileGestalt.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libamsupport.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libcompression.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/updaters/libAppleTconUARPUpdater.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/updaters/libSavageRestoreInfo_iOS.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/updaters/libT200Updater.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (69 classes, 5 protocols)

Classes: `AMAuthInstallOSSsoAuthenticator`, `Ace3RestoreInfoFirmwareCopierOS`, `Ace3SoCRestoreInfoFirmwareCopierOS`, `Ace3SoCRestoreInfoHelperOS`, `AppleTypeCRetimerFirmwareAggregateRequestCreatorOS`, `AppleTypeCRetimerFirmwareCopierOS`, `AppleTypeCRetimerFirmwareRequestCreatorOS`, `AppleTypeCRetimerRestoreInfoHelperOS`, `FTABFileOS`, `FTABSubfileOS`, `MRUHardwareInfo`, `MRULogHelper`, `MRUPersonalizationInfo`, `MRUPersonalizedFirmware`, `MantaFTABFile`, `MantaFTABSubfile`, `NSData`, `NSError`, `NSFileHandle`, `NSMutableData`, `UARPAssetTagOS`, `UARPAssetVersionOS`, `UARPMetaDataTLV16OS`, `UARPMetaDataTLV32OS`, `UARPMetaDataTLV64OS`, `UARPMetaDataTLV8OS`, `UARPMetaDataTLVDataOS`, `UARPMetaDataTLVOS`, `UARPMetaDataTLVStringOS`, `UARPSuperBinaryOS`, `UARPSuperBinaryPayloadOS`, `UARPTLVHostPersonalizationRequiredOS`, `UARPTLVPersonalizationBoardIDOS`, `UARPTLVPersonalizationChipEpochOS`, `UARPTLVPersonalizationChipIDOS`, `UARPTLVPersonalizationChipRevisionOS`, `UARPTLVPersonalizationECIDDataOS`, `UARPTLVPersonalizationECIDOS`, `UARPTLVPersonalizationEnableMixMatchOS`, `UARPTLVPersonalizationFTABPayloadOS`, `UARPTLVPersonalizationFTABSubfileDigestFilenameOS`, `UARPTLVPersonalizationFTABSubfileDigestOS`, `UARPTLVPersonalizationFTABSubfileEPROOS`, `UARPTLVPersonalizationFTABSubfileESECOS`, `UARPTLVPersonalizationFTABSubfileHashAlgorithmOS`, `UARPTLVPersonalizationFTABSubfileLongnameOS`, `UARPTLVPersonalizationFTABSubfileTagOS`, `UARPTLVPersonalizationFTABSubfileTrustedOS`, `UARPTLVPersonalizationLifeOS`, `UARPTLVPersonalizationLogicalUnitNumberOS`, `UARPTLVPersonalizationManifestEpochOS`, `UARPTLVPersonalizationManifestPrefixOS`, `UARPTLVPersonalizationManifestSuffixOS`, `UARPTLVPersonalizationNonceHashOS`, `UARPTLVPersonalizationNonceOS`, `UARPTLVPersonalizationPayloadTagOS`, `UARPTLVPersonalizationPrefixNeedsLogicalUnitNumberOS`, `UARPTLVPersonalizationProductionModeOS`, `UARPTLVPersonalizationProvisioningOS`, `UARPTLVPersonalizationRequiredOS`, `UARPTLVPersonalizationSecurityDomainOS`, `UARPTLVPersonalizationSecurityModeOS`, `UARPTLVPersonalizationSoCLiveNonceOS`, `UARPTLVPersonalizationSuffixNeedsLogicalUnitNumberOS`, `UARPTLVPersonalizationSuperBinaryAssetIDOS`, `UARPTLVPersonalizationSuperBinaryPayloadIndexOS`, `UARPTLVPersonalizationTicketNeedsLogicalUnitNumberOS`, `UARPTLVPersonalizedManifestOS`, `UARPTLVRequiredPersonalizationOptionOS`

Protocols: `ASAuthorizationControllerDelegate`, `NSCoding`, `NSCopying`, `NSObject`, `NSSecureCoding`

## Strings (6,129)

First 2,500 of 6,129.
```
_bootNonce
_layer2Context
appendLittleInt32:
initWithOptions:error:
logicalUnitNumber
objectAtIndexedSubscript:
totalLength
init
_subFileArray
T@\"NSDictionary\",R,V_tssRequest
T@\"MantaFTABSubfile\",R,V_manifest
T@\"NSString\",&,N,V_ssoHost
T@\"NSArray\",R
T@\"NSNumber\",C,V_demote
TQ,R
_rrko
_char2
minorVersion
setDigest:
setObject:forKeyedSubscript:
setQuery:
ticketName
T@\"NSString\",R
_dataLength
queryItemWithName:value:
setEnableMixMatch:
tlvValue:
numberWithBool:
_logContext
initWithFilePath:delegate:delegateQueue:
setDemote:
T@\"NSString\",R,V_longname
TI,V_chipID
removeAllObjects
writeBytes:length:
zone
getBytes:range:
T@\"UARPAssetVersionOS\",R,V_version
TQ,R,V_ecID
dataWithBytes:length:
generateHashForData:
objectAtIndex:
setChipRevision:
T@\"NSData\",R,V_payload
TQ,V_ecID
_logFunction
generateTatsuMeasurements:
superbinary:logString:
T@\"NSNumber\",C,V_trustedOverride
_provisioning
numberWithUnsignedInt:
createDirectoryAtPath:withIntermediateDirectories:attributes:error:
self
unsignedLongLongValue
TB,R,V_needsHostPersonalization
bytes
composeTSSRequest:asMeasurement:
suffixNeedsLogicalUnitNumber
boardID
TI,V_boardID
asDictionary
componentsSeparatedByString:
doesNotRecognizeSelector:
generateRequestDictionary
respondsToSelector:
setTicketNeedsLogicalUnitNumber:
seekToEndReturningOffset:error:
TC,V_productionMode
TQ,R,V_totalBytesRequested
hasPrefix:
setLife:
ticketPrefix
T@\"NSData\",R,V_ecID
TI,R,V_dataLength
_securityEpoch
ssoEnv
stringWithFormat:
TC,R,V_life
readDataToEndOfFileAndReturnError:
stringWithString:
supportsSecureCoding
TC,R,V_ticketNeedsLogicalUnitNumber
data
errorWithDomain:code:userInfo:
generateHashSHA384
intValue
metaData
numberWithUnsignedInteger:
T#,R
_firmwarePathSuffix
filePointer
isMemberOfClass:
setProductionMode:
performRequests
_firmwareInBundleDataDict
_stealthMode
absoluteString
initWithURL:delegate:delegateQueue:
setChipID:
setSsoRealm:
tlvLength
_digest
T@\"NSString\",?,R,C
_rkosData
_tagNumber
ecidData
personalizeSuperBinary:signingServer:ssoOnly:
setTLVs:
T@\"FTABSubfileOS\",R,V_manifest
HTTPMethod
TI,R,V_generation
_ecid
_magic
createDestinationBundleFirmwareDirectoryFor:error:
setManifest:
uarpSeekToEndReturningOffset:error:
T@\"NSString\",R,V_ticketPrefix
TI,R,V_valid
_trustedOverride
payloadsWithout4ccTag:
writeSubfileToURL:tag:
allHTTPHeaderFields
initWithBVERString:
setIsRequired:
setValue:forHTTPHeaderField:
valueForKeyPath:
T@\"NSData\",C,V_manifest
_componentName
_rkos
_trusted
addEntriesFromDictionary:
setSsoHost:
ssoRealm
TI,R,V_chipEpoch
_rrkoData
_url
payloadIndex
setSuffixNeedsLogicalUnitNumber:
unsignedIntValue
value
T@\"NSData\",R,V_digest
TC,R,V_suffixNeedsLogicalUnitNumber
epro
numberFromString:
numberWithUnsignedChar:
retain
T@?,C,N,V_completionHandler
_version
dictionaryWithDictionary:
handleFailureInFunction:file:lineNumber:description:
initWithChipID:chipRev:boardID:securityEpoch:productionStatus:securityMode:securityDomain:ecid:
url
T@\"NSString\",&,N,V_ssoRealm
TI,R,V_tlvLength
initWithData:metaData:tag:version:
nonce
objectName
setFlags:
T@\"NSData\",R,V_nonceHash
T@\"NSData\",C,V_ecidData
initWithContentsOfURL:
setManifestSuffix:
setPrefixNeedsLogicalUnitNumber:
_fileLength
initWithTag:data:
setAuthenticationController:
TC,V_securityMode
_dataPointer
defaultManager
hash
initWithAuthorizationRequests:
payloadData
personalizedData
tag
T@\"NSString\",&,N,V_ssoEnv
version
TC,R,V_provisioning
URLWithString:
lastPathComponent
metaDataTableEntry
tlvValue
TI,R,V_securityEpoch
_deviceInfoArray
code
initWithBytes:length:
nonceHash
_manifest
_ssoRealm
_tlvType
countByEnumeratingWithState:objects:count:
manifestSuffix
setAuthorizationOptions:
string
totalBytesRequested
_majorVersion
TB,N,V_useLegacyAuthURL
T@\"NSData\",R,V_bootNonce
currentHandler
T@\"MRUHardwareInfo\",R,V_hardwareInfo
TC,R,V_liveNonce
TI,R,V_chipRev
authenticationURL
isEqual:
isEqualToString:
HTTPBody
TC,R,V_enableMixMatch
char1
dataWithData:
setTssOption:
tlvWithLength:value:
_keyManifest
firstObject
initWithVersionString:
readFirmwareFileDataWithError:
writeToURL:atomically:
authorizationProviderWithIdentityProviderURL:
getNeedsHostPersonalization
tlvTypeName:
_ssoEnv
T@\"NSString\",R,V_tag
TI,R,V_chipID
_subfiles
initWithTag:dataPointer:dataLength:
processTLVsForPersonalization
setEsec:
setUserInterfaceEnabled:
isProxy
_esec
_suffixNeedsLogicalUnitNumber
setCompletionHandler:
tlvFromKey:value:
isValid
TI,R,V_securityMode
TQ,R,V_ecid
TS,R,V_trusted
authorizationController:didCompleteWithError:
fileExistsAtPath:
securityDomain
setEcID:
setStealthMode:
_fileData
encodeObject:forKey:
esec
_delegate
URL
_securityDomain
_measurements
_tssOption
_valid
enumerateKeysAndObjectsUsingBlock:
layer2Context
parseOptions:
T@\"NSString\",R,C
TQ,R,V_releaseVersion
_requestDictionary
_tlvValue
dataWithContentsOfURL:options:error:
setLiveNonce:
_metaData
conformsToProtocol:
flags
getMeasurements
isRequired
keyWithPrefix:
versionString
_chipID
_ticketPrefix
_useLegacyAuthURL
copyItemAtPath:toPath:error:
createRequest
setService:
T^v,V_layer2Context
_ticketSuffix
dataWithContentsOfURL:
personalizedMetaData
requestDictionary
_securityMode
array
setTicketPrefix:
_char1
_propertyNameSuffix
appendData:
setChipEpoch:
setLogicalUnitNumber:
writeBytes:length:handle:
T@\"NSData\",R,V_magic
_generation
autorelease
char2
majorVersion
tlvs
_componentNameSuffix
removeSubfileWithTag:
setPayloadIndex:
initWithString:
arrayWithObjects:count:
generateTatsuMeasurementsPerPayload:
initWithPayload:manifest:
_longname
_nonceHash
authorizationController:didCompleteWithCustomMethod:
digest
encodeWithCoder:
initWithCoder:
initWithType:length:value:
queryItemsWithParameters:
addSubfile:tag:
TQ,R,V_majorVersion
URLByAppendingPathComponent:
dictionary
requiredTSSOptions
setSsoEnv:
uarpCloseAndReturnError:
TC,R,V_prefixNeedsLogicalUnitNumber
_payloads
bootNonce
manifestEpoch
setAssetID:
setFilename:
tssRequestAsString
TS,R,V_esec
setNonce:
_demote
expandMetaData:
getTlvs
_filePointer
_totalLength
ecid
stringWithValidatedFormat:validFormatSpecifiers:error:
_fileHandleWriteDestination
credential
ssoHost
getPayloads
stringWithCapacity:
_enableMixMatch
_payloadIndex
addObjectsFromArray:
log:
objectForKeyedSubscript:
setBoardID:
stringByExpandingTildeInPath
verboseLog:
T@\"NSData\",R,V_metaData
TS,R,V_epro
_formatVersion
_logicalUnitNumber
noncePropertyName
unsignedShortValue
caseInsensitiveCompare:
filename
seekToOffset:error:
encodeBytes:length:forKey:
initWithChar1:char2:char3:char4:
_service
productionModePropertyName
preparePayload:
class
hashAlgorithm
liveNonce
chipIDPropertyName
rtKitKeyFromBuildIdentityDict:
subdataWithRange:
superclass
TB,V_provisioning
_asset
appendString:
authenticate
initWithBytes:length:encoding:
isGreaterThan:
payloadWith4ccTag:
dataPointer
demote
expandTLVs
queryTatsuSigningServer:ssoOnly:error:
T@\"NSDictionary\",R,V_requestDictionary
TS,R,V_assetID
appendByte:
canPerformAuthorization
initWithData:delegate:delegateQueue:
byteString
parseFileData
tlvFromPropertyListValue:
T@\"NSData\",R
TB,N,V_stealthMode
URLByDeletingLastPathComponent
addSubfileWithTagName:subfileData:
numberWithUnsignedLongLong:
writeToURL:
_manifestSuffix
tlvType
_objectName
_ssoHost
initWithData:
initWithOptions:logFunction:logContext:
isFileExistsError
setUseLegacyAuthURL:
_hashAlgorithm
_life
_tlvs
fileLength
generateHashSHA256
removeSubfile:tag:
ticketNeedsLogicalUnitNumber
unsignedCharValue
Tr*,R,V_dataPointer
processMeasurementsForTSSOptions:unitNumber:asMeasurement:
T@\"NSString\",R,V_filename
Tr^{?=IIQQ^{__CFString}^{__CFString}},N,V_service
_liveNonce
enumerateObjectsUsingBlock:
T@\"NSData\",R,V_nonce
chipRevision
generateHashSHA512
setLongname:
T@\"NSArray\",R,V_tlvs
T@\"NSDictionary\",R
TQ,R,V_totalLength
_char4
count
TB,R,V_securityMode
setSecurityDomain:
unsignedIntegerValue
allHeaderFields
_tlvLength
productionStatus
releaseVersion
dataWithContentsOfFile:
getTssRequest
initWithHardwareInfo:componentName:objectName:nonce:tagNumber:
name
numberWithUnsignedShort:
TI,R,V_tlvType
_needsHostPersonalization
firmwareKeyFromBuildIdentityDict:deviceInfo:
TI,R,V_isRequired
_authenticationController
appendLittleInt16:
TQ,R,V_minorVersion
_minorVersion
chipEpoch
debugDescription
generateTLV:tlvValue:
tssOption
setTag:
TQ,R,V_buildVersion
TI,R,V_productionMode
authorizationController:didCompleteWithAuthorization:
authorizationController:shouldRetryAfterError:
hardwareInfo
provisioning
writeToURL:error:
arrayWithArray:
Tc,R,V_char1
_chipRev
_flags
chipID
productionMode
TC,V_life
_assetID
_suffixNeedsUnitNumber
_verbose
dataLength
writeToDestination
payload
T@\"NSString\",R,V_manifestSuffix
T@\"ASAuthorizationController\",&,N,V_authenticationController
TI,R,V_boardID
fileValidForOffset:length:
uarpReadDataToEndOfFileAndReturnError:
TB,R,V_productionStatus
_chipRevision
_ftab
_prefixNeedsLogicalUnitNumber
decodeObjectForKey:
initWithHardwareInfo:componentName:objectName:nonce:
setNonceHash:
_productionMode
setHashAlgorithm:
generatePersonalizedSuperBinary
TQ,N,V_flags
_ticketNeedsUnitNumber
char3
fileURLWithPath:
initWithData:encoding:
_productionStatus
_tssRequest
_uinitNumber
copyWithZone:
ftabWriteData:error:
isKindOfClass:
performSelector:withObject:withObject:
setDelegate:
T@\"NSArray\",R,V_measurements
T@\"NSData\",R,V_manifest
_boardID
setProvisioning:
subfiles
_manifestEpoch
_nonce
subfileWithTag:
_ecID
_ecidData
_tatsuMeasurements
_totalBytesRequested
fileHandleForWritingToURL:error:
completionHandler
dumpString
queryItems
removeItemAtURL:error:
tssRequest
.cxx_destruct
T@\"NSData\",C,V_nonce
TI,R,V_logicalUnitNumber
readDataUpToLength:error:
securityDomainPropertyName
setLayer2Context:
_chipEpoch
_hardwareInfo
_prefixNeedsUnitNumber
_ticketNeedsLogicalUnitNumber
initFile
setTrustedOverride:
T@\"UARPAssetTagOS\",R,V_tag
release
TC,V_manifestEpoch
_completionHandler
_payloadData
ecidPropertyName
magic
securityEpoch
ecID
logInternal:arguments:
path
percentEncodedQuery
performSelector:withObject:
tatsuMeasurements:
TI,R,V_tag
mutableCopy
Tc,R,V_char2
compare:
configureFileHandleWriteDestinationForURL:
decodeObjectOfClass:forKey:
dictionaryWithObjects:forKeys:count:
longLongValue
numberWithUnsignedLong:
chipRev
T@\"NSURL\",R,V_url
_delegateQueue
_tag
initWithFormat:arguments:
longTagName:
prefixNeedsLogicalUnitNumber
boolValue
measurements
addSubfileWithTagName:contentsOfURL:
enableMixMatch
initWithMajorVersion:minorVersion:releaseVersion:buildVersion:
removeObject:
T@\"NSArray\",R,V_payloads
_buildVersion
boardIDPropertyName
copy
expandSuperBinary
generateTatsuMeasurements:relativeURL:
integerValue
setBootNonce:
T@\"NSData\",R,V_payloadData
_char3
life
setObject:forKey:
setQueryItems:
stringWithUTF8String:
TC,R,V_isRequired
TI,R,V_chipRevision
_filename
_payload
uarpSeekToOffset:error:
_apParameters
longname
needsHostPersonalization
setEcidData:
TQ,R,V_fileLength
addObject:
appendBytes:length:
bverString
domain
removeItemAtPath:error:
tlvFromType:length:value:
_data
_isRequired
generatePersonalizedSuperBinaryInternal:
performSelector:
setSecurityMode:
_epro
stringByAppendingString:
tssKeyName:unitNumber:
uarpReadDataUpToLength:error:
uarpWriteData:error:
useLegacyAuthURL
TS,R,V_hashAlgorithm
authenticationController
getManifest
_releaseVersion
metaDataTable
addSubfiles:
appendFormat:
containsValueForKey:
trustedOverride
TC,V_securityDomain
Tr*,R,V_filePointer
UTF8String
length
setTrusted:
writeData:error:
TI,R,V_securityDomain
_destBundlePathURL
buildVersion
decodeBytesForKey:returnedLength:
generateTLV
_cphyData
_firmwareOverrideData
closeAndReturnError:
createFileAtPath:contents:attributes:
dataWithContentsOfFile:options:error:
composeTSSRequest:
generateHashForSubfile:
manifest
setEpro:
TB,R
description
getDataBlock:offset:
securityMode
valid
TI,R,V_payloadIndex
TI,R,V_tssOption
_trimmedTlvs
char4
configureDataWriteDestination
copyItemAtURL:toURL:error:
generation
setManifestEpoch:
stealthMode
Tc,R,V_char4
_firmwareBundleURL
payloads
retainCount
writeToData
TC,R,V_manifestEpoch
_dataWriteDestination
generatePersonalizedSuperBinaryWithoutRRKO
securityModePropertyName
unsignedLongValue
createFileHandleForWritingToURL:
decodeCharForKey:key:
fileURLWithPath:isDirectory:relativeToURL:
assetID
service
Tc,R,V_char3
authenticatedResponse
copyFirmwareToDestinationBundleWithError:
trusted
@24@0:8I16I20
c
v16@0:8
v24@0:8@\"NSCoder\"16
B24@0:8:16
v20@0:8S16
@20@0:8C16
@\"MantaFTABSubfile\"
@24@0:8o^@16
@56@0:8@16@24@32@40@48
v20@0:8B16
@32@0:8@16@24
@20@0:8S16
^{uarpPlatformAsset={UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}SS{UARP4ccTag=CCCC}{UARPVersion=IIII}ICC{uarpPlatformAssetCallbacks=^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?}i{uarpDataRequestObj=III*I*IC{UARPCompressedHe
@32@0:8I16I20^v24
B16@0:8
@28@0:8Q16B24
v36@0:8@16Q24B32
@40@0:8@16@24@32
B
@\"NSMutableDictionary\"
B32@0:8@16@24
Vv16@0:8
B24@0:8^{UARPPayloadHeader2=I{UARP4ccTag=CCCC}{UARPVersion=IIII}IIII}16
@36@0:8@16r^v24I32
Q16@0:8
@\"UARPAssetTagOS\"
v24@0:8Q16
@24@0:8^{_NSZone=}16
v32@0:8@\"ASAuthorizationController\"16@\"ASAuthorization\"24
I16@0:8
B32@0:8@16^@24
@32@0:8@16Q24
@24@0:8@16
@40@0:8@16^?24^v32
B24@0:8^@16
v32@0:8@16*24
@24@0:8I16S20
B24@0:8^{UARPSuperBinaryHeader=III{UARPVersion=IIII}IIII}16
B32@0:8o^Q16o^@24
v32@0:8@\"ASAuthorizationController\"16@\"NSString\"24
@\"NSURL\"
I
q24@0:8@16
@\"NSObject<OS_dispatch_queue>\"
v24@0:8r^{?=IIQQ^{__CFString}^{__CFString}}16
v20@0:8C16
C16@0:8
S
r^{?=IIQQ^{__CFString}^{__CFString}}
Q
@32@0:8Q16^v24
@\"NSArray\"
@48@0:8Q16Q24Q32Q40
C
@24@0:8I16C20
@24@0:8:16
@\"NSMutableString\"
@40@0:8:16@24@32
B24@0:8#16
v32@0:8@16@24
@\"NSMutableArray\"
c16@0:8
B32@0:8r^v16Q24
r*16@0:8
@\"UARPAssetVersionOS\"
B24@0:8@16
v24@0:8@?16
^v
B36@0:8@16B24^@28
@36@0:8Q16@24B32
@52@0:8I16I20I24I28B32B36I40Q44
^{_NSZone=}16@0:8
@\"NSDictionary\"
B32@0:8@16o^@24
@\"MRUHardwareInfo\"
@\"NSMutableData\"
B24@0:8o^@16
@?
@24@0:8@\"NSCoder\"16
@\"FTABFileOS\"
@\"FTABSubfileOS\"
@48@0:8@16@24@32@40
@\"NSNumber\"
B32@0:8Q16@24
B32@0:8Q16o^@24
@24@0:8^@16
B40@0:8r^v16Q24@32
@\"NSFileHandle\"
v24@0:8@16
@\"NSData\"
B24@0:8I16I20
@24@0:8Q16
@28@0:8I16Q20
#16@0:8
@16@0:8
B24@0:8@\"Protocol\"16
S16@0:8
r*32@0:8@16@24
@\"NSString\"16@0:8
v20@0:8I16
@32@0:8c16c20c24c28
r*
@\"<UARPSuperBinaryDelegate>\"
v32@0:8@\"ASAuthorizationController\"16@\"NSError\"24
@?16@0:8
@\"NSString\"
^v16@0:8
v24@0:8^v16
@\"ASAuthorizationController\"
@32@0:8Q16Q24
r^{?=IIQQ^{__CFString}^{__CFString}}16@0:8
^?
@32@0:8Q16o^@24
@32@0:8@16^@24
@32@0:8:16@24
@28@0:8I16@20
@20@0:8I16
USB_ETHER_MAC
AMAuthInstallCryptoCreateSubjectPublicKeyInfoForKey failed
No eUICC ChipID specified. Not personalizing VinylFirmware at this time.
failed to create receipt directory: %@
eUICC,InfoPlistDataGold
%s::%s: AMSupportDigestSha256 failed:\n
%s: item is NULL
AMAuthInstallProvisioningPopulateRequestDict failed status=%d
\n------ Internal buffer is too small, truncating bytes! ------\n
%s::%s: Unable to copy the firmware:\n
Firmware/all_flash
infoArray: %@\n
trin
outputDict is NULL
Cryptex1,Ticket
MantaMRI
ciof
ginc
%@
%s::%s: failed to remove file (%u)\n
%s::%s: wrong chip rev size\n
Failed to create hashTableContents
%s::%s: failed to copy ftab header\n
SerialString
failed to add payloadCompression to DER file
RecoveryOSOS
AMAuthInstallApImg4EncodeRestoreDict legacy failed
AMAuthInstallBasebandCopyCustomFirmware
mba.mbn
%s::%s: failed to get firmware object\n
AOP2
dstFtabUrl is NULL
Found cached (dictionary) ticket at %@
failed to encode DER buffer
Firmware Object: 
%s::%s: desired type %s, received type %s\n
UOS1_ERROR
ibot
RelativeDestPath
fusingprogram
can't parse top-level restoreinfo sequence
environmentIdentifier
%s::%s: Applying FDR trust object hash override\n
-[Ace3RestoreInfoFirmwareCopierOS firmwareKeyFromBuildIdentityDict:deviceInfo:]
iBEC
SystemVolume
Wireless1,WiFiRxManuf
Failed to copy %@ to %@: %@
%@,ProductionMode%@
_AMAuthInstallApCopyDeviceEntryFromProvidedDeviceMap
%s: securityMode is NULL
%s CFDataCreate failed
AMAuthInstallSupportWriteDataToFileURL failed.
%s::%s: enable gid3En for rtkitos\n
User-Agent
failed to add certId-VAD sequence
firmwareInfoDict: 
%s::%s: failed to add certId\n
%s: AMAuthInstallBundleCreatePreManifest failed because overrides found but dstBundleURL is NULL
*
SBL1-Blob
No partial digest
%s %s\n%04x  
rbmt
Cryptex1,GenericIntegrityCatalog
otherParameters
Firmware/device_map.plist
IMEI2:%@
CFDataGetLength(signatureData) %lld != signatureLength %d
%s::%s: Manifest is not available\n
ypilkyibsrqvlyazp6iuq6tu4i2ume
%s::%s: failed to create mutable data in unoptimized path\n
\tecid: %llu\n
Cannot parse UpdateTable.bsn.
%s: responseTags is NULL or of invalid type
invalid tatsu data: (%p), size %d
----End request
%s::%s: manifest data has no bytes\n
%s::%s: Payload is out of valid range\n
\tsecurityMode: %u\n
Fail to allocate imageProps
options is nullptr
calibration key status not found
requesting fusing program from %@
value == NULL
%s: request failed copy
Fail to parse Apdu]
%s::%s: fwMacData is wrong type\n
ManifestPrefix
Unable to locate security mode for tag %u
Failed to find match in SDK-specific devicemap (via PLATFORM_DIR), falling back to system devicemap.
@
Cryptex1,LiveNonce
UPC-DownloadDigest
~DirectDataRef
%s::%s: failed to obtain data ref\n
\ttagName: %s\n
failed to add manifest version
TDSFW.elf
%s::%s: Fw data dictionary not present in the input\n
CKeyStatus
EUICCFirmwareLoaderVersion
unavailable
releaseVersion
fwData: 
RTP
Invalid hash length
%s::%s: null error parameter\n
AVISP1,Display
AMAuthInstallHttpCreateBaaCertificateData
AMAuthInstallProvisioningSendAck
%s::%s: failed to allocate space for file object\n
Failed to parse FTAB in super binary
both imei and meid are NULL, provisioning failed.
Error empty response create data
Cellular2,Ticket
}: 
Ap,EphemeralDataMode
AVISP1,kmpi
overriding entry: %@
SocksProxySettings
UARPSoCUpdaterExecCommand
ebl.bin
ApCurrentProductionMode
AMAuthInstallMonetCreateMEIDFromString
populateCFError
VinylFirmwareCreate
%s: buildIdentity is NULL
Rap,RestoreRTKitOS
snum=0x%@, 
failed to copy url for %@
%s: did not find %@ in manifest
%s: updaterSharedInfo is unexpected type
%s::%s: Failed to get DebugArgs buffer\n
Personalization Chip Epoch
update/main/profile.bin
%s::%s: failed to get goldNonce\n
Ap,NextStageIM4MHash
RawDataDigest
ap.ticket.8010.insec.cert
Detected empty build identity dictionary
/update/main/profile.bin
failed to to check amai->bbParameters for differences
AMAuthInstallProvisioningCopyResponse
T_MAC:%@
failed to add payload type to DER file
flashpsi-stitch
AMAuthInstallSupportFileURLExists failed.
%s: buildTags is NULL
Fail to DERDecodeSeqNext firmwareArray.
createRequest: wrong digest type
populateDictFromIdentity
Wireless1,Wifi5GLPhy
AMAuthInstallBasebandCopyFirmware
AMAuthInstallBundleSetPropertiesWithBoardConfig
%s::%s: could not create output data\n
%s::%s: failed to determine file size for path '%s' (%s)\n
%s::%s: specified tag name is invalid! Tag name: %s\n
IMPORT_REQUIRED
seos
Cryptex1,RosettaVolume
bbParameters is now non-NULL
acknowledging fusing program from %@
junk following sbl header
%s: amai->updaters is NULL
%s::%s: Failed to get value for: %s, exception: %s\n
Could not find RTKitOS info dictionary
failed to convert chipID
Ap,RestoreDCP2
VinylUpdaterGetTags
ApNonceSlotID
failed to measure \"%@\": %@;
RestoreBehavior
%s: failed to get shared updater info
%s::%s: no chip rev\n
,%d
Binaries: 
~VinylRestoreHost
RestorePSI-DownloadDigest
AMAuthInstallUpdaterLoadFromReceipt
RoseUpdaterGetSharedInfo
num != nullptr
failed to sequence tag
PAICHUSUO:%@
%s: exclaveNonce is NULL
Ap,GFX1Firmware
AMAuthInstallRembrandtMeasureBootPSI
DSP3-DownloadDigest
rtrx
ap.ticket.8960.insec.cert
AMAuthInstallRembrandtMeasureBootImage
FTAB %@:\n
null description
amai/LocalPolicy.restore.img4
Message
manifestData is NULL
%s::%s: failed to get src bundle URL\n
%s::%s: tag '%s' not found in tss-request map, skipping validation\n
AVISP1,ISP
AMAuthInstallBasebandApplyTssOverrides
WDT-DownloadDigest
cncn
entry not found for %@
PartialDigest = %@
PSI Image does not contain recognizable PSI header
addNewFileToFTABOnData
BbGoldCertId
mac : 
LeapHaptics
DPRO
failed to merge build identities
MBN segment components > size of ELF segment
fwData : 
%@ not found in buildIdentity
%s: invalid string
Cellular2,LLB
%s::%s: reducing requested length %zu -> %zu\n
%s::%s: failed to allocate source bundle firmware path dictionary (type: %hhu)\n
%s::%s: failed to get create request Dictionary\n
AMAuthInstallApCopyParameters
local
%s::%s: boot nonce has wrong size\n
Cannot init sequence for DeliveryObject.binaries
AVISP1,LeapBinsDigestsArray
pmcf
RecoveryOSAp,BaseSystemTrustCache
Savage
%s::%s: cannot save data using optimized flow\n
unrecognized chipid: 0x%08X
AMAuthInstallBasebandSupportsLocalSigning
AMAuthInstallBundleCopyReceiptCreateIfNecessary
%
tss_strip_img3_signature
\tSubfiles:\n
osrd
avdf
c411
outputDict: %@
Digest = %@
RFFW.elf
file lacks a hash section
RecoveryRequestEntries
device-map-XXXX
_VinylStitchInternal
tmpStringBuffer allocation failure
MBA-HashTableDigest
CDMA2KFW-HashTableDigest
%s::%s: null device info\n
%s::%s: failed stiching img4 and vad\n
_CalculateSizeOfJMETMetadataSegment
Custpack-HashTableDigest
%@,%@
Ap,ANE3
BbFactoryActivationManifestKeyHash
oauthGrantType
*outResponseDict is NULL
Cryptex1,SubType
tss_stitch_img3
%s::%s: failed to get measurements\n
%s: randomNonce is NULL
Version = %@
PersonID
%s: updater->responseTags is NULL, exiting early
copyFirmware: failed to create src rooted FW URL
%s::%s: failed to get dict entry for sbd1 digest\n
Unsupported firmware version: 
UpdateTable: 
Cryptex1,MobileAssetBrainTrustCache
x86,OSLongVersion
_CopyFileTagsFromRequestedTags
%@ OR %@ key not found, but that's okay. Moving along...
personalizedURL: 
build identity value: 
%s::%s: missing required file %s\n
VinylUpdaterCreateRequest: failed to create request dict
AMAuthInstallApImg4SetParameters
Ap,ApplePMCFirmware
dutf
mistyped provisioningKeyStatusRef
RelativeSrcPath
AMAuthInstallBasebandGetKeyHash failed
AudioCodecFirmware
com.apple.EmbeddedSoftwareRestore.Baseband.SBLVersion
amai/debug
BuildTrain
ECDH Server based provisioning enabled. Creating empty puk.pem file for BBUpdater
* unacknowledged fusing program *
RPCU.elf
Bringup baseband found, doing single stage provisioning
tss_submit_job_with_retry
filename 
_AMAuthInstallSsoCopyTicketUsingSUSSO
Error reading file
Timer,ProductionMode,%u
updateMeasurementDict
setFwInfo
user canceled AppleConnect login.
Timer,AppleTypeCPhyFirmware,1
Failed to create jmetMetadataSegmentData
x-intnt-usbserialstr
tmuf
mistyped iccid
%s: request cannot be empty with server signing
_CanaryGetTags
eUICC,MainFwMac
fwMac : 
ApRequiresImage4
SBL1-HashTableHeaderDefault
Cannot parse per ApduItemSpec
%s: requestEntry is NULL
fusing attempt failed; will consume program
failed to measure: LTE.elf
The server returned an internal error
failed to copy data from %@
gf1f
IsFTAB
AMAuthInstallHttpMessageSendSyncNew returned %d
copyFirmware: could not add 'rrko' object to final ftab
rfta
amai->bbParameters is NULL
%s: Failed to stitch ticket to FTAB file.
bb.rembrandt.gold.leaf.private
%s: failed to allocate keys or values
Test updater requested fake/empty ticket(s)
/usr/lib/libauthinstall.dylib
_FlsParserCopyDebugDescription
RestoreInternal
/usr/local/standalone/firmware/device_map.plist
keyHashData is NULL
@VersionInfo
%s: baseURL is NULL
%s: %s\n %@\n
updateFileInFTABOnData
AMAuthInstallApImg4ValidImage
%2C
%s: _AMAuthInstallSsoCopyTicketWithCredentials is NULL
Cryptex1,ExclaveNonce
%s::%s: =========== FTAB Header ===========\n
Failed to compose destFileURL
Failed to parse updateProperties as per UpdatePropertiesItemSpec.
rcio
Ap,Scorpius
AVISP1,PERTOS
AMAuthInstallBasebandSetParametersWithUpdaterOutput
x-intnt-keyalg-certformat
VinylMainFirmwareCreate
Failed to open file in zip: %s
Ap,AppleVideoEncoder2
Updater %@ forced for local signing by host tools.
euim
%s::%s: read less bytes than required (read: %zu, required: %zu)\n
RoseRestoreInfo
FTAB data is smaller than last payload
invalid snum: %@
GPuK is not properly aligned for partial digest
BatteryCharging
AVISP1,DisplaySec
Cannot parse UpdateTable.
local signing is disabled. vendorID=%d certID=%d
Personalize
failed to find published variants in bundle: %@
AMAuthInstallApImg4AddBooleanProperty
Ap,ANE2
Wireless1,WiFiTxManuf
Ap,TrustedExecutionMonitor
ETHER_MAC2:%@
NeRDEpoch
        <%@>\r
%s::%s: failed to find and/or copy data\n
File error
rdsk
gfxf
thrd
/update/gold/ticket.der
Personalize OS = %s
Cellular1,Nonce
%s::%s: Invalid firmware file\n
trxm
AuthInstallSSOHost
failed to extract bbfw item \"%@\": fileData is NULL
%s::%s: esec data to boolean conversion failure\n
firmwareDict: 
AMAuthInstallSetFusingRootCA
bbcfg.bin
failed to measure: RFFW.elf
debug object written: %@
keys is NULL
Cellular1,BbProvisioningManifestKeyHash
copyFirmware: rtkitos bundle data unavailable
Failed to create hardwareInfo, options: %@
rxcl
0x%08lx
MBN qti_signature_size overflows file
2GFW-DownloadDigest
Error ReadStreamOpen
Cannot allocate memory for outputDict
failed to install link for \"%@\" in personalized bundle
AMAuthInstallHttpMessageSendSyncNew() failed: %d
Options dictionary contains proxy information. Will attempt to use a proxy.
%s: buildIdentityTags is NULL
kern.bootsessionuuid
SOCKSProxy
Ap,AudioBootChime
AMAuthInstallUpdater
Added bbfw file : %@
Done adding additional fields to HTTP header
could not get request tag from path %@
iOS
IsFUDFirmware
Could not find build identity dictionary
parsing
Wireless1,ScanBTLPEM
Baobab,Cabal
%@%@
%@/%@
no device info
SEAC
Internal error
Error writing bbfw zip: %@
chipID: 0x%x is not supported for local provisioning
@HostPlatformInfo
%s: failed to create local manifest
%s::%s: SHA256 failed\n
%s::%s: failed to create capabilities\n
supportsRoseSEPairing
_AMAuthInstallCryptex1RequestSetNonce
The signing server returned an internal error
AudioAP1,ACIBT
ap.ticket.ca.cert
DeviceClass
%@-Original
ETH_MAC
Cryptex1,FakeRoot
BaseSystemVolume
provisioning key status=%d
partition.mbn
RecoveryOSRamDisk
ENANDPRG-Blob
no toc found in this file
getTags: failed to allocate output dictionary
getTags: failed to create response tag list
%@: fileSize=0x%x, srcOffset=0x%x, codeSize=0x%x
AMAuthInstallProvisioningServerSendSyncRequest failed
*outInfo is NULL
FlashPSI-PartialDigest
[in] %s 0x%s
vinylgetFwData certPlusLdrVer just certIdentifier: 
PERTOS
failed to stitch ticket data to file
BBCFG-DownloadDigest
Error getaddrinfo
%s::%s: Failed to write some or all of data\n
failed tss request:<<<<<<<<<<\n%@
%s: Creating user notification
%s::%s: tag %s missing from firmware, skipping\n
TSS Request Options for payload %@
Missing dict along the path
digestRef: 
Diags
failed to convert certid
failed to create ap ticket
AlternateUpdateBrainService
AMAuthInstallPlatformRemoveDirectory
InstanceB
copyDirectData
%s::%s: bad parameter!\n
AMAuthInstallBasebandCreateServerRequestDictionary
%@.%@.%@
outUnescapedValue == NULL
prettyLog
%s::%s: data exceeds local buffer size\n
%s::%s: failed to create full description for type ID %lu\n
failed to add \"%@\"; ignoring it
TPCU.elf
SoftwareUpdateSSO dylib found
chipid=0x%x, certid=0x%x
failed to measure: dbl.mbn
%s::%s: incorrect device info type\n
cabl
Removing %@ from the build identity
Failed to create directory at '%@': %@
failed to process image rules
%s: tagType is NULL
%s::%s: Failed to measure firmware\n
minorVersion
failed to prepend entry name to path
SBL1-HashTableDigest-Blob
Stashing %@ ticket(s) in bundle (LoopInstance=%@)
bb.rembrandt.ticket.root.public
failed to add top-level sequence
CertificateEpoch
SE,OS
unrecognized state; will consume program (commandAccepted=%s, attemptedToFuse=%s, fuseAttemptSucceeded=%s)
%s: SSO user interaction is disabled
@ApImg4Ticket
Cellular2,PMUFW
%s::%s: Unrecognized CF object!\n
AppleConnect not found
/update/main/ticket.der
SinopeUpdaterCreateRequest
inputData is not of type CFDataRef
failed to measure: osbl.mbn
Cryptex1,ExclaveLiveNonceDomain
PSI-Version
CDMA2KFW-DownloadDigest
setBootNonce
%@,ChipID%@
Img4DecodeInit img4 decode failed.
failed to convert VersionStr(%@) to int
%s: failed to write %@ manifest
_AMAuthInstallVinylCreateIm4p
SHA1Result failed=%d
Wireless1,ACIWiFiTxManuf
RoseUpdaterGetSharedInfo: Failed to allocate shared info dict
Cannot find key kSEOptionDeviceInfo in options
%s: invalid image 3 object
%s: 
v24@?0@\"NSDictionary\"8@\"NSError\"16
FlsParserCopyEbl
Cellular2,ChipID
%s::%s: failed to map file: (%s)\n
getCFError
AMAuthInstallApImg4CopyPayload
AMAuthInstallApImg4CreateServerRequestDictionary
trcr
AMAuthInstallBundleCopyBuildIdentityForVariant
Firmware File Dictionary: 
RoseUpdaterGetTags
Failed to parse as per DeliveryObjectItemSpec
%s: dict is NULL
ApSupportsImg4
UNDEF
Wireless1,Ticket
Ap,SystemVolumeCanonicalMetadata
This chipid/certid does not support local or server personalization.
AMAuthInstallBasebandGetKeyHash
PairedWithSecondaryTarget
wrong updateTableEnry with wrong hash size
Hamm
gpuk_offset %d >= sizeToMeasure %lld
%s: server request failed
%s::%s: failed to allocate output dictionary\n
%s::%s: failed to convert tag '%s' from device info type (%s) to tss-request map type (%s)\n
AMAuthInstallSetFusingServerURL
failed to convert fusing status
%5E
ApProductionMode
com.apple.EmbeddedSoftwareRestore.eUICC.bootloaderVersionsSupported
no-timeout
DAWRequest
 
[%@]: Using firmwareOverride\n
msrf
reservationLength=0x%x, codeBytesHashed=0x%x (%s) byte_multiple=%d
EuiccMainTicket
BundleDataDict
%s::%s: Regular bbticket flow\n
%s::%s: Failed to save packaged firmware file\n
\thardwareInfo: %s\n
trst
PersonalizationInfo
%s::%s: failed to create CFError object\n
%s::%s: payload is out of valid range\n
eUICC,ProfileDataMain
filename : 
scef
manifestProvisioningKeyHash not found in ManifestInfo
_AMAuthInstallBundleCreateServerRequestDictionary
.
}
Error WriteStreamOpen
failed to create request dict
drko
enable-transport-logs
ap.ticket.dev.key
fuseAttemptSucceeded
_FindSbl1HeaderInFileData
AMAuthInstallUpdaterSaveToReceipt
CryptexDMG
AMAuthInstallBasebandSetFusings
_AMAuthInstallBundleRemovePersonalizedBbfw
qupv3fw.elf
ICCID
AMAuthInstallEnableAlternateUpdateRequest
AMAuthInstallApCreateImagePropertiesWithDeviceMapZipped
IsX86
CKeyHash
postString=%@
RecoveryOSStaticTrustCache
Failed to create personalizedFileName
AMAuthInstallProvisioningRequestManifest
SSO failed to authenticate.
SHA1ResultPartial failed=%d
%s: image4DeviceGetKeyAlgorithmWithOptions() failed: %d
rsa2048
Failed to create directory at '%@' (%@)
Wireless1,PhyBluetooth5GTrim
Fail to parse MQR
Ap,AppleVideoEncoder1
%@ key not found.
overriding entries: %@
tempData is NULL
DERDecoderGetEncodingWithTag
failed to stitch ticket to %@
performing separate baseband firmware personalization of %@
RequestTags
FIRM
applicationIdentifier
BuildManifesto.plist
%s: could not create measurements: %d
AMAuthInstallApImg4CopyPayloadType
gap 
copyFirmwareUpdater: bad device info parameters
AMAuthInstallBasebandLocalProvisionDevice
%s: failed to create path info key.
Cellular1,BbFactoryDebugEnable
%s::%s: Digest of manifest failed\n
syab
AMAuthInstallApImg4LocalAddImageProperties
Personalization Provisioning
demoteProd
ApSikaFuse
@x86,Ticket
%s::%s: Failed conversion: %s\n
dbl.mbn
AMAuthInstallApAddTag
%s: amai->bbParameters is NULL
%s::%s: path has wrong type %lu\n
AMAuthInstallBasebandN92StitchFirmware
failed to write updater manifests: %@
setting %@ failed
Baseband not reporting manifest status, not attempting to provision yet.
%s::%s: Prov flow\n
removeManifestPadding
Personalization ECID Data
SecurityEpoch
username
failed to install link in personalized bundle: %@
Wireless1,CoexRealTimeArbiter
%s: failed to create mutable dict measurementDict
audl
_localsigning_named
Trusted
%s::%s: failed to initialize object\n
cssy
%s failed to encode tag
EUICCChipID
%s::%s: bundle cert firmware doesn't have 'rrko'\n
Base64Encode failed
Unable to locate device info
trbb
AMAuthInstallBasebandServerRequestAddRequiredTags
created merged response dictionary
_AMAuthInstallBundleShouldPersonalizeOS
Failed to read firmware file at '%@' (%@)
%s::%s: failed to initialize logging\n
Failed to create personalizationInfo with options %@: %@
%s::%s: bad device info parameters\n
no cached text for tss error code %d
AMAuthInstallUpdaterCreateResponse
%s::%s: Unexpected value: %u for Key: %s\n
%s::%s: srcPath memory alloc failed\n
Inserting %@ to Manifest to personalize later
setting B64_BB_CHIPID failed
OK
AMAuthInstallUpdaterBehaviorOverrides
Cellular1,RTKitOS
Ap,RestoreMSRFirmware
dstEncoder cannot be NULL
%s: _AMAuthInstallSsoSUSSOCopyToken returned without ssodata
SBL2-DownloadDigest
%s: %@ in deviceInfo is NULL
AMAuthInstallBasebandGetRFSelfTestTicket
ACDB-DownloadDigest
snum is not CFData
missing amai->bbParameters
baseband apparently doesn't support personalization
createRequest: could not find FW in build ID
%s::%s: failed to get deviceInfoDict\n
LCST
_AMAuthInstallCopyPsiMeasurementAndVersion
restorepsi.bin
failed to write the AP ticket
%s::%s: rooted override data unavailable\n
%s::%s: Failed to create empty trust object hash\n
%s::%s: file name not specified\n
EXPORT_FINISHED
ginf
%29
junk following sbl1 header
%5B
received tss response (server version: %@)
Cryptex1,NonceDomain
AMAuthInstallUpdater.c
Wireless1,ACIWIFI
Failed to build vinyl info.plist dictionary
aciw
_FindSblHeaderInFileData
qdsp6sw_dtbs.elf
PSI-Blob
_DERDecodeLength
Pragma
Wireless1,ProductionMode
rosi
unrelated stage; will hold fusing program
MBN oem_certificate_chain_size overflows file
Server returned STATUS=%@
stealthMode
%s::%s: Could not obtain deviceInfo dictionary. Sharing all digest information.\n
failed to add payloadKeybag to DER file
Wireless1,ChipRev
failed: %@
Bad parameter
Overrides
failed to save username in keychain
rtpf
Ap,SecureM3Firmware
failed to copy urls for firmware images
provisioning server url is NULL
ACMobileShimGetTicket symbol not found
RamPSI-Version
updater is NULL
EUICC,Ticket:
Using global signing
duhf
rampsi-personalized
fullrequest copy allocation failure
_AMAuthInstallUpdateHTTPHeaderWithEntry
%s::%s: invalid type for buildidentity\n
decoder != NULL
%s::%s: could not get 'rrko' object from ftab\n
acdb.mbn
AMAuthInstallUpdaterCreateLocalResponse
createRequest: Failed to build parameters out of device identity
RamPSI-Original
3GFW.elf
char2
%s::%s: sbd1 digest is of an unexpected type\n
Wrong length for updateTableEnry
siof
auac
CEPO
failed to convert value to c-string
getBootNonce
Wireless1,WiFiTx
DMC,VCOMFirmware1
Ap,MinimumOSSecurityVersion
Wireless1,PhyBlueTooth5GManuf
sptm
AMAuthInstallBasebandCopyFirmware failed
DSP3-HashTableDigest
failed to write img4 string to dst file: %s
%s::%s: No manifest present\n
ACFUDebugArgs
%d.%d
ronh
can't parse top-level container
Cryptex1,SystemTrustCache
Attempt to force provision baseband failed
AMAuthInstallBasebandReadVersionFromBbfw
overriding build identity entries: %@
LegacyRATFW-DownloadDigest
true
Error digest->data
error from server=%d (%s)
failed to add DSEC property for '%@'
%s::%s: failed obtain new file data\n
manifestCalibrationKeyHash not found in ManifestInfo
inserting provisioning info (if any) into existing bbfw for \"%@\"
BuildIdentityTags
%s::%s: failed to aquire ftab file header\n
unsupported digest type %@
DGST
Cellular1,BoardID
%s::%s: file data was invalid\n
Failed to create destination bundle firmware directory at '%@' (%@)
RoseUpdaterGetSharedInfo: Failed to open firmware
%s::%s: Count of certID != hashVad \n
SecurityDomain
failed to create file from %@
MBN segment    components != size of ELF segment.
failed to add payload data to DER file
AVISP1,SCodec
failed to find any usable references to \"%@\" in build manifest
no response data (httpStatus=%u)
Loaded credentials from keychain with status %d
UpdaterName
%s::%s: invalid type for rtkitos\n
%s::%s: failed to allocate data for personalized path\n
Forcing server signing\n
BbProvisioningManifestKeyHash
Using default ChipID 0x%08X to measure
setting COMMAND_CODE failed
failed to strip img3 header
<Type = 0x%08x, Length = 0x%08x>
restoreInfo
Server not reachable
%s: missing required baseband parameters
update/gold/profile.bin
%s::%s: copyFirmware: failed to find FW (%s) in build ID\n
CSEC
createRequestDict
diag
nconsumed > 0
Info.plist
restorepsi2.bin
SecItemAdd ret=%d
PSI2-Blob
No Manifest entry in the receipt, passing empty dictionary.
%s::%s: Manifest Offset: %u, Manifest Length: %u, Magic: %s\n
item->objectTag != NULL
failed to remove bbfw: %@
AP: provisioning ack failed, sending provisioning request.
Unable to locate security domain for tag %u
AMAuthInstallBasebandMAV20StitchFirmware
chipID failed to convert to data
Cellular2,SocLiveNonce
setManifestOnData
Wireless1,ScanBluetooth
RootCA has been set!
ExtDCP
failed to convert meid (%@) to data
BbServerNonce
%s::%s: could not allocate data\n
TME-HashTableBody-Blob
LocalSign
ap.ticket.unfused.key.private
failed to measure: AudioFW.elf
Failed creating dictionary for the version data.
decodedDER is NULL
buildIdentityTags not an array
Failed to compose file url
CHIP
pt.mbn
%s::%s: Invalid FDR trust object hash in client updater override\n
Wireless1,WiFiOTPDatabase
Rose-SE Shared Info: 
missing acdb or failed to measure image
STATUS1
successful tss request:<<<<<<<<<<\n%@
butn
failed to measure: ebl.fls
Requesting manifest from server (%@)
eDBL-Version
_CanaryLocalSign
%s::%s: successfully got tags\n
failed to copy payload properties to measurement dictionary.
rmsr
failed to personalize bundle
shrm.elf
%s::%s: firmware file dictionary not provided\n
-----------------------------------------------
DBL-PartialDigest
%s::%s: reset epro to false for all firmware file tags\n
%s::%s: no dataref\n
rlgo
Copying manifest property %@ into request. (Via BuildManifest)
AMAuthInstallPlatformCreateSoftLink
sequencer_ram.elf
RequestHeaderTags
defaultTag->copyValue != NULL
Failed transformatting the property List to CFData obj %@
Failed to get fusing response data from CFPropertyListCreateFromXMLData() error: %@
%27
yes
%s: bundleURL is NULL
AMAuthInstallSsoCreateServiceTicket
RPM-DownloadDigest
AppleTconUARP
%s::%s: failed to create url from string\n
Valid: %u\n
data.data && data.length
bbParameters changed, triggering bbfw re-personalization
SBUserNotificationTextAutocorrectionType
RestoreSBL1-HashTableBody-Blob
force-fusing
%s::%s: attempting to add new file to cache, but not both size and offset are provided. File: %s\n
znkudjqthe3mekdby1z33rifsdmsop
responseData is NULL
AMAuthInstallSupportCreateURLFromString
Cellular1,PMUFW
createRequest: Failed to validate device identity tags
%s::%s: failed to get file system reprensetation\n
VinylRestore::copyFirmwareUpdater kUpdaterDeviceInfo value : 
%s failed: %@
AMAuthInstallApFtabCreateMeasurementsWithTag
iBootTest
MBN qti_certificate_chain_size overflows file
Blob
unsupported URL scheme
%s::%s: mainFwData not present in the input\n
Multitouch
expected outputDict as a dictionary
%3B
Personalization SoC Live Nonce
%s::%s: ldrVers count is zero\n
dvf1
mistyped statusNum
IsiBootEANFirmware
DestBundlePath
ACFUFTABFile
%s::%s
MAX
mdmddr.mbn
x-intnt-certcepo
hasFile
getRecoveryFwData
glyP
%s::%s: successfully created request\n
chipRev
DERDecoderInitialize top level failed
AMAuthInstallUpdaterCryptex1LocalPolicyCreateRequest
_
failed to convert fusing program to xml
Error writing file
char3
failed to measure %@ with error: %@
x-intnt-apsecuritymode
AMAuthInstallSupportWriteDataToFileURL
Personalization Payload Tag
copyFirmware: failed to init certification firmware
hyp.mbn
AMAuthInstallProvisioningServerSendSyncRequest
copyPersonalizationSSOToken symbol not found
%s: failed to set updater response tags, result=%d
Wireless1,UseGlobalSigning
missing security pack
Ap,RestoreTMU
Cryptex1,AppVolume
invalid length fw loader version
This is an install/stitch-only request.
dict is not CFDictionary
%s::%s: failed to determine if url exists (%u)\n
%s: failed to apply tss overrides
failed to create bbfwURL
DBL-DownloadDigest
Failed to close file in zip %s with error: %d %d
goldDict: 
failed to create build identity with overrides
cryptex1-certificate-format
unsupported property type: %d\n
Cryptex1,CryptexInfoPlist
failed to read chipid
failed to retrieve credentials from the keychain
Ap,SoftwareNonceForUpdateFreshness
*manifestData is NULL
Ap,ProductType
%s::%s: Rose Hardware Info (Board ID: 0x%04x, Chip Revision: 0x%04x)\n
Missing string for path key
failed find measurementsDict for entry %@
personalize=%s
BBTicket
mastered_signed_len(%d) + 8 is not a multiple of %d
mainDict: 
NULL session
Error HostCreate
AMAuthInstallApSetParameters
Crypto error
bad local signing key: %@
created digest is NULL
Ap,LocalBoot
gtgv
AMAuthInstallBasebandICE3FirmwareSupported
%3A
LTEFW-HashTableDigest
%s: failed to set updater tags, result=%d
ioBufferLength != NULL
upc.elf
Error key->string
failed to set recovery entitlements
fileSize=0x%x, srcOffset=0x%x, codeSize=0x%x
Cellular1,BbActivationBypassEnable
%s::%s: failed to update file data\n
found SBL header
%s::%s: tag '%s' not found in build identity, skipping validation\n
nonce
personalize=%s %@ ecid=0x%llx, chipid=0x%x, boardid=0x%x, secDom=%d, isProduction=%s, EPRO=%s, isSecure=%s, ESEC=%s, img4=%s, demotionPolicy=%@, managedBaaCert=%s, slowRollBaaCert=%s, dpoc=%@
osbl.mbn
replaced NULL response dictionary with cumulative response
%s::%s: Didn't find a matching embedded ftab\n
ftab.bin
UpdaterRef
Wireless1,Wifi2GLMAC
Ap,SelectNewEpochKey
AVISP1,AudioRight
CarrierID
Vinyl Tags %d Measurements %d
Attempting to load credentials from keychain
/usr/lib/libacmobileshim.dylib
%s::%s: specified tag name is invalid!\n
Rap,FDRAllowUnsealed
failed to convert security domain %@
%s::%s: file path has not been initialized\n
/update/gold/info.plist
requestDictValuesBuffer allocation failed
AMAuthInstallBasebandSetKeyHashInternal
_AMAuthInstallBundleInstallPersonalizedBasebandFirmware
%s: failed to allocate allUpdaters
%s::%s: failed to create personalized rooted FW URL (status: %d)\n
InternalBuild
cryptex1-key-scheme
global ticketData is NULL
%s: failed to allocate chunk buffer
AMAuthInstallBasebandWriteFilesToBbfw failed
%s::%s: failed to allocate internal data structure\n
Nonce
ap.ticket.localpolicy.hacktivation.leaf.cert
%s::%s: failed to validate device identity tags\n
%@,Nonce%@
%s: failed to write finalized image3
amai->bbKeyHashesOverrideDict is NULL
no
%s: CFURLRef passed, retaining copy
AMAuthInstallSetFDRRequestEntry
signing NOT supported
RamPSI-Personalized
DeviceIdentityCreateClientCertificateRequest is not available
200
stitchData is %lld, expected size is %d
%s: failed to create CFUserNotification
%s::%s: failed to init logging\n
AMAuthInstallApImg4StitchRestoreInfoWithAMAI
AMAuthInstallUpdaterCryptex1LocalPolicyCopyDeviceInfo
failed to create an AP ticket URL
[%s] 
Failed to validate delivery object
ProductionUpdatePayloadHash
%s: amai->apParameters is NULL
%s::%s: no file name specified\n
dict && key && out && outLen
VinylTransport::getTicket  firmwareLoaderVersion: 
-[AMAuthInstallOSSsoAuthenticator authorizationController:didCompleteWithAuthorization:]
GetFusingProgram
no server URL
no chip rev
dali
wb
interactivity
No
BT_MAC2:%@
%u
Deserialized plist data is not a dictionary firmwarePlist: 
%s::%s: Unable to allocate memory for fullPath:\n
alpm
_StopRunLoopPerform
AMAuthInstallMonetSetVersionAndPartialDigest
@UUID
PersonalizationInfoArray
Cannot parse UpdateTable entries
/update/gold/firmware.der
getFileDataFromZip fwSrcPath: 
provisioningDict is NULL
SN
Keep-Alive
%s::%s: Tag: %s :: Offset: 0x%04x Raw address: 0x%lx, size: %u\n
Dali
CFDictionaryCreateMutable failed to allocate
Buttons1,ButtonsFirmware
USBPortController1,USBFirmware
EBL Digest: %@
16305813941943436
failed to write receipt: %@
this build lacks UniqueBuildID
libauthinstall_device-1155.40.8
copyFirmware: failed to find FW
gtcd
VendorID
com.apple.EmbeddedSoftwareRestore.Baseband.ChipId
override path: %@
_AMAuthInstallMonetStitchFirstStage
%s::%s: failed to retain file data\n
failed to add private
Options.plist
signing support check completed
%s: failed to allocate parameters for %@
MacEFI
DSP2-HashTableDigest
did not find %@ for %@ updater in the response
_FlsParserFinalize
Wireless1,ACIBT
Alignment
2
PAICHUSUO RGN:%@
BbBehavior
LocalSigningID
CentauriUpdaterGetTags
eUICC Param %d changed
local signing is enabled
size of MQRD doesn't match
getFWSrcPath
hacktivated
SE,Bootloader
ticketPath %@ , withApTicket is %s,  (!%s && ( %s || %s))
\"
AudioAP1,RTKitOS
.plist
%@: version=0x%x, personalizationOffset=0x%x
%s::%s: Tag %s doesn't exist -- continue...\n
%s::%s: failed to build parameters out of device identity\n
copyToPersonalizedBundlePath
TME-HashTableBody
%s::%s: fFirmwareFile has not been initialized.\n
ApEffectiveProductionMode
Cryptex1,RosettaTrustCache
AMAuthInstallMonetCreateReversedMEIDFromString
Bad partial digest length
copyFirmware: failed to remove bundle fw personalized bits
AMAuthInstallApImg4GetPayloadPropertiesData
%s: _AMAuthInstallGeneratePersonalizationEntries() failed: %d
SBUserNotificationBehavesSuperModally
%s: response items not found
@Cellular1,Ticket
AMAuthInstallApImg4EncodeRestoreDict merged restoreInfo failed
%s::%s: failed to get backing length\n
Failed to locate FTAB in super binary
Wireless1,Wifi2GLPhy
failed to add Ap Img4 tags
casy
SE,RapSwBinDsp
AudioFW.elf
DPC.elf
AMAuthInstallBasebandVinylAddMeasurementTags
dtrs
Unable to locate tag number in device info
local signing is not available for production fused devices.
Failed to create partialDigestData
TICKET_VERSION
x86,UseGlobalSigning
%@ updater bundleCopierCallback returned NULL.
copyFirmware: failed to create personalized FW URL
WARNING
%s::%s: failed to open bbfw archive for reading\n
illb
chipID: 0x%x is not supported for local signing
failed to create sso data %@
Failed to initialize SSO
%s: failed to save username in keychain
BbfwReaderFindAndCopyFileData
%s::%s: tag '%s' has different values in device info and build identity\n
Cannot parse ImageBinary.apdus
mefi
BbNonce
ApRequestEntries
escapedValue == NULL
Cryptex1,Type
AMAuthInstallApImg3Finalize
ucon
AMAuthInstallBundleGetManifestEntry
keyPath is NULL
AMAuthInstallBasebandCopyAllPersonalizedComponents
restoresbl1.mbn
AMAuthInstallMonetLocalProvisionDevice failed
Failed to create data for empty manifest
%s::%s: invalid optimization mask\n
RTKitFirmware
Provisioning
TagPrefix
failed to add payload version to DER file
AMAuthInstallBasebandN41SupportsLocalSigning
%s: receipt is NULL
Firmware/%@/Rooted/ftab.bin
%s::%s: destination bundle was not specified, so we are skipping the copy step...\n
failed to measure: CDMA2KFW.elf
AMAuthInstallBundleOverrideEntry
%s::%s: converting from string to number\n
\tticketName: %s\n
postflight
input.data && input.length
IODeviceTree:/chosen
AMAuthInstallProvisioningProvisionIfNecessary failed
restorexbl_sc.elf
Ap,ANE1
cros
ProvisioningManifestExists
%s::%s: failed to copy file data\n
Rap,ProductionMode
fwMacData: 
failed to read data from %@
BbChipID
failed to reverse imei, adding original string to response
RGN
Name
BasebandProvInfo
eUICC,ProfileDataGold
KernelCache
no baseband chipid found in identity, but baseband returned snum. Can't preflight baseband personalization.
ACMobileShim dylib found
Personalization Board ID
plistFilePath : 
failed to check %@ alignment
Ap,RestoreSecurityOverrides3
Nothing to sign, skipping..
Unable to locate firmware data
Wireless1,SecurityDomain
%s::%s: updater options has wrong type\n
DERDecoderInitialize sequence failed
invalid overridesKey
%s: _AMAuthInstallBundleCopyOverrideBuildIdentity() failed: %d
PINECRESTID
%s: _AMAuthInstallSsoCreateUserNotificationSettings failed
x86,Ticket
%s::%s: failed to create number\n
00000000  
Info.Variant
DestURL
not found in this file
NULL parameter
%s::%s: failed to remove bundle fw personalized bits\n
%s::%s: firmware data container is invalid\n
Failed to parse 'seci' value
RamPSI Version: %@
chipID changed
AMAuthInstallBasebandVinylLocalHandleRequest
Invalid image3
No data in partial digest
Cellular2,Nonce
PL
%s::%s: boardID is empty or isn't data type\n
BatteryPlugin
_AMAuthInstallApImg4CreateDefaultRestoreInfo
x-intnt-apboardid
DERDecoderGetDataWithTag
PCIE
CF=(
%s::%s: failed to add certId-VAD sequence\n
BbRequestEntries
14640371804122341
num != NULL
%s: requestDict mistyped
Public key is NULL
lphp
MBN hash_table_size is zero
updater->requestTags is NULL
SinopeUpdaterCreateRequest: failed to open firmware
%s: input options: %@
ObjectName
BbCalibrationEnable
_CFDictionaryGetBoolean
no-cache
device info value converted: 
buildVersion
%s::%s: Identified chip as R1\n
EXPORT_REQUIRED
getFileDataFromZip
failed to stitch vinyl fw
AMAuthInstallBasebandMAV10StitchFirmware
failed to measure: legacy_rat_fw.elf
can't parse response (%u bytes of apparent garbage)
BbSNUM
%s::%s: Manifest digest\n
Cryptex1,GenericTrustCache
%s: tagStr is NULL
getVersion
%s::%s: file not open\n
100
%s::%s: digestRef memory alloc failed\n
Firmware/device_map.txt
failed creating the field key %@ Path.
%s::%s: Boot nonce set for FTAB. Boot nonce value: %llu\n
sha2-384-trunc-256
%@-Personalized
B64_SECDATA
%s: failed to allocate options
%s: buildIdentityCallback is NULL
SN200V (Ceres)
Encoded header is larger than data.
#
%s::%s: no manifest found in ftab\n
%s::%s: context passed is null\n
%s: failed to get CFUserNotification textField values
Cellular1,ProvisioningFirmware
%s::%s: failed to add new file\n
CFELoader
%@,SecurityDomain%@
failed to convert statusNum
bb.rembrandt.gold.leaf.public
Read error or stream too big
ApImg4Ticket
Ap,EngineeringUseOnlyUnit
You are not authorized to make this request. Please check your device or credentials
rkos
amai/receipt.plist
BbFactoryDebugEnable
%s::%s: data length %ld is not within range\n
%s::%s: mainProfileData not present in the input\n
Cryptex1,AppTrustCache
GNSSFW-DownloadDigest
SE,ChipID
AMAuthInstallSupportGetValueForKeyPathInDict
eUICC IM4P
SoftwareUpdateSSO dylib not found
Ap,RestoreSecurityOverrides1
amai->apParameters is NULL
failed to measure: TPCU.elf
AMAuthInstallMonetStitchMav25EBootLoader
updater_log (RestoreInfo): %s
Personalization FTAB Payload Tag
Timer,ECID,%u
%s::%s: VinylUpdaterCreateRequest  ACFUInitLog returning %d\n
outEscapedValue == NULL
_AMAuthInstallSsoCreateUserNotificationSettings
com.apple.MobileSoftwareUpdate
eUICCFwReader
failed to add %@ property for '%@'
Content-Length
failed to create link: %s
CFHTTPMessageCreateRequest failed
AMAuthInstallIsICE19BBGoldCertIDECDSA
bb.rembrandt.ticket.root
_AMAuthInstallRembrandtLocalCreatePSIStitchData
%@ updater getSharedInfo call failed, error=%@
Error ReadStreamRead
Error WSAStartup
productionStatus
RoseRestoreHost
calibration key status=%d
ERROR: Authentication completed with error: %@.
_AMAuthInstallSupportCreateDataFromCopiedOrMappedFileURL
entry.data && entry.length
no variant published for this device (chipID=0x%08X boardID=0x%X secDom=%d bbChipId=0x%08X) in build manifest
failed to copy build variant %d
BbUploadEnable
AMAuthInstallApImg4AddInteger64Property
Ap,AppleVideoEncoder4
failed to measure: partition.mbn
failed to check conditions
AMAuthInstallMonetMeasureEBootLoader
%s: failed to create empty ticket
%s: failed to set updater loop instance, result=%d
signingServerURL is malformed
%s::%s: cannot setData for a memory optimized data container.\n
%s::%s: Chip major revision seems unreasonable: %d\n
%s::%s: failed to create CFString\n
%s::%s: failed to get im4p values\n
AMAuthInstallBasebandSupportsServerSigning
failed to measure: SYS_SW.elf
server provided unneeded baseband data; ignoring it
Invalid response
Attempting to add additional entries to HTTP header
Details: 
No component name in options dict
SE310S (Juno)
ran3
ap.ticket.unfused.key
APPS-HashTableDigest
RoseUpdaterGetSharedInfo: failed to get dict entry for sbd1 digest
AMAuthInstallBundleCopyPublishedVariantsArray failed
MEID:%@
TSS Connection attempt %d of %d.  (Will retry if TSS_ERR_SERVER_NOT_REACHABLE.)
failed to convert chipid
DFUFileType
LEGACY Server based provisioning enabled. Reading provisioning key from settings.
VinylTransport::getTicket  mainFwMac: 
%s: invalid datatype
AMAuthInstallUpdaterCryptex1LocalPolicyCopyTicket
Credentials not found
3GFW-HashTableDigest
DebugArgs
copyFWDataByName
%s::%s: RoseUpdater Version: %s\n
%s::%s: leaving: VinylRestoreHost: %s\n
RecoveryOSiBSS
Ap,TargetType
%s::%s: no firmware override specified\n
%s::%s: This function has not been implemented\n
Personalization Prefix Needs Logical Unit Number
AMAuthInstallApImg4LocalCreateEncodedCertificateChain
_AMAuthInstallBundlePopulatePersonalizedBundle
failed to get CFUserNotification textField values
failed to create firmware
Ap,MSRFirmware
AMAuthInstallBasebandJ2StitchFirmware
AMAuthInstallBundleProcessRules
@AlternateSU
AllowNeRDBoot
failed to copy EBL
Fail to validate delivery object.
RestoreAOP
SE,RootKeyIdentifier
%s::%s: failed to convert tag '%s' from build identity type (%s) to tss-request map type (%s)\n
failed to measure: TDS.elf
failed to compute digest
SSOHost
%s::%s: no digest in build ID (%s)\n
_AMAuthInstallSsoSaveCredentialsInKeychain
%@ updater queryPersonalizationInfo call failed, error=%@
firmware map: 
Failed to create propertylist from data, error: 
%s: objectTags is NULL
%s: AMAuthInstallBundleCopyBuildIdentityForVariant() failed: %d
_AMAuthInstallBundleGetMatchingSoftwareCoprocessorBuildIdentity
_AMAuthInstallBundleLocalPolicyCopyDefaultNSIH
\tpayload: %s\n
AppleConnect user canceled
Personalized
AMAuthInstallSupportCopyFile failed.
_AMAuthInstallSsoCopyPasswordFromKeychain
%s::%s: tag '%s' not found in device info, skipping validation\n
%s::%s: entering: %s\n
%s::%s: VinylFirmware destructor called\n
ftap
AMAuthInstallBasebandN92MeasureFirmware
%s::%s: Get InfoPlist Data from Zip failed\n
%s: failed to get manifest entries
AMAuthInstallApFtabStitchTicketData
failed to find entry for %@
RecoveryMode
statusNum is NULL
GNSS_FW.elf
RequestManifestProperties
Personalization Manifest Suffix
tasf
Ap,DisplayVendorCalibration
AMAuthInstallApImg4LocalCreateEncodedData
%3C
ProductionCMAC
Wireless1,BTOTPDatabase
%s::%s: failed to create capabilities object\n
SE,RapRTKitOS
Failed to load file %@:%@
Null inputs
AMAuthInstallGetFirstVariantInBundle
Neither main nor gold vinyl fw found!
AMAuthInstallBasebandWriteFilesToBbfw
ASAuthorizationController
item %@ not a dictionary
Wireless1,WiFiRx
%s::%s: failed to acquire file path string\n
Wireless1,FDRAllowUnsealed
No buildIdentity key
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
Timer,ChipID,%u
i
%s::%s: failed to init data container object\n
Personalization Chip Revision
AMAuthInstallApImg4ReCreatePayloadWithProperties
%s::%s: no manifest preset in dataref\n
crwn
%s::%s: failed to get build identity dict from options\n
%s::%s: input data has no bytes\n
HardwareInfo
rlg1
phyb
tbms
Ap,NextStageCryptex1IM4MHash
%s::%s: epro data to boolean conversion failure\n
The server could not find the resource requested
----Begin response
AMNM
AMAuthInstallUpdaterCopyTags
%s::%s: Failed to find firmware in restore options\n
Failed to parse updatePayload as per UpdatePayloadItemSpec
B64_MEID
signature_offset %d >= sizeToMeasure %lld
tss-request-bb-local
CFDataGetLength(amai->bbParameters->snum) %lld != snumLength %d
%s: failed to get CFUserNotification response dictionary
\n%@\n
keyHashName is NULL
%s: failed to create request
mistyped encrypted session key
ApDemotionPolicyOverride
Content-Type
setManifestToTopOnData
Personalization Nonce Hash
TagNumber
bad or missing SNUM
AMAuthInstallSupportBase64Decode
No bundleURL
AMAuthInstallApImg4AddInteger32Property
lckr
sbl1.mbn
Failed setting (from build manifest) %@ = %@
info.plist is NULL
%s::%s: optional tag %s missing from build identity, skipping\n
failed to create host object
VinylUpdaterCopyFirmware
mistyped gold nonce
kExpectedOEMSignatureSize == kOEMSignatureSize || 0 == kOEMSignatureSize
_FlsParserFindDownloadItem
%s::%s: cannot update a file if no files exist\n
Cryptex1LocalPolicy
%s::%s: Adding new file to FTAB cache. File: %s, offset: %u, size: %u\n
VinylUpdaterCreateRequest
%s: request is NULL
failed to convert boardID
dtre
Variant
_AMAuthInstallBundleInstallPersonalizedEntry
Ap,InternalUseOnlyUnit
SOCKS proxy host is NULL
Failed to create hashTableBodyData
AMAuthInstallApImg4CopyPayloadVersionProperty
Ap,rOSLogo1
Cryptex1,AppOS
POST
AMAuthInstallLog
%s::%s: Failed to allocate output dictionary\n
%s::%s: failed to update manifest\n
%s::%s: creating request\n
failed to add Digest property for '%@'
_AMAuthInstallSsoCopyCredentialsFromKeychain
%s: invalid %@ response tag %@
Cannot allocate for tmpData
*********************************
Yes
could not prepend entryName to destination path : %@
chipid: 0x%08X unsupported for img4 local signing
version=0x%x, personalizationOffset=0x%x
Request Dictionary:
\tManifest: %@\n
eUICC,MainRecoveryFw
rdtr
_AMAuthInstallSsoAuthSvcsCreateServiceTicketWithAppId
fileVersionLog
index>=0 && index<fObjs.size()
%s: not match found for request tag %@
$s: failed to get tag buffer length
Class getASAuthorizationControllerClass(void)_block_invoke
com.apple.AppleConvergedFirmwareUpdater
securityMode
signing support check failed
SBL1-HashTableBody-Blob
Rap,BoardID
Cellular2,BbActivationManifestKeyHash
dsp2.mbn
relativePath != NULL
failed to create im4p with override tag
( LETOH( header->qti_metadata_size ) == 0 ) || ( LETOH( header->qti_metadata_size ) == sizeof(mav25_authority_meta_field_t) )
%s: responseTags is NULL
qdsp6sw.mbn
createBoolFromData
FTAB:\n
Wireless1,UID_MODE
error:
invalid requestDictKeysBuffer array
Mature baseband found, doing two stage provisioning
RamPSI-Blob
Personalized Bundle FW URL: 
sec.elf
clearing overrides
Existing provisioning manifest found. Not attempting to provision.
%s: tags is NULL
%s::%s: failed to initialize LAI lib create function\n
Invalid img3 object
sha2-256
mistyped fusing status
MBN image_size overflows file
tagPrefix is NULL
Wireless1,FdrRootCaDigest
baseband updater output: %@
NSErrorDomain getASAuthorizationErrorDomain(void)
failed to create soft link: %@
hw.product
B64_BB_CHIPID
Error getting length of request
Payload - 4cc <%@> - Version <%@> - TLVs - %@
Rap,FdrRootCaDigest
invalid HashKeysBuffer array
USB_ETHER_MAC:%@
%s::%s: enable gid3En for iboot\n
%s::%s: failed to get dict entry\n
Cannot parse DeliveryObject.binaries
SESA
snum changed
.bbfw
%2A
fileData argument is NULL
InstanceA
EPRO
%s::%s: failed to open file error: (%s)\n
saveFirmware
failed to stitch manifest header to file: %s
zero length euicc main nonce
inApECID is zero
ModemStack-SecPackDigest
handleMessageCFType
Wireless1,BTRegData
failed to parse debug arguments
RTKitOS
failed to set override object properties for %@
%s: entryKey is NULL
skipping \"%@\" entry
No dstURL provided. Running in restore environment?
Wrong UpdateTable entries
chg1
%s: outTags is NULL
initCache
saveToPath
Unable to locate production status for tag %u
%s: os image info personalized field is empty
getTags
failed to convert chip ID %@
acfw
AudioAP1,SoftwareBinaryDsp1
T_MAC
com.apple.accessoryupdater.uarp
%s::%s: Failed fo retain firmwareDict\n
rpm.mbn
%s: failed to copy receipt
<%@: \r
boot nonce has wrong size
%s::%s: failed to create dirPath\n
RestorePSI-PartialDigest
AMAuthInstallBasebandMAV22StitchFirmware
Found a SOCKS proxy setting. Will attempt to use it.
Cellular1,BbActivationManifestKeyHash
vinylgetFwData fwSrcpath: 
hw.machine
Failed to convert bb filename to cstring
Server message failed to convert: %d
Cellular1,CdpHost
%s::%s: cache does not have entry for file %s. Cache is invalid\n
/update/main/info.plist
%s::%s: Failed to alloc create plistFilePath CFString\n
AMAuthInstallApImg4CreatePayloadWithProperties
VinylFirmware
ENANDPRG-PartialDigest
QueryLoop0 not in request
%s::%s: failed to find FW (%s) in build ID in personalized path\n
%s::%s: converting from data to number\n
Firmware override must be specified if build identity dictionary is empty
| 
UseGlobalSigning
removing personalizedEntry %@
%s::%s: something went wrong, extra bytes in file\n
CFDictionaryRef  _Nullable SoCUpdaterExecCommandDynamic(NSString *__strong _Nullable, SoCUpdaterLogSinkFunction _Nonnull, void * _Nonnull, CFStringRef _Nonnull, CFDictionaryRef _Nonnull, CFErrorRef * _Nullable)
Timer,BoardID,%u
%s::%s: failed to create im4p\n
AMAuthInstallBundleCopyPublishedVariantsArray
AMAuthInstallBundleOverrideRecoveryOSBuildManifest
%s::%s: Key: %s not found while parsing debugArgs, but this is not error\n
missing key 
DemotionPolicy
AMAuthInstallApImg4StitchData
UID value of %ld exceeds maximum array bound of %d\n
LTEFW.elf
Provider cannot perform authorization
Class getASAuthorizationSingleSignOnProviderClass(void)_block_invoke
provisioning/manifest.bin
\trequestTags = %@\n
Status
failed to create key substring
RestorePSI-Version
%s::%s: Generation: %u, Valid: %u, BootNonce: 0x%08llx\n
%s::%s: =========== FTAB Header ===========\n\n
%s::%s: failed to create empty data\n
\tchipRev: %u\n
Cannot init sequence for ImageBinary.apdus
OSRamdisk
digest type in the build manifest is not supported
diss
eUICC,ChipID
%s::%s: wrong chip rev type\n
[%@]: %@ is FTAB subfile with tag '%@', extracting\n
%s::%s: invalid params passed\n
getFileDataFromZip fullPath: 
http://vega-dr.apple.com:8080/vegads/fuser
BT_MAC2
AMAuthInstallApCreateHashFromURL
DevelopmentCMAC
%s::%s: Using FDR trust object hash in updater options override\n
cfTypeDescription
Wireless1,OSLongVersion
AMAuthInstallBasebandPersonalizationRequired
SourceURL
~%d
Error getting length of response
eDBL-PartialDigest
%s::%s: failed to create request dict\n
%s::%s: Missing = for key: %s\n
YonkersIR1,SepObject
AMAuthInstallApImg4FindItemWithTag
outError && outMeasurementDict
%s::%s: No sources found \n
_AMAuthInstallBundleCopyOverrideBuildIdentityRecoveryOS
SSO function returned NULL and no SSO token was provided, SSO disabled.
1.2.12
%s: AMAuthInstallCryptoCreateDigestForData_SHA3_384 returned %d: %@
rsa4096
failed to create dictionary from device_map (Not plist/xml data?): %@
rspt
AMAuthInstallSsoCreateToken
AMAuthInstallBundleCreateURLForKeyEntryInBuildIdentity
createIm4p
Alamo
$
hashSectionTag argument is NULL
PartitionTable-Digest
%s::%s: paddingAfterManifestEnd %u bytes\n
Wireless1,SecurityMode
oauth-pkce
RecoveryOS%@
Count of certID != hashVad
%s::%s: Bad chip ID size\n
tafwLdrVerToFindg4cc : 
Ap,OSReleaseType
AMAuthInstallUpdaterSetInfo
Cannot parse ImageBinary.
kVinylBypassSEPPairing value: 
%s::%s: Deviceinfo is not a dictionary\n
fileData is NULL
Ap,RestoreCIO
AMAuthInstallBasebandICE3MeasureRamPsi
Cellular2,FDRAllowUnsealed
bypass-nvm-sync
ManifestEpoch
RoseUpdaterGetSharedInfo: sbd1 digest is of an unexpected type
kSEOptionDeviceInfo is neither CFData or CFDictionary
BasebandFirmware
%lu
Failed to remove file at '%@' (%@)
Personalization Chip ID
Cannot parse property
signing done
AMAuthInstallBasebandRembrandtMeasureFirmware
using SSO.
%s::%s: rrko bundle data unavailable\n
/firmware.der
phlt
Cryptex1,RosettaOS
```
