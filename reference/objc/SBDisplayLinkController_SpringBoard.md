# `SBDisplayLinkController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightHostObserving`, `BSInvalidatable`
- 7 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"CADisplay" _display;
@"<BLSHBacklightHostObservable>" _backlight;
C _maintainDisplayLinkWhenBacklightIsOffCount;
B _observerRegistered;
B _displayLinkWouldBeOff;
B _displayLinkForcedToFixedRate;
B _invalidated;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDisplayLinkController invalidate];
-[SBDisplayLinkController backlight:didBlankToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:];
-[SBDisplayLinkController backlight:willUnblankToDisplayMode:fromDisplayMode:forEvents:abortedEvents:];
-[SBDisplayLinkController observesBlankingChanges];
-[SBDisplayLinkController _reevaluateForcingFixedRateLinks];
-[SBDisplayLinkController initWithCADisplay:backlight:];
-[SBDisplayLinkController maintainDisplayLinkWhenBacklightIsOffForReason:];
```
