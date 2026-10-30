# `SBSwitcherModifierTimelineEntry`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`
- 3 instance variables, 7 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"SBSwitcherModifierEventSnapshot" _eventSnapshot;
@"SBSwitcherModifierStackSnapshot" _stackSnapshotAfterEvent;
@"SBSwitcherModifierEventResponseSnapshot" _responseSnapshot;
```

## Properties

```
@property (T@"SBSwitcherModifierEventSnapshot",R,N,V_eventSnapshot) eventSnapshot;
@property (T@"SBSwitcherModifierStackSnapshot",R,N,V_stackSnapshotAfterEvent) stackSnapshotAfterEvent;
@property (T@"SBSwitcherModifierEventResponseSnapshot",R,N,V_responseSnapshot) responseSnapshot;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSwitcherModifierTimelineEntry initialize];
```

## Instance methods

```
-[SBSwitcherModifierTimelineEntry membersForCoder];
-[SBSwitcherModifierTimelineEntry initWithEventSnapshot:responseSnapshot:stackSnapshotAfterEvent:];
-[SBSwitcherModifierTimelineEntry eventSnapshot];
-[SBSwitcherModifierTimelineEntry responseSnapshot];
-[SBSwitcherModifierTimelineEntry stackSnapshotAfterEvent];
```
