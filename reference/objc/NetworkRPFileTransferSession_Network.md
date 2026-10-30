# `NetworkRPFileTransferSession`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _isTarget;
@? _receivedFileHandler;
@? _completionHandler;
@"RPFileTransferSession" _session;
```

## Properties

```
@property (TB,R,N,V_isTarget) isTarget;
@property (T@"RPFileTransferSession",R,N,V_session) session;
@property (T@?,C,N,V_receivedFileHandler) receivedFileHandler;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@"NSData",C,N) peerPublicKey;
@property (T@"NSData",R,C,N) selfPublicKey;
@property (T@"NSString",C,N) targetID;
@property (T@"NSURL",C,N) temporaryDirectoryURL;
```

## Instance methods

```
-[NetworkRPFileTransferSession setCompletionHandler:];
-[NetworkRPFileTransferSession completionHandler];
-[NetworkRPFileTransferSession setTargetID:];
-[NetworkRPFileTransferSession invalidate];
-[NetworkRPFileTransferSession prepare];
-[NetworkRPFileTransferSession activate];
-[NetworkRPFileTransferSession targetID];
-[NetworkRPFileTransferSession session];
-[NetworkRPFileTransferSession handleProgress:];
-[NetworkRPFileTransferSession handleReceivedItem:];
-[NetworkRPFileTransferSession initAsTarget:];
-[NetworkRPFileTransferSession isTarget];
-[NetworkRPFileTransferSession peerPublicKey];
-[NetworkRPFileTransferSession receivedFileHandler];
-[NetworkRPFileTransferSession selfPublicKey];
-[NetworkRPFileTransferSession setPeerPublicKey:];
-[NetworkRPFileTransferSession setReceivedFileHandler:];
-[NetworkRPFileTransferSession setTemporaryDirectoryURL:];
-[NetworkRPFileTransferSession temporaryDirectoryURL];
-[NetworkRPFileTransferSession transferFileURL:completion:];
```
