# `SBSwitcherDisplayItemRemovalResolutionResultAction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 4 instance methods, 2 class methods

## Instance variables

```
q _actionType;
@"SBAppLayout" _appLayout;
@"SBAppLayout" _replacementAppLayout;
```

## Properties

```
@property (Tq,R,N,V_actionType) actionType;
@property (T@"SBAppLayout",R,C,N,V_appLayout) appLayout;
@property (T@"SBAppLayout",R,C,N,V_replacementAppLayout) replacementAppLayout;
```

## Class methods

```
+[SBSwitcherDisplayItemRemovalResolutionResultAction defaultRemovalPolicyActionWithAppLayout:];
+[SBSwitcherDisplayItemRemovalResolutionResultAction replacementActionWithAppLayout:replacementAppLayout:];
```

## Instance methods

```
-[SBSwitcherDisplayItemRemovalResolutionResultAction appLayout];
-[SBSwitcherDisplayItemRemovalResolutionResultAction actionType];
-[SBSwitcherDisplayItemRemovalResolutionResultAction _initWithAppLayout:actionType:];
-[SBSwitcherDisplayItemRemovalResolutionResultAction replacementAppLayout];
```
