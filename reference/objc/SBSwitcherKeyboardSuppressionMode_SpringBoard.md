# `SBSwitcherKeyboardSuppressionMode`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 2 instance variables, 6 properties, 14 instance methods, 3 class methods

## Instance variables

```
@"NSSet" _appLayouts;
q _type;
```

## Properties

```
@property (Tq,N,V_type) type;
@property (T@"NSSet",R,N,V_appLayouts) appLayouts;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSwitcherKeyboardSuppressionMode newSuppressionModeForSwitcherScenesFromAppLayouts:];
+[SBSwitcherKeyboardSuppressionMode suppressionModeForAllScenes];
+[SBSwitcherKeyboardSuppressionMode suppressionModeNone];
```

## Instance methods

```
-[SBSwitcherKeyboardSuppressionMode appLayouts];
-[SBSwitcherKeyboardSuppressionMode succinctDescriptionBuilder];
-[SBSwitcherKeyboardSuppressionMode descriptionWithMultilinePrefix:];
-[SBSwitcherKeyboardSuppressionMode succinctDescription];
-[SBSwitcherKeyboardSuppressionMode setType:];
-[SBSwitcherKeyboardSuppressionMode type];
-[SBSwitcherKeyboardSuppressionMode hash];
-[SBSwitcherKeyboardSuppressionMode description];
-[SBSwitcherKeyboardSuppressionMode isEqual:];
-[SBSwitcherKeyboardSuppressionMode descriptionBuilderWithMultilinePrefix:];
-[SBSwitcherKeyboardSuppressionMode _initWithAppLayouts:suppressionType:];
-[SBSwitcherKeyboardSuppressionMode suppressesAllScenes];
-[SBSwitcherKeyboardSuppressionMode suppressesNoScenes];
-[SBSwitcherKeyboardSuppressionMode suppressesSwitcherScenesOnly];
```
