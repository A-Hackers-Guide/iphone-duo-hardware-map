# `SBScreenBrightnessParticipant`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBScreenBrightnessDisplayClientObserver`, `BSInvalidatable`
- 6 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<SBScreenBrightnessObserving>" _observer;
@"SBScreenBrightnessCoordinator" _coordinator;
@"SBScreenBrightnessDisplayClient" _displayClient;
@"SBScreenBrightnessRequest" _request;
B _invalidated;
d _preferredBrightness;
```

## Properties

```
@property (Td,N,V_preferredBrightness) preferredBrightness;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBScreenBrightnessParticipant dealloc];
-[SBScreenBrightnessParticipant invalidate];
-[SBScreenBrightnessParticipant _clearBrightnessRequest];
-[SBScreenBrightnessParticipant _updateBrightnessRequest];
-[SBScreenBrightnessParticipant _updateDisplayClient:];
-[SBScreenBrightnessParticipant displayClient:brightnessDidChange:];
-[SBScreenBrightnessParticipant displayClient:sanitizedBrightnessDidChange:];
-[SBScreenBrightnessParticipant displayClientDidInvalidate:];
-[SBScreenBrightnessParticipant initWithObserver:coordinator:];
-[SBScreenBrightnessParticipant preferredBrightness];
-[SBScreenBrightnessParticipant resignWindowScene];
-[SBScreenBrightnessParticipant setPreferredBrightness:];
-[SBScreenBrightnessParticipant updateWindowScene:];
```
