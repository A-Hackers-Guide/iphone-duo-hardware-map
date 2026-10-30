# `/usr/lib/libobjc.A.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 535,072 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 26 (Size: 4384)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/objc/libobjcMsgSend.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++abi.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libRosetta.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libobjc-env.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (5 classes, 1 protocols)

Classes: `NSObject`, `Object`, `Protocol`, `__IncompleteProtocol`, `__NSUnrecognizedTaggedPointer`

Protocols: `NSObject`

## Strings (570)

```
@16@0:8
^{objc_method_description=:*}24@0:8:16
Q16@0:8
Vv16@0:8
B16@0:8
@40@0:8:16@24@32
v16@0:8
#
r*16@0:8
#16@0:8
B24@0:8#16
v24@0:8:16
@24@0:8:16
^{_NSZone=}16@0:8
B24@0:8:16
^?24@0:8:16
v24@0:8@16
@24@0:8^{_NSZone=}16
B24@0:8@\"Protocol\"16
@\"NSString\"16@0:8
B24@0:8@16
@32@0:8:16@24
... %s\n%s
MallocStackLogging
OBJC_PRINT_REPLACED_METHODS
v28@?0^v8B16^B20
 (inherited)
PREOPTIMIZATION: IGNORING preoptimized categories in image %p %s
capriciously rearrange non-fragile ivars
__DATA_DIRTY
halt when autorelease pools are popped out of order, and allow heap debuggers to track autorelease pools
id2data fastcache is buggy
unexpected call into objc exception typeinfo vtable %d
RESOLVE: +[%s resolveInstanceMethod:%s] returned YES, but no new implementation of %c[%s %s] was found
disable coalescing of autorelease pool pointers
properties
IVARS: DEBUG: forcing ivars for class '%s' to slide (instanceStart %zu -> %zu)
fault
@synchronized(nil) is fatal
??
(cold)
CACHES: %sclass %s: dropping cache (from %s)
retainWeakReference
(full)
LOAD: +[%s load]\n
PREOPTIMIZATION: not attaching preoptimized category, class's %s list %p is still original.
warn about subclasses that may have been broken by subsequent changes to superclasses
warn about autorelease with no pool in place, which may be a leak
__OBJC
**** NXMapRemove: bug\n
INITIALIZE: thread %p: calling +[%s initialize]
CLASS: Adding unattached category (%s) %p for metaclass %s
OBJC_HELP: describe available environment variables
class_rx signing mismatch
INITIALIZE: %d/%d (%g%%) successful shared cache metaclass lookups
+[%s %s]: unrecognized selector sent to instance %p
*** maptable: count differs after rehashing; probably indicates a broken invariant: there are x and y such as isEqual(x, y) is TRUE but hash(x) != hash (y)\n
setInitialized
new
%s is fatal
log processing of method caches
disable safety checks for +initialize after fork
 (bundle)
CACHES: %sclass %s: dropping and disallowing preopt cache (from %s)
%s%s
tag index %u is invalid
_Tt%cs%zu%.*s%s
allocWithZone:
%s %zu bytes, buckets %zu bytes
objc[%d]: %s\n
Swift class %s with a metadata initializer is not allowed to be non-lazy
IMAGES: processing 1 newly-unmapped image...\n
Trampoline block %p, requested invalid index %lu
Invalid or prematurely-freed autorelease pool %p. Set a breakpoint on objc_autoreleasePoolInvalid to debug. 
[%p]  ################  POOL (placeholder)
id2data cache is buggy
__AUTH
couldn't dlsym %s
%s\n%s
on
LOAD: category '%s(%s)' unscheduled for +load
addMethods_finish
mutation detected during 'for(... in ...)'  enumeration of object %p.
disable tagged pointer optimization of NSNumber et al.
IMAGES: processing %u newly-mapped images...\n
IMAGES: loading image for %s%s%s%s\n
task_restartable_ranges_synchronize failed (result 0x%x: %s)
%s%s,
CLASS: found %d classes during launch
objc4
com.apple.obj-c
POOL HIGHWATER: extra sequential autoreleases of objects: %u
rootdev
unable to find caller's image
OBJC_PRINT_CXX_CTORS
stochastic-fault
%s: %s
invalid selector (null)
disable vtable dispatch
Invalid class pointer %p has bits set outside of ISA_MASK
Starting background scan of weak references.
log processing of class vtables
OBJC_DEBUG_UNLOAD
vm_remap trampolines failed (%d)
AUTORELEASE POOLS for thread %p
roots
Incorrect buffer calculation for property string. Partial string is %s, calculated length is %zu.
receiver
Cannot assign to small method %p from method %p
log use of future classes for toll-free bridging
B16@?0#8
%s: %s%s%s
  ...
autorelease
respondsToSelector:
MallocStackLoggingNoCompact
log exception handling
*** NXCreateHashTable: invalid style\n
IMAGES: performing initial category attach\n
print vtable images showing overridden methods
log classes with custom core methods
Superclass of %s at %p in %s is set to %p, indicating it is missing from an installed root
OBJC_PRINT_VTABLE_IMAGES
log preoptimization courtesy of dyld shared cache
isa '%s'
class `%s' not linked into application
disable obfuscation of tagged pointers
task_restartable_ranges_register failed (result 0x%x: %s)
IVARS:    offset %u -> %u for %s (size %u, align %u)
PREOPTIMIZATION: reading classes manually from %s because %s
PREOPTIMIZATION: using dyld selector opt
scribble the IMPs in freed method caches
+[%s initialize] may have been in progress in another thread when fork() was called.
OBJC_DISABLE_CLASS_RO_FAULTS
searching
protocol_addMethodDescription: protocol '%s' is not under construction!
Unable to allocate %zu bytes
Objective-C runtime debugging. Set variable=YES to enable.
warn when objc_sync_enter or objc_sync_exit return an error
Swift requested that class %p be ignored, but libobjc does not support that.
CUSTOM AWZ
_isDeallocating
log high-water marks for autorelease pools
attempt to allocate object of class '%s' failed
OS_object
Assertion failed: (%s) - empty list %p encountered during iteration
\"%s\"%s,
OBJC_DEBUG_POOL_ALLOCATION
Attempted to unregister unknown __weak variable at %p. This is probably incorrect use of objc_storeWeak() and objc_loadWeak().%s
method_exchangeImplementations
OBJC_DEBUG_DONT_CRASH
MISSING POOLS: (%p) Object %p of class %s autoreleased with no pool in place - just leaking - break on objc_autoreleaseNoPool() to debug
bad objc preopt version (want %d, got %d)
OBJC_DEBUG_DUPLICATE_CLASSES
vm_allocate trampolines failed (%d)
<stub class %p>
ObjC weak reference scanner
PREOPTIMIZATION: is ENABLED (version %d)
Memory corruption in class list.
RESOLVE: +[%s resolveClassMethod:%s] returned YES, but no new implementation of %c[%s %s] was found
OBJC_DEBUG_POOL_DEPTH=
log classes with custom retain/release methods
log classes with custom allocWithZone methods
arm64e
v12@?0I8
PREOPTIMIZATION: SCANNING categories in image %p %s - didInitialAttachCategories=%d hi->info()->dyldCategoriesOptimized()=%d hasRoot=%d
log image and library names as they are loaded
OBJC_PRINT_DEPRECATION_WARNINGS
thread is not initializing this class!
PREOPTIMIZATION: copying preoptimized category, class's %s list has already been copied.
disable preattached categories in the dyld shared cache
[%p]  ################  POOL %p
%s has un-signed class_ro_t pointers, but the main executable was compiled with class_ro_t pointer signing enabled
CACHES: %4d slots: %4d caches, %6zu bytes
CXX: calling C++ destructors for class %s
Cannot sort small method list %p
log fault when at least a set number of autorelease pages has been allocated
CLASS: methodizing class '%s' %s
(meta)
INITIALIZE: thread %p: class %s will be marked as fully +initialized after superclass +[%s initialize] completes
PREOPTIMIZATION: %u/%u (%.3g%%) method lists pre-sorted
the image may contain classes with missing weak superclasses
record more info about bad alt handler use
CLASS: Attaching category (%s) %p to metaclass %s
link error: class '%s' not found.
DYLD
Corrupt load image callback, unknown kind %u, func %p
attachCategories
self
OBJC_HELP=
dyld has %zu copies of msgSend, which requires more than %zu ranges
INITIALIZE: thread %p: skipping trivial +[%s initialize] in fork() child process
objc_registerClassPair: class '%s' was already registered!
OBJC_PRINT_ALT_HANDLERS
there are unresolved future classes pending
OBJC_DEBUG_SYNC_ERRORS
OBJC_DEBUG_SCAN_WEAK_TABLES
OBJC_DISABLE_PREOPTIMIZED_CACHES
-[NSObject methodSignatureForSelector:] not available without CoreFoundation
Lazily named class %p wasn't named by lazy name handler
*** Can't set weak ivar layout for already-registered class '%s'
meta
id
NSCF
CACHES: %sclass %s: disallow preopt cache (from %s)
OBJC_PRINT_RESOLVED_METHODS
__DATA
Invalid autorelease pools are a fatal error
task_threads failed (result 0x%x)\n
EXCEPTIONS: releasing completed exception %p (object %p, a %s)
INITIALIZE: %d/%d (%g%%) successful dyld closure metaclass lookups
no class for metaclass %p
OBJC_PRINT_CUSTOM_AWZ
OBJC_DEBUG_SCAN_WEAK_TABLES_INTERVAL_NANOSECONDS
objc_registerClassPair: class '%s' was not allocated with objc_allocateClassPair!
FUTURE: using %p instead of %p for %s
OBJC_DEBUG_MISSING_POOLS
OBJC_PRINT_OPTIONS is set
OBJC_PRINT_POOL_HIGHWATER
<null selector>
Class %s is implemented in both %s (%p) and %s (%p). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
CLASS: '%s'%s %p has missing weak superclass, disabling.
_TtC
OBJC_PRINT_EXCEPTION_THROW
/usr/lib/libobjc-trampolines.dylib
CUSTOM RR
CLASS: IGNORING category ???(%s) %p with missing weak-linked target class
by category 
**** NXMapInsert: bug\n
unused
objc[%d]: HALTED\n
EXCEPTIONS: handling exception %p at %p
thread is already initializing this class!
 (has class properties)
CACHES: new empty buckets at %p (capacity %zu)
EXCEPTIONS: skipping catch(?)
objc_disposeClassPair: class '%s' still has subclasses, including '%s'!
true
OBJC_DISABLE_AUTORELEASE_COALESCING
class_respondsToMethod
unable to find mach header for image
CLASS: found category %c%s(%s)
allowsWeakReference
OBJC_PRINT_OPTIONS=
PREOPTIMIZATION: %u/%u (%.3g%%) classes pre-registered
%.*s.%.*s
OBJC_PRINT_FUTURE_CLASSES
disable preoptimization courtesy of dyld shared cache
log calls to C++ ctors and dtors for instance variables
pthread_create failed with error %d (%s)
Lazily named class %p with no lazy name handler registered
Large Autorelease Pool
cache_t::insert() called with a preoptimized cache for %s
LOAD: class '%s' unscheduled for +load
_objc_blockTrampolineImpl
log processing of non-fragile ivars
OBJC_PRINT_VTABLE_SETUP
PREOPTIMIZATION: IGNORING preoptimized selectors in %s
warn about class_rx_t pointer signing mismatches
__weak variable at %p holds %p instead of %p. This is probably incorrect use of objc_storeWeak() and objc_loadWeak().%s
__CF
OBJC_DEBUG_NONFRAGILE_IVARS
objc_sync_exit(%p) returned error %d
Weak table scan detected a problem
CACHES:      total: %4zu caches, %6zu bytes
CLASS: eagerly realizing class '%s' in objc_readClassPair, overlap found with superclass '%s' - subclass start %u < superclass size %u
CLASS: IGNORING class '%s' with missing weak-linked superclass
##############
OBJC_DISABLE_PREATTACHED_CATEGORIES
class_ro_t enforcement disabled
warn about misuse of objc_storeWeak/objc_loadWeak
autorelease pool page %p corrupted\n  magic     0x%08x 0x%08x 0x%08x 0x%08x\n  should be 0x%08x 0x%08x 0x%08x 0x%08x\n  pthread   %p\n  should be %p\n
network-outbound
    %p
__objc_dupclass
INITIALIZE: thread %p: acquiring lock for +[%s initialize]
release
warn
log methods replaced by category implementations
OBJC_DISABLE_NONPOINTER_ISA
OBJC_DEBUG_CLASS_RX_SIGNING
protocols
(swift)
NSConstantString
isKindOfClass:
DYLD_INSERT_LIBRARIES
OBJC_DISABLE_TAGGED_POINTERS
Method cache corrupted. This may be a message to an invalid object, or a memory error somewhere else.
CUSTOM Core
OBJC_PRINT_CUSTOM_CORE
disable class_rx_t pointer signing enforcement
CLASS: patching class '%s' (%p) to point to body of %p
FUTURE: reserving %p for %s
_Tt%c%zu%.*s%zu%.*s%s
CACHES: %sclass %s: disallow sel-inlined preopt cache (from %s)
PROTOCOLS: protocol at %p is %s  (duplicate of %p)
%s is faulting
*** Can't set ivar layout for already-registered class '%s'
Swift
methods
objc-class_rw_t
OBJC_
OBJC_DEBUG_FRAGILE_SUPERCLASSES
selector '%s'
class
disable os faults for class_ro_t pointer signing mismatches
EXCEPTIONS: catch(%s)
class_lookupMethod
(pre-stable swift)
m != mEnd
yes
log methods created by +resolveClassMethod: and +resolveInstanceMethod:
log progress of class and category setup
 (meta)
OBJC_DEBUG_POOL_DEPTH
_
OBJC_PRINT_CLASS_SETUP
OBJC_DISABLE_PREOPTIMIZATION
.cxx_construct
objc_bp_assist_cfg_np returned %d for values %#llx, %#llx
Swift class is not allowed to be future
objc_disposeClassPair: class '%s' is a metaclass, not a class!
IVARS: sliding ivars for class %s (superclass was %u bytes, now %u)
This may cause crashes or incorrect msgSend dispatch. Continuing execution. This will become a fatal error when this app is rebuilt with a 27.0 SDK.
_TtP
warn about poorly-behaving bundles when unloaded
_objc_rootFinalize called with garbage collection off
INITIALIZE: thread %p: +[%s initialize] threw an exception
NIL SYNC DEBUG: @synchronized(nil); set a breakpoint on objc_sync_nil to debug
[%p]  %#16lx  %s  autorelease count %lu
log calls to class +initialize methods
**** NXMapRemove: incorrect table\n
EXCEPTIONS: throwing %p (object %p, a %s)
LOAD: class '%s' scheduled for +load
INITIALIZE: %d/%d (%g%%) successful secondary metaclass lookups
CLASS: attaching %d categories to%s class '%s'%s
_tryRetain
    category: (%s) %p
operator()
warn about calls to deprecated runtime functions
[%p]  %#16lx  %s
Invalid selref %p found at %p at offset %zu in %s loaded at %p
objc_disposeClassPair: class '%s' was not allocated with objc_allocateClassPair!
CLASS: realizing class '%s'%s %p %p #%u %s%s
halt
OBJC_PRINT_PROTOCOL_SETUP
EXCEPTIONS: skipping catch(%s)
_objc_blockTrampolineStart
disable non-pointer isa fields
[%p]  ................  PAGE %s %s %s
CXX: calling C++ constructors for class %s
entsize_list_tt overflow: count %u with entsize %u
Class of category %s at %p in %s is set to %p, indicating it is missing from an installed root
%c[%s %s]: unrecognized selector sent to instance %p (no message forward handler is installed)
OBJC_DEBUG_SCRIBBLE_CACHES
OBJC_DISABLE_INITIALIZE_FORK_SAFETY
Weak reference at %p contains %p, should contain %p
CACHES: COLLECTING %zu bytes (%zu allocations, %zu collections)
LOAD: category '%s(%s)' scheduled for +load
INITIALIZE: thread %p: setInitialized(%s)
__TEXT
<lazily named class %p>
stochasticFault
POOL HIGHWATER:     
CLASS: Copying preoptimized categories for sparsely loaded class '%s' %s - %u lists, %u loaded - loaded lists are:
id2data is buggy
__DATA_CONST
%s is set
libobjc static initializer found: %p %s at libobjc + %u
CACHES: not collecting; objc_msgSend in progress
PREOPTIMIZATION: is DISABLED %s
unwinding
objc_registerProtocol: protocol '%s' was not allocated with objc_allocateProtocol!
OBJC_PRINT_OPTIONS: list which options are set
disable coalescing of autorelease pool pointers using look back N strategy
Protocol
EXCEPTIONS: catch(id)
REPLACED: %c[%s %s]  %s%s  (IMP was %p (%s), now %p (%s))
OBJC_PRINT_INITIALIZE_METHODS
OBJC_DEBUG_ALT_HANDLERS
+[NSObject methodSignatureForSelector:] not available without CoreFoundation
objc_readClassPair for class %s changed %p to %p
NSSimpleCString
OBJC_PRINT_LOAD_METHODS
OBJC_PRINT_EXCEPTIONS
OBJC_PRINT_RAW_ISA
-[%s %s]: unrecognized selector sent to instance %p
*** NXCreateHashTable: bug\n
+[%s initialize] may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead. Set a breakpoint on objc_initializeAfterForkError to debug.
OBJC_PRINT_IMAGES
(by OBJC_DISABLE_PREOPTIMIZATION)
LOAD: +[%s(%s) load]\n
PREOPTIMIZATION: %zu selector references not pre-optimized
nil
objc_registerProtocol: protocol '%s' was already registered!
RESOLVE: method %c[%s %s] dynamically resolved to %p
preoptimizedCaches
scan the weak references table continuously in the background - set OBJC_DEBUG_SCAN_WEAK_TABLES_INTERVAL_NANOSECONDS to set scanning interval (default 1000000)
[%p]  ................  PAGE (placeholder)
\",
EXCEPTIONS: %s through frame [ip=%p sp=%p] for exception %p
FUTURE: found %p already in use for %s
Can't complete future class request for '%s' because the real class is too big.
OBJC_DEBUG_WEAK_ERRORS
(hot)
PREOPTIMIZATION: honoring preoptimized selectors in %s
fatal
 Break on objc_weak_error to debug.
entsize_list_tt overflow: index %u in list %p with entsize %u
INITIALIZE: %d/%d (%g%%) successful by-name metaclass lookups
CLASS: realizing class '%s'%s (duplicate of %s%s) %p %p
classRoSigningFaults
OBJC_DISABLE_CLASSRX_SIGNING_ENFORCEMENT
IMAGES: unloading image for %s%s\n
Cannot form weak reference to instance (%p) of class %s. It is possible that this object was over-released, or is in the process of deallocation.
EXCEPTIONS: terminating
INITIALIZE: thread %p: finished +[%s initialize]
LOAD: %d categories still waiting for +load\n
CLASS: Attaching category (%s) %p to class %s
CLASS: calling Swift metadata initializer for class '%s' (%p)
warn when multiple classes with the same name are present
bad weak table at %p. This may be a runtime bug or a memory error somewhere else.
protocol_addProtocol: added protocol '%s' is still under construction!
PREOPTIMIZATION: copying preoptimized %s list %p
NSZombiesEnabled
%s is stochastically faulting
+[NSObject instanceMethodSignatureForSelector:] not available without CoreFoundation
_method_setImplementation
retain
OBJC_HELP is set
log calls to class and category +load methods
Weak reference loaded from %p contains %p which is not in the weak references table
rd
OBJC_PRINT_CUSTOM_RR
OBJC_DEBUG_NIL_SYNC
.cxx_destruct
halt the process by exiting instead of crashing
The function %s is obsolete. Do not use it. Set a breakpoint on _objc_warn_deprecated to find the culprit.
_objc_flush_caches
<null>
syncCache corrupted, allocated=%u used=%u
protocol_addProperty: protocol '%s' is not under construction!
*** NXMapInsert: invalid key: -1\n
PROTOCOLS: Skipping reading protocols in image: %s
libobjc is not in the shared cache
*** NXCreateMapTable: invalid creation parameters\n
EXCEPTIONS: rethrowing current exception
PROTOCOLS: protocol at %p is %s
y
Missing pools are a fatal error
%s %p, SEL %p, isa %p, cache %p, buckets and mask 0x%lx, occupied 0x%x
Category %s on Swift class %s has +load method. Swift class extensions and categories on Swift classes are not allowed to have +load methods.
OBJC_DISABLE_VTABLES
OBJC_DISABLE_FAULTS
 (preoptimized)
Proceeding anyway.  Memory errors are likely.
PREOPTIMIZATION: %zu protocol references not pre-optimized
RAW ISA:  %s%s%s
disable preoptimized caches
Object: SubtypeUntil: end of type encountered prematurely\n
*** hashtable: count differs after rehashing; probably indicates a broken invariant: there are x and y such as isEqual(x, y) is TRUE but hash(x) != hash (y)\n
tag index %u used for two different classes (was %p %s, now %p %s)
Cycle in class list:
alloc
/private/var/run/syslog
OBJC_PRINT_PREOPTIMIZATION
log processing of exception alt handlers
OBJC_DISABLE_TAG_OBFUSCATION
objc_setAssociatedObject called on instance (%p) of class %s which does not allow associated objects
(dyld shared cache is absent or out of date)
,
INITIALIZE: thread %p: refusing to call +[%s initialize] in fork() child process because it may have been in progress when fork() was called
_TtCs12_SwiftObject
OBJC_PRINT_IVAR_SETUP
log classes that require raw pointer isa fields
couldn't dlopen libobjc-trampolines.dylib: %s
tagged pointers are disabled
AUTORELEASE!
Hash table corrupted. This is probably a memory error somewhere. (table at %p, buckets at %p (%zu bytes), %u buckets, %u entries, %u tombstones, data %p %p %p %p)
CLASS: Adding unattached category (%s) %p for class %s
setSuperclass
retainCount
log progress of protocol setup
%llu releases pending.
EXCEPTIONS: finishing handler
  %p %s%s
libgmalloc
IMAGES: calling +load methods in %s\n
addSubclass
OBJC_PRINT_CACHE_SETUP
POOL HIGHWATER: new high water mark of %u pending releases for thread %p:
INITIALIZE: thread %p: %s is fully +initialized
 existing
Malloc
disable os faults
OBJC_DISABLE_AUTORELEASE_COALESCING_LRU
protocol_addProtocol: modified protocol '%s' is not under construction!
classRxSigning
log backtrace of every objc_exception_throw()
warn about @synchronized(nil), which does no synchronization
PREOPTIMIZATION: honoring preoptimized header info at %p for %s
error: libobjc release build forbids static initializers, found %zu.
__NSUnrecognizedTaggedPointer
NSObject
Object
__IncompleteProtocol
Protocol
hash
mutableCopy
self
_objc_initiateDealloc
T#,R
finalize
forwardInvocation:
instancesRespondToSelector:
_setWeaklyReferenced
initialize
isEqual:
load
zone
isa
resolveInstanceMethod:
retain
allocWithZone:
debugDescription
instanceMethodSignatureForSelector:
performSelector:withObject:
T@\"NSString\",?,R,C
allowsWeakReference
copy
methodSignatureForSelector:
T@\"NSString\",R,C
description
retainCount
🤯
dealloc
isMemberOfClass:
performSelector:withObject:withObject:
descriptionForClassMethod:
new
_tryRetain
doesNotRecognizeSelector:
instanceMethodForSelector:
retainWeakReference
selector
conformsTo:
isSubclassOfClass:
_isDeallocating
_noteAssociatedObjects
copyWithZone:
methodForSelector:
respondsToSelector:
TQ,R
release
alloc
resolveClassMethod:
mutableCopyWithZone:
isFault
class
conformsToProtocol:
forwardingTargetForSelector:
init
isKindOfClass:
descriptionForInstanceMethod:
isAncestorOfObject:
name
performSelector:
superclass
isProxy
autorelease
```
