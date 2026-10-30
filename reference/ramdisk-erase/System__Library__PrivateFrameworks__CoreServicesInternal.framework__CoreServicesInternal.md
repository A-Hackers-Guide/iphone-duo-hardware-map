# `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 504,048 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 32 (Size: 2912)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/System/Library/PrivateFrameworks/CoreServicesInternal.framework/CoreServicesInternal (compatibility version 1.0.0, current version 609.1.7)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/CoreServices.framework/CoreServices (compatibility version 1.0.0, current version 1226.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78, upward)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (482)

```
_FSURLCopyResourcePropertiesForKeysInternal: NULL result with no real error
%s: error getting path for url=%{public}@: %{public}@
%s: result=<%p: %@> error=%@
kExcludedFromBackupXattrName set on path: %{private}s
5a.  Trying volume url=%@ with partial path %@ volumeDepth=%u
-. Pruning array of potential volumes based on information in the bookmark.
match bookmark, depth=%u matchToURL=%@
%s: this would have gone down the fallback path if enabled: %@
%s: get_fsid_and_file_id error for path=%{public}s: %{errno}d
 -- REJECTED: canonical path does not match the path under test.
 --  on volume=%@ fileIDRefs=%@
_FSURLGetResourcePropertyFlags: false result with no real error
kExcludedFromCloudBackupName set on path: %{private}s
Bookmark was to an item on the boot drive, which does not appear to match the current boot drive by UUID.  Saved uuid=%@
-. Constructing array of potential volumes to be considered for items in this bookmark.
%s: returning <%p %@>
 provisionalURL=%@
(possible) matched volume %@ by capacity=%@ and creationDate=%@ (renamed volume case)
ignoring unsupported value: kCFURLFileProtectionKey=%@ for %@
sandbox_extension_update_file_by_fileid error for fsid={%#x, %#x}, id=%#llx: %{errno}d
cannot attach security scope to a URL that is not a file URL: <%p %@>
Trying relative to bookmark user's home directory: %@
3. - Trying to match by relative path on current boot volume.
kExcludedFromUnencryptedBackupName set on path: %{private}s
FAILED creating bookmark file at %@, error=%@
VOLUME(S) IDENTIFIED; starting the attempt to find this item represented by this bookmark item at depth %u on one of these volumes.
8. Trying to find target at depth 1 solely by documentID on matched volumes.
CFURLCreateBookmarkData
Discarding capacity & creation date match because we found more than one possibility.
Pruning volume list to %@ because its UUID matches the one in the bookmark data.
kExcludedFromUnencryptedBackupName removed from path: %{private}s
<%p %@>: internal sandbox error for <StartAccessing>
failed to consume sandbox extension: %{errno}d
Checking volume for match to bookmark, volumeURL=%@
kExcludedFromCloudBackupName removed from path: %{private}s
sandbox_extension_consume error=%{errno}d for path %@
matched volume %@ by name=%@ and capacity=%@ and creationDate=%@
Consuming sandbox extension in bookmark: %s
matched volume %@ by VolumeMountURL %@
1. Original item was in a home folder, so look for an item in the home directory.
_FSURLSetResourcePropertiesForKeys: returning false without an error
_FSURLCopyResourcePropertyValuesAndFlags: false result with no real error
_FileURLCreateDisplayPathComponentsArray(1): NULL result with no real error
_FSURLCopyResourcePropertyForKeyInternal: false result with no real error
%s: NULL result with no real error
 - provisionalURL=%@
handle %lld: sandbox_extension_release error %{errno}d
BookmarkData: Corrupt bookmark file; container dataItemPtr %{public}p already used
%s: fatal error: no fsid and file id provided or fetched
Adding %u from path components to relative URL
4. Trying to match by volume name + path components, maybeURL=%@ volumePathElements=%@ pathComponents=%@ volumeURL=%@
 -- Attempting to mount ( or find already mounted ) possible network filesystem item, at path %@ which is needed for bookmark resolution.
Register Property Providers
_FSURLGetVolumePropertyFlags: false result with no real error
<%p %@>: called <StopAccessing> too many times or URL isn't security-scoped
unexpected return value from sandbox_extension_consume: %lld
Bookmark failed to issue extension for item %s (depth=%d): %{errno}d
 -- matchURLToBookmark: the path or canonical path is NULL.
_FSURLSetResourcePropertiesForKeys: false result with no real error
_FileURLCreateDisplayPathComponentsArray(2): NULL result with no real error
kExcludedFromBackupXattrName removed from path: %{private}s
handle %lld: released extension for path %@
 -- SUCCESS, bookmark, depth=%u is a matchToURL=%@ because the item properties matched those of the original item, and the item exists.
 -- SUCCESS, bookmark, depth=%u is a matchToURL=%@ because the bookmark doesn't contain any properties to match, and the item exists.
_FSURLCreateStandardError: NULL result with no real error
_URLReplaceObject: false result with no real error
%s/%d: setting QuarantineMountedNetworkVolumesMask for bookmark
Checking for home-directory match by relative path for current user 
Bookmark was to an item on a local drive; checking if it's the boot drive and if the uuid matches.  onBoot=%{bool}d volMountPath=%@
_FSURLSetResourcePropertyForKey: false result with no real error
_FSURLCacheResourcePropertiesForKeys: false result with no real error
%s: not implemented
COMPLETED RESOLUTION of a bookmark to a filesystem item, depth=%u item=<%p: %@>, stale=%{bool}d
sandbox_extension_update_file_by_fileid result=%d, dst=%@, fsid={%d, %d}, file_id=%lld
%p: removing sandbox extension
%s: %s
 -- Trying to match by targetFileID from documentID, options=%#lx fileID=%@ on volume %@
<%p %@>: internal sandbox error for <StopAccessing>
_FSURLGetCachedVolumeTotalCapacity: false result with no real error
CacheItem list corrupted for extension %s
3. Original item was on the boot drive, so looking for an item by relative path on the current boot drive.  path=%@
6. Trying to find target solely by fileID on matched volumes.
Bookmark was homeDirectoryRelative, depth inside homeDirectory=%u
Checking for home-directory relative match by relative path
_URLEnumeratorGetNextURL: NULL result with no real error
_URLEnumeratorGetURLsBulk: NULL result with no real error
result=<%p %@>
Necessary matching props for volume from bookmark: wasLocal=%{bool}d wasNetwork=%{bool}d wasDevFS=%{bool}d/%{bool}d
failed to release sandbox extension handle %lld, error=%{errno}d
%s: finished %@, error=%@
%@: error setting protection class: %{errno}d
%s: failed to get file system representation for the dst path.
sandbox extension cache path count: %ld
handle %lld: new handle for path %@
_URLCreateByResolvingAliasFile: NULL result with no real error
Bookmark was to home directory, so trying %@
5. Trying to match by partial path across all of the volumes ( in case the volume it was on got renamed. )
Bookmark was to an item on the boot drive, which appears to match the current boot drive by UUID, so using that volume. uuid=%@
%s: <%p: %@> options=%#lx propertiesToInclude=%@ relativeToURL=%@
matched volume %@ by uuid %@
Mounting required volumes: %@
2. Bookmark was to a volume, so try to just find a matching volume.
5b. Trying to find by partial paths on volume by mount path, partialPath=%@ maybeURL=%@
7. Trying to find target by fileID and partial paths, to deal with renamed parent items.
%s: (depth=%u bookmarkItemWasLocal=%{bool}d volumeUUID=%@
-. Resolving url to disk image for volume at depth %u to determine image file to be mounted.
_FSURLResourceIsReachable: false result with no real error
_FSGetFileSystemRepresentationForFileID: false result with no real error
%s: no mountpoint for path: %@
%p: releasing extension by path for %s
handle %lld: decrementing ref count to %lld
%p: attaching sandbox extension %{private}s
 -- Returning volumeURLRef=%@
sandboxExtension to attach was not a CFData object
CFURLResolveBookmarkData
REMOVING %u from relative url=%@
Trying relative to current home directory: %@
ERROR-- two mounted volumes (%@,%@) have the same UUID %@
%s: %{bool}d
 -- Attempting to find already mounted URLMount volume item, at url %@ which is needed for bookmark resolution.
<%p %@>: called <StartAccessing> on a URL that is not security-scoped
STARTING RESOLUTION of a bookmark to a filesystem item. options=%#lx, originalItemPath=%@
 -- trying to match by relative path from fileIDsRef=%@ volumeURL=%@
_FSURLCacheResourcePropertyForKey: false result with no real error
 -- Trying to relative path from fileID, maybeURL=%@ depth=%u options=%#lx fileID=%@ fileIDURL=%@  partialPath=%@
%s: downloading %@
handle %lld: incrementing ref count to %lld for path %@
%s: destination URL %{public}@ exists but does not point to a valid file, so exiting with an error %{public}@
 -- Trying to match by targetFileID, depth=%u  options=%#lx fileID=%@ on volume %@
_FSCreatePathForFileID: NULL result with no real error
bookmarkRef=<%p %@>  options=%#lx relativeToURL=%@ propertiesToInclude=%@ repIsStaleP=%p errorRefP=%p
 -- got userCanceledErr from mount attempt, making further resolution for this bookmark fail.
resolve
scopeKeyLength == kBookmarkSecurityScopeCookieSize
!userAccessReadOK
\tvolumeInfo = (\n
%c
createByResolvingBookmarkDataInternal
FALSE 
result != NULL
SupportsHiddenFiles
}
createdWithRelativeURL
effectiveIconData:
!ipod
SetNameAndExtensionLengthFromCString: CFStringCreateWithBytes failed with kCFStringEncodingUTF8; retrying with kCFStringEncodingISOLatin1
!userAccessWriteOK
%s 
v32@?0^{__CFURL=}8^{__CFError=}16@?<v@?>24
extension
GetattrlistRetry: realloc request too large (%d)
_CFURLCreateBookmarkData
!file-ids
<CFURLEnumerator %p>{enumeratorOptions = %ld, propertyKeys = %@
com.apple.coreservicesinternal.vfs_notifications
_FileCacheCopyDebugDesc
!NameIsHidden
\n
\t\thasFullPath\n\t\t\t<CFString %p> %@\n
teamIdentifier:
zeroRuns
file:///.nofollow/
com.apple.metadata:com_apple_unencryptedBackup_excludeItem
FaultLogicalFileIsHidden
volPathComponents:
!vol
!rmvbl
!symlinks
case-sens
 true  
_NSURLBookmarkSecurityScopeCollectionTokenKey
IOBlockSize = %lu
relativeDirsUpMinusOne:
0123456789ABCDEF
NSUserStringVariant
HasPathFromID
%2.2x
baseURLComponentCount:
case-presrv
10.15
} 
(*)
NSURLBookmarkAllPropertiesKey
Props:[
auto
 <number> 
file:///.resolve/
/.nofollow/
<NULL>
BookmarkData
HasDecmpFSCompression
DataProtectFlags = %lu\n\t\t\t
volIDiskUserName:
ext-hid
lifs
__CFURLCreateBookmarkData
relativeDirsUp:
_URLCreateByResolvingAliasFile
!eject
com.apple.bookmarkresolution
fskit
!FaultLogicalFileIsHidden
!userAccessExecuteOK
diskImageDepth:
sym
rw
!case-presrv
kCFBookmarkResolutionWithoutMountingMask was passed and the volume needed wasn't available
\t\thasFinderInfo\n\t\t\t%@\n\t\t\tfinderInfo    = %.2x %.2x %.2x %.2x  %.2x %.2x %.2x %.2x  %.2x %.2x %.2x %.2x  %.2x %.2x %.2x %.2x\n\t\t\textFinderInfo = %.2x %.2x %.2x %.2x  %.2x %.2x %.2x %.2x  %.2x %.2x %.2x %.2x  %.2x %.2x %.2x %.2x\
modificationDate:
%s%s 
!internal
CFURLCreatedFromBookmark
IsMountPoint
AccTime = %@\n\t\t\t
CrTime  = <n/a>\n\t\t\t
\t\thasFileIDs\n\t\t\tInodeNumber = %llu\n\t\t\tFileID = %llu\n\t\t\tParentID = %llu\n
pkg
vis
 false 
createVolumeURL
userAccessWriteOK
bookmark
invalid data section length
file-read-data
\t\thasBase\n\t\t\t%@\n\t\t\t%@\n\t\t\t%@\n\t\t\t%@\n\t\t\t%@\n\t\t\t%@\n\t\t\t%@\n\t\t\t%@\n\t\t\t%@\n\t\t\t%@\n\t\t\t%@\n\t\t\t
volAutomountPath:
testKey2
!file
SupportsHardLinks
NSURLBookmarkQuarantineMountedNetworkVolumesKey
sandboxROExtension:
browse
journal
/.nofollow%s
SandboxExtensionCache.cpp
BookmarkData.cpp
!SupportsHiddenFiles
\t\thasDevice\n\t\t\tFSID = {0x%.8x 0x%.8x}\n\t\t\tVolumeID = %lu\n
  
volMountURL:
 %4.4d/%2.2d/%2.2d %2.2d:%2.2d:%-6.4f 
CFURLEnumerator
NSFileOriginalItemLocationKey
volURL:
displayNamesDict:
dir
_NSURLSecuritySandboxExtensionKey
.
__kCFURLExpensiveVolumeInformationKey
have_carbon_core_block_invoke
AddedTime = <n/a>\n\t\t\t
sandboxRWExtension:
/.resolve/
com.apple.private.CustomSandboxExtension.read-only
file-write-data
NSURLBookmarkAllPropertyKeysKey
shortVersion:
kCFURLBookmarkCreationMinimalBookmarkMask
, 
!HasDecmpFSCompression
\t\tuuid = %@\n
head
invalid header
volInfoDepths:
file-ids
!isJournaling
remove
://
  bookmarkDataSectionOffset = 0x%x\n
!case-sens
NSFileNewItemLocationKey
kern.osproductversion
com.apple.FileURL
_FSURLCreateWithPathAndAttributes: CFURLCreateFromFileSystemRepresentation failed; pathLen = %ld
FSMountUpdateCaseInsensitiveName
[CFNumber?] 
\t\thasFileSecurity\n\t\t\t%@\n
queryString:
volHomeDirRelativePathComponentCount:
creationOptions:
bookmarkCreationTime:
copyVolumesArrayForBookmark
 %3d) itemType=0x%x flags=0x%x dataOffset=0x%x %s
toc:
internal
diskimage
sparseFiles
false
SetNameAndExtensionLengthFromCString: CFStringCreateWithBytes failed with kCFStringEncodingISOLatin1; setting name to empty string
Backup
_FileCache
!HasPathFromID
HasExtendedSecurity
volProps:
file:///.file/id=
/.file/id=%lld.%lld/%s
devfs
v8@?0
file
!app
kCFURLBookmarkCreationAllowCreationIfResourceDoesNotExistMask
createFileResourceIdentifierValue
/?
newItem
] 
volWasBoot:
vol
append
/0x
!sparseFiles
CarbonCore
\t\tflags = 0x%llx\n
Name = <CFString %p> %@\n\t\t\tAccessMask = 0%.4lo\n\t\t\tFlags = %lu\n\t\t\tDirFileLinkCount = %lu\n\t\t\tGenCount = %lu\n\t\t\tDocumentID = %lu\n\t\t\tOwnerID = %d\n\t\t\tGrpID = %d\n\t\t\t
displayName:
!browse
move
com.apple.private.CustomSandboxExtension.read-write
file:///
AddedTime = %@\n\t\t\t
!finderInfoZeros
sys-mut
!external
/.resolve/%u%s
IsTrigger
NSURLBookmarkDetailedDescription
accessDate:
external
!diskimage
/.file/id=
formatter != NULL
finderInfoZeros
\t\tcreationDate = %@\n
_NSURLBookmarkFlagsKey
typeBindingData:
sys-immut
rmvbl
, directoryURL = %@, currentLevel = %ld
Bookmark: dataRef=%p len=%d\n
urlString:
aliasData:
[ 
__kCFURLCheapVolumeInformationKey
Ciao
\tpropertyValues = %@\n\ttemporaryPropertyValues = %@\n\tpermanentPropertyValues = %@\n\tvolumeInfo = %@\n
pathComponents:
 Unknown encoded type, typeID=%d
, currentError = %@
:
volPath:
!dir
Has64BitObjectIDs
!HasExtendedSecurity
CrTime  = %@\n\t\t\t
\t\tvolFileCount = %llu\n\t\tvolDirCount = %llu\n\t\tvolSize = %llu\n\t\tvolSpaceAvail = %llu\n
  | 
IsHFSStandard
  signature = 0x%x\n
pathComponentProps:
eject
 
 \n
tagStyle:
securityScopeCookie:
user-immut
local
symlinks
!zeroRuns
default
TRUE 
\t\tmaxFileSize = %llu\n
DownloadCloudDocumentSync
file:///.file/id=%lld.%lld%s
invalid TOC: cycle
file://
ModTime = %@\n\t\t\t
 flags = %#x\n
relativeDirsDownMinusOne:
com.apple.ResourceFork
!auto
!hard-links
_consume
wasFileIDFormat:
haseBaseURL:
destination || (fsidp && file_id)
/
parseAttributeBuffer: ATTR_CMN_NAME was returned with 0 attr_length
DocumentManager
extensionLength = %hu\n\t\t\t
_CFURLWriteBookmarkDataToFile
ipod
kCFURLBookmarkCreationDoNotIncludeSandboxExtensionsMask
NULL
 %lg 
 %2.2x
NSFileBackupItemLeftBehindLocationKey
\t\thasFileDataLength\n\t\t\tFileDataLength = %llu\n\t\t\tFileDataAllocSize = %llu\n
!IsMountPoint
!IsTrigger
creationDate:
 %ld/0x%lx 
_FileCacheGetForURL would have returned NULL
userAccessExecuteOK
fileID:
ext-vis
app
hard-links
isJournaling
_CFURLCreateByResolvingBookmarkData
#
relativeDirsDown:
volCreationDate:
com.apple.metadata:com_apple_backup_excludeItem
oldItem
_insert
EvolvingiPad
=
!SupportsHardLinks
hid
]
ro
[
!IsHFSStandard
volCapacity:
/dev/disk
fileIDs:
bookmarkFileProviderString:
com.apple.MobileBackup
com.apple.metadata:com_apple_cloudBackup_excludeItem
/private/
insert
resourceProps:
!journal
NSURL
scoped
FileCache.cp
!Has64BitObjectIDs
  version = 0x%x\n
volUUID:
version:
< unrepresentable string>
invalid bookmark length
ChgTime = %@\n\t\t\t
userAccessReadOK
\t\thasRsrcInfo\n\t\t\trsrcLength = %llu\n\t\t\trsrcAllocSize = %llu\n
effectiveFlattenedIconRef:
testKey1
path
invalid data item pointer
fragmentString:
...
, currentURL = %@
\t\thasUserAccess\n\t\t\t%@\n\t\t\t%@\n\t\t\t%@\n
  length = 0x%x\n
 0x%5.5lx:
userUID:
__kCFURLNoDependsVolumeInformationKey
{
fileName:
NSURLKeys
file:///.file/id=%lld.%lld/?.resolve=%u
/dev/rdisk
MM/dd/yyyy HH:mm:ss.SSS
alias
Finalize
\t)\n
**
!pkg
!local
url
i24@?0r^v8r^v16
<_FileCacheRef %p>{\n\tvalidSeed = %d\n\tattributes = (\n
 toc @ offset:0x%x ( 0x%p ) level=%d count=%d next=0x%d\n
attrModificationDate:
volName:
userName:
!sym
kCFURLBookmarkCreationSuitableForBookmarkFile
  bookmarkDataSectionFirstTOCOffset = 0x%x\n
user-mut
\"
NameIsHidden
```
