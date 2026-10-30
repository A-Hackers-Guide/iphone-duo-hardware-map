# `/System/Library/PrivateFrameworks/AppleMipcRouter.framework/AppleMipcRouter`

From the upgrade restore ramdisk (141-29011-104.dmg). 676,384 bytes.

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
Connected
RequestWithCnf
Count
Bin=[
0123456789abcdefghijklmnopqrstuvwxyz
01
AP sleep is blocked by clients: {}
{set<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>={__tree<unsigned int, std::less<unsigned int>, std::allocator<unsigned int>>=^v{?={__tree_end_node<std::__tree_node_base<void *> *>=^v}}{?=Q}}}8@?0
canceled
The replacement field misses a terminating '}'
gateway
router.queue
Error: 
s
RouterAgent
a bool
An argument index may not have a negative value
Received indication from transport
TrxId
 Msg=0x
v8@?0
PeakByteRate
Sleep
 Trx=0x
C8@?0
always-q
an integer
Failed to open router transport
RegisteredIndications
Wakeup
Bytes
telephony
alternate form
The type option contains an invalid value for a string formatting argument
{:#04x}
AllowSleep
RouterServer
Stop
vector
I8@?0
Using manual argument numbering in automatic argument numbering mode
The format specifier contains malformed Unicode characters
0
a character
Registered
Req
RouterGateway
Error
MsgId
<Empty message>
 [
???
The argument index is invalid
with no
Replacement argument isn't a standard signed or unsigned integer type
kMipcRouterServerReadyNotification
Received confirmation from transport
Stopping
{shared_ptr<abb::link::ClientLink>=^{ClientLink}^{__shared_weak_count}}8@?0
The format string contains an invalid escape sequence
zero-padding
The type option contains an invalid value for 
0x
a floating-point
com.apple.telephony.control-msg.xpc
Slept
TIMEOUT for message 
sent
The argument index value is too large for the number of arguments supplied
a pointer
ClientName
RegisteredEvents
DurationSeconds
Start
v16@?0^v8
ClientId
link.accepter.local
<invalid>
with
 does not allow the 
01234567
Init
Indication
TotalCount
not 
]
Integral value outside the range of the char type
 
never-q
server
PeakCountRate
com.apple.router.mipc
sign
Down
Started
Aborting
Sleeping
(unknown)
CR
init-only-q
The width option should not have a leading zero
precision
false
infnanINFNAN
RegisteredWakeables
 formatting argument
proxy
 bytes]
The format string terminates at a '{'
0X
The precision option does not contain a value or an argument index
Starting
ClientStatus
Ind
The format specifier should consume the input or end with a '}'
Confirmation
StartTimeSeconds
[
0B
Router sleep timer
 allow-sleep
agent
skipped
Wakingup
MsgType
com.apple.router.abb
TotalBytes
The argument index should end with a ':' or a '}'
The argument index starts with an invalid character
The fill option contains an invalid value
true
The value of the argument index exceeds its maximum value
Request
link.accepter.xpc
BR
Active
End of input while parsing an argument index
{:#x}
Attempting to start router server without a valid transport
RegisterClient
TimePointSeconds
locale-specific form
0b
Failed to send request to transport
QueuePolicy
The numeric value of the format specifier is too large
EndTimeSeconds
 Client=0x
TimeoutMillisec
End of input while parsing format specifier precision
The format specifier for 
The type does not fit in the mask
Sent request to transport
Stopped
ClientAction
router.client
basic_string
Using automatic argument numbering in manual argument numbering mode
com.apple.telephony.control-msg.xpc.allow
{:#06x}
SimId
 Timeout=
0123456789abcdef
Client connected %s indications to register; Client=0x%02x
Start timer for request; %s
Request not present in tracking queue; %s
Sending status [%s] update to client; Client=0x%02x
Registering new set of indications for client; Client=0x%02x
Gateway moved on to %s; skipping transition to %s
Stop procedure complete
Confirmation received; cancel timer; %s
Client is not registered for this indication; %s
Track indications of interest; Client=0x%02x
Client link is down; Client=0x%02x
Wakeable indications are registered; %s
Received request from client; Msg=0x%04x
Queue client message as client is not connected
Request to close mipc channel; %s
Mipc channel flow-control=%u
Request not tracked; not looking for confirmation or, might be canceled already; %s
Sleep agent procedure complete
Connecting xpc link
Client is shutdown; Client=0x%02x
Cancel [%zu] queued requests; Client=0x%02x
Queue client message as client got disconnected; %s
Request to register all indications; %s; All-indications=[%zu] %s
Mipc channel is closed; %s
Initializing gateway
Registering client events; Client=0x%02x
Request from gateway to shutdown agent
All clients acknowledged for start notification
Sleep procedure complete; Client=0x%02x
Looking for confirmation; %s
Failed to close router transport
Skip queue to send this message; use temporary flow-control [%zu]; %s
Received invalid message type [%u] from transport
Request from gateway to sleep [%s]; Client=0x%02x
Cancel [%zu] pending confirmations; Client=0x%02x
Lookup %s message; %s
Previous gateway sleep session failed for some reason
Pending queue is empty; nothing to send
Notified all clients to shutdown
Sleep procedure is waiting for confirmations; Client=0x%02x
Try sending [%zu] client message from init-queue
Client not registered yet; will retry later
Mipc channel is open now; %s
Sleep clients procedure complete
Received message for Client=0x%02x: %s
Stopping client
Register agent indications
Confirmation is not tracked; %s
Shutting gateway
Notified all clients to sleep
Router transport is closed
Start procedure complete
Shutdown agent procedure complete
Cleared all messages in sent-queue; stop procedure complete; Client=0x%02x
Mipc channel flow control reason=%u
Router transport is already closed
Very unusual to have more than 1 pending action from server
All clients acknowledged for stop notification
Sent request to gateway; %s
Client was already requested to stop
Tracking confirmation; Trx=0x%04x Client=0x%02x
Queue client message as user has not started the client yet; %s
Sending request failed; send error confirmation; %s
Aborting gateway
Stopping gateway
Queuing message to be sent in order [%s]; %s
Handling pending action for %s
Clearing all indication mappings
Sleep session is cleared; Client=0x%02x
Registering client wakeable indications; Client=0x%02x
Request to register wakeable indications; %s; Wakeable-indications=[%zu] %s
Request from gateway to stop agent
Starting timer for request; %s
Sending sleep request; Client=0x%02x
Client is activated; Client=0x%02x
Indication handler found for Msg=0x%04x; Client=0x%02x
Canceling request as client is stopped; %s
Could not send client message (from init queue); %s
Agent has not registered for this indication; %s
Request is not present in tracking queue; %s
TIMEOUT for message with %s
Removing previous indications registered for client; Client=0x%02x
Client is registered; Client=0x%02x
Set indication '%u' as %swakeable; Client=0x%02x
Received error from server: %s; Client=0x%02x
Request to remove client %s indications; Client=0x%02x
Notified all clients to stop
Sleeping gateway
Gateway status changing from %s -> %s
Update flow-control from %zu -> %zu
Wakeup clients procedure complete
Request from gateway to stop [%s]; Client=0x%02x
Cancel message in sent-queue [%s]; %s
Cancel pending confirmations
Wait queue is empty; nothing to send; Client=0x%02x
Sent %zu of %zu messages from wait-queue; Client=0x%02x
Client link disconnected; Client=0x%02x
Client not connected yet; will retry later
Request from gateway to sleep agent
Request to open mipc channel; %s
Ack flow-control update to baseband; %s
Failed to open router transport
Closing router transport
Release sleep session
Forward indication to client; %s
Canceling request as endpoint is down; %s
Mipc channel flow control indication; %s
Wakingup gateway
Stop internal procedure complete
Nothing in wait-queue; shutdown procedure complete; Client=0x%02x
Request to connect with server
Connecting client
Registering indication handler for '%u'; Client=0x%02x
Deregistering indication handler for '%u'; Client=0x%02x
Failed to serialize Open_Req
Unable to deserialize open mipc channel confirmation message; %s
Done!
Proxy is not active [%s]; proceed to stop anyway; Client=0x%02x
Request to connect back with client [%s]; Client=0x%02x
Stop listening to router server ready notification
Registering client indications; Client=0x%02x
Received client status; Client=0x%02x
Notified all clients to start
TIMEOUT for message; %s
Status changing from %s -> %s for client; Client=0x%02x
Cleared all messages in wait-queue; shutdown procedure complete; Client=0x%02x
Connecting local link
Indication handler missing for Msg=0x%04x; may not be a problem; Client=0x%02x
Received client indication; Client=0x%02x
Request from gateway to start agent
Remove request from tracking queue; %s
Error in open mipc channel confirmation message; %s
Starting gateway failed due to transport error
Router sleep timeout; %zd clients failed to ack: %s
Registering new client after gateway is started; Client=0x%02x
Request from gateway to start [%s]; Client=0x%02x
User action stop; Client=0x%02x
Mipc version: %u
%s; %s %{sensitive}s
Start agent procedure complete
Cancel message in wait-queue [%s]; %s
Received request over link [%s]; %s
Canceling request as endpoint is not ready yet; %s
Client init
Start listening to router server ready notification; Client=0x%02x
Preparing gateway open request
Wakeup agent procedure complete
Sleep session is not held; Client=0x%02x
Sleep session is already released
Opening router transport
Request from gateway to shutdown [%s]; Client=0x%02x
Sent client message; %s
Setting client tracker
Confirmation received; cancel timer for %s
Removing invalid client
Adding user client; Client=0x%02x
Notified all clients to wakeup
Canceling request as proxy is down; %s
Received message from server: %s
Clearing all client-proxy instances
Mipc flow-control: %u
Starting gateway
Reporting message timeout; %s
User action start; Client=0x%02x
ServerLink type not recognized (likely test mock) - connection handled externally
Starting client
Reconnecting client
*** Client limit reached; cannot create new client ***
%s; %s %s
Invalid xpc accepter
Client is sleeping; Client=0x%02x
Confirmation handler missing for Trx=0x%04x; may not be a problem; Client=0x%02x
Registering '%s' handler; Client=0x%02x
Failed to serialize Register_Ind_Req
Request from gateway to wakeup agent
Router transport is open
Sent %zu of %zu messages from wait-queue; pending confirmations [%zu]; flow-control [%zu]; Client=0x%02x
Track events of interest; Client=0x%02x
Client is stopped; Client=0x%02x
Sending client action [%s]
Sent client message (from init queue); %s
Clearing all client delegates
Skipping message as link is not ready
Track wakeable indications of interest; Client=0x%02x
Creating default xpc client
Client is connected; Client=0x%02x
Registering client expectations; Client=0x%02x
Request to register all indications; %s
Sent %zu of %zu messages from queue; pending-confirmation [%zu]; flow-control [%zu] %s
Shutdown clients procedure complete
Proxy not active for some reason [%s]; Client=0x%02x
Client is waking up; Client=0x%02x
Received client confirmation; Client=0x%02x
Failed to serialize Close_Req
Unable to deserialize the indication received by agent; %s
Removing user client %s indications; Client=0x%02x
Request from gateway to wakeup [%s]; Client=0x%02x
Nothing in sent-queue; stop procedure complete; Client=0x%02x
Invalid local accepter
Client was already requested to start
Queue client message as client is not registered yet
Error in indication received by agent; %s
Received mipc channel flow control indication without flow-control value
All indications are registered; %s
```
