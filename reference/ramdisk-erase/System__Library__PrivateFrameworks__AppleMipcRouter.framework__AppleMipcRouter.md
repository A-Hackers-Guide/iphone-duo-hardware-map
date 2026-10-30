# `/System/Library/PrivateFrameworks/AppleMipcRouter.framework/AppleMipcRouter`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 676,384 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 22 (Size: 2208)
Flags         = NoUndefs, DyldLink, TwoLevel, BindsToWeak, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/System/Library/PrivateFrameworks/AppleMipcRouter.framework/AppleMipcRouter (compatibility version 1.0.0, current version 0.0.0)`
- `/usr/lib/libMIPCSdk.dylib (compatibility version 1.0.0, current version 1.0.0, weak)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/usr/lib/libTelephonyUtilDynamic.dylib (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/PrivateFrameworks/AppleBasebandLink.framework/AppleBasebandLink (compatibility version 1.0.0, current version 0.0.0)`
- `/usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 2200.32.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (367)

```
The argument index value is too large for the number of arguments supplied
0
The type option contains an invalid value for a string formatting argument
Attempting to start router server without a valid transport
Slept
proxy
Active
{:#06x}
01
ClientName
com.apple.router.abb
PeakCountRate
 Timeout=
The fill option contains an invalid value
0x
 Trx=0x
alternate form
RouterGateway
 Msg=0x
a character
Integral value outside the range of the char type
Wakingup
Bytes
an integer
TIMEOUT for message 
AllowSleep
RegisteredIndications
RegisteredWakeables
com.apple.telephony.control-msg.xpc.allow
EndTimeSeconds
locale-specific form
0X
Received indication from transport
Init
MsgType
Indication
QueuePolicy
not 
The format string contains an invalid escape sequence
canceled
The format specifier contains malformed Unicode characters
Wakeup
TimeoutMillisec
server
TotalCount
<invalid>
The numeric value of the format specifier is too large
 formatting argument
{:#04x}
Down
never-q
agent
01234567
Received confirmation from transport
Error
always-q
I8@?0
End of input while parsing an argument index
false
C8@?0
Start
AP sleep is blocked by clients: {}
Failed to open router transport
0B
gateway
Router sleep timer
Sent request to transport
Count
BR
com.apple.router.mipc
a bool
ClientAction
The format string terminates at a '{'
RouterAgent
Using manual argument numbering in automatic argument numbering mode
The precision option does not contain a value or an argument index
 does not allow the 
infnanINFNAN
kMipcRouterServerReadyNotification
skipped
telephony
0123456789abcdefghijklmnopqrstuvwxyz
RegisteredEvents
link.accepter.local
StartTimeSeconds
TimePointSeconds
]
init-only-q
sent
basic_string
vector
Stopped
TrxId
{set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>={__tree<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}8@?0
[
s
The value of the argument index exceeds its maximum value
Started
 [
Bin=[
zero-padding
ClientId
{shared_ptr<abb::link::ClientLink>=^{ClientLink}^{__shared_weak_count}}8@?0
TotalBytes
The format specifier for 
a floating-point
Stopping
DurationSeconds
The argument index starts with an invalid character
End of input while parsing format specifier precision
RequestWithCnf
PeakByteRate
The width option should not have a leading zero
precision
true
Request
with
with no
(unknown)
v16@?0^v8
The type option contains an invalid value for 
0123456789abcdef
SimId
The argument index is invalid
com.apple.telephony.control-msg.xpc
Sleeping
Confirmation
RouterServer
Ind
<Empty message>
The format specifier should consume the input or end with a '}'
sign
The type does not fit in the mask
MsgId
link.accepter.xpc
 Client=0x
 
0b
Failed to send request to transport
RegisterClient
Connected
CR
router.queue
Req
Error: 
The replacement field misses a terminating '}'
a pointer
Aborting
Registered
 allow-sleep
v8@?0
The argument index should end with a ':' or a '}'
Replacement argument isn't a standard signed or unsigned integer type
An argument index may not have a negative value
router.client
Stop
Sleep
{:#x}
Using automatic argument numbering in manual argument numbering mode
Starting
ClientStatus
 bytes]
???
Client init
Failed to serialize Register_Ind_Req
Mipc flow-control: %u
Shutting gateway
Router transport is already closed
Registering new client after gateway is started; Client=0x%02x
Canceling request as endpoint is down; %s
Sent client message; %s
Looking for confirmation; %s
Confirmation is not tracked; %s
Confirmation received; cancel timer for %s
Unable to deserialize open mipc channel confirmation message; %s
Failed to open router transport
Received invalid message type [%u] from transport
Sleep clients procedure complete
Confirmation received; cancel timer; %s
Router sleep timeout; %zd clients failed to ack: %s
%s; %s %{sensitive}s
Removing previous indications registered for client; Client=0x%02x
Status changing from %s -> %s for client; Client=0x%02x
Wait queue is empty; nothing to send; Client=0x%02x
Sent request to gateway; %s
Invalid local accepter
Registering client indications; Client=0x%02x
Sleeping gateway
Router transport is open
Gateway moved on to %s; skipping transition to %s
Clearing all client delegates
Shutdown agent procedure complete
Received error from server: %s; Client=0x%02x
Error in indication received by agent; %s
Stop internal procedure complete
Indication handler found for Msg=0x%04x; Client=0x%02x
Queue client message as user has not started the client yet; %s
Received client confirmation; Client=0x%02x
Mipc version: %u
Request from gateway to stop [%s]; Client=0x%02x
User action stop; Client=0x%02x
Proxy not active for some reason [%s]; Client=0x%02x
Starting client
Client is connected; Client=0x%02x
Sent client message (from init queue); %s
Request to open mipc channel; %s
Lookup %s message; %s
Sending request failed; send error confirmation; %s
Notified all clients to sleep
Stop procedure complete
Notified all clients to wakeup
Request from gateway to shutdown [%s]; Client=0x%02x
Cleared all messages in sent-queue; stop procedure complete; Client=0x%02x
Removing user client %s indications; Client=0x%02x
Cancel message in wait-queue [%s]; %s
Client was already requested to stop
Stopping client
Client link is down; Client=0x%02x
Try sending [%zu] client message from init-queue
Registering indication handler for '%u'; Client=0x%02x
Deregistering indication handler for '%u'; Client=0x%02x
Cancel pending confirmations
Update flow-control from %zu -> %zu
Very unusual to have more than 1 pending action from server
Failed to serialize Open_Req
Handling pending action for %s
Request from gateway to shutdown agent
All indications are registered; %s
Start procedure complete
All clients acknowledged for start notification
Sent %zu of %zu messages from wait-queue; pending confirmations [%zu]; flow-control [%zu]; Client=0x%02x
Client is activated; Client=0x%02x
Received request from client; Msg=0x%04x
Request from gateway to wakeup agent
TIMEOUT for message; %s
Registering client events; Client=0x%02x
Mipc channel is closed; %s
Wakeup agent procedure complete
Nothing in wait-queue; shutdown procedure complete; Client=0x%02x
Sent %zu of %zu messages from wait-queue; Client=0x%02x
Request to connect with server
Client is stopped; Client=0x%02x
Queue client message as client got disconnected; %s
Received client status; Client=0x%02x
Request is not present in tracking queue; %s
Queue client message as client is not connected
Skipping message as link is not ready
Failed to serialize Close_Req
Registering new set of indications for client; Client=0x%02x
Start agent procedure complete
Reconnecting client
Received message from server: %s
Pending queue is empty; nothing to send
Client is not registered for this indication; %s
Cancel message in sent-queue [%s]; %s
Sending status [%s] update to client; Client=0x%02x
Client was already requested to start
Client is registered; Client=0x%02x
Request from gateway to sleep [%s]; Client=0x%02x
Queuing message to be sent in order [%s]; %s
Sent %zu of %zu messages from queue; pending-confirmation [%zu]; flow-control [%zu] %s
All clients acknowledged for stop notification
Nothing in sent-queue; stop procedure complete; Client=0x%02x
Canceling request as endpoint is not ready yet; %s
Canceling request as client is stopped; %s
Registering '%s' handler; Client=0x%02x
Request not tracked; not looking for confirmation or, might be canceled already; %s
Previous gateway sleep session failed for some reason
Skip queue to send this message; use temporary flow-control [%zu]; %s
Received message for Client=0x%02x: %s
Start listening to router server ready notification; Client=0x%02x
*** Client limit reached; cannot create new client ***
Wakeable indications are registered; %s
Wakingup gateway
Clearing all indication mappings
Track events of interest; Client=0x%02x
Cancel [%zu] queued requests; Client=0x%02x
Clearing all client-proxy instances
Mipc channel flow control reason=%u
Error in open mipc channel confirmation message; %s
Mipc channel is open now; %s
Preparing gateway open request
Notified all clients to start
Proxy is not active [%s]; proceed to stop anyway; Client=0x%02x
Track indications of interest; Client=0x%02x
Request to register all indications; %s; All-indications=[%zu] %s
Mipc channel flow-control=%u
Aborting gateway
Creating default xpc client
Client is shutdown; Client=0x%02x
Confirmation handler missing for Trx=0x%04x; may not be a problem; Client=0x%02x
Queue client message as client is not registered yet
Request from gateway to start agent
%s; %s %s
Reporting message timeout; %s
Shutdown clients procedure complete
Request from gateway to wakeup [%s]; Client=0x%02x
Request from gateway to start [%s]; Client=0x%02x
Sleep session is cleared; Client=0x%02x
Invalid xpc accepter
Unable to deserialize the indication received by agent; %s
Initializing gateway
User action start; Client=0x%02x
Sleep procedure complete; Client=0x%02x
Connecting xpc link
Stop listening to router server ready notification
Received client indication; Client=0x%02x
Agent has not registered for this indication; %s
Client connected %s indications to register; Client=0x%02x
Stopping gateway
Forward indication to client; %s
Registering client expectations; Client=0x%02x
Cancel [%zu] pending confirmations; Client=0x%02x
Sleep session is not held; Client=0x%02x
Connecting client
Connecting local link
Client not connected yet; will retry later
Set indication '%u' as %swakeable; Client=0x%02x
Request to remove client %s indications; Client=0x%02x
Starting gateway failed due to transport error
Sleep session is already released
Removing invalid client
Adding user client; Client=0x%02x
Release sleep session
Done!
Request to connect back with client [%s]; Client=0x%02x
Request to register wakeable indications; %s; Wakeable-indications=[%zu] %s
Register agent indications
Mipc channel flow control indication; %s
Ack flow-control update to baseband; %s
Request not present in tracking queue; %s
Client is sleeping; Client=0x%02x
Client is waking up; Client=0x%02x
Canceling request as proxy is down; %s
Starting timer for request; %s
Notified all clients to stop
Notified all clients to shutdown
Received request over link [%s]; %s
Track wakeable indications of interest; Client=0x%02x
Client not registered yet; will retry later
Setting client tracker
Request from gateway to sleep agent
Received mipc channel flow control indication without flow-control value
TIMEOUT for message with %s
Remove request from tracking queue; %s
Closing router transport
Router transport is closed
Cleared all messages in wait-queue; shutdown procedure complete; Client=0x%02x
Sleep procedure is waiting for confirmations; Client=0x%02x
Failed to close router transport
Sleep agent procedure complete
Start timer for request; %s
ServerLink type not recognized (likely test mock) - connection handled externally
Sending client action [%s]
Indication handler missing for Msg=0x%04x; may not be a problem; Client=0x%02x
Tracking confirmation; Trx=0x%04x Client=0x%02x
Could not send client message (from init queue); %s
Request to register all indications; %s
Opening router transport
Wakeup clients procedure complete
Registering client wakeable indications; Client=0x%02x
Request from gateway to stop agent
Request to close mipc channel; %s
Starting gateway
Gateway status changing from %s -> %s
Client link disconnected; Client=0x%02x
Sending sleep request; Client=0x%02x
```
