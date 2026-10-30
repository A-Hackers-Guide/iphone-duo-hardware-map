# `com.apple.nke.l2tp`

- Name: L2TP
- Version: `1.9`
- UUID: `02729808-EA63-32C3-91C0-8B423DF76C8B`
- Source version: `1043.0.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b1, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0b1, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0b1, [`com.apple.kpi.private`](com.apple.kpi.private.md) 10.0.0d1, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0b1, [`com.apple.nke.ppp`](com.apple.nke.ppp.md) 1.8

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (0) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001098 off=0x00b97430-0x00b984c8 addr=0xfffffe0007b9b430-0xfffffe0007b9c4c8 r--/r--   __TEXT            
	sz=0x00000a63 off=0x00b97a08-0x00b9846b addr=0xfffffe0007b9ba08-0xfffffe0007b9c46b               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000058 off=0x00b98470-0x00b984c8 addr=0xfffffe0007b9c470-0xfffffe0007b9c4c8               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x000043e4 off=0x038fce20-0x03901204 addr=0xfffffe000a900e20-0xfffffe000a905204 r-x/r-x   __TEXT_EXEC       
	sz=0x00003ed4 off=0x038fce20-0x03900cf4 addr=0xfffffe000a900e20-0xfffffe000a904cf4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000510 off=0x03900cf4-0x03901204 addr=0xfffffe000a904cf4-0xfffffe000a905204          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000012d8 off=0x04a1ddc8-0x04a1f0a0 addr=0xfffffe000ba21dc8-0xfffffe000ba230a0 rw-/rw-   __DATA            
	sz=0x00000130 off=0x04a1ddc8-0x04a1def8 addr=0xfffffe000ba21dc8-0xfffffe000ba21ef8               __DATA.__data             
	sz=0x00000150 off=0x00000000-0x00000150 addr=0xfffffe000ba21ef8-0xfffffe000ba22048               __DATA.__common           (Zerofill)
	sz=0x00001058 off=0x00000000-0x00001058 addr=0xfffffe000ba22048-0xfffffe000ba230a0               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000005b0 off=0x01488f68-0x01489518 addr=0xfffffe000848cf68-0xfffffe000848d518 rw-/rw-   __DATA_CONST      
	sz=0x00000200 off=0x01488f68-0x01489168 addr=0xfffffe000848cf68-0xfffffe000848d168         __DATA_CONST.__kalloc_type      
	sz=0x000000a0 off=0x01489168-0x01489208 addr=0xfffffe000848d168-0xfffffe000848d208         __DATA_CONST.__kalloc_var       
	sz=0x00000288 off=0x01489208-0x01489490 addr=0xfffffe000848d208-0xfffffe000848d490         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000088 off=0x01489490-0x01489518 addr=0xfffffe000848d490-0xfffffe000848d518         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 179 at 0x04afc94c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     02729808-EA63-32C3-91C0-8B423DF76C8B
008: LC_SOURCE_VERSION           1043.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004acb648 size=0x68
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `L2TP`
- `CFBundleIdentifier`: `com.apple.nke.l2tp`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `L2TP`
- `CFBundleNumericVersion`: `26247168`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.9`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.9`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2003-2009 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/L2TP.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893644752`
- `_PrelinkExecutableRelativePath`: `L2TP`
- `_PrelinkExecutableSize`: `27908`
- `_PrelinkExecutableSourceAddr`: `-2198893644752`
- `_PrelinkKmodInfo`: `-2198828081720`

## Strings (69) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `l2tp_udp_init: can't alloc mutex\n`
- `site.struct l2tp_wan`
- `L2TP domain terminate : PF_PPP domain does not exist...\n`
- `L2TP command (%p): set peer window = %d\n`
- `L2TP command (%p): get tunnel id = 0x%x\n`
- `L2TP command (%p): set peer tunnel id = 0x%x\n`
- `L2TP command (%p): get new tunnel id = 0x%x\n`
- `L2TP command (%p): set delegated pid = %d\n`
- `l2tp_handle_control mbuf_pullup len %d failed %d\n`
- `111121112221122222211111111`
- `L2TP_wan_attach, error = %d, (ld = %p)\n`
- `L2TP domain init : can't init l2tp protocol RFC, err : %d\n`
- `L2TP domain is in use and cannot terminate, err : %d\n`
- `L2TP command (%p): unknown command = %d\n`
- `111222222`
- `L2TP command (%p): set tunnel id = 0x%x\n`
- `l2tp_rfc_output_queued mbuf_pullup len %d failed %d\n`
- `l2tp_udp_init: can't alloc mutex attributes\n`
- `L2TP domain init\n`
- `L2TP domain init : can't add proto to l2tp domain, err : %d\n`
- `L2TP domain init complete\n`
- `L2TP prepare for freeing (%p)\n`
- `L2TP command (%p): set initial timeout = %d (seconds)\n`
- `l2tp_rfc_lower_input: cannot pullup l2tp header (len %d)\n`
- `site.struct l2tp_elem`
- `N`
- `L2TP domain terminate\n`
- `L2TP command (%p): get our IP address = %d.%d.%d.%d, port %d\n`
- `l2tp_rfc_output_control mbuf_pullup len %d failed %d\n`
- `l2tp_udp`
- `l2tp_udp_init_threads: changing # of threads from %d to %d\n`
- `l2tp_udp_thread_func terminate`
- `L2TP domain terminate : l2tp_wan_dispose, err : %d\n`
- `11111122211222221111`
- `L2TP command (%p): get peer IP address = %d.%d.%d.%d, port %d\n`
- `site.struct l2tp_udp_thread`
- `l2tp`
- `L2TP command (%p): get flags = 0x%x\n`
- `L2TP command (%p): set session id = 0x%x\n`
- `L2TP command (%p): accept\n`
- `12112221`
- `L2TP command (%p): set window = %d\n`
- `L2TP command (%p): set baudrate of the tunnel = %d\n`
- `l2tp_udp_init: can't alloc mutex group attributes\n`
- `l2tp_udp_init: can't alloc mutex group\n`
- `L2TP domain init : PF_PPP domain does not exist...\n`
- `l2tp_timer_sleep`
- `L2TP command (%p): set flags = 0x%x\n`
- `L2TP domain terminate : can't del proto from l2tp domain, err : %d\n`
- `site.struct l2tp_rfc`
- `L2TP command (%p): set max retries = %d\n`
- `on`
- `L2TP output packet contains too many mbufs, circular route suspected for %s%d\n`
- `l2tp_rfc_lower_input mbuf_pullup len %d failed %d\n`
- `L2TP command (%p): set peer session id = 0x%x\n`
- `l2tp_udp_init_threads: can't alloc mutex\n`
- `l2tp_udp_init_threads: kernel_thread_start failed, error %d\n`
- `L2TP command (%p): get session id = 0x%x\n`
- `L2TP command (%p): get baudrate of the tunnel = %d\n`
- `L2TP command (%p): set timeout cap = %d (seconds)\n`
- `L2TP command (%p): set reliability layer %s\n`
- `l2tp_handle_data mbuf_pullup len %lu failed %d\n`
- `l2tp_udp_dispose_threads`
- `l2tp_udp_thread_func`
- `L2TP`
- `L2TP free (%p)\n`
- `L2TP command (%p): set peer IP address = no address\n`
- `L2TP command (%p): set our IP address = no address\n`
- `off`
