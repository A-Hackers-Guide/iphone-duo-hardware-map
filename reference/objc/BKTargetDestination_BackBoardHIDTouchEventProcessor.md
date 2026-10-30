# `BKTargetDestination`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDTouchEventProcessor.framework/BackBoardHIDTouchEventProcessor`](../userland/System__Library__PrivateFrameworks__BackBoardHIDTouchEventProcessor.framework__BackBoardHIDTouchEventProcessor.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSDescriptionStreamable`, `BKTouchLifecycleDestination`
- 4 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
{?="contextID"I} _targetID;
I _clientTaskName;
Q _clientConnectionIdentifier;
@"BKSSceneHostSettings" _inheritedSceneHostSettings;
```

## Properties

```
@property (T{?=I},N,V_targetID) targetID;
@property (TI,N,V_clientTaskName) clientTaskName;
@property (TQ,N,V_clientConnectionIdentifier) clientConnectionIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKTargetDestination appendSuccinctDescriptionToFormatter:];
-[BKTargetDestination appendDescriptionToFormatter:];
-[BKTargetDestination setTargetID:];
-[BKTargetDestination succinctDescription];
-[BKTargetDestination targetID];
-[BKTargetDestination hash];
-[BKTargetDestination description];
-[BKTargetDestination copyWithZone:];
-[BKTargetDestination isEqual:];
-[BKTargetDestination clientConnectionIdentifier];
-[BKTargetDestination clientTaskName];
-[BKTargetDestination initWithTargetID:clientTaskName:];
-[BKTargetDestination initWithTargetID:clientTaskName:clientConnectionIdentifier:];
-[BKTargetDestination setClientConnectionIdentifier:];
-[BKTargetDestination setClientTaskName:];
```
