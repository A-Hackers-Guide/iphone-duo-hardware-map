# `/System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices`

From the upgrade restore ramdisk (141-29011-104.dmg). 146,000 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 23 (Size: 3192)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (6)

- `/System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices (compatibility version 1.0.0, current version 1.0.0)`
- `/System/Library/Frameworks/Security.framework/Security (compatibility version 1.0.0, current version 62460.40.78)`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation (compatibility version 150.0.0, current version 5027.1.8)`
- `/System/Library/Frameworks/Foundation.framework/Foundation (compatibility version 300.0.0, current version 5027.1.8)`
- `/usr/lib/libobjc.A.dylib (compatibility version 1.0.0, current version 228.0.0)`
- `/usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1359.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Objective-C (1 classes, 2 protocols)

Classes: `MOSplunkLogger`

Protocols: `NSObject`, `NSURLSessionDelegate`

## Strings (241)

```
%p %s\n
MOCreateCFTypeFromSerializedBuffer
topic
-[MOSplunkLogger URLSession:didReceiveChallenge:completionHandler:]
Unserialization failed: %@\n
eventType
Got connection on non-listener connection!?
Got dictionary on listener connection! Ignoring.
Can't send a message on a server transport handle!
%s.%d
alert
warn
info
%@.SplunkLoggerQueue
Error in uploading the events to splunk: %@
Maximum number of events exceeded. Discarding oldest event.
handle->flags.isServer
pthread_cond_wait failed
_HandleIncomingMessage
com.apple.MobileSystemServices.Logging.%s
-[MOSplunkLogger _onQueue_loadConfiguration]_block_invoke
metricsUrl
-[MOSplunkLogger uploadEventsWithCompletion:]_block_invoke_3
Error evaluating trust. SecTrustResultType=%d
MOXPCTransportOpen
Got event on connection for %p when connection was NULL!
!(handle->flags.isRunning)
Connection blew up while waiting for messages on %p
Sampling percentage set to %@
Loading configuration
Splunk upload start
_HandleListenerConnection_block_invoke_2
client connection error: %s
No message handler set and no support for receiving messages; dropping message.
%s [%d] <%s> (%p) %s: 
%s [%d] <%s> (%p) 
Splunk upload unexpected status: %d
MOXPCTransportReceiveMessage
pthread_cond_timedwait returned error %d\n
Could not find sampling percentage in configuration
Failed to serialize Splunk payload: %@
debug
events
Configuration does not have the expected format
MOXPCTransportOpen_block_invoke
_HandleClientError
com.apple.MobileSystemServices.Logging
Failed to create log string (malloc failed).
LogLevel
MOCreateSerializedData
postTime
Splunk upload successful
ignoring unknown event type from client
Message received was not a CFDictionary
Payload data received from client did not contain a CF object or failed to deserialize.
%s: set log level to %s
\n
-[MOSplunkLogger uploadEventsWithCompletion:]_block_invoke_2
-[MOSplunkLogger logEventNamed:value:]_block_invoke
MOXPCTransportSendMessageOnConnection
_HandleConnectionError
v12@?0i8
crit
Unable to load configuration. Error: %@
MOXPCTransportSetMessageHandler
gettimeofday returned error %d
err
Failed to create data from buffer
-[MOSplunkLogger _onQueue_loadConfiguration]
Splunk upload challenge
Failed to create xpc_connection!
Timed out waiting for message on %p
failed to register for %s notification
Failed to create log string (conversion failed).
%p %s: %s\n
%s.0
Splunk upload URL set to %@
Could not find metrics URL in configuration
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
Can't call MOXPCTransportReceiveMessage with a message handler set!
unknown server connection error: %s
mobile
MobileSystemServices-%s-%s
notice
eventTime
performance
Received the wrong kind of response: %@
Force Accepting Credential
MOXPCTransport.c
Failed to create log string (failed to get buffer size).
samplingPercentage
v8@?0
received unhandled event from server: %s
MOXPCTransportSetConnectionAuthHandler
Failed to create xpc dictionary
MOXPCTransportSendMessage
emerg
Failed to serialize: %@\n
POST
v16@?0^v8
MOSplunkLogger
NSURLSessionDelegate
NSObject
events
path
respondsToSelector:
setAllowInvalidCert:
setQueue:
conformsToProtocol:
isEqual:
removeAllObjects
removeObjectAtIndex:
setHTTPMethod:
zone
lastSuccessfulConfigurationLoad
.cxx_destruct
T@\"NSString\",&,N,V_splunkTopic
splunkUploadURL
class
hash
numberWithUnsignedLongLong:
objectForKeyedSubscript:
T@\"NSMutableArray\",&,N,V_events
T@\"NSString\",&,N,V_version
setURL:
setSplunkTopic:
_path
debugDescription
performSelector:withObject:
resume
T@\"NSURL\",&,N,V_configurationURL
Td,N,V_lastSuccessfulConfigurationLoad
addObject:
dataTaskWithURL:completionHandler:
isMemberOfClass:
previousFailureCount
setHTTPBody:
setLastSuccessfulConfigurationLoad:
isProxy
protectionSpace
URLSession:didReceiveChallenge:completionHandler:
_queue
_samplingPercentage
authenticationMethod
mutableCopy
samplingPercentage
version
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
_allowInvalidCert
floatValue
self
setConfigurationURL:
setEvents:
setSplunkUploadURL:
TB,N,V_allowInvalidCert
initWithName:configurationURL:splunkTopic:version:allowInvalidCert:
isEqualToString:
queue
retainCount
T@\"NSString\",R,C
URLByAppendingPathComponent:
UTF8String
_splunkTopic
count
ephemeralSessionConfiguration
sessionWithConfiguration:delegate:delegateQueue:
setPath:
T@\"NSNumber\",&,N,V_samplingPercentage
T@\"NSURL\",&,N,V_splunkUploadURL
T#,R
_lastSuccessfulConfigurationLoad
init
uploadEventsWithCompletion:
release
_configurationURL
allowInvalidCert
dictionaryWithObjects:forKeys:count:
setSamplingPercentage:
URLSessionDidFinishEventsForBackgroundURLSession:
configurationURL
credentialForTrust:
isKindOfClass:
retain
URLSession:didBecomeInvalidWithError:
dataWithJSONObject:options:error:
logEventNamed:value:
performSelector:
performSelector:withObject:withObject:
setObject:forKeyedSubscript:
statusCode
stringWithFormat:
TQ,R
URLWithString:
autorelease
description
splunkTopic
timeIntervalSinceReferenceDate
_events
T@\"NSString\",&,N,V_path
T@\"NSString\",?,R,C
_onQueue_loadConfiguration
setVersion:
_version
dataTaskWithRequest:completionHandler:
serverTrust
superclass
JSONObjectWithData:options:error:
_splunkUploadURL
@52@0:8@16@24@32@40B48
v16@0:8
v24@0:8d16
@\"NSMutableArray\"
d16@0:8
#16@0:8
@24@0:8:16
v32@0:8@\"NSURLSession\"16@\"NSError\"24
v24@0:8@\"NSURLSession\"16
v20@0:8B16
@\"NSString\"16@0:8
@\"NSString\"
@\"NSObject<OS_dispatch_queue>\"
d
B24@0:8@\"Protocol\"16
B16@0:8
v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32
v32@0:8@16@24
v40@0:8@16@24@?32
@\"NSURL\"
Vv16@0:8
Q16@0:8
v24@0:8@16
v24@0:8@?16
B
^{_NSZone=}16@0:8
@16@0:8
B24@0:8#16
B24@0:8:16
@\"NSNumber\"
B24@0:8@16
@32@0:8:16@24
@40@0:8:16@24@32
```
