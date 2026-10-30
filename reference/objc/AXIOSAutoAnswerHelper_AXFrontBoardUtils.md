# `AXIOSAutoAnswerHelper`

- Image: [`/System/Library/PrivateFrameworks/AXFrontBoardUtils.framework/AXFrontBoardUtils`](../userland/System__Library__PrivateFrameworks__AXFrontBoardUtils.framework__AXFrontBoardUtils.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AXIDSServicesClient`
- 3 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"CHHapticEngine" _hapticEngine;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _watchActiveWristStateLock;
@"NSMutableDictionary" _watchActiveWristState;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_watchActiveWristState) watchActiveWristState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AXIOSAutoAnswerHelper init];
-[AXIOSAutoAnswerHelper didReceiveIncomingData:];
-[AXIOSAutoAnswerHelper handleIncomingCallStateChangedWithRingerMuted:];
-[AXIOSAutoAnswerHelper _initializeAutoAnswerWatchObserver];
-[AXIOSAutoAnswerHelper _performBlockAsynchronously:afterDelay:];
-[AXIOSAutoAnswerHelper _playSafetySoundAndHapticWithRingerMuted:];
-[AXIOSAutoAnswerHelper _requestOnWristState];
-[AXIOSAutoAnswerHelper setWatchActiveWristState:];
-[AXIOSAutoAnswerHelper shouldAllowActiveWatchToAutoAnswer];
-[AXIOSAutoAnswerHelper watchActiveWristState];
```
