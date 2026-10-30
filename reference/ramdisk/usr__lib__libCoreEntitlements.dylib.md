# `/usr/lib/libCoreEntitlements.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 135,632 bytes.

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
validate_V0
der_decode_data
der_vm_execute_match_string
entitlements blob does not have CCDER_ENTITLEMENTS coding
entitlements blob does not have CCDER_CONSTRUCTED_SET coding
String contains an embedded NUL
boolean should be exactly 1 byte
unable to decode value tag for key-value pair
dictionary decoding failure
der_vm_execute_string_prefix_value_allowed
string_prefix_allowed_iterate
runtime doesn't support acceleration
dictionary key is not a valid string
encountered invalid element in an array
der_vm_execute_select_key
der_vm_iterate_b
der_vm_integer_from_context
der_vm_data_from_context
der_vm_container_from_context
recursivelyValidateEntitlements
bool decode failure
Unexpected type to match against
CoreEntitlements: not a sequence
[%s]: subset validation failed, string array of key '%.*s' not allowed\n
&amp;
&lt;
numeric string element not allowed
extra data at the end of element
Attempting to select a string value from a non-string DER object
CEAcquireManagedContext
[%s]: subset validation failed, type mismatch for key '%.*s' %lu != %lu \n
der_decode_numeric_string
&quot;
key contains an embedded NUL
&gt;
invalid tag or length
der_vm_bool_from_context
manufacturingCallback
key / value decoding failure
key-value pair contains extra elements
der_vm_execute_select_index
API Misuse
recursion limit reached
dictionary keys are not sorted or not unique
could not decode size for next DER sub-sequence
der_decode_string
der_vm_buffer_from_context
[%s]: %s\n
key length is invalid
invalid dictionary element
der_vm_execute_match_string_prefix
iteration over a non-iterable type
fatal error when decoding key/value pair
invalid arguments passed in
Not a CoreEntitlements error!
Invalid Arguments
&apos;
der_vm_string_from_context
CoreEntitlements: Couldn't iterate over DER entitlements\n
critical failure during xml serialization, start != end
Unknown string encoding
A memory allocation has failed
index size overflow
xml-looking blob was passed in
This context's runtime does not support allocating
<integer>
valuesAreAllowed_block_invoke
[%s]: subset validation failed, key %.*s with value '%.*s' not allowed\n
CEDeserialization length mismatch
iterable decoding failure
Attempting to select an integer value from a non-integer DER object
CEBuildIndexForContext
validate_VNext
entitlements blob does not have CCDER_ENTITLEMENTS_DICT as the second element
Unknown DER entitlements encoding
array decoding failure
der_vm_execute_match_bool
unhandled opcode
CoreEntitlements: unknown DER type
CEReleaseManagedContext
could not decode tag for next DER sub-sequence
Unknown data encoding
Attempting to select a boolean value from a non-boolean DER object
[%s]: entitlements blob has unexpected version %lld\n
v40@?0{CESerializedElement=q(?=q)QB}8
der_vm_execute_match_integer
der_decode_boolean
<?xml version=\"1.0\" encoding=\"UTF-8\"?><!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"https://www.apple.com/DTDs/PropertyList-1.0.dtd\"><plist version=\"1.0\">
Not eligible for acceleration
UTC Time element not allowed
der_validate_dictionary
vector
OK
der_vm_execute_nocopy
B16@?0^{?={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}II^v}8
</integer>
[%s]: subset validation failed, bool value of key '%.*s' not allowed\n
sub-sequence size is larger than sequence size
der_decode_entitlements
der_vm_iterate_nocopy
Trying to release an unmanaged context
CEDeserialize_block_invoke
Failed during buffer decoding
der_decode_utc_time
string decode failure
[%s]: subset validation failed, key not found in the superset '%.*s'\n
CEIndexSizeForContext
der_decode_number
The passed in arguments are invalid
Query cannot be satisfied
der_decode_next
Unknown numeric string encoding
der_vm_execute_select_longest_matching_key
Verification failed
%lld
unable to decode value size for key-value pair
integer_allowed_iterate
noop
CESerializeXML
[%s]: subset validation failed, integer value of key '%.*s' not allowed\n
Entitlements element not allowed
Unknown boolean encoding
Unexpected type to match against during iteration
CEValidateWithOptions
This context's runtime does not support freeing
</string>
data element not allowed
number too large
der_decode_key_value
string_value_allowed_iterate
Attempting to select a data value from a non-data DER object
copy_keys_to_accelerator_block_invoke
der_validate_array
Unknown UTC Time encoding
der_vm_execute_string_value_allowed
encountered invalid element in an iterable
objectForActiveContext
encountered invalid tag
dictionary key / value decoding failure
dictionary value verification failure
unknown number encoding
der_vm_execute_integer_value_allowed
addObject:
initWithBytes:length:encoding:
longLongValue
numberWithLongLong:
objectForKeyedSubscript:
allKeys
dataWithLength:
bytes
compare:
countByEnumeratingWithState:objects:count:
dictionaryWithCapacity:
initWithBytes:length:
lengthOfBytesUsingEncoding:
arrayWithArray:
arrayWithCapacity:
boolValue
sortUsingSelector:
UTF8String
length
setObject:forKey:
```
