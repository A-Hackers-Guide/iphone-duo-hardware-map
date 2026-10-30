# `BWSinkNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 10 instance variables, 5 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"FigStateMachine" _stateMachine;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _stateLock;
@"NSMutableArray" _handlersToCallWhenIdle;
@"NSMutableArray" _handlersToCallWhenActive;
@"NSString" _sinkID;
^{OpaqueFigSimpleMutex=} _configurationHandlerLock;
q _liveConfigurationID;
^q _liveConfigurationIDsByInputIndex;
@"NSMutableArray" _configurationLiveHandlers;
@"NSMutableArray" _configurationLiveIDs;
```

## Properties

```
@property (T@"NSString",R,C,N,V_sinkID) sinkID;
@property (T@"NSString",R) currentStateDebugString;
@property (TB,R) isActive;
@property (TB,R) isIdle;
@property (Tq,R) liveConfigurationID;
```

## Class methods

```
+[BWSinkNode initialize];
```

## Instance methods

```
-[BWSinkNode initWithSinkID:];
-[BWSinkNode liveConfigurationID];
-[BWSinkNode isIdle];
-[BWSinkNode dealloc];
-[BWSinkNode didReachEndOfDataForConfigurationID:input:];
-[BWSinkNode isActive];
-[BWSinkNode addOutput:];
-[BWSinkNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWSinkNode sinkID];
-[BWSinkNode nodeType];
-[BWSinkNode notifyWhenIdle:];
-[BWSinkNode currentStateDebugString];
-[BWSinkNode didReachEndOfDataForInput:];
-[BWSinkNode notifyWhenActive:];
-[BWSinkNode notifyWhenConfigurationID:becomesLive:];
```
