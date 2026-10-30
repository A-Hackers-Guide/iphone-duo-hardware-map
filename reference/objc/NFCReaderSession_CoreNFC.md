# `NFCReaderSession`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NFReaderSessionCallbacks`, `NFCHardwareManagerCallbacks`, `NFCSessionCallbacks`, `NFCReaderSession`
- 16 instance variables, 16 properties, 58 instance methods, 2 class methods

## Instance variables

```
@ _delegate;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
@"NSObject<OS_dispatch_queue>" _sessionQueue;
@"NSObject<NFReaderSessionInterface><NSXPCProxyCreating>" _proxy;
q _sessionState;
B _delegateQueueStarted;
q _invalidationCode;
@"<NFTag>" _currentTag;
@"NSObject<OS_dispatch_group>" _sessionStartInProgress;
@"NSString" _alertMessage;
I _daemonExitReason;
@"NSNumber" _sessionId;
@"NFCHardwareManager" _hardwareManager;
@"NFCoreNFCPollConfig" _pollConfig;
q _delegateType;
Q _sessionType;
```

## Properties

```
@property (T@"NSObject<NFReaderSessionInterface><NSXPCProxyCreating>",R,&,N) readerProxy;
@property (T@"<NFTag>",R,N) currentTag;
@property (T@"NSNumber",R,N,V_sessionId) sessionId;
@property (T@"NFCHardwareManager",R,N,V_hardwareManager) hardwareManager;
@property (T@"NFCoreNFCPollConfig",&,N,V_pollConfig) pollConfig;
@property (TB,R,N,GisInvalidated) invalidated;
@property (Tq,R,N,V_delegateType) delegateType;
@property (TQ,R,N,V_sessionType) sessionType;
@property (T@,R,W,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) sessionQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisReady) ready;
@property (T@"NSString",C,N) alertMessage;
```

## Class methods

```
+[NFCReaderSession readingAvailable];
+[NFCReaderSession featureAvailable:];
```

## Instance methods

```
-[NFCReaderSession isReady];
-[NFCReaderSession sessionId];
-[NFCReaderSession dealloc];
-[NFCReaderSession alertMessage];
-[NFCReaderSession didInvalidate];
-[NFCReaderSession isInvalidated];
-[NFCReaderSession setAlertMessage:];
-[NFCReaderSession sessionType];
-[NFCReaderSession sessionQueue];
-[NFCReaderSession delegate];
-[NFCReaderSession invalidateSession];
-[NFCReaderSession beginSession];
-[NFCReaderSession connectTag:error:];
-[NFCReaderSession disconnectTagWithError:];
-[NFCReaderSession didStartSession:];
-[NFCReaderSession checkPresenceWithError:];
-[NFCReaderSession didDetectExternalReader];
-[NFCReaderSession didDetectNDEFMessages:fromTags:connectedTagIndex:updateUICallback:];
-[NFCReaderSession didDetectTags:connectedTagIndex:];
-[NFCReaderSession didTerminate:];
-[NFCReaderSession didUIControllerInvalidate:];
-[NFCReaderSession handleSessionResumed];
-[NFCReaderSession handleSessionSuspended:];
-[NFCReaderSession hwStateDidChange:];
-[NFCReaderSession restartPolling];
-[NFCReaderSession currentTag];
-[NFCReaderSession hardwareManager];
-[NFCReaderSession _callbackDidBecomeActive];
-[NFCReaderSession _callbackDidInvalidateWithError:];
-[NFCReaderSession _connectTag:error:];
-[NFCReaderSession _convertMessageToInternal:];
-[NFCReaderSession _invalidateSessionAndActivateCallbackWithCode:];
-[NFCReaderSession _invalidateSessionWithCode:];
-[NFCReaderSession _invalidateSessionWithCode:message:finalUIState:activateCallback:];
-[NFCReaderSession _restartPollingWithConfig:completionHandler:];
-[NFCReaderSession _resumeDelegateQueue];
-[NFCReaderSession _startPollingWithConfig:completionHandler:];
-[NFCReaderSession _stopPollingWithCompletionHandler:];
-[NFCReaderSession beginSessionWithConfig:];
-[NFCReaderSession cleanupNFCHardwareManagerRegistration];
-[NFCReaderSession connectTag:completionHandler:];
-[NFCReaderSession delegateType];
-[NFCReaderSession initWithDelegate:sessionDelegateType:sessionType:pollConfig:queue:];
-[NFCReaderSession invalidateSessionWithErrorMessage:];
-[NFCReaderSession invalidateSessionWithReason:];
-[NFCReaderSession ndefStatus:maxMessageLength:];
-[NFCReaderSession pollConfig];
-[NFCReaderSession readNdefMessageWithError:];
-[NFCReaderSession readerProxy];
-[NFCReaderSession restartPollingWithConfig:];
-[NFCReaderSession setPollConfig:];
-[NFCReaderSession submitBlockOnDelegateQueue:];
-[NFCReaderSession submitBlockOnSessionQueue:];
-[NFCReaderSession submitBlockOnSessionQueueWithDelay:block:];
-[NFCReaderSession transceive:tagUpdate:error:];
-[NFCReaderSession validateDelegate:expectedType:];
-[NFCReaderSession writeLockNdef];
-[NFCReaderSession writeNdefMessage:error:];
```
