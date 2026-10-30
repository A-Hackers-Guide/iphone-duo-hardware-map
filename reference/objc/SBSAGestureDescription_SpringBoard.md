# `SBSAGestureDescription`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`, `SBSAGestureDescribing`, `NSCopying`, `SBSABlockMutating`
- 3 instance variables, 7 properties, 13 instance methods, 3 class methods

## Instance variables

```
@"NSUUID" _gestureIdentifier;
@"NSUUID" _associatedInterfaceElementIdentifier;
q _gestureRecognizerState;
```

## Properties

```
@property (T@"NSUUID",C,N,S_setGestureIdentifier:,V_gestureIdentifier) gestureIdentifier;
@property (T@"NSUUID",C,N,S_setAssociatedInterfaceElementIdentifier:,V_associatedInterfaceElementIdentifier) associatedInterfaceElementIdentifier;
@property (Tq,N,S_setGestureRecognizerState:,V_gestureRecognizerState) gestureRecognizerState;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSAGestureDescription initialize];
+[SBSAGestureDescription instanceWithBlock:];
+[SBSAGestureDescription mutatorClass];
```

## Instance methods

```
-[SBSAGestureDescription hash];
-[SBSAGestureDescription description];
-[SBSAGestureDescription copyWithZone:];
-[SBSAGestureDescription isEqual:];
-[SBSAGestureDescription copyWithBlock:];
-[SBSAGestureDescription membersForCoder];
-[SBSAGestureDescription _setAssociatedInterfaceElementIdentifier:];
-[SBSAGestureDescription _setGestureIdentifier:];
-[SBSAGestureDescription _setGestureRecognizerState:];
-[SBSAGestureDescription associatedInterfaceElementIdentifier];
-[SBSAGestureDescription gestureIdentifier];
-[SBSAGestureDescription gestureRecognizerState];
-[SBSAGestureDescription initWithGestureDescription:];
```
