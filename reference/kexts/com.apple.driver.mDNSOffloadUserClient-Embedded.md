# `com.apple.driver.mDNSOffloadUserClient-Embedded`

- Name: mDNSOffloadUserClient-Embedded
- Version: `1.0.1b8`
- UUID: `9300A9D0-9C6A-301E-83F1-B99212F30D83`
- Source version: `130.40.1.0.0`
- Depends on: [`com.apple.iokit.IONetworkingFamily`](com.apple.iokit.IONetworkingFamily.md) 3.1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 13.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 13.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 13.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 13.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `mDNSHandoff` | 0x88 |  |
| `mDNSOffloadUserClient` | 0x2128 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000187a off=0x00e1c910-0x00e1e18a addr=0xfffffe0007e20910-0xfffffe0007e2218a r--/r--   __TEXT            
	sz=0x00000010 off=0x00e1cfe0-0x00e1cff0 addr=0xfffffe0007e20fe0-0xfffffe0007e20ff0               __TEXT.__const            
	sz=0x0000119a off=0x00e1cff0-0x00e1e18a addr=0xfffffe0007e20ff0-0xfffffe0007e2218a               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000037b4 off=0x03bb7160-0x03bba914 addr=0xfffffe000abbb160-0xfffffe000abbe914 r-x/r-x   __TEXT_EXEC       
	sz=0x00003554 off=0x03bb7160-0x03bba6b4 addr=0xfffffe000abbb160-0xfffffe000abbe6b4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000260 off=0x03bba6b4-0x03bba914 addr=0xfffffe000abbe6b4-0xfffffe000abbe914          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x0000012c off=0x04a3d3f8-0x04a3d524 addr=0xfffffe000ba413f8-0xfffffe000ba41524 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a3d3f8-0x04a3d4c0 addr=0xfffffe000ba413f8-0xfffffe000ba414c0               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000ba414c0-0xfffffe000ba41520               __DATA.__common           (Zerofill)
	sz=0x00000004 off=0x00000000-0x00000004 addr=0xfffffe000ba41520-0xfffffe000ba41524               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000ad0 off=0x014c1fb8-0x014c2a88 addr=0xfffffe00084c5fb8-0xfffffe00084c6a88 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x014c1fb8-0x014c1fc0 addr=0xfffffe00084c5fb8-0xfffffe00084c5fc0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x014c1fc0-0x014c1fc8 addr=0xfffffe00084c5fc0-0xfffffe00084c5fc8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000007d8 off=0x014c1fc8-0x014c27a0 addr=0xfffffe00084c5fc8-0xfffffe00084c67a0         __DATA_CONST.__const            
	sz=0x00000080 off=0x014c27a0-0x014c2820 addr=0xfffffe00084c67a0-0xfffffe00084c6820         __DATA_CONST.__kalloc_type      
	sz=0x000000f0 off=0x014c2820-0x014c2910 addr=0xfffffe00084c6820-0xfffffe00084c6910         __DATA_CONST.__kalloc_var       
	sz=0x00000130 off=0x014c2910-0x014c2a40 addr=0xfffffe00084c6910-0xfffffe00084c6a40         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x014c2a40-0x014c2a88 addr=0xfffffe00084c6a40-0xfffffe00084c6a88         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 85 at 0x04b00998
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     9300A9D0-9C6A-301E-83F1-B99212F30D83
008: LC_SOURCE_VERSION           130.40.1.0.0
009: LC_FUNCTION_STARTS          offset=0x004acf1f0 size=0x68
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `mDNSOffloadUserClient-Embedded`
- `CFBundleIdentifier`: `com.apple.driver.mDNSOffloadUserClient-Embedded`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `mDNSOffloadUserClient-Embedded`
- `CFBundleNumericVersion`: `16867336`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.1b8`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.1b8`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0d6`
- `OSBundleRequired`: `Network-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/mDNSOffloadUserClient-Embedded.kext`
- `_PrelinkExecutableLoadAddr`: `-2198891001584`
- `_PrelinkExecutableRelativePath`: `mDNSOffloadUserClient-Embedded`
- `_PrelinkExecutableSize`: `23594`
- `_PrelinkExecutableSourceAddr`: `-2198891001584`
- `_PrelinkKmodInfo`: `-2198827953160`

## Strings (70) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `mDNSOffloadUserClient: mDNSHandoff::init - RR records failed sanity check - outside of buffer\n`
- ` H=`
- `Keepalive_keepintvl`
- `mDNSOffloadUserClient: UID for mDNSResponder set to %d by info.plist\n`
- `mDNSOffloadUserClient: mDNSOffloadUserClient::doRequest - filter size mismatch %d wanted %d\n`
- `mDNSOffloadUserClient:  udpPorts 0x%llx\n`
- `t=%d i=%d c=%d h=%d.%d.%d.%d d=%d.%d.%d.%d l=%hd r=%hd m=%hhx:%hhx:%hhx:%hhx:%hhx:%hhx s=%d a=%d w=%hd`
- `mDNSOffloadUserClient: parse_keepalive_data_v6: scan failed, rc %d, token='%s'\n`
- `mDNSOffloadUserClient: getInfoFromInterfaces overflow: numIPv4 %d/%d, numIPv6 %d/%d\n`
- `mDNSOffloadUserClient:  command 0x%x\n`
- `mDNSOffloadUserClient:  rrBufferSize 0x%x\n`
- `site.mDNSHandoff`
- `mDNSOffloadUserClient: needsIPv6AddrHandoff() status 0x%x, err 0x%x\n`
- `mDNSOffloadUserClient`
- `121111121222121211111111111111111111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `mDNSOffloadUserClient - Unknown command: %d\n`
- `mDNSOffloadUserClient: mdns offset ok   [%d] %p, %p, %p\n`
- ` h=`
- `mDNSOffloadUserClient:  compression 0x%x\n`
- `mDNS_UID`
- `mDNSOffloadUserClient::doRequest - failed to create handoff\n`
- `12211112111122121`
- `mDNSOffloadUserClient: mDNSHandoff::init - invalid ResourceRecords offset array (%d)\n`
- `t=%d h=%d.%d.%d.%d d=%d.%d.%d.%d l=%hd r=%hd m=%hhx:%hhx:%hhx:%hhx:%hhx:%hhx s=%d a=%d w=%hd`
- `mDNSOffloadUserClient: parse_keepalive_data_v6: failed to parse: %s\n`
- `site.mDNSOffloadUserClient`
- `mDNSOffloadUserClient: GetKeepaliveData: tcpinfo worked. seq %u, ack %u, tx space %u (scaled %u, scale %u), unacked %llu\n`
- `mDNSOffloadUserClient: doRequestGated - pin/pout,size error\n`
- `mDNSOffloadUserClient: sleepWakeInterestHandler - released assertion %lld, rc=%d\n`
- `mDNSOffloadUserClient: keepalive IPv4 (%d): %s\n`
- `mDNSOffloadUserClient: getBufferData failed to allocate buffer, size %llu\n`
- `mDNSOffloadUserClient:  rrRecords 0x%llx\n`
- `mDNS_Keepalive`
- `mDNSOffloadUserClient: GetKeepaliveData: IPv6 tcp.info worked. seq %u, ack %u, tx space %u (scaled %u, scale %u), unacked %llu\n`
- `mDNSOffloadUserClient: mDNSHandoff::init - invalid ResourceRecord length %lld, offset array (%d)\n`
- `mDNSOffloadUserClient: parse_keepalive_data_v4: keep failed to parse, rc %d, buf='%s'\n`
- `mDNSOffloadUserClient: GetKeepaliveData: tcp.info sysctl failed, err=%d.  %x.%d -> %x.%d\n`
- `mDNSOffloadUserClient::doRequest - size mismatch %d wanted %d\n`
- `mDNSOffloadUserClient: getBufferData: prepare failed to map memory %x\n`
- `mDNSOffloadUserClient: getBufferData: read failed, %llu vs %llu\n`
- ` l=%hd r=%hd m=%hhx:%hhx:%hhx:%hhx:%hhx:%hhx s=%d a=%d w=%hd`
- `mDNSOffloadUserClient: Command buffer, size %ld\n`
- `site.void *`
- `1`
- `mDNSOffloadUserClient: getBufferData buffer too big, size %llu\n`
- `mDNSOffloadUserClient: getBufferData: failed to create memory map\n`
- `D=`
- `mDNSOffloadUserClient: parse_keepalive_data_v6 - parsed ok\n`
- `mDNS_Filter_Version`
- `mDNSOffloadUserClient: mDNS offload disabled via info.plist\n`
- `mDNSOffloadUserClient:  numTCPPorts 0x%x\n`
- `t=%d`
- `i=%d c=%d`
- `H=`
- `mDNSOffloadUserClient: GetKeepaliveData: attempting to sysctl for tcp.info sysctl: %x.%d -> %x.%d\n`
- `mDNSOffloadUserClient: keepalive IPv6 (%d): %s\n`
- `mDNSOffloadUserClient: parse_keepalive_data_v6: failed to get timeout.  rc=%d\n`
- `i=`
- `mDNS_KEY`
- `2009-07-30`
- `Keepalive_keepcnt`
- `mDNSHandoff`
- `mDNSOffloadUserClient: final keepalive retry count %u, interval %u ms\n`
- `mDNSOffloadUserClient:  numUDPPorts 0x%x\n`
- `mDNSOffloadUserClient:  numRRRecords 0x%x\n`
- `net.inet.tcp.info`
- `mDNSOffloadUserClient: GetKeepaliveData: tcp.info IPv6 sysctl failed, err=%d\n`
- `mDNS_DISABLE`
- `mDNSOffloadUserClient: ifnet_get_local_ports() returned 0x%x\n`
- `mDNSOffloadUserClient:  tcpPorts 0x%llx\n`
