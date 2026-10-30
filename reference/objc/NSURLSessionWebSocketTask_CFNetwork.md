# `NSURLSessionWebSocketTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLSessionTask`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
q _maximumMessageSize;
q _closeCode;
@"NSData" _closeReason;
```

## Properties

```
@property (Tq,V_maximumMessageSize) maximumMessageSize;
@property (Tq,R,V_closeCode) closeCode;
@property (T@"NSData",R,C,V_closeReason) closeReason;
```

## Instance methods

```
-[NSURLSessionWebSocketTask sendMessage:completionHandler:];
-[NSURLSessionWebSocketTask setMaximumMessageSize:];
-[NSURLSessionWebSocketTask maximumMessageSize];
-[NSURLSessionWebSocketTask cancelWithCloseCode:reason:];
-[NSURLSessionWebSocketTask receiveMessageWithCompletionHandler:];
-[NSURLSessionWebSocketTask sendPingWithPongReceiveHandler:];
-[NSURLSessionWebSocketTask closeCode];
-[NSURLSessionWebSocketTask closeReason];
```
