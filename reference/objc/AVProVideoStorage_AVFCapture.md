# `AVProVideoStorage`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 3 properties, 28 instance methods, 4 class methods

## Instance variables

```
^{OpaqueFigSimpleMutex=} _lock;
^{OpaqueFigVirtualCaptureCard=} _virtualCaptureCard;
@"AVWeakReference" _weakReference;
@"NSMutableSet" _busyReasons;
B _recoveryRequired;
@? _pendingSetCapacityCompletion;
@? _pendingReplenishCompletion;
Q _replenishMaxAttempts;
q _replenishDecrementBytes;
```

## Properties

```
@property (Tq,R,N) initialCapacity;
@property (Tq,R,N) remainingCapacity;
@property (T@"NSSet",R,N) busyReasons;
```

## Class methods

```
+[AVProVideoStorage initialize];
+[AVProVideoStorage isSupported];
+[AVProVideoStorage sharedStorage];
+[AVProVideoStorage _replenishErrorForOSStatus:];
```

## Instance methods

```
-[AVProVideoStorage init];
-[AVProVideoStorage dealloc];
-[AVProVideoStorage initialCapacity];
-[AVProVideoStorage isBusy];
-[AVProVideoStorage maximumCapacity];
-[AVProVideoStorage performRecoveryWithForce:error:];
-[AVProVideoStorage _attemptReplenishWithCapacity:attemptCount:];
-[AVProVideoStorage _finalizeReplenishWithError:];
-[AVProVideoStorage _isBusyForPropertyReads];
-[AVProVideoStorage _maximumCapacityComponentsIncludingPurgeableSpace:];
-[AVProVideoStorage _reconnectToServer];
-[AVProVideoStorage _setCapacity:options:completion:];
-[AVProVideoStorage _setupVirtualCaptureCard];
-[AVProVideoStorage _syncPropertiesFromServer];
-[AVProVideoStorage _tearDownVirtualCaptureCard];
-[AVProVideoStorage _updateBusyReasons:];
-[AVProVideoStorage _updateRecoveryRequired:];
-[AVProVideoStorage busyReasons];
-[AVProVideoStorage cancelSetCapacity:];
-[AVProVideoStorage hasOpenedSettings];
-[AVProVideoStorage initialCapacityOverhead];
-[AVProVideoStorage isRecoveryRequired];
-[AVProVideoStorage maximumCapacityComponents];
-[AVProVideoStorage openSettings];
-[AVProVideoStorage remainingCapacity];
-[AVProVideoStorage replenishCapacityWithCompletionHandler:];
-[AVProVideoStorage sendGarbageCollectionHint];
-[AVProVideoStorage setCapacity:completion:];
```
