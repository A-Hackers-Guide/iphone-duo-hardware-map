# `AVAudioInterruptionNotificationInternal`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/libSessionUtility.dylib`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__libSessionUtility.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 7 instance methods, 0 class methods

## Instance variables

```
I _interruptionState;
I _sessionOwnerPID;
I _sourceSessionID;
@"NSNumber" _nodeSessionID;
@"NSDictionary" _interruptionInfo;
```

## Properties

```
@property (TI,R,N,V_interruptionState) interruptionState;
@property (TI,R,N,V_sessionOwnerPID) sessionOwnerPID;
@property (TI,R,N,V_sourceSessionID) sourceSessionID;
@property (T@"NSNumber",R,N,V_nodeSessionID) nodeSessionID;
@property (T@"NSDictionary",R,N,V_interruptionInfo) interruptionInfo;
```

## Instance methods

```
-[AVAudioInterruptionNotificationInternal sourceSessionID];
-[AVAudioInterruptionNotificationInternal isEqual:];
-[AVAudioInterruptionNotificationInternal sessionOwnerPID];
-[AVAudioInterruptionNotificationInternal interruptionInfo];
-[AVAudioInterruptionNotificationInternal interruptionState];
-[AVAudioInterruptionNotificationInternal nodeSessionID];
-[AVAudioInterruptionNotificationInternal initWithInterruptionState:sessionOwnerPID:sourceSessionID:nodeSessionID:interruptionInfo:];
```
