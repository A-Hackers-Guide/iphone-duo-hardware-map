# `SBSceneSnapshotRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 3 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
Q _size;
Q _orientation;
Q _userInterfaceStyle;
```

## Properties

```
@property (TQ,R,N,V_size) size;
@property (TQ,R,N,V_orientation) orientation;
@property (TQ,R,N,V_userInterfaceStyle) userInterfaceStyle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSceneSnapshotRequest succinctDescriptionBuilder];
-[SBSceneSnapshotRequest orientation];
-[SBSceneSnapshotRequest descriptionWithMultilinePrefix:];
-[SBSceneSnapshotRequest userInterfaceStyle];
-[SBSceneSnapshotRequest size];
-[SBSceneSnapshotRequest succinctDescription];
-[SBSceneSnapshotRequest description];
-[SBSceneSnapshotRequest isEqual:];
-[SBSceneSnapshotRequest descriptionBuilderWithMultilinePrefix:];
-[SBSceneSnapshotRequest initWithSize:orientation:userInterfaceStyle:];
```
