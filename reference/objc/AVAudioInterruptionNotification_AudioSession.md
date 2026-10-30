# `AVAudioInterruptionNotification`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 6 instance methods, 0 class methods

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
-[AVAudioInterruptionNotification sourceSessionID];
-[AVAudioInterruptionNotification initWithInternal:];
-[AVAudioInterruptionNotification sessionOwnerPID];
-[AVAudioInterruptionNotification interruptionInfo];
-[AVAudioInterruptionNotification interruptionState];
-[AVAudioInterruptionNotification nodeSessionID];
```
