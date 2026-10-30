# `SBSAElementSnapshotContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `NSCopying`, `SAElementIdentifying`, `SAUISnapshotReasonProviding`, `SBSABlockMutating`
- 3 instance variables, 7 properties, 13 instance methods, 3 class methods

## Instance variables

```
@"NSString" _clientIdentifier;
@"NSString" _elementIdentifier;
@"NSString" _snapshotReason;
```

## Properties

```
@property (T@"NSString",C,N,S_setClientIdentifier:,V_clientIdentifier) clientIdentifier;
@property (T@"NSString",C,N,S_setElementIdentifier:,V_elementIdentifier) elementIdentifier;
@property (T@"NSString",C,N,S_setSnapshotReason:,V_snapshotReason) snapshotReason;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAElementSnapshotContext initialize];
+[SBSAElementSnapshotContext instanceWithBlock:];
+[SBSAElementSnapshotContext mutatorClass];
```

## Instance methods

```
-[SBSAElementSnapshotContext clientIdentifier];
-[SBSAElementSnapshotContext snapshotReason];
-[SBSAElementSnapshotContext elementIdentifier];
-[SBSAElementSnapshotContext hash];
-[SBSAElementSnapshotContext description];
-[SBSAElementSnapshotContext copyWithZone:];
-[SBSAElementSnapshotContext isEqual:];
-[SBSAElementSnapshotContext copyWithBlock:];
-[SBSAElementSnapshotContext membersForCoder];
-[SBSAElementSnapshotContext _setClientIdentifier:];
-[SBSAElementSnapshotContext _setElementIdentifier:];
-[SBSAElementSnapshotContext _setSnapshotReason:];
-[SBSAElementSnapshotContext initWithSnapshotIdentity:];
```
