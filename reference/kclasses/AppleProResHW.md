# `AppleProResHW`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md)
- Object size: `0x7f8` (2,040 bytes)
- Metaclass: `0xfffffe000b989750`; metaclass vtable `0xfffffe00081accf0`; class vtable `0xfffffe00081ac798`
- Registration (init): `0xfffffe00093ff120`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (19)

- `apr-a` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,a0', 'apr,a1', 'apr,a2']`
- `apr-b` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,b0']`
- `apr-c` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,c0']`
- `apr-d` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,d0', 'apr,d1', 'apr,d2']`
- `apr-e` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,e0']`
- `apr-f` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,f0']`
- `apr-g` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,g0']`
- `apr-h` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,h0', 'apr,h1', 'apr,h2']`
- `apr-i` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,i0']`
- `apr-j` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,j0', 'apr,j1']`
- `apr-k` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,k0']`
- `apr-l` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,l0']`
- `apr-m` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,m0']`
- `apr-n` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,n0', 'apr,n1', 'apr,n2']`
- `apr-o` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,o0']`
- `apr-p` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,p0']`
- `apr-q` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,q0']`
- `apr-r` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,r0', 'apr,r1', 'apr,r2']`
- `apr-s` in [`com.apple.driver.AppleProResHW`](../kexts/com.apple.driver.AppleProResHW.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['apr,s0']`

## Strings in its kext that name it (60)

- `ERROR AppleProResHW (0x%x): %d: %s(): Invalid method selector\n`
- `AppleProResHW (0x%x): %s(): m_pPMPBandwidthScratchRegMemMapProRes[%p]: v addr = %p ph adr = %p\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): Cannot acquire IOFence for encInputIOSurface\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): Failed to map decoder input buffer with DART. ret = 0x%x.\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): Cannot clear DelayList\n`
- `ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot retrieve or map registers memory object for extended scodec_ps: sys, ced, sys_ssw\n`
- `AppleProResHW (0x%x): %s(): remove leftover decOutputBufRef\n`
- `AppleProResHW (0x%x): %s(): coreIdx = %u DVA = 0x%llx CSID = %d elapsedTime = %lluns\n`
- `AppleProResHW (0x%x): %s(): m_NumClients (%d) >= m_numCoresOwned + 2 (%d) or m_NumDecodeClients (%d) >= m_numCoresOwned (%d) or m_NumEncodeClients (%d) >= m_numCoresOwned (%d), loadBalance mode changed to kLoadBalanceClientFixedToOneCore`
- `ERROR: AppleProResHW: %d: %s(): abort q'd cmds %d\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): Invalid coreIdx %d\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): Program EncodeRAW Descriptor failed\n`
- `AppleProResHW (0x%x): %s(): DecodeYCbCr: Program Input Address=%08x.%08x OffsetH,V=%u,%u SizeH,V=%u,%u\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): No resources to allocate Descriptor ring memory\n`
- `AppleProResHW (0x%x): %s(): override: Compressed=0x%x Packed=0x%x, Interleaved=0x%x Folded=0x%x`
- `ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: cannot allocate m_pClientListLock\n`
- `ERROR AppleProResHW: %d: %s(): kIODARTMapperEarlyReclaimKey failed 0x%x\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): Failed to map encoder output buffer with DART. ret = 0x%x.\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): Could not disable power.\n`
- `AppleProResHW (0x%x): %s(): coreIdx %u: PSD device - cannot set perf state as m_pSetPerfStateFunction is NULL`
- `AppleProResHW (0x%x): %s(): m_RegisterMemMapScodecPS[%d].pIOMemoryMap[%d] = (%p): v addr = %p ph adr = %p \n`
- `ERROR AppleProResHW (0x%x): %d: %s(): m_DRTail[%d]=0x%x > m_DRHead[%d]=0x%x\n`
- `AppleProResHW (0x%x): %s(): subFrame:Id=%d num=%d\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): Could not map bitstream buffer with DART for Ring Descriptor Memory. mapRet = 0x%x.\n`
- `ERROR: AppleProResHW: %d: %s(): enablePsdService(POWER_ON) Failed ret=0x%x\n`
- `AppleProResHW (0x%x): %s(): Published RT bandwidth`
- `ERROR AppleProResHW: %d: %s(): Cannot find encode user client info\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): Failed to map encoder statistics buffer with DART. ret = 0x%x.\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): AppleProResCommandQueue ERROR: Dequeue called for empty queue\n`
- `AppleProResHW (0x%x): %s(): m_coreWorkload[%d] = %u\n`
- `AppleProResHW (0x%x): %s(): EncodeFrameDone: m_coreWorkload[%d] = %u deQ curr Cmd[%d] frame# %d DROffs 0x%x CmdQ %d\n`
- `AppleProResHW (0x%x): %s(): [%d] cmd[%d] Q to DROffset 0x%x next 0x%x # %d DVA 0x%llx\n`
- `AppleProResHW (0x%x): %s(): kPowerOnPending, m_ePowerState[%d]=%d, isCoreOwner(%d)=%d\n`
- `AppleProResHW (0x%x): %s(): kPowerOffPending, numCores %d, m_ePowerState[%d]=%d\n`
- `ERROR AppleProResHW: %d: %s(): AppleProResHW Debug: Failing probe for core3 harvested simulation\n`
- `AppleProResHW (0x%x): %s(): CurrentClient->perfMode %d pDecodeFrame->perfMode %d\n`
- `AppleProResHW (0x%x): %s(): DecodeRaw cmd: fid=%d SwBR=%d 2raw=%d Int=%d dec=%d ga=%d cmpGaEn=%d ds=%d bd=%d cmd-word %08x cmdX-word %08x pk=%d iv=%d cpd=%d FO=%d Fld=%d\n`
- `AppleProResHW (0x%x): %s(): CFA=%d plane allocSize=%llu, planeSize=%u BytesPerRow=%u Data/Stride R=%llx/%u\n`
- `AppleProResHW (0x%x): %s(): terminate() failed.\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): Could not attach user client.\n`
- `ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: Cannot allocate m_pInitLock\n`
- `AppleProResHW (0x%x): %s(): Protected IOSurface is not allowed.`
- `ERROR AppleProResHW (0x%x): %d: %s(): pIOSurface NULL\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): [%d] DecodeFrame ERROR: Out of desc ring, pending %d\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): Power is Off or ProRes doesn't own core %d. Will not clear DelayList\n`
- `AppleProResHW (0x%x): %s(): m_DescRingMemInfo[%d] size %d kAddr %llx DartVM %llx\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): Failed calling start on provider\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): ProRes_EncodeFrame_UserKernel_In_Info NULL\n`
- `AppleProResHW (0x%x): %s(): ProRes Device info: %s \n`
- `ERROR: AppleProResHW: %d: %s(): Invalid DevID %d, no AXI values have been set\n`
- `AppleProResHW (0x%x): %s(): PSD Reset device \n`
- `ERROR AppleProResHW: %d: %s(): AppleProRes ERROR: invalid error type %s\n`
- `AppleProResHW (0x%x): %s(): pIOSurface = %p, pIOFence = %p, ret = 0x%x\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): Zero NumClients\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): No provider for UserClient\n`
- `ERROR AppleProResHW (0x%x): %d: %s(): InInfo->encOutputIOSurface CSID(%d) NULL.\n`
- `ERROR: AppleProResHW: %d: %s(): [%d] commandQ=%d IRQ=0x%x IRQ-En=0x%x st0=0x%x st1=0x%x st2=0x%x m_pTimerEventSource %p\n\n`
- `AppleProResHW (0x%x): %s(): Started core acquisition timer`
- `AppleProResHW (0x%x): %s(): Powering coreIdx %d on\n`
- `AppleProResHW (0x%x): %s(): DecodeFrameDone: m_coreWorkload[%d] = %u deQ curr Cmd[%d] frame# %d DROffs 0x%x CmdQ %d\n`
