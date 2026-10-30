# `BLSHOSInterfaceProviderAbortContext`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHWatchdogAbortContext`
- 12 instance variables, 12 properties, 8 instance methods, 0 class methods

## Instance variables

```
Q _watchdogType;
q _cbDisplayMode;
q _cbFlipbookState;
q _caDisplayState;
q _completedCADisplayState;
B _suppressionServiceActive;
B _flipbookTransparent;
B _deviceSupportsAlwaysOn;
B _deviceSupportsAlwaysOnFlipbook;
B _displayStateClientSupported;
f _backlightDimmedFactor;
Q _abortReason;
```

## Properties

```
@property (TQ,R,N,V_abortReason) abortReason;
@property (T@"NSString",R,C,N) abortReasonString;
@property (Tr^v,?,R,N) payload;
@property (TI,?,R,N) payloadSize;
@property (TB,?,R,N) hasEnsureFlipbookCurrent;
@property (TB,?,R,N) wantsPanic;
@property (Td,?,R,N) panicDelay;
@property (TB,?,R,N) wantsWaitPastFireForCompletionAndTailspin;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHOSInterfaceProviderAbortContext description];
-[BLSHOSInterfaceProviderAbortContext abortReason];
-[BLSHOSInterfaceProviderAbortContext abortReasonString];
-[BLSHOSInterfaceProviderAbortContext initWithWatchdogType:cbDisplayMode:cbFlipbookState:caDisplayState:completedCADisplayState:suppressionServiceActive:flipbookTransparent:deviceSupportsAlwaysOn:deviceSupportsAlwaysOnFlipbook:displayStateClientSupported:backlightDimmedFactor:];
-[BLSHOSInterfaceProviderAbortContext panicDelay];
-[BLSHOSInterfaceProviderAbortContext setSleepImminentAbortReason];
-[BLSHOSInterfaceProviderAbortContext wantsPanic];
-[BLSHOSInterfaceProviderAbortContext wantsWaitPastFireForCompletionAndTailspin];
```
