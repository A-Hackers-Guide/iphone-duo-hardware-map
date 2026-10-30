# `/usr/lib/libCoreEntitlements.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 135,632 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2400)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/usr/lib/libCoreEntitlements.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`

## Entitlements

```xml
  - no entitlements
```

## Strings (162)

```
CoreEntitlements: unknown DER type
index size overflow
This context's runtime does not support allocating
sub-sequence size is larger than sequence size
array decoding failure
der_vm_data_from_context
[%s]: subset validation failed, key not found in the superset '%.*s'\n
string_value_allowed_iterate
iterable decoding failure
Attempting to select a string value from a non-string DER object
CESerializeXML
&lt;
&apos;
key contains an embedded NUL
dictionary value verification failure
Unexpected type to match against during iteration
[%s]: %s\n
CoreEntitlements: Couldn't iterate over DER entitlements\n
invalid arguments passed in
This context's runtime does not support freeing
Invalid Arguments
Not eligible for acceleration
Unknown DER entitlements encoding
unhandled opcode
<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"https://www.apple.com/DTDs/PropertyList-1.0.dtd\"><plist version=\"1.0\">
runtime doesn't support acceleration
boolean should be exactly 1 byte
invalid dictionary element
der_vm_execute_string_prefix_value_allowed
B16@?0^{?={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}II^v}8
Failed during buffer decoding
Trying to release an unmanaged context
dictionary decoding failure
der_vm_execute_match_integer
</string>
invalid tag or length
der_vm_execute_select_index
der_vm_execute_match_string_prefix
iteration over a non-iterable type
der_vm_string_from_context
der_vm_container_from_context
CoreEntitlements: not a sequence
OK
API Misuse
numeric string element not allowed
der_decode_data
key-value pair contains extra elements
manufacturingCallback
unknown number encoding
Unexpected type to match against
string_prefix_allowed_iterate
der_vm_iterate_b
Not a CoreEntitlements error!
A memory allocation has failed
The passed in arguments are invalid
[%s]: subset validation failed, type mismatch for key '%.*s' %lu != %lu \n
UTC Time element not allowed
encountered invalid tag
could not decode tag for next DER sub-sequence
der_decode_entitlements
der_vm_execute_select_key
der_vm_execute_match_bool
CEReleaseManagedContext
critical failure during xml serialization, start != end
der_decode_number
unable to decode value size for key-value pair
Attempting to select an integer value from a non-integer DER object
Attempting to select a boolean value from a non-boolean DER object
&gt;
data element not allowed
could not decode size for next DER sub-sequence
der_decode_string
Unknown numeric string encoding
unable to decode value tag for key-value pair
der_vm_execute_string_value_allowed
[%s]: entitlements blob has unexpected version %lld\n
</integer>
&amp;
Unknown data encoding
der_vm_execute_match_string
[%s]: subset validation failed, integer value of key '%.*s' not allowed\n
CEDeserialization length mismatch
dictionary keys are not sorted or not unique
dictionary key is not a valid string
key length is invalid
noop
encountered invalid element in an iterable
CEIndexSizeForContext
[%s]: subset validation failed, key %.*s with value '%.*s' not allowed\n
der_decode_numeric_string
der_decode_utc_time
bool decode failure
der_vm_integer_from_context
CEValidateWithOptions
CEAcquireManagedContext
encountered invalid element in an array
der_vm_execute_select_longest_matching_key
der_vm_execute_nocopy
Attempting to select a data value from a non-data DER object
validate_V0
der_vm_buffer_from_context
[%s]: subset validation failed, bool value of key '%.*s' not allowed\n
extra data at the end of element
der_decode_next
der_decode_boolean
Unknown UTC Time encoding
validate_VNext
CEDeserialize_block_invoke
Query cannot be satisfied
recursivelyValidateEntitlements
der_vm_execute_integer_value_allowed
objectForActiveContext
entitlements blob does not have CCDER_ENTITLEMENTS_DICT as the second element
[%s]: subset validation failed, string array of key '%.*s' not allowed\n
number too large
fatal error when decoding key/value pair
Entitlements element not allowed
copy_keys_to_accelerator_block_invoke
%lld
Verification failed
dictionary key / value decoding failure
der_decode_key_value
v40@?0{CESerializedElement=q(?=q)QB}8
recursion limit reached
string decode failure
vector
CEBuildIndexForContext
xml-looking blob was passed in
entitlements blob does not have CCDER_CONSTRUCTED_SET coding
String contains an embedded NUL
Unknown string encoding
integer_allowed_iterate
entitlements blob does not have CCDER_ENTITLEMENTS coding
<integer>
valuesAreAllowed_block_invoke
&quot;
Unknown boolean encoding
der_validate_dictionary
der_vm_iterate_nocopy
der_validate_array
key / value decoding failure
der_vm_bool_from_context
setObject:forKey:
addObject:
dataWithLength:
arrayWithArray:
arrayWithCapacity:
countByEnumeratingWithState:objects:count:
length
lengthOfBytesUsingEncoding:
sortUsingSelector:
dictionaryWithCapacity:
longLongValue
numberWithLongLong:
allKeys
boolValue
bytes
initWithBytes:length:encoding:
UTF8String
compare:
initWithBytes:length:
objectForKeyedSubscript:
```
