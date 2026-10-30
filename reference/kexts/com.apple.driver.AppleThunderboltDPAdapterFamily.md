# `com.apple.driver.AppleThunderboltDPAdapterFamily`

- Name: AppleThunderboltDPAdapterFamily
- Version: `8.5.1`
- UUID: `61FB5074-5310-3B44-98B6-779B42111622`
- Source version: `876.40.3.0.0`
- Depends on: [`com.apple.iokit.IOThunderboltFamily`](com.apple.iokit.IOThunderboltFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleThunderboltDPAdapterFamily` | 0x198 | IOThunderboltTunnelDriver → IOService → IORegistryEntry |
| `AppleThunderboltDPAdapterFamilyBase` | 0x190 | IOThunderboltTunnelDriver → IOService → IORegistryEntry |
| `AppleThunderboltDPConnectionManager` | 0xe8 | IOService → IORegistryEntry |
| `AppleThunderboltDPPathManager` | 0xc0 |  |
| `AppleThunderboltDPPathManagerOS` | 0xc0 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000ddf0 off=0x007ee190-0x007fbf80 addr=0xfffffe00077f2190-0xfffffe00077fff80 r--/r--   __TEXT            
	sz=0x0000d79f off=0x007ee7b8-0x007fbf57 addr=0xfffffe00077f27b8-0xfffffe00077fff57               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000020 off=0x007fbf60-0x007fbf80 addr=0xfffffe00077fff60-0xfffffe00077fff80               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0003709c off=0x028d7f80-0x0290f01c addr=0xfffffe00098dbf80-0xfffffe000991301c r-x/r-x   __TEXT_EXEC       
	sz=0x00036c4c off=0x028d7f80-0x0290ebcc addr=0xfffffe00098dbf80-0xfffffe0009912bcc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000450 off=0x0290ebcc-0x0290f01c addr=0xfffffe0009912bcc-0xfffffe000991301c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001a0 off=0x049cd440-0x049cd5e0 addr=0xfffffe000b9d1440-0xfffffe000b9d15e0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049cd440-0x049cd508 addr=0xfffffe000b9d1440-0xfffffe000b9d1508               __DATA.__data             
	sz=0x000000d8 off=0x00000000-0x000000d8 addr=0xfffffe000b9d1508-0xfffffe000b9d15e0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00002108 off=0x012737a8-0x012758b0 addr=0xfffffe00082777a8-0xfffffe00082798b0 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x012737a8-0x012737d0 addr=0xfffffe00082777a8-0xfffffe00082777d0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x012737d0-0x012737f8 addr=0xfffffe00082777d0-0xfffffe00082777f8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001ca0 off=0x012737f8-0x01275498 addr=0xfffffe00082777f8-0xfffffe0008279498         __DATA_CONST.__const            
	sz=0x00000140 off=0x01275498-0x012755d8 addr=0xfffffe0008279498-0xfffffe00082795d8         __DATA_CONST.__kalloc_type      
	sz=0x00000228 off=0x012755d8-0x01275800 addr=0xfffffe00082795d8-0xfffffe0008279800         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000b0 off=0x01275800-0x012758b0 addr=0xfffffe0008279800-0xfffffe00082798b0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 160 at 0x04ae92a0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     61FB5074-5310-3B44-98B6-779B42111622
008: LC_SOURCE_VERSION           876.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab54c0 size=0x1f8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleThunderboltDPAdapterFamily`
- `CFBundleIdentifier`: `com.apple.driver.AppleThunderboltDPAdapterFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleThunderboltDPAdapterFamily`
- `CFBundleNumericVersion`: `139558912`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `8.5.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `8.5.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `AppleThunderboltDPAdapters version 8.5.1, Copyright © 2009-2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Local-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleThunderboltDPAdapters.kext/PlugIns/AppleThunderboltDPAdapterFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897483376`
- `_PrelinkExecutableRelativePath`: `AppleThunderboltDPAdapterFamily`
- `_PrelinkExecutableSize`: `291124`
- `_PrelinkExecutableSourceAddr`: `-2198897483376`
- `_PrelinkKmodInfo`: `-2198828411840`

## Strings (587) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - added %d commands to fAuxTxTransmitCommandPool\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to allocate fAuxTxReceiveQueue\n`
- `%lldus AppleThunderboltDPPathManager<%p>::startAllQueues - ERROR: failed to submit rx_command to fAuxTxReceiveQueue\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::destroySnoopRings - %d commands released from fAuxRxReceiveCommandPool\n`
- `%lldus Thunderbolt DP - DPCM(%u) STAGE (5) Begin evaluation for [%u:0x%llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::registerWithDPConnectionManager\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - TBT depth = %u < TBT depth %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::dispatchNotifyDPConnectionManagerNeedEvaluation - dispatchAsync( notifyDPConnectionManagerNeedEvaluation )\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getLocalDPCapabilities - data = 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPath - use_primary_lane = %d, use_secondary_lane = %d, routing_options = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::unregisterFromDPConnectionManager\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::verifyAndReservePort - ( %p )->reserveDPPort( true, %p )\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPath - ERROR: setDestinationPort failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - creating videoPath\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findDPInPortAtRoute - adding DPI port 0x%x to affinity_port_array\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - creating fAuxTxReceiveCommandPool\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - port number = %u < port number %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `Thunderbolt DP - DPF [%d:0x%llx:0x%x] - DP_CON_CHANGE [%u:%u:%u]\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - WARNING: activating auxRxPath failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::logPathCreation - activating %s - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - DP_REMOTE_CAP = 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::free\n`
- `%lldus  %02x %02x`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::getSSCOffset - ssc_offset (prop) = 0x%x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findExistingPaths - ERROR: incomplete path set found: video_path = %p, aux_tx_path = %p, aux_rx_path = %p\n`
- `AppleThunderboltDPPathManager`
- `%lldus AppleThunderboltDPPathManager<%p>::findExistingPaths - number of active DPO paths = %d\n`
- `%lldus [LOG ERROR]`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - creating fAuxRxTransmitQueue\n`
- `121111121222121211122222211111111111122222222221112`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setRemoteDPCapabilities - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - creating fAuxRxReceiveQueue\n`
- `%lldus AppleThunderboltDPPathManager<%p>::startAllQueues - ERROR: starting fAuxRxReceiveQueue failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - ERROR: DPPMCallback not valid\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::broadcastUpdateEstimatedBandwidth - an adapter requested broadcast estimated bandwidth update\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getLocalDPCapabilities - data = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - DP_LOCAL_CAP = 0x%08x, overwriting with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPath - ERROR: new_path = NULL\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - WARNING: activating auxRxPathSnoopToSource failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::enableDP - ERROR: enableDP failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setDPState - commandWakeup( &fDPState )\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::unregisterFromDPConnectionManager - ERROR: DP connection manager not found!\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - WARNING: activating auxTxPathSnoopToSink failed with 0x%08x\n`
- `%lldus HPD\t\t`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::enableDP - disable video and aux\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::configHopIDs - configure video link\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getDPAdapterCapOffset - WARNING: fTerminated = true\n`
- `AppleThunderboltDPPathManagerOS`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - WARNING: activating videoPath failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPortInternal - ERROR: caller cannot release a reservation it does not hold\n`
- `%lldus AppleThunderboltDPPathManager<%p>::verifyAndReservePort - ( %p )->isAdapterAvailableForClient( %p )\n`
- `%lldus AppleThunderboltDPPathManager<<<static>>>::setDPPort - ERROR: could not find adapter (dp_client = %p, adapter_type = 0x%x)\n`
- `%lldus AppleThunderboltDPPathManager<%p>::startAllQueues - ERROR: queues not ready\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findDPInPortAtRoute - WARNING: unable to find available DPI port\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - ERROR: unrecognized pathSetType (%d)\n`
- `Thunderbolt DP - DPF [%d:0x%llx:0x%x] - DPTX_DISCOVERY\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findDPInPortAtRoute - adding DPI port 0x%x to nonaffinity_port_array\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::startAllQueues - submitted %d commands to fAuxTxReceiveQueue\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::stopAllQueues\n`
- `Group ID Array`
- `AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - ERROR: couldn't cast objects to DP adapters!, obj1 = %p, obj2 = %p\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::isAdapterAvailableForClient - client = %p, fReservedClient = %p, available = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - DP_LOCAL_CAP = 0x%08x\n`
- `tbdp_at_d`
- `%lldus AppleThunderboltDPPathManager<<<static>>>::setDPPort - ERROR: failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - creating auxRxPath\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to create fAuxRxTransmitQueue\n`
- `%lldus AppleThunderboltDPPathManager<%p>::destroySnoopRings - %d commands released from fAuxTxTransmitCommandPool\n`
- `%lldus SET_CONFIG\t`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::getSSCOffset - ssc_offset (default) = 0x%x\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - route = 0x%llx\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getMaxSupportedLinkRate - WARNING: fTerminated = true\n`
- `tbdp`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::notifyDPConnectionManagerNeedEvaluation - ERROR: DP connection manager not found!\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<<<static>>>::calculateDPBandwidthFromLinkRateAndLaneCount - link_rate = %u, lane_count = %u, number_of_lanes = %u, bandwidth = %u\n`
- `%lldus  %02x`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to allocate fAuxTxTransmitQueue\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::findOrCreateDPConnectionManager\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPath - source_hop_id_range = { %d, %d }\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::sendHPD - ERROR: fAuxRxTransmitQueue->submit() failed with 0x%08x\n`
- `\"AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - UNEXPECTED ERROR: Out of Group IDs! group_id = %u route = 0x%08llx\\n\" @%s:%d`
- `%lldus Thunderbolt DP - DPCM(%u) STAGE (4) Dequeue for evaluation (%u left), APR=%u RER=%u\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::dispatchRemoveNotifiers - ERROR: dispatchAsync( checkIfAllAdaptersFound ) failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::registerWithDPConnectionManager - ERROR: DP connection manager not found!\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findExistingPaths - number of active DPI paths = %d\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::transmitCommandCallback - ERROR: receive_queue->submit failed with 0x%08x\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter wants to deactivate = %u > Adapter wants to deactivate = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::start - rid = 0x%x, route = 0x%llx, port = 0x%02x, fChipType = 0x%x\n`
- `Evaluating Connections`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::setRemoteDPCapabilities - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::finalize - commandSleep( fWaitingForNotifiers )\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - creating fAuxTxTransmitQueue\n`
- `%lldus AppleThunderboltDPPathManager<%p>::transmitCommandCallback - WARNING: incomingStatus = 0x%08x\n`
- `%lldus  %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - creating auxRxPathSinkToSnoop\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::readDPCapabilitiesRegister - remote = %d\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - creating auxTxPathSourceToSnoop\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to create fAuxTxTransmitQueue\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to create fAuxRxTransmitCommandPool\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - creating fAuxRxTransmitQueue\n`
- `%lldus AppleThunderboltDPPathManager<%p>::sendAuxPacket - ERROR: insertAuxData failed with 0x%08x\n`
- `[UNKNOWN PATH TYPE]`
- `%lldus AppleThunderboltDPPathManagerOS<<<static>>>::setDPPort - ERROR: could not find adapter (dp_client = %p, adapter_type = 0x%x)\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::finalize - fWaitingForNotifiers woke up\n`
- `Aux Tx path (A)`
- `%lldus DPA  filtered\t`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::transmitCommandCallback - WARNING: incomingStatus = 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::insertAuxData - ERROR: transmit_queue->submit() failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findExistingPaths - all paths found\n`
- `unregister`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::writeDPCapabilitiesRegister - remote = %d\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findDPInPortAtRoute - reserving DPI: route 0x%llx, port 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::setDPState - commandWakeup( &fDPState )\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getTMUCapOffset - fTMUCapOffset = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::earlyWake\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPortInternal - clearing fReservedClient\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::enableDP - enable = %d\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPath - dest_hop_id_range = { %d, %d }\n`
- `status`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::enableDP - set adapter reset bit (0x%x)\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::readDPCapabilitiesRegister - DP_LOCAL_CAP = 0x%08x, overwriting with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::readDPCapabilitiesRegister - DP_LOCAL_CAP = 0x%08x\n`
- `%lldus  %02x %02x %02x %02x %02x %02x %02x %02x`
- `%lldus  %02x %02x %02x %02x`
- `%lldus AppleThunderboltDPConnectionManager(%u)::broadcastUpdateEstimatedBandwidth - requesting update estimated bandwidth for adapter at [%u:0x%llx:0x%x]\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::dispatchEvaluateConnections - evaluateConnections() is already running, request re-evaluation and exit\n`
- `TBTDPLowToHigh`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::determineMaxSupportedLinkRate - fMaxSupportedLinkRate = %d\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::reserveDPPortInternal - clearing fReservedClient\n`
- `tbdp_at_i`
- `%lldus AppleThunderboltDPPathManager<%p>::createPath - ERROR: pathSetConfigData = NULL\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - creating fAuxTxReceiveCommandPool\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findDPInPortAtRoute - DPI route = 0x%llx, DPI port = 0x%x, DPO route = 0x%llx, client = %p\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::destroySnoopRings\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getDFTCapOffset - ERROR: finding fDFTCapOffset failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::verifyAndReservePort - WARNING: reserveDPPort on port 0x%x (%p) failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::startAllQueues - ERROR: starting fAuxTxReceiveQueue failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::startAllQueues - ERROR: queues not ready\n`
- `12111112122212121211111111122`
- `Waiting for all DP adapters to register`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter wants to deactivate = %u < Adapter wants to deactivate = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter has HPD deassert = %u < Adapter has HPD deassert = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::enableDP - enable video and aux\n`
- `%lldus AppleThunderboltDPPathManager<%p>::receiveCommandCallback - ERROR: receive_queue->submit failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::getSSCOffset - ssc_offset (prop) = 0x%x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - creating fAuxTxTransmitCommandPool\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::insertAuxData - ERROR: data = %p, length = %d\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findExistingPaths - ERROR: DPI port not found for Rx path\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter has bandwidth allocation request = %u < Adapter has bandwidth allocation request = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::cleanup\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::needsEarlyWake\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::free\n`
- `Thunderbolt DP - DPCM(%u) Evaluating: %s, Evaluation Queue: `
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter failed to light = %u < Adapter failed to light = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - ERROR: failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<<<static>>>::setDPPort - ERROR: failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::configHopIDs - configure aux link\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getDPAdapterCapOffset - fDPAdapterCapOffset = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::cleanup\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::isAdapterAvailableForClient - WARNING: fStarted = false\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - found %d DPI ports @ route 0x%llx\n`
- `Registered DP Out Adapters`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getDFTCapOffset - fDFTCapOffset = 0x%x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::destroySnoopRings\n`
- `%lldus AppleThunderboltDPPathManager<%p>::transmitCommandCallback - ERROR: unrecognized path_type (%d)\n`
- `%s\n`
- `tbdp_v_s`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - There are DP ports without registered adapters, wait until all adapters are registered. (%d registered adapters, %d registered ports, %d ports in topology)\n`
- `AppleThunderboltDPConnectionManager(%u)::compareByDefaultActivationOrder - ERROR: Found 2 port objects with the same depth (%u), route string (0x%08llx), and port number (%u), adapter1<%p>, adapter2<%p>!\n`
- `12111112122212121112222221111111111111222222221112`
- `%lldus AppleThunderboltDPPathManager<%p>::updateExistingPaths - dp_bandwidth = %d\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to create tx_command\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPath - dest_hop_id_range = { %d, %d }\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPath - set PM Packet support\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::start\n`
- `\"Couldn't make a DP connection manager!!!\" @%s:%d`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - WARNING: activating auxRxPathSnoopToSource failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to allocate fAuxRxReceiveQueue\n`
- `%lldus AppleThunderboltDPPathManager<%p>::getSSCOffset - ssc_offset (bootarg) = 0x%x\n`
- `%lldus EDM  filtered\t`
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - found adapter [%u:0x%llx:0x%x] for current group\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::setDPState - changing state from %d to %d\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - WARNING: activating videoPath failed with 0x%08x\n`
- `%lldus < NULL >\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::verifyAndReservePort - ERROR: invalid port (%p)\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to create fAuxRxTransmitCommandPool\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::startAllQueues - ERROR: starting fAuxRxReceiveQueue failed with 0x%08x\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::checkForAdapterFailedToLight - An activated DP adapter that failed to light exists [%u:0x%llx:0x%x], adapter failed to light exists = %u\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::isAdapterAvailableForClient - client = %p, fReservedClient = %p, available = %d\n`
- `%lldus AppleThunderboltDPPathManager<%p>::startAllQueues - submitted %d commands to fAuxRxReceiveQueue\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::configHopIDs - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - found %u switches at depth %u\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getLocalDPCapabilities - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPPathManager<%p>::startAllQueues - ERROR: starting fAuxRxTransmitQueue failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::startAllQueues - ERROR: failed to submit rx_command to fAuxRxReceiveQueue\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::receiveCommandCallback - ERROR: unrecognized path_type (%d)\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setDPState - changing state from %d to %d\n`
- `%lldus AppleThunderboltDPPathManager<%p>::destroySnoopRings - %d commands released from fAuxRxTransmitCommandPool\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - creating fAuxRxReceiveQueue\n`
- `AppleThunderboltDPConnectionManager`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - Registered DP adapter count exceeds DP port count.. there are likely terminating adapters (%d registered adapters, %d registered ports, %d ports in topology)\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter failed to light = %u > Adapter failed to light = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::postEnableDPHook - enable = %d\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::destroySnoopRings - %d commands released from fAuxRxTransmitCommandPool\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::notifyNeedEvaluation - DP adapter at [%u:0x%llx:0x%x] requested evaluation\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPath - ERROR: setDestinationPort failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - WARNING: activating auxRxPathSinkToSnoop failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to create fAuxTxReceiveQueue\n`
- `%lldus AppleThunderboltDPPathManager<%p>::transmitCommandCallback - ERROR: incomingStatus = 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::logPathCreation - activating %s - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - creating auxTxPath\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::transmitCommandCallback - ERROR: leaking txCommand %p\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::updateExistingPaths - dp_bandwidth = %d\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::reserveDPPortInternal - ERROR: acquireDPAdapterSynchronous failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - WARNING: activating auxTxPath failed with 0x%08x\n`
- `%lldus -`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::setup\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::createResources\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::configHopIDs - deconfigure aux link\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::reserveDPPort - WARNING: fTerminated = true\n`
- `%lldus # RX ###\t`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::removeNotifiers - commandWakeup( fWaitingForNotifiers )\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::free\n`
- `AppleThunderboltDPInAdapter`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter has bandwidth allocation request = %u > Adapter has bandwidth allocation request = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `site.AppleThunderboltDPAdapterFamily`
- `tbsc`
- `bw_allocation_panic_value_100_mbps`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::destroySnoopRings - %d commands released from fAuxTxReceiveCommandPool\n`
- `Thunderbolt DP - DPF [%d:0x%llx:0x%x] - HPD = %d\n`
- `site.AppleThunderboltDPAdapterFamilyBase`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPath - credit_options = 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - WARNING: activating auxRxPathSinkToSnoop failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findExistingPaths - number of active DPO paths = %d\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - creating auxTxPath\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - creating fAuxTxReceiveQueue\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::checkForHigherPriorityPendingEvaluations - DP adapter at [%u:0x%llx:0x%x] checking for higher priority pending evaluations\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - found existing Group ID %u for route 0x%llx\n`
- `Evaluating DP Adapter`
- `%s `
- `DP Out Adapters Waiting for Evaluation`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter has desired state = %u > Adapter has desired state = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::writeDPCapabilitiesRegister - ERROR: failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findDPInPortAtRoute - WARNING: unable to find availble DPI port\n`
- `AppleThunderboltDPOutAdapter`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to create fAuxTxTransmitCommandPool\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to create fAuxRxTransmitQueue\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::configHopIDs - enable = %d\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::reserveDPPortInternal - setting fReservedClient = %p\n`
- `tbdp_at_s`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to allocate fAuxRxTransmitQueue\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findDPInPortAtRoute - available DPI found: route 0x%llx, port 0x%x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::startAllQueues - ERROR: starting fAuxTxTransmitQueue failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - route = 0x%llx, tunnel flags = 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::getSSCOffset - ssc_offset (default) = 0x%x\n`
- `Aux Rx path (B)`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter has HPD assert = %u < Adapter has HPD assert = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::enableDP - enable video and aux\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::postEnableDPHook - clear adapter reset bit (0x%x)\n`
- `%lldus AppleThunderboltDPPathManager<%p>::transmitCommandCallback - ERROR: receive_queue->submit failed with 0x%08x\n`
- `%lldus +`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::checkForHigherPriorityPendingEvaluations - Highest priority DP adapter is [%u:0x%llx:0x%x], higher priority evaluation exists = %u\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - freed existing Group ID %u for route 0x%llx\n`
- `reserve`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPortInternal - WARNING: this port is already reserved\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findDPInPortAtRoute - WARNING: unable to reserve DPI: route 0x%llx, port 0x%x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::startAllQueues - submitted %d commands to fAuxTxReceiveQueue\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - found %d DPO ports @ route 0x%llx\n`
- `%lldus Thunderbolt DP - DPCM(%u) STAGE (3) (Re-)Populate evaluation queue, FI=%u APR=%u RER=%u\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - re-evaluation requested, dispatching evaluation\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter waiting to terminate = %u > Adapter waiting to terminate = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::findOrCreateDPConnectionManager - ERROR: failed to attach the DP Connection Manager to the controller!\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - added %d commands to fAuxRxReceiveCommandPool\n`
- `AppleThunderboltDPOutAdapterBase`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::configHopIDs - enable = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::dispatchNotifyDPConnectionManagerNeedEvaluation - ERROR: dispatchAsync( notifyDPConnectionManagerNeedEvaluation ) failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<<<static>>>::setDPPort - ERROR: invalid port (%p)\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - ERROR: unrecognized pathSetType (%d)\n`
- `Aux Tx path (B)`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::verifyAndReservePort - WARNING: port 0x%x is already reserved\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::receiveCommandCallback - ERROR: receive_queue->submit failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findExistingPaths - number of active DPI paths = %d\n`
- `tbdp_v_i`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getTMUCapOffset - fTMUCapOffset = 0x%x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::free\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - creating auxTxPathSnoopToSink\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - added %d commands to fAuxTxTransmitCommandPool\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - creating fAuxRxReceiveCommandPool\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::sendAuxPacket - sequenceByte = 0x%02x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getDPInVSECOffset - fDPInVSECOffset = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getTMUCapOffset - ERROR: finding fTMUCapOffset failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::removeNotifiers - commandWakeup( fWaitingForNotifiers )\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - creating videoPath\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - creating fAuxRxTransmitCommandPool\n`
- `%lldus AppleThunderboltDPPathManager<%p>::receiveCommandCallback - ERROR: transmit_queue->submit failed with 0x%08x\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - route string = 0x%08llx < route string 0x%08llx, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - creating fAuxTxReceiveQueue\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::writeDPCapabilitiesRegister - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to create fAuxRxReceiveQueue\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::insertAuxData - ERROR: snoop appears to not be enabled, aborting\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - TBT depth = %u > TBT depth %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `client`
- `pathcr`
- `%lldus AppleThunderboltDPPathManager<%p>::verifyAndReservePort - WARNING: port 0x%x is already reserved\n`
- `%lldus  %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x %02x`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - WARNING: activating auxTxPathSourceToSnoop failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getDPOutVSECOffset - ERROR: finding fDPOutVSECOffset failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<<<static>>>::calculateDPBandwidthFromDPCapability - dp_capability = 0x%08x, link_rate = %d, lane_count = %d\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPath - req_bandwidth = %d, max_bandwidth = %d\n`
- `%lldus Thunderbolt DP - DPCM(%u) STAGE (2) Verify registered ports, FI=%u RER=%u\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::determineMaxSupportedLinkRate - ERROR: readDPCapabilitiesRegister failed (0x%08x)\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getChipType - chip_type = %d\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getLCCapOffset - fLCCapOffset = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::createResources - fDPConnectionManager = %p\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setRemoteDPCapabilities - no extended caps\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findDPInPortAtRoute - ERROR: unable to reserve DPI: route 0x%llx, port 0x%x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::receiveCommandCallback - WARNING: transmit_queue->submit failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::sendHPD - ERROR: fAuxRxTransmitQueue->submit() failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getMaxSupportedLinkRate - max_link_rate = %d\n`
- `DP State`
- `%lldus AppleThunderboltDPPathManager<%p>::verifyAndReservePort - ( %p )->reserveDPPort( true, %p )\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to create rx_command\n`
- `Thunderbolt DP - destroying %s - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x]\n`
- `Aux Tx path`
- `%lldus  `
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - allocated Group ID %u for route 0x%llx\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getLocalDPCapabilities - no extended caps\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findDPInPortAtRoute - WARNING: unable to reserve DPI: route 0x%llx, port 0x%x\n`
- `\"AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - UNEXPECTED ERROR: Tried to free an invalid Group ID! old_group_id = %u route = 0x%08llx\\n\" @%s:%d`
- `<%u:0x%08llx:0x%08x>`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findDPInPortAtRoute - reserving DPI: route 0x%llx, port 0x%x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findDPInPortAtRoute - adding DPI port 0x%x to nonaffinity_port_array\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::startAllQueues - ERROR: starting fAuxRxTransmitQueue failed with 0x%08x\n`
- `%lldus Thunderbolt DP - DPCM(%u) STAGE (5) Skipped evaluation for [%u:0x%llx:0x%x], APR=%u FW=%u\n`
- `Registered Ports`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::dispatchRemoveNotifiers - dispatchAsync( removeNotifiers )\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::findOrCreateDPConnectionManager - allocated the DP Connection Manager!\n`
- `site.AppleThunderboltDPPathManager`
- `%lldus AppleThunderboltDPPathManager<%p>::insertAuxData - ERROR: data = %p, length = %d\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::startAllQueues - submitted %d commands to fAuxRxReceiveQueue\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - allocated Group ID %u (=%u) for adapter at [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setDPState - current = %d, new = %d --> change = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::notifyDPConnectionManagerNeedEvaluation\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to create fAuxRxReceiveCommandPool\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - done, status = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::createResources\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::configHopIDs - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::setDPState - current = %d, new = %d --> change = %d\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - creating auxRxPath\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to allocate fAuxRxTransmitQueue\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - checking for DP ports at depth %u\n`
- `Thunderbolt DP - DPCM(%u) No evaluation in progress\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findExistingPaths - ERROR: incomplete path set found: video_path = %p, aux_tx_path = %p, aux_rx_path = %p\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findExistingPaths - no paths found\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - creating auxTxPathSourceToSnoop\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - UNEXPECTED ERROR: Tried to free an invalid Group ID! old_group_id = %u route = 0x%08llx\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::lateSleep\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::postEnableDPHook - set adapter reset bit (0x%x)\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPath - ERROR: setSourcePort failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<<<static>>>::setDPPort - ERROR: invalid port (%p)\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::readDPCapabilitiesRegister - DP_REMOTE_CAP = 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findDPInPortAtRoute - adding DPI port 0x%x to affinity_port_array\n`
- `site.AppleThunderboltDPPathManagerOS`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::reserveDPPortInternal - ERROR: updateCrossbar failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::writeDPCapabilitiesRegister - WARNING: fTerminated = true\n`
- `tblog`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPath - ERROR: new_path = NULL\n`
- `121111111111122222111111`
- `tbdp_v_d`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - done with iteration, fReevaluationRequested = %d\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::configHopIDs - deconfigure video link\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPortInternal - WARNING: this port is already unreserved\n`
- `%lldus AppleThunderboltDPPathManager<%p>::sendHPD - ERROR: unrecognized type (%d)\n`
- `%lldus < NO DATA >\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - using Group ID %u for route 0x%llx\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findExistingPaths - all paths found\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findExistingPaths - no paths found\n`
- `AppleThunderboltDPAdapterFamily`
- `%lldus AppleThunderboltDPPathManager<%p>::verifyAndReservePort - ERROR: invalid port (%p)\n`
- `%lldus AppleThunderboltDPPathManager<%p>::receiveCommandCallback - ERROR: unrecognized path_type (%d)\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::sendHPD - ERROR: unrecognized type (%d)\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::broadcastUpdateEstimatedBandwidth - done, status = 0x%08x\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - start\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getDPAdapterCapOffset - ERROR: finding fDPAdapterCapOffset failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPath - ERROR: pathSetConfigData = NULL\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::destroyPathSet\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - assigning Group ID %u to adapter [%u:0x%llx:0x%x]\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - All ports in the topology have a registered DP adapter!\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getLocalDPCapabilities - no extended caps\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::configHopIDs - configure aux link\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPortInternal - reserve = %d, client = %p, fReservedClient = %p\n`
- `tbdp_ar_s`
- `%lldus ACK\t\t`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - ERROR: createSnoopRings failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::receiveCommandCallback - ERROR: transmit_queue->submit failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::enableDP - clear adapter reset bit (0x%x)\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::isProviderPortHPDPacket - Thunderbolt HPD packet for rid = %d route = 0x%llx port = %d plug = %d\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - creating fAuxTxTransmitQueue\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::startAllQueues - ERROR: failed to submit rx_command to fAuxRxReceiveQueue\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - found %d DP ports in the topology\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findExistingPaths\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPath - ERROR: setSourcePort failed with 0x%08x\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter waiting to terminate = %u < Adapter waiting to terminate = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::createResources - fDPPathManager = %p\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::finalize\n`
- `AppleThunderboltDPAdapterFamilyBase.cpp`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - ERROR: DPPMCallback not valid\n`
- `Video path`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - WARNING: activating auxRxPath failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - creating fAuxRxTransmitCommandPool\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findDPInPortAtRoute - adding DPI port 0x%x to gpu_muxed_away_port_array\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findDPInPortAtRoute - availble DPI found: route 0x%llx, port 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::start - rid = 0x%x, route = 0x%llx, port = 0x%02x, fChipType = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getDPInVSECOffset - ERROR: finding fDPInVSECOffset failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::verifyAndReservePort - ERROR: invalid adapter (adapter_type = 0x%x, dp_client = %p)\n`
- `sscOffset`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::logPathDestruction - destroying %s - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setup\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::reserveDPPortInternal - WARNING: this port is already reserved\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::reserveDPPort - dispatchSync( reserveDPPortDispatch )\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::dispatchRemoveNotifiers\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to create fAuxTxReceiveQueue\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPortInternal - setting fReservedClient = %p\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to create fAuxTxReceiveCommandPool\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to create fAuxRxReceiveCommandPool\n`
- `tb`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::destroyResources\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setupNotifiers\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - ERROR: createSnoopRings failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - creating auxRxPathSinkToSnoop\n`
- `%lldus AUX_DATA\t`
- `AppleThunderboltDPInAdapterBase`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::verifyAndReservePort - ERROR: invalid adapter (adapter_type = 0x%x, dp_client = %p)\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::reserveDPPortInternal - ERROR: caller cannot release a reservation it does not hold\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::writeDPCapabilitiesRegister - remote = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::isAdapterAvailableForClient - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::registerDPAdapter - %s DP adapter at [%u:0x%llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPort - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findDPInPortAtRoute - adding DPI port 0x%x to gpu_muxed_away_port_array\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - UNEXPECTED ERROR: Out of Group IDs! group_id = %u route = 0x%08llx\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::needsEarlyWake\n`
- `Thunderbolt DP - DPF [%d:0x%llx:0x%x] - DP_BW\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::findOrCreateDPConnectionManager - ERROR: failed to allocate the DP Connection Manager!\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - creating auxTxPathSnoopToSink\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::verifyAndReservePort - WARNING: reserveDPPort on port 0x%x (%p) failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findExistingPaths\n`
- `AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - WARNING: failed to assign Group ID for adapter at [%u:0x%08llx:0x%x], tmp_status = 0x%08x, continuing\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - Registered DP adapter count matches DP port count! (%d registered adapters, %d registered ports, %d ports in topology)\n`
- `Cached Local DP Capabilities`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - creating fAuxRxReceiveCommandPool\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::createResources - fDPPathManager = %p\n`
- `Cached Local DP Capbilities`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::writeDPCapabilitiesRegister - writing DP_REMOTE_CAP = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::findOrCreateDPConnectionManager - found the DP Connection Manager!\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findDPInPortAtRoute - ERROR: unable to create switch array\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to create fAuxTxReceiveCommandPool\n`
- `%lldus \n`
- `\"AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - UNEXPECTED ERROR: Two or more adapters in the same group have different Group IDs! (%u != %u) [%u:0x%llx:0x%x]\\n\" @%s:%d`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::startAllQueues - ERROR: failed to submit rx_command to fAuxTxReceiveQueue\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - route string = 0x%08llx > route string 0x%08llx, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::dispatchNotifyDPConnectionManagerNeedEvaluation\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPathSet - creating auxRxPathSnoopToSource\n`
- `%lldus AppleThunderboltDPPathManager<%p>::startAllQueues - ERROR: starting fAuxTxTransmitQueue failed with 0x%08x\n`
- `%lldus 0x`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::receiveCommandCallback - WARNING: transmit_queue->submit failed with 0x%08x\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::dispatchEvaluateConnections - dispatching evaluateConnections()\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getLocalDPCapabilities - WARNING: fTerminated = true\n`
- `tbdp_ar_i`
- `%lldus AppleThunderboltDPPathManager<%p>::createPath - credit_options = 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findDPInPortAtRoute - ERROR: unable to reserve DPI: route 0x%llx, port 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::setRemoteDPCapabilities - no extended caps\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getDPOutVSECOffset - fDPOutVSECOffset = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::readDPCapabilitiesRegister - route = 0x%llx, tunnel flags = 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::insertAuxData - ERROR: snoop appears to not be enabled, aborting\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::verifyAndReservePort - ( %p )->isAdapterAvailableForClient( %p )\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - creating auxRxPathSnoopToSource\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to allocate fAuxTxReceiveQueue\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::writeDPCapabilitiesRegister - writing DP_LOCAL_CAP = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::isProviderPortHPDPacket - Thunderbolt HPD packet for rid = %d route = 0x%llx port = %d plug = %d\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::verifyAndReservePort - port_num = 0x%x, adapter_type = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::configHopIDs - deconfigure aux link\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to create tx_command\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::destroyResources\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getChipType - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::readDPCapabilitiesRegister - ERROR: failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPath - ERROR: unrecognized pathType (%d)\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - upstream cio port number is %u and the other adapter's port number is %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::finalize\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::writeDPCapabilitiesRegister - writing DP_REMOTE_CAP = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::dispatchRemoveNotifiersSynchronous\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPath - use_primary_lane = %d, use_secondary_lane = %d, routing_options = 0x%08x\n`
- `%lldus DPPM received\t`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::findDPInPortAtRoute - ERROR: unable to create switch array\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - found just one active adapter for route 0x%llx\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::lateSleep\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::dispatchRemoveNotifiers - ERROR: dispatchAsync( removeNotifiers ) failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - ERROR: failed to allocate fAuxTxTransmitQueue\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - UNEXPECTED ERROR: Two or more adapters in the same group have different Group IDs! (%u != %u) [%u:0x%llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::reserveDPPortInternal - reserve = %d, client = %p, fReservedClient = %p\n`
- `%lldus AppleThunderboltDPPathManager<%p>::verifyAndReservePort - port_num = 0x%x, adapter_type = 0x%x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::sendAuxPacket - sequenceByte = 0x%02x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to create fAuxTxTransmitQueue\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::sendAuxPacket - ERROR: insertAuxData failed with 0x%08x\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - check if all DP adapters are registered\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::dispatchRemoveNotifiers - dispatchAsync( removeNotifiers )\n`
- `%lldus AppleThunderboltDPPathManager<%p>::insertAuxData - ERROR: transmit_queue->submit() failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - WARNING: activating auxTxPathSourceToSnoop failed with 0x%08x\n`
- `AppleThunderboltDPAdapterFamilyBase`
- `%lldus AppleThunderboltDPPathManager<%p>::destroySnoopRings - %d commands released from fAuxRxReceiveCommandPool\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to create fAuxRxReceiveQueue\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::checkForAdapterFailedToLight - There is no DP adapter that failed to light, adapter failed to light exists = %u\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::transmitCommandCallback - ERROR: unrecognized path_type (%d)\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::isAdapterAvailableForClient - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getDPAdapterCapOffset - ERROR: finding fDPAdapterCapOffset failed with 0x%08x\n`
- `Remote DP Capabilities`
- `\"Special mode expects port 5 to be used but instead using port %d\\n\" @%s:%d`
- `%lldus Special mode expects port 5 to be used but instead using port %d\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::transmitCommandCallback - ERROR: incomingStatus = 0x%08x\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - clear the flags: first_iteration = %d, fReevaluationRequested = %d\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getDPAdapterCapOffset - fDPAdapterCapOffset = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::readDPCapabilitiesRegister - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPPathManager<%p>::destroySnoopRings - %d commands released from fAuxTxReceiveCommandPool\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to create rx_command\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::start\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::reserveDPPortInternal - ERROR: dropDPAdapterSynchronous failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getLCCapOffset - ERROR: finding fLCCapOffset failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::configHopIDs - deconfigure video link\n`
- `%lldus AppleThunderboltDPPathManager<%p>::findExistingPaths - ERROR: DPI port not found for Rx path\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - added %d commands to fAuxTxReceiveCommandPool\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter has HPD deassert = %u > Adapter has HPD deassert = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getDFTCapOffset - ERROR: finding fDFTCapOffset failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPath - ERROR: unrecognized pathType (%d)\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPath - source_hop_id_range = { %d, %d }\n`
- `%lldus ### TX #\t`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPort - dispatchSync( reserveDPPortDispatch )\n`
- `%lldus AppleThunderboltDPPathManager<%p>::logPathDestruction - destroying %s - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x]\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - WARNING: activating auxTxPathSnoopToSink failed with 0x%08x\n`
- `register`
- `AppleThunderboltDPConnectionManager<%p>(%u)::dispatchEvaluateConnections - ERROR: failed to dispatch evaluateConnections(), status = 0x%08x\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter has desired state = %u < Adapter has desired state = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - remote = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::writeDPCapabilitiesRegister - writing DP_LOCAL_CAP = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getMaxSupportedLinkRate - refresh = %d\n`
- `%lldus AppleThunderboltDPPathManager<%p>::destroyPathSet\n`
- `Thunderbolt DP - activating %s - SRC [%d:0x%llx:0x%x] DST [%d:0x%llx:0x%x] - req_bandwidth = %d\n`
- `%lldus AppleThunderboltDPConnectionManager(%u)::evaluateGroupIDForRouteString - found more than one active adapter for route 0x%llx\n`
- `AppleThunderboltDPConnectionManager.cpp`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::earlyWake\n`
- `Reserved Client`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to allocate fAuxRxReceiveQueue\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::evaluateConnections - finished evaluating connections with status = 0x%08x\n`
- `Aux Rx path`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createPathSet - WARNING: activating auxTxPath failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - ERROR: failed to create fAuxTxTransmitCommandPool\n`
- `Registered DP In Adapters`
- `%lldus AppleThunderboltDPPathManager<%p>::findDPInPortAtRoute - DPI route = 0x%llx, DPI port = 0x%x, DPO route = 0x%llx, client = %p\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getDFTCapOffset - fDFTCapOffset = 0x%x\n`
- `tbdp_ssc`
- `%lldus AppleThunderboltDPPathManager<%p>::stopAllQueues\n`
- `%lldus DPPM  xmitted\t`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::startAllQueues - ERROR: starting fAuxTxReceiveQueue failed with 0x%08x\n`
- `%lldus AppleThunderboltDPConnectionManager::compareByDefaultActivationOrder - Adapter has HPD assert = %u > Adapter has HPD assert = %u, prioritizing [%u:0x%08llx:0x%x] over [%u:0x%08llx:0x%x]\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - creating fAuxTxTransmitCommandPool\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::getSSCOffset - ssc_offset (bootarg) = 0x%x\n`
- `%lldus AppleThunderboltDPConnectionManager<%p>(%u)::checkForAdapterFailedToLight - DP adapter at [%u:0x%llx:0x%x] checking for adapter that failed to light\n`
- `AppleThunderboltDPConnectionManager(%u)::broadcastUpdateEstimatedBandwidth - WARNING: failed to update estimated bandwidth for adapter at [%u:0x%08llx:0x%x], status = 0x%08x, continuing\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::configHopIDs - configure video link\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::enableDP - WARNING: enableDP failed with 0x%08x (hardware removed?)\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::writeDPCapabilitiesRegister - ERROR: failed with 0x%08x\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createPath - req_bandwidth = %d, max_bandwidth = %d\n`
- `%lldus AppleThunderboltDPPathManager<%p>::createSnoopRings - added %d commands to fAuxRxTransmitCommandPool\n`
- `Aux Rx path (A)`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - added %d commands to fAuxRxTransmitCommandPool\n`
- `%lldus Thunderbolt DP - DPCM(%u) STAGE (1) Scan port topology, FI=%u RER=%u\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::free\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::dispatchRemoveNotifiers\n`
- `%lldus AppleThunderboltDPPathManager<%p>::transmitCommandCallback - ERROR: leaking txCommand %p\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - added %d commands to fAuxRxReceiveCommandPool\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::enableDP - disable video and aux\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getTMUCapOffset - ERROR: finding fTMUCapOffset failed with 0x%08x\n`
- `tbdp_ar_d`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::createSnoopRings - added %d commands to fAuxTxReceiveCommandPool\n`
- `%lldus AppleThunderboltDPPathManagerOS<%p>::destroySnoopRings - %d commands released from fAuxTxTransmitCommandPool\n`
- `site.AppleThunderboltDPConnectionManager`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::enableDP - enable = %d\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::earlyWakeComplete - commandWakeup fWaitforEarlyWakeComplete\n`
