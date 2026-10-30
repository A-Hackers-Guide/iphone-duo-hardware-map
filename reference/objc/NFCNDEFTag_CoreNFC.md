# `NFCNDEFTag`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NFCNDEFTag`
- 5 instance variables, 6 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"<NFTag>" _tag;
@"NSNumber" _sessionKey;
B _writeLocked;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
@"NFCHardwareManager" _hardwareManager;
```

## Properties

```
@property (T@"NFCHardwareManager",R,N,V_hardwareManager) hardwareManager;
@property (TB,R,N,GisAvailable) available;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[NFCNDEFTag supportsSecureCoding];
```

## Instance methods

```
-[NFCNDEFTag isAvailable];
-[NFCNDEFTag encodeWithCoder:];
-[NFCNDEFTag initWithCoder:];
-[NFCNDEFTag copyWithZone:];
-[NFCNDEFTag _setSession:];
-[NFCNDEFTag _setDelegateQueue:];
-[NFCNDEFTag _disconnectWithError:];
-[NFCNDEFTag _connectWithCompletionHandler:];
-[NFCNDEFTag hardwareManager];
-[NFCNDEFTag writeLockWithCompletionHandler:];
-[NFCNDEFTag _connectWithError:];
-[NFCNDEFTag _getInternalReaderSession];
-[NFCNDEFTag _setTag:];
-[NFCNDEFTag _updateNdefStatusWithSession:];
-[NFCNDEFTag dispatchBlockOnDelegateQueueAsync:];
-[NFCNDEFTag initWithSession:tag:startupConfig:];
-[NFCNDEFTag isMatchingSession:outError:];
-[NFCNDEFTag queryNDEFStatusWithCompletionHandler:];
-[NFCNDEFTag readNDEFWithCompletionHandler:];
-[NFCNDEFTag writeNDEF:completionHandler:];
```
