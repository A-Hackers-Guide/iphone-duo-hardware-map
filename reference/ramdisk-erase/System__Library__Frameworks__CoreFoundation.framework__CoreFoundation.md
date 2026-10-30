# `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 14,159,408 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 24 (Size: 5240)
Flags         = NoUndefs, DyldLink, TwoLevel, AppExtensionSafe
```

## Linked libraries (6)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0, reexport)`
- `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal (compatibility version 1.0.0, current version 609.1.7, upward)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8, upward)`
- `/usr/lib/libicucore.A.dylib (compatibility version 1.0.0, current version 78.1.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (142 classes, 9 protocols)

Classes: `CFPDCFDataBuffer`, `CFPDCloudSource`, `CFPDContainerSource`, `CFPDDataBuffer`, `CFPDMirroredSource`, `CFPDObserverOnlyTombstone`, `CFPDPurgeableBuffer`, `CFPDSource`, `CFPDSourceLookUpKey`, `CFPrefsCloudSource`, `CFPrefsConfigurationFileSource`, `CFPrefsDaemon`, `CFPrefsManagedSource`, `CFPrefsPlistSource`, `CFPrefsSearchListSource`, `CFPrefsSource`, `CFPrefsSuiteSearchListSource`, `NSArray`, `NSBlock`, `NSBlockInvocation`, `NSCFArray`, `NSCFData`, `NSCFDictionary`, `NSCache`, `NSCalendar`, `NSConstantArray`, `NSConstantData`, `NSConstantDate`, `NSConstantDictionary`, `NSData`, `NSDate`, `NSDateComponents`, `NSDictionary`, `NSEnumerator`, `NSException`, `NSFileSecurity`, `NSIndirectTaggedPointerString`, `NSInputStream`, `NSInvocation`, `NSLocale`, `NSMachPort`, `NSMethodSignature`, `NSMutableArray`, `NSMutableData`, `NSMutableDictionary`, `NSMutableOrderedSet`, `NSMutableSet`, `NSNull`, `NSObject`, `NSOrderedSet`, `NSOutputStream`, `NSPort`, `NSRunLoop`, `NSSet`, `NSSharedKeyDictionary`, `NSSharedKeySet`, `NSStream`, `NSTaggedPointerString`, `NSTaggedPointerStringCStringContainer`, `NSTimeZone`, `NSTimer`, `NSURL`, `NSUserDefaults`, `_CFPrefsClientContext`, `_CFPrefsOversizedPlistDescription`, `_CFPrefsPendingKVONotification`, `_CFPrefsSynchronizer`, `_CFStreamDelegate`, `_CFXPreferences`, `_CFXPreferencesHandle`, `_NSMoribundCache`, `_NSPlaceholderLocale`, `_NSZombie_`, `__CFNotification`, `__CFPrefsWeakObservers`, `__NSArray0`, `__NSArrayI`, `__NSArrayI_Transfer`, `__NSArrayM`, `__NSArrayReverseEnumerator`, `__NSArrayReversed`, `__NSAtom`, `__NSAutoBlock`, `__NSBlockVariable`, `__NSCFArray`, `__NSCFAttributedString`, `__NSCFBoolean`, `__NSCFCharacterSet`, `__NSCFConstantString`, `__NSCFData`, `__NSCFDictionary`, `__NSCFError`, `__NSCFInputStream`, `__NSCFLocale`, `__NSCFNumber`, `__NSCFOutputStream`, `__NSCFSet`, `__NSCFStreamWeakDelegateWrapper`, `__NSCFString`, `__NSCFTimer`, `__NSCFType`, `__NSConstantArrayEnumerator`, `__NSConstantDictionaryEnumerator`, `__NSDate`, `__NSDictionary0`, `__NSDictionaryI`, `__NSDictionaryM`, `__NSDictionaryObjectEnumerator`, `__NSEnumerator0`, `__NSFastEnumerationEnumerator`, `__NSFileSecurity`, `__NSFinalizingBlock`, `__NSFrozenArrayM`, `__NSFrozenDictionaryM`, `__NSFrozenOrderedSetM`, `__NSFrozenSetM`, `__NSGenericDeallocHandler`, `__NSGlobalBlock`, `__NSMallocBlock`, `__NSMessageBuilder`, `__NSOrderedSetArrayProxy`, `__NSOrderedSetI`, `__NSOrderedSetM`, `__NSOrderedSetReverseEnumerator`, `__NSOrderedSetReversed`, `__NSOrderedSetSetProxy`, `__NSPlaceholderArray`, `__NSPlaceholderDate`, `__NSPlaceholderDictionary`, `__NSPlaceholderFileSecurity`, `__NSPlaceholderOrderedSet`, `__NSPlaceholderSet`, `__NSPlaceholderTimeZone`, `__NSSKGraph`, `__NSSetI`, `__NSSetM`, `__NSSingleEntryDictionaryI`, `__NSSingleObjectArrayI`, `__NSSingleObjectEnumerator`, `__NSSingleObjectSetI`, `__NSStackBlock`, `__NSTaggedDate`

Protocols: `NSCacheDelegate`, `NSCoding`, `NSCopying`, `NSFastEnumeration`, `NSMutableCopying`, `NSObject`, `NSRedactedDescription`, `NSSecureCoding`, `NSStreamDelegate`

## Strings (61,123)

First 2,500 of 61,123.
```
attempt to write to a container %{private}s that does not yet exist. Using client-provided container path without resolving symlinks.
Failed access token check because path of token doesn't match verification path (%s vs %s)
cfprefsd could not create a shmem named %s, cross-process preferences will not work correctly
All kCFPreferencesCurrentUser domains in this process will be volatile, because homeDirPath %{public}s
Updating Key-Value Observers Of Preferences
-[%s %s]: unrecognized selector sent to instance %p
couldn't stat file at %{private}s due to \"%{public}s\"
The file could not be opened: %{darwin.errno}d
client-%i %{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu
__CFRunLoopModeFindSourceForMachPort returned NULL for mode '%@' livePort: %u
sendSystemAndUserMessage
*** %s: object cannot be nil (key: %@)
Successfully created directory %{private}s. Retrying write.
dlfcn load bundle %{public}@ closing existing reference to handle %p
dlfcn load framework %{public}@ closing existing reference to handle %p
DistributedNotificationCenter: Unable to create restore timer
Disabling factories in array %{public}p for bundle %{public}p
*** %s: index %lu in index set beyond bounds [0 .. %lu]
_CFCopyHomeDirURLForUser failed to create a proper home directory. Falling back to /var/empty. Error(s):\n%{public}@
Attempted to create instance, but factory %{public}@ is disabled
AddInstanceForFactory: Added instance on %p for %{public}@
RemoveInstanceForFactory: Removed instance on %p for %{public}@
failed to get file system representation for url: %{private}@
Unable to read key-paths %@ from .strings file: %@ / %@: %@
DistributedNotificationCenter: Scheduling restore in %llu ms
Attempt to set a non-property-list object %{public}@ as an NSUserDefaults/CFPreferences value for key %{public}@
Disabling saving preferences for { %{public}@, %{private}@, %{public}s, %{private}@ } because home directory is inaccessible
Couldn't get parent path due to %{darwin.errno}d
Couldn't %{public}s %{private}s due to %{darwin.errno}d. Asking client to create directory.
Could not target user session daemon connection for user %@: user session with UID %i is not active
Cannot find executable for %{public}@
*** %{public}s, break on '_CFMachPortDeallocationFailure' to debug: {p:%{private}d c:%d is:%d <i:%d,d:%d> s:%d,r:%d nsi:%d,nss:%d,nsr:%d - ic:%d,ip:%d}
dlsym cannot find symbol %{public}@ in %{public}@: %s
*** CFMessagePortCreateLocal(): CFMachPortCreateWithPort() failed, port = %{public}d
Unable to load .strings file: %@ / %@: Top-level object was not a dictionary
Found potentially bad plist after draining pending changes {%@ %@}
#prefsbeforeunlock Attempt to access %{private}s by %{public}@
Using ~iphone resources (classic)
Internal error unloading bundle %{public}@ : %s
*** CFMachPortCreateWithPort(): mach_port_type for 0x%lx failed with %d
CFURL initialized with \"/.file/id=\" file system representation
error \"%{public}s\" creating file %{private}s
Replacing preferences for EUID change: %u -> %u %{public}@
Resetting CFPreferences/NSUserDefaults
Could not lookup group container %{public}s: %{public}s
cfprefsd crashed, retrying message
read an unexpected amount of data from %{private}s. This likely means that someone wrote directly to that file behind cfprefsd's back, which is unsupported.
*** CFMessagePortCreateLocal(): mach_port_insert_right(MACH_MSG_TYPE_MAKE_SEND) returned %{public}d, port = %{public}d
loctable overridden by installed files. Bundle: %@, table: %@, language: %@
Could not resolve UID for user identifier %@. Please use _CFPreferencesGetUserIdentifierForUid() to target a specific user
%{private}@: Attempt to store >= %d bytes of data in CFPreferences/NSUserDefaults was allowed by virtue of direct mode
main bundle %{public}@ getting handle %p
Attempt to load executable of a type that cannot be dynamically loaded for %{public}@
*** %s: index %lu in index set beyond bounds for empty ordered set
*** %s: set argument is not an NSSet
*** %s: index %lu beyond bounds [0 .. %lu]
No defaults configuration file found for %{public}@ (looked at %{public}@)
sendSystemMessage
Validation of plist read from disk failed. DELETING file. {%@ %@}
Resource lookup at %{private}@\n\tRequest       : %{public}@\n\tResult        : %{public}@\n
range.location out of range (<0)
Notifying observers of { %{public}@, managed: %d }
handleRequest
%{private}@: Transitioning into direct mode
plist diff for %{private}@ was invalid
*** %s: range {%lu, %lu} extends beyond bounds for empty set
RemoveInstanceForFactory: No factory registered for id %{public}@
Responding to device unlock to refresh preferences reads previously denied by data protection { %@, %@, %@ }
Found potentially bad pre-existing plist, but not clearing yet, as we weren't asked to validate {%@ %@}
Failed access token check because the file could not be opened: %{darwin.errno}d
Could not return a uncanonicalized path to client
Failed to compute parent directory path for %{private}s.
*** %s: string argument is not an NSString
*** %s: url argument is not an NSURL
-[%s %s]: attempt to insert nil
Could not get uncanonicalized path (domain: %{public}@, user: %{public}@) from daemon
*** %s: keys argument is not an NSArray
%s
loctable overridden by installed files. Bundle: %@, table: %@
%{private}@: Storing >= %d bytes of data in CFPreferences/NSUserDefaults. If this exceeds %{public}d, it may %{public}s. This is a bug in %{public}@ or a library it uses.\n%@
Cannot find executable for bundle %{public}@
writing key %{private}@ in cloud domain %{public}@ failed with exception %{public}@
Using ~ipad resources (classic)
file read from disk for %{private}@ was not a plist. Error: %{public}@
Volatilizing domain, because home directory is invalid. %{private}@
*** CFMachPortCreate failed. mach_port_allocate() returned %d
PlugIn %{public}@ is about to be unloaded
Identifier: %{public}@ User: %{private}@ %{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu
`WrappedBundle` link too short or pointed outside bundle at %{public}@
*** %s: key cannot be nil
loctable failed to load for bundle: %@, table: %@: %@
Lookup inconsistency for request from pid %d
Replacing preferences for non-launch persona UID change: %u -> %u %{public}@
A filtered Info.plist result was not a dictionary at URL %{private}@ (for key paths %{public}@)
dlfcn check load bundle %{public}@, dlopen of %{public}s mode 0x%x getting handle %p
%{public}ld factories found for requested plugin type %{public}@
RegisterPlugInType: No factory registered for id %{public}@
Invalid file descriptor %d
cfprefsd couldn't open temporary path appropriate for %{private}s for writing due to \"%{public}s\". Cancelling attempt to save preferences
Failed access token check because inode of token doesn't match verification inode
There was an error parsing the Info.plist for the bundle at URL <%{public}p>: %{public}@ - %{public}ld
Data for { %@, %@ } was purged due to memory pressure
This is cfprefsd listening on %s
Process %{public}@ running as root is attempting to look up an app group container. That's not supported
Loading Preferences From System Session CFPrefsD
couldn't read preferences file %{private}s due to %{public}s
writing key %{private}@ in cloud domain %{public}@
looked up invalid value %{private}@ for key %{public}@ in %{private}@. Replacing with NULL.
Invalid data written from preferences to path %s
Found defaults configuration for %{public}@ at %{public}@
Failed access token check because _actualPath has changed since the last-known path (%s vs %s)
forcing direct access mode on for this process. It's slower, uses more memory, and doesn't respond to changes immediately. Update your sandbox profile to allow cfprefsd access!
Not allowing process impersonation by process %{public}s (%{public}d) due to missing com.apple.private.defaults-impersonate entitlement.
Notifying observers of %{private}@
Could not resolve UID for user \"%{public}s\".
Couldn't write values for keys %{private}@ in %{private}@: %{public}s
Cannot recognize type of executable for %{public}@
Registering factory %{public}@ type %{public}@
Process %{public}@ began observing %{private}@
cfprefsd agents don't exist on non-macOS platforms
Notifying CFPrefsD Of Updated Managed Preferences
flushCachesForAppIdentifier
serialized plist for %{private}@ was not a dictionary
*** CFMachPortCreateWithPort(): allocation failure
*** %s: comparator cannot be nil
MISS: %s
Couldn't create URL for managed preferences container
*** CFMachPortCreateWithPort(): bad Mach port parameter (0x%lx) or unsupported mysterious kind of Mach port (%d, %ld)
*** CFMessagePortCreateLocal(): existing port invalid
Failed access token check because cacheFileInfo failed
DistributedNotificationCenter: Sending restore attempt (%d registrations) ...
length cannot be less than zero
bad plist data: %{public}@
Ensure bundle %{private}@ set loaded fallback
Month %d is out of bounds
dlfcn unload bundle %{public}@, handle %p
Attempting to interact with NSCache instance that is being deallocated. Break on \"NSMoribundCache_invalidAccess\" to debug.
Simulating ENOSPC in cacheFileInfo for testing
Validation of pre-existing plist failed. Clearing cache and re-reading from disk. {%@ %@}
Failed access token check because the it was not opened for writing
temporarily rejecting %{public}s in %{private}@ from process %{public}@ because an access token is needed
rejecting write of key(s) %{private}s in %{private}@ from process %{public}@ because %{public}s
*** -[%s %s]: index %lu beyond bounds for empty array
CFPreferences: user home directory is unavailable. User domains will be volatile.
Failed to create directory %{private}s (mode %d, UID %d, GID %d) because of %{darwin.errno}d.
createDiskWrite
Failed access token check because F_GETPATH failed: %{darwin.errno}d
Could not look up the username for %{public}d after three tries
proc_pidpath(%i) error: %{darwin.errno}d
CFPrefs client received non-reply message: %s
*** %s: attempt to insert nil object from objects[%lu]
CFBundle Function Call: Source location: %{public}s:%d %{public}s
Ensure bundle exists failed for path %{private}@
dlfcn load bundle %{public}@, dlopen of %{public}s mode 0x%x returns handle %p
Detected potentially harmful notification post rate of %g notifications per second
Couldn't get path for fd %d
CFPreferences: error writing file %s: %{darwin.errno}d\n
Failed access token check because the file it references has been unlinked
*** %s: index %lu beyond bounds for empty ordered set
CFVolumeObserver: Notifying client about disk %{public}@ (%{private}@) because it's path changed to NULL.
sendUserMessage
Bundle: %{private}@, key: %@, value: %@, table: %{public}@, localizationNames: %{public}@, result: %{public}@
Unable to load .strings file: %@ / %@: %@
No write access to parent directory of %{private}s
Couldn't get real path for %{private}s due to %{public}s
Initial attempt to validate sandbox access of message %{private}s in container %{private}s due to no plist path, but we recovered successfully by recalculating the path.
`WrappedBundle` link invalid or pointed outside bundle at %{public}@
Lazy cache miss for bundle: %@ key: %@ table: %@
respondToFileWrittenToBehindOurBack
couldn't delete temporary file at %{private}s due to \"%{public}s\"
Detected corrupted preferences in %{public}s, replacing them with an empty dictionary to recover. Error: %@
acceptMessage
Managed preferences are %{public}s for %{private}@
plist read from disk for %{private}@ was not a dictionary
*** %s: predicate cannot be nil
*** %s: index %lu beyond bounds for empty array
Found non-dictionary property list, which is invalid for preferences. Ignoring it.
Cannot find function pointer %{public}@ for factory %{public}@ in %{public}@
Unregistered factory %{public}@ (%{public}@)
Received remote change notification from process %lld for { domain: %s, user: %s, byHost: %d, path: %s, cloud configuration path: %s }
setting %{public}@ in %{private}@
going volatile, because unable to obtain shmem entry for role: %d name: %{public}s. %{private}@
range.location out of range (>len)
AddInstanceForFactory: No factory registered for id %{public}@
%{public}ld factories found for requested plugin type %{public}@ in plugin %{public}@
serialized data for %{private}@ was not a plist. Error: %{public}@
%{private}@: Value for key %{public}@ was %{private}@. Expected %{private}@ (%{public}@)
A RequestNewData response gave an invalid plist. We'll return wrong data this time, but NOT going volatile. Sent a request to validate the plist in the daemon and remove it if invalid. %{private}@
*** %s: index set argument is not an NSIndexSet
ending index out of bounds
*** CFMessagePortCreateLocal(): CFMachPortCreate() failed
Bundle %{public}@ contains a factory UUID of 00000000-0000-0000-0000-000000000000 with function 'MyFactoryFunction'. This bundle is not a valid plugin.
Registering static factory %{public}@ %{public}@ bundle %{public}p
_CFPreferencesGetUserIdentifierForUID(): Could not resolve user with UID %i: %{darwin.errno}d
*** %s: range {%lu, %lu} extends beyond bounds for empty array
Error: CFDateFormatter time zone has an empty name: %@
Type %{public}@ added to factory %{public}@
wrote file %{private}s
failed to map file from disk for %{private}@. error: %{darwin.errno}d
*** %s: index set cannot be nil
attempted to write invalid value %{private}@ for key %{public}@ in %{private}@. Replacing with NULL.
CFURLCopyParameterString is deprecated and now always returns NULL. The path component now includes the part of the URL string which CFURLCopyParameterString used to return.\nURL = %{private}@
%{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu
plist had invalid size: %zu.
*** %{public}s, break on '_CFMachPortDeallocationFailure' to debug: {null - ic:%d,ip:%d}
Cannot find factory %{public}@
UnregisterFactory: No factory registered for id %{public}@
Registered factory %{public}@ (%{public}@)
Process %{public}@ read data for %{private}@, backed by %{private}s
attempt to set %{private}@ for key in %{private}@ in read-only (due to a previously logged write error) preferences domain %{private}@
Unable to resolve directory (%d)
error renaming file %s to %s (errno: %d).
Re-marking { %@, %@ } as dirty because previous write failed with ENOSPC
Failed access token check because verification path doesn't match known actual path (%s vs %s)
Need to call TCC to ascertain if client %d has sandbox access. Moving to a different queue
%{public}@ skipping setting already-present value for key %{private}@
Extensions of wrapped bundles did not match (one missing) at %{public}@
-[%s %s]: index (%ld%s) beyond bounds (%ld)
Process %{public}@ wrote the key(s) %{private}s in %{private}@
Process %{public}@ read nothing for %{private}@, backed by %{private}s
setting %{private}@ in %{private}@
*** %s: pointer to objects array is NULL but length is %lu
Type %{public}@ removed from factory %{public}@
Unable to load .stringsdict file: %@ / %@: %@
unable to validate sandbox access of message %{private}s in container %{private}s due to no plist path, conservatively assuming not allowed.
%{private}@: Attempting to store >= %d bytes of data in CFPreferences/NSUserDefaults on this platform is invalid. This is a bug in %{public}@ or a library it uses.\n%@
*** -[%s %s]: index %lu beyond bounds [0 .. %lu]
Unable to create bundle at URL (%@): unable to create file system representation of URL (%d)
Extensions of wrapped bundles did not match at %{public}@
*** %s: ordered set argument is not an NSOrderedSet
+[%s %s]: unrecognized selector sent to class %p
Found potentially bad plist when reading from disk, but not deleting, because we weren't asked to validate {%@ %@}
Loading Preferences From Direct CFPrefsD
plist is too large to deserialize in this process: %zu.
PlugIn %{public}@ is now scheduled for unloading
Couldn't get uncanonicalized path for domain %{public}@
Domain: %{public}@, User: %{public}@, ByHost: %i, Managed: %i %{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu
About to serve up potentially bad plist {%@ %@}
invalid argument (path instead of domain/application identifier) %{private}s
*** %s: range {%lu, %lu} extends beyond bounds for empty ordered set
dyld image path for pointer %p is %{public}@
cloud preferences changed for %{public}@
Client (%d) passed an invalid cloud store identifier value.
serialized validation data for %{private}@ was not a dictionary plist. Error: %{public}@
*** CFMachPortCreate failed. mach_port_insert_right() returned %d for port %d
bundle %{public}@ handle %p dlsym returns symbol %p for %{public}s
Attempting to use the main runloop, but the main thread has exited. This message will only log once.
Could not look up bundle for identifier %{public}@ due to: %{public}@
Process %{public}@ sent a request related to %{private}@
rejecting read of %{private}@ from process %{public}@ because %{public}s
Process %{public}@ %{public}s for domain %{public}s
More than one bundle with the same identifier has been added: %{public}@
cfprefsd has asked to provide an access token for %{private}s too many times. Bailing out.
Created instance of plugin for factory %{public}@ type %{public}@
failed to get file system representation for temporary file path appropriate
CFPreferences: error fsyncing file %s: %{darwin.errno}d\n
Validation of plist read from disk succeeded. {%@ %@}
no cache for %{private}@, loading from %{private}s
CFURL initialized with \"/.file/id=\" path
CFVolumeObserver: Notifying client about disk %{public}@ (%{private}@) being unmounted because it disappeared.
error %d setting do-not-back-up attribute on file %s
Couldn't open parent path %{private}s due to %{darwin.errno}d
setting new value %{private}@ for key %{private}@ in %{private}@
sandbox check for %{public}s on %{private}s failed with error: %{darwin.errno}d
looked up value %{private}@ for key %{private}@ in %{private}@ via %{private}@
dlfcn load framework %{public}@, dlopen of %{public}s mode 0x%x returns handle %p
Language lookup at %{private}@\n\tLocalizations : %{public}@\n\tDev language  : %{public}@\n\tUser prefs    : %{public}@\n\tMain bundle   : %{public}@\n\tAllow mixed   : %{public}lu %{public}s\n\tResult        : %{public}@\n
flushManagedSources
Flushing Cached Preferences Data
failed to lstat plist fd: %{darwin.errno}d.
*** %s: count (%lu) of objects array is ridiculous
couldn't deallocate purgable buffer. Leaking it to avoid crashing. Error was %{public}d
*** CFMachPortCreateWithPort(): invalid mach port %p (from cache: %d)
Caught exception during runloop's autorelease pool drain of client objects %{public}@: %{private}@ userInfo: %{private}@
*** %s: objects argument is not an NSArray
Domain: %{public}@, User: %{private}@, ByHost: %i, Managed: %i %{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu
An error occurred while setting iopolicy: %{darwin.errno}d
*** %s: object cannot be nil
Could not parse markdown while retrieving localized string for key %{public}@ in bundle %{public}@
%{private}@ loaded: %s and %s
Loading Preferences From User Session CFPrefsD
dlfcn check load bundle %{public}@, dlopen of %{public}s mode 0x%x no handle
DistributedNotificationCenter: Exceeded maximum recent restore attempts, will not attempt restore for now.
Error creating data ref from plist, data was %p.
unable to find user information for requested user %s
looked up value %{private}@ for key %{private}@ in %{private}@
Re-marking { %@, %@ } as dirty because attempt to open temporary path failed with ENOSPC
Failed access token check because fstat failed: %{darwin.errno}d
NSUserDefaults/CFPreferences is doing direct file access for this process
Could not connect to cfprefsd. No CFPreferences/NSUserDefaults changes will be saved
Too many nested arrays or dictionaries
Unable to create bundle at URL (%@): does not exist or not a directory (%d)
UnregisterPlugInType: No factory registered for id %{public}@ type %{public}@
PlugIn %{public}@ is now unscheduled for unloading
Factory %{public}@ has been disabled
Couldn't %{public}s %{private}s due to %{public}s
diskWriteIO
CFPreferences detected an inconsistency. An attempt by process %{public}d to access preferences in \n%{private}@\n actually resolved to \n%{private}@\n Typically this indicates that the process's sandbox profile changed in a way that added 
*** %s: range {%lu, %lu} extends beyond bounds [0 .. %lu]
Error getting app group containers for %s: %s
*** %s: marker cannot be nil
ERROR: %@ not found in table %@ of bundle %@
attempt to set %{private}@ for key in %{private}@ in non-persistent preferences domain %{private}@
Couldn't apply changes: %{private}@
Unable to create bundle at URL (%@): normalized URL null
*** CFMessagePort: bootstrap_register(): failed %d (0x%x) '%s', port = 0x%x, name = '%s'\nSee /usr/include/servers/bootstrap_defs.h for the error codes.
Couldn't get container path for managed preferences due to error %llu
Couldn't get file name due to %{darwin.errno}d
Process %{public}@ requested to stop observing %{private}@
Couldn't read values in %{private}@: %{public}s, detaching from cfprefsd
More than one bundle with the same factory UUID detected: %{public}@ in %{public}@ and %{public}@
*** %s: dictionary argument is not an NSDictionary
*** CFMessagePortCreateLocal(): memory allocation failed
Factory %{public}@ does not support type %{public}@
CFString: %s(): Expect mutable string
Simulating out of disk space on creation
Process %{public}@ %{public}s
Couldn't read values in %{private}@: %{public}s
*** %s: block cannot be nil
Simulating out of disk space on write
flushing cache for %{private}@ because %{public}@
cfprefsd required creation of a directory, but failed to provide the path.
Requesting validation of plist after invalid data detected
*** _CFMachPortCreateReply failed. mach_port_construct() returned %d
This is cfprefsd with %i workloops listening on %s
Using ~%@ resources
Validation of pre-existing plist succeeded. {%@ %@}
Failed access token check because %d is invalid
Couldn't map preferences shmem named %{public}s
*** %s: array argument is not an NSArray
*** %s: capacity (%lu) is ridiculous
Unable to create bundle at URL (%@): malloc failure
Error loading %{public}s (%lu):  %{public}s
Failed to register dependent notification %{public}@ -> %{public}@
*** %s: index %lu in index set beyond bounds for empty array
cfprefsd has asked to create directory for %{private}s too many times. Bailing out.
Couldn't write values for keys %{private}@ in %{private}@: %{public}s, detaching from cfprefsd
found no value for key %{private}@ in %{private}@
Domain: %{public}@ %{public, signpost.description:begin_time}llu %{public, signpost.description:end_time}llu
UIAccessibilityLoader
CFBundlePrimaryIcon
_findEdges
Setup:/Network/Service/[^/]+/Interface
rootObject
PFL.Budget.Siri.SpeechGlobalNNLM:Metrics
NSURLVolumeSupportsCompressionKey
RBSMimicTaskSuspensionAttribute
com.apple.FocusSettings
com.apple.imfoundation.IMRemoteURLConnectionAgent
suite/com.apple.health.shared/kCFPreferencesAnyUser
com.apple.private.security.storage.Weather
call_being_recorded_silence.wav
useMusicCuesForTimeline
pound-force
MLCGPUHelper
ZLASTACTIVITYSUMMARYVIEWEDDATE
https://www.google.com/
com.apple.corespeech.speechmodeltraining.xpc
pagingBehavior
R -> dBASPL
/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
tiledArtworkRequest
MallocStackLoggingDirectory
legibilityGradientOpacity
MapsSyncManagedCachedUserReview
com.apple.private.health.respiratory/A//B/L
USDLib_FormatLoaderProxy
TTYHardwareEnabledPreference
-[__NSArrayM insertObject:atIndex:]
eligibleServices
fmadminws_gateway_url
locationpushd
com.apple.siri.tts.voice.tr_TR.yelda.vocalizer.premium
-[NSMutableArray addObjects:count:]
sendToDigestThresholdForNumNonEngagements
com.adobe.xfdf
SUCoreEventReporterDelegate
com.apple.BTServer.pbap
com.apple.UIKit/A//B/L
/System/Library/Frameworks/Accessibility.framework/Accessibility
com.apple.mkb.usersession.info
/System/Library/PrivateFrameworks/SceneIntelligence.framework
applyRotationToFirstAndLast
BSXPCServiceConnectionProxy<UISApplicationStateXPCServerInterface>
com.menufy
com.apple.reminders.button.menu.inline
managed/com.apple.security/kCFPreferencesAnyUser
/System/Library/Frameworks/AudioToolbox.framework
XPCServices
x11app
viewModeTransitionSpringStiffness
file:///Applications/GameCenterWidgets.app/
com.apple.PDUIApp
relayServerHostsToHandleUniversalLinks
com.apple.diagnosticpipeline.cloudkit_expedited_upload
com.apple.private.alloy.continuity.unlock
/system/time
ZBOOKMARKDATA
gear2@1x.png
file:///System/Library/Audio/UISounds/New/Fanfare.caf
/Library/Logs/CrashReporter/
apple-originating-system
/System/Library/PrivateFrameworks/Lexicon.framework
_NSURLVolumeRefNumKey
MailComposeScene
deliverUpdatedScheduleSettings
Transfer Transport Management
_PSSharingContactRankerMLModelInUse
timeToLive
mergeTargetPerson
_DKApplicationMetadataKey__dyldPlatform
com.apple.private.health.localdevice
modify-activity-session-airplay
shared-store-review-enabled
/System/Library/PrivateFrameworks/SiriCrossDeviceArbitrationFeedback.framework
/uts/v2/init/features
_DKNotificationScreenLockImputedMonitor
muteToggleButtonAutoHideDelay
/System/Library/LocationBundles/Emergency SOS.bundle
_convolution3
_ZPROCESSIDTS
-[__NSFrozenSetM enumerateObjectsWithOptions:usingBlock:]
en_US_POSIX
flow_estimation_5.espresso.net
com.microsoft.bmp
com.apple.pay
autoEditProductionSimulatedDelay
feedCardPortraitAspectRatio
AAPCommandQuit
pairingURL
accounts.momd/
_ci_read_pixel_420_packed_h
CustomPreferences
com.apple.SiriTTSTrainingAgent
com.apple.coreaudio.device/C//*/L
Z_DKSIRIINTENTEVENTMETADATAKEY__EVENTDATA
_INPBIntentMetadata
INRequestRideIntent
SignatureDigestMD4
/System/Library/PrivateFrameworks/FamilyCircle.framework
_DKMapsShareEtaFeedbackMetadataKey__contactId
MACaptionSystemDefaultProfile
com.apple.osanalytics.OTATaskingAgent/A//B/L
Localizable-Lyon.loctable
/Applications/Siri.app
com.apple.dasd.dailyPeriodicUtilityNetworking
UNRequiresTopics
FilesMarkedPurgeable
audioOutcue
containingPath
com.apple.private.alloy.keytransparency.accountkey.pinning
INTrainReservation
iphone
cpx
application/mp4
Server Has Provisioned Myriad
Rating-Brazil_12.tiff
StockIntentsStock
io.quadrant
com.apple.MarkupUI.MarkupPhotoExtension
com.apple.proactive.SpringBoard.DockApps
com.apple.Maps.tripsharing.sharing
initWithCoder:
suite/com.apple.WebUI/kCFPreferencesAnyUser
cloudVideoCount
CIPortraitBlurV3.metallib
com.apple.remindd.reminderAlarm.nextMorning.weekend
_ci_to_l16_as_rg8
magnifierBrightness
com.apple.DataDeliveryServices/C//*/L
staging-walletshare.sandbox.googleapis.com
m
viewProductPersonalized
ZACTIVITYEVENTSDATA
rgbTransformMap_Contour_NEAR_fp16_RGBAslice5
_LSExecutablePath
_hlg_srmapping
CellularPlanManager
http://loinc.org
Syndication.photoslibrary
/System/Library/Frameworks/CoreML.framework/CoreML
com.apple.MTLCompiler
file:///System/Library/PrivateFrameworks/AppleAccount.framework/
unarchivedObjectOfClasses:fromData:error:
-[__NSOrderedSetM removeObjectAtIndex:]
YYYY
/device/isPluggedIn
SEARCH_QUICK_ACTION_TITLE
BKSWorkspace
ShowAlwaysDeliverSwitch
bluetoothuserd
CNIndexRequestHandler
managed-preference-read
AppIconMask@3x.png
com.apple.proactive.PersonalizationPortrait.NamedEntityImport
com.apple.accessoryd
com.apple.siri.nl.snlc
com.apple.CFFileDescriptor
kk-
0.0
com.apple.siri.tts.voice.en_US.quinn.gryphon.premium
communityID
AMSSamplingSession-TLSSessionTickets
LearnMoreTagsViewController.storyboardc
minus.slash.plus
/System/Library/Frameworks/WebKit.framework
ZISLOCALLYAVAILABLE
SiriAnalytics
com.apple.ax.TTSResource.LaunchActivity
com.apple.certificates
com.apple.frontboard.layout-monitor
com.apple.locationd.synchronous
ZCLOUDVERIFIEDTYPE
ICD-10-PCS
com.apple.deviceactivityui.report-extension
/System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
MPEG-4 audio
retrieveGallery
takeValue:forKey:
kCFDateFormatterMonthSymbolsKey
com.apple.DiagnosticsService.Diagnostic-8253
scenenet_op-v8d.plist
file:///System/Library/PrivateFrameworks/RecapPerformanceTesting.framework/
downloads-url
_CFBT_.materialrecipe
x-maps-ac-auth
com.apple.transparency.storage
Lodging Reservation
Show Symbol Price
https://gspe21-ssl.ls.apple.com/attributionsearch/button-dasoertliche-1@2x.png
/private/var/mobile/Library/Maps/ReportAProblem/
com.apple.FRC
_colorPolynomialRGB
Photos Event URL (Deprecated)
softdepot.filemaker.com
/System/Library/PrivateFrameworks/MobileSystemServices.framework
com.apple.coreservices.appleidauthentication.keychainaccessgroup
cubic foot
PFL.Budget.Tips.TipsPFLPlugin:Metadata
/var/mobile/Media/DCIM/
com.apple.homed.notbackedup/C//*/L
croppingQuadTopRightX
com.apple.FileProvider.GenericShared
5.0~fmf.plist
cnn_facepose.espresso.net
platterClientStyle.visualstyleset
CPLProxyLibraryManager
ZSUPPORTEDCONNECTORS
/uts/v3/siri/content
com.apple.NanoRegistry
DiagnosticsService
https://setup.icloud.com/setup/qualify/syncMachine
com.apple.WatchListKit/C//*/L
com.apple.mica.haptic
com.apple.private.alloy.biz
/System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore
answerRTTCallsAsMuted
com.apple.virtualMemoryMode.plist
videoGravity
NanoDefaultIcon-40.0@2x.png
ZVALUESTRING
PrivacyProxyConfigurationServerPath
adjustToWallClockTime
  numKey = %u\n
pfl:com.apple.proactive.PMLDESPlugin.responses:metadata:
VNTrackObjectRequest
ZLOCKEDNOTESMODE
allPhotosAspectFitFocusPadding
dayGroupHighlightBeingSummaryAssets
lookupConeAngle
_ci_swizzle_rgba8_to_rgb10_wide
managed/com.apple.siri.shortcuts/kCFPreferencesCurrentUser
normalizedStackVerticalOffset
NSRegulatoryPrivacyDisclosureOBKPrivacyBundle
com.apple.private.alloy.healthapp.messaging
Albanian
ZEMBEDDEDTHUMBNAILOFFSET
credentialType
buttonColor
NSBlockOperation
com.apple.private.ZhuGeSupport.CopyValue
com.apple.SensorKit.physicalActivityEvents
Waveform-Audio
cancellationDate
device-queries-per-hour-com.apple.private.alloy.arcade
com.apple.StoreDemoViewService
lock@2x-812h.ca
-[NSSharedKeyDictionary countByEnumeratingWithState:objects:count:]
shareSheetLinkAssetCountThreshold
allowDictation
com.apple.CoreSpotlight
com.apple.sociallayerd
currentPreset
file:///System/Library/PrivateFrameworks/DataMigration.framework/
checkMeEmailAvailabilityUrl
WFMatchTextGetGroupIntent
/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex
platformChromeFillLight
https://gspe21-ssl.ls.apple.com/attributionsearch/button-tripadvisor-logo-5.png
AMSSharedStoreReviewMetrics-com.apple.mobilesafari
_CFBT_.3.1_9c7zcipfrc_558001.espresso.net
CN
com.apple.UIKit/C//*/L
com.apple.coresymbolicationd
fc-sw-5.dat
com.apple.control-center.VoiceMemosModule
OrientationLockModule
ZCLOUDRELATIONSHIPSTATELOCAL
com.apple.Preferences/C//*/L
Z_3REMOTEPARTICIPANTHANDLES
activityDescriptorsWithError:
Data
com.apple.icloud-container.com.apple.mediasetupd
captionWidgetFadeInDuration
com.apple.news.articleViewing
ZNEEDSLOCALDELETE
ATXUserEducationSuggestionExploreFacesServer_tryAgainIntervalSeconds
unexpected error decoding FileSecurity
asynchronousRenderMaxAPL
CloudMasterMediaMetadata
BatchMetadata
CMCaptureCore
Configured Name
com.apple.posterboardservices.data-store.accessSwitcherFocusConfiguration
powerLogStatus
VideoRoutingCorner-j71.ca/
md-profile-authorize
kAXSupportsAdvancedDisplayFiltersPreference
^com.apple.Retail$
previewUpdateDate
https://uts-api.itunes.apple.com/uts/v2/browse/channel/{brandId}
writing to another user's preferences requires sufficient permissions to write to the file
https://itunes.apple.com/WebObjects/MZStoreServices.woa/wa/libraryLink
switchControlLaunchRecipeUUID
kMTUPPTransitionContextUPPDomainVersionKey
elen
globalCookieCleanup
_subscriptionsToSave
platformStrokeThinDark.descendantstyleset
38.migrator.sqlite
home-cb-internal
osservice<com.apple.followupd>
x-apple-application-site
registerForStateUpdatesWithRequestDetails:completionHandler:
PinchCPDark.ca/
file:///System/Library/PrivateFrameworks/NanoUniverse.framework/
previewedPattern
Message Attachment
oc
com.apple.springboard.SpringBoardDiagnosticExtension
com.apple.siri.sp.mitigation
com.apple.medialibraryd
CFDateComponentsSetCalendar
_stringTableFromCacheSatisfyingRequest
plist on disk is invalid
grb
ZCOMPLETE
_CFBT_.rtlib
_oset_enumerateObjectsWithOptionsUsingBlock
gear11@2x.png
ampMusicAPIHost
TextToSpeech
Continuity.loctable
VNPersonSegmentationGeneratorInstanceBased4People
odt_1_2.dat
com.apple.CarPlayUIServices
_DKDataModel22.mom
%s: Immutable character set passed to mutable function
-[__NSSetI getObjects:count:]
_ZORIGIN
cj_quant.espresso.weights
https://gspe21-ssl.ls.apple.com/attributionsearch/button-tabelog-1@3x.png
PFL.AppleMediaDiscovery.ASLExperimental:Metadata
https://gspe21-ssl.ls.apple.com/attributionsearch/button-pagesjaunes-2.png
Camera Recording Management
https://uts-api.itunes.apple.com/uts/v3/channels/{channelId}
org.openoffice.text
com.apple.locationd.userprofile
NSGetSizeAndAlignment(): unsupported type encoding spec '%c' at '%s' in '%s'
speaker.bluetooth.fill.rtl
AGXDeviceUserClient
standardNumberOfTopAssetRows
HWLayoutGroups.plist
-[NSOrderedSet enumerateObjectsWithOptions:usingBlock:]
headerGradientHeight
_CDEntityMetadataKey__bestLanguage
AXPhonemes
HighPhotoQualitySupported
com.apple.private.amfi.set-csp
__clampToRect
managed/com.apple.siri.cdm/kCFPreferencesAnyUser
com.apple.Batteries.BatteriesWidgetIntentsExtension
AppStoreFoundation
gk-invitation-break-before-make-timeout
WirelessBoardSnum
com.apple.pay.finance
ZEXTENDEDCOUNT
JCOP6.5 R19.3  R
LoadingPlaceholder_27.00
com.apple.developer.payment-pass-provisioning
/System/Library/PrivateFrameworks/AppleSRP.framework
^/webobjects/lzdirectory.woa/wa/
_DKShareSheetSuggestLessFeedbackMetadataKey__derivedIntentIdentifier
__ZoomServices
DidFixExcludedFromBackupFlagsV3
_DKApplicationActivityMetadataKey__contentDescription
modify-assertion
SpotlightServices.loctable
microphoneNotAccessible
OneHotEncoding
AXWordDescriptionsData_zh.momd
_colorcubeopaque_extend
failure to grow array
PFL.Budget.AppleMediaDiscovery.ASLArcadeRanking:Metadata
com.apple.Music.Messages
AVCaptureSessionPresetHigh60
file:///System/Library/Audio/UISounds/Swish.caf
approximateLongitude
_shouldSkipPCSRetryBehavior
character.bubble.he
Climate Sensor
com.apple.gpsd
ranSoundMigrator13.0
UnsendMessages
/System/Library/Frameworks/Combine.framework
com.apple.health.Heart
WindDownReminderCategory
enableDaysEffect
com.apple.telephonyutilities.callservicesdaemon.callprovidermanager
MultiKeySet
AppMediaUsage
CDMQRRequestCommand
com.apple.ControlCenterServices
https://gspe21-ssl.ls.apple.com/attributionsearch/maps-yandex-alt-3@3x.png
Z_DKMETADATAHOMEAPPVIEW__VIEWINFORMATION
max-hls-ratio
allowEraseContentAndSettings
com.apple.sharing.RemoteInteractionSession
arrow.2.circlepath.circle.fill
phone.arrow.up.right.fill
textexpanderalias
Ticketed Event
assistiveTouchMouseZoomPanningStyle
_FAFamilyCircleRequestConnectionProvider
_CFBT_.strings
wln
twoStageModelEngagementResult
ZATTACHMENT
ZGEOMAPREGION
SKProductPageExtensionSupportedItemKinds
com.apple.private.MobileContainerManager.unrestrictedPersona
getAppActionsForModeIdentifier:withRequestDetails:completionHandler:
_ci_to_rg16_as_bgra8
wa
Model.momd/
item.title_order_section
https://dzc-metrics.mzstatic.com/WebObjects/DZC.woa/wa/reportBrowse
duckingFadeDuration
DayOfWeekConditionedProbabilityAcrossAllBucketsInTheLastMonth
MobileBackup
/System/Library/PrivateFrameworks/AppSupportUI.framework/AppSupportUI
AIFF-C hang
com.apple.NanoCalendar
transitionSpringDamping
dayGroupAssetsCount
hourglass.end
ZPAYMENTMETHODS
com.apple.security.ts.asset-access
speaker.bluetooth
stroke_classification.codemap
default_factors_1280.pb
RespiratoryHealth
x-maps-bulletin
com.apple.posterboardservices.data-store
_ci_write_block_h
CarPlayWallpaper
Delta-en_NZ.idx
managed/com.apple.stocks2/kCFPreferencesAnyUser
file:///System/Library/Frameworks/AVKit.framework/
VNCoreMLRequest
com.apple.AppC3D
reservedSeat
item.composer_order_section
divide:by:
_NSURLIsCompressedKey
com.apple.DataAccess.BehaviorOptions/C//*/L
CKOperationCallbacks
1519034860
file:///System/Library/PrivateFrameworks/EmojiKit.framework/
https://gspe21-ssl.ls.apple.com/attributionsearch/snippet-winnie-logo-1@3x.png
_NSURLVolumeIsCDKey
CFBundleGetDevelopmentRegion
http://apps.identrust.com/roots/dstrootcax3.p7c
com.apple.appResume.freezerRecommendations
setAssetURL:
sign-sap-request
shared-channels-disabled
/Library/Preferences/com.apple.mediaremote.plist
targetBundleIDInConsequent
com.chargepoint
inAppSubStatus
ATTrackingEnforcementManager
setRepresentativeSong:
file:///System/Library/PrivateFrameworks/ARKitFoundation.framework/
*** %s: date2 cannot be nil\nFuture exception.\nA few of these errors are going to be reported with this complaint, then further violations will simply be ignored.\nHere is the backtrace where this occurred this time (some frames may be mis
SupportsRegistration
/System/Library/PrivateFrameworks/PersonaUI.framework/PersonaUI
com.apple.CertInfo
_CFBT_.4_sa1.4_ae1.4_r9_opt_int8_pca256.pcadata
com.apple.chronod.nextScheduledTimelineRefresh
%@%ld : %@ (%ld)\n
ICSERootViewController
com.apple.VoiceMemos.VoiceMemosShareExtension
lossEndMachContinuousTimestamp
http://hl7.org/fhir/medication-order-status
public.heics
file:///System/Library/PrivateFrameworks/AuthKitUI.framework/
setShortTitle:
context.keyPath./ids/app/foregroundServices.0
droppedPinFloorOrdinal
com.apple.Home.CompactControlCenter
defaultBackdropScaleAdjustment
PLUnknownImage@3x.png
ZLASTOPENEDDATE
Ruanda
Phrases-en_SG.dat
/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework
Preferences/
MapsUNCategoryPredictedDestination
numPreviousDaysToCheckForNotificationProblem
com.apple.mail.favorites
ConfigurationIntent.intentdefinition
_CFBT_.apple.WebKit.WebContent
com.apple.private.mis.online_auth_agent
com.apple.private.alloy.messagesquickswitch
com.apple.siri.morphun
WrappedBundle/Contents/_MASReceipt/receipt
paymentDateRange
file:///System/Library/PrivateFrameworks/StudyLog.framework/
MessagesDefaultIcon-27@2x.png
https://gspe21-ssl.ls.apple.com/attributionsearch/button-plugshare-1@2x.png
com.apple.appleaccount.beneficiary
MobileStorageMounter
Ukrainian-
token-service-enabled
arrow.right.arrow.left.square
_DKAudioMetadataKey__portType
Phoneme Data
com.apple.camera.CameraMessagesApp
com.apple.screen-recorder-services
file:///System/Library/ColorSync/Profiles/Display%20P3.icc
syndicationEnabled
kCKBrowserSelectionControllerVersionDictionaryKey
egenskapsliste
com.apple.Messages.StateRestoration
zero
<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE 
file:///usr/libexec/
CTNotifyUIService
auth-token-receipt-date
Start an ${isOpenEnded} ${workoutLocationType} ${workoutName} workout
kMDItemSubject=\"%@v*\"cwd
SoftwareUpdateCoreConnect
voiceOverExploreFocusAffectsNativeFocus
StoreDemoViewService
Encountered non-empty <false> on line %u
Faster Route
PhoneSceneDelegate
com.apple.backboardd.eventAuthenticationVerification
Progress.loctable
FuseSubscriptionStatus
com.apple.cdp.recovery
/System/Library/PrivateFrameworks/CMCapture.framework
managed/com.apple.AssistantServices/kCFPreferencesAnyUser
CollectionTransitItem
fc_has_edr_factor
_ci_to_YCbYCr_as_rg8
com.apple.FileCoordination
https://cn-smp-device.apple.com/broker
com.apple.multitasking.systemappassertions
_linearMapping
sharedLibrarySuggestions
ZCONFIDENCE
com.apple.backboardd.pointerPreferences
CallHistory 6.mom
English.lproj/
Jibbler.loctable
com.apple.private.alloy.location.motion
INNextFreshmintRefreshDateKey
pa_Latn.lproj/
ICAllowNotificationsViewController.loctable
SBSUIWindowSceneSessionRoleSystemNotes
com.apple.iohid
sign:%s 1st:%u 2nd:%u 3rd:%u 4th:%u 5th:%u
pairedAppIdentifier
/System/Library/Frameworks/HealthKit.framework/healthd
com.apple.shortcuts.background-running
PFL.PeopleSuggester.ProactiveShareSheetLighthousePFLPlugin:Metrics
suite/com.apple.AssistantServices/kCFPreferencesAnyUser
/System/Library/CoreServices/SystemVersion.plist
com.apple.LearnedFeatures
com.apple.private.alloy.amsaccountsync
file:///System/Library/PrivateFrameworks/CoreIDV.framework/
_PMSmartPowerNap
id-provision-ds-id
MobileGestaltHelper
com.apple.purplebuddy.budd.access
suite/com.apple.Metal/kCFPreferencesAnyUser
favoriteItem
emergency-20
inAppMessagesSerialCheck
AddingEmojiKeyboardHandled
Delta-en_ZA.idx
file:///System/Library/PrivateFrameworks/AutoLoop.framework/
epic_stage
paymentStatus
com.apple.nanonews.service.companion
//System/Library/LinguisticData//RequiredAssets_en.bundle
_DKBluetoothMonitor
_DKEvent.App.InFocus
/System/Library/PrivateFrameworks/VisualIntelligence.framework
CardGloss_Perforated_Horizontal_Mask@3x.png
simulateImportFailure
Photos Navigation URL
tg_Cyrl
EventInvitation.CouldBeJunk
DayOfWeekConditionedProbabilityAcrossAllBucketsInTheLast3Months
Memories Engaged Medium
en-gb-u-sd@sd=gbsct
com.apple.sharing.transfer-observer
marketingItemDynamicUIUrl
aspectFillAnimationStyle
SwiftNSCharacterSet
en-US-POSIX
com.apple.notes.analytics
hvfproject
PFL.Tips.TipsPFLPlugin:Metadata
showMusicAndColorGradeEditor
com.apple.networkextension.app-push
performSelectorInBackground:withObject:
RequestRide
AppIconMask@2x~iphone.png
com.apple.private.security.storage.News
file:///System/Library/Frameworks/OpenAL.framework/
@\"NSSet<__BKSHIDEventHitTestClientContext__>\"
agreements-uata.apple.com
libraryScopeShareState
SensorKitALSHelper
croatian
/usr/bin/defaults
.lproj
ffwd0 shape
FromServiceID
on_device_personalization
application/xml
cloudVerifiedType
Beekman_Localizable.loctable
BYODManualDomainSetupUrl
tk_Cyrl
@\"CHSTimelineReloadRequest\"
PrototypeToolsUI
TripleClickChoice
bottomCenterSecondaryToolbarWidth
Workflow_Private.intentdefinition
suite/com.apple.WebKit.WebContent.AppCacheDisabled/kCFPreferencesAnyUser
spotlightknowledged
GSAddition
App Clip Usage
ZL6BUSYGB3.com.apple.news.marketingnotificationextension
js-app-url
vehicleState
MACaptionVideoOverrideWindowColor
titleReferenceWidthPortrait
com.apple.textInput.keyboardServices.textReplacement
-[NSMutableOrderedSet unionSet:]
com.apple.mobile.user_preferences/UserSetLanguage
audio MPEG-4 protejat
Base.lproj/Messages.intentdefinition
fallbackImageCryptoTag
com.apple.private.cloudphotod.access
LSSupportedRegions
all-artist-images-map-url
keychain-cloud-circle
com.apple.diagnosticpipeline.tasking_invalidation_activity
com.apple.frontboard.launchapplications
com.apple.photos.service
NEW_MESSAGE_ACTION
Dynamically Registered chvc Video Decoder
com.apple.mt
INCancelWorkoutIntent
es_CO.lproj
com.apple.uikit.viewservice.com.apple.facetime
ZSESSIONIDENTIFIER
/System/Library/CoreServices/ServerVersion.plist
com.apple.system.clock_set
com.apple.proactive.PersonalizationPortrait.DecayedFeedbackCleanup
https://gspe21-ssl.ls.apple.com/attributionsearch/snippet-ipeen-logo-3.png
KeyboardServices
./ro.lproj/
cloudMultipleContributorsEnabled
ZCLUSTERREJECTED
browseWebLanding
allowCellularHDUploads
_CFBundleFlushBundleCaches
com.apple.TextInput.accessibility
_accordionMix
hapticmetrics_verbose
CID-editundomessage-learn-edit-a
CLSilo.Version
^one[.]apple[.]com$
_gradientNormalizeV1
<CFCharacterSet Predefined Punctuation Set>
hat
/System/Library/Frameworks/PhotosUI.framework/PhotosUI
com.apple.markup-private
/Applications/MobileSMS.app
com.apple.appconduitd.device-connection.connect.allow
bundle-owns-check
com.apple.protectedcloudstorage.protectedcloudkeysyncing
managed/com.apple.osanalytics/kCFPreferencesAnyUser
bootUUIDOnLastInit
file:///System/Library/AppPlaceholders/AppleTV.app/
AXWordDescriptionsData_zh.momd/
Access-Control-Expose-Headers
subscribed-container-background-refresh-secs
sortUsingComparator:
com.apple.powerlog.plxpclogger.xpc
Contact Identifier
face_validation_warp_4.dat
extensionsPendingDescriptorRefetch
_NSURLFileAllocatedSizeOfResourceForkKey
E+00
com.apple.xpc.amsaccountsd
com.apple.coreidv.idv-data
UIAccessibility
setArtistUploadedContent:
zh-Hans
VN4nFZhnOcBOiJmeVWzBWsv
PhotosEngagement2To3Seconds
com.apple.StreamingUnzipService
pfl:com.apple.AppleMediaDiscovery.ASLAppEmbedding:metadata:
blurEnabled
forceClassroomUnpromptedScreenObservation
j.square.fill.on.square.fill
com.apple.Trial.NamespaceDescriptor.890.plist
CDInteractionDataModel-6.mom
com.apple.DiagnosticsReporter
OPEN_RECENTS
ZCONVERSATION
Quantity
kCTCellMonitorUARFCN
ZCROPPINGQUADTOPLEFTX
rgbTransformMap_v1_Studio_NEAR_fp16_RGBAslice4
Workflow_Private.loctable
invalidateModeAssertionWithUUID
com.apple.private.coreservices.canmapbundleidtouuid
Shows and gets the current weather for the specified location.
WelcomeScreenDisclaimer.rtf
-[__NSArrayM removeObjectsInRange:]
com.apple.matter.support.xpc.device-pairing
ids-datachannels-maxbitrate-over-quick-relay
osservice<com.apple.mobiletimerd>
endTimeZoneOffset
HealthMenstrualCyclesNotificationContentExtension.NotificationViewController
suite/com.apple.keyboard.preferences/kCFPreferencesAnyUser
_ci_nearest
http://fdasis.nlm.nih.gov
quicknoteScene
com.apple.locationd.Mobility.ProcessBouts
<CFTree context %p>
-[NSOrderedSet indexesOfObjectsWithOptions:passingTest:]
ZPICKEDUPDATE
isLibraryAdded
variantWeight
ZIMPORTDATE
_grassAndSkyAdjust
_MPC_CLEAR_EVS
forceDateTimeMetadataBaking
kCFDateFormatterShortMonthSymbolsKey
CFSet
BoatReservation
FlashlightLevel
radiowaves.left
com.apple.private.homekit.allow-secure-access
_LSDirectoryClass
CFURLCreateFromFileSystemRepresentation failed to create URL for upwd->pw_dir value: %s
totalUnitCount
increase.indent
ConversationScene
/System/Library/Frameworks/_PhotosUI_SwiftUI.framework
com.apple.accessibility.PersonalAudio
documentMenuSettings
partiality-opt-out
com.apple.duetexpertd.logDigestGlobalNotificationFeedback
jg44aq9q
coex_sac.plist
getCollectionById
public.mpeg
NSForceRightToLeftLocalizedStrings
Invalid CFRelativeDateTimeFormattingContext
com.apple.SensorKit.speechEmotion.telephony
xcplaygroundpage
kern.osversion
com.apple.AppleIDSSOAuthentication
localCacheForMediaAnalysisRecipes
com.apple.trial.status.namespace-name.allow
file:///System/Library/PrivateFrameworks/CoreEmoji.framework/
Kernel resource shortage handling out-of-line memory
com.apple.linkd.registry
/usr/libexec/cloudpaird
com.apple.ind.xpc
_highlightsAndShadows2
paymentDate
OrderWebServiceLogEntry
com.apple.coordination.timers
io
com.apple.BarcodeSupport.BarcodeNotificationExtension2
.google.com.pe
_ZTARGET
Roman-Accent-[{
_NSURLCanSetHiddenExtensionKey
XML parser error:\n\t%@\nOld-style plist parser error:\n\t%@\n
SpecLength
dropInsertionAnimationSettings
NSMirageDescription
summaryCountShared
setMinimumBackgroundFetchInterval:
kCFDataURLTextEncodingName
ZISCAPTION
Base.lproj/TTRIReminderDetailRecurrenceEndTableViewController.storyboardc/
editorialUpdate
DriverApprovalState
ZZZZPackedAsset-3.0.0-gamut0
faceprintVersion
switchControlShouldAlwaysActivateKeyboardKeys
colorGradeEditorPreviewMode
testDefinitions~iphone.plist
suite/com.apple.itunesstored/kCFPreferencesCurrentUser
h63QSdBCiT/z0WU6rdQv6Q
file:///Applications/PeopleViewService.app/
loadDevicesUI
prewarmWithCompletion
setDontFetchFromServer:
com.apple.siri.tts.resource.pt_PT
setTvEpisode:
/System/Library/PrivateFrameworks/PhotosPlayer.framework/PhotosPlayer
com.apple.tips.TipsPFLPlugin
com.apple.private.activitykit.assertionRequester
BoundingPathData
isEdgeForJoin
conversionCohort
_ZNOTEUSINGTITLEFORNOTETITLE
MenstrualCyclesAppPlugin.BeforePeriodStart2Weeks
setRecordIDsToDeleteToEtags:
com.apple.announced:com.apple.announced
PFL.PeopleSuggester.ProactiveShareSheetLighthousePFLPlugin:Metadata
com.apple.ScreenTimeAgent.activity.fail-stuck-sent-messages
TrustResultNotAfter
1560383515
settingsAppStorageDetailsURL
com.apple.sharing.sharesheet
com.apple.ScreenTimeAgent.plist
_DKAppMediaUsageMetadataKey__mediaURL
com.microsoft.internet-shortcut
InternetAccounts
managed/com.apple.keyboard.preferences/kCFPreferencesAnyUser
NSURLVolumeLocalizedFormatDescriptionKey
-[NSMutableSet setSet:]
text.cursor.th
_CFBT_.json
com.apple.sysmond
com.apple.CMCapture.diagnosticextension
com.apple.private.tty.database
_lanczosUpH
com.apple.dasd.dailyPeriodicUtilityInactivityPlugin
Roman-Accent-%
cnn_human_pose_lite_v2.espresso.shape
available-software-updates-extended-reload-frequency-seconds
Software Update.loctable
oneUpSettings
sharingSuggestionsBannerUnreadCountThreshold
/Media/iTunes_Control/iTunes/
EMLStandard@2x~ipad.png
file:///System/Library/PrivateFrameworks/ScreenTimeCore.framework/
ZACTIVATIONDATE
com.apple.mlruntimed.xpc_activity-classaonbattery
public.geometry-definition-format
/uts/v3/siri/watchlist
_oset_getObjectsRange
compactName
allowed-anonymous-arcade-keys
(?:apps|tv|music)[.]apple[.]com(?:/\\w+/subscription/link)(?:[?]|$)
bplist00
de-
NSExtensionActivationDictionaryVersion
powerCostDL
prng_seedctl
com.apple.private.healthd.server-extended
com.apple.TTY/C//*/L
apple.bubble.middle.bottom
syncstatus.plist
243LU875E5
ShortSessionDataByAppID
/.file/id=%lld.%lld/%s%s
 %@
Device.Power.LowPowerMode
com.apple.accessibility.visual.alerts
setRecordLabel:
com.apple.backboardd.virtualDisplay
file:///System/Library/PrivateFrameworks/AppleSauce.framework/
com.apple.springboard.openurlswhenlocked
cloudBatchID
Z_DKSHARESHEETSUGGESTIONMETADATAKEY__DERIVEDINTENTIDENTIFIER
com.apple.private.MobileGestalt.AllowedProtectedKeys
@?<v@?@\"DNDModeConfiguration\"@\"NSError\">
NSStringFormatLocaleKey
multicolor-0:systemYellowColor
TvAppViaQueryParam
createAndRegisterAppleIdBaseUrl
Z_DKBLUETOOTHMETADATAKEY__NAME
com.apple.avfoundation.videoperformancehud
locationd.loctable
seh-
/System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
com.apple.FeatureFlagsSupport
_CFBT_.lproj
com.apple.ClipServices
com.apple.control-center.CameraModule
CoreGlyphsPrivate
ManualBootstrap
endingAirDate
ZCOUNTER
com.apple.GameCenterUI.GameCenterDashboardExtension
setNumber:
com.apple.nanoprefsyncd
/var/mobile/Media/Downloads/
managed/com.apple.demo-settings/kCFPreferencesAnyUser
rectangle.righthalf.inset.fill.arrow.right
pronunciationHint
paidBadgeEnabledForPaidUsers
https://uts-api.itunes.apple.com/uts/v3/sports/{sportId}
cursorInteractionSettings
com.apple.siri.tts.resource.ja_JP
no
/Library/Caches/Configuration/remote-configuration
com.apple.networkextension.dns-proxy
file:///Applications/ClarityCamera.app/
AlwaysLoggedIn
ZCUSTOMERFAMILYNAME
com.apple.AppStoreDaemon
ZGLOBALKEYVALUE
com.apple.transparencyd.dutycycle
com.apple.sleepd
Choose a Symbol
com.apple.MobileAsset.LanguageDetectorAssets
/System/Library/PrivateFrameworks/MobileSafari.framework
iTunesBrand
com.apple.private.alloy.keysharing
Payment_Localizable-A222.loctable
%@-%@~%@%@%@
/Remote
com.apple.findmy.FindMyNotificationsContentExtension
wishlist-event-url
_internal_material@2x.png
_DKSearchFeedbackMetadataKey__interactionType
health insurance
https://gspe21-ssl.ls.apple.com/attributionsearch/button-tiqets-1.png
ZGROUPINGIDENTIFIER
VideoMinIntegrationTime
performSelectorOnMainThread:withObject:waitUntilDone:
Centimeters
contentEpisodes
/Library/Caches/com.apple.MapsSupport/
decomposedMessage
Chinese
ListeningModeNoiseCancellation.ca
_ZDEFAULTSTORE
Punctuation
MTCoreSpotlightDataHasBeenIndexed_v2
drawableAvailable
ZISMARKEDASCOMPLETE
apple.cash.circle.fill
languagesSupported
p2-launch-ebookstore-host-patterns
/System/Library/PrivateFrameworks/AssetCacheServices.framework
managed/com.apple.Home.ControlCenter/kCFPreferencesAnyUser
unnamedFaceCount
public.mp2
*** %s: marker cannot be nil
Encountered non-empty <true> on line %u
isExportHUDEnabled
com.microsoft.excel.xla
1272422144
Volume Control Type
Control home
ZCOUNTRYCODE
https://play.itunes.apple.com/WebObjects/MZPlay.woa/wa/subPlaybackDispatch
gsw-
PluralLocalizable.loctable
com.apple.springboard.launchapplications
com.apple.coreidvd.digital-presentment.firstpartyclient
EnableSafariTopHitsLogic
isLessThanOrEqualTo:
/System/Library/Frameworks/Speech.framework/Speech
file:///System/Library/Frameworks/JavaScriptCore.framework/
lowConfidenceRuleCount
configurations
ojg
com.apple.avfoundation.avcapturedevice.built-in_video:0
fsr-keys-url
com.apple.coreauthd
35.migrator.sqlite
geoClassificationInfoPath
System.RideVehicle
Senders Operator
updateWithSettingsDiff
licensePlate
sgi
client-%d-secondary
gug
/System/Library/PrivateFrameworks/SiriTTSService.framework
ZLOCATIONDATA
file:///System/Library/PrivateFrameworks/VisualIntelligence.framework/
usw2-ondevice-agreements.apple.com
film MPEG-4
timelineSchedulerMode
MobileLockdown
Goal Unit Type
forceSaliency
managed/com.apple.lookup.shared/kCFPreferencesAnyUser
/System/Library/LocationBundles/AppGenius.bundle
aspectRatioForCompactLandscapeYears
com.apple.security.device.usb
com.apple.financed
SetupVersion
SBDemoRole
https://gspe21-ssl.ls.apple.com/attributionsearch/snippet-menufy-logo-1@3x.png
com.apple.Dataclass.Availability
_CFBundleCopyFrameworkURLForExecutablePath
com.apple.proactive.ProactiveHarvesting.Cleanup
Z_27ALBUMS
askToBuyUpsellPage
com.apple.private.healthkit.obliteration
file:///System/Library/PrivateFrameworks/CoreLocationReplay.framework/
Access-Control-Allow-Methods
stabilizeLivePhotos
AVFoundation
com.apple.Jet
Bus Trip Reservation
ZEXTERNALSEQUENCENUMBER
com.apple.BatteryCenter.BatteryWidget/C//*/L
allowShowingUndownloadedTV
MobilityAppPlugin.WalkingSteadinessRepeat.Low
/System/Library/PrivateFrameworks/AppConduit.framework/AppConduit
mobileCatalogUpdatePeriodSeconds
com.apple.ScreenReaderCore
https://gspe21-ssl.ls.apple.com/attributionsearch/snippet-dimmi-logo-3@2x.png
FindMyLocationChange
PersonSearch
/System/Library/CoreImage/CIBarcode.cifilter/CIBarcode
digitalZoomRatio
com.apple.private.ids.messaging.urgent-priority
/System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
/photos/livePhotos/longExposure
file:///System/Library/PrivateFrameworks/CTCarrierSpace.framework/
NSTaggedPointerString cannot be allocated
Payment_MaestroCardLogo@2x.png
/inApps/v1/inAppRegrantPurchaseHistory
*** %@: method sent to an uninitialized FileSecurity object
ZHISTTXRETRANS
com.apple.ClarityCamera
INIntentParameterRelationshipParentName
additionalContentThreshold
-[NSArray objectsWithOptions:passingTest:]
newArrayWithObjects:count:
<CFString %p [%p]>{contents = \"%@\"}
com.apple.private.FairPlayIOKitUserClient.access
file:///System/Library/Frameworks/MetalPerformanceShaders.framework/
com.apple.NPKCompanionAgent.client
deliverActiveModeAssertion
performSelector:onThread:withObject:waitUntilDone:modes:
CFBurstTrieCursorCreateByCopy
com.apple.private.ac
com.apple.EN.UserNotification
_DKMetadataHomeKitAccessoryControl__characteristicType
/System/Library/PrivateFrameworks/MobileInstallation.framework
com.apple.siri.SiriTTSService
file:///System/Library/Frameworks/HomeKit.framework/
com.apple.voiceservices.diagnosticextension
WebObjects/MZFinance.woa/.*(useCommerceApp=true)
L-BulletinAccessoryBell@2x.png
image/avci
com.apple.siri.tts.voice.it_IT.francesca.neural.premium
com.apple.idcredd.mafetch
_smartBlackAndWhite
+0.0
Contents %p\n
RTTUtilities
AppIcon-Small@2x
getStateDumpWithRequestDetails
suite/com.apple.bluetooth/kCFPreferencesAnyUser
dismissedCameraUpgradeOfferBanner
_CFBT_.apple.coreduet.systemevents.plist
com.apple.mobilesafari.shortcut.openReadingListView
p2-u.itunes.apple.com
/System/Library/PrivateFrameworks/Message.framework
file:///System/Library/PrivateFrameworks/MobileTimer.framework/
com.apple.private.alloy.siri.location
EntityResolution
dtb
com.apple.ManagedSettingsAgent
ZDEVICEIDENTIFIER
EKDirectorySearchResultSet
com.apple.private.mobile_storage.allowedSPI
backdropScale
com.apple.share-services-discovery
_internal_harmony@1x.png
Err260.duv
com.apple.seld.tsmamnager
ZICSERVERCHANGETOKEN
managed/com.apple.Synapse/kCFPreferencesAnyUser
ZORDERPAYMENTSUMMARYITEM
NanoIconMaskChiclet-27.5@2x.png
com.apple.MapsSupport
8.migrator.sqlite
managed/com.apple.assistant.support/kCFPreferencesAnyUser
com.apple.GSS
TTRIDebugMenuViewController.loctable
/System/Library/PrivateFrameworks/PhotoFoundation.framework
LastIndexTidAlreadySetUp
kCLConnectionMessageSignificantLocationChange
VNDetectFaceGazeRequest
file:///System/Library/Frameworks/MetalKit.framework/
https://idmsac-qa1.corp.apple.com/IDMSWebAuth/
cnn_moflow.espresso.weights
camera.rotate
assistiveTouchMouseAlwaysShowSoftwareKeyboardEnabled
aze
com.apple.dasd.widgetBudgetReset
com.apple.aprs.FreezerModelUpdate
allowMailPrivacyProtection
kTCCServiceSystemPolicyDocumentsFolder
root.home.dismissedNaturalLightingOnboarding
ZLAUNCHURL
TopHitsThreshold
ZTRANSITLINESTORAGE
legacyFaces
attributionLabel
_CFBT_.r14.l3.espresso.shape
/System/Library/PrivateFrameworks/LearnedFeatures.framework
_client_exclusive
__NSVariableWidthString
ALLOW_WPA2_PSK
/System/Library/PrivateFrameworks/TemplateKit.framework
com.apple.EmailFoundation
PSDocumentsPolicy.loctable
com.apple.posterboardservices.data-store.refreshConfigurations
FBSWorkspaceServiceClientInterface
RTITextOperations
com.apple.VIDEO
CAProcessCanAccessGPU
ZPACKEDACCEPTABLECROPRECT
forceWristDetect
localeIdentifier
roman-latin1
com.apple.news.notification_receipt_event_user_data
circles.hexagonpath
com.apple.CMCaptureCore
MenstrualCyclesAppPlugin.BeforePeriodStart5Days
SentenceCorrection
NoteDataOld.momd/
Track your next upcoming event.
ty
line.horizontal.3.circle.fill
photos-migrate-iphoto
ZSHIPPEDDATE
com.apple.iBooks.BooksNotificationContentExtension
https://cl2-cn.apple.com/6/v1
Expected terminating '>' for data at line %d
ben
http://hl7.org/fhir/ValueSet/immunization-status
.google.co.vi
com.apple.dasd.dock.persistence
ZSERVERSIDEUPDATETASKLASTATTEMPTEDBUILD
com.apple.frontboard.shutdown
/uts/v3/user/settings
1120208127
com.apple.Safari.Core
com.apple.corespeech.corespeechd.ssv.service
hairColorType
gear20@3x.png
com.apple.-AppIntents-SwiftUI
imagine GIF
com.apple.DiagnosticsService.Diagnostic-4276
com.apple.uikitservices.userInterfaceStyleMode/A//B/L
vc-always-on-audio-redundancy-enable-threshold
com.apple.MediaPlayer
IDXIndexDataFields
simulatedAuthenticationType
HeroCard_Discover@3x.png
default.pipelinelib
rapport-friend-keys-initial-delay
circle.grid.cross.up.fill
Validation Expiration
Target Heater-Cooler State
HKDatabaseChangesQueryClientInterface
access-moments
com.apple.rootless.storage.sensorkit
setHomeSharingAsset:
nep
vc-ab-test-rate-control-enhancement-feature-combinations
_boostHybrid
allowsTextSelection
ZMAPSTOKENTTL
LocalizedStrings
UI-NumberPad-8
com.apple.mobilemail.services.xpc
thai
<CFMachPort context %p>
Unknown character '%c' (0x%x) in <integer> on line %u
com.apple.MobileAsset.MobileAssetBrain
dayGroupSummaryAssetsCountShared
setObservesDeferringResolutions
SafariFoundation
ZPREFERREDBACKGROUNDTYPE
memoryFeatureWeight1
PFL.QuickTypeDESPlugin.CNN:Metrics
com.apple.icloud-container.com.apple.sociallayerd
cart.fill.badge.plus
NSRegulatoryPrivacyDisclosureSummary
sb_blur_notch@2x.png
http://hl7.org/fhir/quantity-comparator
outgoingMessageType
assetTrackProperty_QuickTimeMetadata
file:///Applications/ScreenshotServicesService.app/
MemoriesEngagedMedium
AXSDSettings
cos
capacitySystem
_ci_swizzle_LA
com.apple.frontboard.system-service
suite/com.apple.Music/kCFPreferencesAnyUser
gear23@2x.png
com.apple.frontboard.systemappservices
TTRIListSharingParticipantCell.nib
com.apple.KeyValueService.Production.Private.user-requested-backup
/uts/v2/watchlist/continueWatching
NSStringLocalizedFormatKey
PFL.Budget.ReminderKit.REMMLTitleListTagMatcher:Metadata
NTKMotionFaceBundle
StageMonoV2.scube
MFP_CAPABLE
https://gspe21-ssl.ls.apple.com/attributionsearch/button-heroldat-1@2x.png
com.apple.CheckerBoard
*** CFHash() called with NULL ***
/System/Library/PrivateFrameworks/BulletinBoard.framework/BulletinBoard
credentialIdentifier
touchAccommodationsUsageConfirmed
com.apple.fitcore.session
RTCSecureHierarchyToken
/Library/HTTPStorages/com.apple.MapsSupport/
feedConfiguration_143441
:com.apple.health.view.sharing
com.apple.atc.xpc.runkeeplocaltask
NSIndirectTaggedPointerString cannot be allocated
Media Item Type
managed/com.apple.SOS/kCFPreferencesCurrentUser
nptocompaniond
comgooglewallet
file:///System/Library/PrivateFrameworks/SpringBoardUIServices.framework/
bm-
pleasantPerspectiveScore
freeBadgeEnabledForPaidUsers
$(PRODUCT_NAME)
CID-accessibility-collection
a.book.closed.fill
/System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth
$(D
com.apple.mobilesafari/C//*/L
com.apple.WebKit.WebAuthn
Supported Audio Recording Configuration
NSURLContentTypeKey
com.apple.OfficeImport.OfficeSpotlightImporter
com.apple.corelocation.precaching.NPLOI7
com.apple.private.push-to-wake
com.phaseone.raw-image
ZRESOURCEDATA
/System/Library/PrivateFrameworks/EmojiFoundation.framework
DAEGrantedDelegatesListContext
com.apple.Accessibility.SwitchControl
MPModelPlaybackPosition
album.date_played_local
/System/Library/PrivateFrameworks/CoreDuetContext.framework
ipad.homebutton
Memories the users spent 0-5s viewing
daftar properti
setHLSKeyCertificateURL:
com.apple.AssetCacheLocatorService
wallet:accountRemoved
storeplatform-lookup-url-unpersonalized
Based on time and location
wallet:expressPassInfoChanged
alternatives
com.apple.passd
http://crl3.digicert.com/Omniroot2025.crl
NanoDefaultIcon-50.0@2x.png
suite/com.apple.Accessibility/kCFPreferencesCurrentUser
Siri Input Type
recurrenceRule
file:///Applications/MobileSlideShow.app/PlugIns/PhotosFileProvider.appex/
qp_blocklist.bundle
MedicationsHealthAppPlugin
com.apple.audio.AppleTimeSyncAudioClock
ConfigSystemVersion
SGDSuggestManagerMessagesProtocol
cr_tr_model_v1.mlmodelc.bundle/
Break on __THE_PROCESS_HAS_FORKED_AND_YOU_CANNOT_USE_THIS_COREFOUNDATION_FUNCTIONALITY___YOU_MUST_EXEC__() to debug.\n
com.apple.notify.root_access
shareSheetLinkTotalFileSizeThresholdMB
suite/com.apple.weather.sensitive/kCFPreferencesAnyUser
com.apple.mobileslideshow.memory
Contact Event Trigger
ZHIGHLIGHT
com.apple.ShazamNotifications.category.actionable
Negative buffer length passed to CFDataReplaceBytes
vc-vcrc-faceTime-experiment-experimentConfig
beats_sound_anc.wav
customDomainEnabled
System.SpatialEvent
file:///System/Library/PrivateFrameworks/PhoneNumbers.framework/
localVersionDate
com.apple.poweruiagent.audioAccessoriesDailyMetrics
iPhone-Landscape
MessagesBadgeIconMask-32.0@2x.png
MFPreviewViewController
ZDAYGROUPASSETSCOUNT
com.apple.notes.newNote
com.apple.bluetoooth.CBMetrics
CIPhotoEffect3DSilverplate.scube
/System/Library/Frameworks/SensorKit.framework
QLUTIAnalyzer
com.apple.private.allow-external-storage
com.apple.icloud-container.clouddocs.com.apple.CloudDocs
file:///Applications/SIMSetupUIService.app/
https://gspe21-ssl.ls.apple.com/attributionsearch/snippet-evsmart-logo-1@3x.png
com.apple.private.rsr-cryptex-access
PersonUUIDSetConditionedProbabilityAcrossAllCandidatesInTheLast3Months
ZUUIDHASH
ctc_latn.bundle/
rgbTransformMap_Contour_NEAR_fp16_RGBAslice11
com.apple.HID
PFSceneTaxonomyData_84.bz2
com.apple.mobilemail.MailSpotlightIndexExtension
Track an order.
:com.apple.health.view.category
https://gspe21-ssl.ls.apple.com/attributionsearch/button-evgo-1@3x.png
PFL.AppleMediaDiscovery.ASLExperimental:Results
Launch Storyboard.storyboardc
CIPassThroughGeneralFilter
VIAnalytics
merge sort - count/elementSize overflow
com.apple.sportsd.session.xpc
tl
setHasBeenPlayed:
rgbTransformMap_v1_Studio_FAR_fp16_RGBAslice10
com.apple.MobileAccessoryUpdater
/System/Library/Frameworks/GameController.framework/GameController
-[__NSFrozenSetM countByEnumeratingWithState:objects:count:]
ja_JP
HAENKnownAccessoryExpiryDays
printer.fill.and.paper.fill
callbackInterval
_pixellate
NSURLVolumeIsEncryptedKey
core-seed-name
/System/Library/PrivateFrameworks/PrivacyAccounting.framework
CloudConfigurationUIComplete
UIApplicationShortcutItemType
EmptyClass
magnetometer
com.apple.DiagnosticExtensions.BluetoothHeadset
editingButtonDark.materialrecipe
_AXNotification_TTYShouldBeRealtimePreference
suite/com.apple.WebKit.WebContent/kCFPreferencesCurrentUser
PFL.ReminderKit.REMMLTitleListTagMatcher:Results
sr-
com.apple.security.ts.nano-preference.read-write
com.apple.BTServer.allowRestrictedServices
sharedLibraryDataSourceType
ZAUTOMATICARCHIVINGDATE
com.apple.proactive.PersonalizationPortrait
NWParameters
PhotosEngagement0To1Seconds
URLFormatting
file:///System/Library/PrivateFrameworks/InstallCoordination.framework/
x3d
rectangle.on.rectangle.fill
lastFetchedDate
cancelPreorderItemsSrv
ZRECIPIENTGIVENNAME
Assets that have been cropped in the edit tool
bih
com.apple.iCloudQuotaUI.remote-extension
/System/Library/PrivateFrameworks/JetPack.framework
Z_DKMICROLOCATIONMETADATAKEY__DOMAIN
modeIdentifier
_CFBT_.precompilation_info
/System/Library/Frameworks/CoreText.framework
allowsResponse
managed/com.apple.newscore/kCFPreferencesAnyUser
request_delay_range_limit_seconds
com.apple.MediaSocial
Unicode (UTF-7)
ArtworkDeviceIdiom
CourierNewPSMT
/System/Library/PrivateFrameworks/NetAppsUtilities.framework
com.canon.cr2-raw-image
<CFTree %p [%p]>{children = %lu, context = %@}
com.apple.tv.bulletins.explicit
com.apple.texttospeech
StillImageCaptureNowAfterAutofocusTimeout
Gujarati.lm/
backgroundassets.user
PSGShouldShowMatter
    selector = %s\n
getPlayablesForContent
dateWeight3
AXPhonetics/
com.apple.Safari
CompassCalibrationViewService
MM
com.apple.AppSupport/C//*/L
IsInAMeeting
_CFBT_.wav
recordTypeForRedialing
file:///System/Library/ColorSync/Profiles/ITU-2100-HLG.icc
AIFF-C-ljud
com.apple.DataDeliveryServices
header->_flags & __CFURLHasHost
_ZCHANNEL
https://gspe21-ssl.ls.apple.com/attributionsearch/button-thefork-2@2x.png
secondaryToolbarAlwaysVisible
mr_IN
KeybagLockState
ZTITLELOCALE
vc-profile-edit-page
_vividLightBlendMode
file:///Applications/PosterBoard.app/
vi-
Start a ${type} timer for ${duration}
com.apple.searchd/A//B/L
com.apple.CFURL.magic
%@: invalid archive (invalid dictionary)
com.apple.dt.remotepairing.rollexpiredpairings
com.apple.photo.NeutrinoCore
intrusiveObjectPresenceScore
com.apple.healthd.healthrecords.HDHealthRecordsAPIReminderRegistry-FirstUnlock
-[NSMutableArray insertObjectsFromSet:atIndex:]
exposureBleedTransitionCueAlignment
SecErrorMessages.loctable
nl_NL.plist
file:///System/Library/PrivateFrameworks/FTServices.framework/
allowInAppPurchases
etel
@\"SBSDebugActiveWidgetInfo\"
com.apple.security.system-groups
com.apple.security.ts.nano-preference.read-only
desiredKeys
_cubicDownsample2v
SystemPaper.loctable
_UIBackdropViewSettingsSemiLight
ZCACHEDUSERREVIEW
tahoma_searchlanding
CDMRepetitionDetectionRequestCommand
void CFDictionaryAddValue(CFMutableDictionaryRef, const void *, const void *)
sw-
com.apple.private.healthkit.zeppelin
ServerSuggestionThreshold
http://www.whocc.no/atc
/var/mobile/Library/Weather/countrycodes.db
deletePlaceholder
com.apple.suggestd.process-pending-geocodes
MapsUNCategoryRAP
promotesFramebuffer
FinanceKit_Localizable.loctable
/System/Library/PrivateFrameworks/FSEvents.framework
Apple News Spotlight
safarifetcherd
View Most Recent Call
ZCLOUDRELATIONSHIPSTATE
FeatureChangeObserver
customFeatures
memoryFeatureWeight4
file:///System/Library/PrivateFrameworks/SafariShared.framework/
individual
de-1996
com.apple.news.private.secure.demo2
SGAssetIdentifier
SpringBoard.loctable
NanoDefaultIcon-24.0@2x.png
limitKeyAssetAspectRatioToFeedCard
/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal
__NSTaggedDate_new
/System/Library/PrivateFrameworks/SocialLayer.framework
1328318286
-[__NSSingleObjectArrayI countByEnumeratingWithState:objects:count:]
kr
ZALBUMLIST
file:///System/Library/Frameworks/AppTrackingTransparency.framework/
Roman-Accent-7&
More actions
com.apple.CloudDocs.iCloudDriveFileProvider.apple-extension-service
songDownloadDone
CharacterRecognitionAttributes
abs-enable
/usr/libexec/promotedcontentd
_DKLocationMetadataKey__latitude
MOVE_ONE_NORMAL_ITEM_TITLE
com.apple.NetworkServiceProxyFramework
DayOfWeekConditionedProbabilityAcrossAllBucketsInTheLast6Months
com.apple.media-group.media-system
group.com.apple.pommes
kal
bootwatchd-shim
LastKnownReindexReasons
pleasantCompositionScore
_CFBT_.5.espresso.net
(CFMachPort) %s
com.apple.uikit.Artwork
WorldClockWidget
com.apple.email.maild:com.apple.email.maild
file:///System/Library/Frameworks/Accelerate.framework/
AMSCleanedUpUserDefaultsDataAfterMigrationToStorage
showFloatingBanner
kt-disabled
WrappedBundle
suite/com.apple.messages.nicknames/kCFPreferencesAnyUser
0:^https://.*-?buy[.]itunes[.]apple[.]com.*/offers/device($|[?].*)
animationDuration
/System/Library/PrivateFrameworks/Heimdal.framework/Heimdal
com.apple.powerui.smartcharging
com.apple.imdmessageservices.IMDMessageServicesAgent
context.keyPath./app/inFocus.0
sourceItemsCount == 1
usesTiledLayers
com.apple.CredentialSharingService.ShareableCredentialsMessagesExtension
hu-
/Applications/Preferences.app/Preferences/
NSCKHistoryAnalyzerState
systemgroup.com.apple.configurationprofiles
com.apple.assetsd.periodicmaintenance
^/webobjects/mzstore.woa/wa/(viewradiomain|viewplaylist|viewactivity|viewbrand)
HMDAppleMediaAccessoryShouldOverrideRepeatScanningIntervals
com.apple.siri.tts.voice.en_GB.martha.gryphon.premium
plus.rectangle.fill.on.rectangle.fill
DefaultIcon-60@2x~iphone.png
MTCoreDataMigrationVersion
-[NSArray arrayByExcludingToObjectsInArray:]
RealityDevice
ZORIGINALFILESIZE
enableViewRenderer
com.apple.differentialprivacy.thirdEnhancedPrivacyBudgetTestKey
_ZMONTHKEYASSETPRIVATE
file:///System/Library/PrivateFrameworks/CoreODI.framework/
lineItemObjects
Setup Data Stream Transport
com.apple.sidecar.extension.capture
PFL.Budget.Photos.PhotosDESPlugin.Large:Metadata
mobileassetd
lifeInsurance
com.apple.news.magazineSections
rgbTransformMap_Studio_NEAR_fp16_RGBAslice10
CNUIIdentityAvatarConfiguration.json
fr_CH.lproj
file:///System/Library/Accounts/ServiceOwners/GCCloudServiceOwner.bundle/
suite/com.apple.private.health.respiratory/kCFPreferencesCurrentUser
com.apple.pf.allow
AVFigRemoteRouteDiscovererFactory
MACaptionFontSmallCapital
AudioRoutingControl-Light.ca/
minItemSize
AppIdentifier
DefaultIcon-29@2x.png
lookup-url
itms-appss
/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
LowLightVideoCaptureSupported
com.apple.mediastream
it_IT-phrase-to-emojis.plist
SIRI_DATA_INTEGRATION_TEST2
com.apple.weathercore
streamName
fetchContentObstructionBoundsForPosterConfiguration:orientation:completion:
MonzaV4_1.mlmodelc/
com.apple.mediaparserd
U -> <i>^<i>
Lista de propiedades
std_vert1_lph
ArtworkDisplayGamut
file:///Applications/FunCameraEmojiStickers.app/
com.apple.rapport
DediscoDirectUploadTest
gaxInternalSettingsECID
mobile_assertion_agent
com.apple.private.kernel.global-proc-info
/System/Library/PrivateFrameworks/SessionFoundation.framework
com.apple.siri.SpokenNotificationsModule
portrait_filters_archive_bin.metallib
System.NoteContent
UpdateDisplayDate
summaryAssets
Courier-Bold
groupConcat:
pCircBuf->pDataBegin <= pCircBuf->pBufferEnd
NSStringGenderRuleType
count % CHANGE_QUEUE_TUPLE_COUNT == 0
Encountered unparseable Unicode sequence at line %u while parsing data (input did not result in a real string)
com.apple.fileprovider.trash-put-back#PN
IOReportGroupName
com.apple.bulletinboard.observerconnection
com.apple.private.ckks.currentitempointers_read
vc-hevc-wifi-tiers-enable-threshold
https://play.itunes.apple.com/WebObjects/MZPlay.woa/wa/leaseRenew
AFibBurden_OnboardingRecordIsPresent
com.apple.locationd.emergencyplace_inference
podcast-dzc-subscribe-podcast
Humidity Sensor
file:///var/mobile/Library/com.apple.WatchListKit/serverConfiguration.plist
_CFBT_.apple.datadetectorscore.cache.full.default.system
CLASSIC_SUFFIX
10
ConverterSettings.loctable
setSavePolicy:
-[__NSFrozenDictionaryM countByEnumeratingWithState:objects:count:]
%s(): immutable collection %p given to mutating function
%@: Index %lu out of bounds; string length %lu
LOITypeToOneHotTransformer.mlmodelc
axel.2.rear.engaged
com.apple.TV
com.apple.StatusKit.publish
com.apple.podcasts.MTPlaybackQueueController.GenericQueue
pickedUpDate
com.apple.developer.networking.multipath
endDateComponents
-[NSSet objectsWithOptions:passingTest:]
com.apple.Safari.SandboxBroker
Feedback Type
inferredTimeZoneOffset
/System/Library/PrivateFrameworks/AppleCV3DModels.framework
lossStartUnixTimeZone
lockScreenWallpapers
ShareETASupportedReceivedTransportMask
c
DuplicateExtension
Z_DKAPPINSTALLMETADATAKEY__TITLE
logAXNotificationPosting
Your location is used to search for photos that were taken nearby.
deliverUpdatedBehaviorSettings
com.apple.MobileAsset.Trial.Siri.SiriExperienceCam
ams-store.apple.com
Payment_MirLogo@2x.png
phone.fill.connection
hh2AutoMigrationEnabled-seed
com.apple.HealthAlgorithms.DayStreamProcessorService
com.apple.Contacts.ViewingCard
/uts/v3/favorite-people
RingerChanged.aif
/System/Library/PrivateFrameworks/Stocks.framework/Stocks
/System/Library/PrivateFrameworks/CoreIDVShared.framework/CoreIDVShared
conn && xpc_get_type(conn) == XPC_TYPE_CONNECTION
BSCnx:client:com.apple.activitykit.output
/System/Library/PrivateFrameworks/ARKitFoundation.framework/ARKitFoundation
MemoryPeak
CMPhotoProcessMonitor
Russian
dayGroupHighlightBeingAssets
amp-api-edge.apps.apple.com
SiriExecution
CloudKit/NSCKRecordMetadata
handwritingd
AirPlayRoutePrediction
CFPreferencesCloudStoreIdentifier
/System/Library/PrivateFrameworks/VFX.framework/VFX
iPUPEnabled
AppLinks.loctable
/System/Library/Frameworks/LinkPresentation.framework
com.apple.audio.caulk
TimeOffset-system
ZASSETURL
com.apple.coordination.messaging
en.lproj/Voiceover.strings
ZACTIONDATA
SoundAnalysis
SleepHealthUI
8
file:///System/Library/PrivateFrameworks/IntlPreferences.framework/
CNAssistantCommandCancelPerson
EnableCardioFitnessAgeGating
com.apple.MobileAccessoryUpdater.deviceIdleCheck
com.apple.PassKit.issuer-provisioning
text
orm
.google.com.ni
/Library/Preferences/
reduceMotionEnabled
com.apple.weather.complication.moonEvents
originalTransmissionReference
defaultCalendarDatabaseID
file:///System/Library/PrivateFrameworks/CoreServicesStore.framework/
com.apple.networkd_privileged
End Workout
cloudNotificationsEnabled
localizationQACaptionShowUSString
com.apple.photo.PhotoImaging
com.apple.coreduetd.people
/System/Library/PrivateFrameworks/PhysicsKit.framework
ZHISTOGRAM
com.apple.AppleMediaServices.accountmediatype.production
/uts/v3/channels/{channelId}
com.apple.remindd.reminderAlarm.tonight
com.apple.icloud.searchpartyd.advertisementcache
circle.grid.cross.left.fill
Encountered unparseable unicode sequence at line %u while parsing data (too large of a value for a Unicode sequence)
simulateDownloadFailure
destroyScenesPersistentIdentifiers:animationType:destroySessions:completion:
Base.lproj/Payments.intentdefinition
ZSPECIALINSTRUCTIONS
ZALTTEXT
OSAnalytics.Hardware.Reliability
com.apple.duetexpertd.periodiclog
payloadData
call_category
-[NSMutableArray replaceObjectsInRange:withObjectsFromOrderedSet:range:]
/System/Library/PrivateFrameworks/IMTranscoding.framework
setAllowsItemLiking:
ICBrowseAttachmentsEmpty.loctable
-[NSArray firstObjectCommonWithArray:]
NSSurroundLocalizedStrings
com.apple.account.iTunesStore
com.apple.StudyLog
Event capturing entity impressions.
/System/Library/PrivateFrameworks/CoreCDPInternal.framework/CoreCDPInternal
_DKBluetoothMetadataKey__batteryLevelHeadphoneRight
ZCOMPACTUTI
SceneNet5_relationships-v8d.txt
ZWORKFLOW
com.apple.private.ClipServices
com.apple.watchkit
com.apple.iapd.xpc
kt-gossip-subsequent-gossip-chance
com.apple.weather.sensitive
managed/com.apple.ids/kCFPreferencesAnyUser
SOExtensionViewService
com.apple.health.view.data.all
AppleIDAuthSupport
deliveryDate
AnnouncementsLastUpdated
ADDED_BY_OTHER
com.apple.mediaexperience
Retrieve
CIPhotoEffectStageMono.scube
com.apple.studentd.notifications
com.apple.private.health.feature-availability-requirement-overrides/C//*/L
install-attribution-max-impressions-age
com.apple.BacklinkIndicator
DictationLanguagesEnabled
en-iphoneos
DE
applewatch
fullStateForDocument
HKDateRangeQueryClientInterface
Message Identifier
LocalizedSubTitle
Event capturing information about the next and previous sunrises and sunsets.
com.apple.tvremotecore.xpc
register-media-types-url
modern-media-controls/
flightNumber
photos-8.1.mom
/System/Library/Frameworks/ContactsUI.framework
-Hang
fitcored-engagement-category
accountSummary
MobileTimerUI
personWeight2
https://uts-api.itunes.apple.com/uts/v2/show/{showId}/itunesSeasons
VNSmartCamClassifier
com.apple.applejpeg
com.pkware.zip-archive
SidebarGenericFolder.icns
bam
id-authenticate-multiple-users
_DKBluetoothMetadataKey__deviceType
Property list format kCFPropertyListXMLFormat_v1_0 specified but was not a valid property list type
_CFBT_.caf
com.apple.developer.ubiquity-container-identifiers
DidDoInitialDisableHashtagImages
KeyboardAutocorrection_previousValue
/System/Library/Frameworks/_AppIntents_SwiftUI.framework/_AppIntents_SwiftUI
ANSCKEVENT
UnifiedAssetFramework
com.apple.registration
com.apple.StocksCore
currency
com.apple.location.region_polygonal
character.textbox.ko
com.apple.pef-binary
registerForSettingsUpdatesWithRequestDetails
OID.loctable
UTTypeTagSpecification
com.apple.private.link.donate-dynamicterms-as
contactMatchingDictionary
PKUserNotificationsRemoteNotificationServiceConnection
52.migrator.sqlite
de_??
com.apple.ParsecSubscriptionServiceSupport
/System/Library/PrivateFrameworks/Espresso.framework/Espresso
SuggestionDetailTextBehaviorType
com.apple.Heimdal
com.apple.security.personal-information.addressbook
ubidi_open return NULL object
<CFCharacterSet Predefined AlphaNumeric Set>
/System/Library/Frameworks/Contacts.framework
com.apple.coreaudio.CanRecordPastData
HomeKit App View
ModelBreakout.cdm
emojiBuckets.plist
CloudKit/NSCKMirroredRelationship
Single_0ms_S10-D52-D53-D54.ahap
_DKMetadataHomeAppView__viewName
com.apple.FileProvider.maintenance.auto-trash
file:///System/Library/PrivateFrameworks/PegasusKit.framework/
TLSSessionTicketsEnabled
displayNameIncludingCountryUsesOnlyCountry
file:///System/Library/PrivateFrameworks/Catalyst.framework/
ASFIAPItem
NSNumber
ZCLOUDGUID
CIPhotoEffect3DSilverplateBG.1.scube
https://gateway.icloud.com:443//acsnservice
voiceOverShouldDisallowUSBRestrictedMode
propertyKey
CardGloss_Square@2x.png
minimumVisibilityForVideoPlayback
transitionCompletion
com.apple.FaceTime
appLaunchUpsellQuiescenceInterval
ScreenReaderOutput
__OBJC
afds-enabled-odi
HSCheckOutRentalAssetRequest
duplicateAssetVisibilityState
keyboard.chevron.compact.down.svg
StoreSentMessagesOnServer
zyb
CFPlugInIsLoadOnDemand
pushTokensChanged:
MediaServices
kMRMediaRemoteCommandInfoSupportedPlaybackRates
allowMultitasking
item_artist.representative_item_pid
assetTrackProperty_MediaPlaybackValidation
file:///System/Library/PrivateFrameworks/CoreAccessories.framework/
com.apple.rtfd
ZTHUMBNAILINDEX
naturalLightingEnabledRetryInterval
/Library/Caches/com.apple.siri.bundleservicecache.plist
System Files
public.heif-standard
arrow.left.arrow.right.square.fill
VNPersonSegmentationGeneratorFast
System.TaskPriority
separatorEffectsShowcaseMode
siri_allowlist
applicationUserChoiceUrl
dvi
tungstenSettings
enableRectDiagnosticsForTitleSubtitleSprites
com.apple.mobileslideshow
file:///System/Library/PrivateFrameworks/Heimdal.framework/
isMarkedAsComplete
/System/Library/PrivateFrameworks/SEService.framework
com.apple.DeviceOMatic
ava
DataAccessExpress
com.apple.transparencyd
com.apple.private.translation-ui
bin.xmark.fill
sysstatuscheck
kCTCellMonitorCSGIndication
com.apple.siri.tts.resource.tr_TR
gear3@1x.png
SpatialMultichannelOff.ca/
domainInviteMemberURL
ZUNNAMEDFACECOUNT
expirationInSeconds
zoomingHeaderTintOpacity
_CFBT_.1_fa1.3.espresso.shape
*** Unable to create run loop mode queue port. ***
com.apple.availability
checkBookQueue
DTCompiler
/dasd/activityprofile
GKCloudServiceOwner
_setValue:forKeyPath:ofObjectAtIndex:
Rating-TV_US_D.tiff
Immagine JPEG
targetDhcpLatencyMs
%@~%@%@%@
nus-
analysisStates
com.pentax.raw-image
com.apple.CloudPhotoLibrary
\"NSArray\"
browseStore
ethiopic-amete-alem
root@collation=search
flashFired
RegisteredForPeerPayments
/System/Library/Frameworks/AdSupport.framework/AdSupport
com.apple.private.alloy.continuity.encryption
com.apple.proactive.EvaluationNotifications
rejectChildTransferRequest
arrow.up.right.circle
drawTypographicGuidelines
com.apple.mediasafetynet.exceptions
daysFocusPadding
/System/Library/PrivateFrameworks/MorphunAssets.framework/MorphunAssets
tsCircularBuffer.c
/System/Library/PrivateFrameworks/DMCUtilities.framework
suite/com.apple.voiceservices/kCFPreferencesAnyUser
ck-remove-from-backup-version-V3
kCFRunLoopDefaultMode
com.apple.ScreenTimeAgent.persistent-history-cleanup
com.apple.nanoregistryd
PHOTOS_WALLPAPER_SWITCHER_TITLE_PHOTOS
com.apple.clock.stopwatch
savedAssetViewVisibility
/System/Library/PrivateFrameworks/TelephonyUI.framework/TelephonyUI
file:///System/Library/PrivateFrameworks/CarKit.framework/
/System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
/System/Library/Frameworks/MetalPerformanceShaders.framework
Galician
MTDidPromptForNotificationsPermissionsKey
file:///Applications/FunCameraText.app/
(null)Observers
com.apple.health.Sleep
com.microsoft.excel.sheet.binary.macroenabled
NSURLFileResourceIdentifierKey
0:/up/backgroundUpdateProduct
PriceRange
com.apple.mobileaccessoryupdater
/System/Library/PrivateFrameworks/ControlCenterServices.framework
Contained messages must be dictionaries or nulls in multimessages
com.apple.CarPlayApp.user-alerts-service
tileFallback.pdf
CAPABILITIES
productionSimulatedDelay
R -> pt_us
NSContactsUsageDescription
semantic_to_descriptive_name.strings
HomeKey_Localizable.loctable
deviceMigrationStates
vc-enable-red-audio
_CFBT_.1.3b_fa1.3.espresso.net
TRITrialExperimentFields
A request to create a new note.
userCuratedAssets
__getSeparatorLengthsForComponent
_DKShareSheetFeedbackMetadataKey__supportedBundleIDs
aggregationScore
-[NSArray indexesOfObjectIdenticalTo:inRange:]
com.apple.assistant.contextprovider.com.apple.mobilecal
automaticAccessibilityVisualizationsEnabled
file:///Applications/MobileSMS.app/PlugIns/MobileSMSSpotlightImporter.appex/
%@%ld : %@ = %@\n
com.apple.EN.UserNotificationInteraction
photoAnalysisAttributes
firmwareUpdateRegisterFailureRetryDuration
UIBarStyleDefault
CalendarMonth-29.png
ReadReceiptsEnabled
autoSharePolicy
https://downloaddispatch.itunes.apple.com/up/backgroundUpdateProduct
storagedatad
M3U-playliste
CNAssistantCommandUpdatePerson
LastBookmarksDatabaseHealthReportDate
ProtectedCloudKeySyncing
kTCCServiceSensorKitPhoneUsage
qr-max-participants
SetCarLockStatus
override.algorithmparameters.plist
escrowProxyUrl
voiceOverPunctuationGroup
bottomLegibilityGradientHeight
com.apple.CoreCDPUI.CDPFollowUpExtension
-[NSArray indexesOfObjectsWithOptions:passingTest:]
EnableClientDrapedVectorPolygons
chinSuggestionsAreDisabled
square.2.layers.3d.bottom.filled
paymentMethod
enableInlineVideo
com.apple.springboard.smartCoverObserving
NSURLFileProtectionKey
PlistFD
/System/Library/UserNotifications/Bundles/com.apple.mobiletimer.bundle
com.apple.coreduet.knowledge
https://gspe21-ssl.ls.apple.com/attributionsearch/button-wongnai-1@3x.png
smallcircle.filled.circle
ZFRAMEWORKUUID
com.apple.ProximityReaderUIService
safariAcceptCookies
/System/Library/PrivateFrameworks/iTunesStore.framework/iTunesStore
com.apple.triald.client
/System/Library/PrivateFrameworks/Preferences.framework
customKeyAsset
more-to-follow
ZCRYPTOTAG
totalAttemptsAllowed
checkFormatOfPhoneNumber
setIconListsHidden:
file:///System/Library/Audio/UISounds/nano/MultiwayJoin.caf
com.apple.HealthKitUI
com.apple.siri.xpc_activity.refresh_validation
_DKMicroLocationMetadataKey__domain
DisabledCountries
fc-sw-3.dat
pfl:com.apple.PhotoAnalysis.PhotoAnalysisLighthousePlugin.large:metrics:
managed/com.apple.WebFoundation/kCFPreferencesCurrentUser
https://cl2-cn.apple.com/1/v1
com.apple.icloud-container.com.apple.securityd
movieAssetState
CallHistory 11.mom
cloudVersionHash
com.apple.Safari.SyncedTabs
enableAutoCrossfade
wallet:DCINotificationForMarketAdded
arrow.left.and.right.righttriangle.left.righttriangle.right.fill
_smartcolor_contrast
privacyAcknowledgementUrl
ZCHANNEL
com.apple.LinkServices
az_Latn
cloudServerPublishDate
/System/Library/PrivateFrameworks/KeychainCircle.framework
file:///System/Library/PrivateFrameworks/FlexMusicKit.framework/
dismissedWalletKeyExpressModeOnboarding
+[CNContactHeaderView descriptorForRequiredKeysIncludingAvatarViewDescriptors:]
com.apple.WallpaperKit.CollectionsPoster
entitlements
ZSHOULDIGNOREBUDGETS
graphMemoryIdentifier
com.apple.icloud-container.com.apple.Maps
AAPCommandFilterNonRestricted
createChildInline
className
/System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager
ZEXPIRYDATE
AXAirPods-B698.loctable
/photos/share/hide
MobileObliteration
ZREMOTEAVAILABILITY
badgeValueWithCompletion
com.apple.private.tipsd.discoverability
nl-BE
com.apple.avfoundation.figcam
kTCCServiceUbiquity
MusicNotificationContentExtension.MusicUserNotificationViewController
dragDropSettings
file:///System/Library/PrivateFrameworks/PhotoFoundation.framework/
AXAirPods-B494.loctable
https://gspe21-ssl.ls.apple.com/attributionsearch/button-wikipedia-1@2x.png
ZTRAININGTYPE
_thresholdRed
System.PersonHandle
com.apple.performance.DiagnosticRequest
com.apple.iconset
DSIDSelectorV4
com.apple.PrototypeTools/A//B/L
com.apple.SafariLaunchAgent
/System/Library/PrivateFrameworks/CoreTime.framework/CoreTime
com.microsoft.powerpoint.pps
clearsBackground
com.apple.uikit.viewservice.com.apple.RTTNotifications
OptionalBodyContent.mom
META-INF/
%@=%p {
Notes PencilKit drawing attachment
disBcnLossCount
/System/Library/PrivateFrameworks/ProtectedCloudStorage.framework
com.apple.news.public.qa
/System/Library/PrivateFrameworks/CoreOptimization.framework
com.apple.developer.device-information.user-assigned-device-name
Night Vision
managed/com.apple.messages.nicknames/kCFPreferencesAnyUser
Desired
NSAppleMusicUsageDescription
com.apple.iconservices.claimed-type-app-icon
com.apple.safetyalerts.xpcactivity
aspectRatioForCompactPortraitMonths
com.apple.control-center.WalletModule
com.apple.runningboard.targetidentities
Z_DKSHARESHEETSUGGESTIONMETADATAKEY__SOURCEBUNDLEID
kCFAllocatorMallocZone
ex
com.apple.private.alloy.arcade
VNPersonSegmentationGeneratorLearnedMattingTiled
https://setup.icloud.com/setup/familykit/ios/familyFlow/familyPicker
CNKClarityUISceneDelegate
com.apple.TVWatchList
providerID
https://play.itunes.apple.com/WebObjects/MZPlay.woa/wa/leaseStart
/System/Library/Frameworks/AVFAudio.framework/AVFAudio
com.apple.DocumentManager.Service
com.apple.news.private.secure.sandbox
TileGrid container
platformStrokeLightTertiary
AppClipLaunch
NSURLUseSwift
CFPreferencesInvalidOperation == [self alreadylocked_addPreferencesObserver:obs]
<CFSocket context %p>
com.apple.stocks.watchkitextension
notifyWallpaperUpdates:
setRecordIDsToVersionETags:
UIApplicationSupportsIndirectInputEvents
feedCardLandscapeAspectRatio
Media properties associated with a Master entity.
_pseudo_randPBN
zoomPanZoomKbShortcutEnabled
HFSortedIdentifierStrings_roomServices_legacy
containermanagerd
NSCollectionLayoutItem
InsightsCompressedIconicScenes
CIPhotoEffect3DVivid.1.scube
ProactiveInputPredictions
UIWhitePointAdaptivityStyleReading
file:///System/Library/CoreServices/CoreTypes.bundle/
com.apple.news.history
allowCloudBackup
kTCCServiceReminder
com.apple.registration/A//B/L
VideoRoutingCorner.ca/
suite/com.apple.mobilenotes/kCFPreferencesCurrentUser
/usr/libexec/securityd
da-
NSStringFormatClassInfoKey
com.apple.keystore.fdr-access
https://gspe21-ssl.ls.apple.com/attributionsearch/snippet-dimmi-logo-3@3x.png
CardGloss_Perforated_Vertical@3x.png
pagingVelocityThreshold
XPC_SERVICE_NAME
file:///System/Library/Audio/UISounds/New/News_Flash.caf
lu
<CFMachPort %p [%p]>{valid = %s, port = %x, source = %p, callout = %s (%p), context = %@}
AutomaticContentDownload.plist
collectionId
view-software-updates
musicTargetLoudnessLKFS
https://gspe21-ssl.ls.apple.com/attributionsearch/snippet-zomato-logo-2.png
CanonicalRegion
assistant_cdmd
presence-subscription-ttl-sec
chapterSettings
switchControlUserDidReadUSBRestrictedModeAlert
/var/mobile/Library/IntelligencePlatform/graph.db
CongestionZonesEnabled
French.lproj
com.apple.mobile.keybagd.data-analytics
HKMedicationsTimeZone
com.apple.cloudphotod.maintenance
SMS_FILTER_INEN_CLASSIFICATION
EmailDomains
ur_IN
tv-app-url
file:///private/var/mobile/
https://gspe21-ssl.ls.apple.com/attributionsearch/snippet-openrice-logo-1.png
file:///System/Library/PrivateFrameworks/MediaControls.framework/
Dynamically Registered qhvc Video Decoder
PosterBoard
com.apple.seserviced.transactionStatsReportingActivity
schema.mdplist
rgbTransformMap_v1_Studio_FAR_fp16_RGBAslice9
com.apple.private.securityd.ae.disable
setRecordsToSave:
accessible-extended
com.apple.mobileassetd.auto-asset-scheduler
ASMessagesProvider
setBadgeNumber
Can't interpret CFSTR() as MacOS Roman, crashing
DifferentialPrivacyDataModel.momd/
ZENTITYPK
com.apple.private.applemediaservices.engagement.extension
.AppleHongKongChineseFont
impress
systemgroup.com.apple.icloud.searchpartyd.sharedsettings
+[CNContactHeaderDisplayView descriptorForRequiredKeysForContactFormatter:]
com.apple.SharingUI
com.apple.imagent.av
com.apple.HomeKitEventRouter
```
