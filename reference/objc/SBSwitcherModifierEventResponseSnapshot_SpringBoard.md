# `SBSwitcherModifierEventResponseSnapshot`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`
- 2 instance variables, 6 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _responseNames;
@"NSArray" _responseDescriptions;
```

## Properties

```
@property (T@"NSArray",R,N,V_responseNames) responseNames;
@property (T@"NSArray",R,N,V_responseDescriptions) responseDescriptions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSwitcherModifierEventResponseSnapshot initialize];
```

## Instance methods

```
-[SBSwitcherModifierEventResponseSnapshot membersForCoder];
-[SBSwitcherModifierEventResponseSnapshot initWithEventResponse:];
-[SBSwitcherModifierEventResponseSnapshot responseDescriptions];
-[SBSwitcherModifierEventResponseSnapshot responseNames];
```
