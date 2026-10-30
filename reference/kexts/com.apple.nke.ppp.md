# `com.apple.nke.ppp`

- Name: PPP
- Version: `1.9`
- UUID: `390D3415-3B69-36AD-AA74-5C033D1C1BA0`
- Source version: `1043.0.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b1, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0b1, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0b1, [`com.apple.kpi.private`](com.apple.kpi.private.md) 10.0.0d1, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0b1

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
000: LC_SEGMENT_64 sz=0x00002170 off=0x00b984d0-0x00b9a640 addr=0xfffffe0007b9c4d0-0xfffffe0007b9e640 r--/r--   __TEXT            
	sz=0x00001968 off=0x00b98aa8-0x00b9a410 addr=0xfffffe0007b9caa8-0xfffffe0007b9e410               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000230 off=0x00b9a410-0x00b9a640 addr=0xfffffe0007b9e410-0xfffffe0007b9e640               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00007bd0 off=0x03901210-0x03908de0 addr=0xfffffe000a905210-0xfffffe000a90cde0 r-x/r-x   __TEXT_EXEC       
	sz=0x000074b0 off=0x03901210-0x039086c0 addr=0xfffffe000a905210-0xfffffe000a90c6c0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000720 off=0x039086c0-0x03908de0 addr=0xfffffe000a90c6c0-0xfffffe000a90cde0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x0000039c off=0x04a1f0a0-0x04a1f43c addr=0xfffffe000ba230a0-0xfffffe000ba2343c rw-/rw-   __DATA            
	sz=0x000002d0 off=0x04a1f0a0-0x04a1f370 addr=0xfffffe000ba230a0-0xfffffe000ba23370               __DATA.__data             
	sz=0x000000a1 off=0x00000000-0x000000a1 addr=0xfffffe000ba23370-0xfffffe000ba23411               __DATA.__bss              (Zerofill)
	sz=0x00000024 off=0x00000000-0x00000024 addr=0xfffffe000ba23418-0xfffffe000ba2343c               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000006f0 off=0x01489518-0x01489c08 addr=0xfffffe000848d518-0xfffffe000848dc08 rw-/rw-   __DATA_CONST      
	sz=0x00000040 off=0x01489518-0x01489558 addr=0xfffffe000848d518-0xfffffe000848d558         __DATA_CONST.__const            
	sz=0x00000300 off=0x01489558-0x01489858 addr=0xfffffe000848d558-0xfffffe000848d858         __DATA_CONST.__kalloc_type      
	sz=0x00000390 off=0x01489858-0x01489be8 addr=0xfffffe000848d858-0xfffffe000848dbe8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000020 off=0x01489be8-0x01489c08 addr=0xfffffe000848dbe8-0xfffffe000848dc08         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 232 at 0x04afcc18
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     390D3415-3B69-36AD-AA74-5C033D1C1BA0
008: LC_SOURCE_VERSION           1043.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004acb6b0 size=0xa8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `PPP`
- `CFBundleIdentifier`: `com.apple.nke.ppp`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `PPP`
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
- `NSHumanReadableCopyright`: `Copyright © 2000-2009 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.1`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/PPP.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893640496`
- `_PrelinkExecutableRelativePath`: `PPP`
- `_PrelinkExecutableSize`: `42956`
- `_PrelinkExecutableSourceAddr`: `-2198893640496`
- `_PrelinkKmodInfo`: `-2198828076896`

## Strings (128) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ppp_link_detach : (link = %s%d)\n`
- `pppserial_input: (ifnet = %s%d) (link = %s%d) too few input mbufs!\n`
- `ppp%d: decompression error\n`
- `122222122222222222222222222222222222222212222222222222222222222222222222221222222222222222222222222222222222122222222222222222222222222222222212222222222222222222222222222222221222222222222222222222222222222222122222222222222222222222222222222212222222222222222222222222222222221222222222222222222222`
- `pppserial_init: ppp_fam_init error = 0x%x\n`
- `ppp%d: Trying to send data with link detached\n`
- `ppp_if_init: lck_grp_alloc_init failed\n`
- `ppp_if_control: PPPIOCSMRU\n`
- `ppp_if_del_proto, ifp = %p\n`
- `ppp_ipv6_detach\n`
- `ppp%d: VJ uncompress failed on type PPP_VJC_COMP\n`
- `ppp_if_control: PPPIOCGUNIT\n`
- `ppp_link_control : PPPIOCDISCONN, (link = %s%d), detach from interface = %s%d \n`
- `ppp_link_send`
- `pppserial_ioctl: (ifnet = %s%d) (link = %s%d) TIOCFLUSH\n`
- ` `
- `11211111111111111`
- `%s: [ifnet = %s%d] [link = %s%d]\n`
- `%02x `
- `ppp_fam_ifoutput : no memory for transmit header\n`
- `pppserial_input: (ifnet = %s%d) (link = %s%d) no carrier\n`
- `ppp line %d input: %*D\n`
- `ppp%d: no compressor for [%x %x %x], %x\n`
- `pppserial_ioctl: (ifnet = %s%d) (link = %s%d) TCSAFLUSH\n`
- `lo0`
- `ppp%d: decomp_alloc failed\n`
- `ppp_link_control:  (link = %s%d), PPPIOCSFLAGS = 0x%x\n`
- `111121112221122222211111111222222211221122211122111222`
- `pppserial_ioctl: (ifnet = %s%d) (link = %s%d) TIOCSETD\n`
- `pppserial_input: (ifnet = %s%d) (link = %s%d) mbuf_setdata!\n`
- `ppp_domain_terminate : can't del proto from PPP domain, error = 0x%x\n`
- `ppp%d: VJ uncompress failed: trailingspace (%d) < hlen (%d) - vjlen (%d)\n`
- `ppp_if_ioctl, unsupported ioctl SIOCGIFMEDIA\n`
- `ppp_link_control:  (link = %s%d), PPPIOCGMRU = 0x%x\n`
- `pppserial_input: (ifnet = %s%d) (link = %s%d) packet too big, mru = %d, inlen = %d\n`
- `ppp_terminate: ppp_domain_dispose error = 0x%x\n`
- `%s:  0x  `
- `ppp_if_control: PPPIOCGDEBUG (level = 0x%x)\n`
- `ppp_if_control: PPPIOCSNPMODE/PPPIOCGNPMODE\n`
- `pppserial_input: (ifnet = %s%d) (link = %s%d) mbuf_setdata failed!\n`
- `ppp_comp_ccp: not enough data in mbuf (expected = %d, got = %d)\n`
- `  '`
- `site.struct ppp_if`
- `ppp_if_control: PPPIOCSFLAGS, old flags = 0x%x new flags = 0x%x, \n`
- `ppp_if_control: PPPIOCSMAXCID\n`
- `ppp_if_ioctl, SIOCSIFMTU\n`
- `pppserial_lk_ioctl: (ifnet = %s%d) (link = %s%d) ld = 0x%x, PPPIOCGXASYNCMAP\n`
- `pppserial_init: ppp_proto_add error = 0x%x\n`
- `ppp_proto_add : can't add proto to PPP domain, error = 0x%x\n`
- `ppp%d ppp_if_input mbuf_pullup len %d failed %d\n`
- `site.struct slcompress`
- `ppp_if_ioctl: cmd = SIOCSIFDSTADDR\n`
- `ppp_link_input: cannot pullup header\n`
- `ppp_ip_attach: ifnet_attach_protocol error = 0x%x\n`
- `ppp_ip_detach: ifnet_detach_protocol error = 0x%x\n`
- `ppp%d: comp_alloc failed\n`
- `ppp`
- `ppp_if_control: PPPIOCSDEBUG (level = 0x%x)\n`
- `ppp_link_control:  (link = %s%d), PPPIOCSMRU = 0x%x\n`
- `ppp_ipv6_ioctl: cmd = SIOCSIFADDR/SIOCAIFADDR\n`
- `pppserial_input: (ifnet = %s%d) (link = %s%d) no input mbufs!\n`
- `'\n`
- `ppp%d: mbuf_pulldown failed\n`
- `ppp_if_init: lck_grp_attr_alloc_init failed\n`
- `ppp_if_ioctl: cmd = SIOCADDMULTI/SIOCDELMULTI\n`
- `ppp_if_ioctl, unknown ioctl, cmd = 0x%x\n`
- `ppp_terminate: pppserial_dispose error = 0x%x\n`
- `ppp_terminate: ppp_link_dispose error = 0x%x\n`
- `ppp_ipv6_detach: ifnet_detach_protocol error = 0x%x\n`
- `   `
- `ppp%d: VJ uncompress failed on type TYPE_UNCOMPRESSED_TCP\n`
- `ppp_link_control : PPPIOCCONNECT, (link = %s%d), attach to interface = %d \n`
- `pppserial_input: (ifnet = %s%d) (link = %s%d) line error %x\n`
- `ppp_ipv6_attach: ifnet_attach_protocol family = 0x%x\n`
- `ppp_if_control: PPPIOCSNPAFMODE/PPPIOCGNPAFMODE\n`
- `site.struct pppserial`
- `ppp_terminate: ppp_ipv6_dispose error = 0x%x\n`
- `ppp_terminate: ppp_comp_dispose error = 0x%x\n`
- `ppp_i6_attach: ifnet_attach_protocol family = 0x%x\n`
- `PPP`
- `ppp_domain_terminate : can't del PPP domain, error = 0x%x\n`
- `ppp_if_init: lck_attr_alloc_init failed\n`
- `pppserial_lk_ioctl: (ifnet = %s%d) (link = %s%d) ld = 0x%x, PPPIOCSMRU = 0x%x\n`
- `pppserial_lk_ioctl: (ifnet = %s%d) (link = %s%d) ld = 0x%x, PPPIOCSXASYNCMAP\n`
- `ppp_ip_ioctl: cmd = SIOCSIFADDR/SIOCAIFADDR\n`
- `ppp_proto_input no space, so = %p, len = %d\n`
- `ppp_if_ioctl: cmd = SIOCSIFADDR/SIOCAIFADDR\n`
- `pppserial_lk_ioctl: (ifnet = %s%d) (link = %s%d) ld = 0x%x, PPPIOCGRASYNCMAP = 0x%x\n`
- `pppserial_ioctl: (ifnet = %s%d) (link = %s%d) TIOCGETD\n`
- `ppp_ip_attach: name = %s, unit = %d\n`
- `111121211212221221122111111221`
- `ppp_if_ioctl: cmd = SIOCSIFFLAGS\n`
- `???`
- `pppserial_attach, error = %d, (ld = 0x%x)\n`
- `site.struct ppp_comp`
- `%s: \n`
- `pppserial_lk_ioctl: (ifnet = %s%d) (link = %s%d) ld = 0x%x, PPPIOCSASYNCMAP = 0x%x\n`
- `pppserial_lk_ioctl: (ifnet = %s%d) (link = %s%d) ld = 0x%x, PPPIOCSRASYNCMAP = 0x%x\n`
- `pppserial_input: (ifnet = %s%d) (link = %s%d) missing UI (0x3), got 0x%x\n`
- `pppserial_input: (ifnet = %s%d) (link = %s%d) bad protocol %x\n`
- `ppp_if_ioctl, SIOCGPPPSTATS\n`
- `ppp_if_add_proto = %d, ifp = %p\n`
- `pppserial_ioctl: (ifnet = %s%d) (link = %s%d) TIOCMGET\n`
- `pppserial_input: (ifnet = %s%d) (link = %s%d) garbage received: 0x%x (need 0xFF)\n`
- `ppp_terminate: ppp_proto_remove error = 0x%x\n`
- `ppp_if_ioctl: cmd = SIOCDIFADDR\n`
- `pppserial_input: (ifnet = %s%d) (link = %s%d) too short (%d)\n`
- `ppp%d: VJ structure not allocated\n`
- `ppp_if_control: PPPIOCSDELEGATE\n`
- `ppp_ipv6_attach: ifnet_attach_protocol error = 0x%x\n`
- `ppp_link_input`
- `ppp_terminate: ppp_ip_dispose error = 0x%x\n`
- `  `
- `N`
- `ppp_if_control: unknown ioctl, cmd = 0x%x\n`
- `ppp_fam_demux, ifp = %p, bad proto = 0x%x\n`
- `ppp_ipv6_attach: name = %s, unit = %d\n`
- `ppp_ip_detach\n`
- `ppp_if_control: PPPIOCGFLAGS\n`
- `serial`
- `pppserial_input: (ifnet = %s%d) (link = %s%d) bad fcs %x, pkt len %d\n`
- `ppp_terminate: ppp_if_dispose error = 0x%x\n`
- `%c`
- `ppp_if_control: PPPIOCGIDLE\n`
- `ppp_link_control:  (link = %s%d), PPPIOCGFLAGS = 0x%x\n`
- `pppserial_open EPERM\n`
- `pppserial_lk_ioctl: (ifnet = %s%d) (link = %s%d) ld = 0x%x, PPPIOCGASYNCMAP = 0x%x\n`
- `pppserial_ioctl: (ifnet = %s%d) (link = %s%d) PPPIOCGCHAN = %d\n`
