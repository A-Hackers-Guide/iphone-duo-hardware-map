# `/usr/lib/libTLE.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 166,064 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 24 (Size: 3160)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/libTLE.dylib (compatibility version 1.0.0, current version 1.0.0)`
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

## Objective-C (3 classes, 0 protocols)

Classes: `LWCR`, `LWCRExecutor`, `LWCRFact`

## Strings (140)

```
$in
RefCounted object destroyed, but is not fully released
comp
LWCRs 'requirements' field is not a dictionary
Query Operation expected the Fact to be a CoreEntitlements dictionary
Bool op requires boolean parameter
Attempted to execute a non-iterable query
This LWCR is not compatible with this runtime
$and operator disallowed for active fact
Got an unexpected type (not a dictionary) when trying to generate dependent operations for evaluation.
Invalid fact type for this operation (expected data)
In Operation expected the Fact to be an integer, string or data
B16@?0^{?={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}II^v}8
Int op requires int parameter
reqs
{Fact=I{?=*Q}(?=q{?=*Q}^{CEQueryContext})}24@?0{?=*Q}8
Incorrect number of elements in operator Array tuple
Unexpected operator in Array tuple
$gte
Attempted resurection of an object
Attempted to execute unknown CoreEntitlements operation
vers
Got an unexpected type (not an integer, string or data) when trying to generate an In operation.
$query deserialization failed since it has an invalid query definition
Non array element found in operator Array
String op requires string parameter
This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.
LWCRs do not specify a constraint category or explicit requirements
The array of dependent operations is empty.
$lte
bounded_ptr<T>::operator+=(n): Calculating the number of bytes to add to the offset (n * sizeof(T)) would trigger an overflow
LWCRError
B24@?0{?=*Q}8
[%s]: %s\n
LWCRs constraint category cannot be less that zero
Unexpected type in Array tuple
$flag-check
$query
Invalid fact type for this operation (expected an integer or bool)
Invalid fact type for this operation (expected a string)
R
Constraint is too deeply nested. Failing to avoid recursion overflow
Unexpected key for parsing context
$and
v32@?0@\"NSString\"8@\"LWCRFact\"16^B24
loadFromCE
There should only be one operation to match a fact
Null query context
Unexpected type of an operation declaration.
The offset of the pointer inside its valid memory range can't be represented using int32_t
{FactDefinition=I{?=*Q}}24@?0{?=*Q}8
$lt
Got an unexpected type (not an integer) when trying to generate an integer operation.
ccat
Too many elements in dictionary
Fact not allowed in context
$optional
$and-array
The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range
bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally
$optional only supports a single dependent operation
$or
Got an unexpected type (not a dictionary) when trying to generate a query operation.
The dictionary of dependent operations is empty.
Unexpected type of an fact declaration.
bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.
Expected operator string in Array tuple
factless operator disallowed for active fact
$gt
Over-release of an object
LWCR: invalid version / compatible version fields
LWCRs are not encoded correctly
Got an unexpected type (not a sequence) when trying to read the array of matches.
$or operator disallowed for active fact
Array contains too many elements
$or-array
LWCR
LWCRFact
LWCRExecutor
errorWithDomain:code:userInfo:
lwcr
stringFactStorage
.cxx_destruct
fact
initWithBytes:length:encoding:
withData:withError:
hasRequirements
backingContext
dataFact:
externalRepresentation
stringFact:
.cxx_construct
bindName:
dictionaryWithObjects:forKeys:count:
integerFact:
backingStorage
bindName:withLength:
boolFact:
constraintCategory
enumerateKeysAndObjectsUsingBlock:
numberWithInt:
evaluateRequirements:withFacts:
TB,R
T@\"NSDictionary\",R
_dictionary
bytes
dictionary
dictionaryWithDictionary:
entitlementsFact:
dataFactStorage
Tq,R
init
length
longLongValue
numberWithLongLong:
setObject:forKeyedSubscript:
version
dealloc
UTF8String
executor
valueForKey:
withVersion:withConstraintCategory:withRequirements:withError:
copy
v16@0:8
@20@0:8B16
@32@0:8@16^@24
{LWCR=\"_version\"q\"_compatVersion\"q\"_constraintCat\"q\"ctx\"{CEQueryContext=\"der_context\"{der_vm_context=\"runtime\"^{CERuntime}\"lookup\"{CEAccelerationContext=\"index\"^{CEAccelerationElement}\"index_count\"Q}\"dictionary_tag\"Q\"so
v24@0:8@16
{Fact=\"type\"I\"name\"{?=\"data\"*\"length\"Q}\"value\"(?=\"integer\"q\"string\"{?=\"data\"*\"length\"Q}\"queryContext\"^{CEQueryContext})}
@\"NSString\"
@16@0:8
@\"NSData\"
@24@0:8@16
B32@0:8@16@24
q16@0:8
B16@0:8
^{CEQueryContext={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}B}
@\"NSDictionary\"
v32@0:8r*16Q24
@48@0:8q16q24@32^@40
```
