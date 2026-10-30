# `NFCTag`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NFCTag`, `NFCNDEFTag`
- 6 instance variables, 9 properties, 41 instance methods, 3 class methods

## Instance variables

```
@"<NFTag>" _tag;
@"NSNumber" _sessionKey;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
q _configuration;
@"NFCHardwareManager" _hardwareManager;
```

## Properties

```
@property (Tq,R,N) configuration;
@property (T@"NFCHardwareManager",R,N,V_hardwareManager) hardwareManager;
@property (TQ,R,N) type;
@property (T@"<NFCReaderSession>",R,W,N) session;
@property (TB,R,N,GisAvailable) available;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[NFCTag supportsSecureCoding];
+[NFCTag _MaxRetry];
+[NFCTag _MaxRetryInterval];
```

## Instance methods

```
-[NFCTag isAvailable];
-[NFCTag capacity];
-[NFCTag identifier];
-[NFCTag disconnect];
-[NFCTag configuration];
-[NFCTag type];
-[NFCTag encodeWithCoder:];
-[NFCTag isReadOnly];
-[NFCTag initWithCoder:];
-[NFCTag session];
-[NFCTag copyWithZone:];
-[NFCTag _setSession:];
-[NFCTag applicationData];
-[NFCTag _setDelegateQueue:];
-[NFCTag isEqualToNFTag:];
-[NFCTag selectedAID];
-[NFCTag systemCode];
-[NFCTag historicalBytes];
-[NFCTag _disconnectWithError:];
-[NFCTag _connectWithCompletionHandler:];
-[NFCTag asNFCISO7816Tag];
-[NFCTag hardwareManager];
-[NFCTag isNDEFFormatted];
-[NFCTag writeLockWithCompletionHandler:];
-[NFCTag _connectWithSession:outError:];
-[NFCTag _getInternalReaderSession];
-[NFCTag _sendAPDU:completionHandler:];
-[NFCTag _setTag:];
-[NFCTag _supportsPACE];
-[NFCTag _transceiveWithData:completionHandler:];
-[NFCTag _transceiveWithSession:sendData:receivedData:error:];
-[NFCTag asNFCFeliCaTag];
-[NFCTag asNFCISO15693Tag];
-[NFCTag asNFCMiFareTag];
-[NFCTag dispatchOnDelegateQueueAsync:];
-[NFCTag initWithSession:tag:startupConfig:];
-[NFCTag isMatchingSession:outError:];
-[NFCTag proprietaryApplicationDataCoding];
-[NFCTag queryNDEFStatusWithCompletionHandler:];
-[NFCTag readNDEFWithCompletionHandler:];
-[NFCTag writeNDEF:completionHandler:];
```
