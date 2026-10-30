# `__NSURLSessionWebSocketTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `__NSCFLocalSessionTask`
- 13 instance variables, 3 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _webSocketHandshakeCompleted;
B _readInProgress;
i _pingSeed;
q _maximumMessageSize;
q _closeCode;
@"NSData" _closeReason;
@"NSMutableArray" _pendingSendWork;
@"NSMutableArray" _pendingReceiveWork;
@"NSMutableArray" _highPriorityPendingWork;
@"NSMutableArray" _delegateWork;
@"NSError" _webSocketError;
@"NSString" _protocolPicked;
@"NSObject<OS_nw_protocol_options>" _wsOptions;
```

## Properties

```
@property (Tq,V_maximumMessageSize) maximumMessageSize;
@property (Tq,R,V_closeCode) closeCode;
@property (T@"NSData",R,C,V_closeReason) closeReason;
```

## Instance methods

```
-[__NSURLSessionWebSocketTask _onqueue_cancel];
-[__NSURLSessionWebSocketTask _onqueue_didReceiveResponse:completion:];
-[__NSURLSessionWebSocketTask _onqueue_resume];
-[__NSURLSessionWebSocketTask connection:didFinishLoadingWithError:];
-[__NSURLSessionWebSocketTask initWithOriginalRequest:ident:taskGroup:];
-[__NSURLSessionWebSocketTask sendMessage:completionHandler:];
-[__NSURLSessionWebSocketTask dealloc];
-[__NSURLSessionWebSocketTask setMaximumMessageSize:];
-[__NSURLSessionWebSocketTask maximumMessageSize];
-[__NSURLSessionWebSocketTask _sendCloseCode:reason:];
-[__NSURLSessionWebSocketTask cancelWithCloseCode:reason:];
-[__NSURLSessionWebSocketTask isKindOfClass:];
-[__NSURLSessionWebSocketTask cancel];
-[__NSURLSessionWebSocketTask receiveMessageWithCompletionHandler:];
-[__NSURLSessionWebSocketTask sendPingWithPongReceiveHandler:];
-[__NSURLSessionWebSocketTask closeCode];
-[__NSURLSessionWebSocketTask closeReason];
```
