# `/System/Library/PrivateFrameworks/CoreServicesStore.framework/CoreServicesStore`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 515,952 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 4152)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/System/Library/PrivateFrameworks/CoreServicesStore.framework/CoreServicesStore (compatibility version 1.0.0, current version 1141.1.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.12)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (9 classes, 3 protocols)

Classes: `CSStoreAttributedStringWriter`, `NSAttributedString`, `_CSStore`, `_CSStore2DataContainer`, `_CSStoreAccessContext`, `_CSVisualizationArchiver`, `_CSVisualizer`, `_CSVisualizerPredicate`, `_CSVisualizerTableFunctions`

Protocols: `NSCoding`, `NSCopying`, `NSSecureCoding`

## Strings (853)

```
flag:name:color:
dealloc
T@\"NSPredicate\",&,N,V_unitDescriptionPredicate
write:code:
writeUnit:inTable:
beginFlags:flags:
initWithLeftExpression:rightExpression:modifier:type:options:
setCaseSensitive:
writeSeparator
_numericPredicate
getDescription
getRanges:inDescription:options:limit:searchedInRange:
initWithVisualizer:fileHandle:closeWhenDone:error:
isFileURL
missingFlag:name:
numberWithUnsignedShort:
writeUnit:inTable:state:
elidesEmptyValues
objectForKeyedSubscript:
predicateWithFormat:argumentArray:
provideVisualizerToConnection:fileHandle:providerBlock:
removeObjectForKey:
setTimeZone:
visualizer
TB,N,GisReadOnly,SsetReadOnly:
attributedString
handleFailureInFunction:file:lineNumber:description:
initWithStore:
numberWithDouble:
queryItems
replaceCharactersInRange:withAttributedString:
setGetSummary:
numberWithBool:
p
countByEnumeratingWithState:objects:count:
initWithBytesNoCopy:length:deallocator:
longLongValue
T@\"NSLocale\",C,D
valueWithRange:
predicateOperatorType
unitDescriptionPredicate
withTextColor:block:
TB,R
finishWriting
initWithFormat:locale:arguments:
replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:
setAllowsFractionalUnits:
setUnitIdentifierExhaustionHandler:
write:bool:
decimalNumberWithString:
T@?,C,V_getDescription
uppercaseString
_functions
cs_writeToFileHandle:
T@?,C,V_getSummary
_lock
setReadOnly:
setUnitDescriptionPredicate:
_accessContext
_title
addAttributes:range:
bytes
dateWithTimeIntervalSinceReferenceDate:
expressionWithFormat:argumentArray:
initWithDomain:code:userInfo:
isEqualToString:
_fileHandle
comparisonPredicateModifier
pathExtension
setVisualizer:
stringFromByteCount:
initByMovingStore:
UTF8String
decimalNumberWithDecimal:
deleteCharactersInRange:
encodeXPCObject:forKey:
initWithExpression:
newWithBuffer:
pAllocatedLength
initWithFormat:
indexSet
initWithCapacity:
intValue
childUnit:unit:
initWithBytesNoCopy:length:encoding:freeWhenDone:
initWithStore:useStandardTableFunctions:
setGetDescription:
value
write:format:
enumerateValuesForTitlesInDescription:block:
handleFailureInMethod:object:file:lineNumber:description:
setPath:
unsignedLongLongValue
write:args:
withReferenceToUnit:unit:block:
absoluteString
breakDownTable:inStore:buffer:
writeMetadata:forStore:error:
compressedDataUsingAlgorithm:error:
expressionForVariable:
failWithError:
setCalendar:
subpredicates
_unitDescriptionPredicate
evaluateNumerically:
objectAtIndexedSubscript:
writeAllUnitsInTable:block:
writeArrayID:
writeNumber:
childUnit:table:unit:
expressionType
numberWithUnsignedLong:
numberWithUnsignedLongLong:
rangeOfString:options:range:
T@\"_CSVisualizer\",R,V_visualizer
insertsNewlines
encodedData
initWithVisualizer:fileHandle:closeWhenDone:allowCompression:error:
systemLocale
writeDictionary:error:
TB,D
_searchString
beginProvidingVisualizationArchivesWithMachServiceName:queue:creatingVisualizersWithBlock:
write:number:
.cxx_destruct
_writer
_visualizer
caseInsensitiveCompare:
numberWithUnsignedInt:
write:arrayIDs:count:
T@\"NSMutableDictionary\",R,V_userInfo
_userInfo
allocWithZone:
encodeWithCoder:
linkURL:linkedAttributedText:
write:array:
currentHandler
write:interval:
rightExpression
initWithContentsOfURL:error:
timeIntervalSinceNow
write:separator:
writeSeparator:
setUnitsStyle:
string
_attributedString
cs_rangesMatchingPredicate:
evaluateWithObject:substitutionVariables:
initWithType:subpredicates:
separatorForTitle:separator:
setTimeStyle:
write:arrayStringID:
_impl
attribute:atIndex:effectiveRange:
init
initForSharedReading
writeAllUnitsWithBlock:
stringFromDate:
encodeObject:forKey:
enumerateReferencesToUnit:inTable:block:
setElidesEmptyValues:
evaluateWithObject:
write:attributedString:
writeLink:unitID:linkedText:
initWithString:attributes:
isReadOnly
appendString:
expressionForConstantValue:
fileSystemRepresentation
getSummary
leftExpression
predicateWithFormat:
withAppliedAttribute:value:block:
_store
fwrite:size:numberOfItems:error:
enumerateIndexesWithOptions:usingBlock:
linkURL:
unlock
write:format:args:
newWithStore:buffer:
unsignedIntegerValue
_operator
getWriteUnitState:forTable:
mutableCopy
objectForKey:
predicateForSearchingDescriptionWithString:error:
stringByAppendingString:
.cxx_construct
getUnit:inTable:fromURL:
numberWithUnsignedChar:
processCommandFromConnection:fileHandle:providerBlock:
withWarningColors:
_getDescription
URLByAppendingPathComponent:isDirectory:
functionsForTableNoCopy:
initWithSearchString:operator:error:
writeAttributedString:
new
finishEncoding
initWithSearchString:forTitle:operator:error:
missingFlag:name:color:
readOnly
substringWithRange:
link:unit:linkedAttributedText:
getCString:maxLength:encoding:
initWithCoder:
temporaryDirectory
timeIntervalSince1970
write:
URLForUnit:inTable:
domain
endFlags
getFileSystemRepresentation:maxLength:
linkURL:linkedText:
calendarIdentifier
setStandardTableFunctions
stringWithUTF8String:
T@\"_CSVisualizer\",&,D
_stats
doubleValue
initRequiringSecureCoding:
link:unitID:linkedAttributedText:
stringFromTimeInterval:
stringByAppendingPathComponent:
_getSummary
characterAtIndex:
initialize
link:unit:linkedText:
predicateWithValue:
scanDecimal:
scanHexLongLong:
T^{__CSStore=},R,V_store
appendBytes:length:
copy
dictionaryWithObjects:forKeys:count:
operatorIsNumeric:
scanString:intoString:
setDateStyle:
stringWithFormat:
keyPath
predicateFormat
_closeWhenDone
componentsJoinedByString:
copyWithZone:
description
enumerateReferencesToUnitsInUnitDescription:block:
errorWithDomain:code:userInfo:
enumerateAttribute:inRange:options:usingBlock:
enumerateAttributesInRange:options:usingBlock:
getBytes:length:
setAccessContext:
stringByDeletingPathExtension
translateNSPredicate:error:
withTextColor:backgroundColor:block:
write:string:
_hadEPIPE
appendAttributedString:
constantValue
decodeXPCObjectOfType:forKey:
initWithFormat:arguments:
scheme
setOutputFormat:
store
lowercaseString
_dictWriteLock
dictionary
initWithBytes:length:encoding:
predicateWithFormatString:error:
writeArray:
writeArrayIDs:count:
hasSuffix:
isEqual:
summaryOfUnit:inTable:
attributedSubstringFromRange:
enumerateKeysAndObjectsUsingBlock:
initWithBytesNoCopy:length:
setResourceValues:error:
writeString:
stringByAppendingPathExtension:
write:stringID:
addEntriesFromDictionary:
flag:name:
initWithContentsOfURL:options:error:
initWithURL:resolvingAgainstBaseURL:
length
write:arrayID:
addObject:
constantValueForExpression:
setInsertsNewlines:
writeStringID:
count
initWithString:
_outputAsXML
initWithCharactersNoCopy:length:freeWhenDone:
initWithError:
name
rangeOfValueForTitle:inDescription:
URL
insertAttributedString:atIndex:
T@\"NSAttributedString\",R,C,D
descriptionOfUnit:inTable:
initWithBytes:length:
setObject:forKeyedSubscript:
beginBitfieldFlags:
code
enumerateObjectsUsingBlock:
lock
userInfo
addIndex:
appendFormat:
array
boolValue
functionsForTable:
setFunctions:forTable:
unitDescription:referencesUnit:inTable:
initWithCharacters:length:
locale
mutableCopyWithZone:error:
writeFormat:
getRanges:matchingPredicate:inDescription:
initWithBytesNoCopy:length:freeWhenDone:
supportsSecureCoding
compoundPredicateType
init:outBuffer:
calendarWithIdentifier:
path
stringByAppendingFormat:
breakDownUsage
cs_writeToFileHandle:supportingANSIEscapeCodes:
defaultManager
link:unit:
numberWithUnsignedInteger:
setCollapsesLargestUnit:
setLocale:
addAttribute:value:range:
debugDescription
systemTimeZone
@\"NSMutableDictionary\"
@\"NSMutableAttributedString\"
v28@0:8^{_CSWriteUnitState=@@?@?@}16I24
v32@0:8I16I20r^{_CSWriteUnitState=@@?@?@}24
@40@0:8@16Q24^@32
B32@0:8@16@24
B48@0:8r^v16Q24Q32^@40
^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}
[2Q]
v32@0:8@16I24I28
@32@0:8^{_NSZone=}16^@24
v40@0:8^v16^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}24@?32
B16@0:8
v20@0:8c16
v36@0:8@16r^I24I32
@24@0:8@16
I
{shared_ptr<CSStore2::CSStoreAccessContextInterface>=\"__ptr_\"^{CSStoreAccessContextInterface}\"__cntrl_\"^{__shared_weak_count}}
v28@0:8^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}16B24
B32@0:8@16^@24
@\"_CSStoreAccessContext\"
@24@0:8^{_NSZone=}16
v32@0:8Q16@24
v28@0:8@16c24
@24@0:8@\"NSCoder\"16
B24@0:8@16
B40@0:8^I16^I24@32
v32@0:8@16d24
@24@0:8I16I20
{optional<CSStore2::AttributedStringWriter>=\"\"(?=\"__null_state_\"c\"__val_\"{AttributedStringWriter=\"_vptr$AttributedStringWriter\"^^?\"_reserved\"[30Q]\"_impl\"^{Impl}})\"__engaged_\"B}
B24@0:8Q16
v40@0:8r^{Table={Unit=b30b2I[0c]}[48c]QQII}16r^v24*32
B32@0:8@16I24I28
@24@0:8^{__CSStore=}16
@20@0:8I16
v40@0:8@16@24@?32
@32@0:8@16@24
@28@0:8^{Data=ICCSIII{Table={Unit=b30b2I[0c]}[48c]QQII}}16I24
@\"NSString\"
@?16@0:8
@?
v32@0:8@16@24
v40@0:8@16@24*32
v24@0:8@\"NSCoder\"16
@\"NSPredicate\"
v20@0:8B16
B40@0:8@16^{__CSStore=}24^@32
v24@0:8@16
{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}
v36@0:8Q16@24I32
v32@0:8I16I20@?24
v20@0:8I16
^{Data=ICCSIII{Table={Unit=b30b2I[0c]}[48c]QQII}}
@24@0:8^@16
v28@0:8r^I16I24
v40@0:8^v16@24@32
@48@0:8@16@24Q32^@40
v24@0:8@?16
@32@0:8^{__CSStore=}16@24
v32@0:8@16*24
B56@0:8^v16@24Q32Q40^{_NSRange=QQ}48
v32@0:8@16@?24
v24@0:8^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}16
@44@0:8@16^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}24B32^@36
v28@0:8I16@?20
@\"_CSVisualizer\"
@28@0:8@16c24
v28@0:8@16B24
@28@0:8^{__CSStore=}16B24
@\"NSRecursiveLock\"
@48@0:8@16^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}24B32B36^@40
B
@32@0:8@16^@24
{_NSRange=QQ}32@0:8@16@24
v24@0:8I16I20
@16@0:8
v28@0:8@16I24
@24@0:8^v16
Q
^{__CSStore=}16@0:8
v16@0:8
{atomic<bool>=\"__a_\"{__cxx_atomic_impl<bool, std::__cxx_atomic_base_impl<bool>>=\"__a_value\"AB}}
{Store=\"dataContainer\"@\"tableOffsets\"{array<unsigned int, 64UL>=\"__elems_\"[64I]}\"arrayTable\"^{Table}\"stringTable\"^{Table}\"dictionaryTable\"^{Table}\"enumerationState\"{atomic<long long>=\"__a_\"{__cxx_atomic_impl<long long, std::
^{__CSStore=}
v32@0:8@16Q24
@32@0:8I16I20@24
0x
predicate != nil
callbacks
 { buckets = %llu, count = %llu }
-----
lockdown_send
CS_ENABLE_IO_LOGGING
Tables
An exception was thrown while parsing the predicate string (interpreting as an expression because predicate parsing already failed.)
Failed to allocate NSPredicate instance.
characters
 }
_CSVTDlt
void CSStore2::AttributedStringWriter::beginBitfieldFlags(NSString *const __strong _Nonnull)
XPCRepresentation
v16@?0r*8
virtual void CSStore2::CSStoreUnfairLockAccessContext::assertHeldForWriting() const
0x%08llx %08llx:
_CSVFGColor
name
IdentifierCache
Total bytes used
CSStoreAccessContextPrivInternal.h
virtual void CSStore2::CSStoreSharedReadingAccessContext::assertHeldForWriting() const
empty count
_CSVLink
Could not find string unit %llx!
%s\n
s
CalculatedChecksum
CSStore.mm
values
wb+
virtual void CSStore2::CSStoreSharedReadingAccessContext::assertHeldForReading() const
TERM
block != nil
_CSAttributedStringWriterIsChildUnitWithTitle
ZeroedRanges
{ 
Z
Called flag() without calling beginFlags() first.
0x%llx
:%C%@
v40@?0@8{_NSRange=QQ}16^B32
EIO
Hash map at %llu has invalid buckets range %llu-(%llu*%zu)
context already held for reading
i
!( inValueOptions & ( kCSDictionaryValueOptionsStringPersonality | kCSDictionaryValueOptionsArrayPersonality ) )
hashCode
_CSVFixed
v40@?0@\"NSDictionary\"8{_NSRange=QQ}16^B32
breakdown
%@ (POSIX %.3f%@)
void CSStore2::AttributedStringWriter::beginFlags(NSString *const __strong _Nonnull, uintmax_t)
unit count
CS_VISUALIZATION_OUTPUT_XML
com.apple.CSStore
predicate
@\"NSAttributedString\"24@?0@\"_CSVisualizer\"8I16I20
<%@ %p> { p = %p, gen = %llu, length = %llu/%llu/%llu }
NEEDLE
<%@ %p> { \"%@\" }
v32@?0I8I12B16B20^B24
[ %@ ]
_CSVBGColor
1`
v32@?0@\"NSString\"8@\"NSAttributedString\"16^B24
kCSStoreBadDataErr
unit ID
v32@?0r^I8r^{_StringCacheEntry=Cb1b7S}16^B24
B
ERANGE
kCSStoreNameInvalidErr
CSStoreUnitID CSStoreAllocUnit(CSMutableStoreRef _Nonnull, CSStoreTableID, _CSStoreSize)
Operator
context not held for reading
_CSVOutputType
paramErr
Unit identifier cache entry invalid.
Expression
x-csstore-vis-unit
com.apple.coreservicesstore
v24@?0Q8^B16
_CSVFWeight
1 `
Bucket [%llu,%llu] has invalid key-value pairs offset range %llu-(%llu*%zu)
Unsupported expression type (left-hand side).
HAYSTACK
version
$HAYSTACK MATCHES[cd] $NEEDLE
CSDictionaryID _CSDictionaryCreateWithKeysAndValues(CSMutableStoreRef _Nonnull, CSDictionaryKeyOptions, CSDictionaryValueOptions, const CSDictionaryKey * _Nonnull, const CSDictionaryValue * _Nonnull, _CSStoreUnitCount, CFErrorRef * _Nullabl
t
kCSStoreConflictErr
Aggregate operations (ANY, ALL, etc.) are not supported.
context cannot be held for writing
virtual void CSStore2::CSStoreSharedReadingAccessContext::accessForWriting(void (^ _Nonnull __strong)())
void CSStore2::AttributedStringWriter::flag(uintmax_t, NSString *const __strong _Nonnull, const std::optional<RGBColor> &)
_CSbr%u
Version
Structure Sizes
SearchString
virtual void CSStore2::CSStoreUnfairLockAccessContext::accessForWriting(void (^ _Nonnull __strong)())
sizeof(Unit)
_CSVNum
^() in 
%cb%lu
Somehow thought CSStore header was OK when it's too short.
bool CSStore2::Store::reserve(_CSStoreSize, _CSStoreSize *)
table ID
length
Title
0x%llx?
kCSStoreNameAlreadyInUseErr
sizeof(IdentifierCache)
\"%@\"
_LSWarning
description != nil
visualizer != nil
os
\n
<catalog>
header length
threshold
_CSVIsRelated
v32@?0I8r^v12I20*24
static std::unique_ptr<Store> CSStore2::Store::_Create(void *, _CSStoreSize, bool, bool, NSError *__autoreleasing *)
CSPredicate.mm
C
 (%016llx)
%@
Exception
table
deleted marker
default
framework-version
v12@?0I8
\n******************************************************************************\nstore:       %p\nbytes:       %p\nlength:      %llu\ntable count: %llu\n
bytes
%@ @ 0x%llx
String caches
retainCount
NSString *CSStore2::NameOfType() [T = CSStore2::HashMap<unsigned int, CSStore2::_StringCacheEntry, CSStore2::_StringFunctions>]_block_invoke
tableCount
w+
<dictionary>
%10llu (%10s)
An exception was thrown while parsing the predicate string.
, 
v8@?0
ENOMEM
d
void CSStore2::AttributedStringWriter::missingFlag(uintmax_t, NSString *const __strong _Nonnull, const std::optional<RGBColor> &)
CSStore+Store.mm
string$
mFulErr
\n%@}
packed
errnum
rb
_CSVisualizationArchiver queue for table %@
code
%llu units
<CSStoreSharedReadingAccessContext: %p>
v16@?0Q8
CSVisualizationArchiver.mm
Checksum
[aDecoder isKindOfClass:[NSXPCCoder class]]
count
v28@?0I8r^I12^B20
invocation function for block in 
Nesting flag lists is not supported. Possible missing call to endFlags()?
Called missingFlag() without calling beginFlags() first.
<string>
*** %s ***\n
sizeof(Table)
Predicate
v24@?0I8I12^B16
{optional<CSStore2::Array>=(?=c{Array=^{Store}^{_Data}II})B}16@?0^v8
The system can only read CSStore2 files, which first shipped with iOS 9 and OS X El Capitan.
ConsumedLength
%02x
0 (const)
{
<CSStoreQueueAccessContext: %@>
v32@?0@\"NSString\"8@16^B24
lockdown_disconnect
\t
Unsupported operator type.
{ }
v40@?0I8^{__CFString=}12r^v20I28*32
kCSStoreValidationErr
New CSStore size is smaller than the old size!
Key-value pair [%llu,%llu,%llu] is in the wrong bucket (should be %llu)
FullTable
%llx
x-csstore-vis-unit:?t=%llu&u=%llu
v32@?0@\"NSURLQueryItem\"8Q16^B24
kCSStoreOldVersionErr
UsedLength
==============================================================================\n
<CSStoreUnfairLockAccessContext: %p writeOK: %d>
v24@?0^v8Q16
ls-XXXXXXXXXXXXXXXX
kCSStoreAllocFailedErr
writing
This file is in the CSStore1 format.
kCSStoreBadChecksumErr
  
`
[aCoder isKindOfClass:[NSXPCCoder class]]
@\"NSString\"24@?0@\"_CSVisualizer\"8I16I20
serviceName != nil
lockdown event
_CSVTime
fileBoundsErr
Failed to create data for store extension!
Unit %llx is out of range (total %llu bytes long.)
\t%s\n
unit
/usr/lib//liblockdown.dylib
\xf0\xf01
v64@?0@\"NSString\"8{_NSRange=QQ}16@\"NSAttributedString\"32{_NSRange=QQ}40^B56
oversized
Missing CSStore
/System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
Key-value pair [%llu,%llu,%llu] has invalid value (interpreted as Offset) %s
lockdown_checkin_xpc
attrstrwriter
Localized
0x%llX-0x%llX (%@)
*
)\n
csstore-writer-%llu-%llu.log
u
%@ (POSIX %lld%@)
_CSdwbr
void CSStore2::Store::setBytesNoCopy(void *, _CSStoreSize)
NSString *CSStore2::NameOfType() [T = CSStore2::HashMap<unsigned int, unsigned int, CSStore2::_IdentifierFunctions, 1>]_block_invoke
%llu (0x%llx)
Memory Summary
Unsupported expression type (right-hand side).
 (0x%llx)
Ran out of unit identifiers.
$HAYSTACK LIKE[cd] $NEEDLE
Destroying shared reading access context with active readers!
filecmp
GC
kCSStoreNotFoundErr
N/A (packed)
CS_SYMBOLICATE_IO_CALLERS
Called endFlags() without calling beginFlags() first.
v24@?0I8I12*16
@0x%llX, $@0x%llX
Table %s (%llx) has no remaining unit identifiers.
os-build
CS_VISUALIZATION_COMPRESSION_LEVEL
CSAttributedStringWriter.mm
Length
MKBDeviceUnlockedSinceBoot
CSStoreAssertOnIncorrectQueue
bucket count
capacity
Invalid parameter not satisfying: %@
true
void CSStore2::AttributedStringWriter::endFlags()
StringCache
    
Memory by Table
_CSMapUpdateCache
fileHandle != NULL
lockdown_recv
Collectable
Nonsensical bucket count %llu
\t\t%s(
empty marker
errno
CSStore2 dispatch data deallocation
v24@?0r^{Unit=b30b2I[0c]}8^B16
Unit %llx in table %llx has an invalid address.
kCSStorePredicateErr
os-version
v24@?0^{_lockdown_connection=}8^{__CFDictionary=}16
false
%@ offs
All units
Unit %llx is insanely long (payload %llu bytes long.)
Line
metadata
w
com.apple.launchservices.CSStore2
sizeof(Data)
Identifier caches
\t\t\t%s\n
true 
(%llx~)
Failed to create data for empty bytes argument!
v24@?0r^{Table={Unit=b30b2I[0c]}[48c]QQII}8^B16
Could not translate generated predicate to a form usable by CoreServicesStore.
virtual CSStore2::CSStoreSharedReadingAccessContext::~CSStoreSharedReadingAccessContext()
CSDictionary.mm
soft_lockdown_checkin_xpc
<array>
 
Unit %llx/%llx is garbage
Could not translate generated expression to a form usable by CoreServicesStore.
<_CSStoreAccessContext: %@>
<CSStoreDebugQueueAccessContext: %@, queueAssert: %p, queueAssertBarrier: %p>
virtual void CSStore2::CSStoreSharedReadingAccessContext::accessForReading(void (^ _Nonnull __strong)())
Failed to unpack array when preparing for new value (old count = %llu)
Beginning remote visualization service '%{public}@'
Attempting to lengthen store by %llu bytes
Refusing to allocate unit of length %llu in table %{public}s
Error calling fflush(%p): %i (%{public}s).
Unexpected predicate operator '%u'!
%s: Bogus bucketCount %u or unitlen (%u, needed %zu)
Callback block didn't vend a _CSVisualizer; no data will be returned to the Mac
Failed to construct URL for table/unit %llx %llx
Unexpectedly could not encode store: %@
could not create a copy of the store mapping while encoding store.
Wrote a ludicrously long stream (%lli bytes) that cannot fit back in an NSData.
Unable to set array capacity! Current capacity was %llu, wanted %llu
could not create dispatch data from store mapping while encoding store.
Writing store (no GC) %p with writer %p
Out-of-bounds array write: %llu >= %llu
Out-of-bounds array erasure: %llu >= %llu
Writing %llu+%llu bytes to gzip stream
Eliding empty array value for title \"%{public}@\"
Eliding empty flags value (%016llx) for title \"%{public}@\"
Could not create XPC data from dispatch data while encoding store.
Failed atomic move of temporary CSStore file %{private}@ to %{private}@: %@
*** CSStore corruption detected (4). %llx %llx %llx %llx
verifying map with file: URL %@ could not be opened
Successfully called fsync(%i)
Error funopening file handle for %{public}s: %i (%s)
Eliding value \"%{private}@\" for title \"%{public}@\"
*** CSStore corruption detected (2). %llx %llx %llx %llx
Failed to create file handle from file descriptor for store writer: %i (%{public}s).
Suppressing exception during predicate parsing: %{private}@
Out-of-bounds array read: %llu >= %llu
Failed to reserve array capacity when preparing for new value (old count = %llu)
Array was unpacked or needed to be unpacked to take new values
Mac commanded we send a store archive
file/map mismatch: file longer than map of length %#zx
Failed to save space, to the order of %.3f KB.
Error calling fsync(%i): %i (%{public}s).
Suppressing exception during expression parsing: %{private}@
Received request for service %{public}@ from connection %p: %@
File handle %p passed to _CSVisualization[Un]Archiver is not backed by a file descriptor. Will not compress/decompress.
Checked CSStore data with lengths %llu/%llu/%llu
Unexpected: garbage collection succeeded, but did not get an NSData object.
MKBDeviceUnlockedSinceBoot failed: %d %d
Failed to create _CSVisualizationArchiver for streaming visualization data: %{public}@
Failed to open file handle for streaming visualization data: %i (%s)
Ran out of unit IDs for table %{public}s (%llx): process will terminate.
*** CSStore corruption detected (1). %llx %llx %llx
Error calling fcntl(%i, F_FULLFSYNC), trying fsync(): %i (%{public}s).
Forced. Will collect.
Unsupported: file handle %p had neither an underlying buffer nor a file descriptor.
Unpacking array (or already unpacked) for value replacement
Error running garbage collection: failed to create temporary file handle
file/map mismatch between offsets %#zx and %#zx
Successfully called fflush(%p)
Store wastes %llu bytes. Will collect.
Failed to create file descriptor for store writer: %i (%{public}s).
Skipping appearance of title in range %{public}@ because it's in a range marked as a related unit
Unable to reserve array capacity! Current capacity was %llu, count was %llu, wanted %llu more
Out-of-bounds array insertion: %llu > %llu
Creating CSStore from XPC coder with length %llu
Moved temporary CSStore file %{private}@ to %{private}@
file/map mismatch: file shorter than map of length %#zx
Successfully called fcntl(%i, F_FULLFSYNC)
Error calling fcntl(%i, F_FULLFSYNC): %i (%{public}s).
Failed to map fd %i: error %i %{public}s.
Failed to allocate %llu bytes with kernel error %llx.
%{public}s: no table ID supplied
Error opening file handle for %{public}s with gzdopen(): %i (%s)
Unknown error opening file handle for %{public}s with gzdopen()
Encountered CSStore1 file, can't read it.
CSStore file has zeroed pages and has been corrupted at a low level. Offsets: %{public}@
Creating temporary file for store writer at %{private}s
Size of array unit was invalid for a CSArray; discarding
Underflow getting array capacity (%llu)
Overflow sizing array (%llu * %llu + %llu)
file/map comparison read error
CSStore checksum matches: %llx
Writing to temporary CSStore file %{private}@
Failed to open file descriptor for writing store file: %{public}@
Failed to set resource values at %{private}@ to %{public}@ (non-fatal error): %{public}@
Failed to reserve %llu bytes of virtual memory
*** CSStore corruption detected (3). %llx %llx %llx %llx
Failed to create NSData for mapped file %i.
Unrecognized reserved value %llu received from the Mac, ignoring and closing.
GCing and writing store %p with writer %p
Performing garbage collection to try to recover %.3f KB of %.3f KB.
Saved %.3f KB.
Failed to set protection of region at %p length %zu to %lx: %lx
Creating dispatch_data for XPC coder with length %llu
Creating CSStore from file with length %llu
Failed to close file handle for store writer: %i (%{public}s).
Identifier cache on table '%{public}s' is unbalanced. Will collect.
Array was packed and can remain packed with new values
Failed to convert description of unit %llu in table %llu to data: %{public}@
Writing child unit with title -- eliding value \"%{private}@\" for title \"%{public}@\"
CSStore checksum expected to be %llx, was %llx.
Failed to create file handle from file descriptor for writing store file: %{public}@
Table %llu (shifted %llu) cannot fit in the in-memory table offset list. Consider lengthening the tableOffsets field.
CSStore zero-page check could not allocate memory. Skipping check.
Failed to get file offset after GC: %@
Failed to stat fd %i: error %i %{public}s.
Disabling compression for file handle %p passed to _CSVisualization[Un]Archiver. Will not compress/decompress.
Error duplicating file descriptor for %{public}s: %i (%s)
Failed to collect-and-write store file: %{public}@
Error running garbage collection: %{public}@
Failed to deallocate %llu bytes with kernel error %llx.
Failed to close file descriptor for store writer: %i (%{public}s).
Keeping array packed for value replacement
_CSVisualizerTableFunctions
CSVisualizerMethods
_CSVisualizationArchiver
CSRemoteVisualization
_CSStore2DataContainer
_CSStore
NSSecureCoding
NSCoding
_CSVisualizerPredicate
_CSStoreAccessContext
CSStoreAttributedStringWriter
_CSVisualizer
NSCopying
```
