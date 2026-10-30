# `SBSwitcherModifierQuerySnapshot`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCAutoCoding`
- 5 instance variables, 9 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _implementingQueryMethods;
@"NSArray" _nonImplementingQueryMethods;
@"NSDictionary" _queryMethodsToDescriptions;
@"NSArray" _contextMethods;
@"NSDictionary" _contextMethodsToDescriptions;
```

## Properties

```
@property (T@"NSArray",R,N,V_implementingQueryMethods) implementingQueryMethods;
@property (T@"NSArray",R,N,V_nonImplementingQueryMethods) nonImplementingQueryMethods;
@property (T@"NSDictionary",R,N,V_queryMethodsToDescriptions) queryMethodsToDescriptions;
@property (T@"NSArray",R,N,V_contextMethods) contextMethods;
@property (T@"NSDictionary",R,N,V_contextMethodsToDescriptions) contextMethodsToDescriptions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSwitcherModifierQuerySnapshot initialize];
```

## Instance methods

```
-[SBSwitcherModifierQuerySnapshot membersForCoder];
-[SBSwitcherModifierQuerySnapshot initWithModifier:];
-[SBSwitcherModifierQuerySnapshot _buildFromModifier:];
-[SBSwitcherModifierQuerySnapshot contextMethods];
-[SBSwitcherModifierQuerySnapshot contextMethodsToDescriptions];
-[SBSwitcherModifierQuerySnapshot implementingQueryMethods];
-[SBSwitcherModifierQuerySnapshot nonImplementingQueryMethods];
-[SBSwitcherModifierQuerySnapshot queryMethodsToDescriptions];
```
