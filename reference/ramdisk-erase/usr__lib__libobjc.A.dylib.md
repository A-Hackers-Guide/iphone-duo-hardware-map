# `/usr/lib/libobjc.A.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 535,072 bytes.

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
respondsToSelector:
log backtrace of every objc_exception_throw()
<null>
unable to find caller's image
PREOPTIMIZATION: IGNORING preoptimized categories in image %p %s
NIL SYNC DEBUG: @synchronized(nil); set a breakpoint on objc_sync_nil to debug
POOL HIGHWATER:     
ObjC weak reference scanner
class_lookupMethod
network-outbound
 (inherited)
CLASS: attaching %d categories to%s class '%s'%s
y
disable coalescing of autorelease pool pointers
class_respondsToMethod
(full)
thread is already initializing this class!
_objc_blockTrampolineImpl
Weak reference at %p contains %p, should contain %p
(by OBJC_DISABLE_PREOPTIMIZATION)
objc_registerProtocol: protocol '%s' was not allocated with objc_allocateProtocol!
log processing of method caches
disable safety checks for +initialize after fork
OBJC_DISABLE_CLASS_RO_FAULTS
__TEXT
protocol_addMethodDescription: protocol '%s' is not under construction!
LOAD: class '%s' unscheduled for +load
%s: %s%s%s
CLASS: Attaching category (%s) %p to metaclass %s
warn about poorly-behaving bundles when unloaded
OBJC_DISABLE_VTABLES
%s\n%s
OBJC_PRINT_EXCEPTION_THROW
 (preoptimized)
EXCEPTIONS: catch(id)
+[%s initialize] may have been in progress in another thread when fork() was called.
This may cause crashes or incorrect msgSend dispatch. Continuing execution. This will become a fatal error when this app is rebuilt with a 27.0 SDK.
PREOPTIMIZATION: not attaching preoptimized category, class's %s list %p is still original.
yes
on
OBJC_PRINT_ALT_HANDLERS
OBJC_PRINT_RAW_ISA
*** NXCreateHashTable: bug\n
Attempted to unregister unknown __weak variable at %p. This is probably incorrect use of objc_storeWeak() and objc_loadWeak().%s
objc_readClassPair for class %s changed %p to %p
CLASS: eagerly realizing class '%s' in objc_readClassPair, overlap found with superclass '%s' - subclass start %u < superclass size %u
warn about calls to deprecated runtime functions
selector '%s'
<lazily named class %p>
CLASS: Adding unattached category (%s) %p for class %s
RESOLVE: +[%s resolveClassMethod:%s] returned YES, but no new implementation of %c[%s %s] was found
warn about misuse of objc_storeWeak/objc_loadWeak
id2data fastcache is buggy
INITIALIZE: thread %p: skipping trivial +[%s initialize] in fork() child process
Invalid selref %p found at %p at offset %zu in %s loaded at %p
OBJC_PRINT_REPLACED_METHODS
 (has class properties)
/private/var/run/syslog
PREOPTIMIZATION: SCANNING categories in image %p %s - didInitialAttachCategories=%d hi->info()->dyldCategoriesOptimized()=%d hasRoot=%d
OS_object
preoptimizedCaches
log image and library names as they are loaded
PREOPTIMIZATION: %u/%u (%.3g%%) classes pre-registered
Cannot assign to small method %p from method %p
(pre-stable swift)
OBJC_PRINT_EXCEPTIONS
[%p]  %#16lx  %s  autorelease count %lu
task_restartable_ranges_register failed (result 0x%x: %s)
<stub class %p>
operator()
FUTURE: reserving %p for %s
class
retain
class `%s' not linked into application
OBJC_DEBUG_NONFRAGILE_IVARS
*** NXCreateHashTable: invalid style\n
LOAD: +[%s(%s) load]\n
CLASS: methodizing class '%s' %s
new
OBJC_PRINT_OPTIONS=
%s is fatal
log classes with custom core methods
vm_remap trampolines failed (%d)
CACHES: %sclass %s: disallow sel-inlined preopt cache (from %s)
disable obfuscation of tagged pointers
??
**** NXMapRemove: bug\n
OBJC_DISABLE_PREOPTIMIZATION
OBJC_DISABLE_PREATTACHED_CATEGORIES
searching
*** Can't set weak ivar layout for already-registered class '%s'
__OBJC
Assertion failed: (%s) - empty list %p encountered during iteration
stochastic-fault
log methods replaced by category implementations
CACHES: %4d slots: %4d caches, %6zu bytes
IVARS: sliding ivars for class %s (superclass was %u bytes, now %u)
    category: (%s) %p
Swift
OBJC_PRINT_IMAGES
class_rx signing mismatch
entsize_list_tt overflow: index %u in list %p with entsize %u
OBJC_DISABLE_INITIALIZE_FORK_SAFETY
objc_setAssociatedObject called on instance (%p) of class %s which does not allow associated objects
method_exchangeImplementations
Memory corruption in class list.
NSSimpleCString
CLASS: IGNORING category ???(%s) %p with missing weak-linked target class
classRoSigningFaults
IMAGES: loading image for %s%s%s%s\n
attempt to allocate object of class '%s' failed
(hot)
log progress of protocol setup
__weak variable at %p holds %p instead of %p. This is probably incorrect use of objc_storeWeak() and objc_loadWeak().%s
(meta)
PREOPTIMIZATION: reading classes manually from %s because %s
OBJC_PRINT_PREOPTIMIZATION
##############
LOAD: class '%s' scheduled for +load
halt the process by exiting instead of crashing
v28@?0^v8B16^B20
... %s\n%s
rd
the image may contain classes with missing weak superclasses
 (bundle)
Missing pools are a fatal error
OBJC_PRINT_PROTOCOL_SETUP
objc[%d]: HALTED\n
%s is set
%c[%s %s]: unrecognized selector sent to instance %p (no message forward handler is installed)
CACHES: %sclass %s: dropping cache (from %s)
NSConstantString
IVARS: DEBUG: forcing ivars for class '%s' to slide (instanceStart %zu -> %zu)
OBJC_PRINT_VTABLE_IMAGES
POOL HIGHWATER: extra sequential autoreleases of objects: %u
OBJC_DEBUG_FRAGILE_SUPERCLASSES
OBJC_DEBUG_ALT_HANDLERS
OBJC_DEBUG_MISSING_POOLS
_objc_flush_caches
CUSTOM Core
 existing
vm_allocate trampolines failed (%d)
%llu releases pending.
[%p]  ................  PAGE (placeholder)
[%p]  ################  POOL (placeholder)
EXCEPTIONS: finishing handler
EXCEPTIONS: skipping catch(%s)
Lazily named class %p with no lazy name handler registered
FUTURE: using %p instead of %p for %s
RESOLVE: +[%s resolveInstanceMethod:%s] returned YES, but no new implementation of %c[%s %s] was found
release
%s is stochastically faulting
OBJC_PRINT_CUSTOM_AWZ
objc_registerClassPair: class '%s' was already registered!
Class of category %s at %p in %s is set to %p, indicating it is missing from an installed root
_
self
OBJC_DEBUG_NIL_SYNC
Cannot sort small method list %p
CACHES: %sclass %s: disallow preopt cache (from %s)
OBJC_PRINT_CACHE_SETUP
log use of future classes for toll-free bridging
[%p]  ................  PAGE %s %s %s
Weak table scan detected a problem
fatal
PREOPTIMIZATION: honoring preoptimized selectors in %s
protocol_addProtocol: modified protocol '%s' is not under construction!
attachCategories
_TtC
autorelease pool page %p corrupted\n  magic     0x%08x 0x%08x 0x%08x 0x%08x\n  should be 0x%08x 0x%08x 0x%08x 0x%08x\n  pthread   %p\n  should be %p\n
receiver
isa '%s'
CXX: calling C++ destructors for class %s
CLASS: found category %c%s(%s)
log calls to class and category +load methods
AUTORELEASE POOLS for thread %p
Class %s is implemented in both %s (%p) and %s (%p). This may cause spurious casting failures and mysterious crashes. One of the duplicates must be removed or renamed.
OBJC_DEBUG_SCAN_WEAK_TABLES
Starting background scan of weak references.
objc-class_rw_t
CLASS: IGNORING class '%s' with missing weak-linked superclass
Can't complete future class request for '%s' because the real class is too big.
OBJC_DISABLE_PREOPTIMIZED_CACHES
INITIALIZE: %d/%d (%g%%) successful by-name metaclass lookups
fault
OBJC_PRINT_RESOLVED_METHODS
CACHES: COLLECTING %zu bytes (%zu allocations, %zu collections)
*** Can't set ivar layout for already-registered class '%s'
disable preoptimization courtesy of dyld shared cache
Large Autorelease Pool
OBJC_DISABLE_CLASSRX_SIGNING_ENFORCEMENT
<null selector>
PREOPTIMIZATION: honoring preoptimized header info at %p for %s
NSCF
com.apple.obj-c
by category 
log classes with custom retain/release methods
Invalid class pointer %p has bits set outside of ISA_MASK
CLASS: Attaching category (%s) %p to class %s
halt when autorelease pools are popped out of order, and allow heap debuggers to track autorelease pools
warn about class_rx_t pointer signing mismatches
\",
protocol_addProtocol: added protocol '%s' is still under construction!
Lazily named class %p wasn't named by lazy name handler
%s: %s
unable to find mach header for image
OBJC_DISABLE_TAGGED_POINTERS
-[NSObject methodSignatureForSelector:] not available without CoreFoundation
objc_disposeClassPair: class '%s' still has subclasses, including '%s'!
IVARS:    offset %u -> %u for %s (size %u, align %u)
id2data is buggy
%s%s
nil
OBJC_DISABLE_AUTORELEASE_COALESCING_LRU
OBJC_DEBUG_CLASS_RX_SIGNING
Swift class %s with a metadata initializer is not allowed to be non-lazy
no class for metaclass %p
objc[%d]: %s\n
properties
retainWeakReference
OBJC_PRINT_IVAR_SETUP
task_restartable_ranges_synchronize failed (result 0x%x: %s)
allowsWeakReference
**** NXMapRemove: incorrect table\n
objc_registerProtocol: protocol '%s' was already registered!
INITIALIZE: %d/%d (%g%%) successful shared cache metaclass lookups
_isDeallocating
log methods created by +resolveClassMethod: and +resolveInstanceMethod:
OBJC_PRINT_CXX_CTORS
cache_t::insert() called with a preoptimized cache for %s
task_threads failed (result 0x%x)\n
    %p
m != mEnd
Cannot form weak reference to instance (%p) of class %s. It is possible that this object was over-released, or is in the process of deallocation.
LOAD: category '%s(%s)' scheduled for +load
_TtP
CACHES: %sclass %s: dropping and disallowing preopt cache (from %s)
INITIALIZE: %d/%d (%g%%) successful dyld closure metaclass lookups
Malloc
CACHES: new empty buckets at %p (capacity %zu)
OBJC_PRINT_FUTURE_CLASSES
setInitialized
EXCEPTIONS: throwing %p (object %p, a %s)
INITIALIZE: thread %p: class %s will be marked as fully +initialized after superclass +[%s initialize] completes
%.*s.%.*s
OBJC_HELP is set
warn when multiple classes with the same name are present
disable os faults for class_ro_t pointer signing mismatches
syncCache corrupted, allocated=%u used=%u
Method cache corrupted. This may be a message to an invalid object, or a memory error somewhere else.
tag index %u is invalid
classRxSigning
OBJC_DISABLE_FAULTS
Corrupt load image callback, unknown kind %u, func %p
Protocol
rootdev
alloc
%s%s,
IMAGES: processing %u newly-mapped images...\n
IMAGES: calling +load methods in %s\n
id
*** hashtable: count differs after rehashing; probably indicates a broken invariant: there are x and y such as isEqual(x, y) is TRUE but hash(x) != hash (y)\n
PREOPTIMIZATION: copying preoptimized %s list %p
OBJC_DEBUG_DUPLICATE_CLASSES
EXCEPTIONS: terminating
addSubclass
CLASS: Copying preoptimized categories for sparsely loaded class '%s' %s - %u lists, %u loaded - loaded lists are:
NSZombiesEnabled
Swift class is not allowed to be future
__objc_dupclass
INITIALIZE: thread %p: +[%s initialize] threw an exception
capriciously rearrange non-fragile ivars
disable class_rx_t pointer signing enforcement
_Tt%cs%zu%.*s%s
@synchronized(nil) is fatal
__DATA_CONST
libobjc static initializer found: %p %s at libobjc + %u
OBJC_DEBUG_SCAN_WEAK_TABLES_INTERVAL_NANOSECONDS
IMAGES: performing initial category attach\n
IMAGES: processing 1 newly-unmapped image...\n
EXCEPTIONS: skipping catch(?)
  %p %s%s
objc4
bad weak table at %p. This may be a runtime bug or a memory error somewhere else.
Proceeding anyway.  Memory errors are likely.
*** NXMapInsert: invalid key: -1\n
CLASS: found %d classes during launch
objc_registerClassPair: class '%s' was not allocated with objc_allocateClassPair!
(swift)
OBJC_DEBUG_POOL_DEPTH=
OBJC_PRINT_CUSTOM_CORE
PREOPTIMIZATION: %u/%u (%.3g%%) method lists pre-sorted
PROTOCOLS: protocol at %p is %s
disable tagged pointer optimization of NSNumber et al.
objc_bp_assist_cfg_np returned %d for values %#llx, %#llx
**** NXMapInsert: bug\n
invalid selector (null)
The function %s is obsolete. Do not use it. Set a breakpoint on _objc_warn_deprecated to find the culprit.
CLASS: Adding unattached category (%s) %p for metaclass %s
true
print vtable images showing overridden methods
setSuperclass
halt
log processing of non-fragile ivars
tagged pointers are disabled
Cycle in class list:
+[%s %s]: unrecognized selector sent to instance %p
-[%s %s]: unrecognized selector sent to instance %p
LOAD: category '%s(%s)' unscheduled for +load
OBJC_DEBUG_POOL_DEPTH
OBJC_DEBUG_SCRIBBLE_CACHES
pthread_create failed with error %d (%s)
Swift requested that class %p be ignored, but libobjc does not support that.
OBJC_DEBUG_DONT_CRASH
id2data cache is buggy
__AUTH
thread is not initializing this class!
FUTURE: found %p already in use for %s
B16@?0#8
CUSTOM AWZ
log calls to class +initialize methods
Incorrect buffer calculation for property string. Partial string is %s, calculated length is %zu.
INITIALIZE: thread %p: %s is fully +initialized
there are unresolved future classes pending
disable preattached categories in the dyld shared cache
_objc_rootFinalize called with garbage collection off
Invalid or prematurely-freed autorelease pool %p. Set a breakpoint on objc_autoreleasePoolInvalid to debug. 
_method_setImplementation
v12@?0I8
OBJC_DEBUG_SYNC_ERRORS
addMethods_finish
log processing of exception alt handlers
Trampoline block %p, requested invalid index %lu
EXCEPTIONS: rethrowing current exception
scribble the IMPs in freed method caches
OBJC_DEBUG_WEAK_ERRORS
/usr/lib/libobjc-trampolines.dylib
autorelease
DYLD_INSERT_LIBRARIES
libobjc is not in the shared cache
unused
RAW ISA:  %s%s%s
Superclass of %s at %p in %s is set to %p, indicating it is missing from an installed root
log processing of class vtables
.cxx_construct
 Break on objc_weak_error to debug.
%s %p, SEL %p, isa %p, cache %p, buckets and mask 0x%lx, occupied 0x%x
couldn't dlsym %s
(cold)
  ...
retainCount
OBJC_PRINT_POOL_HIGHWATER
protocol_addProperty: protocol '%s' is not under construction!
log exception handling
AUTORELEASE!
OBJC_PRINT_DEPRECATION_WARNINGS
+[NSObject methodSignatureForSelector:] not available without CoreFoundation
RESOLVE: method %c[%s %s] dynamically resolved to %p
disable coalescing of autorelease pool pointers using look back N strategy
%s has un-signed class_ro_t pointers, but the main executable was compiled with class_ro_t pointer signing enabled
POOL HIGHWATER: new high water mark of %u pending releases for thread %p:
EXCEPTIONS: catch(%s)
INITIALIZE: thread %p: calling +[%s initialize]
methods
OBJC_DEBUG_POOL_ALLOCATION
warn about @synchronized(nil), which does no synchronization
Object: SubtypeUntil: end of type encountered prematurely\n
LOAD: +[%s load]\n
Invalid autorelease pools are a fatal error
CACHES: not collecting; objc_msgSend in progress
EXCEPTIONS: releasing completed exception %p (object %p, a %s)
OBJC_PRINT_CUSTOM_RR
.cxx_destruct
roots
CXX: calling C++ constructors for class %s
 (meta)
OBJC_
log high-water marks for autorelease pools
_Tt%c%zu%.*s%zu%.*s%s
dyld has %zu copies of msgSend, which requires more than %zu ranges
EXCEPTIONS: %s through frame [ip=%p sp=%p] for exception %p
scan the weak references table continuously in the background - set OBJC_DEBUG_SCAN_WEAK_TABLES_INTERVAL_NANOSECONDS to set scanning interval (default 1000000)
__DATA
CLASS: calling Swift metadata initializer for class '%s' (%p)
PREOPTIMIZATION: copying preoptimized category, class's %s list has already been copied.
OBJC_HELP: describe available environment variables
[%p]  ################  POOL %p
Hash table corrupted. This is probably a memory error somewhere. (table at %p, buckets at %p (%zu bytes), %u buckets, %u entries, %u tombstones, data %p %p %p %p)
PREOPTIMIZATION: is DISABLED %s
PREOPTIMIZATION: %zu selector references not pre-optimized
objc_disposeClassPair: class '%s' was not allocated with objc_allocateClassPair!
log calls to C++ ctors and dtors for instance variables
disable vtable dispatch
OBJC_DISABLE_AUTORELEASE_COALESCING
meta
bad objc preopt version (want %d, got %d)
*** NXCreateMapTable: invalid creation parameters\n
protocols
tag index %u used for two different classes (was %p %s, now %p %s)
CLASS: realizing class '%s'%s %p %p #%u %s%s
CLASS: realizing class '%s'%s (duplicate of %s%s) %p %p
allocWithZone:
record more info about bad alt handler use
PROTOCOLS: Skipping reading protocols in image: %s
OBJC_DISABLE_NONPOINTER_ISA
error: libobjc release build forbids static initializers, found %zu.
unwinding
PREOPTIMIZATION: using dyld selector opt
Unable to allocate %zu bytes
stochasticFault
OBJC_PRINT_OPTIONS: list which options are set
MISSING POOLS: (%p) Object %p of class %s autoreleased with no pool in place - just leaking - break on objc_autoreleaseNoPool() to debug
(dyld shared cache is absent or out of date)
disable os faults
objc_disposeClassPair: class '%s' is a metaclass, not a class!
entsize_list_tt overflow: count %u with entsize %u
_tryRetain
MallocStackLogging
CACHES:      total: %4zu caches, %6zu bytes
INITIALIZE: thread %p: acquiring lock for +[%s initialize]
%s is faulting
REPLACED: %c[%s %s]  %s%s  (IMP was %p (%s), now %p (%s))
disable preoptimized caches
INITIALIZE: thread %p: finished +[%s initialize]
libgmalloc
OBJC_PRINT_LOAD_METHODS
OBJC_PRINT_VTABLE_SETUP
log preoptimization courtesy of dyld shared cache
log progress of class and category setup
disable non-pointer isa fields
+[NSObject instanceMethodSignatureForSelector:] not available without CoreFoundation
EXCEPTIONS: handling exception %p at %p
isKindOfClass:
DYLD
Objective-C runtime debugging. Set variable=YES to enable.
log classes that require raw pointer isa fields
Category %s on Swift class %s has +load method. Swift class extensions and categories on Swift classes are not allowed to have +load methods.
unexpected call into objc exception typeinfo vtable %d
OBJC_PRINT_INITIALIZE_METHODS
warn about subclasses that may have been broken by subsequent changes to superclasses
CLASS: patching class '%s' (%p) to point to body of %p
_objc_blockTrampolineStart
PREOPTIMIZATION: %zu protocol references not pre-optimized
*** maptable: count differs after rehashing; probably indicates a broken invariant: there are x and y such as isEqual(x, y) is TRUE but hash(x) != hash (y)\n
%s %zu bytes, buckets %zu bytes
INITIALIZE: thread %p: refusing to call +[%s initialize] in fork() child process because it may have been in progress when fork() was called
warn when objc_sync_enter or objc_sync_exit return an error
OBJC_DISABLE_TAG_OBFUSCATION
[%p]  %#16lx  %s
_TtCs12_SwiftObject
\"%s\"%s,
+[%s initialize] may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead. Set a breakpoint on objc_initializeAfterForkError to debug.
INITIALIZE: thread %p: setInitialized(%s)
INITIALIZE: %d/%d (%g%%) successful secondary metaclass lookups
log fault when at least a set number of autorelease pages has been allocated
CLASS: '%s'%s %p has missing weak superclass, disabling.
CUSTOM RR
link error: class '%s' not found.
warn
log classes with custom allocWithZone methods
,
MallocStackLoggingNoCompact
warn about autorelease with no pool in place, which may be a leak
PREOPTIMIZATION: IGNORING preoptimized selectors in %s
PROTOCOLS: protocol at %p is %s  (duplicate of %p)
OBJC_HELP=
OBJC_DEBUG_UNLOAD
IMAGES: unloading image for %s%s\n
__DATA_DIRTY
Weak reference loaded from %p contains %p which is not in the weak references table
OBJC_PRINT_CLASS_SETUP
PREOPTIMIZATION: is ENABLED (version %d)
LOAD: %d categories still waiting for +load\n
OBJC_PRINT_OPTIONS is set
objc_sync_exit(%p) returned error %d
class_ro_t enforcement disabled
__CF
mutation detected during 'for(... in ...)'  enumeration of object %p.
arm64e
couldn't dlopen libobjc-trampolines.dylib: %s
Object
__IncompleteProtocol
Protocol
__NSUnrecognizedTaggedPointer
NSObject
_setWeaklyReferenced
T@\"NSString\",R,C
doesNotRecognizeSelector:
respondsToSelector:
isa
methodSignatureForSelector:
_isDeallocating
instancesRespondToSelector:
isSubclassOfClass:
retainWeakReference
allowsWeakReference
release
T#,R
conformsTo:
isMemberOfClass:
retainCount
dealloc
new
autorelease
performSelector:
debugDescription
description
isKindOfClass:
mutableCopyWithZone:
descriptionForInstanceMethod:
finalize
methodForSelector:
mutableCopy
performSelector:withObject:
TQ,R
init
instanceMethodForSelector:
isEqual:
load
name
superclass
descriptionForClassMethod:
instanceMethodSignatureForSelector:
retain
copyWithZone:
🤯
isProxy
_objc_initiateDealloc
allocWithZone:
isAncestorOfObject:
resolveClassMethod:
resolveInstanceMethod:
selector
alloc
class
conformsToProtocol:
performSelector:withObject:withObject:
_noteAssociatedObjects
T@\"NSString\",?,R,C
isFault
_tryRetain
copy
hash
zone
forwardInvocation:
forwardingTargetForSelector:
initialize
self
v24@0:8:16
v16@0:8
r*16@0:8
B24@0:8#16
B24@0:8:16
B24@0:8@\"Protocol\"16
#
^{objc_method_description=:*}24@0:8:16
@24@0:8^{_NSZone=}16
@\"NSString\"16@0:8
B16@0:8
@16@0:8
B24@0:8@16
Q16@0:8
#16@0:8
@24@0:8:16
v24@0:8@16
^{_NSZone=}16@0:8
Vv16@0:8
^?24@0:8:16
@32@0:8:16@24
@40@0:8:16@24@32
```
