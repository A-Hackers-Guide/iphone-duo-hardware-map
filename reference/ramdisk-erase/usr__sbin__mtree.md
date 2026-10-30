# `/usr/sbin/mtree`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 108,432 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = EXECUTE
CPU           = AARCH64, 0xc caps: USR00
Commands      = 19 (Size: 1864)
Flags         = NoUndefs, DyldLink, TwoLevel, PIE
```

## Linked libraries (2)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (273)

```
#\t   tree: %s\n#\t   date: %s
atime=%ld.%09ld
siblingid=%llu
siblingid
, removed
, not removed :%s
 modified
%*s..\n
mval returned a non-zero mval: %d\n
user & group
%s: %s not modified: %s\n
%smetadata modification time expected %.24s.%09ld 
Could not get gname for gid=%u
com.apple.ResourceFork
%sflags expected \"%s\"
w:
cannot generate the XML dictionary
 (%s not created: group not specified)
miss returned non-zero rrval: %d\n
 uname=%s
ptime: getattrlist
filename %s is ill-encoded
%stime added to parent folder expected %.24s.%09ld 
%*s%s
line %d: unknown user %s
\n error deleting item (or descendant) at path %s (%s)
user
%sSHA-256: %s: %s\n
 nxattr=%llu
gid
\n\t 
get_xattr_count: failed to allocate xattr buffer size:(%zd)\n
block
sha256digest=%s
time=%ld.%09ld
 acldigest=%s
e:
w
mtree_verifyspec returned a non-zero status: %d
ptime=%ld.%09ld
acldigest
sha1digest
uname
line %d: missing field
 siblingid=%llu
strdup
get_xattr_count: listxattr failed with %s(%d) while calculating xattr buffer size for path<%s>\n
%sbirth time expected %.24s.%09ld 
size
rval returned a non-zero rval: %d\n
line %d: invalid time %s
%ssibling id expected %llu found %llu\n
#\t   user: %s\n#\tmachine: %s\n
fts_open()
xattrsdigest=%s.%llu
 uid=%lu
protectionclass
com.apple.mtree.io
\ttype expected %s found %s\n
SHA256_Path_ACL: SHA256_Data
%spurgeable expected %llu found %llu for file %s\n
# %s\n
protectionclass=%u
atime
ctime
line %d: unknown group %s
 atime=%ld.%09ld
found %.24s.%09ld
DATEADDED
md5digest=%s
 gid=%lu
sha256digest
time
line %d: invalid checksum %s
\t\t
%s - SHA256_Path_XATTRs APFSIOC_XDSTREAM_OBJ_ID failed with %d
statf(): calloc() failed
%*s
fl=%d time=%ld\n
%s: file flags not set: %s\n
%sRIPEMD160 expected %s found %s\n
mode=%#o
flags=%s
mtree exiting with a non-zero status: %d
calloc
line %d: invalid link count %s
invalid root in vwalk
%smodification time expected %.24s.%09ld 
found %.24s.%09ld\n
 mode=%#o
btime
= \t\n
 (directory not created: mode not specified)
 found \"%s\"
cksum
get_xattr_count: listxattr failed with %s(%d) for <%s>\n
%sMD5 expected %s found %s\n
memory allocation error
Time is more then 30 days in the future
line %d: unknown file type %s
%scksum expected %lu found %lu\n
BIRTH
char
ctime=%ld.%09ld
nochange
uid
set
 xattrsdigest=%s.%llu
line %d: invalid size %s
get_purgeable_flags: fsctl failed for path <%s>
%sSHA-1 expected %s found %s\n
set_key_value_pair: key/value is null
 rmd160digest=%s
unknown
line %d: invalid gid %s
malloc
 dataless=%lu
SHA256_Path_XATTRs getxattr of \"%s\" at path \"%s\" failed with error
type=%s
 (created)
v24@?0B8^{dispatch_data_s=}12i20
none
 flags=%s
(%d:%d)
get_sibling_id: getattrlist failed for %s\n
%sacldigest missing, expected: %s\n
gname=%s
gname
%sSHA-256 expected %s found %s\n
r
%FT%T
 sha1digest=%s
 \\\n%*s
 \t\n
line %d: invalid private id %s
i24@?0r^v8r^v16
line %d: %s
uname=%s
type
line %d: invalid xattr count %s
 purgeable=%llu
fifo
xattrsdigest
%s checksum: %lu
%*s    %s
cksum=%lu
sha1digest=%s
line %d: invalid inode %s
 (%s not created: user not specified)
%s: permissions not set: %s\n
ACCESS
link=%s
purgeable=%llu
 %s
%s%s/
 time=%ld.%09ld
symlink
 (symlink not created: %s)\n
btime=%ld.%09ld
%s extra
0123456789abcdef
%sinode expected %llu found %llu\n
uid=%u
unset
authapfs
%sxattrsdigest expected %s found %s\n
 btime=%ld.%09ld
%s
SHA256_Path_ACL: getattrlist
%sRIPEMD160: %s: %s\n
dir
line %d: invalid file mode %s
line %d: invalid value for dataless: %s
line %d, invalid value for purgeable: %s
line %d too long
%s%s %s
 gid=%d
file
%llu
dataless=%llu
 nlink=1
 ptime=%ld.%09ld
vwalk failed: r1: %d and r2: %d\n
 (directory not created: %s)
.
%sprotectionclass expected %d found %d for file %s\n
Could not get uname for uid=%u
inode=%llu
 gname=%s
Cannot parse timestamp '%s' using format \"%s\"\n
v12@?0i8
%ssize expected %jd found %jd\n
/set type=file
md5digest
nlink
purgeable
 uid=%d
 \t,
invalid flag %s
%sSHA-1: %s: %s\n
%sacldigest expected %s found %s\n
symlink %s is ill-encoded
%saccess time expected %.24s.%09ld 
%*s# %s\n
%s: %s
size=%jd
ptime
line %d: missing value
 protectionclass=%d
?*[
line %d: invalid sibling id %s
%sxattrsdigest missing, expected: %s\n
escape_path(): calloc() failed
directory
%s changed\n
%sdataless expected %llu found %llu for file %s\n
gid=%u
dataless
ignore
ripemd160digest
dev=%s result=%d 
 mode=%o
%suser expected %lu found %lu
MODIFICATION
/set type=dir
%s:%s
Could not open metrics log file %s
get_protection_class: getattrlist failed for path <%s>
%spermissions expected %#o found %#o
Time is too far in the past
could not write manifest to the file\n
line %d: fts_open
ripemd160digest=%s
line %d: unknown keyword %s
%sgid expected %lu found %lu
nlink=%u
mode
illegal seed value -- %s
line %d: no parent node
CHANGE
%stime added to parent folder expected %.24s.%09ld found that it is not supported\n
\t
%sMD5: %s: %s\n
socket
flags
 cksum=%lu
%slink_ref expected %s found %s\n
cdef:iK:k:LNnPp:qrs:UuvwxX:m:F:t:E:SD
line %d: invalid flag %s
 md5digest=%s
 inode=%llu
 not modified: %s\n
%sxattr count expected %llu found %llu for file %s\n
acldigest=%s
usage: mtree [-LPUScdeinNqruxwD] [-f spec] [-K key] [-k key] [-p path] [-s seed] [-m xml dictionary] [-t timestamp]\n\t[-X excludes]\n
%s, %s:%s
line %d: slash character in file name
 nlink=%d
 sha256digest=%s
%slink_count expected %u found %u\n
nxattr
group
%scksum: %s: %s\n
line %d: invalid uid %s
line %d: invalid value for protectionclass: %s
 ctime=%ld.%09ld
%sinvalid sibling id(original sibling id: %llu and the new sibling id: %llu)\n
 size=%jd
B40@?0^{dispatch_data_s=}8Q16r^v24Q32
link
nxattr=%llu
inode
%s missing
```
