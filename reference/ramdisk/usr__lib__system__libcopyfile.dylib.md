# `/usr/lib/system/libcopyfile.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 115,136 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 28 (Size: 2224)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (11)

- `/usr/lib/system/libcopyfile.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0)`
- `/usr/lib/system/libsystem_kernel.dylib (compatibility version 1.0.0, current version 13432.52.1)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libsystem_blocks.dylib (compatibility version 1.0.0, current version 98.0.0)`
- `/usr/lib/system/libsystem_asl.dylib (compatibility version 1.0.0, current version 409.40.3)`
- `/usr/lib/system/libsystem_info.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/system/libdispatch.dylib (compatibility version 1.0.0, current version 1605.40.4)`
- `/usr/lib/system/libxpc.dylib (compatibility version 1.0.0, current version 3298.52.1)`

## Entitlements

```xml
  - no entitlements
```

## Strings (203)

```
fchmodx_np on destination readonly fd: %m
copyfile_unpack
setting security information: %m
unable to punch trailing hole in destination file, offset %lld: %m
Destination %s already exists as a symlink, refusing to copy: %m
i16@?0Q8
copytree
fstat failed on readonly fd during validation: %m
Corrupt attribute entry (name length is %d bytes): %m
%s: set times: %m
copyfile_check
acl_clear_permset: %m
acl_set_qualifier: %m
%s:%d:%s() copyfile_unpack: calloc(1, %zu) returned NULL\n
com.apple.decmpfs
com.apple.TextEncoding
open_dst_rsrc_fork
%s:%d:%s() no extended attributes found (%d)\n
%s:%d:%s() extended attribute list too long\n
%s:%d:%s() preallocating %lld bytes on destination\n
No memory for copy buffer: %m
could not change mode of destination file %s to match source file %s: %m
%s:%d:%s() open failed because it is a directory (%s)\n
v8@?0
%s:%d:%s() closing %s fd: %d\n
open_src_rsrc_fork
%s: remove: %m
skipping attr \"%s\" due to error %d: %m
%s:%d:%s() input block size: %zu output block size: %zu\n
writing to output file got error: %m
copyfile_security
%s:%d:%s() open successful on source (%s)\n
acl_get_permset: %m
%s:%d:%s() file descriptors not open (src: %d, dst: %d)\n
cannot readlink %s: %m
fcopyfile
copyfile_preamble
copyfile_pack
i24@?0r^v8r^v16
(rsrc)
copyfile_set_bsdflags
unable to advance dst to next data section: %m
lseek during hole punching failed: %m
add ACL_SYNCHRONIZE: %m
couldn't write file header: %m
%s:%d:%s() unsetting uuid attribute on %s\n
%s:%d:%s() unsetting group uuid attribute on %s\n
source's xattr list size (%zu) exceeds the threshold (%d); trying to allocate: %m
copyfile_data
com.apple.metadata:
PS
src
%s:%d:%s() %s has large resource fork, will use namedfork to copy\n
%s:%d:%s() copied name [%s]\n
writing to resource fork got error: %m
file %s changed behind our feet: %m
failed to determine copy protection on (%s) with error <%d>: %m
PCS
dst
add ACL_APPEND_DATA: %m
add ACL_WRITE_SECURITY: %m
 copied 32 bytes of \"%s\" data @ offset 0x%08x: %m
copyfile_unset_acl
stat on %s: %m
%s:%d:%s() truncating existing file (%s)\n
CS
error processing security information: %m
Incomplete or corrupt attribute entry: %m
%s:%d:%s() fchflags failed on %s (%d)\n
unable to punch hole in destination file, offset %lld length %lld: %m
copyfile_open
%s:%d:%s() copied %ld bytes of \"%s\" data @ offset 0x%08x\n
missing FTS entry during recursive copy\n: %m
Cannot lstat destination %s: %m
unknown
skipping attr \"%s\" due to fetch error %d: %m
Corrupt attribute entry (only %d bytes): %m
%s:%d:%s() failed to read %u bytes at offset %u\n\n
open on %s: %m
B
acl_set_permset: %m
bad attribute header: %m
%s:%d:%s() could not allocate %zu bytes for rsrcforkdata\n
%s:%d:%s() extracting \"%s\" (%d bytes)\n
%s:%d:%s() Resource fork copy (fsetxattr) failed (%d - state %d - errno %d)\n
com.apple.metadata:kMDItemIsShared
com.apple.ResourceFork
error processing data: %m
unexpected size (%ld) for \"%s\": %m
com.apple.root.installed
reading from %s %s: %m
repeat stat on %s\n: %m
/Library/Caches/com.apple.xbs/F5CB97C0-F415-4D9E-AED6-CF62F46E3ECD/TemporaryDirectory.Ktomyr/Sources/copyfile/copyfile.c
bad attribute header:  %zu < %zu: %m
%s:%d:%s() not setting empty resource fork on directory\n
fstat failed on writable fd during validation: %m
couldn't write resource fork: %m
%s:%d:%s() pread returned: %zd\n
could not set attributes %s on destination file descriptor: %m
com.apple.metadata:kMDItemOwnerName
fstatx_np on src fd %d: %m
error closing files: %m
add ACL_WRITE_EXTATTRIBUTES: %m
copyfile_pack_acl
%s:%d:%s() couldn't stat destination file\n
%s:%d:%s() altered acl\n
com.apple.security.
%s:%d:%s() set dst_fd <- %d\n
%s%s%s
getting acl: %m
%s:%d:%s() error %d setting resource fork attribute\n
(null string)
Invalid compression_type <%d> on attribute %s for src file %s: %m
Invalid file descriptor offset, cannot perform a sparse copy: %m
file type (%u) does not match expected %u on %s\n: %m
%s:%d:%s() returning: %d errno %d\n\n
set ACL_EXTENDED_ALLOW: %m
com.apple.acl.text
%s:%d:%s() no memory for %u bytes\n\n
destination's xattr list size (%zu) exceeds the threshold (%d); trying to allocate: %m
resource fork getxattr failed: %m
failed to set dst to first data section: %m
writing to output file failed: %m
add ACL_WRITE_DATA: %m
figgledidiggledy
error processing extended attributes: %m
Mac OS X        
malloc: %m
copyfile_get_bsizes
Could not zero destination file before copy: %m
unable to find next hole in file during copy: %m
%s:%d:%s() no acl entries found (errno = %d)\n
%s:%d:%s() Resource fork copy (fd) failed (%d - state %d - errno %d)\n
%s:%d:%s() compression_type <5> on attribute com.apple.decmpfs for src file %s is not copied.\n
%s:%d:%s() couldn't stat destination file for st_flags (%d)\n
(null tmp)
could not apply acl to destination file %s from source file %s: %m
Cannot make directory %s: %m
SET_PROT_CLASS failed on (%s) with error <%d>: %m
%s:%d:%s() open successful on destination rsrc (%s)\n
skipping attr \"%s\" (too big): %m
copyfile_pack_rsrcfork
%s:%d:%s() extracting \"%s\" (%d bytes) at offset %u\n
xattr named %s has size (%zu), which exceeds the threshold (%d); trying to allocate: %m
%s:%d:%s() copied acl entry from %s to %s\n
GET_PROT_CLASS failed on (%s) with error <%d>: %m
Cannot open symlink %s for reading: %m
..namedfork/rsrc
%s:%d:%s() debug value set to: %d\n
fstat failed on destination readonly fd: %s: %m
%s:%d:%s() copied acl (%ld) %p\n
%s%s
com.apple.metadata:kMDItemCollaborationIdentifier
PC
S
Corrupt attribute entry (name is not NUL-terminated): %m
com.apple.quarantine
N
%s:%d:%s() set src_fd <- %d\n
%s:%d:%s() returning %d errno %d\n
error %d setting attribute %s: %m
realloc for resource fork failed: %m
open on %s resource fork: %d: %m
COPYFILE_DEBUG
com.apple.FinderInfo
couldn't read entire resource fork: %m
%s:%d:%s() pread couldn't read entire header: %d of %d\n
com.apple.metadata:kMDItemFavoriteRank
%s:%d:%s() replacing string %s (%s) -> (%s)\n
add ACL_WRITE_ATTRIBUTES: %m
cannot open destination for permission elevation: %s: %m
copyfile_internal
writing to output %d times resulted in 0 bytes written: %m
error %d reading from %s: %m
cannot allocate %zd bytes: %m
copyfile
error closing source rsrc file descriptor: %d: %m
(null src)
%s:%d:%s() copied %zd bytes of \"%s\" data @ offset 0x%08x\n
copyfile_xattr
unable to advance src to next data section: %m
unable to reset file descriptors to punch holes: %m
fstat on open fd failed for %s\n: %m
%s:%d:%s() open successful on source rsrc (%s)\n
%s:%d:%s() couldn't read resource fork (only read %d bytes of %d)\n
%s:%d:%s() rounding up block size from fsize: %lld to multiple of %zu\n
%s:%d:%s() open failed, retrying (%s)\n
%s:%d:%s() open successful on destination (%s)\n
/
%s:%d:%s() setting flags: 0x%x\n
(null dst)
/dev/null
Cannot open directory %s for reading: %m
%s:%d:%s() check result: %d (%s)\n
com.apple.metadata:kMDItemSharedItemCurrentUserRole
destination file %s changed behind our feet: %m
Not a valid Apple Double header: %m
%s:%d:%s()  extracting \"%s\" (32 bytes)\n
%s:%d:%s() couldn't read resource fork\n
%s:%d:%s() unsetting acl attribute on %s\n
Could not set destination file size before copy: %m
Cannot make symlink %s: %m
open/malloc/stat on %s resource fork: %d: %m
```
