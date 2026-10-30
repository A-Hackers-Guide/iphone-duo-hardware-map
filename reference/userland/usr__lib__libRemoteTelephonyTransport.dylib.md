# `/usr/lib/libRemoteTelephonyTransport.dylib`

iOS 27.2 dyld shared cache image. Version `6575.0.0.0.0`. **[DSC]**

## Linked libraries (6)

- `/usr/lib/libTelephonyUtilDynamic.dylib`
- `/usr/lib/libpcap.A.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`

## Strings (171)

```
Ignoring unsupported message type: %s, length: %zu
Unable to compile filter expression, error: %s
Data link type is: %s ; Expected: %s
Providing readQueue is mandatory when read mode is specified
Skipping Unknown message type of length: %zu
Unable to start tcp server
Zero size message is not expected in read indication
Failed to process the message properly
Failed to create NetworkSocketBridge
Failed to create destination write only protocol
Only kPDPIP message type is supported here
TxnId is missing. Skipping MessageType: %s, length: %zu
Unable to create read handle! Details: %s
Failed to initialize writer
Warning: Already started reading
Unable to set immediate mode, error: %s
Response doesn't contain result
%s
Transport token is missing. Skipping MessageType: %s, length: %zu
Delegate is mandatory for modes that require reader
Unable to set filter
No valid handle exists to determine link type.
Unable to create read source
Error encountered while reading: %s
Created transport token is missing
No data read
Write is not supported
Emplace should always succeed (duplicate txnId is fatal)
Unable to retrieve a selectable fd
Failed to send message. RequestT: %s
Timed out waiting for response
Processed bytes cannot exceed length. Processed: %zu, Length: %zu
Failed to create socket
Unable to create accept source
Failed to create destination transport
Invalid network interface parameters
Providing readQueue is mandatory
Data available in buffer must not be greater than kHeaderSize + payloadLength
Invalid address: %s
Cannot handle packet of length: %lu
Failed to create SocketAndEthernetIfaceBridge
Failed to create source read only protocol
Failed to create source transport
IP header version: %u is invalid
Failed to create SocketAndRawIPIfaceBridge
Received response type doesn't match expected response type. TxnId: %llu, Expected: %s, Received: %s
Response doesn't contain messageId
Write failed: %s
Providing acceptQueue is mandatory
Accept failed: %s
Warning: Unable to mark socket as non blocking
Failed to send response of MessageType: %s, TxnId: %llu
Emplace failed while inserting token
Unable to set direction, error: %s
Unable to find index for interface: %s
Failed to create base protocol
Oversteer: Starting PCIClient
Failed to update snapshot length for read handle
Unable to create write handle! Details: %s
Failed to initialize reader
Create must return valid token
PCI transport for Oversteer created successfully with token %u
Couldn't find mac address for interface: %s
%s is missing. Skipping MessageType: %s
Sending notification to indicate that PCIClient is ready
Response messageId must match request messageId
%s failed
Failed to create destination write only transport
Must provide a valid delegate
Unable to bind to %s:%u - %s
Failed to enable port reuse
Failed to initialize
Unable to set SO_NOSIGPIPE option
Failed to deserialize message. MessageType: %s, length: %zu
messageId is missing. Skipping MessageType: %s, length: %zu
Oversteer: Waiting for connection...
Not instantiating PCI client because oversteer and bbsimulation are disabled
Changed snaplength from %d to %d
Can't read more bytes than requested
Already started reading
Read issue: %s
Failed to connect to: %s:%u
Received another connection. Restarting process...
Failed to create PCIClientTransport
No response
Unable to fulfil promise for - MessageType: %s, length: %zu
Failed to listen for %s:%u - %s
Unable to bind to interface: %s
Received indication with failure
Failed to determine link type. pcap_datalink returned: %d
Failed to write packet to %s, error: %s
Invalid socket descriptor
Delegate is mandatory
Unable to get interface addresses
WhichRegister
tcpclienttransport
kFlushReadResponse
tcpclientsocketfactory
Flags
kFreeResponse
kUnblockReadRequest
whichRegister
basic_string
SizeReadIO
pciservicetransport
PCIClientContext
TTPCIClientReadyNotification
kCreateRequest
kReadRequest
ip or ip6
PciTransportInterface
PCIClientTCPServer
pci
com.apple.rtt
kCreateResponse
kStatusIndication
transportToken
arg2
network
TimeoutMs
kReadRegisterRequest
result
createdTransportToken
kUnblockReadResponse
NumReadIO
CreateTimeOutMs
BytesToRead
PCIClientTransport
TTStartPCIClientNotification
factory
txnId
v8@?0
vector
kWriteResponse
kFreeRequest
kReadRegisterResponse
cookie
numReadIO
nwiface
kReadIndication
bytesWritten
flags
baseproto
tcpserver
timeoutMs
createTimeOutMs
openRetryCount
NetworkIface
pciclienttransport
bytesToRead
arg1
networksocket
data
Status
kReadResponse
kWriteRequest
kFlushReadRequest
pciTransportInterface
sizeReadIO
PCIServiceTransport
tcpsockstream
default
OpenRetryCount
Arg1
kSendImageRequest
status
TCPSocketStream
messageId
messageId()->hasTransportToken
Arg2
kSendImageResponse
```
