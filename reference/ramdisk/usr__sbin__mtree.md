# `/usr/sbin/mtree`

From the upgrade restore ramdisk (141-29011-104.dmg). 108,432 bytes.

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
malloc
get_protection_class: getattrlist failed for path <%s>
purgeable=%llu
uname
illegal seed value -- %s
%s: file flags not set: %s\n
line %d: invalid file mode %s
%sRIPEMD160 expected %s found %s\n
found %.24s.%09ld\n
 modified
xattrsdigest=%s.%llu
uid
 ptime=%ld.%09ld
line %d: %s
%s checksum: %lu
line %d: invalid value for protectionclass: %s
v24@?0B8^{dispatch_data_s=}12i20
found %.24s.%09ld
%sMD5: %s: %s\n
%sxattr count expected %llu found %llu for file %s\n
 gname=%s
ptime: getattrlist
inode
%s:%s
\ttype expected %s found %s\n
 gid=%lu
cksum
line %d: invalid inode %s
siblingid=%llu
(%d:%d)
set
 nxattr=%llu
 (directory not created: %s)
block
mtree exiting with a non-zero status: %d
line %d: invalid xattr count %s
directory
%suser expected %lu found %lu
nlink=%u
%FT%T
line %d: missing value
Could not get gname for gid=%u
ptime=%ld.%09ld
flags
md5digest
inode=%llu
ripemd160digest
line %d too long
invalid root in vwalk
com.apple.mtree.io
uid=%u
= \t\n
%s missing
user
0123456789abcdef
ripemd160digest=%s
 mode=%#o
 protectionclass=%d
ACCESS
 sha256digest=%s
none
SHA256_Path_ACL: SHA256_Data
fts_open()
nlink
nxattr
line %d: invalid private id %s
line %d: invalid sibling id %s
dir
atime=%ld.%09ld
xattrsdigest
Cannot parse timestamp '%s' using format \"%s\"\n
%sxattrsdigest missing, expected: %s\n
sha256digest=%s
Time is too far in the past
line %d: invalid uid %s
%s: permissions not set: %s\n
%sRIPEMD160: %s: %s\n
%stime added to parent folder expected %.24s.%09ld found that it is not supported\n
char
Could not get uname for uid=%u
gid=%u
time=%ld.%09ld
%s%s %s
invalid flag %s
%sSHA-256: %s: %s\n
%smetadata modification time expected %.24s.%09ld 
%*s..\n
%s extra
Time is more then 30 days in the future
 sha1digest=%s
get_xattr_count: failed to allocate xattr buffer size:(%zd)\n
%ssize expected %jd found %jd\n
atime
calloc
line %d: fts_open
%llu
nxattr=%llu
line %d: invalid time %s
line %d: unknown file type %s
 mode=%o
 purgeable=%llu
size=%jd
ctime=%ld.%09ld
ignore
.
%sgid expected %lu found %lu
file
%s: %s
%slink_count expected %u found %u\n
%sSHA-1: %s: %s\n
BIRTH
 %s
symlink
miss returned non-zero rrval: %d\n
%sbirth time expected %.24s.%09ld 
nochange
w:
%s%s/
 (created)
SHA256_Path_XATTRs getxattr of \"%s\" at path \"%s\" failed with error
%s
btime=%ld.%09ld
 \t,
mval returned a non-zero mval: %d\n
%sflags expected \"%s\"
\n\t 
line %d: invalid value for dataless: %s
rval returned a non-zero rval: %d\n
SHA256_Path_ACL: getattrlist
%slink_ref expected %s found %s\n
%sinvalid sibling id(original sibling id: %llu and the new sibling id: %llu)\n
statf(): calloc() failed
dataless=%llu
r
line %d: unknown keyword %s
fifo
#\t   user: %s\n#\tmachine: %s\n
 xattrsdigest=%s.%llu
btime
dataless
 gid=%d
 btime=%ld.%09ld
 (%s not created: group not specified)
%s - SHA256_Path_XATTRs APFSIOC_XDSTREAM_OBJ_ID failed with %d
%*s    %s
\n error deleting item (or descendant) at path %s (%s)
i24@?0r^v8r^v16
protectionclass=%u
 nlink=1
authapfs
CHANGE
 uname=%s
 uid=%lu
 flags=%s
symlink %s is ill-encoded
line %d: unknown user %s
 nlink=%d
\t
link=%s
protectionclass
usage: mtree [-LPUScdeinNqruxwD] [-f spec] [-K key] [-k key] [-p path] [-s seed] [-m xml dictionary] [-t timestamp]\n\t[-X excludes]\n
strdup
md5digest=%s
line %d: unknown group %s
line %d: invalid size %s
%smodification time expected %.24s.%09ld 
link
socket
get_sibling_id: getattrlist failed for %s\n
%sSHA-256 expected %s found %s\n
%spermissions expected %#o found %#o
 \\\n%*s
acldigest
sha256digest
?*[
 ctime=%ld.%09ld
%s, %s:%s
%sMD5 expected %s found %s\n
%stime added to parent folder expected %.24s.%09ld 
%sdataless expected %llu found %llu for file %s\n
mode=%#o
acldigest=%s
line %d: invalid link count %s
 md5digest=%s
%sinode expected %llu found %llu\n
 \t\n
 siblingid=%llu
get_xattr_count: listxattr failed with %s(%d) while calculating xattr buffer size for path<%s>\n
%sacldigest missing, expected: %s\n
 rmd160digest=%s
group
%sprotectionclass expected %d found %d for file %s\n
ctime
, not removed :%s
cksum=%lu
purgeable
e:
line %d: slash character in file name
get_xattr_count: listxattr failed with %s(%d) for <%s>\n
ptime
dev=%s result=%d 
 size=%jd
MODIFICATION
 found \"%s\"
unknown
escape_path(): calloc() failed
gname
could not write manifest to the file\n
filename %s is ill-encoded
%*s%s
Could not open metrics log file %s
 uid=%d
type=%s
memory allocation error
line %d: invalid checksum %s
 time=%ld.%09ld
set_key_value_pair: key/value is null
 (%s not created: user not specified)
 (symlink not created: %s)\n
 not modified: %s\n
%scksum: %s: %s\n
%sSHA-1 expected %s found %s\n
%sxattrsdigest expected %s found %s\n
%spurgeable expected %llu found %llu for file %s\n
flags=%s
sha1digest
cannot generate the XML dictionary
v12@?0i8
%s changed\n
%*s
/set type=file
gid
 atime=%ld.%09ld
%s: %s not modified: %s\n
 (directory not created: mode not specified)
%sacldigest expected %s found %s\n
%ssibling id expected %llu found %llu\n
#\t   tree: %s\n#\t   date: %s
# %s\n
type
line %d: no parent node
line %d, invalid value for purgeable: %s
%saccess time expected %.24s.%09ld 
DATEADDED
%*s# %s\n
time
fl=%d time=%ld\n
line %d: invalid flag %s
line %d: invalid gid %s
siblingid
 cksum=%lu
 inode=%llu
line %d: missing field
user & group
B40@?0^{dispatch_data_s=}8Q16r^v24Q32
mode
size
unset
 dataless=%lu
com.apple.ResourceFork
%scksum expected %lu found %lu\n
cdef:iK:k:LNnPp:qrs:UuvwxX:m:F:t:E:SD
, removed
uname=%s
gname=%s
/set type=dir
 acldigest=%s
w
get_purgeable_flags: fsctl failed for path <%s>
sha1digest=%s
vwalk failed: r1: %d and r2: %d\n
mtree_verifyspec returned a non-zero status: %d
\t\t
```
