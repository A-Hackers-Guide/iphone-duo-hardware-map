# `SBSwitcherModifierEventSnapshot`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`
- 2 instance variables, 6 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSString" _eventName;
@"NSString" _eventDescription;
```

## Properties

```
@property (T@"NSString",R,N,V_eventName) eventName;
@property (T@"NSString",R,N,V_eventDescription) eventDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSwitcherModifierEventSnapshot initialize];
```

## Instance methods

```
-[SBSwitcherModifierEventSnapshot initWithEvent:];
-[SBSwitcherModifierEventSnapshot eventName];
-[SBSwitcherModifierEventSnapshot eventDescription];
-[SBSwitcherModifierEventSnapshot membersForCoder];
```
