# `SBSwitcherModifierStackSnapshot`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`
- 4 instance variables, 8 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSString" _modifierName;
@"NSString" _modifierDescription;
@"SBSwitcherModifierQuerySnapshot" _querySnapshot;
@"NSArray" _childSnapshots;
```

## Properties

```
@property (T@"NSString",R,C,N,V_modifierName) modifierName;
@property (T@"NSString",R,C,N,V_modifierDescription) modifierDescription;
@property (T@"SBSwitcherModifierQuerySnapshot",R,C,N,V_querySnapshot) querySnapshot;
@property (T@"NSArray",R,C,N,V_childSnapshots) childSnapshots;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSwitcherModifierStackSnapshot initialize];
```

## Instance methods

```
-[SBSwitcherModifierStackSnapshot initWithRootModifier:];
-[SBSwitcherModifierStackSnapshot membersForCoder];
-[SBSwitcherModifierStackSnapshot modifierDescription];
-[SBSwitcherModifierStackSnapshot _enumerateModifierSnapshots:stop:];
-[SBSwitcherModifierStackSnapshot childSnapshots];
-[SBSwitcherModifierStackSnapshot countOfAllChildSnapshots];
-[SBSwitcherModifierStackSnapshot enumerateModifierSnapshots:];
-[SBSwitcherModifierStackSnapshot modifierName];
-[SBSwitcherModifierStackSnapshot querySnapshot];
```
