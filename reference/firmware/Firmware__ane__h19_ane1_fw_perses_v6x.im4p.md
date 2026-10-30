# `Firmware/ane/h19_ane1_fw_perses_v6x.im4p`

- File size: 1,556,505 bytes
- IM4P: Tag: IM4P  Type: ane1  Version: 1
- BuildManifest components that use it: `Ap,ANE1`, `Ap,RestoreANE1`

## IM4P header [FW]

```
IM4P (Payload):
  Tag:          IM4P
  Type:         ane1
  Version:      1
  Data:         1.6 MB (1556480 bytes)
```

## Payload [FW]

- Size after IM4P unwrap / decompression: 1,556,480 bytes
- Format: Mach-O 64-bit

## Identity strings (versions, build tags) [FW]

- `(%s@%s) RTKit Version: %u.%u.%u`
- `RTKSTACKRTKit_armv8_chinook_Oz_flto_pac-3514.40.18.release`
- `RTKit: %s - Client: %s`

## Strings (2,592) [FW]

Printable runs of 6+ characters with at least three letters, in file order, with payload offset. For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that describe what the processor does.

```
00000028  __TEXT
00000068  __text
00000078  __TEXT
000000b8  __const
000000c8  __TEXT
00000108  __cstring
00000118  __TEXT
00000158  ce_env
00000168  __TEXT
000001a8  __constructor
000001b8  __TEXT
000001f8  __init_offsets
00000208  __TEXT
00000248  text_env
00000258  __TEXT
000002a0  __DATA
000002e0  __const
000002f0  __DATA
00000330  _rtk_heap
00000340  __DATA
00000380  __data
00000390  __DATA
000003d0  _rtk_power
000003e0  __DATA
00000420  _rtk_patchbay
00000430  __DATA
00000470  _rtk_init_stack
00000480  __DATA
000004c0  _rtk_irq_stack
000004d0  __DATA
00000510  _rtk_exc_stack
00000520  __DATA
00000560  _rtk_tunables
00000570  __DATA
000005b0  _rtk_boot
000005c0  __DATA
00000600  _rtk_page_tables__DATA
00000650  _rtk_threads
00000660  __DATA
000006a0  _fwinfo
000006b0  __DATA
000006f0  __data_copy
00000700  __DATA
00000740  __sysvars
00000750  __DATA
00000790  _rtk_boot_l1
000007a0  __DATA
000007e0  __chain_starts
000007f0  __DATA
00000830  _rtk_mtab
00000840  __DATA
00000880  __mod_init_func
00000890  __DATA
000008d0  __gxf_data
000008e0  __DATA
00000920  __zerofill
00000930  __DATA
00000978  __DATA_CONST
00004951  wwwwwww
0000bdd6  F9avN0
0000c5d8  @=NpI>N
0000fbe7  Thr@9H
0000fcdf  Thr@9(
00010341  |Lpib@
00010374  @{Lpkv@
000103ad  yLpkz@
000103e5  wLpk~@
000108fd  RLPi^@
00010944  `RLpiB@
00013af6  JpCNKP
00013ed2  Jpc/KP
00014d3d  fJP!QJp
00014e71  GJp$oK
00014f7c  A?JpcSJ0
0001570a  Jpc5Jp
000198d3  TU]HpP
00019a33  T`THPP
0001fc7a  E0#BEP
000201e0  @|EPi.@
000201f8   |EPi6@
00020229  {EPiv@
0002027c  `{Epi2@
00021ec8  (aQyKeQy
000221ac  (aQyKeQy
000224a8  (aQyKeQy
000227b3  rhbQy9
00026ca9  OBpZ3B
00037631  w;pct9P
000397b1  k:pch8P
00039bd5  J:pCG8P
0003b7d5  j9pCg7P
0003b991  \9pcY7P
000434be  4PAM60
0004b652  3pcs/P
0004b872  2pcb/P
0004ba92  2pcQ/P
0004bbf2  2pcF/P
0004cd2a  0PAO2p
0004cd86  0PaL2p
0004eaa6  @ysc1p
0004fc92  0pcA-P
00050096  @yBL1p
000516f2  0pcn,P
00051896  /pCa,P
00051c52  /pcC,P
00061776  *pCj$P
00061bd4  !e*pCG$P
000847cf  TBis8pys
000a4210  UNKNOWN ID
000a80a8  Copyright (c) APPLE Inc. All Rights Reserved.
000a80da  release
000a80e2  Oct  7 2026
000a8108  iPhone OS
000a8117  clang/clang++
000a8b38  RTKSTACKRTKit_armv8_chinook_Oz_flto_pac-3514.40.18.release
000a8b98  cold boot counter: %u
000a8bb8  Initial Heap: Total size: %ld bytes used: %ld bytes
000a8bed  Current Extra Heap: Total size: %ld bytes used: %ld bytes
000a8c28  !OVERFLOW!
000a8c33  BUF_H2T
000a8c3b  BUF_T2H
000a8c43  ChManTarget
000a8c4f  ChManHost
000a8c59    token semaphore = %#08x
000a8c7a  RealChannelTableTarget.cpp
000a8c9a  ISRManager
000a8ca5  IPIManager
000a8cb0  RTOSTimer
000a8cba  GPTimer0
000a8cc3  CPlatformEnvironment.cpp
000a8cdc  This is my first UART test, ShMem %p with size 0x%zx
000a8d12  SHAREDMALLOC
000a8d22  DATA_CHAIN_H2T
000a8d38  SharedMemoryHost
000a8d49  SharedMemoryManager
000a8d5d  DEBUG AGENT
000a8d69  TERMINAL
000a8d72  IPSynchro
000a8d7c  FSMMan
000a8d83  (%s@%s) RTKit Version: %u.%u.%u
000a8da4  Oct  7 2026
000a8db9  rtbuddyFW: %s
000a8dd3  VM mode: %s
000a8de0  dynamic
000a8de8  enabled
000a8df0  disabled
000a8df9  mmu logger : %s
000a8e0a  CE script location %p
000a8e21  perses
000a8e28  System Thread
000a8e36    base address = %p
000a8e4b  management
000a8e56  crashlog
000a8e65  ane_to_ane
000a8e70  ane_to_isp
000a8e7b  sys_clock_when_coredump=%llu 
000a8e9d  Exception:  NMI
000a8eb2  Exception:  IRQ
000a8ec7  Exception:  FIQ
000a8edc  Exception:
000a8ee9  Thread (%s)
000a8ef6  Interrupt Context
000a8f09  CPU = %d
000a8f15  Call stack:
000a8f22    0x%08llX
000a8f30  Registers:
000a8f3c    pc    0x%016llX  psr   0x%016llX
000a8f60    far   0x%016llX  esr   0x%016llX
000a8f85    x0    0x%016llX  x1    0x%016llX
000a8fa9    x2    0x%016llX  x3    0x%016llX
000a8fcd    x4    0x%016llX  x5    0x%016llX
000a8ff1    x6    0x%016llX  x7    0x%016llX
000a9015    x8    0x%016llX  x9    0x%016llX
000a9039    x10   0x%016llX  x11   0x%016llX
000a905d    x12   0x%016llX  x13   0x%016llX
000a9081    x14   0x%016llX  x15   0x%016llX
000a90a5    x16   0x%016llX  x17   0x%016llX
000a90c9    x18   0x%016llX  x19   0x%016llX
000a90ed    x20   0x%016llX  x21   0x%016llX
000a9111    x22   0x%016llX  x23   0x%016llX
000a9135    x24   0x%016llX  x25   0x%016llX
000a9159    x26   0x%016llX  x27   0x%016llX
000a917d    x28   0x%016llX  x29   0x%016llX
000a91a1    lr    0x%016llX  sp    0x%016llX
000a91c8  Register frame unavailable
000a91e4    L2C_ERR_STS  0x%016llX
000a91fe    L2C_ERR_ADR  0x%016llX
000a9218    L2C_ERR_INF  0x%016llX
000a9232  <null>
000a9240  BUFFER: child of %s
000a9255  BUFFER: no parent
000a9268    this = %p, debug level = %d
000a9287    retain = %d
000a9296    cached = %s
000a92a5    writeback = %s
000a92b7    invalidate = %s
000a92ca    data blocks = %zu
000a92df      block[%zu] = %p, size =%u, stride = %u, payload = %u
000a935a    total/max buffers = %d
000a9374    data cached = %s
000a9393    bundled blocks = %d
000a93aa      block[%d] size = %zu, alignment = %zu, stride = %zu
000a93e3    There is no block descriptor because this is a dummy buffer pool.
000a9428  ------------- Active Buffers -------------
000a9481  ./ffw/ffw/CAsyncBufferManager.cpp
000a94a3  CAsyncBufferManager buf %p invalid groupId -1
000a94d1  CAsyncBufferManager buf %p invalid indexOfGroup -1
000a9504  CAsyncBufferManager buf %p invalid mpGroups[%d][%d] buf %p, state %d 
000a954a    buffers internally allocated = %s
000a956f    buffers actually received = %d, available = %d, %s
000a95e6    Max channels = %d
000a95fb    Thread priority = %d
000a9613    Signal semaphore = %#x
000a962d    Die request semaphore = %#x
000a964c    Doorbell cadence = %d us
000a9679  [UNIDIRECTIONAL]
000a968a      IOP ch = %p, slots = %d, user_signal = %d
000a96b9      tx = %ld [out = %d]
000a96ea  CController.cpp
000a96fa    Thread = %#x, priority = %d
000a9719    Semaphores =
000a9730    Processed commands = %zu
000a974c    Processed signals = %zu
000a9767  ./ffw/ffw/CDMediaBusManager.cpp
000a9787  %s .Sanity check failure!
000a97a2  cmdBufLen < sizeof(sCDMediaBusManagerEndPointMsgHdr)
000a97d7  pCmdHdr->cmd >= CDMEDIABUSMANAGER_ENDPOINT_CMD_TOT
000a980a  cmdBufLen < sizeof(sCDMediaBusManagerEndPointPingCmd
000a983f  cmdBufLen < sizeof(sCDMediaBusManagerEndPointRemapCmd)
000a9876  cmdBufLen < sizeof(sCDMediaBusManagerEndPointSendBufMsgCmd)
000a98b2  IPC Endpoint cmd failed %d
000a98cd  IPC Endpoint cmd failure
000a98e6  hello DMBus ACK
000a98f7  CDMediaBusManager.cpp
000a990d  NULL != pItem->pBase
000a9922  ERROR: Remap out of space : handle 0x%x size 0x%lx
000a995e  ERROR: UnRemap out of space : handle 0x%x size 0x%lx
000a9994  pCmd->bufNbr > maxAneIpcBufMsg
000a99b3  pItem->refCount
000a99c3  ERROR: msg.bufAddr[%d] 0x%llx size 0x%llx
000a99ed  ERROR: pItem pBase 0x%llx memSize 0x%llx
000a9a16  ERROR: couldn't find shared buffer item
000a9a3f  ERROR: couldn't find SAP callback registered
000a9a6d  CDMediaBusManager Property Operation(%s): id %d 
000a9a9f  hello DMBus
000a9aac  No Endpoint is running to send the Ping Message
000a9add  pCmd->endPointId < maxEndpoint
000a9afc  ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_IDLE == endPointCb[pCmd->endPointId].curState
000a9b4e  false == ringBufferCfgDone[pCmd->endPointId]
000a9b7b  (0 != pCmd->readRingBufferAddr) && (0 != pCmd->readRingBufferLen)
000a9bbd  (0 != pCmd->writeRingBufferAddr) && (0 != pCmd->writeRingBufferLen)
000a9c01  ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_RUNNING == endPointCb[pCmd->endPointId].curState
000a9c56  true == ringBufferCfgDone[pCmd->endPointId]
000a9c82  EndPointUnset remap not by local %llu
000a9ca9  Run out of cmdDepth !!!
000a9cc2  Run out of CSharedMemory !!!
000a9ce0  Run out of Shared Mem Info !!!
000a9d00  pCmd->wired == pItem->bWired
000a9d1d  unremap WriteMessage failed
000a9d3a  Couldn't find ShareMemInfoItem to free !!!
000a9d66  Recieved a SendBufMsg command during idle state %d
000a9d9a  Couldn't find spare SapInfo !!!
000a9dbb  Couldn't find SapId %d registered !!!
000a9de2    total command acked = %d
000a9dfe    total command processed = %d
000a9e1e    total command failed = %d
000a9e3b  CDebugAgent.cpp
000a9e4b  %s: ROOT GET - Root handle : %p
000a9e6c  %s: ENV GET - Environment handle : %p
000a9e93  %s: OBJECT BY NAME - handle : %p, name %s
000a9ebe  %s: CMD = %x - No object with such name : %s
000a9eec  %s: CMD = %x - String name too long [> %d]
000a9f18  %s: CHILDREN TOT - handle : %p [%s], children %d
000a9f4a  %s: CMD = %x - Wrong component handle : %p
000a9f76  %s: CHILD BY INDEX - handle : %p [%s], child[%03d] %p [%s]
000a9fb2  %s:  CMD = %x - handle : %p [%s] - Wrong child index: %d > %d
000a9ff1  %s: GET DEBUG LEVEL - object: %p - level = %d
000aa020  %s: SET DEBUG LEVEL - object: %p - level = %d [before = %d]
000aa05d  %s: SET RECURSIVE DEBUG LEVEL - root: %p - level = %d
000aa094  FSM TOT = %d
000aa0a2  %s: FSM BY INDEX - FSM[%03d] %p [%s]
000aa0c8  %s:  CMD = %x - Wrong FSM index: %u > %zu
000aa0f3  %s: FSM BY NAME - handle : %p, name %s
000aa11b  %s: GET FSM DEBUG LEVEL - handle: %p [%s] - level = %d
000aa153  %s: SET DEBUG LEVEL - FSM: %p [%s] - level = %d [before = %d]
000aa192  %s: CMD = %x - Wrong FSM handle : %p
000aa1b8    Queues: Total: %zd, Available = %d
000aa1de    Mailboxes: Total: %zd, Available = %d
000aa207    Signals: Total: %zd, Available = %d
000aa22e    Mutexes: Total: %zd, Available = %d
000aa255    Semaphores: Total: %zd, Available = %d
000aa27f    Signals: Total: %d, Available = %d
000aa2a5  Unit Test Status:
000aa2b8   Complete: %s
000aa2ce   Passes: %4d
000aa2dc   Fails:  %4d
000aa2ea   Time Elapsed (ms): %d
000aa302  %s: SPECIAL FN - object: %p - return = %llX 
000aa330  %s: S2R FLAG - return : 0x%lx 0x%x
000aa36a  MMUManager
000aa375  %s-ane%d
000aa37e    Restart count : %d
000aa394    Platform : mode = %s, ID = %#08x, HW = %08x.%08x
000aa3cd  TARGET
000aa3d4    Arch: arm64e
000aa3e4    System Clock : %zu Hz
000aa3fd    Data Cache Line Size: %u [%#x]
000aa41f    Instruction Cache Line Size: %u 
000aa443    MMU Page Size: %zu bytes
000aa45f    Boot arguments entries : %zu
000aa4c6    Main memory :   base : %p
000aa4e3                    size : %zu [%#08zx] [%zu.%zu MB]
000aa517    Extra heap :    base : %p
000aa534    Shared memory : base : %p 
000aa552                    size : %zu [%#08lx] [%zu.%zu MB]
000aa586    TEXT : %zu [%#zx] - text %zu, cstring  %zu, const %zu
000aa5bf    DATA : %zu [%#zx] - data %zu, bss %zu, common %zu
000aa5f4    Initial heap free space : %zu [%#08zx]
000aa61e    Initial heap allocated space : %zu [%#08zx]
000aa64d    Current extra heap free space : %zu [%#08zx]
000aa67d    Current extra heap allocated space : %zu [%#08zx]
000aa6b2    Disclaimer : %s
000aa6c5    Application : %s [%s]
000aa6de    Linked on : %s - %s
000aa6f5    Release : %s
000aa705    Device : %s
000aa714    Sideloaded : %s
000aa732    Commit Hash : %s
000aa746    Tool-chain : %s - %s [%s]
000aa763    AneIpcVersion : Major 0x%x, Minor 0x%x
000aa795  CEnvironment.cpp
000aa7a6  MailboxPool
000aa7b2  QueuePool
000aa7bc  ResourcePool
000aa7c9  SemaphorePool
000aa7d7  SignalPool
000aa7e2  TaskPool
000aa7eb  TimerPool
000aa7fb  Preparing coredump
000aa80f  Waiting for coredump %d
000aa828  CExpandablePool.cpp
000aa83c  ./ffw/ffw/CFSM.cpp
000aa84f  The  [%d, %s] is duplicated.
000aa86c  The  [%d, %s] -> [%d, %s] transition is duplicated.
000aa8a0  The transition's destination [%d, %s] -> [%d, %s] is invalid.
000aa8de  Invalid entry type [%d].
000aa8f7    [%03d] %p - %s - state: %s
000aa915  %s: STATUS EXITING FAILED (%d, %s): [%d, %s]->[%d, %s]
000aa94c  %s: ACTION FAILED (%d, %s): [%d, %s]->[%d, %s]
000aa97b  %s: STATUS ENTERING FAILED (%d, %s): [%d, %s]->[%d, %s]
000aa9b3    GPIO registers = %zu
000aa9cb  ./ffw/ffw/CIndexPool.cpp
000aa9e4  Invalid Index
000aa9f2  index exceed the entries range : %zu %zu
000aaa1b    Depth(%zu) NodeBuf(0x%08x) wr(%u) rd(%u) rdCnt(%u) wrCnt(%u) errCode(0x%x) 
000aaa6b  [31m">>>>>>> Tasks sending cmd to CIOObject %s task1 name %s task2 name %s"
000aaabd    Command Mailbox semaphore = %#04x [%s]
000aaae7    Command reply semaphore = %#04x [%s]
000aab0f    Semaphores
000aab2d    Started = %s
000aab3d    Commands issued = %zu, processed = %zu %s
000aab6a  [currently processing one]
000aab9a    Processed messages = %zu
000aabb6    Processed buffers = %zu
000aabd1    Processed data messages = %zu
000aabf2    Processed in-line commands = %zu
000aac16    Dropped messages = %zu
000aac30    Dropped buffers = %zu
000aac49    Delivered Messages = %zu
000aac65    inputs = %zu, max = %zu
000aac80      pin [%02d] - pipe = %p (%s)
000aaca1    outputs = %zu, max = %zu
000aacbd    buffer pools = %zu, max = %zu
000aacde      pin [%02d] - pool = %p (%s)
000aacff  ./ffw/ffw/CIOObject.cpp
000aad17  name %s got empty cmd %lld/%lld from cmdMbox 0x%x
000aad49  ./ffw/ffw/CIOPRingBuffer.cpp
000aad66  ((IOP_RINGBUFFER_VERSION_V2 == (pBuf->_header._version>>16)) || (IOP_RINGBUFFER_VERSION == (pBuf->_header._version>>16))) && ((pBuf->_header._wrptr < dataBufSize) && (pBuf->_header._rdptr < dataBufSize)) && ((pBuf->_header._size == dataBufS
000aae5c  ((IOP_RINGBUFFER_VERSION == (pBuf->_header._version>>16)) || (IOP_RINGBUFFER_VERSION_V2 == (pBuf->_header._version>>16))) && ((pBuf->_header._wrptr < dataBufSize) && (pBuf->_header._rdptr < dataBufSize)) && ((pBuf->_header._size == dataBufS
000aaf52  IOP racing
000aaf5d  pBuf->_header._rdptr + GET_CACHE_LINE_ALGIN_SIZE(sizeof(sIOPRingBufferMsgHeader_t) + payloadSize) <= localCopyWrPtr
000aafd1  pBuf->_header._rdptr + GET_CACHE_LINE_ALGIN_SIZE(sizeof(sIOPRingBufferMsgHeaderV2_t) + payloadSize) <= localCopyWrPtr
000ab047  rdptr + GET_CACHE_LINE_ALGIN_SIZE(sizeof(sIOPRingBufferMsgHeader_t) + payloadSize) <= localCopyWrPtr
000ab0ac  rdptr + GET_CACHE_LINE_ALGIN_SIZE(sizeof(sIOPRingBufferMsgHeaderV2_t) + payloadSize) <= localCopyWrPtr
000ab113  IOP Ring buffer skip item with larger size
000ab13e  pBuffer is %p
000ab14d  bufLen is %lu
000ab15c  reader is %d
000ab16a  peerNotifier is %p
000ab17e  newMsgSema is %lu
000ab191  isrHandle is %d
000ab1a2  isrNbr is %d
000ab1b0  regAddr is 0x%lx regValue is 0x%x
000ab1d3  count (0x%x 0x%x 0x%x)
000ab1eb  TC %p int (0x%x 0x%x 0x%llu)
000ab209  Read IOP_RINGBUFFER_VERSION is 0x%x
000ab22e  Read rdptr is 0x%x and wrptr is 0x%x
000ab254    Interrupts enabled: %s
000ab275    IRQs lines = %d
000ab288    Line %d IRQs = %zu
000ab29e      [%02d][%02d] count = %zu - registered callbacks = %zu
000ab2d9    semaphore = %#08x
000ab2ee  [%zu:%lld]
000ab2f9  [%zu:%lld]%s
000ab32c  CLoggerInterProcessor.cpp
000ab346  CMultiFilter.cpp
000ab357  %s [ch %zu]: ChannelStop timed out!
000ab37b    IN Channels = %zu
000ab390      Max ports = %zu
000ab3a5      Max inputs = %zu
000ab3bb    OUT Channels = %zu
000ab3d1      Max outputs = %zu
000ab3e8      Max buffer pools = %zu
000ab404  %s ERROR %p 0x%lx, 0x%lx, ret 0x%x, uncached
000ab432  WireSharedInternal
000ab445  %s ERROR %p 0x%lx, 0x%lx, ret 0x%x, cached
000ab471  sts 0x%x %p, 0x%lx
000ab485  CMMU.cpp
000ab48e  %s ERROR %p 0x%lx, 0x%lx
000ab4a8  WireUncached
000ab4b5  rc: %d, physicalAddr: 0x%lx, length: %zu, flag: 0x%zx
000ab4ec  Entry %zu: start: 0x%lx, length: %zu, refcount: %zu, parent: %zu
000ab534  UNWIRED
000ab53c  F_WIRING
000ab545  F_UNWIRING
000ab550    Buffers operations = %zu
000ab56c        Wired: successful = %zu, failed = %zu
000ab599      UnWired: successful = %zu, failed = %zu
000ab5c6    LOG: Last %zu operations [total = %zu]:
000ab5f1  [%4zu]:[%4zu] %10s: vir=%p, phy=%p, len=%#08x[%zu]
000ab652    LOG: There no wiring/unwiring operations
000ab67e    Wiring history index = %d
000ab69b  [%3d]: %10s: vir=%p, len=%zu, poolId=%d
000ab6c4                     thread=%s, %s:%d
000ab6e9  rc: %d, virtualAddr: 0x%p, length: %zu, flag: 0x%zx
000ab71e  Entry %zu: start: %p, length: %zu, refcount: %zu, parent: %zu
000ab761    Wiring history index = %d
000ab789  OBJECT: %s child of %s
000ab7a1  OBJECT: %s
000ab7ad    this = %p, children = %d, debug level = %d
000ab7e9    pool messages = %d
000ab7ff    downstream filter = %p [%s]
000ab81e  <NONE>
000ab825    Semaphores %#04x [%s]
000ab83e    messages:
000ab84b      posted = %zu
000ab85d      exchanged = %zu
000ab872      in-use = %zu, watermark = %zu
000ab895      free = %zu
000ab8a5    buffer ref messages:
000ab8c2    free = %dzun
000ab8d2  Not occurred, cannot say anything about waiting
000ab902  Occurred, cannot say anything about waiting
000ab92e  [SMALL_SM_ALLOC] marker=%c%c%c%c size=%5lu=(%5lu) caller=%s:%d
000ab96e    Total number of successful allocations = %zu
000ab99e    Number of outstanding allocations = %zu
000ab9c9    pool = %d
000ab9d6    in-use = %zu, watermark = %zu
000ab9f7    free = %zu
000aba05    exchanged = %zu
000aba18  TASKTERMINATOR
000aba2b  IDLETASK
000aba34  RUNNABLE
000aba3d  SUSPENDED
000aba47  WAITING
000aba4f  SEMWAIT
000aba57  BLOCKED
000aba5f            Task       Pri     State         Stack Base        Size          Name
000abadf    in-use = %d, watermark = %d
000abafe    free = %d
000abb0b    exchanged = %d
000abb1d  ERROR: Requested thread priority %d
000abb42    Profiling: start #%d (%#x) end #%d (%#x)
000abb6e  EVT#%d: %s @ %#x, (%f), diff: %d us, delta: %d us
000abba1    [handle = %lu]
000abbb3    started = %s
000abbc3  YES [indefinite]
000abbd4    started = YES [%ld to go]
000abbf1    call-back = %p
000abc03    started = NO
000abc13    max period [ns] = %ld
000abc2c    min period [ns] = %ld
000abc45  host_shared_memory
000abc5e  ./ffw/ffw/rtkit/ffwMMU.cpp
000abc79  Wiring is currently disabled for mem type %d
000abca7  RTK_mmu_map(): status: 0x%x.
000abcc5  UnWiring is currently disabled for mem type %d
000abcfb  ./ffw/ffw/rtkit/CMMUDynamic.cpp
000abd1b  Old %s %p
000abd26  UnwireShared
000abd33  CMMUDynamic.cpp
000abd43  MMUdynamic logger %p
000abd59  CANEController.cpp
000abd6c  ASSERT: 
000abd75  ./sne/controller/target/CANEController.cpp
000abda0  cmdLog != 0
000abdac  signalArray != 0
000abdbd  chDescr != 0
000abdce  fsm != 0
000abddd  chDescr[i].fsm != 0
000abdf1  signalAvail == true
000abe05  chDescr[i].notificationSema != (SEMA)0
000abe2c  NotifCh
000abe34  TimeProfiler
000abe41  RPCDaemon
000abe4b  __null != pPowerControlService
000abe6a  rpcWaitSem != (SEMA)0
000abe80  AneEngine
000abe8a  pAneExe
000abe92  __null != pProgManager
000abea9  AneCallManager
000abeb8  SneDMBusManager
000abec8  ANETraceBuffer
000abed7  DebugUtil
000abee1  DbgEventsManager
000abef2  AneServer
000abefc  LoadMonitor
000abf08  CANEController() done
000abf1f  ((pMsg)->hdr.data0 & 0xFF000000) == 0x01000000
000abf4e  pNotificationMsg->id < NOTIFICATION_TOT
000abf78  pServer
000abf80  AneProfiler
000abf8c  Ring GPU doorbell succeed.
000abfa8  Chip don't supported.
000abfbf  Ring GPU doorbell failed.
000abfda  Unknown property
000abfeb  [%s] CMD = %#04x [%s] at %lld
000ac00a  insize == sizeof(struct sCSneCmdPowerSupplyControl)
000ac03e  *outsize >= sizeof(struct sCSneCmdPowerSupplyControl)
000ac074  [%s]  CMD = %#04x [%s] at %lld : Device Power=0x%x
000ac0a8  insize == sizeof(struct sCSneCmdTraceEnable)
000ac0d5  *outsize >= sizeof(struct sCSneCmdTraceEnable)
000ac104  [%s] CMD = %#04x [%s] at %lld : flags 0x%x
000ac130  insize == sizeof(struct sCSneCmdConfigGet)
000ac15b  *outsize >= sizeof(struct sCSneCmdConfigGet)
000ac188  insize == sizeof(struct sCSneCmdPlatformInfo)
000ac1b6  *outsize >= sizeof(struct sCSneCmdPlatformInfo)
000ac1e6   PlatForm ID = %#08x, rev %04x
000ac206  resource_info_get: maxProgram=%d, maxProcess=%d, maxProcPerProg=%d, maxCallPerProcess=%d, maxRequestPerPriority=%d
000ac27a  [%s] CMD = %#04x [%s] at %lld : dsid=%d
000ac2a3  !isProgramLoaded
000ac2b4  [%s] CMD = %#04x [%s], nbrOfSettings=%llu at %lld
000ac2e7  regId: %d, value 0x%x
000ac2fe  stats_buffer[%d]: %d dram %d validCount %d logEvents %llu statEvents %llu
000ac349  *outsize >= sizeof(struct sCSneCmdStatsBufferSizeV0)
000ac37e  *outsize >= sizeof(struct sCSneCmdStatsBufferSize)
000ac3b1  Invalid command size CSNE_CMD_STATS_BUFFER_SIZE_GET %llu
000ac3ea  pCmd->eventTableAddress != 0
000ac407  pCmd->eventTableSize > 0
000ac420  pCmd->numOfTarget > 0
000ac436  insize == sizeof(struct sCSneCmdReset)
000ac45d  CSNE_CMD_START
000ac46c  START PROCESSED
000ac47c  insize == sizeof (struct sCSneCmdCpuLoadGet)
000ac4a9  insize == sizeof (struct sCSneCmdSuspend)
000ac4d3  insize == sizeof(struct sCSneCmdPowerDown)
000ac4fe  insize == sizeof(struct sCSneCmdTimeProfileStart)
000ac530  insize == sizeof(struct sCSneCmdTimeProfileStop)
000ac561  insize == sizeof(struct sCSneCmdTimeProfileShow)
000ac592  PMU base is 0x%x
000ac5a4  __null != pPC
000ac5b2  PMU base is 0x%llx
000ac5c6  [%s]  CMD = %#04x [%s] at %lld : MODE = 0x%x 
000ac5f5  [%s]  CMD = %#04x [%s] at %lld :
000ac617  expected version major=0x%x, minor=0x%x
000ac640  real version major=0x%x, size=0x%x
000ac664  pCmd->expected_ver.major == 0x0003
000ac687  Warning: ANE program interface minor version mismatch between driver (0x%x) and firmware (0x%x)
000ac6e8  [%s] CMD = %#04x [%s] : Dummy return success
000ac716  [%s]  CMD = %#04x [%s] at %lld
000ac736  generic buf    = 0x%llx, size=0x%llx
000ac75c  kernel buf     = 0x%llx, size=0x%llx
000ac782  Descriptor buf = 0x%llx, size=0x%llx
000ac7a8  operation buf  = 0x%llx, size=0x%llx
000ac7ce  procedure buf  = 0x%llx, size=0x%llx
000ac7f4  kernelProp buf = 0x%llx, size=0x%llx
000ac81a  tdProp buf     = 0x%llx, size=0x%llx
000ac840  opDbg buf      = 0x%llx, size=0x%llx
000ac866  proc buf       = 0x%llx, size=0x%llx
000ac88c  [%s]  CMD = %#04x [%s] : ProgramId = %d
000ac8b5  program Id is invalid, load_program failed
000ac8e1  [%s] CMD = %#04x [%s] at %lld : ProgramId = %d
000ac919  [%s]  CMD = %#04x [%s] at %lld : ProgramId = %d
000ac94a  pCmd->programId != (0xFFFFFFFF)
000ac96a  create_process failed
000ac981  [%s]  CMD = %#04x [%s] at %lld : ProgramId = %d Process = %d 
000ac9c0  pCmd->programId != ECSneCmdId_Invalid
000ac9e6  [%s]  CMD = %#04x [PROC CALL] at %lld : ProgId=%d ProcId=%d Proc=%d Pri=%d
000aca33  Bufs = %d uuid = 0x%llx
000aca4c  buf[%ld]=0x%llx, size=0x%llx, type=%d
000aca73  (pCmd->priority >= 2)&&(pCmd->priority <= 7)
000acaa0  [%s]  CMD = %#04x [PROC CALL WITH BARS] at %lld : ProgId=%d ProcId=%d Proc=%d Pri=%d
000acaf6  bar[%d]: config=%d, type=%d, barId=%d, value=%lld
000acb29  pCmd->nbrOfCustomBars <= (122)
000acb48  [%s]  CMD = %#04x [PROC CALL WITH EVENTS] at %lld : ProgId=%d ProcId=%d Proc=%d Pri=%d
000acba0  signal events[%d]: eventType=%d, targetId=%d, idx=%lld, value=%lld
000acbe4  pCmd->nbrOfSignalEvents > 0 && pCmd->nbrOfSignalEvents <= (16)
000acc23  [%s]  CMD = %#04x [CR] at %lld : ProgramId = %d ProcessId = %d, Procedure = %d
000acc74  Bufs = %d Priority = %d
000acc8d  (pCmd->priority >= 0)&&(pCmd->priority <= 7)
000accba  cache request failed
000accd0  cache request success: cacheHandler = 0x%llx
000accfe  [%s]  CMD = %#04x [CR WITH CUSTOM BARS] at %lld : ProgramId = %d ProcessId = %d, Procedure = %d
000acd5f  [%s]  CMD = %#04x [CR WITH EVENTS] at %lld : ProgramId = %d ProcessId = %d, Procedure = %d
000acdbc  Bufs = %d Priority = %d CustomBars = %d WaitEvents = %d SignalEvents = %d
000ace07  wait events[%d]: eventType=%d, targetId=%d, idx=%lld, value=%lld
000ace49  pCmd->nbrOfWaitEvents + pCmd->nbrOfSignalEvents > 0
000ace7d  [%s]  CMD = %#04x [%s] at %lld : cacheHandler = 0x%llx
000aceb5  invalidate request failed
000aced0  [%s]  CMD = %#04x [%s] : forceDisable = 0x%x
000acf04  CSNE_CMD_FORCE_DISABLE_CACHE_REQUESTS only expects disable to be set to true
000acf51  pCmd->forceDisable == 1
000acf69  [%s]  CMD = %#04x [%s] at %lld : enable = %d
000acf97  [%s]  CMD = %#04x [%s] at %lld : property = 0x%x value = 0x%x
000acfd6  false == ipcEndpointSetDone
000acff2  true == AFPPLoaded
000ad005  [%s]  CMD = %#04x [%s] at %lld : id = %d
000ad02f  true == ipcEndpointSetDone
000ad04a  readBufAddr 0x%llx, writeBufAddr 0x%llx, readBufLen 0x%x, writeBufLen 0x%x, DoorBellBit 0x%x, DoorBellReg 0x%llx
000ad0bc  Unsupported IPC endpoint type %d
000ad0de  ReadRingBufAddr 0x%llx, writeBufAddr 0x%llx, readBufLen 0x%x, writeBufLen 0x%x, DoorBellBit 0x%x, DoorBellReg 0x%llx
000ad154  CSNE_CMD_IPC_ENDPOINT_UNSET2 ProgramUnsetup
000ad181  pReadRing != NULL
000ad193  pWriteRing != NULL
000ad1a6  pCmd->readRingBufferAddr == (uint64_t)BSP_TARGET_TO_HW(pReadRing)
000ad1e8  pCmd->writeRingBufferAddr == (uint64_t)BSP_TARGET_TO_HW(pWriteRing)
000ad22c  CSNE_CMD_LOAD_AFPP is not allowed after IPC endpoint set
000ad266  CSNE_CMD_LOAD_AFPP is not allowed multi AFPP 
000ad295  false == AFPPLoaded
000ad2a9  CSNE_CMD_LOAD_AFPP does not support dummy response
000ad2dd  package buf = 0x%llx, size=0x%llx
000ad300  Load AFPP
000ad30b  CSNE_CMD_UNLOAD_AFPP is not allowed after IPC endpoint set
000ad347  CSNE_CMD_UNLOAD_AFPP is not allowed if there is no AFPP load before
000ad38c  CSNE_CMD_UNLOAD_AFPP does not support dummy response
000ad3c2  Unload AFPP
000ad3cf  [%s] CMD = %#04x [%s] at %lld : val=0x%x
000ad3f9  CSNE_CMD_PREMAP_BUFFER preMap op %d > max %d
000ad427  pCmd->numOfPreMapOp <= (16)
000ad443  Process should have only 1 stats buffer (%d) for PreMap
000ad47c  pPreMapOp->nbrOfBuffers == 1
000ad499  PreMap Stats Buf: progId=%d, procId=%d, map=%d, addr 0x%llx, size 0x%llx
000ad4e3  CSNE_CMD_PREMAP_BUFFER preMapInferencePropertyBuf op %d != 1 
000ad522  pCmd->numOfPreMapOp == 1
000ad53b  CSNE_CMD_PREMAP_BUFFER preMapInferencePropertyBuf nbrOfBuffers %d != 1 
000ad584  CSNE_CMD_PREMAP_BUFFER preMapInferencePropertyBuf bufValid == 0 
000ad5c6  pPreMapOp->buffer[0].valid
000ad5e1  CSNE_CMD_PREMAP_BUFFER preMapInferencePropertyBuf bufAddr == 0 
000ad622  bufAddr
000ad62a  CSNE_CMD_PREMAP_BUFFER preMapInferencePropertyBuf bufSize == 0 
000ad66b  bufSize
000ad673  PreMap InferenceCallPropertyBuf: addr 0x%llx, size 0x%llx
000ad6ae  Unexpected premap type %d
000ad6c8  rcLocal == 0
000ad6d5    Streams = %d
000ad6e5    Controller = %p
000ad6f8    Command log [Last issued first]:
000ad75f      No commands issued so far.
000ad77f  [%s]  CMD = %#04x [%s] ack %d at %lld
000ad7a6  POWER_ON
000ad7af  [%s] POWERON (this=%p)
000ad7c7  [%s] CTRL READY
000ad7d8  CTRL_READY
000ad7e3  [%s: %.6f] CH = %x CMD = %#04x [%s]
000ad808  [%s: %.6f (delta: %f us)] CMD = %#04x [%s] Executed.
000ad83d  CH = %x NOT READY, CMD = %#04x [%s]
000ad862  pDMBus failed to get its EndPoint status
000ad88b  Wrong DMBUS EndPoint Status
000ad8a7  state == ECDMEDIABUSMANGER_ENDPOINT_CB_STATE_IDLE
000ad8d9  %d programs are NOT unloaded!
000ad8f7  %d processes are NOT terminated!
000ad918  power callback: to sleep: counter=%u
000ad93e  power callback: wakeup: counter=%u
000ad962  Uncorrectable L2C error overflow
000ad984  ProgramId = %d
000ad994  [%s] CMD = %#04x [%s] at %lld : ProgramId = %d Process = %d 
000ad9d2  [%s] CMD = %#04x [%s] at %lld not supported in normal channel
000ada10  mInstance
000ada1a  ./sne/controller/target/CAneControllerStringsH11.cpp
000ada4f  ID 0x%x not supported!
000ada66  CSNE_CMD_STOP
000ada74  CSNE_CMD_RESET
000ada83  CSNE_CMD_CONFIG_GET
000ada97  CSNE_CMD_PRINT_ENABLE
000adaad  CSNE_CMD_REG_FILE_LOAD
000adac4  CSNE_CMD_BUILDINFO
000adad7  CSNE_CMD_TIMEPROFILE_START
000adaf2  CSNE_CMD_TIMEPROFILE_STOP
000adb0c  CSNE_CMD_TIMEPROFILE_SHOW
000adb26  CSNE_CMD_FW_RUN_MODE
000adb3b  CSNE_CMD_POWER_DOWN
000adb4f  CSNE_CMD_SET_SNE_PMU_BASE
000adb69  CSNE_CMD_SET_SNE_RPC_CHECK_CMD
000adb88  CSNE_CMD_RPC_ENABLE
000adb9c  CSNE_CMD_PLATFORM_INFO
000adbb3  CSNE_CMD_BOOT
000adbc1  CSNE_CMD_PING
000adbcf  CSNE_CMD_CONFIG_GET_EXT
000adbe7  CSNE_CMD_POWER_DEVICE_ON
000adc00  CSNE_CMD_POWER_DEVICE_OFF
000adc1a  CSNE_CMD_IPC_ENDPOINT_SET
000adc34  CSNE_CMD_IPC_ENDPOINT_UNSET
000adc50  CSNE_CMD_CH_INFO_GET
000adc65  CSNE_CMD_CH_BUFFER_RECYCLE_MODE_SET
000adc89  CSNE_CMD_CH_BUFFER_RECYCLE_START
000adcaa  CSNE_CMD_CH_BUFFER_RECYCLE_STOP
000adcca  CSNE_CMD_CH_BUFFER_RETURN
000adce4  CSNE_CMD_CH_BUFFER_POOL_CONFIG_GET
000add07  CSNE_CMD_CH_BUFFER_POOL_CONFIG_SET
000add2a  CSNE_CMD_CH_DATA_FILE_LOAD
000add45  CSNE_CMD_CH_PROPERTY_WRITE
000add60  CSNE_CMD_CH_PROPERTY_READ
000add7a  CSNE_CMD_TRACE_ENABLE
000add90  CSNE_CMD_RESOURCE_INFO_GET
000addab  CSNE_CMD_STATS_BUFFER_SIZE_GET
000addca  CSNE_CMD_SUSPEND
000adddb  CSNE_CMD_DSID_SET
000added  CSNE_CMD_MCACHE_SIZE_GET
000ade06  CSNE_CMD_SECURE_MODE_START
000ade21  CSNE_CMD_SECURE_MODE_STOP
000ade3b  CSNE_CMD_SET_SNE_PMU_BASE2
000ade56  CSNE_CMD_IPC_ENDPOINT_SET2
000ade71  CSNE_CMD_IPC_ENDPOINT_UNSET2
000ade8e  CSNE_CMD_CH_DATA_FILE_LOAD2
000adeaa  CSNE_CMD_SET_DYNAMIC_POWERGATE
000adec9  CSNE_CMD_ANE_DEFAULT_SETTING_SET
000adeea  CSNE_CMD_INIT_SHARED_EVENT_INFO
000adf0a  CSNE_CMD_EXCLAVE_MODE_START
000adf26  CSNE_CMD_EXCLAVE_MODE_STOP
000adf41  CSNE_CMD_QUIESCE_STATE
000adf58  CSNE_CMD_CPU_LOAD_GET
000adf6e  CSNE_CMD_SECURE_MODE_RESUME_TRANSITION
000adf95  CSNE_CMD_RESUME
000adfa5  CSNE_CMD_CH_ERROR_NOTIFICATION
000adfc4  CSNE_CMD_CH_POWER_CONTROL
000adfde  CSNE_CMD_CH_SIGNPOST_NOTIFICATION
000ae000  CSNE_CMD_CH_SIGNPOST_NOTIFICATION_GROUP
000ae028  CSNE_CMD_CH_RESET_NOTIFICATION
000ae047  CSNE_CMD_CH_SIGNPOST64_NOTIFICATION
000ae06b  CSNE_CMD_CH_SIGNPOST64_NOTIFICATION_GROUP
000ae095  CSNE_CMD_CPU_LOAD_NOTIFICATION
000ae0b4  CSNE_CMD_TM_SYNC_ERR_NOTIFICATION
000ae0d6  CSNE_CMD_LOAD_PROGRAM
000ae0ec  CSNE_CMD_UNLOAD_PROGRAM
000ae104  CSNE_CMD_CREATE_PROCESS
000ae11c  CSNE_CMD_TERMINATE_PROCESS
000ae137  CSNE_CMD_PROCEDURE_CALL
000ae14f  CSNE_CMD_LOAD_AFPP
000ae162  CSNE_CMD_UNLOAD_AFPP
000ae177  CSNE_CMD_PROGRAM_INTERFACE_VERSION_CHECK
000ae1a0  CSNE_CMD_PROCEDURE_CALL_CACHE_REQUEST
000ae1c6  CSNE_CMD_PROCEDURE_CALL_TRIGGER_CACHE_REQUEST
000ae1f4  CSNE_CMD_PROCEDURE_CALL_RECYCLE_OUTPUT_BUFFER
000ae222  CSNE_CMD_PROCEDURE_CALL_INVALIDATE_CACHE_REQUEST
000ae253  CSNE_CMD_PROCEDURE_CALL_WITH_CUSTOM_BARS
000ae27c  CSNE_CMD_PREMAP_BUFFER
000ae293  CSNE_CMD_PROCEDURE_CALL_CACHE_REQUEST_WITH_CUSTOM_BARS
000ae2ca  CSNE_CMD_PROCEDURE_CALL_CACHE_REQUEST_WITH_SHARED_EVENTS
000ae303  CSNE_CMD_FORCE_DISABLE_CACHE_REQUESTS
000ae329  CSNE_CMD_PROCEDURE_CALL_WITH_SIGNAL_EVENTS
000ae354  CSNE_CMD_SET_ACTIVE_CACHE_REQUEST_IN_GROUP
000ae37f  CSNE_CMD_SET_SIGNAL_EVENTS
000ae39a  CSNE_CMD_PROGRAM_EVENT
000ae3b1  CSNE_CMD_USER_EVENT
000ae3c5  CSNE_CMD_DBG_EVENT
000ae3d8  CSNE_CMD_DATA_CHAINING_EVENT
000ae3f5  CSNE_CMD_PREFETCH_DSID_EVENT
000ae412  CSNE_CMD_SECURE_MODE_EVENT
000ae42d  CSNE_CMD_REQUEST_PROGRAM_ID
000ae449  CSNE_CMD_RETURN_PROGRAM_ID
000ae464  CSNE_CMD_REQUEST_PROCESS_ID
000ae480  CSNE_CMD_RETURN_PROCESS_ID
000ae49b  CSNE_CMD_INFERENCE_CALL
000ae4b3  CSNE_CMD_BACK_CHANNEL_RPC
000ae4cd  CSNE_CMD_DEBUG_COMMAND_DATA_CHECK
000ae4ef  ./sne/common/misc/CLoadMonitor.cpp
000ae512  Unknown property write 0x%x
000ae52f  ./sne/common/framework/CRPCClient.cpp
000ae555  mutex != (FFWMUTEX)0
000ae56a  cmdMutex != (FFWMUTEX)0
000ae582  endpointFToH->getMsgBufferSize() >= totalSharedMemSize
000ae5b9  CRPCClient.cpp
000ae5c8  pSharedMemBuf != __null
000ae5e0  cmdSemaT2H != (SEMA)0
000ae5f6  fileSema != (SEMA)0
000ae60a  pcSema != (SEMA)0
000ae61c  resetMutex != (FFWMUTEX)0
000ae636  traceFlushTimer != __null
000ae650  traceFlushSema != (SEMA)0
000ae66a  CRPCClientPipe
000ae679  %s:[%lld] traceFlushSema is up
000ae698  SignalProcessor
000ae6a8  pointer != __null
000ae6ba  size > 0
000ae6c3  message != __null
000ae6d5  rc == true
000ae6e0  Ack Secure Mode event
000ae6f6  idx[%d] buffer address (%p) does not match message (%p)
000ae72e  directProcCallEvent[idx].pCmdBuf == message
000ae75a  cacheReqEvent[idx].pCmdBuf == message
000ae780  CR idx (%d) not in use, used by %llx event %d alloc at %lld, free at %lld id:%d
000ae7d0  (event->bUsed == 1)
000ae7e8  message
000ae7f0  pCachedCmd != __null
000ae805  Normal Program Event should go through caller directly.
000ae83d  Debug Event should go through caller directly.
000ae86c  pPowerControlCmd
000ae87d  Power Control Notification (0x%x) being sent to the host with Norm %d
000ae8c8  pResetCmd
000ae8d2  Reset Notification (%d) being sent to the host. start=%d, end=%d
000ae913  pErrorCmd
000ae91d  Error Notification (%d) ch %d being sent to the host.
000ae953  Cpu Load Notification should go through caller directly.
000ae98c  Data Chaining Event should go through caller directly.
000ae9c3  pEventCmd
000ae9cd  Dsid (%d) Event (0x%x)
000ae9e9  nameLen <= maxNameLen
000aea04  Program Event (0x%x) (0x%x 0x%x 0x%x 0x%llx)
000aea31  pCacheReqData->inputInfoListIdx != (0xFFFFFFFF)
000aea61  pReqInputInfo
000aea6f  numInput == pEventCmd->nbrOfInputBuffers
000aea98  invalid pointer for cacheHander 0x%llx event %d
000aeac8  pReqInputInfo != __null
000aeae0  Data Chaining Event (0x%x) (0x%x 0x%x 0x%x)
000aeb0c  Cache handler 0x%llx, outputBufferSetId %d, nbrOfInputBuffers %d
000aeb4d  Input %d surfaceId 0x%x, offset 0x%llx
000aeb74  pDbgCmd
000aeb7c  Dbg Event (0x%x) (0x%x 0x%x 0x%x 0x%x 0x%llx)
000aebaa  pEvent != __null
000aebbb  Invalid secure mode %d
000aebd2  mode < eAnsCmdSecureMode_Max
000aebef  Secure Mode Event %d at 0x%llx)
000aec0f  sending reset notification to driver
000aec34  pNotificationCmd
000aec45  CPU Load Notification (%d) being sent to the host.
000aec78  trace type %zu code %d  %lld %lld %lld %lld %lld
000aeca9  Invalid trace log in ISR! type %zu code %d  %lld %lld %lld %lld %lld
000aecee  ANE_PROPERTY_PRCDAEMON_KTRACE_FLUSH_TIME %d
000aed23  eventMapMutex != (FFWMUTEX)0
000aed40  traceBufferMutex != (FFWMUTEX)0
000aed60  map[i].index == i
000aed72  RPCEventMap[%d] is dirty. (No ack from driver) : cmd[%d]
000aedab  size == 0
000aedb5  WRN: ffwTimerStop() called without start from %s
000aede7  sharedBuffer
000aedf4  bufferCount
000aee00  element
000aee08  index < mapSize
000aee18  map[index].index == index
000aee32  map[index].dirty
000aee43  map[index].cmdId == cmdId
000aee5d  Direct procedure call event idx (%d) out of range
000aee8f  (event->idx >= 0 && event->idx < (4))
000aeeb5  Direct procedure call event idx (%d) not in use
000aeee5  Direct procedure call event invalid type
000aef0e  (event->bDirectProcCall == 1)
000aef2c  Direct procedure call event address (%p) mismatch
000aef5e  (event == &directProcCallEvent[event->idx])
000aef8a  Direct procedure call cmd buffer (%p) mismatch (%p)
000aefbe  (event->pCmdBuf == ((uint8_t*)pDirectProcCallCmdBuf + event->idx * directProcCallCmdSize))
000af019  Cache request event idx (%d) out of range
000af043  (event->idx >= 0 && event->idx < (64))
000af06a  Cache request event idx (%d) not in use
000af092  Cache request event invalid type
000af0b3  (event->bCacheRequest == 1)
000af0cf  Cache request event address (%p) mismatch
000af0f9  (event == &cacheReqEvent[event->idx])
000af11f  Cache request cmd buffer (%p) mismatch (%p)
000af14b  (event->pCmdBuf == ((uint8_t*)pCacheReqCmdBuf + event->idx * cacheReqCmdSize))
000af19a  RPC direct post failed
000af1b1  status == RTK_ST_OK
000af1c5  out of command cache!
000af1dc  No Cache request event available
000af1fd  pCacheReqEventPool->Size() > 0
000af21c  Cache request event idx (%d) used already
000af246  (pEvent->bUsed == 0)
000af25b  (pEvent->idx >= 0 && pEvent->idx < (64))
000af284  (pEvent->bCacheRequest == 1)
000af2a1  (pEvent == &cacheReqEvent[pEvent->idx])
000af2c9  (pEvent->pCmdBuf == ((uint8_t*)pCacheReqCmdBuf + pEvent->idx * cacheReqCmdSize))
000af31a  traceBufferSize == (64)
000af332  pushCQ(traceBuffer) != -1
000af34c  All %d of trace buffer cache is used. (trace point drops)
000af386  ./sne/common/framework/driverCmdErr.cpp
000af3b2  ./sne/common/misc/tunable/TunableManager.cpp
000af3df  Current ANE doens't have tunables!
000af402  [%d] addr:value=(%#lx:%#x)
000af41d  Tunable is not loaded!
000af435  ---------- RELOAD TUNABLES ----------
000af481  ./sne/common/Debug/CDebugUtility.cpp
000af4a6  CRPCClient is not up yet
000af4c0  CDebugUtility.cpp
000af4d2  FileWrite invalid file %s
000af4ec  ./sne/common/Debug/CTraceBuffer.cpp
000af510  mutex != (FFWMUTEX) 0
000af526  CTraceBuffer.cpp
000af537  CTraceBuffer() create: pPtr=%p
000af557  ANE Trace Buffer starts:
000af571  TraceBuffer:     %p
000af586  ./sne/common/Debug/CCommandLogger.cpp
000af5ac  cmdLog[%d] is not valid
000af5c4  pCmdLog->valid == 1
000af5d8  cmdLog[%d] cmd id match (0x%x v 0x%x)
000af5fe  pCmdLog->cmdId == cmdId
000af616  First %d buffers info:
000af62e  Buffer %d: Index: %2lld, Addr: 0x%llx
000af655  ^^^^^^^^^^ LAST CMD LOG ENTRY ^^^^^^^^^^
000af6b5  %2d: CMD: %#04x [%s]
000af6cb  ProgId %lld
000af6d8  ProgId %lld, ProcId %lld
000af6f2  ProgId %lld, ProcId %lld, ProcedureId %lld, UUID %llu
000af729  ProgId %lld, ProcId %lld, ProcedureId %lld, UUID %llu, customBars %lld
000af771  ProgId %lld, ProcId %lld, ProcedureId %lld, %s, CacheHandler 0x%llx
000af7b6  SINGLE USE
000af7c1  NORMAL
000af7c8  CacheHandler 0x%llx
000af7dd  Group CacheHandler 0x%llx, active 0x%llx
000af807  ENABLE
000af80e  DISABLE
000af816  ProgId %lld, ProcId %lld, ProcedureId %lld, UUID %llu, Event %lld
000af859  CacheHandler 0x%llx, Event %lld
000af87a  CH: %s [%s], RECV: %lld, ACK: %lld, TIME: %04dus
000af8ac  EXELOOP
000af8b8  THREAD
000af8bf  [%s] SEND: %lld
000af8d0  ./sne/common/Debug/CAneLatencyProfiler.cpp
000af8fb  RPCClient does not exist
000af914  CRPCClient::Instance() != __null
000af942  ./sne/drivers/FE/CConfigDrv.cpp
000af962  H11ConfigDrv
000af96f  ./sne/drivers/tm/CSneTMDrvHx.cpp
000af990  ./sne/drivers/tm/CSneTMDrvH18g.cpp
000af9b3  queueId < (8)
000af9c1  waitTQIdle() for TQ(%d) failed after waiting for more than 2 sec
000afa02  tqStatus.f.Idle == 1
000afa17  Setting TQ[%d] to invalid TQ state %d
000afa3d  state < MAX_NUM_ANE_TQ_STATE
000afa5a  Set TQ[%d] priority to 0x%x
000afa76  Set TQ[%d] cfg to 0x%x
000afa8d  ./sne/drivers/mcw/CSneMCWDrv.cpp
000afaae  pInstance == __null
000afac2  __null != pInstance
000afad6  ./sne/drivers/mcw/CSneMCWDrvH15.cpp
000afafa  baseAddr
000afb03  ANE MCW pending IRQ for DSID_CLR (0x%x) should be 0
000afb37  (irqStatus.all & 0xF) == 0
000afb52  MCW module driver reset complete. baseAddr 0x%llx
000afb84  dsid %d out of range
000afb99  (dsid >= (124)) && (dsid <= (127))
000afbbc  dsidCtl for DSID %d (addr 0x%llx): 0x%x
000afbe4  dsidCtl for DSID %d (addr 0x%llx): 0x%x is BUSY
000afc14  ./sne/drivers/itq/CSneItqDrvHx.cpp
000afc37  ./sne/drivers/itq/CSneItqDrvH18g.cpp
000afc5c  (itqId >= (21)) && (itqId <= (23))
000afc7f  Setting ITQ[%d] to invalid TQ state %d
000afca6  state <= ANE_ITQ_TQCFG_STATE_ENABLED
000afccb  Set ITQ[%d] priority to 0x%x
000afce8  ./sne/drivers/CE/CSneCEDrv.cpp
000afd07  ./sne/drivers/CE/CSneCEDrvH18g.cpp
000afd2a  IPCE was in error state: 0x%08x
000afd4a  GetError() == 0
000afd5a  IPCE ID1=%d ID2=%d
000afd6e  SOC_CFG_IPCE_STATUS_ERROR_STATUS0 0x%lx: 0x%x
000afd9d  SOC_CFG_IPCE_STATUS_ERROR_STATUS1 0x%lx: 0x%x
000afdcc  SOC_CFG_IPCE_STATUS_ERROR_STATUS2 0x%lx: 0x%x
000afdfb  SOC_CFG_IPCE_STATUS_ERROR_STATUS3 0x%lx: 0x%x
000afe2a  script_%derror
000afe3a  soc_cfg_error_interrupt
000afe53  ipce_error_interrupt
000afe69  ./sne/aneEngine/common/CAneProgramManager.cpp
000afe97  __null == mInstance
000afeb0  __null != progList[i].pProgram
000afed4  pAneProgramInfo
000afee4  mInstance == this
000afef6  progId < maxProg
000aff07  progId %d not in use
000aff1c  progList[progId].used == 1
000aff37  procId < maxProc
000aff48  procId %d for progId %d not in use
000aff6b  processList[procId].used == 1
000aff89  processList[%d].progId %d vs. %d
000affaa  Rsvd Inconsistent programId in ANE request.
000affd6  nbr of proc=%d
000affe6  !progList[progId].nbrOfProcess
000b0005  __null != prog
000b0014  index < maxProg
000b0024  progList[index].used == 0
000b003e  progList[index].builtinProgramId == ANE_NET_TOT
000b006e  pProg->used == 0
000b007f  pProg->builtinProgramId == ANE_NET_TOT
000b00a6  invalid program ID: programId=%d max=%d
000b00ce  program not in use: programId=%d
000b00ef  process not empty: programId=%d processNum=%d
000b011d  Received a Load Program request
000b0147  CAneProgramManager.cpp
000b015e  call->stats.buffer >= pProc->pStatArrayBaseOrig
000b018e  statsBufOffset + call->stats.size < pProc->sizeOfStatBufArray
000b01cc  stats buffer size is not enough: size=%lld, statsData=%d, statsDescrptor=%d, statsDataDbgEvent=%d
000b022f  call->stats.size >= sizeof(sCAneStatsData) + sizeof(sEventDescriptors) + sizeof(sCAneStatsDataDbgEvent)
000b0297  debug event buffer: offset=%d, size=%d
000b02be  bypass mode only works for type0 or type3 or type4
000b02f2  (getProcedureCallType(call->programId, call->procedureId) == eCSneCmdProgramProcedureContentType_0) || (getProcedureCallType(call->programId, call->procedureId) == eCSneCmdProgramProcedureContentType_3) || (getProcedureCallType(call->progra
000b0424  (cmd->priority >= (1) && cmd->priority <= (5))
000b0453  pProc->state == eProcessState_running
000b0479  cmd->statsBuffer.size >= sizeof(sCAneStatsData) + sizeof(sEventDescriptors) + sizeof(sCAneStatsDataDbgEvent)
000b04e6  cmd->statsBuffer.buffer >= pProc->pStatArrayBaseOrig
000b051b  statsBufOffset + cmd->statsBuffer.size < pProc->sizeOfStatBufArray
000b055e  debug event buffer: offset=%d size=%d
000b0585  bypass mode only works for type0 or type3
000b05b0  (getProcedureCallType(call->programId, call->procedureId) == eCSneCmdProgramProcedureContentType_0) || (getProcedureCallType(call->programId, call->procedureId) == eCSneCmdProgramProcedureContentType_3)
000b067b  Invalid jobQueueId returned
000b0697  jobQueueId != (uint32_t)-1
000b06b2  pRequest
000b06bb  eventIn < eAneRequestCallBackEvent_max
000b06e8  Output set %d is in wrong state %d in Callback
000b0717  pCacheReqIoInfo->pOutputSets[pCacheReqData->outputSetId].state == ANE_DATA_CHAINING_OUTPUT_SET_IN_EXECUTION
000b0783  pProc != __null
000b0793  pRequest->id < maxProcTdSection
000b07b3  0 == requestCnt
000b07c9  pProg != __null
000b07d9  [Fail] Unmap StatsBuffer (addr:0x%llx, size:0x%x)
000b080b  Unexpected pFinishEvent %p detected
000b082f  pRequest->bFinishEventSent == 0
000b084f  programId %d %d %d %d tdPartitionId %d tdPartitionToT %d %d %d report finishEvent1 %d
000b08a5  programId %d %d %d %d tdPartitionId %d tdPartitionToT %d %d %d report finishEvent2 %d
000b08fb  auxInfo->userData[0] == 1
000b0915  auxInfo->userData[1]
000b092a  pProg->builtinProgramId < ANE_NET_TOT
000b0950  The program ID is out of range: progId=%d
000b097a  The program ID passed from driver is not used: progId=%d
000b09b3  totDbgEvent is invalid
000b09cb  statsBufferSizeGet(): sizeof: %d, %d, %d, %d. cnt=%d, totSize=%d
000b0a0c  stats buffer: useDramLog: %d, size: %d
000b0a33  ret < maxProcTdSection
000b0a4a  programId %d processId %d ret %u
000b0a6b  programId %d processId %d requestId %d
000b0a92  processId %d programId %d requestId %d invalid
000b0ac1  requestId < maxProcTdSection
000b0ade  new jobQueueId (%d) does not match jobQueuedId (%d) saved in process
000b0b23  pProc->jobQueueId == jobQueueId
000b0b43  TerminateCacheRequest waited for single use cache request too long
000b0b86  cache request state (%d) is not expected in TerminateCacheRequest()
000b0bca  cacheReqState == ANE_DATA_CHAINING_CACHE_REQUEST_IN_USE
000b0c02  TerminateCacheRequest waited for state change too long
000b0c39  TerminateCacheRequest waited for pending cnt too long
000b0c6f  TerminateCacheRequest waited for abort too long
000b0c9f  Number of input buffers mismatch for single use cache request. Total (%d), Network (%d)
000b0cf7  totalNbrOfInputBuffers == numOfInputInNetwork
000b0d25  Number of output buffers mismatch for single use cache request. Total (%d), Network (%d)
000b0d7e  totalNbrOfOutputBuffers == numOfOutputInNetwork
000b0dae  Should be only 1 output set for single use cache request (%d)
000b0dec  nbrOfOutputBufferSets == 1
000b0e07  pChainingIOInfo->pOutputSets != __null
000b0e33  pChainingIOInfo->inputs.pBuffer != __null
000b0e5d  pChainingIOInfo->inputs.pHashTable != __null
000b0e8a  pChainingIOInfo->inputs.pReadyMap != __null
000b0eb6  pOutputSet->pBuffer != __null
000b0ed4  [Fail] Unmap StatsBuffer (addr:0x%llx, size:0x%llx)
000b0f0e  Unexpected command Id (%d)
000b0f29  The ANE request address passed from AneExeLoop is invalid
000b0f63  pRequest != __null
000b0f76  The ChainingInfo address passed from AneExeLoop is invalid
000b0fb1  pChainingIOInfo != __null
000b0fcb  jobQueueId passed from AneExeLoop is invalid
000b0ff8  pushToHWDirect() function should be overridden
000b1027  Must have at least 2 entries in fifo (%zu)
000b1052  CRPCClient::Instance()->GetDirectProcCallEventPoolAvailNum() >= 2
000b1094  programId %d %d %d report programEvent %d
000b10be  Must have valid buffe address (0x%llx) and size (0x%llx)
000b10f7  statsBufAddr && statsBufSize
000b1114  prog %d proc %d already has mapped stats buf. V: 0x%llx P: 0x%llx
000b1156  pProc->pStatsBufArrayMapped == __null
000b117c  prog %d proc %d has no mapped stats buf.
000b11a5  prog %d proc %d stats address does not match. O: 0x%llx A: 0x%llx
000b11e7  pProc->pStatArrayBaseOrig == statsBufAddr
000b1211  [Fail] Unmap StatsBuffer (addr:0x%p, size:0x%x)
000b1241  pInferenceCallPropertyBufMapped == __null
000b126b  nextProcedureSegIdx
000b127f  bIsLastSegment
000b128e  bIsTidRewind
000b129b  runningProcedureSegIdx >= 0
000b12b7  true == pReq->bIsMultipleSegments
000b12d9  false == pReq->bIsLastSegPushed
000b12ff  myProg
000b1306  nextExecuteOrderIdxListIdx < (int32_t)pReq->nbrOfExecuteOrder
000b1344  runningProcedureSegIdx < (int32_t)pProcedureContent->numOfSegments
000b1387  myNextProcedureSegIdx > 0
000b13a1  nextProgramSegIdx == pNextProgramSegProp->programSegmentIndex
000b13df  segment (%d) property's len is 0
000b1401  pNextProgramSegProp->len != 0
000b141f  Update Prog %d Procedure %d Seg %d:
000b1443    nextIdx %d, isLast %d, nextRewind %d
000b146a  Last seg firstTID %d, numTdInSegment %d
000b1492  nextSegIdx
000b149d  runningSegIdx >= 0
000b14b0  pCallProperty
000b14be  runningSegIdx < (int32_t)pCallProperty->nbrOfSegments
000b14f4  nextIdx > 0
000b1500  nextIdx < (int32_t)pCallProperty->nbrOfSegments
000b1530  pNextSeg->len
000b153e  *bIsTidRewind == false
000b1555  Update prog=%d proc=%d seg=%d:
000b1574    nextSeg=%d isLast=%d isRewind=%d
000b1598  Last seg's firstTID=%d
000b15b0  Net steps %zu crc %d
000b15c5  No Direct procedure call event available
000b15ee  pDirectProcCallEventPool->Size() > 0
000b1613  Direct procedure call event idx (%d) used already
000b1645  (pEvent->idx >= 0 && pEvent->idx < (4))
000b166d  (pEvent->bDirectProcCall == 1)
000b168c  (pEvent == &directProcCallEvent[pEvent->idx])
000b16ba  (pEvent->pCmdBuf == ((uint8_t*)pDirectProcCallCmdBuf + pEvent->idx * directProcCallCmdSize))
000b1717  ./sne/aneEngine/common/CAneEngineExeLoop.cpp
000b1744  mInstance == __null
000b1758  eCmdStatsItem_IsrEnter
000b176f  eCmdStatsItem_IsrHandler
000b1788  eCmdStatsItem_IsrMem1
000b179e  eCmdStatsItem_IsrMem2
000b17b4  eCmdStatsItem_IsrDone
000b17ca  eCmdStatsItem_IsrELRecv
000b17e2  eCmdStatsItem_IsrCmdHandle_1
000b17ff  eCmdStatsItem_IsrCmdHandle_2
000b181c  eCmdStatsItem_IsrCmdHandle_3
000b1839  eCmdStatsItem_IsrCmdHandle_4
000b1856  eCmdStatsItem_IsrElDone
000b186e  maxPriorityNbr <= (6)
000b1884  maxJobNbr <= (144 * 2)
000b189b  maxClinetNbr <= 2
000b18ad  avgQueueDepth <= 32
000b18c1  maxUserRequest <= ((6) * 32 * 2)
000b18e2  clientInfo
000b18ed  clientMutex != (FFWMUTEX)0
000b1908  pCmdChPendingCmd
000b1919  sharedEventsSema != (SEMA)0
000b1935  sharedEventsCntMutex != (FFWMUTEX)0
000b1959  ipcSema != (SEMA)0
000b196c  jobCount(%d) should <= maxJobNbr(%d)
000b1992  jobCount <= maxJobNbr
000b19a8  priorityCount <= maxPriorityNbr
000b19c8  exceed max client count %d
000b19e4  id != CIndexPool::invalidIndex
000b1a03  !clientInfo[id].valid
000b1a19  userId < maxClinetNbr
000b1a2f  clientInfo[userId].valid
000b1a48  PerfMode (%d) have been set previously already.
000b1a78  SwitchExclaveMode not supported
000b1a98  setDirectAneRequestInfo() function should be overridden
000b1ad0  idx(%d) for reserved network desc out of range
000b1aff  idx < (2)
000b1b09  reserved network desc [%d] is NULL
000b1b2c  pReservedNetworkDesc[idx] != __null
000b1b50  enableEventLogInNetworkDesc() function should be overridden
000b1b8c  pStatsBufferBase != 0
000b1ba2  ANE_DRAM_EVENT_STATS_BUFFER_VERSION not supported
000b1bd4  pStatsBuffer->version != (uint16_t)0x0201
000b1bfe  command padding (0x%x) is not 0
000b1c1e  pCmd->padding == 0
000b1c31  magic number (0x%x) incorrect
000b1c4f  pCmd->magic == 0x55AA55AA
000b1c69  first three uint32_t in command checksum (0x%x) incorrect
000b1ca3  cmdChecksum == 0xFFFFFFFF
000b1cbd  cmd addr 0x%p expected data = 0x%x, actual data[%d] = 0x%x
000b1cf8  pCmd->data[i] == expectedValue
000b1d17  invalid bar number: %d
000b1d2f  nbrBars && nbrBars <= 122
000b1d49  invalid bar value: index=%d value=0x%llx size=%lld
000b1d7d  value && bufferSize
000b1d91  invalid bar prefetch dsid value: index=%d dsid=%lld
000b1dc5  (value >= (124)) && (value <= (127))
000b1dea  invalid bar type: index=%d type=%d
000b1e0e  invalid 32bit bar id: index=%d barId=%d
000b1e37  barId < 122
000b1e43  invalid 64bit bar id: index=%d barId=%d
000b1e6c  hwBarId < 122
000b1e7a  invalid bar config: index=%d config=%d
000b1ea2  CMD = %#04x [INFERENCE CALL] at %lld : programId=%d processId=%d priority=%d
000b1ef0  nbrBar=%d nbrSeg=%d nbrWaitEvt=%d nbrSigEvt=%d
000b1f20  inferenceCallProperty addresses: offset=%lld size=%lld mappedBase=%p mappedSize=%llu dvaBase=%p dvaAddr=0x%llx
000b1f90  ProcedureId=%d uuid=0x%llx
000b1fac  nid=%d nid2=0x%d isBonded=%d isHWbranch=%d isRewind=%d
000b1fe4  generic
000b1fec  kernel 
000b1ff4  mkernel
000b1ffc  input  
000b2004  output 
000b200c  intMdia
000b2014  mcdsid 
000b201c  unknown
000b2036  bar[%d]: type=%d(%s) cfg=%d(%s) barId=%d value=0x%llx bufSize=%lld
000b207a  seg[%d]: id=%d nextId=%d 1stTid=%d isBranching=%d isBranched=%d isLast=%d isRewind=%d tdNbr=%d glbSegId=%d addr=0x%llx len=%lld
000b20fb  waitEvent[%d]: type=%d mask=%x id=%lld value=%lld
000b212e  signalEvent[%d]: type=%d mask=%d id=%lld value=%lld
000b2163  pRealSize
000b216d  CSNE_CMD_INFERENCE_CALL dropped. prog %d process %d not running.
000b21af  appPriority %d
000b21be  cmd->priority >= (1) && cmd->priority <= (5)
000b21eb  nbrOfSegments=0
000b21fb  pCallProperty->nbrOfSegments != 0
000b221d  cmd->priority >= (2) && cmd->priority <= ((2) + (3) - 1)
000b2256  bonded nid out of range %d
000b2271  pCallProperty->nid < 10
000b2289  2nd bonded nid out of range %d
000b22a8  pCallProperty->nidSecondary < 10
000b22c9  message != 0
000b22d6  insize > 0
000b22e1  insize <= sizeof(union uCExeLoopSupportedCmd)
000b230f  CAneEngineExeLoop.cpp
000b2325  messageAddr < 1UL << 36
000b233d  CSNE_CMD_PROCEDURE_CALL dropped. prog %d process %d not running
000b237d  Unexpected priority %d
000b2394  CMD = %#04x [PROC CALL] at %lld : ProgId=%d ProcId=%d Proc=%d Pri=%d
000b23da  pFinishEvent != __null
000b23f1  realSize <= insize
000b2404  cmd at 0x%llx, nbrOfCustomBars (%d) exceeded limit (%d)
000b243c  CSNE_CMD_PROCEDURE_CALL_WITH_CUSTOM_BARS dropped. prog %d process %d not running
000b248d  CMD = %#04x [PROC CALL WITH BARS] at %lld : ProgId=%d ProcId=%d Proc=%d Pri=%d
000b24dd  (supplementCmdOffset + supplementCmdSize) <= insize
000b2511  cmd->procCallWithSignalEvents.nbrOfCustomBars <= (122)
000b2548  cmd at 0x%llx, nbrOfCustomBars (%d) outside limit (%d)
000b257f  cmd->procCallWithSignalEvents.nbrOfSignalEvents > 0 && cmd->procCallWithSignalEvents.nbrOfSignalEvents <= (16)
000b25ee  CSNE_CMD_PROCEDURE_CALL_WITH_SIGNAL_EVENTS dropped. prog %d process %d not running
000b2641  CMD = %#04x [PROC CALL WITH EVENTS] at %lld : ProgId=%d ProcId=%d Proc=%d Pri=%d
000b2693  CSNE_CMD_PROCEDURE_CALL_TRIGGER_CACHE_REQUEST dropped. cacheHandler 0x%llx not in use
000b26e9  CMD = %#04x [CR TRIGGER] at %lld : cacheHandler 0x%llx
000b2721  CSNE_CMD_PROCEDURE_CALL_RECYCLE_OUTPUT_BUFFER dropped. cacheHandler 0x%llx not in use
000b2777  CSNE_CMD_SET_ACTIVE_CACHE_REQUEST_IN_GROUP dropped. group/active cacheHandler not in use
000b27d0  [ISR] CMD = %#04x [%s] at %lld
000b27f0  Unexpected CMD = %#04x in ExeLoop command channel
000b2822  pendingCmdIdx != size_t (-1)
000b283f  Unexpected pendingCmdIdx %d
000b285b  pendingCmdIdx >= 0 && pendingCmdIdx < (64)
000b2886  Ane Engine ExeLoop CMD = %#04x
000b28a5  [EXELOOP] CMD = %#04x [CR TRIGGER] at %lld : cacheHandler 0x%llx
000b28e7  Cmd 0x%x is not supported through ExeLoop cmd channel
000b291d  [EXELOOP] CMD = %#04x [PROC CALL] at %lld : ProgId=%d ProcId=%d Proc=%d Pri=%d
000b296d  [EXELOOP] CMD = %#04x [PROC CALL WITH BARS] at %lld : ProgId=%d ProcId=%d Proc=%d Pri=%d
000b29c7  [EXELOOP] CMD = %#04x [PROC CALL WITH EVENTS] at %lld : ProgId=%d ProcId=%d Proc=%d Pri=%d
000b2a23  DELAYED_ACK: Processed POWER_GATING cmd %#04x in exeloop
000b2a5c  DELAYED_ACK: No pending ACK for POWER_GATING cmd %#04x
000b2aa6  ExeLoop endpoint CMD = %#04x
000b2ac3  Cmd %d is not supported through ExeLoop IPC
000b2aef  execTimestamp (%lld) is not valid compared to current timestamp (%lld)
000b2b36  Trigger delay is %lldus
000b2b4e  Cache Requests for Data Chaining not supported
000b2b7e  -- Input ----------------------------------
000b2bab  Total number of input buffers: %d
000b2bd6  surfaceId: 0x%llx
000b2be9  offset: 0x%llx
000b2bf9  bufferIndex: %d
000b2c0a  hwBarIndex_lo: %d
000b2c1d  inputMapIndex: %d
000b2c30  bufferAddress: 0x%llx
000b2c47  bufferSize: 0x%llx
000b2c69  Number of inputs in network: %d
000b2c8a  Ready Count: %d
000b2c9b  fifo entries: %zu
000b2cae  -- Output ---------------------------------
000b2cdb  Number of output buffer sets: %d
000b2cfd  Number of output sets in fifo: %zu
000b2d21  Number of outputs in network: %d
000b2d43  -- Set %2d ---------
000b2d59  State: %d
000b2d64  offset: 0x%llxd
000b2d75  -- Stats --
000b2d82  endPointId (%d) for Exeloop must be CSNE_CMD_IPC_ENDPOINT_TYPE_DATA_CHAINING
000b2dcf  endPointId == CSNE_CMD_IPC_ENDPOINT_TYPE_DATA_CHAINING
000b2e06  Exeloop pIpcRingBufferIn is not NULL
000b2e2b  __null == pIpcRingBufferIn
000b2e46  Exeloop pIpcRingBufferOut is not NULL
000b2e6c  __null == pIpcRingBufferOut
000b2e88  IPC create readRingBufferLen %d with readRingBufferAddr at 0x%lx
000b2eca  IpcRingBufferIn
000b2eda  __null != pIpcRingBufferIn
000b2ef5  IPC create writeRingBufferLen %d with writeRingBufferAddr at 0x%lx
000b2f39  IpcRingBufferOut
000b2f4a  IPC Writer regAddr 0x%lx regValue 0x%x
000b2f72  __null != pIpcRingBufferOut
000b2f8e  Exeloop pIpcRingBufferIn is NULL
000b2faf  Exeloop pIpcRingBufferOut is NULL
000b2fd1  __null != ppReadBufferAddr
000b2fec  __null != ppWriteBufferAddr
000b3008  mpDataChainingStat
000b301b  mpDataChainingStat[i].pLatency[j]
000b303d  mpDataChainingStat[idx].pLatency[phase]
000b3065  numOfSharedEventsTarget <= MAX_ANE_SHARED_EVENT_AGENT_NUM
000b309f  Invalid event target!
000b30b6  eventTargetInfo[i].id < MAX_ANE_SHARED_EVENT_AGENT_NUM
000b30ed  Target alreadly set!
000b3103  false == sharedEventsTarget[eventTargetInfo[i].id].targetEnabled
000b3144  CISRManager::Instance()
000b315c  [Fail] Unmap Share Event Table (addr:0x%p, size:0x%llx)
000b3194  pNbrOfSignalEvents != __null && ppSignalEvents != __null
000b31cd  pSignalEvents != __null
000b31e5  mappedEventsTableAddress != __null
000b3208  pSignalEvents[i].targetMask < 0x1<<MAX_ANE_SHARED_EVENT_AGENT_NUM
000b324a  target %ld is not enabled for signal event %ld
000b3279  sharedEventsTarget[targetIdx].targetEnabled
000b32a5  Shared events ring doorbell failed for target id: %ld
000b32db  DELAYED_ACK: Enqueued cmd %#04x, slot %d
000b3304  DELAYED_ACK: Pending ACK queue full! Cannot enqueue cmd %#04x
000b3342  DELAYED_ACK: Invalid parameters for SendAckToDriver
000b3376  DELAYED_ACK: Failed to send ACK via endpoint, status=%d
000b33ae  DELAYED_ACK: Sent ACK for cmd %#04x (value=%d), cleared slot %d
000b33f3  pBuf->valid
000b343d  (pInferenceCallPropertyBufOrig <= bufAddr && bufAddr < (pInferenceCallPropertyBufOrig + sizeOfInferenceCallPropertyBuf) && (bufAddr + pBuf->size) <= (pInferenceCallPropertyBufOrig + sizeOfInferenceCallPropertyBuf) )
000b3515  programId < maxProg
000b3529  processId < maxProc
000b353d  (appPriority >= 0 && appPriority <= 0) || (appPriority >= (1) && appPriority <= (5))
000b3592  idx != CIndexPool::invalidIndex
000b35b2  function should be overridden
000b35d1  function should be overidden
000b35ef  ./sne/aneEngine/common/CAneProgramInfo.cpp
000b361a  !instance
000b3624  type < eProgramProcedureEvent_max
000b3646  type < eProcedureAbort_max
000b3661  procBuf
000b3669  wrong command id
000b367a  pProgram
000b3683  genericSection
000b3692  kernelSection
000b36a0  textSection
000b36ac  operationSection
000b36bd  procedureSection
000b36ce  kernelPropSection
000b36e0  textPropSection 
000b36f1  opDbgSection
000b36fe  procPropSection
000b3719  %s.bin
000b3720  [Fail] Generic section sanity check
000b3745  verifyGenericSection(pbuf, section->size)
000b376f  genericBuffer
000b377d  [Fail] KernelProp section sanity check
000b37a5  verifyKernelPropSection(pbuf, section->size)
000b37d2  [Fail] Operation section sanity check
000b37f9  verifyOperationSection((void*)(size_t)(section->buffer), section->size, &opVersion)
000b384d  [Fail] Invalid Opeartion version
000b386e  opVersion != 0
000b387d  [Fail] Procedure section sanity check
000b38a4  verifyProcedureSection(pbuf, section->size)
000b38d0  textPropSection
000b38e0  [Fail] Descriptor prop section sanity check
000b390d  verifyDescriptorPropSection((void *)(size_t)(textPropSection->buffer), textPropSection->size, (uint8_t*)(size_t)textSection->buffer, textSection->size)
000b39a5  ./sne/aneEngine/callManager/CAneCallManagerH11.cpp
000b39d8  myIntSema != (SEMA)0
000b39ed  myDummyRepeatSema != (SEMA)0
000b3a0a  myFlushSyncSmea != (SEMA)0
000b3a3c  instance == this
000b3a4d  size == sizeof(*pCmd)
000b3a63  __null != pReq
000b3a72  Waited out one batch done %u
000b3a90  __null != call
000b3a9f  Allocate proc call request failed
000b3ac1  illegal signal event count: %d, %d
000b3ae4  nbrOfSignalEvents <= (16)
000b3afe  illegal signal event not support custom order execution
000b3b36  0 == pSignalEventCall->bSubNetworkCustomExecuteOrder
000b3b6b  illegal custom bar count: %d, %d
000b3b8c  nbrOfCustomBars <= (122)
000b3ba5  illegal nbrOfCustomExecuteOrder %d
000b3bc8  pCustomBarsCall->nbrOfCustomExecuteOrder <= (128)
000b3bfa  illegal callSize2: %ld, %ld
000b3c16  (pCustomBarsCall->customExecuteOrderArrayOffset + pCustomBarsCall->nbrOfCustomExecuteOrder * sizeof(uint32_t)) <= sizeof(sCSneCmdProcedureCallCopyContainer)
000b3cb3  illegal customExecuteOrderArrayOffset: %d, %ld
000b3ce2  callSize <= pCustomBarsCall->customExecuteOrderArrayOffset
000b3d1d    out = %zu, avail = %zu
000b3d37  Got an event from the ANEEngine : %u %u %u %u 
000b3d67  Signal one batch done : %u %u %u %u 
000b3d8d  __null != pReqPool
000b3da0  __null != pItem
000b3db0  ./sne/aneEngine/common/CAneProgram.cpp
000b3dd7  ./program/program.bin
000b3ded  CAneProgram.cpp
000b3dfd  ./program/generic.bin
000b3e13  ./program/kernel.bin
000b3e28  ./program/td.bin
000b3e39  ./program/operation.bin
000b3e51  ./program/procedure.bin
000b3e69  ./program/kernelProp.bin
000b3e82  ./program/tdProp.bin
000b3e97  ./program/opDbg.bin
000b3eab  ./program/procProp.bin
000b3ec2  StatsBuf is null !!!
000b3ed7  ./program/statsbuf%d-%d-%d.bin
000b3ef6  ./sne/aneEngine/exeLoop/CAneEngineClient.cpp
000b3f23  userId != (uint32_t)(-1)
000b3f46  Switch
000b3f4d  ./sne/aneEngine/common/CAneDebugEventsManager.cpp
000b3f7f  Creating AneDebugEventsManager
000b3f9e  CAneDebugEventsManager.cpp
000b3fb9  pNewBufBase != __null
000b3fcf  initDbgEventMem failed due to outstanding entries being used.
000b400d  initDbgEventMem with dbgEventPerTd %d, entry size %d, total mem size %d
000b4055  CAneDebugEventsManager reallocate DbgEventMem
000b4083  No action since extra memory has already been allocated for AneDebugEventsManager.
000b40d6  TD debug event record overflow may occur. b_debugEventPerTd %d, tdCount %d, default td num %d
000b4134  pDbgEventCtrlBuf != __null
000b414f  debug event stats buffer: totalSpace=%d
000b4177  debug event stats buffer not enabled
000b41a5  idx >= 0 && idx < mNumOfEntries
000b41c5  pEntry->event.info.event < ANE_TM_EVENT_MAX
000b41f1  event_type < ANE_TM_EVENT_MAX
000b420f  No Event Received yet!
000b4226  Debug event manager detected overflow number of perf events for TDs, max event number allowed: %d
000b4289  If perf event per TD is required, please use PROPERTY WRITE 0x%x
000b42cb  Net ID : %d
000b42d8   TID         Event           Tick
000b4323   %5d     %7s     %12lld
000b433c   TID         Event           Tick
000b438c   %5d       %7s       %12lld
000b43aa  ******** Total time: %d ticks, %d us ********
000b43da  Net performance stats for %d TDs
000b43fc      TDs,      Start,        End,      Time(in us)
000b442f  Profilng incomplete for task %d: no finish execution event
000b446a  TD[%5d],%12lld,%12lld,%5d
000b4485  Profilng incomplete for task %d: no start execution event
000b44bf  ******** Total time: %llu ticks, %d us ********
000b44f0  Network Profilng incomplete. b_firstTdStartValid %d, b_lastTdEndValid %d
000b453a  TaskSwitchEvent to TD[%5d] (nTd %d), %12lld
000b4567  TaskSwitchStat: %d times for Net %d
000b458c   TID         Event       Ticks
000b45d9  L2Spill
000b45e1  ./sne/aneEngine/common/CAneProgramManagerHx.cpp
000b4611  Create process failed to allocate from pool
000b463e  index < maxProc
000b464e  pProcess->used == 0
000b4662  pProcess->state == eProcessState_Idle
000b4688  Create Process failed to allocate from pool
000b46b4  processList[index].used == 0
000b46d1  processList[index].state == eProcessState_Idle
000b4700  pProg->pProgram && pProgLoad && pProgLoad->textSection.size
000b4742  pProc->used
000b474e  Invalid cacheHandler 0x%llx in process
000b4775  cacheHandler != 0
000b4787  Process has pending command in ExeLoop
000b47ae  pProc->pendingExeLoopCmdCnt == 0
000b47cf  CAneProgramManagerHx.cpp
000b47e8  processId (%d) Job queue (%d) scheduleInfo should be invalid
000b4825  pAneExeLoop->IsScheduleInfoInvalid(pProc->jobQueueId) == true
000b4863  pCustomBar
000b486e  prefetch dsid value %lld out of range
000b4894  Custom Bar [%d] invalid type %d
000b48b4  barIndex < 122
000b48c3  barIndex %d with value 0x%x
000b48df  barIndex < (122 >> 1)
000b48f5  hwBarIndex_lo %d with value 0x%x, hwBarIndex_hi %d with value 0x%x
000b4938  Custom Bar [%d] invalid config %d
000b495a  (call->priority >= 0 && call->priority <= 0) || (call->priority >= (1) && call->priority <= (5))
000b49d4  req.pExecuteOrderIdxList
000b49ed  call->procedureId < pProg->pProgram->procNbr
000b4a1a  Invalid procedureId (%d) in procedureSection tot (%d)
000b4a50  call->procedureId < pProcProp->tot
000b4a73  numOfSegments is 0 in procedure content
000b4a9b  pProcedureContent->numOfSegments > 0
000b4ac0  req.pExecuteOrderIdxList[0] < pProcedureContent->numOfSegments
000b4aff  pSegmentProp->prop[segmentIdx].len != 0
000b4b27  No resource for new Procedure call.
000b4b4b  Found an output here 0x%llx with size %d for bufIndex %d
000b4b84  opId < pProg->pProgram->operationNbr
000b4ba9  logicalBarIndex < (122 >> 1)
000b4bc6  logical BarIndex %d is for Kernel
000b4be8  logicalBarIndex %d is for TD
000b4c05  Error! The bufIdx in the operation doesn't exist
000b4c36  Total OP bar=%d, curr=%d, bufIdx=%d
000b4c5a  Operation buffer, total=%d:
000b4c76  [%d] bufIdx=%d, barIdx=%d
000b4c90  Procedure Call buffer, total=%d:
000b4cb1  [%d] bufIdx=%d
000b4cc0  Kernel section: valid=%d bufIdx=%d
000b4ce3  Segment section: valid=%d  bufIdx=%d
000b4d08  found == 1
000b4d13  bufIndex %d: hwBarIndex_lo %d with value 0x%x, hwBarIndex_hi %d with value 0x%x
000b4d63  pCustomBar != __null
000b4d78  pCallProperty->nbrOfSegments == 1
000b4d9a  pCallProperty->bHasTidRewind == 0
000b4dbc  invalid signal event number=%d
000b4ddc  nbrEvents <= (16)
000b4dee  maxNumOfBar == 122
000b4e01  pOpItem->data.aneOp.nbrOfLocalbarSetup <= (122 >> 1)
000b4e36  freeUnusedL2SpillBufferPool numProc %zu numCurrL2SpillBufferPool %d
000b4e7a  Not all unused L2 spill buffer pools are freed sucessfully
000b4eb5  numPoolFreed == numPoolToFree
000b4ed3  Unexpected command 0x%x
000b4eeb  (pCmdHdr->id == CSNE_CMD_PROCEDURE_CALL_CACHE_REQUEST) || (pCmdHdr->id == CSNE_CMD_PROCEDURE_CALL_CACHE_REQUEST_WITH_CUSTOM_BARS) || (pCmdHdr->id == CSNE_CMD_PROCEDURE_CALL_CACHE_REQUEST_WITH_SHARED_EVENTS)
000b4fba  Normal CR entries (%d) exceeded maximum size (%d) with active shared events nbr (%ld)
000b5010  pProc->pCacheReqList->Size() <= ((8) + (8)) - (8) + pAneExeLoop->getActiveSharedEventsNbr()
000b506c  new shared event (%lld) while pSharedEventsRequestList is full
000b50ab  pAneExeLoop->getActiveSharedEventsNbr() <= (8)
000b50da  pCall->procedureId < pProg->pProgram->procNbr
000b5108  pCall->procedureId < pProcProp->tot
000b512c  myGeneral
000b5136  numOfInputInNetwork > 0 && numOfInputInNetwork <= (32)
000b516d  numOfOutputInNetwork > 0
000b5186  pChainingIOInfo
000b5196  pCall->bSingleUse == false
000b51b1  pChainingIOInfo->nbrOfOutputSets == pCall->nbrOfOutputBufferSets
000b51f2  pChainingIOInfo->inputs.totalNbrOfBuffers == pCall->totalNbrOfInputBuffers
000b523d  pChainingIOInfo->inputs.nbrOfBuffers == numOfInputInNetwork
000b5279  logicalBarIndex %d is for Text
000b5298  Data Chaining Intermeidate buffer at (%d) type mismatch (%d).
000b52d6  pDataChainingIntermediateBufferDesc->buffer.type == eCSneBufferDescriptorType_IntermediateBuffer
000b5337  logicalBarIndex %d is for intermediate
000b535e  pIoOutputBufferCnt != __null
000b537b  getCacheRequestIoBuffersNbr((void*)pCall) < 64
000b53aa  stats buffer outputBufferSetId (%d) in buffer descriptor exceeds nbrOfOutputBufferSets (%d) in command
000b5411  pDataChainingBufferDesc->outputBufferSetId < pCall->nbrOfOutputBufferSets
000b545b  pOutputSet->statsBuffer.bufferSize >= sizeof(sCAneStatsData) + sizeof(sEventDescriptors) + sizeof(sCAneStatsDataDbgEvent)
000b54d5  numOfStatsBuffer == 0
000b54eb  Data Chaining Input buffer at (%d) type mismatch (%d).
000b5522  pDataChainingBufferDesc->buffer.type == eCSneBufferDescriptorType_InputBuffer
000b5570  Fifo for input buffer index (%d) should be allocated already
000b55ad  pInputMap->pFifo != __null
000b55c8  bufIndex for new input buffer index (%d) should be invalid (%d)
000b5608  pInputMap->bufferIndex == 0xFFFFFFFF
000b562d  Fifo for new input buffer index (%d) should be NULL
000b5661  pInputMap->pFifo == __null
000b567c  number of input buffers in IO buffer list exceeds total number (%d)
000b56c0  ioInputBufferCnt < pChainingIOInfo->inputs.totalNbrOfBuffers
000b56fd  Data Chaining Output buffer at (%d) type mismatch (%d).
000b5735  pDataChainingBufferDesc->buffer.type == eCSneBufferDescriptorType_OutputBuffer
000b5784  output buffer outputBufferSetId (%d) in buffer descriptor exceeds nbrOfOutputBufferSets (%d) in command
000b57ec  number of output buffers in IO buffer list exceeds total number (%d)
000b5831  pIoOutputBufferCnt[pDataChainingBufferDesc->outputBufferSetId] < pOutputSet->nbrOfBuffers
000b588b  bufIndex for new output buffer desc should be invalid (%d)
000b58c6  pDataChainingOutBufDesc->bufferIndex == 0xFFFFFFFF
000b58f9  pDataChainingBufferDesc->buffer.type == eCSneBufferDescriptorType_IntermediateBuffer
000b594e  numOfIntermediateBuffer == 0
000b596b  Invalid data chaining IO buffer type %d
000b5993  (foundBufferMap & bufferMask) == 0
000b59b6  logicalBarIndex %d is for Segment
000b59d8  number of outputs (%d) in set (%d) does not match number of output in network (%d)
000b5a2b  pIoOutputBufferCnt[i] == numOfOutputInNetwork
000b5a59  No resource for new Cache request trigger.
000b5a84  Invalid L2 spill buffer index
000b5aa2  l2BufferIdx != (0xFF)
000b5ab8  pL2BufferIdx
000b5ac5  pFinishEvent
000b5ad2  bIsMultipleSegments
000b5ae6  pLastEnqueuedSegIdx
000b5aff  pPrefetchDsid
000b5b0d  bonded nid out of range: %d
000b5b2a  Custom Bar [%d] invalid fieldSizeInBits %d
000b5b55  pBarInfo->fieldSizeInBits <= 32 && pBarInfo->fieldSizeInBits != 0
000b5b97  Custom Bar [%d] invalid fieldBitOffset %d fieldSizeInBits %d
000b5bd4  pBarInfo->fieldBitOffset < 32 && (pBarInfo->fieldBitOffset + pBarInfo->fieldSizeInBits) <= 32
000b5c32  Custom Bar [%d] value %lld exceed size in bits %d
000b5c64  value < (1ULL << pBarInfo->fieldSizeInBits)
000b5c90  pBarInfo->fieldSizeInBits <= 64 && pBarInfo->fieldSizeInBits != 0
000b5cd2  pBarInfo->fieldBitOffset < 64 && (pBarInfo->fieldBitOffset + pBarInfo->fieldSizeInBits) <= 64
000b5d30  barBaseAddr
000b5d3c  sharedEventsActiveNbr < (8)
000b5d58  Invalid Command ID!
000b5d6c  pReq->dbgEventIdx != CIndexPool::invalidIndex
000b5d9a  fwPriority < (6)
000b5dab  hwqId < ((8) + (1))
000b5dbf  allocL2SpillBufferIdx failed
000b5ddc  index != -1
000b5de8  freeL2SpillBuffIdx returns invalid refCount (%d)
000b5e19  refCount >= 0
000b5e27  getL2SpillBufferAddr failed
000b5e43  addr != 0
000b5e4d  ./sne/aneEngine/common/CAneProgramHx.cpp
000b5e76  prog->procedureSection.valid
000b5e93  prog->procedureSection.size >= sizeof(sCSneCmdProgramProcedureSectionListHeader)
000b5ee4  prog->procedureSection.buffer
000b5f02  pProc->tot <= maxProcPerProgram
000b5f22  prog->procedureSection.size >= sizeof(sCSneCmdProgramProcedureSectionListHeader) + pProc->tot * sizeof(sCSneCmdProgramProcedureProperty)
000b5fab  getProcedureCallType(): invalid procedureId=%d, tot=%d
000b5fe3  procedureId < pProc->tot
000b5ffc  getProcedureCallType(): invalid procedureType=%d
000b602e  eCSneCmdProgramProcedureContentType_0 == pProcHdr->type || eCSneCmdProgramProcedureContentType_3 == pProcHdr->type
000b60a1  procedureType=%d, addr=0x%llx
000b60bf  procedureId < procNbr
000b60d5  Invalid procedure content type %d
000b60f7  pProcedureContent->type == eCSneCmdProgramProcedureContentType_3
000b6138  invalid segmentIdx %d segmentProp total %d
000b6163  segmentIdx < pSegmentProp->tot
000b6182  TD Num (%d) invalid for segmentIdx %d
000b61a8  pSegmentProp->prop[segmentIdx].numTdInSegment > 0 && pSegmentProp->prop[segmentIdx].numTdInSegment <= 0xFFFF
000b6215  mutexGlobal != (FFWMUTEX) 0
000b6231  __null != localProg
000b6245  refCount
000b624e  prog->operationSection.valid
000b626b  prog->operationSection.buffer
000b6289  prog->operationSection.size >= sizeof(sCSneCmdProgramOperationSectionListHeader)
000b62da  pOperation->tot <= maxOperationPerProgram
000b6304  prog->operationSection.size >= sizeof(sCSneCmdProgramOperationSectionListHeader) + pOperation->tot * sizeof(sCSneCmdProgramOperationProperty)
000b6392  Received an program whose has more than 1 operation : %d
000b63cb  pProcItem->nbrOfEventMask == 1
000b63ea  procedure[%d] operation index %d exceeds total nbr %d
000b6420  procInfo[i].operationIndex < operationNbr
000b644a  __null != pTdProp
000b645c  local program not valid
000b6474  localProg->valid == true
000b648d  pbuf->size != 0
000b649d  CAneProgramHx.cpp
000b64af  localProg->textSectionBuf != __null
000b64d3  Map genericSection failed (addr:0x%llx, size:0x%llx)
000b6509  Map textPropSection failed (addr:0x%llx, size:0x%llx)
000b6540  Map operationSection failed (addr:0x%llx, size:0x%llx)
000b6578  Map procedureSection failed (addr:0x%llx, size:0x%llx)
000b65b0  Map kernelPropSection failed (addr:0x%llx, size:0x%llx)
000b65e9  Map procPropSection failed (addr:0x%llx, size:0x%llx)
000b6620  Unmap genericSection failed (addr:0x%llx, size:0x%llx)
000b6658  Unmap textPropSection failed (addr:0x%llx, size:0x%llx)
000b6691  Unmap operationSection failed (addr:0x%llx, size:0x%llx)
000b66cb  Unmap procedureSection failed (addr:0x%llx, size:0x%llx)
000b6705  Unmap kernelPropSection failed (addr:0x%llx, size:0x%llx)
000b6740  Unmap procPropSection failed (addr:0x%llx, size:0x%llx)
000b6779  Not supported
000b678c  ./program/procedure_%d/cmdprocedurecallcustombars.bin
000b67c2  ./program/procedure_%d/iobuf%d-%d-%d.bin
000b67eb  ./td_%d/ane_reg_%d-%d-%d.bin
000b6808  ./td_%d/kmem_%d-%d-%d_%d.bin
000b6825  ./td_%d/l2_%d-%d-%d.bin
000b683d  ./td_%d/cmdprocedurecallcustombars.bin
000b6864  ./td_%d/iobuf%d-%d.bin
000b687b  ./sne/aneEngine/common/CAneProgramCheckerHx.cpp
000b68ab  section
000b68b3  pSegmentPropSection
000b68c7  pDescriptor
000b68d3  pOpSection
000b68de  pAneOp
000b68e8  generic->buffers[j].valid
000b6902  program
000b690a  program->operationSection.valid
000b692a  operation
000b6934  program->genericSection.valid
000b6952  generic->totalBufferNbr > 0
000b696e  program->textSection.valid
000b6989  program->textSection.size
000b69a3  program->kernelSection.size
000b69bf  CAneProgramCheckerHx.cpp
000b69d8  Map textSection failed (addr:0x%llx, size:0x%llx)
000b6a0b  Unmap textSection failed (addr:0x%llx, size:0x%llx)
000b6a40  generic->totalBufferNbr
000b6a58  ./sne/aneEngine/common/CAneEngineExeLoopHx.cpp
000b6a87  pReqPool
000b6a90  poolMutex != (FFWMUTEX)0
000b6aa9  pFwPriorityQueue
000b6aba  pJobQueue
000b6ac4  nidMutex != (FFWMUTEX)0
000b6adc  mpNetworkDescPool_base
000b6af3  intHandler
000b6afe  dbgQintHandler
000b6b0d  tqStopintHandler
000b6b1e  mcwDoneIntHandler
000b6b30  mcwErrorIntHandler
000b6b43  nonsec2SecHandler != 0
000b6b5a  sec2NonsecHandler != 0
000b6b71  cacheRequest[cacheReqIdx].pDelayTriggerTimer != __null
000b6ba8  cacheReqIdxMutex != (FFWMUTEX)0
000b6bc8  cacheInputInfoPoolMutex != (FFWMUTEX)0
000b6bef  cacheInputListIdxMutex != (FFWMUTEX)0
000b6c15  mySyncSema != (SEMA)0
000b6c2b  dbgQIntSema != (SEMA)0
000b6c42  tqStopIntSema != (SEMA)0
000b6c5b  nonsec2SecSema != (SEMA)0
000b6c75  sec2NonsecSema != (SEMA)0
000b6c8f  myTimeoutSema != (SEMA)0
000b6ca8  dataChainSema != (SEMA)0
000b6cc1  mcwIntSema != (SEMA)0
000b6cd7  cacheRequest[cacheReqIdx].delayTriggerTimerSema != (SEMA)0
000b6d12  semaIndex <= sizeof(semaArray)/sizeof(semaArray[0])
000b6d51  pFrameDoneTimer != 0
000b6d66  pPC != __null
000b6d74  SneCEDrv
000b6d7d  __null != pSneCEDrv
000b6d91  SneTMDrvHx
000b6d9c  __null != pSneTMDrv
000b6db0  SneItqDrvHx
000b6dbc  __null != pSneItqDrv
000b6dd1  SneMCWDrv
000b6ddb  __null != pSneMCWDrv
000b6e09  scheduleInfo
000b6e16  mDummyNetworkPhysAddr != 0
000b6e31  pSneDrv == __null
000b6e43  isAllIdle == true
000b6e55  Cannot find nid %llu with tid %llu event %llu
000b6e83  foundIndex < ((8) + (1))
000b6e9c  slot < 2
000b6ea5  Invalid preapred finish event
000b6ec3  pReq->request.pFinishEvent != __null
000b6ee8  0 == pReq->request.bFinishEventSent
000b6f0c  eventCount <= 64
000b6f1d  (nid >= ((2))) && (nid < 64)
000b6f3a  Unexpected call. bIsExclaveSupported %d, bEnableSecureModeHandshake %d
000b6f81  pThis->bIsExclaveSupported && pThis->bEnableSecureModeHandshake
000b6fc1  DebugInfo event %d nid %d tid %d irq %d
000b6fe9  Cannot find nid %d with tid %d event %d
000b7011  matchAneReqNid(&reqRunning[foundIndex][slot], info.event.info.nid)
000b7054  Found Matched Priority %d Slot %d
000b7076  nonSec2SecCnt=%d, sec2NonSecCnt=%d
000b709a  request nonSec -> Sec received: currState=%d
000b70c8  request Sec -> NonSec received: currState=%d
000b70f6  Debug Queue Interrupt trigger
000b7114  Timeout Interrupt trigger
000b712e  should not have switched out request when ANE is idle
000b7164  switchedOutReqStats.numSwitchedOut == 0
000b71a7  switchedOutReqStats.saveCnt == (switchedOutReqStats.handleAbortCnt + switchedOutReqStats.handleFinishCnt + switchedOutReqStats.handleContextSwitchCnt)
000b723e  [EventInfo] event %d nid %d tid %d irq %d abort %d q_dummy %d TS %lld
000b7285  [31m"Ignore aborted start event queue %d slot %d (nid %d)"
000b72c5  false == pReq->request.bIsLastSegPushed
000b72ed  false == pReq->request.bIsLastSegStarted
000b7316  hw branching got too many start events
000b733e  pReq->request.hwBrNbrOfStartEvents < 2
000b7365  Event 5 TID %d TQ %d
000b737a  Event 6 TID %d TQ C %d P %d Idle %d
000b739e  numReqAborting[%d] (%d) should not be negative
000b73cd  numReqAborting[foundIndex] >= 0
000b73ed      Found Matched Priority Q[%d]S[%d]
000b7413  Unexpected
000b741e  info.userData.f.b_queue_dummy_network == 1
000b7449  CR 0x%llx is not in correct state %d
000b746e  pCacheReq->state == ANE_DATA_CHAINING_CACHE_REQUEST_INVALIDATING
000b74af  Program %d Process %d not in correct state!
000b74db  CAneProgramManager::Instance()->isProcessTerminating(auxInfo->programId, auxInfo->processId) == true
000b7540  Rewinded flag segment finish event, NID %d Q[%d]S[%d] at %lld
000b757e  unexpected usage for nidSecondary (%d), bIsMultipleSegments %d, bIsBondedNetwork %d
000b75d2  pReq->request.bIsMultipleSegments && !pReq->request.bIsBondedNetwork
000b7617  Debug Queue not empty!
000b762e  pCacheReq->state != ANE_DATA_CHAINING_CACHE_REQUEST_AVAILABLE
000b766c  should not receive any event in the PAUSE state: currState=%d
000b76aa  (nidStopTq > 0) && (nidStopTq < 64)
000b76ce  Cannot find nid %d
000b76e1  MCW interrupt for dsid %d, irq %d at %lld
000b770b  mcacheDsidPending[dsid - (124)] > 0
000b772f  send MCW command for dsid %d must succeed here
000b775e  CAneProgramManager::Instance()->isProcessRunning(auxInfo->programId, auxInfo->processId) == true
000b77bf  bUseNidSecondary set from 0 to 1 after first segment
000b77f4  pReq->isLastTDCompleted == 0
000b7811  pReq->isLastTDFetched == 0
000b782c  pReq->isAborting == 0
000b7842  pReq->bMultipleSegmentAborted == 0
000b7865  ITQ is not enabled
000b7878  pSneItqDrv != __null
000b788d  fwPriorityQ[%d] has %s
000b78a9  no req
000b78b0  pReqTemp == pReq
000b78c1  slotNext != -1
000b78d0  AbortTQ() for TQ(%d) failed after waiting for more than 2 sec
000b790f  [31m"[ABORT] queue %d reqMatched ? %d"
000b793b  jobId < maxJobNbr
000b794d  foundQueue == ((8) + (1)) || foundQueue == i
000b797a  abort bonded not supported
000b7995  pReq->request.bIsBondedNetwork == 0
000b79ba  [34m"reqMatched %d foundQueue %d slotMatched %d"
000b79f0  Abort HW is false only for AFPP workloads
000b7a1a  CAneProgramManager::Instance()->isHwqIdOfAfpp(foundQueue) == true
000b7a5c  foundQueue == ((8) + (1))
000b7a76  pCmd->cmdId < eExeLoopCmdNum
000b7a93  [WRN] Exeloop cmd %d latency %dus
000b7ab5  pCmd->body.pCheckIdle
000b7acb  ANE HW Dynamic Power Gating is disabled
000b7af3  Reenable and power down ANE HW if possible
000b7b1e  ANE HW Power is still on
000b7b37  TDBase to P6 failed
000b7b4b  %s [userId %d jobId %d fwPriority %d hwqId %d tqId %d] queueId %d
000b7b8e  [31m"ExeLoop Request Received"
000b7bb3  [31m"Executed the Server Request"
000b7bda  slot != -1
000b7be6  [31m"hwqId %d Slot %d"
000b7c03  [31m"Cached the Server Request to Priority queue"
000b7c3a  0 == result
000b7c47  [31m"Cached the Server Request to Job queue"
000b7c79  aneSecurePhase == false
000b7c91  secureMode Phase START
000b7ca8  aneSecurePhase == true
000b7cbf  secureMode Phase STOP
000b7cd5  EXCLAVE_MODE_PHASE_START
000b7cee  aneExclavePhase == false
000b7d07  aneExclavePhase == true
000b7d1f  EXCLAVE_MODE_PHASE_STOP
000b7d37  SwitchExclaveMode() invalid phase %d
000b7d5c  queueId >= 0 && queueId < jobQCount
000b7d80  request
000b7d88  pJobQueueId != __null
000b7d9e  Allocate user request fail
000b7dba  phase == SECURE_MODE_PHASE_START || phase == SECURE_MODE_PHASE_STOP
000b7dfe  ANE pre powering up, isAllIdle: %d
000b7e21  ANE powering up for job submission, isAllIdle: %d
000b7e53  ane in wrong power state: %d
000b7e70  pPC->anePowerState() == ANE_POWER_STATE_ALL_OFF
000b7ea0  pPC->anePowerState() == (ANE_POWER_STATE_ALL_OFF + 1)
000b7ed6  check the cache q: idx=%2d, pending_job_cnt=%ld
000b7f06  check HW slot: queue_idx=%2d, slot_status: [0]=%d, [1]=%d
000b7f40  isAneIdle return true
000b7f56  my hwq = 0x%x
000b7f65  my hwq is free
000b7f75  my hwq is full
000b7f85  my hwq: slot %d has more segments to go
000b7fae  my hwq: slot %d has more hw branching segments to go
000b7fe4  my hwq is waiting for dummy network to complete
000b8014  my hwq is free
000b8023  paired hwq = 0x%x
000b8036  paired hwq is waiting for dummy network to complete
000b806a  paired hwq is free
000b807e  paired hwq is full
000b8092  paired hwq: slot %d is waiting to start
000b80bb  paired hwq: slot %d has more segments to go
000b80e8  paired hwq: slot %d: same process: no enough L2 spill buf
000b8123  paired hwq is free
000b8136  [isHWReady] my hwq has more req to start!
000b8160  [isHWReady] paired hwq has more req to start!
000b818e  [isHWReady] fw priority queue is not empty!
000b81ba  [isHWReady] job queue is not empty!
000b81de  [isHWReady] schedule info is not available!
000b820a  [isHWReady] switching to the secure mode: state=%d
000b823d  [isHWReady] ready!
000b8250  Value for TM_LTH register must be non zero
000b827b  regValue != 0
000b8289  [ANE_EVENT_CONTEXT_SWITCH_IN]: tid=%3d, nid=%3d, prevTQ=%3d, progId=%3d, procId=%3d, currTQ=%d, timeStamp=%lld
000b82f9  [ANE_TM_EVENT_START]:       tid=%3d, nid=%3d, progId=%3d, procId=%3d, currTQ=%d, timeStamp=%lld
000b835a  [ANE_TM_EVENT_FINISH]:      tid=%3d, nid=%3d, progId=%3d, procId=%3d, currTQ=%d, timeStamp=%lld
000b83bb  CAneEngineExeLoopHx.cpp
000b83d3  pNetworkDesc
000b83e0  (idx < 64) || (10 && idx >= 245 && idx < (245 + 10))
000b8415  dramLogHdr (0x%llx) must be 64 byte aligned
000b8441  ((uint64_t)pEventLogBase & 0x3F) == 0
000b8467  mcw have interrupts waiting to be handled first
000b8497  Pending deprioritize commands present for dsid[%d] %d
000b84cd  Send deprioritize command for dsid[%d] to MCW returns %d
000b8506  Direct path should be executed when everything is idle, allocated slot should be 0
000b8559  slot == 0
000b8563  Low latency path doesn't support multiple segment for now.
000b859e  Unexpected L2 spill buffer mapping[%d] = %d in direct path
000b85d9  (call->barInfo[i].value >= (124)) && (call->barInfo[i].value <= (127))
000b8620  Invalid prepared finish event for direct path
000b864e  Call Procedure command  (Prog %d, Process %d, procedure%d CustomBars %d) 
000b8698  %s [userId %d jobId %d priority %d] queueId %d
000b86c7  pReq->fwPriority < ((8) + (1))
000b86e7  [31m"Priority %d Slot %d"
000b8706  No new cache request should be created when bDisableCacheRequestHandling is set
000b8756  bDisableCacheRequestHandling == false
000b877c  NULL pointer passed pJobQueueId %p pNid %p pRequest %p pChainingIOInfo %p
000b87c6  (pJobQueueId != __null) && (pNid != __null) && (pRequest != __null) && (pChainingIOInfo != __null)
000b8829  pCmdHdr->id == CSNE_CMD_PROCEDURE_CALL_CACHE_REQUEST_WITH_CUSTOM_BARS || pCmdHdr->id == CSNE_CMD_PROCEDURE_CALL_CACHE_REQUEST_WITH_SHARED_EVENTS
000b88ba  cacheReqIdx != CIndexPool::invalidIndex
000b88e2  cacheReqIdx (%d) in wrong state %d
000b8905  pCacheReq->state == ANE_DATA_CHAINING_CACHE_REQUEST_AVAILABLE
000b8943  pCall->cacheHandler
000b8957  groupCacheReqIdx < ((8) + (8))
000b8976  bGroupRequest set with invalid group cacheHandler %llx expect %llx.
000b89ba  pCall->cacheHandler == cacheRequest[groupCacheReqIdx].cacheHandler
000b89fd  cacheRequest[groupCacheReqIdx].pGroupInfo != __null
000b8a31  cacheRequest[groupCacheReqIdx].pGroupInfo == __null
000b8a65  pGroupInfo->isActive == false
000b8a83  pCall->bSingleUse
000b8a95  pCall->nbrOfWaitEvents + pCall->nbrOfSignalEvents > 0
000b8acb  Current pSharedEventsRequestList entries (%d), maximum size (%d), no place for more
000b8b1f  pSharedEventsRequestList->Size() < (8)
000b8b46  pRpc != __null
000b8b55  Create start event message for single use cache request failed
000b8b94  pAneReq->request.pStartEvent != __null
000b8bbb  Create finish event message for single use cache request failed
000b8bfb  pAneReq->request.pFinishEvent != __null
000b8c23  Allocate ane request fail
000b8c3d  cacheHandler is 0
000b8c4f  ane request invalid in cache request
000b8c74  pCacheReq->pAneRequest != __null
000b8c95  cacheHandler (0x%llx) does not match the one stored in cache request (0x%llx)
000b8ce3  pCacheReq->cacheHandler == cacheHandler
000b8d0b  invalidate in ExeLoop only valid for Single Use cache request
000b8d49  pCacheReq->bSingleUse
000b8d5f  delay trigger pool for data chaining still have outstanding (%zu) entries
000b8da9  pCacheReq->pDelayTriggerPool->Outstanding() == 0
000b8dda  Single use cache request only has one output set (%d)
000b8e10  pChainingIOInfo->nbrOfOutputSets == 1
000b8e36  Untriggered Single use cache request must not be pushed to HW
000b8e74  pCacheReq->bSingleUseQueuedToHW == 0
000b8e99  pStartEvent should not be used for untriggered Single use cache request
000b8ee1  pCacheReq->pAneRequest->request.pStartEvent != __null
000b8f17  pFinishEvent should not be used for untriggered Single use cache request
000b8f60  pCacheReq->pAneRequest->request.pFinishEvent != __null
000b8f97  NID should not be used for untriggered Single use cache request
000b8fd7  pCacheReq->pAneRequest->nid != (0xFFFFFFFF)
000b9003  Pushed to HW Single use cache request must have been triggered
000b9042  pCacheReq->bSingleUseTriggered == 1
000b9066  pStartEvent should be NULL for Single use cache request pushed to HW
000b90ab  pCacheReq->pAneRequest->request.pStartEvent == __null
000b90e1  pFinishEvent should be NULL for Single use cache request pushed to HW
000b9127  pCacheReq->pAneRequest->request.pFinishEvent == __null
000b915e  NID should be invalid for Single use cache request pushed to HW
000b919e  pCacheReq->pAneRequest->nid == (0xFFFFFFFF)
000b91ca  pCacheReq->pGroupInfo
000b91e0  pCacheReq->pGroupInfo->isActive
000b9200  cacheRequest[groupCacheReqIdx].cacheHandler == pCacheReq->pGroupInfo->groupCacheHandler
000b9258  cacheRequest[groupCacheReqIdx].bGroupCacheRequest == true
000b9292  cache request index (%d) in wrong state %d
000b92bd  pInputInfoPool
000b92cc  pInputInfo
000b92d7  (idx >= 0) && (idx < maxCacheRequest)
000b92fd  pCacheReq->pGroupInfo != __null
000b931d  0 != pCacheReq->pGroupInfo->subCacheHandlerArray[i]
000b9351  Trigger command for cacheHandler 0x%llx from src 0x%x with %d input buffers
000b939d  pTriggerCmd->cacheHandler != 0
000b93bc  cache request index (%d) with handler 0x%llx in wrong state %d
000b93fb  false == pCacheReq->bSingleUse
000b941a  sub cache request index (%d) with handler 0x%llx in wrong state %d
000b945d  pTriggerCmd->bGroup
000b9471  pTriggerCmd->cacheHandler == pGroupCacheReq->pGroupInfo->groupCacheHandler
000b94bc  CR 0x%llx single use already triggered
000b94e3  false == pCacheReq->bSingleUseTriggered
000b950c  [31m"Cached the request to Priority queue"
000b953d  [31m"Cached the Request to Job queue"
000b9568  Drop trigger for cacheHandler 0x%llx in state (%d) after disable handling
000b95b2  execTimestamp (%lld) is not valid compared to last trigger exec timestamp (%lld)
000b9603  (pTriggerCmd->execTimestamp > pGroupCacheReq->lastTriggerExecTimestamp) || ((pGroupCacheReq->lastTriggerExecTimestamp - pTriggerCmd->execTimestamp) & (0xF000000000000000LLU))
000b96b2  No more delay trigger entry for cache request (%d)
000b96e5  pDelayTriggerCmd
000b96f6  prepare timer for delayed trigger command for cache request idx (%d)
000b973b  pGroupCacheReq->cacheHandler == pTriggerCmd->cacheHandler
000b9775  number of input buffers (%d) in trigger command exceeds limit (%d)
000b97b8  pTriggerCmd->nbrOfInputBuffers <= (16)
000b97df  SC ptdIndex for L stream mismatch 0x%x vs 0x%x
000b980e  pCacheReqDataScInfo->ptdIndex[0] == pTriggerScInfo->ptdIndex[0]
000b984e  SC surfaceId for L stream mismatch 0x%x vs 0x%x
000b987e  pCacheReqDataScInfo->outputSurfaceId[0] == pTriggerScInfo->outputSurfaceId[0]
000b98cc  SC ptdIndex for R stream mismatch 0x%x vs 0x%x
000b98fb  pCacheReqDataScInfo->ptdIndex[1] == pTriggerScInfo->ptdIndex[1]
000b993b  SC surfaceId for R stream mismatch 0x%x vs 0x%x
000b996b  pCacheReqDataScInfo->outputSurfaceId[1] == pTriggerScInfo->outputSurfaceId[1]
000b99b9  input %d surfaceId 0x%x offset 0x%llx
000b99df  could not find input buffer with surface Id 0x%x with offset 0x%llx
000b9a23  inputReadyMap (%d) buffer index %d does not match with buffer descriptor %d
000b9a6f  pInputs->pReadyMap[inputMapIndex].bufferIndex == pBufDesc->bufferIndex
000b9ab6  Input list is not empty for reporting input overflow
000b9aeb  pInputs->pInfoList[inputOverflowListIdx]->Size() == 0
000b9b21  put trigger input into fifo must succeed here
000b9b4f  Trigger input dropped for CR 0x%llx, triggerCnt %d, inputOverflowCnt %d
000b9b97  Input list is not empty for new request
000b9bbf  pInputs->pInfoList[inputInfoListIdx]->Size() == 0
000b9bf1  input SurfaceId [0x%x] offset [0x%llx] userData type [%d], value [%lld]
000b9c39  [Secure mode] trigger dropped for CR 0x%llx, triggerCnt %d, droppedInSecureModeCnt %d
000b9c8f  outputBufferSetId (%d) exceeds number of output sets (%d)
000b9cc9  outputSetId < pIoInfo->nbrOfOutputSets
000b9cf1  [31m"Executed Cache Request Idx %d"
000b9d1b  [31m"[WARNING] HW is not ready for data chaining request"
000b9d5a  nextOutputSetId < pIoInfo->nbrOfOutputSets
000b9d85  pInputs->pReadyMap[i].bufferIndex == pBufDesc->bufferIndex
000b9dc0  No output buffers are ready for CR 0x%llx, triggerCnt %d, outputUnderflowCnt %d
000b9e10  Trigger command for cacheHandler 0x%llx from src 0x%x with %d input handled in ISR
000b9e63  sharedEventsEnabled == true
000b9e7f  pSharedEventsRequestList != __null
000b9ea2  Shared events trigger dropped. cacheHandler 0x%llx not in use
000b9ee1  pCacheReq->state == ANE_DATA_CHAINING_CACHE_REQUEST_IN_USE
000b9f1c  pCacheReq->waitEventCnt == pCacheReq->nbrOfWaitEvents && pCacheReq->bSingleUseTriggered == 0
000b9f79  sharedEventsPendingCnt >= 0
000b9f95  pThis->sharedEventsEnabled == true
000b9fb8  pThis->pSharedEventsRequestList != __null
000b9fe2  Doorbell ring with no shared events waiting!
000ba010  cacheHandler (0x%llx) in wrong state (%d) for trigger. trigger dropped
000ba057  process (%d) for CR (0x%llx) is terminating. trigger dropped
000ba094  eventIdx < pThis->sharedEventsTableSize
000ba0bc  pSharedEventsRequestList->RemoveByEntry((void*)cacheHandler) != 0
000ba0fe  shared events ISR triggered without any wait event updated!
000ba13b  Recycle output buffer command for cacheHandler 0x%llx for output set %d
000ba183  pRecycleCmd->cacheHandler != 0
000ba1a2  Drop recycle output for cacheHandler 0x%llx in state (%d) after disable handling
000ba1f3  pCacheReq->cacheHandler == pRecycleCmd->cacheHandler
000ba228  cache request index (%d) with handler 0x%llx is single use, does not expect recycle output command
000ba28b  pCacheReq->bSingleUse == 0
000ba2a6  pActiveCacheReq->cacheHandler == pCacheReq->pGroupInfo->activeSubCacheHandler
000ba2f4  pActiveCacheReq->state == ANE_DATA_CHAINING_CACHE_REQUEST_IN_USE
000ba335  outputSet (%d) is in wrong state %d
000ba359  (pIoInfo->pOutputSets[outputSetId].state != ANE_DATA_CHAINING_OUTPUT_SET_AVAILABLE) && (pIoInfo->pOutputSets[outputSetId].state != ANE_DATA_CHAINING_OUTPUT_SET_IN_EXECUTION)
000ba407  group cacheHandler is 0
000ba41f  pSetActiveCmd->groupCacheHandler != 0
000ba445  active cacheHandler is 0
000ba45e  pSetActiveCmd->activeCacheHandler != 0
000ba485  group cache request index (%d) with handler 0x%llx in wrong state %d
000ba4ca  pGroupCacheReq->state == ANE_DATA_CHAINING_CACHE_REQUEST_IN_USE
000ba50a  group cacheHandler (0x%llx) does not match the one stored in cache request (0x%llx)
000ba55e  pGroupCacheReq->cacheHandler == pSetActiveCmd->groupCacheHandler
000ba59f  invalid group 0x%llx active 0x%llx cacheHandler
000ba5cf  pSetActiveCmd->groupCacheHandler == pSetActiveCmd->activeCacheHandler
000ba615  active cache request index (%d) with handler 0x%llx in wrong state %d
000ba65b  active cacheHandler (0x%llx) does not match the one stored in cache request (0x%llx)
000ba6b0  pActiveCacheReq->cacheHandler == pSetActiveCmd->activeCacheHandler
000ba6f3  pGroupCacheReq->pGroupInfo != __null
000ba718  pGroupCacheReq->pGroupInfo == pActiveCacheReq->pGroupInfo
000ba752  pGroupCacheReq->pGroupInfo->isActive
000ba777  cache request must have pending trigger cmd in fifo
000ba7ab  pCacheReq->pDelayTriggerFifo->Size()
000ba7d0  Handle delayed trigger command for cache request idx (%d)
000ba80a  exec timestamp %lld at %lld
000ba826  prepare timer for next delayed trigger command for cache request idx (%d)
000ba870  No more pending delayed trigger command for cache request idx (%d).  Stopping timer
000ba8c4  ********* CACHE REQUEST INDEX %2d *********
000ba8f1  cacheHandler: 0x%llx
000ba907  -- Engine Request -------------------------
000ba934  programId: %d
000ba943  processId: %d
000ba952  procedureId: %d
000ba963  priority: %d
000ba971  cache request index (%d) is not used
000ba997  ANE not in non-secure mode
000ba9b2  secModeStat == 0
000ba9c3  switchToIsolatedMode failed in thread (interrupt disabled)
000ba9fe  switchToIsolatedMode failed in ISR
000baa21  switchToIsolatedMode failed in thread (interrupt enabled)
000baa5b  TQ[%d] state 0x%x
000baa6d  Num of switched out requests exceeded numbrt of TQs
000baaa1  switchedOutReqStats.numSwitchedOut <= ((8) + (1))
000baad3  Switched out TQ[%d][%d] req 0x%llx
000baaf6  Saved SO request to %d with 0x%llx DSID %d 
000bab22  Switched out request not saved
000bab41  bSaved == true
000bab50  Clear switched out req from %d
000bab6f  handleSwitchedOutReq for aborted req 0x%llx
000bab9b  handleSwitchedOutReq for finished req 0x%llx
000babc8  handleSwitchedOutReq from TQ %d req 0x%llx
000babf3  Switched out request is NULL!
000bac11  pSwitchedOutReq != __null
000bac2b  Switched out request does not have mcache DSID
000bac5a  pSwitchedOutReq->request.mcacheDsid != (0xFF)
000bac88  pSneTMDrv
000bac92  index < ((8) + (1))
000baca6  finishEvent < ANE_TM_EVENT_MAX
000bacc5  queueId < priorityQCount
000bacde  pushHWQ: hwqId=%d jobId=%d isMultiSeg=%d segId=%d isRewind=%d
000bad1d  isLast=%d nid=%d,%d using=%d
000bad3b  pushHWQ: hwqId=%d jobId=%d isMultiSeg=%d nid=%d
000bad6c  pReq->nbrOfExecuteOrder
000bad84  pReq->pExecuteOrderIdxList
000bad9f  scheduleInfo[queueId].sche_fwPriority != (uint32_t(-1))
000badd7  scheduleInfo[queueId].count
000badf3  RemoveScheduleInfo: %d[userId %d jobId %d priority %d] count %d
000bae33  (1 << slot) & reqRunningStatus[index]
000bae59  nid != CIndexPool::invalidIndex
000bae79  userId == pReq->userId
000bae90  queueId < jobQCount
000baea4  pReq->userId == userId
000baebb  pReq->jobId == jobId
000baed0  scheduleInfo[queueId].count == 0
000baef1  scheduleInfo[queueId].sche_fwPriority == pReq->fwPriority
000baf2b  AddScheduleInfo: %d[userId %d jobId %d priority %d] count %d
000baf68  AvailableScheduleInfo: %d[userId %d jobId %d priority %d] priority %d count %d
000bafb7  priorityId < maxPriorityNbr
000bafd9  sharedEventsActiveNbr > 0
000baff3  WRN: ffwTimerRestart() called without start from %s
000bb028  TQ[%d] exceeded max TQ num
000bb043  TQ[%d] should have request running
000bb066  reqRunningStatus[index] != 0
000bb083  TQ[%d][0] should have enqueue Ts
000bb0a4  reqRunning[index][0].request.hwEnqueueTimestamp
000bb0d4  TQ[%d][1] should have enqueue Ts
000bb0f5  reqRunning[index][1].request.hwEnqueueTimestamp
000bb125  ./sne/aneEngine/common/CAneEngineExeLoopHxFSMDef.cpp
000bb15a  FSMSwitchSecure() TQEn should be 0
000bb17d  !pExeLoop->pSneTMDrv->getTQEn()
000bb19d  switched from Iso -> Sec, ANE goes to PAUSE
000bb1ca  switched from NonSec -> Sec, ANE goes to PAUSE
000bb1fa  FSMSwitchNonSecure() TQEn should be 0
000bb220  switched from Sec, ANE goes to RUN
000bb244  ./sne/aneEngine/exeLoop/CAneEngineExeLoopH18g.cpp
000bb276  tmSyncErrIntHandler
000bb28a  tmSyncErrIntSema != (SEMA)0
000bb2a6  __null != pMsgBox
000bb2b8  pThis->pMsgBox != __null
000bb2d1  targetIdx (%zu) exceed shared event agent num (%d)
000bb304  targetIdx < MAX_ANE_SHARED_EVENT_TYPE_NUM
000bb32e  __null != pMailbox
000bb341  cacheReqIdx (%d) out of range
000bb35f  (cacheReqIdx >=0) && (cacheReqIdx < maxCacheRequest)
000bb394  /Library/Caches/com.apple.xbs/96BD7295-2E6C-40F1-901E-B8E997EFC517/TemporaryDirectory.0PDvHS/Sources/AppleH16AneFW/sne/ssi/src/common/msgQ.c
000bb421  false == inited
000bb431  mutexId_Invalid != msgQLock
000bb44d  mutexId_Invalid!= msgQCb[i].lock
000bb46e  semaId_Invalid != msgQCb[i].seamIdSend
000bb495  semaId_Invalid != msgQCb[i].seamIdRecv
000bb4bc  NULL != msgQCb[i].pBuffer
000bb4d6  msgQ < MAXMSGQNBR
000bb4e8  true == msgQCb[msgQ].used
000bb502  msgSize <= msgQCb[msgQ].width
000bb520  msgQCb[msgQ].depth >= msgQCb[msgQ].wr
000bb546  nextWr != msgQCb[msgQ].rd
000bb560  *pMsgSize >= msgQCb[msgQ].width
000bb580  msgQCb[msgQ].depth >= msgQCb[msgQ].rd
000bb5a6  msgQCb[msgQ].rd != msgQCb[msgQ].wr
000bb5c9  /Library/Caches/com.apple.xbs/96BD7295-2E6C-40F1-901E-B8E997EFC517/TemporaryDirectory.0PDvHS/Sources/AppleH16AneFW/sne/ssi/src/rtxc/CWorkTask.cpp
000bb65b  %s/%d assertion failed: %s
000bb677  msgQId_Invalid != msgQ
000bb68e  msgQId_Invalid != intQ
000bb6a5  _workloop_thread != EISP_THREAD_INVALID
000bb6cd  NULL != pCore
000bb6db  myWork
000bb6e2  ./sne/ssi/src/rtxc/CWorkTaskCore.cpp
000bb707  __null != pWorkIn
000bb719  %s: Start the initialization! (%p)
000bb73d  %s: Created! (%p)
000bb750  semaProcDone != (SEMA)0
000bb768  DCNPipeIn
000bb772  __null != pRequest
000bb785  size == sizeof(sReq)
000bb79a  WL: Finished all message handler
000bb7bc  WL: Finished all interrupt handler
000bb7e0  WorkTask Core Finished One Request @ %f ms
000bb80c  ./sne/ssi/src/rtxc/CWorkTaskCoreCmd.cpp
000bb834  ./sne/ssi/src/rtxc/CWorkThreadInfo.cpp
000bb85b  __null == pInstance
000bb86f  ((mutexId_t) -1) != threadLock
000bb88e  this == pInstance
000bb8a0  __null != pThread
000bb8b2  /Library/Caches/com.apple.xbs/96BD7295-2E6C-40F1-901E-B8E997EFC517/TemporaryDirectory.0PDvHS/Sources/AppleH16AneFW/sne/ssi/src/rtxc/memObj.cpp
000bb941  mutexId_Invalid != mutex
000bb95a  memObj.cpp
000bb965  /Library/Caches/com.apple.xbs/96BD7295-2E6C-40F1-901E-B8E997EFC517/TemporaryDirectory.0PDvHS/Sources/AppleH16AneFW/sne/ssi/src/rtxc/mutex.cpp
000bb9f3  rc == FFW_OK
000bba00  /Library/Caches/com.apple.xbs/96BD7295-2E6C-40F1-901E-B8E997EFC517/TemporaryDirectory.0PDvHS/Sources/AppleH16AneFW/sne/ssi/src/rtxc/sema.cpp
000bba8d  0 == inited
000bba99  mutexId_Invalid != semaLock
000bbab5  1 == inited
000bbac1  (SEMA)0 != sema[i].sema
000bbad9  semaId < MAXSEMANBR
000bbaed  sema[semaId].isUsed
000bbb01  MyThread
000bbb0a  /Library/Caches/com.apple.xbs/96BD7295-2E6C-40F1-901E-B8E997EFC517/TemporaryDirectory.0PDvHS/Sources/AppleH16AneFW/sne/ssi/src/common/CEispInterruptBuffer.cpp
000bbba9  NULL != pNodeBuf
000bbbba  ./sne/server/aneServer/CAneServer.cpp
000bbbe0  __null == instance
000bbbf3  serialPollTimer != 0
000bbc08  serialPortPoolTimeOut != (SEMA)0
000bbc29  CAneServerCmdPool
000bbc52  CAneServerPipe
000bbc61  CAneServerPipeCb
000bbc72  %s: Created! (%p)
000bbc84  __null != instance
000bbc97  progProcInfo[i].progId != ECSneCmdId_Invalid
000bbcc4  progProcInfo[i].procId != -1
000bbce1  CAneServer.cpp
000bbcf0  CmdAFPPLoad starting %d
000bbd0d  insize == sizeof(*pCmd)
000bbd25  AFPP has been loaded. reload is not allowed
000bbd52  pAneProgramDesc2 != __null
000bbd6d  CmdAFPPUnload starting %d
000bbd87  local copy of pAneProgramDesc2 was not allocated
000bbdb8  AFPP unload AFPPBuf(buffer 0x%llx, size 0x%llx) is different to the pCmd (buffer 0x%llx, size 0x%llx)
000bbe1f  AFPP unload is not allowed after program setup done
000bbe54  AFPP is not loaded. Should not call unload AFPP here.Please check the caller
000bbea2  CmdProgramSetup starting %d
000bbebe  !programSetupDone
000bbed0  __null != CDMediaBusManager::Instance()
000bbef8  !sapRegistered
000bbf07  builtinProgramId < maxProgramServerSupported
000bbf34  pProgDesc
000bbf3e  pProgDesc->numIoBuffers < maxAneIpcProgCallBufNbr
000bbf70  CAneBuiltInNetworkId::ANE_NET_T287_FD2D <= id
000bbf9e  id < CAneBuiltInNetworkId::ANE_NET_TOT
000bbfc5  0 == (size % sizeof(sCSneCmdProcedureCall))
000bbff1  0 < procedureCallCmdsNum[id]
000bc00e  program %d cmdProcedureCall %lu procedureId %u
000bc03e  i == pCmd->procedureId
000bc055  buf[%lu] bufIndex = %u, type = %u
000bc078  program %d cmdProcedureCallCustomBars %lu procedureId %u nbrOfCustomBars %d
000bc0c5  callCmdsNum == pCmd->procedureId
000bc0e6  0 < callCmdsNum
000bc0f6  AFPP is not setup yet
000bc10d  AFPP buffer 0x%llx, magic 0x%x, major 0x%x, minor 0x%x, program_offset_entry_num 0x%x
000bc164  ((uint32_t)(((uint32_t)'H' << 24) | ((uint32_t)'E' << 16) | ((uint32_t)'N' << 8) | (uint32_t)'A')) == package->magic
000bc1d9  Program magic 0x%x, size  0x%llx, builtin_program_id 0x%x, version 0x%x
000bc222  compiler_version 0x%x, program_load_version 0x%x
000bc254  chip_list_entry_num 0x%x
000bc26e  section_offset_entry_num 0x%x
000bc28d  ((uint32_t)(((uint32_t)'P' << 24) | ((uint32_t)'E' << 16) | ((uint32_t)'N' << 8) | (uint32_t)'A')) == program->magic
000bc302  program->builtin_program_id < maxProgramServerSupported
000bc33a  ((uint32_t)(((uint32_t)'S' << 24) | ((uint32_t)'E' << 16) | ((uint32_t)'N' << 8) | (uint32_t)'A')) == section->magic
000bc3af  (uint32_t)-1 != program_section_index
000bc3d5  Section magic 0x%x, size  0x%llx, section_id 0x%x, alignment 0x%x
000bc418  bHasProcedureCallCustomBarsSection == false
000bc444  bHasProcedureCallSection == false
000bc466  unsupported section type %d
000bc483  CmdProgramUnsetup starting %d
000bc4a1  true == programSetupDone
000bc4ba  builtInProgramId %d exceeded max (%d)!
000bc4e1  builtInProgramId %d should be invalid!
000bc508  !progProcInfo[builtinProgramId].valid
000bc52e  progProcInfo[builtinProgramId].progId != ECSneCmdId_Invalid
000bc56a  progProcInfo[builtinProgramId].procId != -1
000bc596  builtInProgramId %d is not valid!
000bc5b8  progProcInfo[builtinProgramId].valid
000bc5e2  (uint32_t)pCtx->programId != ECSneCmdId_Invalid
000bc612  pCtx->programId == (int32_t) progIn[builtinProgramId].programId
000bc652  pCtx->processId != -1
000bc668  (int32_t) progProcInfo[builtinProgramId].progId == pCtx->programId
000bc6ab  progProcInfo[builtinProgramId].procId == pCtx->processId
000bc6e4  callParaBuf
000bc6f0  AFPP does not support partial network execution
000bc720  pCmd->bSubNetworkCustomExecuteOrder == false
000bc74d  illegal nbrOfCustomBars=%d
000bc768  nbrOfCustomBars <= (128)
000bc781  No AFPP prefetch dsid provided
000bc7a0  nbrAfppMCacheDsid > 0
000bc7b6  AFPP prefetch dsid at [%d] is invalid
000bc7dc  afppMCacheDsid[idx] != (0xFF)
000bc7fa  AFPP intermdate spill dsid is invalid
000bc820  afppInterSpillDsid != (0xFF)
000bc83d  AFPP should not support circular buffer custom bar yet. Please check with algorithm
000bc891  AFPP should not support generic custom bar yet. Please check with algorithm
000bc8dd  anfd attr procedureId is out of range %d
000bc906  procedureId <= tempMaxProcedure
000bc926  anfd trk E procedureId is out of range %d
000bc950  anfd trk X procedureId is out of range %d
000bc97a  pContext && cbUserData
000bc991  Events Received in Server: %d %d %d %llu 0x%x
000bc9c0  __null != callParaBuf
000bc9d6  __null != pCallPara
000bc9ea  Prog %d %dms,cnt%d,avg%lld,max%d dtEnq:%d,avg%lld dtHW:%d,avg%lld
000bca2c  Prog %d %dms,cnt%d,avg%lld,max%d dtEnq:%d,avg%lld
000bca5e  ANE processCallProc+ %zu
000bca77  __null != ref
000bca85  __null != ref[0]
000bca96  __null != cmdBuf
000bcaa7  ref[0]->Size() == maxCmdBufSize
000bcac7  maxCmdBufSize >= sizeof(*pMsg) + pCmdHdr->size
000bcaf6  sapId 0x%x with nbrOfBuf %d size %lu %lu subPacketSize %d cmd %d
000bcb38  Invalid msg bufAddr 0%llx and bufSize 0x%llx
000bcb65  (uint64_t)pMsg->bufAddr[0] != 0 && (uint64_t)pMsg->bufSize[0] != 0
000bcba8  pMsg->bufNbr == 1
000bcbba  Invalid bufSize 0x%llx sAneProgramDescription 0x%llx
000bcbef  (uint64_t)pMsg->bufSize[0] >= sizeof(sAneProgramDescription)
000bcc2c  GetProgramDescription rc %d %d
000bcc4c  Invalid bufSize 0x%llx sAneProgramDescription 0x%llx sAneProgramContext 0x%llx
000bcc9b  (uint64_t)pMsg->bufSize[0] >= (sizeof(sAneProgramDescription) + sizeof(sAneProgramContext))
000bccf7  LoadProgram rc %d progId %d procId %d
000bcd1e  UnloadProgram rc %d progId %d procId %d
000bcd47  pMsg->bufNbr == 1 + progDesc.numIoBuffers
000bcd71  Invalid iobufs[%d].buffer 0%llx
000bcd91  (uint64_t)progDesc.iobufs[i].buffer != 0
000bcdba  [ipc] callProc %llu
000bcdce  buffer number (%d) in message is not expected
000bcdfc  Invalid bufSize 0x%llx sAneProgramDescription2 0x%llx
000bce32  (uint64_t)pMsg->bufSize[0] >= sizeof(sAneProgramDescription2)
000bce70  Invalid bufSize 0x%llx sAneProgramDescription2 0x%llx sAneProgramContext 0x%llx
000bcec0  (uint64_t)pMsg->bufSize[0] >= (sizeof(sAneProgramDescription2) + sizeof(sAneProgramContext))
000bcf1d  pMsg->bufNbr == 1 + pAneProgramDesc2->procedures[pProgCallSubPacket->procedureId].numIoBuffers
000bcf7c   CANE_SUB_PACKET_CMD_PROCEDURE_CALL program id %d, procedureId %d, numIoBuffers %d
000bcfd0  Invalid iobufs[%d].buffer 0%llx fpr procedureID %d
000bd003  (uint64_t)pAneProgramDesc2->procedures[pProgCallSubPacket->procedureId].iobufs[i].buffer != 0
000bd061  Procedure %d exceeded maximum for program %d
000bd08e  ERROR: AneSever cmd %d not expected
000bd0b2  sapId 0x%x with nbrOfBuf %d subPacketSize %d
000bd0e0  cmdBuf->Size() >= sizeof(*pMsg) + subPacketSize
000bd110  __null != pData
000bd120  pContext
000bd129  Got an unknown Command
000bd141  CAneServer Property Operation(%s): id %d 
000bd170  AFPPLoaded
000bd17b  0 != AFPPBuf.bufDesc.buffer
000bd197  AFPPBuf.bufDesc.size > 0
000bd1b0  program->version == programVer[program->builtin_program_id]
000bd1ec  chip_list[%d] 0x%x
000bd200  ./dump.afpp
000bd20c  CDebugUtility null
000bd21f  saved : [%s] size %d
000bd234  net: %16s, compiler 0x%x
000bd24e    total request GetDescription = %d
000bd273    total request LoadProgram = %d
000bd295    total request UnloadProgram = %d
000bd2b9    total request CallProc = %d
000bd2d8    total process CallProc = %d
000bd2f7  number of mcache DSIDs exceed max (%d)
000bd31e  nbrAfppMCacheDsid < maxAfppMCacheDsid
000bd344  afpp mcacheDsid[%d]: %d
000bd35c  afpp interspill dsid: %d
000bd375  Invalid field for updateDefSetting
000bd3b0  anfd_ssd
000bd3b9  anfd_trk_ex
000bd3c5  anfd_trk_xcorr
000bd3d4  anfd_attr
000bd3e6  anfd2_ssd
000bd3f0  anfd2_trk_ex
000bd3fd  anfd2_trk_xcorr
000bd40d  anfd2_attr
000bd418  anfd2_sal
000bd422  ./sne/Service/PowerControlService/CPowerControlService.cpp
000bd45d  instance
000bd466  instance == __null
000bd479  should be overloaded!
000bd48f  mPowerControlServiceCreated == false
000bd4b4  PMU Address is NULL
000bd4c8  PMU address already set %d
000bd4e3  PowerControlSet: pAddr=%p
000bd4fd  PowerControlSet: Delay 1ms, pPMUAddress %p
000bd528  Enabling the Dymanic PowerGating...
000bd54c  Disabling the Dymanic PowerGating...
000bd571  Disable PSD flag %d
000bd585  PowerControl_H18g
000bd597  ./sne/Service/PowerControlService/CPowerControlServiceAneH18g.cpp
000bd5d9  PMU address (0x%llx) already set
000bd5fa  pPMUAddress == __null
000bd610  InitPMUBaseAddress: pPMUAddress 0x%llx
000bd637  result == RTK_ST_OK
000bd64b  PowerControlSet: SetPMUBaseAddress deprecated
000bd679  PMU address is not set
000bd690  false == GetPowerStatus(PowerDomain_Id_H18g_ANE_TDBASE)
000bd6c8  Unknown powerState
000bd6db  Dymanic PowerGating is disabled
000bd6fb  ANE_TM_STATUS 0x%x
000bd70e  TDBase is not OFF yet
000bd724  TDBase set to P6 (Rail Gate) state
000bd747  onVal == (powerStatus & mask)
000bd765  offVal == (powerStatus & mask)
000bd784  PowerControlSet: Domain %d Pre-set status: %s, Target %s
000bd7cb  PowerControlSet: on by non-PSD
000bd7ea  PowerControlSet: off by non-PSD
000bd80a  PowerControlSet: Base %p index %d bDisablePsd %d : %d using %d us
000bd84c  PowerControlSet: Domain: %d %s %d times, Used %d
000bd87d  powerDomain >= PowerDomain_Id_H18g_ANE_START && powerDomain < PowerDomain_Id_H18g_ANE_END
000bd8d7  pPMUAddress == (size_t*)(0x28070c020 + (0x4000))
000bd908  PowerControlGet: Domain: %d status %s
000bd92e  PSD must be enabled
000bd942  bDisablePsd == 0
000bd953  ANE MPM Domain already in desired state (%d)
000bd99c  stk_fail
000bd9a5  initial heap size must > _ffwHeapSystemHeapAllocation * 2!
000bd9e0  rtkpsd_platform_default.cpp
000bd9fc  %s: Invalid client
000bda0f  initClientConfig
000bda20  Invalid numServiceSlots: 0x%x
000bda3e  %s:client not init
000bda51  getServiceName
000bda60  %s: invalid param
000bda72  %s: Invalid slot pio index for client: %#x service: %#x
000bdaaa  %s: invalid id: %u
000bdabd  getResetSendPayload
000bdad1  %s: invalid payload ptr
000bdae9  Client not initialized!!
000bdb02  Latency to P State Translation Failed
000bdb28  Invalid slot pio index for client: %#x service: %#x
000bdb5c  %s: client not init
000bdb70  initServiceConfig
000bdb82  %s: Invalid initConfig
000bdb99  %s: serviceId 0x%x already initialized
000bdbc0  getNumServiceSlots
000bdbd3  getServiceConfig
000bdbe4  %s: Error Flags 0x%x, Sent id 0x%x, Rcvd id 0x%x
000bdc2b  %s: Flags 0x%x, Sent id 0x%x, Rcvd id 0x%x
000bdc56  rtkpsd_common.cpp
000bdc68  %s: getServiceConfig(0x%x) err: 0x%x
000bdc8d  _initServiceDashboard
000bdca3  %s: Unsupported service id: 0x%x
000bdcc4  %s:RTK dev init(0x%x) fail: 0x%x
000bdce5  %s:RTK dev config(0x%x) fail: 0x%x
000bdd08  %s:RTK dev wake(0x%x) fail: 0x%x
000bdd29  %s: Not support PSD ACK mode: %d
000bdd4a  _stateChange
000bdd57  %s: Prev req pending service=0x%x wrVal=0x%x: 0x%x
000bdd8a  %s: Prev reqs caused sem signal service=0x%x wrVal=0x%x: 0x%x
000bddc8  PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) rdVal: (%#x) prevRdVal: (%#x) timeout after %llu usec
000bde3a  %s: PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) sem wait err: (%#x)
000bde88  %s: PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) != rdVal: (%#x) err
000bded6  %s: PSD Service (%s) id: (%#x) Client: (%#x) wrVal: (%#x) rdVal: (%#x)
000bdf1d  _getPowerStateVote
000bdf30  %s: client=0x%x service=0x%x err: 0x%x
000bdf57  %s: clientId=0x%x serviceId=0x%x pstate=%d
000bdf82  %s: initClientConfig err: 0x%x
000bdfa1  initPSDService
000bdfb0  %s: initServiceConfig err: 0x%x
000bdfd0  %s: initServiceDashboard err: 0x%x
000bdff3  %s: done clientId=0x%x serviceId=0x%x
000be019  %s: clientId=0x%x serviceId=0x%x active=%u ltr_usec=%u
000be050  enablePSDService
000be061  %s: getNumServiceSlots err: 0x%x
000be082  %s: invalid params
000be095  %s: stateChange(serviceId 0x%x) err: 0x%x
000be0bf  %s: clientId=0x%x serviceId=0x%x
000be0e0  getPSDServiceVote
000be0f2  %s: _getPowerStateVote(serviceId 0x%x) err: 0x%x
000be123  %s: Reset already initialized
000be141  initPSDReset
000be14e  %s: routingEpId=0x%x
000be163  %s: Reset not initialized
000be17d  sendPSDReset
000be18a  %s: getResetSendPayload err: 0x%x
000be1ac  %s: Start - routingEpId=0x%x id=0x%x payload=0x%llx
000be1e0  %s: MBI send msg timeout (routingEpId=0x%x id=0x%x)
000be214  %s: MBI send msg err (routingEpId=0x%x id=0x%x): 0x%x
000be24a  %s: MBI recv msg timeout (routingEpId=0x%x id=0x%x)
000be27e  %s: MBI recv msg err (routingEpId=0x%x id=0x%x): 0x%x
000be2b4  %s: checkResetRcvdPayload err: 0x%x
000be2d8  %s: Done - routingEpId=0x%x id=0x%x payload=0x%llx
000be312  setPSDLogLevel
000be321  !MIDR: 0x%x
000be32d  ~CsPTR
000be334  !ROf %#lx %#x
000be342  MMU out of tables: %zu,%zu
000be35d  MMU private: s:%llx!=%llx b:%llx!=%llx
000be384  MMU VA sz %u 0=%zu 1=%zu
000be39d  MMU private !fit: b:%lx<%lx s:%lx>%lx
000be3c3  GPTBAT !vm export: %x
000be3d9  PPL handoff !vm export: %x
000be3f4  MMU invalid page size: %x
000be40e  RTKit: %s - Client: %s
000be425  !clg: %08x
000be430  Not implemented
000be440  Message Log
000be44c  !Mthd:%p
000be455  !msgmbxint
000be460  !msgdoordashint
000be470  mme:0x%x
000be479  !Heapblk:%p
000be485  ThIntr:%u,%u,%u,%u
000be498  ThLock:%p
000be4a2  Terminator
000be4ad  VmOv %d %d
000be4b8  !vm nodes
000be4c6  Duty cycle
000be4d7  Sleep count
000be4e3  Wake count
000be4ee  Power state
000be4fa  Free heap
000be504  Total heap
000be50f  Peak heap alloc
000be51f  Used stack
000be52a  Total stack
000be536  CPU count
000be547  !ASLRHeapAlign
000be556  CXXPureVirt
000be562  rtk_ep_work
000be56e  MGMT msg=0x%llx st=%x
000be584  MGMT st=%x
000be593  MBI queue overflow:%s
000be5a9  Unbalanced transients
000be5bf  Invalid AP power: %d
000c87d8  CPS_M2A
000c8828  PACC_CLUSTER
000c8878  EACC_CLUSTER
000c88c8  GPU_CLUSTER
000c8918  IBOOT_P0
000c8968  SIO_UART0
000c89b8  SIO_UART1
000c8a08  SIO_UART2
000c8a58  SIO_UART3
000c8aa8  SIO_UART4
000c8af8  SIO_UART5
000c8b48  SIO_I2C0
000c8b98  SIO_I2C1
000c8be8  SIO_I2C2
000c8c38  SIO_I2C3
000c8c88  SIO_I2C4
000c8cd8  SIO_QSPI
000c8d28  SIO_SPI0
000c8d78  SIO_SPI1
000c8dc8  SIO_SPI2
000c8e18  SIO_SPI3
000c8e68  SIO_SPI_DMASHIM
000c8eb8  SIO_UART_DMASHI
000c8f08  IBOOT_DCP_SEC
000c8f58  SIO_CPU_BLOCKIN
000c8fa8  SIO_AES
000c8ff8  ANE0_CPU_0
000c9048  ANE0_SYS_0
000c9098  ANE1_CPU_0
000c90e8  ANE1_SYS_0
000c9138  ISP_CPU_BLOCKIN
000c9188  ISP_FE_0
000c91d8  ISP_SENSE0
000c9228  ISP_SENSE1
000c9278  DISP_CPU_0
000c92c8  DISP_SMB0_0
000c9318  DISP_SMB1_0
000c9368  DISP_DP_0
000c93b8  DISPSEC_CPU_0
000c9408  DISPSEC_SMB0_0
000c9458  DISPSEC_SMB1_0
000c94a8  DISPSEC_DP_0
000c94f8  EDISP0_CPU_0
000c9548  EDISP0_DP_0
000c95e8  MSR_BLOCKING
000c9638  AVD_BLOCKING
000c9688  AVE_CPU_BLOCKIN
000c96d8  APCIE_GP
000c9728  APCIE_GP0_0
000c9778  PRORES
000c97c8  AON_ATC0_COMMON
000c9818  AON_ATC0_USB_AO
000c9868  AON_ATC_USB
000c98b8  DBG_AVE_ALL
000c9908  DBG_DISP_ALL
000c9958  DBG_ISP_ALL
000c99a8  DBG_ANS_ALL
000c99f8  DBG_ANE_ALL
000c9a48  DBG_MISC_ALL
000c9a98  GPU_ASC0
000c9ae8  GPU_ASC1
000c9b38  APCIE_GP1_0
000c9b88  IBOOT_DCP
000c9bd8  ANE0_CPU_BLOCKI
000c9c28  ANE1_CPU_BLOCKI
000c9c78  ANE0_BASE_0
000c9cc8  ANE1_BASE_0
000c9d18  PIO_NONE_0
000c9d68  PIO_NONE_1
000c9db8  PIO_NONE_2
000c9e08  IBOOT_DCP_EXT
000c9e58  PIO_NONE_3
000c9ea8  DISP_CPU_1
000c9ef8  ANE0_CPU_1
000c9f48  ANE1_CPU_1
000c9f98  ISP_CPU_0
000c9fe8  DISPSEC_CPU_1
000ca038  APCIE_GP0_1
000ca088  APCIE_GP1_1
000ca0d8  DISP_CPU_2
000ca128  ANE0_CPU_2
000ca178  ANE1_CPU_2
000ca1c8  ISP_CPU_1
000ca218  DISPSEC_CPU_2
000ca268  APCIE_GP0_2
000ca2b8  APCIE_GP1_2
000ca308  ANE0_SYS_1
000ca358  ANE1_SYS_1
000ca3a8  ANE0_CPU_3
000ca3f8  ANE1_CPU_3
000ca498  DISP_CPU_3
000ca4e8  DISPSEC_CPU_3
000ca538  SIO_CPU
000ca588  DISP_CPU_4
000ca5d8  DISP_PIPELINE
000ca628  DISP_RCA
000ca678  DISP_OLED
000ca6c8  AON_DISP_DSG_PR
000ca718  DISP_SMB0_1
000ca768  DISP_SMB1_1
000ca7b8  DISP_DP_1
000ca808  DISP_DBE
000ca858  DISP_SPI
000ca8a8  DISP_DP_PHY
000ca8f8  DISP_MIPI_0
000ca948  AON_DISP_HPD_PR
000ca998  EDISP0_CPU_1
000ca9e8  EDISP0_DBE
000caa38  PIO_NONE_4
000caa88  EDISP0_DP_1
000caad8  PIO_NONE_5
000cab28  ISP_CPU_2
000cab78  ISP_STS0
000cabc8  ISP_STS1
000cac18  ISP_DPRX
000cac68  ISP_PEARL
000cacb8  ISP_CVD
000cad08  ISP_CLR
000cad58  ISP_SECURE
000cada8  ISP_FE_1
000cadf8  ISP_BE
000cae48  ANE0_CPU_4
000cae98  ANE0_BASE_1
000caee8  ANE0_MPM
000caf38  ANE1_CPU_4
000caf88  ANE1_BASE_1
000cafd8  ANE1_CPU_5
000cb028  ANE1_BASE_2
000cb078  ANE1_MPM
000cb0c8  ANE0_CPU_5
000cb118  ANE0_BASE_2
000cb168  AVE_CPU
000cb1b8  AVE_PIPE
000cb2a8  DISPSEC_CPU_4
000cb2f8  DISPSEC_PIPELIN
000cb348  DISPSEC_RCA
000cb398  DISPSEC_OLED
000cb3e8  AON_DISPSEC_DSG
000cb438  DISPSEC_SMB0_1
000cb488  DISPSEC_SMB1_1
000cb4d8  DISPSEC_DP_1
000cb528  DISPSEC_DBE
000cb578  DISPSEC_SPI
000cb5c8  DISP_SEC_DP_PHY
000cb618  DISP_MIPI_1
000cb668  AON_DISPSEC_HPD
000cbf20  not set
000cc068  lCytuDTR
000cc0c0  tnCplSTR
000cc118  tnCkaWTR
000cc170  tffOnOTR
000cc1c8  EERFPHTR
000cc221  LLAPHTR
000cc278  KAEPPHTR
000cc2d2  UKTSTR
000cc32a  AKTSTR*
000cc380  UPCmuNTR6
00170740  not set
00170888  lCytuDTR
001708e0  tnCplSTR
00170938  tnCkaWTR
00170990  tffOnOTR
001709e8  EERFPHTR
00170a41  LLAPHTR
00170a98  KAEPPHTR
00170af2  UKTSTR
00170b4a  AKTSTR*
00170ba0  UPCmuNTR6
```
