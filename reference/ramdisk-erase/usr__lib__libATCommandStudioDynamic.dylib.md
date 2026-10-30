# `/usr/lib/libATCommandStudioDynamic.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 796,208 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 25 (Size: 2680)
Flags         = NoUndefs, DyldLink, TwoLevel, WeakDefines, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (8)

- `/usr/lib/libATCommandStudioDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libmav_ipc_router_dynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libTelephonyCapabilities.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libQMIParserDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (539)

```
debug_ipc
(index+1)
radio
subscriber
(fTlv->getLength() - fIndex)
QMI Qos Service
pthread_create() failed, error = %d\n
(null)
global
atomicAdd(&fRefCount, (int) 0xa5a5a5a5)
 msgid=0x
QOS
exit_low_power
v16@?0^{ServiceType=C}8
cat
QMI Wireless Data Service
QMI BSP APPS Service
this
remote_log_level
result
v16@?0^{dispatch_group_s=}8
dms
Running
Req
WMS
fsDriver
buf_ptr
\t
 [
QMI Control Service
SFT
, pending-rx=
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/ATCommandStudio/Common/IPCDriver/ATCSRouterIPCDriver.cpp
sim
ssctl
QMI Vinyl Service
kLowPowerPendingSends
(fIndex+1)
(fIndex + strlen)
fMainState
Should never restart() a QMux that is being destroyed!
fMap.end()
j
kRevoked
QMI Mav P2P Service
qmux5
,
{vector<qmi::ClientProxy, std::allocator<qmi::ClientProxy>>=^{ClientProxy}^{ClientProxy}{?=^{ClientProxy}}}8@?0
0
 simSlot=
:0x
<=
location
AWD
PDC
kAll
cellmonitor
fPending
low_power_reply
dispatch_get_current_queue()==fState->queue()
header.msgType
MAV_BUFFER_SUCCESS
(fLength - fIndex)
fTlv->getLength()
VS
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/ATCommandStudio/QMI/QMITransactionQueue.cpp
kInit
Cannot queue send: Client is empty! (svc=?? client=?? txid=%d msgid=0x%x)
fBuffer
com.apple.telephony.abm
not accepted
logchan
coredump_
UIM
i->second.lock()
 |flow-control: tx-limit=
ret
fSize
CIQ
ATCS_TIMEOUT on message for svc=
bsp
stw
QMI Media Service Extension
QMux read parsing error: bad I/F type
v32@?0r^{QMuxHeader=CSCCCiS}8r*16i24i28
registration
client
PoweringDown(
fPowerUpState
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/ATCommandStudio/Common/IPCDriver/ATCSFileDescriptorIPCDriver.cpp
callback
kLowPowerStalled
]
QMI Apple Wireless Diagnostics
 timedout(
fAutostart
QMI Coexistence Service
QMI Mav 5WI Service
atcs.timer
connect
kFailed
QMI 5WI 787 Service
QMI Wireless Data Administrative Service
ind_qmi_message
fSendQueue.empty()
Failed set attributes, err = %s (%d)
raw_request
 stalled=
qmi::Client[
ims
fLength
(fIndex + length)
QMI Device Management Service
ATCSTimer Thread
fClientMap.count(key)
qmi::QMuxHeader::IND
pdc
QMI Subsystem Control
QMux destroyed while still attached to IPCDriver
fLock.isLocked()
 not 
 (txid=
 client=
vector
v12@?0S8
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/ATCommandStudio/Common/Timers/ATCSDPCQueue.cpp
elqm
ELQM
qmux_test
(fTlv->getLength() - index)
status
isInternalError(response.getError())
) [
 pending=
server
!=
QMI Modem File System Extended Service
CAT
kSecondary
raw_header_size
(fLength - index)
WDA
Attempted to enumerate an empty client map
fNext->fPrev == &fNext
qmux4
Baseband_QMI_LowPower_Error
, pending-tx=
i8@?0
awd
QMI Audio Service
QMI Mav L1 Service
PBM
send_timeout_ms
::QMIControl
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/ATCommandStudio/Common/IPCDriver/ATCSThreadedIPCDriver.cpp
fRunningWorkers
dfs
MAVL1
timer list lock
is not
reinterpret_cast<const char *>(buf) + buf_length
, lowpower=
)
4
atcsfdipc writer
QMIServerConnection
endpoint
txid
 
low_power
I8@?0
MAV_ROUTER_SUCCESS
Stopped
com.apple.commcenter.atcs.xpc
antenna
(index + length)
QMIClient must still be alive if we're adding something!
Should never start() a QMux that is being destroyed!
QMI client double request for ID
v16@?0^{PowerSaveState=I}8
???
name
Resp
B40@?0^{dispatch_data_s=}8Q16r^v24Q32
QMI User Identity Module
NAS
SSCTL
relativeTimeoutMilliseconds
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/ATCommandStudio/QMI/QMux.cpp
fPowerDownClientsState
kOffline
sendable=
Started
CTL
state
No way to call _sync functions after in kOffline; refs should be gone!
stopWorkersIfNeeded()
 sent(
(fIndex+2)
787
v16@?0r^v8
ptr
%s
atcs.disp
QMI Board Support Package Service
BSP
qmux_logchannel
QMIControl::appendPowerModeSet should not have been called! It does not make any sense
prevRefCount
(index+2)
QMI Access Terminal Service
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/ATCommandStudio/AT/Interface/Helpers/ATCSCommPortConfigurer.cpp
==
B16@?0^{Tlv=CS*S}8
QMI Card App Toolkit
tx->wasSent()
ATCSRouterIPCDriver
std::numeric_limits<int>::max()
dormancy
qmux3
QMI client has an ID and is waiting for one,
indSet.size()
v16@?0r^{AssignedId=CC}8
QMI Wireless Messaging Service
P2P
Can never reach here!
{QMIWakeReason={vector<unsigned char, std::allocator<unsigned char>>=**{?=*}}Q}8@?0
buffer
kDestroying
QMI Enhnaced Link Quality Metric Service
COEX
B16@?0r^v8
fPowerDownState
value
 svc=
255
com.apple.telephony.bb
This event cannot take a dispatch parameter
qmux2
media
qos_
PoweringUp(
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/ATCommandStudio/QMI/QMIControl.cpp
v16@?0^{PowerSaveDescriptor=IC}8
audio
p2p
AUDIO
true
*fPrev
boot-args
remote_log_bytes
qmux
kStopped
data_
send_window
set_ind_wake
kSync
fClientMap.end()
Exception at %s:%u: \n\t
kRunning
dsd
DMS
|
kStarting
LowPowerExit
eos
AT
QMux read parsing error: bad control flags
(4 + fMsgLength)
v8@?0
basic_string
at
aqm
MAVIMS
(empty QMux)
kNobody
acceptor
ServerError
qmux_control
Unknown Service
MS
map::at:  key not found
Failed get attributes, err = %s (%d)\n
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/ATCommandStudio/Common/Timers/ATCSTimer.cpp
TIME_GTE(fATCSTimerList->fDeadline, now)
(unknown)
v16@?0^v8
QMI Position Determination Service
WDS
VINYL
kPrimary
!tx.wasSent()
qmux_loc
S8@?0
src
(fIndex+4)
!fCallback
qmux_extra
ATCS.QMux.queue('
QMux read parsing error: buffer underrun for incomplete frame
Ind
B8@?0
timeout
LowPower
coex
MFSE
send_qmi_message
qmi_transaction_queue
targetProfile
(none)
Low power handler cannot take an XPC object paramter
QMI Carrier IQ Service
svc_type
resp_qmi_message
qmi::kQMIPower_Normal
!fPowerDownState
data
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/ATCommandStudio/QMI/TLV.cpp
>
QMI Data Filter Service
i
Assertion failure %s %s %s
{endpoint={object=^v}}8@?0
profile
qmi::kQMIPower_Low
vinyl
settings
NULL
QMI Persistent Device Service
>=
fDriver==NULL
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/ATCommandStudio/QMI/QMIServiceMsg.cpp
Assertion failure %s %s %s, left operand %p right operand %p
(index+4)
APPS
||
internal_error
kUnknown
false
kPoweredDown
com.apple.CommCenter.ATCS.QMIControl.Callbacks
QMI Stewie Service
DSD
error
/Library/Caches/com.apple.xbs/ABFEE097-B7D1-4B25-965F-348CD411B0E1/TemporaryDirectory.u1jxGk/Sources/AppleBasebandServices/ATCommandStudio/AT/Interface/ATDispatcherSupport.cpp
wda
ussd
(fIndex+8)
QMI Voice Service
QMI Data System Determination
fNext == NULL
Irrecoverable parsing error
(uint8_t*)bufferPtr + bufferLen
qmux1
voice
(index+8)
QMI Network Access Service
buf_length
\n
Writing to read buffer failed
sizeof( buff )
supp
desense
QMI Phonebook Manager Service
PDS
DFS
fState
{set<std::pair<const qmi::ServiceType, const unsigned short>, std::less<std::pair<const qmi::ServiceType, const unsigned short>>, std::allocator<std::pair<const qmi::ServiceType, const unsigned short>>>={__tree<std::pair<const qmi::ServiceT
qmi::Server
clientproxy_transaction
!fPowerUpState
atcsfdipc reader
sms
phonebook
diag
amount
fReverseMap.end()
v16@?0^{AssignedId=CC}8
[%s] Invalid interface type byte (got 0x%02x, available=%d); stream is corrupt; resetting QMux
[%s] handleReadData: Unknown message type %s; dropping (svc=%d client=%d txid=%d msgid=0x%x sim=%hhu)
[%s] Entering power mode %d; must wait until QMux is running (mainState=%s)
[%s] Entering power mode %d; signalling all clients
Sleeping
client '%s' ignoring XPC_ERROR_TERMINATION_IMMINENT
[%s]: Changing sim slot from %d to %d
Client: [%{public}s], invalid fTransport when handling indication
ATCS_TIMEOUT for message but client dead (txid=%d msgid=0x%x)
[%s] Stopping QMux (mainState=%s, powerState=%s)\n
Select exception on FD %d
ATCS_TIMEOUT was for a ctl::Sync message; this is expected sometimes [%s]\n
[%s] Retry timer is%sactive, retry attempts %d of max %d
Client: [%{public}s], invalid fTransport when sending internal error response for remote id
Message pended due to send window for svc=%d client=%d (txid=%d msgid=0x%x) [%s]
[%s] Cannot queue send: Unknown client (svc=%d client=%d txid=%d msgid=0x%x)
[%s] EXTRA:     -- signal QMIClient(svc=%d client=%d) to resume
QMI: Svc=0x%02x(%s) %s MsgId=0x%04x Sim=%d Bin=[%{sensitive,libTelephonyDecoder:QMI}.*P]
Send indication - Checking whether the client name matches: '%s' - '%s'
[%s]   QMIControl(%zd clients pending) %s\n    ind_wake={%s}\n
[%s]: Nothing further to send: low-power hold is complete
[%{public}s]   qmi::ClientProxy(svc=%d) [%{public}s] %{public}s ind_wake=[%{public}s]
Client: [%{public}s], invalid fTransport when sending disconnect message
Message force-sent for svc=%d client=%d (txid=%d msgid=0x%x) [%s]
QMI: Svc=0x%02x(%s) %s MsgId=0x%04x Bin=[%{libTelephonyDecoder:QMI}.*P]
Got %zd from %s
%d bytes for read on %s
[%s]: Stopping client and cleaning up
[%s]: Call back has been registered for this request 0x%04x
[%s] send: Truncated binary from %d bytes to %u bytes for QMI client(svc=%d client=%d)
Register response - Checking whether the client name matches: '%s' - '%s'
Deregister response - Checking whether the client name matches: '%s' - '%s'
XPC Listener: creating qmi::Server
[%s] Could not revoke client id, because QMIClient(svcType=%d,clientId=%d) isnt attached
[%s]     svc=%d (%s) registered ids={%s}
[%s]: Send window not changed due to illegal value of %d
[%s] ****** Client connection has been lost!
Message discarded because stopped for svc=%d client=%d (msgid=0x%x) [%s]
[%s] QMux is kStopped; dropping incoming %u bytes
[%s] Invalid control flags (got 0x%02x, available=%d); stream is corrupt; resetting QMux
Bailing due to low power
Client: [%{public}s], invalid fTransport at time of initialization
Client: [%{public}s], invalid fTransport when triggering low power state
[%s] Client connection rejected!
No transaction found for message for svc=%d client=%d (txid=%d msgid=0x%x); dropping response [%s]
[%s] queueing qmux pdu for svc=%d client=%d (txid=%d msgid=0x%x) [tx-slot=%d, rx-pending=%d]
[%s] EXTRA:     -- wait for QMIControl to set the power mode
ReleaseClientId::Response returned error 0x%x (%s) during removeClient_sync [%s]
[%s] Retrying request for client, svc type: %d
[%s] Client connection interrupted; retrying.
[%s] handleReadData: Client did exist, but is now dead; dropping (svc=%d client=%d txid=%d msgid=0x%x)
[%s] EXTRA:     -- wait for QMIControl to set QMI to power up
Incoming connection was not accepted; dropped.
QMux '%s' rejects incoming client due to bad service type 0x%x
Timeout waiting for response to QMI_CTL_SYNC; retrying ([%s])
Received unknown QMI CTL indication (0x%04x) [%s]
[%{public}s]: Received client id (svc=0x%x id=%d), but client was manually released; releasing id now.
Client: [%{public}s], invalid fTransport when handling response
[%s] QMux mainState=%s, powerState=%s, client count=%d%s
[%s] Not enough bytes for even the header (needs at least %u bytes), only %u available
[%s] More bytes in the buffer, expecting %d, but %d available; continuing
[%s] Normal power mode resumed; signalling all clients
[%s] Power-down configuration done; entering power-down mode %d
QMI: Svc=0x%02x(%s) %s MsgId=0x%04x Sim=%d Bin=[%{libTelephonyDecoder:QMI}.*P]
Woken with count %d
ERROR: handleClientIdRequest: 0x%x (%s) for type: %d; QMux dead; nothing happens now [%s]
Client: [%{public}s], invalid fTransport when triggering exit low power state
Client: [%{public}s], invalid fTransport when shutting down
[%s] Triggering Reset with reason %s
[%s] No reset invoker available; resetting QMux for reason=%s
Stale client id request received (no client still wants it: svc=%d new_id=%d); releasing it [%s]
Reader stopped
Client: [%{public}s], invalid fTransport when setting connected state
[%s] Warning! QMux destroyed while still attached to IPCDriver; attempting detach
[%s]     power down tags: %zu clients; all complete
[%s] Irrecoverable parsing error (available=%d), resetting QMux
Stop requested
 -- details of dropped connection: %s
QMux '%s' accepted client(svcType=0x%x, name='%s')
handleClientIdRequest received, but QMux is dead; dropping [%s]
[%{public}s]: Client created of type 0x%x
[%s] ****** Client message DROPPED because local connect message not yet sent. Message: %s
[%s] EXTRA:     -- wait for QMIControl to finish configuring IND sets
Received ctl::RevokeClientId::Indication [%s]
[%s] ****** Client message DROPPED because of invalid local connection. Message: %s
[%s] Sending client id revocation to QMIClient(svcType=%d,clientId=%d)
[%s] Cannot call handleSentData, QMI client(svc=%d client=%d) not found
QMI: Svc=0x%02x(%s) %s MsgId=0x%04x Bin=[%{sensitive,libTelephonyDecoder:QMI}.*P]
Failed to write to completion, ret = %zd, fd = %d
QMI: Svc=0x%02x(%s) %s MsgId=0x%04x Sim=%d Bin=[%{public,libTelephonyDecoder:QMI}.*P]
[%{public}s]: handleStatus_sync(%s), current fQMuxState=%s
[%{public}s]: ERROR: Triggered enter-low-power but we are in state %s already!
Attemping to create a QMI client on a device that does not support it!\n
[%s] QMux in sync with baseband, starting clients
[%s] Error with mainState=%s, powerState=%s
[%s] fMainState=%s fPowerState=%s
QMI: Svc=0x%02x(%s) %s MsgId=0x%04x Bin=[%{public,libTelephonyDecoder:QMI}.*P]
[%s] Cannot queue send: QMux is %s (svc=%d client=%d txid=%d msgid=0x%x)
Connection error: %s
ATCS_TIMEOUT should invoke reset but QMux is no longer alive [%s]
[%s] Client reconnect skipped because server is not reachable.
[%s] EXTRA:     -- signal QMIClient(svc=%d client=%d) to power down
QMux '%s' validation failed for incoming client(svcType=0x%x, name='%s')
Unable to synchronize with baseband QMI: error=%d (%s); retrying ([%s])
XPC Listener: go!
Timeout fired, but no transaction found for message (txid=%d) but client is dead; ignoring
[%s] Exiting low power mode
[%s] Baseband did not allocate client for svc type: %s, error: 0x%x (%s)
No callback for message for svc=%d client=%d (txid=%d msgid=0x%x); dropping response [%s]
Setting state to %s
Read available on %s
Giving %u bytes
 %d
[%s] Clearing all messages in the QMux send/pending queues
[%s] Control message error: %s%s
QMI: Svc=0x%02x(%s) %s MsgId=0x%04x
[%s]: Message pended for svc=0x%x (txid=%u, msgId=0x%04x); pending=%zu
Could not find subscription %s
[%s] handleReadData: Broadcast IND for QMI client (svc=%d client=%d msgid=0x%x)
Writer stopped
Client: [%s], invalid fTransport in server error handler
Dispatcher consumed %d bytes
[%s]: Starting client
Client: [%s], invalid fTransport passed in as parameter to state constructor
[%s]: Client connected to modem; old state=%s
Message stalled for svc=%d client=%d (txid=%d msgid=0x%x) [%s]
Timeout fired, but no transaction found for svc=%d client=%d (txid=%d); ignoring [%s]
[%s] Client power-down complete; configuring indication sets for power mode %d
[%{public}s]: Client id received successfully: svc=0x%x id=%d; starting client
[%s]: Client low-power group ++ Holding open (%p)
[%s] ****** Client message DROPPED (not queued) because of invalid local connection. Message: %s
ATCS_TIMEOUT on message for svc=%d client=%d (txid=%d msgid=0x%x) [%s]
[%s] ERROR: QMux should be powered down but the send queue is not empty!
Reader started
[%s]: SimSlot not changed due to illegal value of %d
Client: [%s], invalid fTransport when checking client validity
[%s]     power down tags: %zu clients; remaining={%s}
[%s]: Changing send window from %d to %d
[%s] Client connection invalid.
[%s] handleReadData: Cannot find QMI client, dropping (svc=%d client=%d txid=%d msgid=0x%x)
Received ctl::Sync::Indication [%s]\n
[%s]: Client low-power group -- Done (%p)
[%s]: Stopping client before it started; will re-start
XPC Listener: shutdown!
[%s] QMIClient(svcType=%d,clientId=%d) is dead but still registered; recycling the id
[%s] Got error 0x%x (%s), will retry client request for svc type: %d in %d msec
[%{public}s]: Client disconnect from modem; temp failure=%d; old state=%s
[%s] *** Client got message: %s
[%s] Client connection other error.
[%s] Could not revoke client id, because QMIClient(svcType=%d,clientId=%d) was attached but marked dead
[%s] Sending control indication to QMIClient(svcType=%d,clientId=%d) on sync
[%s] recv: Truncated binary from %zd bytes to %zu bytes for QMI client(svc=%d client=%d)
[%s] enterPowerMode(%d) ignored (QMux is %s)
[%s] All pending clients started, QMux fully initialized
[%s] ****** Client message DROPPED because no connection
QMux '%s' rejects incoming client(svcType=0x%x) due to empty name
[%s] Destroying QMux
[%s] Not enough bytes in the buffer: expecting %d, only %d available
QMux '%s' rejects incoming client(svcType=0x%x, name='%s') because of a bad endpoint
Writer started
Failed to write, ret = %zd, err = %s(%d)
```
