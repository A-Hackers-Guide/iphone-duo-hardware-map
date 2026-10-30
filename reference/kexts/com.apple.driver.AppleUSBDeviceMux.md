# `com.apple.driver.AppleUSBDeviceMux`

- Name: AppleUSBDeviceMux
- Version: `1.0.0d1`
- UUID: `B8FE497C-F7E1-3E3A-B56A-4DBF80E2B129`
- Source version: `574.0.0.0.0`
- Depends on: [`com.apple.iokit.IOUSBDeviceFamily`](com.apple.iokit.IOUSBDeviceFamily.md) 2.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### Apple USB Device Multiplexor
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBDeviceMux`
- `IOClass`: `AppleUSBDeviceMux`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUSBDeviceMux`
- `IOPropertyMatch`:
  - `USBDeviceFunction`: `AppleUSBMux`
- `IOProviderClass`: `IOUSBDeviceInterface`
- `IOResourceMatch`: `IOBSD`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUSBDeviceMux` | 0x1d0 | IOService → IORegistryEntry |
| `IOSocketEventSource` | 0x68 | IOEventSource |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001a0d off=0x008d13c0-0x008d2dcd addr=0xfffffe00078d53c0-0xfffffe00078d6dcd r--/r--   __TEXT            
	sz=0x00000034 off=0x008d1a40-0x008d1a74 addr=0xfffffe00078d5a40-0xfffffe00078d5a74               __TEXT.__const            
	sz=0x00001359 off=0x008d1a74-0x008d2dcd addr=0xfffffe00078d5a74-0xfffffe00078d6dcd               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00005ce0 off=0x02b1c550-0x02b22230 addr=0xfffffe0009b20550-0xfffffe0009b26230 r-x/r-x   __TEXT_EXEC       
	sz=0x00005820 off=0x02b1c550-0x02b21d70 addr=0xfffffe0009b20550-0xfffffe0009b25d70          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000004c0 off=0x02b21d70-0x02b22230 addr=0xfffffe0009b25d70-0xfffffe0009b26230          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000134 off=0x049d0c30-0x049d0d64 addr=0xfffffe000b9d4c30-0xfffffe000b9d4d64 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049d0c30-0x049d0cf8 addr=0xfffffe000b9d4c30-0xfffffe000b9d4cf8               __DATA.__data             
	sz=0x00000068 off=0x00000000-0x00000068 addr=0xfffffe000b9d4cf8-0xfffffe000b9d4d60               __DATA.__common           (Zerofill)
	sz=0x00000004 off=0x00000000-0x00000004 addr=0xfffffe000b9d4d60-0xfffffe000b9d4d64               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000e90 off=0x012a3e48-0x012a4cd8 addr=0xfffffe00082a7e48-0xfffffe00082a8cd8 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x012a3e48-0x012a3e58 addr=0xfffffe00082a7e48-0xfffffe00082a7e58         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x012a3e58-0x012a3e68 addr=0xfffffe00082a7e58-0xfffffe00082a7e68         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000780 off=0x012a3e68-0x012a45e8 addr=0xfffffe00082a7e68-0xfffffe00082a85e8         __DATA_CONST.__const            
	sz=0x00000440 off=0x012a45e8-0x012a4a28 addr=0xfffffe00082a85e8-0xfffffe00082a8a28         __DATA_CONST.__kalloc_type      
	sz=0x00000260 off=0x012a4a28-0x012a4c88 addr=0xfffffe00082a8a28-0xfffffe00082a8c88         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x012a4c88-0x012a4cd8 addr=0xfffffe00082a8c88-0xfffffe00082a8cd8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 162 at 0x04aeb8ac
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     B8FE497C-F7E1-3E3A-B56A-4DBF80E2B129
008: LC_SOURCE_VERSION           574.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab7488 size=0x90
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleUSBDeviceMux`
- `CFBundleIdentifier`: `com.apple.driver.AppleUSBDeviceMux`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUSBDeviceMux`
- `CFBundleNumericVersion`: `16785409`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0d1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2006-2011 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUSBDeviceMux.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896553024`
- `_PrelinkExecutableRelativePath`: `AppleUSBDeviceMux`
- `_PrelinkExecutableSize`: `34481`
- `_PrelinkExecutableSourceAddr`: `-2198896553024`
- `_PrelinkKmodInfo`: `-2198828397520`

## Strings (145) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `void AppleUSBDeviceMux::bmsRetain(struct BulkUSBMuxSession *, const char *)`
- `DebugLevel`
- `void AppleUSBDeviceMux::vsendMuxRST(struct tcphdr *, bool, const char *, va_list)`
- `void AppleUSBDeviceMux::bmsRelease(struct BulkUSBMuxSession *, const char *)`
- `site.struct USBWriteBuffer`
- `%s: mbuf_gethdr failed, out of mbufs?`
- `OUT %u %d->%d %u:%u(%d) %s%s%s%s ack=%u win=%d\n`
- `%s OUT ZLP\n`
- `%s space for only %d byte message\n`
- `111222221221`
- `handleMuxInput`
- `%s _headerLength == 0\n`
- `IOReturn AppleUSBDeviceMux::allocateUSBReadBuffers()`
- `resyncWithHost`
- `Error: %s IOSocketEventSource::socketEventSource failed\n`
- `%s th.th_seq(0x%x) + length(%lu) > advertised window(0x%x) by %lu\n`
- `writeMbufToUSB`
- `startUSBWrite`
- `%s %d leading space, _headerLength = %d\n`
- `%s failed`
- `%s::%s: USB mux statistics: \n`
- `AppleUSBDeviceMux.cpp`
- `23:29:00`
- `%s failed to allocate read IO buffer %d\n`
- `IN  Copying %lu byte mbuf\n`
- `%s send error: %d`
- `%s Received short packet (%d bytes)\n`
- `%s IOMallocZeroData (debug_buffer) returned NULL\n`
- `%s:%d USB write status = %#x\n`
- `site.struct USBReadBuffer`
- `detected duplicate packet. Expected %d received %d\n`
- `%s:%d USB read status = %#x\n`
- `%s failed to allocate IOMemoryDescriptor withRanges (%lu ranges)\n`
- `void AppleUSBDeviceMux::asyncWriteComplete(struct USBWriteBuffer *, IOReturn, UInt32)`
- `Error: %s sock_getsockopt SO_SNDBUF failed: %d\n`
- `%s th.th_seq = %u, expected %u\n`
- `%s The usbmuxd attempted to set the log level but its version supposedly doesn't support it\n`
- `%s Version packet too short (%d bytes)\n`
- `1211121112111`
- `%s sock_connect failed: %d\n`
- `%s failed to allocate USBReadBuffer object %d\n`
- `121`
- `Error: %s sock_socket failed: %d\n`
- `%s failed to allocate IOMemoryDescriptor withRanges (%d ranges)\n`
- `startUSBRead`
- `%s finalizeConfiguration\n`
- `handleMuxTCPInput`
- `%s IOMallocZeroData returned NULL\n`
- `%s internal error, mbuf chain is too short, %d bytes remaining\n`
- `AppleUSBDeviceMux`
- `speed`
- `%s Log Level packet too short (%d bytes)\n`
- `Partial packet was discarded successfully.\n`
- `%s IOMallocZeroData (debug_buffer_as_string) returned NULL\n`
- `OUT %u done.\n`
- `%s connection closed`
- `Error: %s sock_ioctl(FIONBIO) failed: %d\n`
- `%s reducing send size to failsafe size %d\n`
- `%s pushing onto block queue\n`
- `socketIsClosed`
- `site.struct BulkUSBMuxSession`
- `IN  %d->%d %u:%lu(%ld) %s%s%s%s ack=%u win=%d\n`
- `F`
- `ScatterGatherSupport`
- `message`
- `Warning: %s duplicate ack received, ignoring\n`
- `vsendMuxRST`
- `%s::%s out of sync for too long. waiting for: %u, have: %u\n`
- `site.IOSocketEventSource`
- `\"%s called outside gate!\\n\" @%s:%d`
- `%s short tcp header received (%d bytes), ignoring\n`
- `%s I don't know why I'm here\n`
- `USB mux: %lu reads / %lu errors, %lu writes / %lu errors\n`
- `111`
- `Error: %s writeMbufToUSB failed, closing session\n`
- `Error: %s failed to set traffic class SO_TC_BK_SYS: %d\n`
- `handleMuxVersionInput`
- `%s expected %d bytes, received %d\n`
- `%s failed to allocate IO buffer\n`
- `Oct 13 2026`
- `%s mbuf_next(packet) != NULL, will be ignored\n`
- `%s: sending from rewrite list, length %d/%d\n`
- `IOSocketEventSource`
- `1211111212221212111111112222222211211111112111111222222222`
- `AppleUSBDeviceMux::%s - kMessageInterfaceWasSuspended\n`
- `%s: failure - %d`
- `%s writeMbufToUSB failed to send rstbuf\n`
- `site.AppleUSBDeviceMux`
- `asyncWriteComplete`
- `AppleUSBDeviceMux::%s - kMessageInterfaceWasDeActivated\n`
- `handleConnectResult`
- `Error: %s mbuf_gethdr failed, closing session\n`
- `A`
- `%02x`
- `Offset %6u : %s\n`
- `%s connection was closed`
- `%s failed to allocate USBWriteBuffer object %d\n`
- `void AppleUSBDeviceMux::freeBufferList(struct USBWriteBuffer *)`
- `%s::%s missing more packets. restarting timer. waiting for: %u, have: %u\n`
- `%s failed to allocat mbuf\n`
- `%s sock_receive returned errno %d\n`
- `%s new session to port %d failed: %d\n`
- `%s short tcp header received (%d/%d bytes), ignoring\n`
- `%s, message was too large (%d bytes, max = %d)\n`
- `IOReturn AppleUSBDeviceMux::writeToUSBPipe(struct USBWriteBuffer *)`
- `USBDeviceCommand`
- `AppleUSBDeviceMux build: %s %s\n`
- `%s th.th_flags = 0x%x, not TH_ACK(0x%x)\n`
- `IN  Injecting %lu bytes using %lu bytes directly\n`
- `asyncMbufWriteComplete`
- `Apple USB Multiplexor`
- `asyncReadComplete`
- `%s no memory descriptor`
- `sendMuxSegment`
- `%s writeMbufToUSB failed: 0x%08X`
- `%s no matching session`
- `handleMuxHostLogLevelInput`
- `%s Failed to send version, out of mbufs\n`
- `%s hdr_length updated to %d\n`
- `Long packet was truncated. Original length appeared to be %llu bytes\n`
- `%s failed to allocate write IO buffer %d\n`
- `AppleUSBDeviceMux::%s - kMessageInterfaceWasActivated\n`
- `Error: %s sock_setsockopt(SO_UPCALLCLOSEWAIT) failed: %d\n`
- `DumpDebug`
- `11122111`
- `\"%s buffer already free\" @%s:%d`
- `%s`
- `%s raw_length longer than expected (%lu bytes), truncating\n`
- `IOReturn AppleUSBDeviceMux::setPropertiesGated(OSObject *)`
- `%s setting debug level to %d\n`
- `IOReturn AppleUSBDeviceMux::allocateUSBWriteBuffers()`
- `site.struct MBufList`
- `%s matches existing session, closing old session and sending RST\n`
- `%s IOMalloc IOMallocType`
- `S`
- `R`
- `Total bytes dumped: %u\n`
- `%s::%s unexpected EINPROGRESS from sock_connectwait\n`
- `%s hdrlen != packet lenth`
- `sessionUpcall`
- `USB mux: %lu short packets, %lu dups\n`
- `newSession`
- `Error: %s IOMallocType failed\n`
- `OUT done.\n`
- `reportStats`
