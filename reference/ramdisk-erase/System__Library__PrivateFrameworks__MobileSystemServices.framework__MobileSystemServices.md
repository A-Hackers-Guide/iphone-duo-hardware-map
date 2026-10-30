# `/System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 146,000 bytes.

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
Can't call MOXPCTransportReceiveMessage with a message handler set!
No message handler set and no support for receiving messages; dropping message.
v12@?0i8
Failed to create log string (malloc failed).
Failed to create log string (conversion failed).
%p %s\n
\n
eventType
samplingPercentage
ignoring unknown event type from client
com.apple.MobileSystemServices.Logging.%s
crit
warn
Splunk upload URL set to %@
Maximum number of events exceeded. Discarding oldest event.
-[MOSplunkLogger URLSession:didReceiveChallenge:completionHandler:]
v16@?0^v8
err
Splunk upload start
Error evaluating trust. SecTrustResultType=%d
Got event on connection for %p when connection was NULL!
_HandleIncomingMessage
%@.SplunkLoggerQueue
%s.0
notice
MOCreateSerializedData
Could not find sampling percentage in configuration
Unable to load configuration. Error: %@
MOXPCTransportSetConnectionAuthHandler
MOXPCTransportSendMessageOnConnection
client connection error: %s
Message received was not a CFDictionary
Payload data received from client did not contain a CF object or failed to deserialize.
%s: set log level to %s
-[MOSplunkLogger _onQueue_loadConfiguration]_block_invoke
POST
Splunk upload challenge
MOXPCTransportOpen
Failed to create xpc_connection!
Got dictionary on listener connection! Ignoring.
Can't send a message on a server transport handle!
info
metricsUrl
MOXPCTransport.c
MOXPCTransportSendMessage
pthread_cond_timedwait returned error %d\n
_HandleConnectionError
mobile
eventTime
Failed to serialize Splunk payload: %@
Splunk upload successful
-[MOSplunkLogger logEventNamed:value:]_block_invoke
received unhandled event from server: %s
%p %s: %s\n
%s.%d
topic
-[MOSplunkLogger uploadEventsWithCompletion:]_block_invoke_2
Failed to create data from buffer
Could not find metrics URL in configuration
-[MOSplunkLogger _onQueue_loadConfiguration]
Loading configuration
Error in uploading the events to splunk: %@
Connection blew up while waiting for messages on %p
%s [%d] <%s> (%p) %s: 
LogLevel
alert
Configuration does not have the expected format
performance
-[MOSplunkLogger uploadEventsWithCompletion:]_block_invoke_3
Force Accepting Credential
failed to register for %s notification
debug
MOCreateCFTypeFromSerializedBuffer
Unserialization failed: %@\n
MOXPCTransportOpen_block_invoke
gettimeofday returned error %d
_HandleListenerConnection_block_invoke_2
Failed to serialize: %@\n
!(handle->flags.isRunning)
handle->flags.isServer
MOXPCTransportSetMessageHandler
MOXPCTransportReceiveMessage
com.apple.MobileSystemServices.Logging
Failed to create log string (failed to get buffer size).
%s [%d] <%s> (%p) 
emerg
postTime
events
Got connection on non-listener connection!?
_HandleClientError
MobileSystemServices-%s-%s
Received the wrong kind of response: %@
Sampling percentage set to %@
v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24
v8@?0
Failed to create xpc dictionary
Timed out waiting for message on %p
pthread_cond_wait failed
unknown server connection error: %s
Splunk upload unexpected status: %d
MOSplunkLogger
NSURLSessionDelegate
NSObject
splunkUploadURL
mutableCopy
performSelector:
setAllowInvalidCert:
setPath:
T@\"NSString\",&,N,V_version
_splunkTopic
objectForKeyedSubscript:
setHTTPMethod:
setURL:
TQ,R
UTF8String
_samplingPercentage
dictionaryWithObjects:forKeys:count:
isMemberOfClass:
path
setLastSuccessfulConfigurationLoad:
protectionSpace
T@\"NSURL\",&,N,V_configurationURL
addObject:
credentialForTrust:
isKindOfClass:
samplingPercentage
serverTrust
setHTTPBody:
T@\"NSString\",?,R,C
Td,N,V_lastSuccessfulConfigurationLoad
URLSession:didBecomeInvalidWithError:
_allowInvalidCert
self
sessionWithConfiguration:delegate:delegateQueue:
setSplunkUploadURL:
stringWithFormat:
T@\"NSURL\",&,N,V_splunkUploadURL
T#,R
setSplunkTopic:
_onQueue_loadConfiguration
authenticationMethod
class
count
dataTaskWithURL:completionHandler:
release
.cxx_destruct
autorelease
description
ephemeralSessionConfiguration
performSelector:withObject:
queue
removeObjectAtIndex:
_lastSuccessfulConfigurationLoad
configurationURL
init
performSelector:withObject:withObject:
resume
retain
setEvents:
timeIntervalSinceReferenceDate
_events
T@\"NSString\",&,N,V_splunkTopic
hash
initWithName:configurationURL:splunkTopic:version:allowInvalidCert:
splunkTopic
uploadEventsWithCompletion:
TB,N,V_allowInvalidCert
URLSession:didReceiveChallenge:completionHandler:
removeAllObjects
retainCount
isProxy
T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue
URLSessionDidFinishEventsForBackgroundURLSession:
_configurationURL
_path
statusCode
JSONObjectWithData:options:error:
T@\"NSNumber\",&,N,V_samplingPercentage
conformsToProtocol:
debugDescription
logEventNamed:value:
setConfigurationURL:
_queue
_splunkUploadURL
_version
allowInvalidCert
dataTaskWithRequest:completionHandler:
isEqual:
isEqualToString:
numberWithUnsignedLongLong:
T@\"NSMutableArray\",&,N,V_events
URLWithString:
events
previousFailureCount
setQueue:
setSamplingPercentage:
dataWithJSONObject:options:error:
setObject:forKeyedSubscript:
lastSuccessfulConfigurationLoad
T@\"NSString\",&,N,V_path
URLByAppendingPathComponent:
floatValue
respondsToSelector:
setVersion:
superclass
zone
T@\"NSString\",R,C
version
v24@0:8@16
v32@0:8@\"NSURLSession\"16@\"NSError\"24
v24@0:8@\"NSURLSession\"16
B
Q16@0:8
B24@0:8@16
#16@0:8
@16@0:8
@40@0:8:16@24@32
Vv16@0:8
v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32
v32@0:8@16@24
v16@0:8
v24@0:8d16
@\"NSURL\"
@\"NSNumber\"
@\"NSString\"16@0:8
d
@52@0:8@16@24@32@40B48
d16@0:8
v20@0:8B16
@\"NSMutableArray\"
@24@0:8:16
B24@0:8@\"Protocol\"16
v40@0:8@16@24@?32
@\"NSString\"
@\"NSObject<OS_dispatch_queue>\"
^{_NSZone=}16@0:8
@32@0:8:16@24
B24@0:8#16
B24@0:8:16
v24@0:8@?16
B16@0:8
```
