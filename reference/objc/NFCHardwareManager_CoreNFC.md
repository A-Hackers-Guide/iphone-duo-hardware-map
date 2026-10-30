# `NFCHardwareManager`

- Image: [`/System/Library/Frameworks/CoreNFC.framework/CoreNFC`](../userland/System__Library__Frameworks__CoreNFC.framework__CoreNFC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NFCSessionCallbacks`, `NFCPresentmentSuppressionDelegate`, `NFCHardwareManagerCallbacks`
- 9 instance variables, 5 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSHashTable" _delegates;
@"NFCSession" _xpcSession;
@"NSMutableDictionary" _queuedCoreNFCSessions;
@"NSObject<OS_dispatch_semaphore>" _hwSupportStateUpdate;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _readerSessionLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _presentmentSuppressionLock;
@"NFCPresentmentSuppression" _presentmentSuppression;
@"NSObject<NFCPresentmentSuppressionDelegate>" _presentmentSuppressionDelegate;
Q _lastPresentmentSuppressionReleaseTime;
```

## Properties

```
@property (T@"NSArray",R,C,N,GgetDelegates) delegates;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[NFCHardwareManager sharedHardwareManager];
```

## Instance methods

```
-[NFCHardwareManager init];
-[NFCHardwareManager didInvalidate];
-[NFCHardwareManager areFeaturesSupported:outError:];
-[NFCHardwareManager hwStateDidChange:];
-[NFCHardwareManager dequeueSession:];
-[NFCHardwareManager _cleanupPresentmentAssertion];
-[NFCHardwareManager _queueSession:];
-[NFCHardwareManager _releasePresentmentSuppressionAssertion:completion:];
-[NFCHardwareManager addNFCHardwareManagerCallbacksListener:];
-[NFCHardwareManager areFeaturesSupported:expiry:completion:];
-[NFCHardwareManager didExpire];
-[NFCHardwareManager getDelegates];
-[NFCHardwareManager getReaderSessionWithKey:];
-[NFCHardwareManager isCardSessionEligibleWithCompletionHandler:];
-[NFCHardwareManager queueCardFieldDetectSession:completionHandler:];
-[NFCHardwareManager queueCardSession:sessionConfig:completionHandler:];
-[NFCHardwareManager queueReaderSession:sessionConfig:completionHandler:];
-[NFCHardwareManager releasePresentmentSuppression:completion:];
-[NFCHardwareManager removeNFCHardwareManagerCallbacksListener:];
-[NFCHardwareManager requestPresentmentSuppressionWithDelegate:completion:];
```
