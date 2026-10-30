# `/usr/lib/libbz2.1.0.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 137,552 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 18 (Size: 1544)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (2)

- `/usr/lib/libbz2.1.0.dylib (compatibility version 1.0.0, current version 1.0.8)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (40)

```
\n*** A special note about internal error number 1007 ***\n\nExperience suggests that a common cause of i.e. 1007\nis unreliable memory or other hardware.  The 1007 assertion\njust happens to cross-check the results of huge numbers of\nmemo
w
MEM_ERROR
IO_ERROR
    final combined CRC = 0x%08x\n   
      pass %d: size is %d, grp uses are 
code lengths %d, 
codes %d\n
        depth %6d has 
%6d unresolved strings\n
b
PARAM_ERROR
      %d in block, %d after MTF & 1-2 coding, %d+2 syms in use\n
rt+rld
    too repetitive; using fallback sorting algorithm\n
        bucket sorting ...\n
        reconstructing block ...\n
\n    combined CRCs: stored = 0x%08x, computed = 0x%08x
r
        main sort initialise ...\n
        %d pointers, %d sorted, %d scanned\n
DATA_ERROR
UNEXPECTED_EOF
    block %d: crc = 0x%08x, combined CRC = 0x%08x, size = %d\n
%d 
      bytes: mapping %d, 
        qsort [0x%x, 0x%x]   done %d   this %d\n
OK
OUTBUFF_FULL
???
      initial group %d, [%d .. %d], has %d syms (%4.1f%%)\n
      %d work, %d block, ratio %5.2f\n
1.0.8, 13-Jul-2019
SEQUENCE_ERROR
selectors %d, 
\n\nbzip2/libbzip2: internal error number %d.\nThis is a bug in bzip2/libbzip2, %s.\nPlease report it to: bzip2-devel@sourceware.org.  If this happened\nwhen you were using some program which uses libbzip2 as a\ncomponent, you should also r
DATA_ERROR_MAGIC
\n    [%d: huff+mtf 
 {0x%08x, 0x%08x}
CONFIG_ERROR
```
