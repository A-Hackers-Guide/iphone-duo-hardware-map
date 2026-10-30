# `/usr/lib/libTLE.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 166,064 bytes.

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
@48@0:8q16q24@32^@40
@\"NSDictionary\"
@20@0:8B16
@32@0:8@16^@24
@16@0:8
@24@0:8@16
v32@0:8r*16Q24
q16@0:8
B16@0:8
@\"NSData\"
{LWCR=\"_version\"q\"_compatVersion\"q\"_constraintCat\"q\"ctx\"{CEQueryContext=\"der_context\"{der_vm_context=\"runtime\"^{CERuntime}\"lookup\"{CEAccelerationContext=\"index\"^{CEAccelerationElement}\"index_count\"Q}\"dictionary_tag\"Q\"so
v24@0:8@16
{Fact=\"type\"I\"name\"{?=\"data\"*\"length\"Q}\"value\"(?=\"integer\"q\"string\"{?=\"data\"*\"length\"Q}\"queryContext\"^{CEQueryContext})}
v16@0:8
^{CEQueryContext={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}B}
@\"NSString\"
B32@0:8@16@24
vers
Fact not allowed in context
$and
$optional
Expected operator string in Array tuple
Unexpected type of an fact declaration.
$query
B16@?0^{?={der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}{der_vm_context=^{CERuntime}{CEAccelerationContext=^{CEAccelerationElement}Q}QBB(?={ccder_read_blob=**}{?=**})}II^v}8
Bool op requires boolean parameter
The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range
bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.
{FactDefinition=I{?=*Q}}24@?0{?=*Q}8
ccat
Null query context
This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.
reqs
comp
Unexpected type of an operation declaration.
In Operation expected the Fact to be an integer, string or data
Got an unexpected type (not an integer, string or data) when trying to generate an In operation.
$gt
The offset of the pointer inside its valid memory range can't be represented using int32_t
$gte
Unexpected operator in Array tuple
Unexpected type in Array tuple
loadFromCE
$optional only supports a single dependent operation
There should only be one operation to match a fact
Got an unexpected type (not a dictionary) when trying to generate a query operation.
factless operator disallowed for active fact
Got an unexpected type (not an integer) when trying to generate an integer operation.
v32@?0@\"NSString\"8@\"LWCRFact\"16^B24
The dictionary of dependent operations is empty.
Unexpected key for parsing context
$lte
$flag-check
String op requires string parameter
R
LWCRs constraint category cannot be less that zero
$or
Non array element found in operator Array
Invalid fact type for this operation (expected an integer or bool)
Invalid fact type for this operation (expected data)
B24@?0{?=*Q}8
[%s]: %s\n
LWCR: invalid version / compatible version fields
LWCRs 'requirements' field is not a dictionary
LWCRs do not specify a constraint category or explicit requirements
$and operator disallowed for active fact
Got an unexpected type (not a dictionary) when trying to generate dependent operations for evaluation.
$in
$lt
Got an unexpected type (not a sequence) when trying to read the array of matches.
$or-array
Attempted to execute unknown CoreEntitlements operation
Attempted to execute a non-iterable query
LWCRs are not encoded correctly
This LWCR is not compatible with this runtime
Invalid fact type for this operation (expected a string)
Attempted resurection of an object
Int op requires int parameter
Incorrect number of elements in operator Array tuple
Too many elements in dictionary
$and-array
Array contains too many elements
$or operator disallowed for active fact
The array of dependent operations is empty.
RefCounted object destroyed, but is not fully released
Over-release of an object
bounded_ptr<T>::operator+=(n): Calculating the number of bytes to add to the offset (n * sizeof(T)) would trigger an overflow
{Fact=I{?=*Q}(?=q{?=*Q}^{CEQueryContext})}24@?0{?=*Q}8
$query deserialization failed since it has an invalid query definition
Constraint is too deeply nested. Failing to avoid recursion overflow
Query Operation expected the Fact to be a CoreEntitlements dictionary
bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally
LWCRError
LWCRExecutor
LWCR
LWCRFact
constraintCategory
executor
integerFact:
numberWithInt:
setObject:forKeyedSubscript:
.cxx_construct
dataFact:
lwcr
numberWithLongLong:
stringFactStorage
dataFactStorage
hasRequirements
initWithBytes:length:encoding:
dictionaryWithDictionary:
enumerateKeysAndObjectsUsingBlock:
errorWithDomain:code:userInfo:
externalRepresentation
init
dealloc
T@\"NSDictionary\",R
Tq,R
UTF8String
backingContext
bindName:
bytes
copy
TB,R
version
_dictionary
bindName:withLength:
boolFact:
dictionaryWithObjects:forKeys:count:
entitlementsFact:
fact
.cxx_destruct
length
longLongValue
stringFact:
evaluateRequirements:withFacts:
backingStorage
dictionary
valueForKey:
withData:withError:
withVersion:withConstraintCategory:withRequirements:withError:
```
