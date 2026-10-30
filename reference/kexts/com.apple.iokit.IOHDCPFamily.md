# `com.apple.iokit.IOHDCPFamily`

- Name: IOHDCPFamily
- Version: `1.0.0`
- UUID: `42C5B82A-B36D-3405-A2A8-6A049F4ADB4A`
- Source version: `80.0.0.0.0`
- Depends on: [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0b2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0b2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (9) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOHDCP1TransmitterAuthSession` | 0x60 | IOHDCPAuthSession → IOEventSource |
| `IOHDCP2AuthSession` | 0xb8 | IOHDCPAuthSession → IOEventSource |
| `IOHDCP2DPTransmitterAuthSession` | 0x558 | IOHDCP2TransmitterAuthSession → IOHDCP2AuthSession → IOHDCPAuthSession → IOEventSource |
| `IOHDCP2LocalMessageTransport` | 0x30 | IOHDCPMessageTransport |
| `IOHDCP2ReceiverAuthSession` | 0x188 | IOHDCP2AuthSession → IOHDCPAuthSession → IOEventSource |
| `IOHDCP2TransmitterAuthSession` | 0x340 | IOHDCP2AuthSession → IOHDCPAuthSession → IOEventSource |
| `IOHDCPAuthSession` | 0x60 | IOEventSource |
| `IOHDCPInterface` | 0x98 | IOService → IORegistryEntry |
| `IOHDCPMessageTransport` | 0x20 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000629f off=0x009e99f0-0x009efc8f addr=0xfffffe00079ed9f0-0xfffffe00079f3c8f r--/r--   __TEXT            
	sz=0x00000038 off=0x009ea0c0-0x009ea0f8 addr=0xfffffe00079ee0c0-0xfffffe00079ee0f8               __TEXT.__const            
	sz=0x00004554 off=0x009ea0f8-0x009ee64c addr=0xfffffe00079ee0f8-0xfffffe00079f264c               __TEXT.__cstring          (CstringLiterals)
	sz=0x00001643 off=0x009ee64c-0x009efc8f addr=0xfffffe00079f264c-0xfffffe00079f3c8f               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000e72c off=0x03151fb0-0x031606dc addr=0xfffffe000a155fb0-0xfffffe000a1646dc r-x/r-x   __TEXT_EXEC       
	sz=0x0000e41c off=0x03151fb0-0x031603cc addr=0xfffffe000a155fb0-0xfffffe000a1643cc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000310 off=0x031603cc-0x031606dc addr=0xfffffe000a1643cc-0xfffffe000a1646dc          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000244 off=0x049f0e48-0x049f108c addr=0xfffffe000b9f4e48-0xfffffe000b9f508c rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049f0e48-0x049f0f10 addr=0xfffffe000b9f4e48-0xfffffe000b9f4f10               __DATA.__data             
	sz=0x00000178 off=0x00000000-0x00000178 addr=0xfffffe000b9f4f10-0xfffffe000b9f5088               __DATA.__common           (Zerofill)
	sz=0x00000004 off=0x00000000-0x00000004 addr=0xfffffe000b9f5088-0xfffffe000b9f508c               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00002220 off=0x0137d9e0-0x0137fc00 addr=0xfffffe00083819e0-0xfffffe0008383c00 rw-/rw-   __DATA_CONST      
	sz=0x00000050 off=0x0137d9e0-0x0137da30 addr=0xfffffe00083819e0-0xfffffe0008381a30         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000048 off=0x0137da30-0x0137da78 addr=0xfffffe0008381a30-0xfffffe0008381a78         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001c60 off=0x0137da78-0x0137f6d8 addr=0xfffffe0008381a78-0xfffffe00083836d8         __DATA_CONST.__const            
	sz=0x00000340 off=0x0137f6d8-0x0137fa18 addr=0xfffffe00083836d8-0xfffffe0008383a18         __DATA_CONST.__kalloc_type      
	sz=0x00000188 off=0x0137fa18-0x0137fba0 addr=0xfffffe0008383a18-0xfffffe0008383ba0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000060 off=0x0137fba0-0x0137fc00 addr=0xfffffe0008383ba0-0xfffffe0008383c00         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 110 at 0x04af2404
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     42C5B82A-B36D-3405-A2A8-6A049F4ADB4A
008: LC_SOURCE_VERSION           80.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004abff88 size=0x1f8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOHDCPFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOHDCPFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOHDCPFamily`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2014-2016 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOHDCPFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895404560`
- `_PrelinkExecutableRelativePath`: `IOHDCPFamily`
- `_PrelinkExecutableSize`: `93743`
- `_PrelinkExecutableSourceAddr`: `-2198895404560`
- `_PrelinkKmodInfo`: `-2198828265912`

## Strings (560) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `after writeEncryptedKs: E_dkey_ks[%zu] = { %*D }\n`
- `P0_No_Rx_Attached`
- `after consumeRiv: riv[%zu] = { %*D }\n`
- `before loadStoredKm: E_kh_km[%zu] = { %*D }\n`
- `hdcp-channel`
- `State::A1_Exchange_km_WaitForAKE_Send_H_prime == state()`
- `IOHDCP2ReceiverAuthSession`
- `/Library/Caches/com.apple.xbs/A313B9F7-0A29-4EBC-8321-D899E264CFEB/TemporaryDirectory.Omi04X/Sources/IOHDCPFamily/IOHDCP2ReceiverAuthSession.cpp`
- `State::B1_Compute_km_WaitForAKE_some_km == state()`
- `validateIsOpen`
- `ret = fillAKE_Init(&message.data.DP_AKE_Init) == 0 `
- `B2_Compute_L_prime_WaitForLC_Init`
- `wait terminated prematurely with 0x%08x\n`
- `setPowerState`
- `HDCPTXCapabilities`
- `after consumeStoredKm: m[%zu] = { %*D }\n`
- `_timerEventSource`
- `before readL: L_prime[%zu] = { %*D }\n`
- `Initial`
- `fillRepeaterAuth_Stream_Manage`
- `State::A9_Content_Stream_Management == state()`
- `ret = recvMessage(&message) == 0 `
- `ret = 0x%08x\n`
- `IOHDCP2LocalMessageTransport`
- `F8_Send_Receiver_ID_List_acknowledgement`
- `messageCountWaitForZero`
- `channel`
- `ret = takeLC_Send_L_prime(&inMessage->data.LC_Send_L_prime) == 0 `
- `receiver    %p unknown-msg_id %d\n`
- `before readCert: cert_rx[%zu] = { %*D }\n`
- `ret = fillRepeaterAuth_Send_Ack(&message.data.RepeaterAuth_Send_Ack) == 0 `
- `IOHDCPAuthSession`
- `AKE_Send_rrx`
- `Upstream_AbortAuthentication`
- `site.IOHDCPInterface`
- `after consumeRtx: rtx[%zu] = { %*D }\n`
- `C7_Content_stream_management`
- `_wl`
- `121112111112`
- `A1_Exchange_km_WaitForAKE_Send_rrx`
- `ret = sendKm() == 0 `
- `ret = fillAKE_Send_Pairing_Info(&message.data.AKE_Send_Pairing_Info) == 0 `
- `after readL: L_prime[%zu] = { %*D }\n`
- `F1_Exchange_km`
- `failed to create parent matching dictionary\n`
- `receiver    %p handleMessage %d %s state %d %s\n`
- `after consumeNewKm: E_kpub_km[%zu] = { %*D }\n`
- `before consumeStoredKm: E_kh_km[%zu] = { %*D }\n`
- `Unknown`
- `transmitter unexpected timeout state()=%s(%d)\n`
- `yes`
- `invalid hdcp_bool 0x%02x\n`
- `F6_Wait_for_Receiver_ID_List`
- `_rx_version >= 2`
- `RTT_Challenge`
- `B1_Compute_km`
- `before verifyVPrime: V_prime[%zu] = { %*D }\n`
- `before generateRtx: rtx[%zu] = { %*D }\n`
- `State::A5_Authenticated == state()`
- `ret = fillLC_Init(&message.data.LC_Init) == 0 `
- `before generateRiv: riv[%zu] = { %*D }\n`
- `ret = getInterface()->generateEKhKm(&AKE_Send_Pairing_Info->E_kh_km) == 0 `
- `IOEventSource::init(owner, (IOEventSource::Action)action)`
- `ksvList=\n[%zu] = { %*D }\n`
- `after generateEncryptedKm: E_kpub_km[%zu] = { %*D }\n`
- `ret = fillAKE_Send_H_prime(&message.data.AKE_Send_H_prime) == 0 `
- `F4_Test_for_Repeater`
- `ret = getInterface()->readL(&LC_Send_L_prime->L_prime) == 0 `
- `A1_Exchange_km`
- `receiver unknown state %d\n`
- `free`
- `Reserved22`
- `ret = takeAKE_No_Stored_km(&inMessage->data.AKE_No_Stored_km) == 0 `
- `takeAKE_Stored_km`
- `IOHDCPMessageTransport::init(refCon)`
- `Upstream_Reset`
- `_commandGate`
- `m0=\n[%zu] = { %*D }\n`
- `channels`
- `fillAKE_Send_Cert`
- `i8@?0`
- `ret = getInterface()->consumeRtx(AKE_Init->rtx) == 0 `
- `sendMessage`
- `ret == 0`
- `IOHDCP2AuthSession.cpp`
- `before consumeRtx: rtx[%zu] = { %*D }\n`
- `transport lacks valid auth session\n`
- `M != M', retrying RepeaterAuth_Stream_Manage\n`
- `ret = setTimeoutMS(100) == 0 `
- `/Library/Caches/com.apple.xbs/A313B9F7-0A29-4EBC-8321-D899E264CFEB/TemporaryDirectory.Omi04X/Sources/IOHDCPFamily/IOHDCP2DPTransmitterAuthSession.cpp`
- `hdcp_use_storedkm`
- `transport`
- `IOHDCP1TransmitterAuthSession`
- `ret = sendMessage(&message) == 0 `
- `State::A3_Exchange_ks_WaitFor200ms == state()`
- `ret = getInterface()->consumeRiv(SKE_Send_Eks->riv) == 0 `
- `workLoop->removeEventSource(_timerEventSource) == 0 `
- `IOHDCPInterface::open(kHDCPInterfacePowerStateOff) called while in kHDCPInterfacePowerStateOff\n`
- `AKE_Stored_km`
- `C3_Compute_L_ks`
- `ret = getInterface()->resetKeys() == 0 `
- `ret = fillAKE_Send_Cert(&message.data.AKE_Send_Cert) == 0 `
- `F2_Locality_Check`
- `State::H1_Transmit_Low_value_Content == state()`
- `ret = takeLC_Init(&inMessage->data.LC_Init) == 0 `
- `Reserved24`
- `ret = getInterface()->computeH(_H_input_data) == 0 `
- `AKE_Send_Cert`
- `Unable to get workloop\n`
- `invalid _receiverID\n`
- `ret = getInterface()->readH(&AKE_Send_H_prime->H_prime) == 0 `
- `ret = takeAKE_Send_Cert(&inMessage->data.AKE_Send_Cert) == 0 `
- `ret = setTimeoutMS(200) == 0 `
- `\"failed to add _timerEventSource to workLoop\\n\" @%s:%d`
- `ret = getInterface()->writeEncryptedKs(SKE_Send_Eks->E_dkey_ks) == 0 `
- `(_seq_num_V & 0xFF000000 ) == 0`
- `validateKSVList`
- `transmitter %p handleMessage %d %s state %d %s\n`
- `12111211111211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `ret = getInterface()->verifyLPrime(LC_Send_L_prime->L_prime) == 0 `
- `A3_Exchange_ks`
- `C1_Compute_km`
- `ret = getInterface()->generateRtx(&DP_AKE_Init->rtx) == 0 `
- `_hdcp_capable`
- `after verifyVPrime: V_prime[%zu] = { %*D }\n`
- `11`
- `SKE_Send_Eks`
- `Reserved21`
- `after consumeStoredKm: E_kh_km[%zu] = { %*D }\n`
- `session`
- `ret = setTimeoutMS(110) == 0 `
- `site.IOHDCP2TransmitterAuthSession`
- `after generateEncryptedKs: E_dkey_ks[%zu] = { %*D }\n`
- `ret = fillAKE_Send_rrx(&message.data.AKE_Send_rrx) == 0 `
- `enable`
- `IOHDCP2DPTransmitterAuthSession`
- `hdcp-parents`
- `fillAKE_Send_Pairing_Info`
- `State::A1_Exchange_km_WaitForAKE_Receiver_Info == state()`
- `ret = takeAKE_Receiver_Info(&inMessage->data.AKE_Receiver_Info) == 0 `
- `B3_Compute_ks_WaitForSKE_Send_Eks`
- `cancelTimeout`
- `VPrime=[%zu] = { %*D }\n`
- `ret = getInterface()->consumeNewKm(AKE_No_Stored_km->E_kpub_km) == 0 `
- `init`
- `F3_Exchange_ks`
- `ret = takeAKE_Send_rrx(&inMessage->data.AKE_Send_rrx) == 0 `
- `State::B2_Compute_L_prime_WaitForRTT_Challenge == state()`
- `/Library/Caches/com.apple.xbs/A313B9F7-0A29-4EBC-8321-D899E264CFEB/TemporaryDirectory.Omi04X/Sources/IOHDCPFamily/IOHDCP2LocalMessageTransport.cpp`
- `AKE_Transmitter_Info`
- `P1_Transmit_Low_value_Content`
- `validateReceiverID(_receiverID)`
- `1211121111121112222222222222222222222222222222222`
- `A0_Determine_Rx_HDCP_Capable`
- `_handleActionThreadCall`
- `fillLC_Init`
- `ret = takeSKE_Send_Eks(&inMessage->data.SKE_Send_Eks) == 0 `
- `fillAKE_Send_H_prime`
- `ret = authStreamReadyTimeout() == 0 `
- `interface`
- `ret = getInterface()->generateRiv(&SKE_Send_Eks->riv) == 0 `
- `Reserved25`
- `IOHDCPAuthSession::free: destroying...\n`
- `F0_Determine_Rx_HDCP_Capable`
- `IOHDCP2AuthSession::setTimeoutMS %p started %llu %ums\n`
- `ret = getInterface()->readV(&V) == 0 `
- `powerstate = %lx, isOpen()=%u\n`
- `ret = takeAKE_Send_Pairing_Info(&inMessage->data.AKE_Send_Pairing_Info) == 0 `
- `ret = getInterface()->writeCert(AKE_Send_Cert->cert_rx) == 0 `
- `Reserved31`
- `protocolList`
- `IOHDCP2TransmitterAuthSession`
- `State::A1_Exchange_km_WaitForAKE_Send_Pairing_Info == state()`
- `Reserved29`
- `%06llu.%06llu IOHDCP[%llu] %s %s`
- `ret = IOHDCP2TransmitterAuthSession::hPrimeAvailable() == 0 `
- `hdcpInterface`
- `Upstream_CP_desired`
- `before writeEncryptedKs: E_dkey_ks[%zu] = { %*D }\n`
- `C5_Assemble_Receiver_ID_List`
- `State::A1_Exchange_km_WaitForAKE_Send_Cert == state()`
- `fillAKE_No_Stored_km`
- `after generateRiv: riv[%zu] = { %*D }\n`
- `after readCert: cert_rx[%zu] = { %*D }\n`
- `after generateEKhKm: E_kh_km[%zu] = { %*D }\n`
- `after consumeRn: rn[%zu] = { %*D }\n`
- `IOHDCPAuthSession::validateIsOpen: <%s>\n`
- `hdcpIsTrue`
- `open_block_invoke`
- `after loadStoredKm: E_kh_km[%zu] = { %*D }\n`
- `C4_Wait_for_Downstream`
- `after readV: V[%zu] = { %*D }\n`
- `failed to remove _commandGate from workLoop\n`
- `ret = fillAKE_No_Stored_km(&message.data.AKE_No_Stored_km) == 0 `
- `before consumeRrx: rrx[%zu] = { %*D }\n`
- `ret = getInterface()->consumeRn(LC_Init->rn) == 0 `
- `IOHDCPAuthSession(%p)::init owner %p action %p transport %p interface %p\n`
- `takeAKE_Init`
- `AKE_Init`
- `fillRepeaterAuth_Send_Ack`
- `IOHDCPMessageTransport`
- `_messageQLock = IOSimpleLockAlloc()`
- `Receiver_AuthStatus`
- `setState`
- `ret = getInterface()->computeL() == 0 `
- `B0_Unauthenticated`
- `after verifyHPrime: H_prime[%zu] = { %*D }\n`
- `ret = takeAKE_Send_Cert(&inMessage->data.DP_AKE_Send_Cert) == 0 `
- `hPrimeAvailable`
- `HDCPChannel`
- `before generateRn: rn[%zu] = { %*D }\n`
- `after generateRn: rn[%zu] = { %*D }\n`
- `State::A2_Locality_Check_WaitForRTT_Ready == state()`
- `setWorkLoop`
- `ret = getInterface()->consumeRrx(DP_AKE_Send_Cert->rrx) == 0 `
- `, `
- `C1_Unauthenticated`
- `receiverIDListAvailable`
- `site.IOHDCP2LocalMessageTransport`
- `site.IOHDCPMessageTransport`
- `State::H0_No_Rx_Attached == state()`
- `before consumeStoredKm: m[%zu] = { %*D }\n`
- `ret = getInterface()->consumeStoredKm(storedKm) == 0 `
- `A3_Exchange_ks_WaitFor200ms`
- `A4_Test_for_Repeater`
- `F5_Authenticated`
- `ret = fillAKE_Transmitter_Info(&message.data.AKE_Transmitter_Info) == 0 `
- `ret = getInterface()->consumeRrx(AKE_Send_rrx->rrx) == 0 `
- `before generateEKhKm: E_kh_km[%zu] = { %*D }\n`
- `seq_num_V == _seq_num_V`
- `ret = fillDP_Send_Type(&message.data.DP_Send_Type) == 0 `
- `dict`
- `ret = setTimeoutMS(1000) == 0 `
- `Internal_EnableEncryption`
- `Ignoring redundant CP_IRQ`
- `setTimeoutMS`
- `newWorkLoop->addEventSource(_commandGate) == 0 `
- `1211111212221212112`
- `Protocols`
- `after generateRtx: rtx[%zu] = { %*D }\n`
- `ret = fillRepeaterAuth_Stream_Manage(&message.data.DP_RepeaterAuth_Stream_Manage) == 0 `
- `no`
- `RepeaterAuth_Send_ReceiverID_List`
- `1211`
- `Upstream_Receiver_disconnected`
- `B1_Compute_km_WaitForAKE_Transmitter_Info`
- `before generateEncryptedKs: E_dkey_ks[%zu] = { %*D }\n`
- `site.MessageQueueEntry`
- `A2_Locality_Check`
- `C2_Compute_L_prime`
- `handleMessage`
- `already reached or cancelled\n`
- `AKE_Send_H_prime`
- `hdcp_log_level`
- `A9_Content_Stream_Management`
- `before consumeRn: rn[%zu] = { %*D }\n`
- `after consumeRrx: rrx[%zu] = { %*D }\n`
- `transmitter %p state %d %s\n`
- `ret = getInterface()->generateRn(&LC_Init->rn) == 0 `
- `H1_Transmit_Low_value_Content`
- `fillSKE_Send_Eks`
- `A2_Locality_Check_WaitForRTT_Ready`
- `A5_Authenticated`
- `Transmitter`
- `parents`
- `AKE_Receiver_Info`
- `Upstream_Receiver_connected`
- `ret = getInterface()->sendKsRivDP(_stream0ContentType) == 0 `
- `timeout`
- `site.MessageQueue`
- `IOHDCP2AuthSession::timeout %p reached %llu already reached or cancelled\n`
- `(_seq_num_M & 0xFF000000 ) == 0`
- `_rx_version %d _hdcp_capable %d _repeater %d rx_caps 0x%02x%02x%02x receiverID:[%zu] = { %*D }\n`
- `RepeaterAuth_Send_ReceiverID_List<MAX_DEVS_EXCEEDED=%d MAX_CASCADE_EXCEEDED=%d DEVICE_COUNT=%d DEPTH=%d HDCP2_LEGACY_DEVICE_DOWNSTREAM=%d HDCP1_DEVICE_DOWNSTREAM=%d> rx_info[%zu] = { %*D }\n`
- `parent`
- `F7_Verify_Receiver_ID_List`
- `Unexpected state %d %s for timeout, ignored\n`
- `ret = setTimeoutMS(3000) == 0 `
- `IOHDCPInterface`
- `ret = takeAKE_Send_H_prime(&inMessage->data.AKE_Send_H_prime) == 0 `
- `ret = IOHDCP2TransmitterAuthSession::pairingInfoAvailable() == 0 `
- `ok`
- `Reserved28`
- `ret = getInterface()->computeV(bytes, checksumLength) == 0 `
- `takeAKE_Send_rrx`
- `ret = fillLC_Send_L_prime(&message.data.LC_Send_L_prime) == 0 `
- `Reserved27`
- `takeRepeaterAuth_Stream_Ready`
- `hdcp-channels`
- `handleStart`
- `_messageQ = ({ static __attribute__((used, section(\"__DATA_CONST\" \", __kalloc_type, \" \"regular, live_support\"))) struct kalloc_type_view kalloc_type_view_81[1] = { { .kt_zv.zv_name = \"site.\" \"MessageQueue\", .kt_flags = static_cast<kalloc_type_flags_t>((KT_SHARED_ACCT | KT_CHANGED | KT_CHAN`
- `_timerEventSource %p\n`
- `ret = validateIsOpen() == 0 `
- `ret = fillSKE_Send_Eks(&message.data.SKE_Send_Eks) == 0 `
- `A7_Verify_Receiver_ID_List`
- `workLoop->removeEventSource(_commandGate) == 0 `
- `failed to match interface\n`
- `ret = getInterface()->verifyHPrime(AKE_Send_H_prime->H_prime) == 0 `
- `ret = getInterface()->computeM(RepeaterAuth_Stream_Manage->seq_num_M, RepeaterAuth_Stream_Manage->StreamID_Type, _streamCount * sizeof(RepeaterAuth_Stream_Manage->StreamID_Type[0])) == 0 `
- `Receiver`
- `takeAKE_Send_Cert`
- `ret = akeSendCertTimeout() == 0 `
- `after verifyLPrime: L_prime[%zu] = { %*D }\n`
- `IOHDCP2AuthSession::disable\n`
- `ret = fillRTT_Ready(&message.data.RTT_Ready) == 0 `
- `IOHDCP2AuthSession::enable\n`
- `ret = takeReceiver_AuthStatus(&inMessage->data.Receiver_AuthStatus) == 0 `
- `ret = getInterface()->generateRtx(&AKE_Init->rtx) == 0 `
- `ret = fillAKE_Receiver_Info(&message.data.AKE_Receiver_Info) == 0 `
- `before computeH: H_prime[%zu] = { %*D }\n`
- `B3_Compute_ks`
- `before verifyLPrime: L_prime[%zu] = { %*D }\n`
- `H0_No_Rx_Attached`
- `fillAKE_Init`
- `mqe`
- `Null`
- `newWorkLoop->addEventSource(_timerEventSource) == 0 `
- `Topology violation detected\n`
- `%s state()=%s(%d)\n`
- `Reserved23`
- `DP_Send_Type:`
- `after workLoop %p removeEventSource\n`
- `pairingInfoAvailable`
- `HDCPRXCapabilities`
- `ret = takeAKE_Transmitter_Info(&inMessage->data.AKE_Transmitter_Info) == 0 `
- `IOHDCP2ReceiverAuthSession::timeout %p started %llu state %d\n`
- `site.IOHDCP2AuthSession`
- `\"failed to add _commandGate to workLoop\\n\" @%s:%d`
- `before loadStoredKm: m[%zu] = { %*D }\n`
- `takeAKE_Send_Pairing_Info`
- `IOHDCP2TransmitterAuthSession::init(owner, action, transport, interface)`
- `before readV: V[%zu] = { %*D }\n`
- `ret = sendLPrimeTimeout() == 0 `
- `after generateRrx: rrx[%zu] = { %*D }\n`
- `(State::A6_Wait_for_Receiver_ID_List == state()) || (State::A5_Authenticated == state())`
- `after computeH: H_prime[%zu] = { %*D }\n`
- `after generateRtx: tx_caps[%zu] = { %*D }\n`
- `handleTimeout`
- `fillAKE_Stored_km`
- `before sendKsRiv\n`
- `B2_Compute_L_prime`
- `C8_Authenticated`
- `initial state %d %s\n`
- `ret = IOHDCP2TransmitterAuthSession::receiverIDListAvailable() == 0 `
- `V     =[%zu] = { %*D }\n`
- `ret = fillAKE_Init(&message.data.AKE_Init) == 0 `
- `ret = getInterface()->sendKsRiv() == 0 `
- `transmitter unknown msg_id %d\n`
- `site.IOHDCP2DPTransmitterAuthSession`
- `State::B2_Compute_L_prime_WaitForLC_Init == state()`
- `State::B3_Compute_ks_WaitForSKE_Send_Eks == state()`
- `ret = getInterface()->verifyMPrime(RepeaterAuth_Stream_Ready->M_prime) == 0 `
- `ret = getInterface()->generateEncryptedKm(&AKE_No_Stored_km->E_kpub_km) == 0 `
- `DP_CP_IRQ_Timeout`
- `A1_Exchange_km_WaitForAKE_Receiver_Info`
- `C6_Verify_Receiver_ID_list_Acknowledgement`
- `thread_call_allocate_with_options() failed\n`
- `ret = getInterface()->enableHDCP(false) == 0 `
- `No %s entry in the provider properties\n`
- `takeAKE_Send_H_prime`
- `before consumeNewKm: E_kpub_km[%zu] = { %*D }\n`
- `after sendKsRiv\n`
- `takeMessage`
- `ret = getInterface()->verifyVPrime(RepeaterAuth_Send_ReceiverID_List->V_prime) == 0 `
- `ret = takeRepeaterAuth_Send_ReceiverID_List(&inMessage->data.DP_RepeaterAuth_Send_ReceiverID_List) == 0 `
- `121111`
- `A2_Locality_Check_WaitForLC_Send_L_prime`
- `B1_Compute_km_WaitForAKE_some_km`
- `disable`
- `commandSleep() failed, ret=0x%x; workLoop %p\n`
- `site.IOHDCP2ReceiverAuthSession`
- `RepeaterAuth_Stream_Ready`
- `12111211111211122222222`
- `RepeaterAuth_Send_Ack`
- `/Library/Caches/com.apple.xbs/A313B9F7-0A29-4EBC-8321-D899E264CFEB/TemporaryDirectory.Omi04X/Sources/IOHDCPFamily/IOHDCP2AuthSession.cpp`
- `hdcp-parent`
- `before generateRrx: rrx[%zu] = { %*D }\n`
- `Reserved30`
- `B1_Compute_km_WaitForAKE_Init`
- `B4_Authenticated`
- `/Library/Caches/com.apple.xbs/A313B9F7-0A29-4EBC-8321-D899E264CFEB/TemporaryDirectory.Omi04X/Sources/IOHDCPFamily/IOHDCPInterface.cpp`
- `ret = takeRTT_Ready(&inMessage->data.RTT_Ready) == 0 `
- `IOHDCPAuthSession::init(owner, action, transport, interface)`
- `ret = fillRTT_Challenge(&message.data.RTT_Challenge) == 0 `
- `takeLC_Send_L_prime`
- `ret = getInterface()->generateEncryptedKs(&SKE_Send_Eks->E_dkey_ks) == 0 `
- `transport lacks peer\n`
- `before generateEncryptedKm: E_kpub_km[%zu] = { %*D }\n`
- `LC_Send_L_prime`
- `F9_Content_Stream_Management`
- `AssertMacros: %s, %s file: %s, line: %d, value: %lld\n`
- `received unexpected message %d %s for current state %d %s\n`
- `ret = getInterface()->readCert(&AKE_Send_Cert->cert_rx) == 0 `
- `site.IOHDCPAuthSession`
- `A1_Exchange_km_WaitForAKE_Send_Pairing_Info`
- `failed to remove _timerEventSource from workLoop\n`
- `takeRepeaterAuth_Send_ReceiverID_List`
- `ret = setTimeoutMS(16) == 0 `
- `clearStoredKm ret=0x%08X\n`
- `ret = getInterface()->generateRrx(&AKE_Send_rrx->rrx) == 0 `
- `ret = getInterface()->enableHDCP(true) == 0 `
- `ret = takeAKE_Init(&inMessage->data.AKE_Init) == 0 `
- `before consumeRiv: riv[%zu] = { %*D }\n`
- `LC_Init`
- `IOHDCP2AuthSession::cancelTimeout %p reached %llu already reached or cancelled\n`
- `IOHDCP2AuthSession::init(owner, action, transport, interface)`
- `ret == 0 `
- `State::A2_Locality_Check_WaitForLC_Send_L_prime == state()`
- `ret = enableEncryption() == 0 `
- `A1_Exchange_km_WaitForAKE_Send_H_prime`
- `after saveStoredKm: E_kh_km[%zu] = { %*D }\n`
- `takeSKE_Send_Eks`
- `AKE_No_Stored_km`
- `IOHDCP2AuthSession`
- `takeAKE_No_Stored_km`
- `RTT_Ready`
- `Reserved26`
- `timeout %llu cancelled\n`
- `State::B1_Compute_km_WaitForAKE_Transmitter_Info == state()`
- `/Library/Caches/com.apple.xbs/A313B9F7-0A29-4EBC-8321-D899E264CFEB/TemporaryDirectory.Omi04X/Sources/IOHDCPFamily/IOHDCPAuthSession.cpp`
- `RepeaterAuth_Stream_Manage`
- `B2_Compute_L_prime_WaitForRTT_Challenge`
- `_stream0ContentType %d\n`
- `channelData`
- `before verifyHPrime: H_prime[%zu] = { %*D }\n`
- `ret = takeAKE_Stored_km(&inMessage->data.AKE_Stored_km) == 0 `
- `takeLC_Init`
- `A1_Exchange_km_WaitForAKE_Send_Cert`
- `_repeater %d _receiverID: [%zu] = { %*D }\n`
- `/Library/Caches/com.apple.xbs/A313B9F7-0A29-4EBC-8321-D899E264CFEB/TemporaryDirectory.Omi04X/Sources/IOHDCPFamily/IOHDCP2TransmitterAuthSession.cpp`
- `%s[%d] entry is absent in the provider properties\n`
- `after loadStoredKm: m[%zu] = { %*D }\n`
- `222222222222222222222222222222222222222222222222222222222222222222221`
- `sendKsRivDP _stream0ContentType 0x%02x\n`
- `fillLC_Send_L_prime`
- `AKE_Send_Pairing_Info`
- `before saveStoredKm: E_kh_km[%zu] = { %*D }\n`
- `fillAKE_Send_rrx`
- `ret = getInterface()->writeCert(DP_AKE_Send_Cert->cert_rx) == 0 `
- `parentMatching`
- `State::A1_Exchange_km_WaitForAKE_Send_rrx == state()`
- `abortAuthentication while not connected()\n`
- `ret = getInterface()->saveStoredKm(AKE_Send_Pairing_Info->E_kh_km) == 0 `
- `A6_Wait_for_Receiver_ID_List`
- `121112111112111222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `Illegal DP msg_id %d\n`
- `A8_Send_Receiver_ID_List_acknowledgement`
- `authsession %p already in state %d %s\n`
- `currentState != state()`
- `site.IOHDCP1TransmitterAuthSession`

**[__TEXT.__os_log]**

- `No %s entry in the provider properties\n`
- `transmitter unexpected timeout state()=%s(%d)\n`
- `invalid _receiverID\n`
- `before verifyHPrime: H_prime[%zu] = { %*D }\n`
- `after generateRn: rn[%zu] = { %*D }\n`
- `thread_call_allocate_with_options() failed\n`
- `IOHDCP2AuthSession::cancelTimeout %p reached %llu already reached or cancelled\n`
- `IOHDCP2AuthSession::timeout %p reached %llu already reached or cancelled\n`
- `before loadStoredKm: m[%zu] = { %*D }\n`
- `after consumeRtx: rtx[%zu] = { %*D }\n`
- `before sendKsRiv\n`
- `wait terminated prematurely with 0x%08x\n`
- `after verifyVPrime: V_prime[%zu] = { %*D }\n`
- `Ignoring redundant CP_IRQ`
- `_repeater %d _receiverID: [%zu] = { %*D }\n`
- `before generateRn: rn[%zu] = { %*D }\n`
- `after computeH: H_prime[%zu] = { %*D }\n`
- `IOHDCPAuthSession(%p)::init owner %p action %p transport %p interface %p\n`
- `commandSleep() failed, ret=0x%x; workLoop %p\n`
- `failed to match interface\n`
- `IOHDCPInterface::open(kHDCPInterfacePowerStateOff) called while in kHDCPInterfacePowerStateOff\n`
- `before readCert: cert_rx[%zu] = { %*D }\n`
- `Topology violation detected\n`
- `m0=\n[%zu] = { %*D }\n`
- `before generateRtx: rtx[%zu] = { %*D }\n`
- `before loadStoredKm: E_kh_km[%zu] = { %*D }\n`
- `before consumeStoredKm: m[%zu] = { %*D }\n`
- `after consumeRn: rn[%zu] = { %*D }\n`
- `failed to remove _timerEventSource from workLoop\n`
- `authsession %p already in state %d %s\n`
- `V     =[%zu] = { %*D }\n`
- `%s[%d] entry is absent in the provider properties\n`
- `Unable to get workloop\n`
- `%s state()=%s(%d)\n`
- `after generateRiv: riv[%zu] = { %*D }\n`
- `before computeH: H_prime[%zu] = { %*D }\n`
- `before consumeRn: rn[%zu] = { %*D }\n`
- `Unexpected state %d %s for timeout, ignored\n`
- `before consumeRrx: rrx[%zu] = { %*D }\n`
- `receiver    %p handleMessage %d %s state %d %s\n`
- `IOHDCP2ReceiverAuthSession::timeout %p started %llu state %d\n`
- `before generateEKhKm: E_kh_km[%zu] = { %*D }\n`
- `after writeEncryptedKs: E_dkey_ks[%zu] = { %*D }\n`
- `after workLoop %p removeEventSource\n`
- `transmitter %p handleMessage %d %s state %d %s\n`
- `Illegal DP msg_id %d\n`
- `abortAuthentication while not connected()\n`
- `after loadStoredKm: m[%zu] = { %*D }\n`
- `after readL: L_prime[%zu] = { %*D }\n`
- `IOHDCPAuthSession::free: destroying...\n`
- `invalid hdcp_bool 0x%02x\n`
- `_timerEventSource %p\n`
- `timeout %llu cancelled\n`
- `before readV: V[%zu] = { %*D }\n`
- `received unexpected message %d %s for current state %d %s\n`
- `after consumeStoredKm: E_kh_km[%zu] = { %*D }\n`
- `before writeEncryptedKs: E_dkey_ks[%zu] = { %*D }\n`
- `IOHDCPAuthSession::validateIsOpen: <%s>\n`
- `after readV: V[%zu] = { %*D }\n`
- `M != M', retrying RepeaterAuth_Stream_Manage\n`
- `ret = 0x%08x\n`
- `after verifyLPrime: L_prime[%zu] = { %*D }\n`
- `before consumeStoredKm: E_kh_km[%zu] = { %*D }\n`
- `after consumeStoredKm: m[%zu] = { %*D }\n`
- `transport lacks peer\n`
- `_stream0ContentType %d\n`
- `sendKsRivDP _stream0ContentType 0x%02x\n`
- `failed to create parent matching dictionary\n`
- `transmitter unknown msg_id %d\n`
- `before generateEncryptedKm: E_kpub_km[%zu] = { %*D }\n`
- `after loadStoredKm: E_kh_km[%zu] = { %*D }\n`
- `after saveStoredKm: E_kh_km[%zu] = { %*D }\n`
- `already reached or cancelled\n`
- `after readCert: cert_rx[%zu] = { %*D }\n`
- `after consumeNewKm: E_kpub_km[%zu] = { %*D }\n`
- `after generateRtx: rtx[%zu] = { %*D }\n`
- `receiver unknown state %d\n`
- `before readL: L_prime[%zu] = { %*D }\n`
- `after consumeRiv: riv[%zu] = { %*D }\n`
- `transport lacks valid auth session\n`
- `IOHDCP2AuthSession::disable\n`
- `RepeaterAuth_Send_ReceiverID_List<MAX_DEVS_EXCEEDED=%d MAX_CASCADE_EXCEEDED=%d DEVICE_COUNT=%d DEPTH=%d HDCP2_LEGACY_DEVICE_DOWNSTREAM=%d HDCP1_DEVICE_DOWNSTREAM=%d> rx_info[%zu] = { %*D }\n`
- `before verifyVPrime: V_prime[%zu] = { %*D }\n`
- `clearStoredKm ret=0x%08X\n`
- `before consumeNewKm: E_kpub_km[%zu] = { %*D }\n`
- `_rx_version %d _hdcp_capable %d _repeater %d rx_caps 0x%02x%02x%02x receiverID:[%zu] = { %*D }\n`
- `before generateRrx: rrx[%zu] = { %*D }\n`
- `after generateRrx: rrx[%zu] = { %*D }\n`
- `after consumeRrx: rrx[%zu] = { %*D }\n`
- `before verifyLPrime: L_prime[%zu] = { %*D }\n`
- `receiver    %p unknown-msg_id %d\n`
- `before consumeRtx: rtx[%zu] = { %*D }\n`
- `after generateEKhKm: E_kh_km[%zu] = { %*D }\n`
- `before consumeRiv: riv[%zu] = { %*D }\n`
- `powerstate = %lx, isOpen()=%u\n`
- `transmitter %p state %d %s\n`
- `after verifyHPrime: H_prime[%zu] = { %*D }\n`
- `before generateEncryptedKs: E_dkey_ks[%zu] = { %*D }\n`
- `after generateEncryptedKs: E_dkey_ks[%zu] = { %*D }\n`
- `before generateRiv: riv[%zu] = { %*D }\n`
- `after sendKsRiv\n`
- `IOHDCP2AuthSession::setTimeoutMS %p started %llu %ums\n`
- `after generateEncryptedKm: E_kpub_km[%zu] = { %*D }\n`
- `before saveStoredKm: E_kh_km[%zu] = { %*D }\n`
- `initial state %d %s\n`
- `IOHDCP2AuthSession::enable\n`
- `failed to remove _commandGate from workLoop\n`
- `after generateRtx: tx_caps[%zu] = { %*D }\n`
- `ksvList=\n[%zu] = { %*D }\n`
- `VPrime=[%zu] = { %*D }\n`
