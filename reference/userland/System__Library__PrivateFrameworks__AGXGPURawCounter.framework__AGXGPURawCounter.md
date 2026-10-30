# `/System/Library/PrivateFrameworks/AGXGPURawCounter.framework/AGXGPURawCounter`

iOS 27.2 dyld shared cache image. Version `362.5.0.0.0`. **[DSC]**

## Linked libraries (7)

- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/PrivateFrameworks/IOGPU.framework/IOGPU`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`

## Strings (360)

```
AGXGRC:AGXGRC:%s:%d:%s: *** Counter width must be 16, 32, 48, or 64!\n
AGXGRC:AGXGRC:%s:%d:%s: *** Inconsistent ring buffer count for source[%u]. (%u != %u)\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"((cfCoreMask = (CFNumberRef)CFArrayGetValueAtIndex(cfCoreMaskList, i)) != NULL) && CFNumberGetValue(cfCoreMask, kCFNumberSInt32Type, (void*)(&coreMask))\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"CFNumberGetValue (cfIndex, kCFNumberSInt32Type, &index) && (index < _partitionInfoNum) && ((cfName == NULL) || CFStringGetCString(cfName, _partitionInfoList[index].name, sizeof(_partitionInfoList[index].name), 
AGXGRC:AGXGRC:%s:%d:%s: *** \"sourceCounterIdxList[i] != NULL\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** Sampling has been started! Stop sampling before starting again.\n
AGXGRC:AGXGRC:%s:%d:%s: *** Invalid ring buffer count (%u)!\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"info != NULL\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"perfCtrSamplerGetSourceInfo(sourceIdx, &sourceInfo, _sharedConnection) == KERN_SUCCESS\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** parseSampleHeader() is not set!\n
AGXGRC:AGXGRC:%s:%d:%s: *** Unexpected number of kickslot data to be added to the queue!\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"((cfContTimeOffset = (CFNumberRef)IORegistryEntryCreateCFProperty(_acceleratorPort, CFSTR(\"ContTimeOffset\"), NULL, 0)) != NULL) && CFNumberGetValue(cfContTimeOffset, kCFNumberSInt64Type, (void*)(&_samplingSta
AGXGRC:AGXGRC:%s:%d:%s: *** \"(_partitionInfoList[index].optInfo = (OptionalPartitionInfo*)malloc(sizeof(OptionalPartitionInfo))) != NULL\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"(_sourceList[sourceIdx] = chipDispatchTable->createSource( this, sourceIdx, &sourceInfo, sourceCounterIdxList[sourceIdx], sourceCounterIdxNum [sourceIdx], chipDispatchTable)) != nullptr\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** srcSize/Read/Write is not aligned to 64-bits!\n
AGXGRC:AGXGRC:%s:%d:%s: *** Potential intermediate buffer overflow! (bufferSize=%llu processedPayloadSizeMax=%llu)\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"plistPath != nil\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"(cfShaderProfilerCounterName = CFStringCreateWithCString(kCFAllocatorDefault, shaderProfilerCounterName, kCFStringEncodingUTF8)) != NULL\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"chipDispatchTable != nullptr\"\n
AGXGRC:AGXGRC:%s:%d:%s: !!! AGXGPURawCounterImpl is not initialized!\n
AGXGRC:AGXGRC:%s:%d:%s: *** Metadata (%s) counter must be added before any other counters!\n
AGXGRC:AGXGRC:%s:%d:%s: *** Insufficient space to add metadata counter (%s)!\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"(_sharedConnection = IOGPUDeviceGetConnect(_deviceRef)) != 0\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** Amount of data to be drained must be aligned to 64-bits!\n
AGXGRC:AGXGRC:%s:%d:%s: *** HW counter (%s) must be added before any shader profiler counters!\n
AGXGRC:AGXGRC:%s:%d:%s: *** calcBufferSizeWithRingBufferSize should never be called with zero buffer size!\n
AGXGRC:AGXGRC:%s:%d:%s: *** Source sample size is unexpectedly larger than the maximum! (%llu > %u)\n
AGXGRC:AGXGRC:%s:%d:%s: *** Unknown meta counter type!\n
AGXGRC:AGXGRC:%s:%d:%s: *** Selectable events must be specified via the EventSelect array option\n
AGXGRC:AGXGRC:%s:%d:%s: *** Invalid ring buffer index (%u >= %u)\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"_sourceNum <= AGXGPURawCounterImpl::kSourceNumMax\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"(counterDesc.name != NULL) && (counterDesc.description != NULL)\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"(counterDesc.nameLen >= 2) && (counterDesc.descriptionLen >= 2)\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** Insufficient space to add HW counter (%s)!\n
AGXGRC:AGXGRC:%s:%d:%s: *** Counter width must be <= 32 as \"%s\" has only 32 valid bits\n
AGXGRC:AGXGRC:%s:%d:%s: *** alignBufferSize should never be called with zero buffer size!\n
AGXGRC:AGXGRC:%s:%d:%s: *** Ring buffers have not been allocated. Was sampling ever started on source %s?\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"((cfAbsTimeOffset = (CFNumberRef)IORegistryEntryCreateCFProperty(_acceleratorPort, CFSTR(\"AbsTimeOffset\"), NULL, 0)) != NULL) && CFNumberGetValue(cfAbsTimeOffset, kCFNumberSInt64Type, (void*)(&_samplingState.
AGXGRC:AGXGRC:%s:%d:%s: *** Fail to find dispatch table for gpuGen=%u sourceName=%s\n
AGXGRC:AGXGRC:%s:%d:%s: *** Insufficient free space in the final destination buffer!\n
AGXGRC:AGXGRC:%s:%d:%s: *** kick_timestamp > rde_sample_timestamp, [%u] timestampMax=%16llx timestamp=%16llx type=%2u encoderId=%8x traceId=%8x slotIdx=%2u\n\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"((cfCoreConfig = createInternalCoreConfigDict(_sharedConnection)) != NULL) && ((cfCoreNum = (CFNumberRef)CFDictionaryGetValue(cfCoreConfig, CFSTR(\"num_cores\"))) != NULL) && CFNumberGetValue(cfCoreNum, kCFNumb
AGXGRC:AGXGRC:%s:%d:%s: *** \"driverBundle != nil\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** Failed to reserve pre-determined counterDesc space from allocator!\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"allocator.reserve(sizeof(CounterDescImpl) * _masterCounterNum) != NULL\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"IOGPUDeviceGetName(_deviceRef, _deviceName, sizeof(_deviceName)) == kIOReturnSuccess\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"CFNumberGetValue(cfEventSelectsNumMax, kCFNumberSInt32Type, &eventSelectsNumMax)\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** Invalid ring buffer index (%u >= %u)!\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"(_deviceRef = IOGPUDeviceCreate(_acceleratorPort)) != NULL\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"((cfMmetalPluginName = (CFStringRef)IORegistryEntryCreateCFProperty(_acceleratorPort, CFSTR(\"MetalPluginName\"), NULL, 0)) != NULL) && CFStringGetCString(cfMmetalPluginName, metalPluginName, sizeof(metalPlugin
AGXGRC:AGXGRC:%s:%d:%s: *** \"buildMasterCounterListInitialize()\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"_sourceList[sourceIdx] == nullptr\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"(allocator.free() == 0) && (perfCtrIdx == _masterCounterNum)\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** chip dispatch table is not propertly set!\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"((cfPartitionInfoList = (CFArrayRef)IORegistryEntryCreateCFProperty(_acceleratorPort, CFSTR(\"PerfCtrPartitionInfoList\"), NULL, 0)) != NULL) && ((_partitionInfoNum = (uint32_t)CFArrayGetCount(cfPartitionInfoLi
AGXGRC:AGXGRC:%s:%d:%s: *** Inconsistent sub-buffer count! (%u != %u)\n
AGXGRC:AGXGRC:%s:%d:%s: *** Error, invalid uscIndex (%u >= %u) and/or invalid regIndex (%u >= %u)!\n
AGXGRC:AGXGRC:%s:%d:%s: *** Failed to retrieve dictionary info for perf counter '%s'\n
AGXGRC:AGXGRC:%s:%d:%s: *** All parameters must be non-zero! (src=%p size=%llu read=0x%p write=%llu dst=0x%p size=%llu read=%llu write=%p\n
AGXGRC:AGXGRC:%s:%d:%s: *** Error, adding unknown trigger (0x%x)\n
AGXGRC:AGXGRC:%s:%d:%s: *** Cannot add user-defined counter (%s) using GPURawCounter internal partition!\n
AGXGRC:AGXGRC:%s:%d:%s: *** Fail to allocate ring buffer for source[%u]!\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"perfCtrSamplerGetSourceNum(&_sourceNum, _sharedConnection) == KERN_SUCCESS\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"(cfIndex != NULL) || (cfFreeNum != NULL) || (cfSourceMask != NULL)\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"(cfDict = cfDictionaryCreateFromPlist([plistPath UTF8String])) != NULL\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"((perfCtrList = (CFArrayRef)CFDictionaryGetValue(cfDict, CFSTR(\"DeviceCounters\"))) != NULL) && ((perfCtrNum = (uint32_t)CFArrayGetCount(perfCtrList)) != 0)\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"ret && (perfCtrIdx != 0) && (sourceMaskAll != 0)\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** dstSize/Read/Write is not aligned to 64-bits!\n
AGXGRC:AGXGRC:%s:%d:%s: *** \"buildMasterCounterListFinalize()\"\n
AGXGRC:AGXGRC:%s:%d:%s: *** Error, reserving more than available memory! (%u > %llu)\n
AGXGRC:AGXGRC:%s:%d:%s: *** srcRead and/or dstWrite is out of bound! (*srcRead=%llu size=%llu *dstWrite=%llu size=%llu\n
AbsTimeOffset
_6603636646e67d7b38cf68c5008435aad6d5a66027b296efde7009cd434f5332
Kick trace ID. Valid only for kick boundary sample. ** MUST be added BEFORE any HW counter **
AGXGRC:%s:%d:%s: *** alignBufferSize should never be called with zero buffer size!\n
_8559a1fb193dfac9b2b12abcf6576fabd1e8adf0f89f747295d96e677b62f8b8
_a39457ef02c4eba61c7c4f20947a9faef25c665daad750eb237765576919727c
AGXGRC:%s:%d:%s: *** \"((cfCoreMask = (CFNumberRef)CFArrayGetValueAtIndex(cfCoreMaskList, i)) != NULL) && CFNumberGetValue(cfCoreMask, kCFNumberSInt32Type, (void*)(&coreMask))\"\n
GBL_USC_PROFILE_DATA_00_USC_00
_bc5df9147f8d326921739e3d106fad58481c04f9c13797f55a00a1f82aad96d4
_a15d25db5b58bb3c0e8476af40e7f148eb3815e4f840a0a86454d577d7df3efa
_1c78734593e462261ce75dbf17c5e07b05be1e860464e30a26d8a4530efcb3a4
_8bfc7b1f9d249874ac4bceb13bd33db0a07019e40966575d55f67024e5ba9b1b
AGXGRC:%s:%d:%s: *** \"driverBundle != nil\"\n
_028a38375018839c82eab7982165ba80bb66c92e4a3e8d77e50c7d756935df2e
_7607e6e2405d82a59dec3f22c6c38f944423754f2d01427743e0bdf027f83a68
EmitPos
AGXGRC:%s:%d:%s: *** \"IOGPUDeviceGetName(_deviceRef, _deviceName, sizeof(_deviceName)) == kIOReturnSuccess\"\n
gpu_gen
TAKickEnd
_96edb4c311b04cf93d502c01085cefacefb6e5e1658d08c8f1f9028c7309bd2b
_8acbc6551dd07639b7e6d3a1303cb6910c60d429b3f041395cd8ded423f06c44
chipDispatchTableForSource
DisableOverlap
SourceBufferSizeInKB
BufferSizeInKB
num_mgpus
PerfCtrPartitionInfoList
_212ddf4a034092ca1e63afb1f396088951e969487c65a9d01e49061ed180298f
AGXGRC:%s:%d:%s: *** \"((cfMmetalPluginName = (CFStringRef)IORegistryEntryCreateCFProperty(_acceleratorPort, CFSTR(\"MetalPluginName\"), NULL, 0)) != NULL) && CFStringGetCString(cfMmetalPluginName, metalPluginName, sizeof(metalPluginName), 
/AppleInternal/Library/AGX/Performance/%s/AGXMetalPerfCounters.plist
3DKickEndTimestamp
CLKickEndTimestamp
Sub-source ID. ** MUST be added BEFORE any HW counter **
_ea278f3104373805151ccd1366be515e7efcfea751c5317591340b6a2957ce87
virtual bool AGXGPURawCounterImpl::setGPUPerfState(uint32_t)
AGXGRC:%s:%d:%s: *** Invalid ring buffer index (%u >= %u)\n
AGXGRC:%s:%d:%s: *** \"((perfCtrList = (CFArrayRef)CFDictionaryGetValue(cfDict, CFSTR(\"DeviceCounters\"))) != NULL) && ((perfCtrNum = (uint32_t)CFArrayGetCount(perfCtrList)) != 0)\"\n
virtual bool AGXGPURawCounterImpl::startSampling()
_dc648ffae2d11fae6f40e3415c7016686141c75f5e5248823a881a299dca9a14
copyMetaCounterList
AGXGRC:%s:%d:%s: *** \"allocator.reserve(sizeof(CounterDescImpl) * _masterCounterNum) != NULL\"\n
Source ID. ** MUST be added BEFORE any HW counter **
postProcessData
AGXGRC:%s:%d:%s: *** Insufficient free space in the final destination buffer!\n
AGXGRC:%s:%d:%s: *** kick_timestamp > rde_sample_timestamp, [%u] timestampMax=%16llx timestamp=%16llx type=%2u encoderId=%8x traceId=%8x slotIdx=%2u\n\n
rb
_c294c37a2ef850efbcc73686d32117dd11e47c4f8eb046b0de7844c8f0f9a573
_20208f9ab4416d8278aac00fd86af2e1f9b5e0ee1afbbbb6a485ffc137cb60d8
AGXGRC:%s:%d:%s: *** Error, reserving more than available memory! (%u > %llu)\n
Timestamp when the sample is taken in n-clock tick. ** MUST be added BEFORE any HW counter **
AGXGRC:%s:%d:%s: *** Error, adding unknown trigger (0x%x)\n
AGXGRC:%s:%d:%s: *** Cannot add user-defined counter (%s) using GPURawCounter internal partition!\n
AGXGRC:%s:%d:%s: *** Fail to allocate ring buffer for source[%u]!\n
operator()
GRC_SUB_SOURCE_ID
SystemTimePeriod
AGXGRC:%s:%d:%s: *** \"((cfAbsTimeOffset = (CFNumberRef)IORegistryEntryCreateCFProperty(_acceleratorPort, CFSTR(\"AbsTimeOffset\"), NULL, 0)) != NULL) && CFNumberGetValue(cfAbsTimeOffset, kCFNumberSInt64Type, (void*)(&_samplingState.absTime
event_selects_num_max_list
Sample type (TA kick start/end, etc). ** MUST be added BEFORE any HW counter **
addTrigger_block_invoke
AGXGRC:%s:%d:%s: *** Selectable events must be specified via the EventSelect array option\n
ReadThreshold
obfuscatedUSCProfileName
_3db6b9ee25cabbc8d43e92a3f3999b477e90fedab5146cade30d72089def82fa
_259f973fb86f28b91137a13e6c6d3073a884637867d0c3d2331062c946773b7b
_11e02291883a066a05051a8a65c086043ceab5bbf31f442b3a12da26a7900977
Partition
AGXGPURawCounterSourceAPSImpl.mm
KickTimestamp
_ad5e5242674d4c53c3cf93b3676d4e8ab3e718c545a0e6085c28729f0345008a
AGXGRC:%s:%d:%s: *** Failed to retrieve dictionary info for perf counter '%s'\n
B12@?0i8
AGXGRC:%s:%d:%s: *** \"_sourceNum <= AGXGPURawCounterImpl::kSourceNumMax\"\n
AGXGRC:%s:%d:%s: *** \"(_deviceRef = IOGPUDeviceCreate(_acceleratorPort)) != NULL\"\n
_10709c421d0cd17c2abad53ef74f920d8cf61496d93ddbb2236f2184a6f8376c
TargetThreshold
AGXGRC:%s:%d:%s: *** All parameters must be non-zero! (src=%p size=%llu read=0x%p write=%llu dst=0x%p size=%llu read=%llu write=%p\n
ContTimeOffset
SyncDrainMode
addTrigger
postProcessReset
_a4f6668160aac3fe6078c7242087f391f340d2ee20767663566f29d49a4ec326
_e27d2fe7c6525911fe5480a790c46d25cad21319c4bcd983ba5f3a241f86779a
_afdc9e059619ecbabafbd3e16ff3ede7b18888b5acc5b2083b90e986e8b058a3
AGXGRC:%s:%d:%s: *** Failed to reserve pre-determined counterDesc space from allocator!\n
/System/Library/Extensions/%s.bundle
BMPR_RDE
_e3f98f0b565ac7b8f78c890e3d1e551b968eadef54148e347e84f4ff9c4238f4
AGXGRC:%s:%d:%s: *** calcBufferSizeWithRingBufferSize should never be called with zero buffer size!\n
AGXGRC:%s:%d:%s: *** \"(_partitionInfoList[index].optInfo = (OptionalPartitionInfo*)malloc(sizeof(OptionalPartitionInfo))) != NULL\"\n
_41dcdfbaf3b45fff80d22d04f459d2fe0f6fa20f45661614549e61bd3cbdeec7
_d31683364b183eddce97badb9fd6dc7a5c576bc62f997737809a53adb2d644d4
APS_USC
free_num
name
_c5de75234561497463498b27faad30740fe0a55c3ecf802992cd751ebcc8d553
virtual uint32_t AGXGPURawCounterImpl::sourceList(Source **, uint32_t)
3DKickStartTimestamp
SWResetOnRead
ringBufferAlloc
mGPUMask
core_mask_list
ConstantAGX_PostProcessBufferSizeMin
_c2457745b53d6a543543b037d5a4ecf76f0ae2b4669251b02907d927060ce404
_4855a7a22dac1c11f346062739f06eedd88b05896da422b95d2af8782073a526
GRC_SHADER_PROFILER_DATA_00
@\"NSNumber\"24@?0@\"NSString\"8@\"NSDictionary\"16
virtual bool AGXGPURawCounterImpl::setFlags(uint32_t)
_c68ce0c92b300d5cc1fca4a76ac7094534d3aa8ff8f059b1e7c38be89381441b
bad_optional_access was thrown in -fno-exceptions mode
Select
AGXGRC:%s:%d:%s: *** srcSize/Read/Write is not aligned to 64-bits!\n
_a445d6ebbd353b7ef84ef76162810f44d4a49b4c7d0cb8175f3a8d7da1db6eb2
GRC_ENCODER_ID
GRC_KICK_SLOT_IDX
init
MetalPluginName
AGXGRC:%s:%d:%s: *** Sampling has been started! Stop sampling before starting again.\n
Flag
TileTracing
AGXGRC:%s:%d:%s: *** Invalid ring buffer index (%u >= %u)!\n
_41dde4b7f68a419b892403f92ecfb6179bc7f5e8c0d2f8ec201cf613a51aad7b
AGXGRC:%s:%d:%s: *** Counter width must be 16, 32, 48, or 64!\n
AGXGRC:%s:%d:%s: *** \"perfCtrSamplerGetSourceInfo(sourceIdx, &sourceInfo, _sharedConnection) == KERN_SUCCESS\"\n
AGXGRC:%s:%d:%s: *** \"buildMasterCounterListInitialize()\"\n
DisablePowerOff
ConstantAGX_ContTimeOffset
CLKickEnd
AGXGRC:%s:%d:%s: *** Error, invalid uscIndex (%u >= %u) and/or invalid regIndex (%u >= %u)!\n
virtual void AGXGPURawCounterImpl::resetOptions()
_fd5e6c1358c75438997a6208a6b4c80da83c842b2fec01f9285fdb17fb90892b
AGXGRC:%s:%d:%s: *** \"(allocator.free() == 0) && (perfCtrIdx == _masterCounterNum)\"\n
AGXGRC:%s:%d:%s: *** Potential intermediate buffer overflow! (bufferSize=%llu processedPayloadSizeMax=%llu)\n
_409630cc8c0633fd91c2d5fc75ffdd7d3c03db35708db418f3fbf05de3837b8d
_6f0b8306b3affa8811a757f59930d14d4930c20366529e0f3b6c9dbd6fbf4187
_37ad0f11cd72f11f7231ef2ca1abbfe5cbb8778b066caef785d9abdedd8c2a1c
3DKickStart
_79c953a4355465c6a6896b013bf07e65640bbbcf9d23a7d82c605854edc1235a
_e8adcee7789c7ed8a980ad6fde70f13fbb9208d058f345c22abdcc3421f1abeb
Unknown
SingleVDMChannel
_5138e61a5671dfe21ce6fb23375a4bfe3f7c31a458aa73a1c58c7e462b7c0e12
GRC_SOURCE_ID
ConstantAGX_AbsTimeOffset
_de3119bbf56354f00749bda840e173d2f2722fc27892b1ebe5f39ca910a6319c
_ea99c3486cd23daa411aa60fb0dd550765c751554582d1fe64c8cd6e69c7cedd
CountPeriod
AGXMetalPerfCountersExternal
AGXGRC:%s:%d:%s: *** \"(cfShaderProfilerCounterName = CFStringCreateWithCString(kCFAllocatorDefault, shaderProfilerCounterName, kCFStringEncodingUTF8)) != NULL\"\n
AGXGRC:%s:%d:%s: *** Fail to find dispatch table for gpuGen=%u sourceName=%s\n
_6b86beb0b607a088bbe85d513c34a951d77dede2274848976f92f7bf9e330e78
USCNumPerMGPU
_07333ef72907406cb2f95790f76ac94a0d00fe89ff7b2c56ff9a805f016ca075
AGXGRC:%s:%d:%s: *** Insufficient space to add HW counter (%s)!\n
AGXGRC:%s:%d:%s: *** Invalid ring buffer count (%u)!\n
AGXGRC:%s:%d:%s: *** \"info != NULL\"\n
_47c0a6541bdf42ec524ec8853919cfef79ab706fd26d965dc1999c0d396bb1be
virtual bool AGXGPURawCounterImpl::setOptions(NSDictionary *__strong)
DisableMCH
addCounter
AGXGRC:%s:%d:%s: *** Metadata (%s) counter must be added before any other counters!\n
AGXGRC:%s:%d:%s: *** Unknown meta counter type!\n
DeviceAPSEventSelects
_7e8cf89ef1c67f9c5171db8c788a0f4ab7c36542ae5719055fae29eccc0f983c
CLKickStartTimestamp
_50f88f730c15d9a093469c70c841e09e6265b6801763222309875e6c50f06f2f
_1f7cdb637dd7a473552ff64b34d93f5a7a448d3cd0f5d1ef361701edd4418268
GRC_GPU_CYCLES
GRC_TIMESTAMP
Encoder ID. Valid only for kick boundary sample. ** MUST be added BEFORE any HW counter **
USCMaskForMGPU
_5e5deb98eafc93cac0bf82a1f53618a96d02bb08036905c33025010de1346d9e
num_cores
AGXGRC:%s:%d:%s: *** \"sourceCounterIdxList[i] != NULL\"\n
_fa573e6a7258a84f4ffa5f9e8442e7fb660db0745b89a17596b513c0842f94f0
AGXGRC:%s:%d:%s: *** \"buildMasterCounterListFinalize()\"\n
Q
_6ba0d19594024e68c928f09181d5fd35e1cc121d19356b9080de41ab538c067c
generateKickTimestampSamples
_423ccc54aeb6a01f9abb7b533d6542a7d502c505be6e14c69056cc6886c4d1b5
_253e1db24915155d74238748432abbb4bc4fa7a163a40ae1aac6028f3f2bc5aa
AGXGRC:%s:%d:%s: *** \"(cfIndex != NULL) || (cfFreeNum != NULL) || (cfSourceMask != NULL)\"\n
AGXGRC:%s:%d:%s: *** Amount of data to be drained must be aligned to 64-bits!\n
emitKickTimestampSamples
AGXGRC:%s:%d:%s: *** \"((cfContTimeOffset = (CFNumberRef)IORegistryEntryCreateCFProperty(_acceleratorPort, CFSTR(\"ContTimeOffset\"), NULL, 0)) != NULL) && CFNumberGetValue(cfContTimeOffset, kCFNumberSInt64Type, (void*)(&_samplingState.cont
AGXGRC:%s:%d:%s: *** \"CFNumberGetValue (cfIndex, kCFNumberSInt32Type, &index) && (index < _partitionInfoNum) && ((cfName == NULL) || CFStringGetCString(cfName, _partitionInfoList[index].name, sizeof(_partitionInfoList[index].name), kCFStri
_b95b869f2bde26f7d42a8a8b04f3da987a9d1eb3e97ab1c3416178ba5e7a781e
_9df17482eba01fddc5cab1f4ed417176f667cdf82c60b0272eb9fb58735ceae5
reserve
AGXGRC:%s:%d:%s: *** dstSize/Read/Write is not aligned to 64-bits!\n
AGXGRC:%s:%d:%s: *** \"(cfDict = cfDictionaryCreateFromPlist([plistPath UTF8String])) != NULL\"\n
startSampling
_40a8402511beee36c39c57f6ad9106d3d8a8094460bbb71542189713e7abccd6
Virtual counter to read shader profiler trace buffer from USC 00
v12@?0i8
ConstantAGX_CoreConfig
AGXGRC:%s:%d:%s: *** \"ret && (perfCtrIdx != 0) && (sourceMaskAll != 0)\"\n
GRC_SAMPLE_TYPE
AGXGRC:%s:%d:%s: *** \"(counterDesc.name != NULL) && (counterDesc.description != NULL)\"\n
EmitThreadControlFlow
AGXGRC:%s:%d:%s: *** srcRead and/or dstWrite is out of bound! (*srcRead=%llu size=%llu *dstWrite=%llu size=%llu\n
DeviceCounters
_862d2287f75264ad8adf0616274d8a4fae99561b8249e8009d2bb262fe83b541
CliqueSubSampling
Firmware
_ab6eee28a62c00458af472ce12c89a6aa9452a5ea38c60a97e5b001174a94bef
GRC_KICK_TRACE_ID
AGXGRC:%s:%d:%s: *** \"chipDispatchTable != nullptr\"\n
TAKickStart
3DKickEnd
_ee3137bdbfdd823234a27887d21e8139caa25dd4ea68729e6af860153dab347b
_ae63c64c395f57bf4c8024c925bf02c4b62aa454dfc05e6eab5c21e696b09b72
_0b7b594c8a7442a9c7452c1e19c37d770416fb5212b076c70295fc3eb66ccd33
_1a495313b093a9b9a3a85d65b581f67038040358a9fc438383d2f0405996ad27
AGXGRC:%s:%d:%s: !!! AGXGPURawCounterImpl is not initialized!\n
_29200ede6afa548bfa44e711dd5dd65dab8250ae951a54f97abeaa39330837e7
ESLInstTracing
LockGPUPerfState
AGXGRC:%s:%d:%s: *** Counter width must be <= 32 as \"%s\" has only 32 valid bits\n
Period
ShaderProfiler
AGXGRC:%s:%d:%s: *** \"perfCtrSamplerGetSourceNum(&_sourceNum, _sharedConnection) == KERN_SUCCESS\"\n
Periodic
_f0397395ae329f9745436d1ee9609a77c7459a030940abc0696e2d46d5b1fc88
_3efc67512480e33e1cea7bc73a6af91b7e77b81afa6141b49b139fc20065a3bc
_c05b2a6dde69210102d49e20cde2e953315d5888e81693b21ad7a9361a8666fd
drain
AGXGRC:%s:%d:%s: *** HW counter (%s) must be added before any shader profiler counters!\n
AGXGRC:%s:%d:%s: *** parseSampleHeader() is not set!\n
AGXGRC:%s:%d:%s: *** chip dispatch table is not propertly set!\n
AGXMetalPerfCounters
AGXGRC:%s:%d:%s: *** Inconsistent sub-buffer count! (%u != %u)\n
_d9579ad535e5486a3450aaec05e6179058989a17397e6b15b084e2d8a8b70d25
_5a1f8d3ba0b91ec6b67e24aa2ab2abea87d3848e91d4405fbb61727fc169e566
virtual uint32_t AGXGPURawCounterImpl::flags() const
virtual uint32_t AGXGPURawCounterImpl::gpuPerfState() const
AGXGRC:%s:%d:%s: *** \"((cfPartitionInfoList = (CFArrayRef)IORegistryEntryCreateCFProperty(_acceleratorPort, CFSTR(\"PerfCtrPartitionInfoList\"), NULL, 0)) != NULL) && ((_partitionInfoNum = (uint32_t)CFArrayGetCount(cfPartitionInfoList)) !=
source_mask
_b4777f6aaa86ad079be670de60aa97c86b8c186d0796de50a23cd48ffb06d7de
_9cf54ddc043a729ff51f60c2fc48bd10db8e4ab128dd450670cc6c21c4264f6d
AGXGRC:%s:%d:%s: *** Insufficient space to add metadata counter (%s)!\n
AGXGRC:%s:%d:%s: *** \"plistPath != nil\"\n
CLKickStart
Number of GPU cycles elapsed since previous HW sample. ** MUST be added BEFORE any HW counter **
CliqueTraceLevel
AGXGRC:%s:%d:%s: *** Ring buffers have not been allocated. Was sampling ever started on source %s?\n
AGXGRC:%s:%d:%s: *** \"(_sourceList[sourceIdx] = chipDispatchTable->createSource( this, sourceIdx, &sourceInfo, sourceCounterIdxList[sourceIdx], sourceCounterIdxNum [sourceIdx], chipDispatchTable)) != nullptr\"\n
calcBufferSizeWithRingBufferSize
TAKickStartTimestamp
_45f483f7528b9fff50ebdd89c76151b1155dc002041194901ad251f69b400db8
Description
AGXGRC:%s:%d:%s: *** \"(counterDesc.nameLen >= 2) && (counterDesc.descriptionLen >= 2)\"\n
CliqueAdvanceReason
RingBufferSizeInKB
AGXGRC:%s:%d:%s: *** Unexpected number of kickslot data to be added to the queue!\n
AGXGRC:%s:%d:%s: *** \"((cfCoreConfig = createInternalCoreConfigDict(_sharedConnection)) != NULL) && ((cfCoreNum = (CFNumberRef)CFDictionaryGetValue(cfCoreConfig, CFSTR(\"num_cores\"))) != NULL) && CFNumberGetValue(cfCoreNum, kCFNumberSInt3
index
_27a61a5598c57b0e20af16809e44f0b13885d1ce4a7a064ed3402b61513037e9
PulsePeriod
ProfileControl
AGXGRC:%s:%d:%s: *** \"(_sharedConnection = IOGPUDeviceGetConnect(_deviceRef)) != 0\"\n
AGXGRC:%s:%d:%s: *** \"CFNumberGetValue(cfEventSelectsNumMax, kCFNumberSInt32Type, &eventSelectsNumMax)\"\n
RDE
ReduceCDMCluster
virtual bool AGXGPURawCounterImpl::stopSampling()
Kick slot index. Valid only for kick boundary sample. ** MUST be added BEFORE any HW counter **
alignBufferSize
_98496d1b8b35ed09f94d2c931fcfac95be3b9fc8c933e02acc9d2236422febd8
ringBuffer
AGXGRC:%s:%d:%s: *** Source sample size is unexpectedly larger than the maximum! (%llu > %u)\n
plist
ConstantAGX_PostProcessBufferAddrAlignment
TAKickEndTimestamp
_7c45575717b419225ea4088604b706bc8b2f79307539b6bcc431041f350ef736
_cea4110b16912871341d3db3aeeee2807a8388b85ce1623435d1107b4c854b96
AGXGPURawCounterImpl.mm
ConstantAGX_SampleTypeList
@\"NSNumber\"16@?0@\"NSString\"8
MinTraced
i24@?0r^v8r^v16
AGXGRC:%s:%d:%s: *** Inconsistent ring buffer count for source[%u]. (%u != %u)\n
AGXGRC:%s:%d:%s: *** \"_sourceList[sourceIdx] == nullptr\"\n
ConstantAGX_PostProcessBufferSizeAlignment
_49917e2aa4c9d63ecdb76572f7c5d143190565be42b4a6ddee0b586369c6fc71
_3a2c07090e4a9514e2186ae5ea625797e5115783c813092a5d6841bdcc9c0ff6
_eca0a9e48247bc97aeafcffd971cde3d8f7b2b02a6e240f54cc444590d0c8438
_adff2119b0a5e2ea9199225523fe534f2b05442d9623a62d6a7bc95039b4d30a
_f85269f93d315727998ef5425c9b7d5087d36ef299e4a33040a44dafe6eebe51
USCConfigOverride
```
