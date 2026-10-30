# `SBMedusaHostedKeyboardWindow`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindow`
- Protocols: `BSInvalidatable`
- 3 instance variables, 5 properties, 20 instance methods, 2 class methods

## Instance variables

```
@"<UIScenePresenter>" _remoteHostedKeyboardScenePresenter;
@"SBMedusaHostedKeyboardWindowLevelAssertion" _defaultWindowLevelAssertion;
@"NSMutableArray" _windowLevelAssertions;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_windowLevelAssertions) windowLevelAssertions;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBMedusaHostedKeyboardWindow _isSecure];
+[SBMedusaHostedKeyboardWindow autorotates];
```

## Instance methods

```
-[SBMedusaHostedKeyboardWindow setHidden:];
-[SBMedusaHostedKeyboardWindow succinctDescriptionBuilder];
-[SBMedusaHostedKeyboardWindow dealloc];
-[SBMedusaHostedKeyboardWindow hitTest:withEvent:];
-[SBMedusaHostedKeyboardWindow descriptionWithMultilinePrefix:];
-[SBMedusaHostedKeyboardWindow succinctDescription];
-[SBMedusaHostedKeyboardWindow invalidate];
-[SBMedusaHostedKeyboardWindow description];
-[SBMedusaHostedKeyboardWindow isActive];
-[SBMedusaHostedKeyboardWindow _shouldControlAutorotation];
-[SBMedusaHostedKeyboardWindow descriptionBuilderWithMultilinePrefix:];
-[SBMedusaHostedKeyboardWindow _updateWindowLevel];
-[SBMedusaHostedKeyboardWindow addWindowLevelAssertion:];
-[SBMedusaHostedKeyboardWindow initWithWindowScene:keyboardScene:];
-[SBMedusaHostedKeyboardWindow medusaHostedKeyboardWindowWillHide:];
-[SBMedusaHostedKeyboardWindow medusaHostedKeyboardWindowWillShow:];
-[SBMedusaHostedKeyboardWindow newWindowLevelAssertionWithPriority:windowLevel:];
-[SBMedusaHostedKeyboardWindow removeWindowLevelAssertion:];
-[SBMedusaHostedKeyboardWindow setWindowLevelAssertions:];
-[SBMedusaHostedKeyboardWindow windowLevelAssertions];
```
