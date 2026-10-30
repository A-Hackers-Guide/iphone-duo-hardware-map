# `NWURLSessionWebSocketTask`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NWURLSessionTask`
- 9 instance variables, 3 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _receiving;
S _pingSeed;
q _maximumMessageSize;
q _closeCode;
@"NSData" _closeReason;
@"NSURLResponse" _storedResponse;
@"NSMutableArray" _pendingWork;
@"NWURLError" _pendingReceiveError;
@"NSMutableArray" _pendingReceiveCompletionHandlers;
```

## Properties

```
@property (Tq,N,V_maximumMessageSize) maximumMessageSize;
@property (Tq,R,N) closeCode;
@property (T@"NSData",R,C,N) closeReason;
```

## Class methods

```
+[NWURLSessionWebSocketTask isSubclassOfClass:];
```

## Instance methods

```
-[NWURLSessionWebSocketTask sendMessage:completionHandler:];
-[NWURLSessionWebSocketTask setMaximumMessageSize:];
-[NWURLSessionWebSocketTask error];
-[NWURLSessionWebSocketTask maximumMessageSize];
-[NWURLSessionWebSocketTask _sendCloseCode:reason:];
-[NWURLSessionWebSocketTask cancelWithCloseCode:reason:];
-[NWURLSessionWebSocketTask isKindOfClass:];
-[NWURLSessionWebSocketTask receiveMessageWithCompletionHandler:];
-[NWURLSessionWebSocketTask sendPingWithPongReceiveHandler:];
-[NWURLSessionWebSocketTask response];
-[NWURLSessionWebSocketTask closeCode];
-[NWURLSessionWebSocketTask closeReason];
-[NWURLSessionWebSocketTask completeTaskWithError:retryable:];
-[NWURLSessionWebSocketTask isWebSocket];
-[NWURLSessionWebSocketTask startNextLoad];
```
