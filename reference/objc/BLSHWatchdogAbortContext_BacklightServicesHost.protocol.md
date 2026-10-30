# `BLSHWatchdogAbortContext` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 9 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) abortReason;
@property (T@"NSString",R,C,N) abortReasonString;
@property (Tr^v,?,R,N) payload;
@property (TI,?,R,N) payloadSize;
@property (TB,?,R,N) hasEnsureFlipbookCurrent;
@property (TB,?,R,N) wantsPanic;
@property (Td,?,R,N) panicDelay;
@property (TB,?,R,N) wantsWaitPastFireForCompletionAndTailspin;
```

## Instance methods

```
-[BLSHWatchdogAbortContext abortReason];
-[BLSHWatchdogAbortContext abortReasonString];
-[BLSHWatchdogAbortContext setSleepImminentAbortReason];
-[BLSHWatchdogAbortContext payload];
-[BLSHWatchdogAbortContext hasEnsureFlipbookCurrent];
-[BLSHWatchdogAbortContext payloadSize];
-[BLSHWatchdogAbortContext panicDelay];
-[BLSHWatchdogAbortContext wantsPanic];
-[BLSHWatchdogAbortContext wantsWaitPastFireForCompletionAndTailspin];
```
