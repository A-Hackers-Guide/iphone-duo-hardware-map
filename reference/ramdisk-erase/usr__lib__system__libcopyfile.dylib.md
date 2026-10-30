# `/usr/lib/system/libcopyfile.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 115,136 bytes.

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
unable to punch hole in destination file, offset %lld length %lld: %m
repeat stat on %s\n: %m
file type (%u) does not match expected %u on %s\n: %m
Cannot open directory %s for reading: %m
com.apple.ResourceFork
%s:%d:%s() debug value set to: %d\n
%s:%d:%s() file descriptors not open (src: %d, dst: %d)\n
%s:%d:%s() extracting \"%s\" (%d bytes) at offset %u\n
%s:%d:%s() no memory for %u bytes\n\n
PS
fstat failed on readonly fd during validation: %m
Could not set destination file size before copy: %m
missing FTS entry during recursive copy\n: %m
PCS
B
com.apple.metadata:kMDItemIsShared
com.apple.metadata:
com.apple.security.
%s:%d:%s() %s has large resource fork, will use namedfork to copy\n
%s:%d:%s() extended attribute list too long\n
skipping attr \"%s\" due to fetch error %d: %m
%s:%d:%s() copyfile_unpack: calloc(1, %zu) returned NULL\n
%s:%d:%s() compression_type <5> on attribute com.apple.decmpfs for src file %s is not copied.\n
unable to advance src to next data section: %m
%s:%d:%s() copied acl entry from %s to %s\n
skipping attr \"%s\" (too big): %m
copyfile_xattr
%s:%d:%s() set dst_fd <- %d\n
copyfile_preamble
%s:%d:%s() copied name [%s]\n
couldn't write file header: %m
Invalid compression_type <%d> on attribute %s for src file %s: %m
resource fork getxattr failed: %m
could not change mode of destination file %s to match source file %s: %m
com.apple.quarantine
%s:%d:%s() copied %zd bytes of \"%s\" data @ offset 0x%08x\n
%s:%d:%s() error %d setting resource fork attribute\n
file %s changed behind our feet: %m
cannot readlink %s: %m
Cannot lstat destination %s: %m
%s:%d:%s() check result: %d (%s)\n
%s:%d:%s() replacing string %s (%s) -> (%s)\n
(null src)
copyfile_pack
%s%s
add ACL_WRITE_ATTRIBUTES: %m
copyfile_internal
getting acl: %m
destination's xattr list size (%zu) exceeds the threshold (%d); trying to allocate: %m
writing to output %d times resulted in 0 bytes written: %m
%s:%d:%s() open successful on source (%s)\n
Cannot make symlink %s: %m
SET_PROT_CLASS failed on (%s) with error <%d>: %m
%s:%d:%s() no extended attributes found (%d)\n
%s:%d:%s() couldn't read resource fork\n
copyfile_unset_acl
unknown
cannot open destination for permission elevation: %s: %m
figgledidiggledy
Corrupt attribute entry (only %d bytes): %m
setting security information: %m
%s:%d:%s() rounding up block size from fsize: %lld to multiple of %zu\n
copyfile_get_bsizes
error %d reading from %s: %m
open_dst_rsrc_fork
Corrupt attribute entry (name is not NUL-terminated): %m
open on %s: %m
fstat on open fd failed for %s\n: %m
fstat failed on destination readonly fd: %s: %m
%s:%d:%s() copied %ld bytes of \"%s\" data @ offset 0x%08x\n
bad attribute header: %m
%s:%d:%s() couldn't stat destination file\n
copyfile_set_bsdflags
Cannot open symlink %s for reading: %m
error closing source rsrc file descriptor: %d: %m
%s:%d:%s() input block size: %zu output block size: %zu\n
copyfile_data
lseek during hole punching failed: %m
cannot allocate %zd bytes: %m
com.apple.metadata:kMDItemCollaborationIdentifier
N
%s:%d:%s() returning %d errno %d\n
copytree
acl_set_permset: %m
com.apple.acl.text
%s:%d:%s() failed to read %u bytes at offset %u\n\n
com.apple.root.installed
unable to reset file descriptors to punch holes: %m
%s:%d:%s() altered acl\n
fstatx_np on src fd %d: %m
acl_set_qualifier: %m
copyfile_pack_rsrcfork
%s:%d:%s() couldn't read resource fork (only read %d bytes of %d)\n
xattr named %s has size (%zu), which exceeds the threshold (%d); trying to allocate: %m
copyfile_security
%s:%d:%s() open failed, retrying (%s)\n
/Library/Caches/com.apple.xbs/F5CB97C0-F415-4D9E-AED6-CF62F46E3ECD/TemporaryDirectory.Ktomyr/Sources/copyfile/copyfile.c
add ACL_SYNCHRONIZE: %m
skipping attr \"%s\" due to error %d: %m
could not set attributes %s on destination file descriptor: %m
v8@?0
acl_get_permset: %m
couldn't write resource fork: %m
%s:%d:%s() pread returned: %zd\n
%s:%d:%s() unsetting uuid attribute on %s\n
No memory for copy buffer: %m
stat on %s: %m
failed to determine copy protection on (%s) with error <%d>: %m
CS
src
%s:%d:%s() setting flags: 0x%x\n
%s: remove: %m
copyfile_unpack
%s: set times: %m
%s:%d:%s() truncating existing file (%s)\n
i16@?0Q8
copyfile_pack_acl
%s:%d:%s() not setting empty resource fork on directory\n
copyfile_open
%s:%d:%s() open successful on source rsrc (%s)\n
%s:%d:%s() returning: %d errno %d\n\n
realloc for resource fork failed: %m
failed to set dst to first data section: %m
com.apple.metadata:kMDItemOwnerName
%s:%d:%s() set src_fd <- %d\n
dst
/
%s:%d:%s() pread couldn't read entire header: %d of %d\n
%s:%d:%s() could not allocate %zu bytes for rsrcforkdata\n
%s:%d:%s() fchflags failed on %s (%d)\n
writing to output file failed: %m
(null tmp)
error closing files: %m
fstat failed on writable fd during validation: %m
Not a valid Apple Double header: %m
unable to find next hole in file during copy: %m
unable to advance dst to next data section: %m
Cannot make directory %s: %m
%s:%d:%s() open failed because it is a directory (%s)\n
com.apple.TextEncoding
open on %s resource fork: %d: %m
add ACL_WRITE_SECURITY: %m
set ACL_EXTENDED_ALLOW: %m
couldn't read entire resource fork: %m
com.apple.metadata:kMDItemSharedItemCurrentUserRole
com.apple.metadata:kMDItemFavoriteRank
malloc: %m
Corrupt attribute entry (name length is %d bytes): %m
error %d setting attribute %s: %m
%s:%d:%s() Resource fork copy (fsetxattr) failed (%d - state %d - errno %d)\n
PC
acl_clear_permset: %m
fchmodx_np on destination readonly fd: %m
i24@?0r^v8r^v16
%s:%d:%s() copied acl (%ld) %p\n
bad attribute header:  %zu < %zu: %m
%s:%d:%s() Resource fork copy (fd) failed (%d - state %d - errno %d)\n
writing to resource fork got error: %m
GET_PROT_CLASS failed on (%s) with error <%d>: %m
..namedfork/rsrc
add ACL_WRITE_EXTATTRIBUTES: %m
error processing security information: %m
%s:%d:%s() extracting \"%s\" (%d bytes)\n
Could not zero destination file before copy: %m
copyfile
error processing extended attributes: %m
Mac OS X        
writing to output file got error: %m
reading from %s %s: %m
Invalid file descriptor offset, cannot perform a sparse copy: %m
%s:%d:%s() open successful on destination (%s)\n
open/malloc/stat on %s resource fork: %d: %m
%s:%d:%s() open successful on destination rsrc (%s)\n
add ACL_WRITE_DATA: %m
Destination %s already exists as a symlink, refusing to copy: %m
S
%s:%d:%s() closing %s fd: %d\n
COPYFILE_DEBUG
unexpected size (%ld) for \"%s\": %m
%s:%d:%s() unsetting group uuid attribute on %s\n
%s:%d:%s() couldn't stat destination file for st_flags (%d)\n
unable to punch trailing hole in destination file, offset %lld: %m
could not apply acl to destination file %s from source file %s: %m
%s%s%s
destination file %s changed behind our feet: %m
error processing data: %m
%s:%d:%s() no acl entries found (errno = %d)\n
%s:%d:%s() unsetting acl attribute on %s\n
source's xattr list size (%zu) exceeds the threshold (%d); trying to allocate: %m
%s:%d:%s() preallocating %lld bytes on destination\n
copyfile_check
fcopyfile
open_src_rsrc_fork
add ACL_APPEND_DATA: %m
com.apple.FinderInfo
(null dst)
com.apple.decmpfs
(null string)
/dev/null
 copied 32 bytes of \"%s\" data @ offset 0x%08x: %m
Incomplete or corrupt attribute entry: %m
%s:%d:%s()  extracting \"%s\" (32 bytes)\n
(rsrc)
```
