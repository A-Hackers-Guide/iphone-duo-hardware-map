# `SBTraitsSceneOrientationRequestsAssistant`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBTraitsSceneParticipantDelegate" _traitsDelegate;
@"NSString" _errorDomain;
```

## Properties

```
@property (T@"SBTraitsSceneParticipantDelegate",R,W,N,V_traitsDelegate) traitsDelegate;
@property (T@"NSString",R,W,N,V_errorDomain) errorDomain;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBTraitsSceneOrientationRequestsAssistant invalidate];
-[SBTraitsSceneOrientationRequestsAssistant errorDomain];
-[SBTraitsSceneOrientationRequestsAssistant _startSceneOrientationRequestWithDesiredOrientations:error:];
-[SBTraitsSceneOrientationRequestsAssistant checkValidityAgainstUpdateReasons:];
-[SBTraitsSceneOrientationRequestsAssistant coalescedNotifyArbitrationUpdateNeeded:withReason:];
-[SBTraitsSceneOrientationRequestsAssistant initWithTraitsSceneDelegate:errorDomain:];
-[SBTraitsSceneOrientationRequestsAssistant setUpForTransitionContextIfNeeded:];
-[SBTraitsSceneOrientationRequestsAssistant traitsDelegate];
```
