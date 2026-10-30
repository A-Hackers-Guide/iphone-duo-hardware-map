# `AppleThunderboltDPOutAdapterOS`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltDPOutAdapter`](../kexts/com.apple.driver.AppleThunderboltDPOutAdapter.md)
- Object size: `0x2c8` (712 bytes)
- Metaclass: `0xfffffe000b9d1b10`; metaclass vtable `0xfffffe000827fe08`; class vtable `0xfffffe000827f128`
- Registration (init): `0xfffffe0009956a68`
- Superclasses: [`AppleThunderboltDPOutAdapterCM`](AppleThunderboltDPOutAdapterCM.md) → [`AppleThunderboltDPOutAdapterBase`](AppleThunderboltDPOutAdapterBase.md) → [`AppleThunderboltDPAdapterFamilyBase`](AppleThunderboltDPAdapterFamilyBase.md) → [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleThunderboltDPOutAdapterOS2`](AppleThunderboltDPOutAdapterOS2.md) — `com.apple.driver.AppleThunderboltDPOutAdapter`

## IOKit personalities that instantiate it (1)

- `AppleThunderboltDPOutAdapterOS` in [`com.apple.driver.AppleThunderboltDPOutAdapter`](../kexts/com.apple.driver.AppleThunderboltDPOutAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `11`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::doOpenSpecBandwidthAllocationMode - requesting DPCM to broadcast update estimated bandwidth\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::updateEstimatedBandwidth - done, fCachedEstimatedBW = %u, estimated_bandwidth = %u, status = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::postCreateDPTunnels - updating video path\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::doOpenSpecBandwidthAllocationMode - ERROR: failed to write CM_ID! status = 0x%08x\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::updateEstimatedBandwidth - ERROR: failed to write Estimated Bandwidth and Granularity! status = 0x%08x\n`
- `AppleThunderboltDPOutAdapterOS.cpp`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processDPBandwidthNotification - OPTION ENABLED: ignoring DP_BW notification\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - ERROR: failed to write 0 to CM Ack! cm_ack_status = 0x%08x\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::doOpenSpecBandwidthAllocationMode - ERROR: failed to write Maximal Link Rate and Lane Count! status = 0x%08x\n`
- `AppleThunderboltDPOutAdapterOS`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::doOpenSpecBandwidthAllocationMode - done, status = 0x%08x\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::configModifyDWordWithMask - WARNING: modifying %s returned: status = 0x%08x, retrying once\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - ERROR: DP paths are not all allocated!\n`
- `\"AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::updateEstimatedBandwidth - UNEXPECTED ERROR: DP video path is missing!\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::updateEstimatedBandwidth - UNEXPECTED ERROR: DP IN BW Allocation Mode not supported!\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processDPBandwidthNotification - notifying DP Connection Manager that we need evaluation\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - requesting DPCM to broadcast update estimated bandwidth\n`
- `\"AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - ERROR: failed to write 0 to CM Ack! cm_ack_status = 0x%08x\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterOS2<%p>::probe - service = %p\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - WARNING: CM Ack is already set! Applying workaround\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processDPBandwidthNotification - status = 0x%08x\n`
- `\"AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::doOpenSpecBandwidthAllocationMode - UNEXPECTED ERROR: DP video path is missing!\\n\" @%s:%d`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::configReadDWordProtected - WARNING: read %s returned: status = 0x%08x, retrying once\n`
- `\"AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::updateEstimatedBandwidth - UNEXPECTED ERROR: DP IN BW Allocation Mode not supported!\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - Beginning CM Ack flow\n`
- `%lldus AppleThunderboltDPOutAdapterOS2<%p>[%u:0x%llx:0x%x]::doOpenSpecALPM - done, status = 0x%08x\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::configModifyDWordWithMaskProtected - skipping modify DWORD [%u:0x%llx:0x%x] [s:%u, o:0x%08x, d:0x%08x, m:0x%08x] - \"%s\"\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::doOpenSpecBandwidthAllocationMode - established bandwidth is different from DPO local caps, restoring original caps: DPI remote writeDPCapabilitiesRegister( 0x%08x )\n`
- `\"AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - ERROR: failed to write new Allocated BW! status = 0x%08x\\n\" @%s:%d`
- `\"AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - ERROR: failed to read DPTX Req! status = 0x%08x\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - Finished CM Ack workaround, cm_ack_status = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::doOpenSpecBandwidthAllocationMode - dpo_link_rate = %u, dpo_lane_count = %u, dpi_link_rate = %u, dpi_lane_count = %u\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::assignGroupID - Group ID (%u -> %u)\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::assignGroupID - ERROR: failed to get DPI capabilities offset! status = 0x%08x\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::updateEstimatedBandwidth - WARNING: estimated bandwdith exceeded maximum value, estimated_bandwidth = %d, max value = %d\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - ERROR: failed to write 1 to CM Ack! cm_ack_status = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::updateEstimatedBandwidth - UNEXPECTED ERROR: DP video path is missing!\n`
- `%lldus AppleThunderboltDPOutAdapterOS2<%p>[%u:0x%llx:0x%x]::doOpenSpecALPM - ALPM Support = %u\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::doOpenSpecBandwidthAllocationMode - DPI does not support extended capabilities, skip\n`
- `\"AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - ERROR: failed to write 1 to CM Ack! cm_ack_status = 0x%08x\\n\" @%s:%d`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::doOpenSpecBandwidthAllocationMode - force enabling DP In BW Allocation Mode Support\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - ERROR: got an error polling DPTX Req! dptx_poll_status = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - Beginning CM Ack workaround\n`
- `AppleThunderboltDPOutAdapterOS2`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::configPollDWordWithMaskProtected - skipping modify DWORD [%u:0x%llx:0x%x] [s:%u, o:0x%08x, v:0x%08x, m:0x%08x, i:0x%08x, c:0x%08x] - \"%s\"\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::finishStateChangeCompleteInternal - done\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - UNEXPECTED ERROR: DP IN BW Allocation Mode not supported!\n`
- `%lldus AppleThunderboltDPOutAdapterOS2<%p>[%u:0x%llx:0x%x]::doOpenSpecALPM - cl1_exit_time = %u\n`
- `\"AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - ERROR: failed to read CM Ack (workaround)! cm_ack_status = 0x%08x\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>::initializeMemberVariables\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - WARNING: DPTX Req = 0\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - done, status = 0x%08x, cm_ack_status = 0x%08x dptx_poll_status = 0x%08x\n`
- `\"AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - ERROR: got an error polling DPTX Req! dptx_poll_status = 0x%08x\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::deactivateAdapterInternal - requesting DPCM to broadcast update estimated bandwidth\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - DPTX Req = 0x%08x\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::assignGroupID - ERROR: failed to set Group ID! status = 0x%08x\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::processBandwidthAllocationRequest - ERROR: failed to read Requested Bandwidth! status = 0x%08x\n`
- `AppleThunderboltDPOutAdapterOS2<%p>[%u:0x%llx:0x%x]::doOpenSpecALPM - ERROR: failed to write CL1 Exit Time! status = 0x%08x\n`
