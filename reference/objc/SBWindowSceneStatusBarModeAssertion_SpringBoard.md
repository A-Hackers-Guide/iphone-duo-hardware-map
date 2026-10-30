# `SBWindowSceneStatusBarModeAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `SBWindowSceneStatusBarAssertion`
- 4 instance variables, 8 properties, 13 instance methods, 0 class methods

## Instance variables

```
q _mode;
@"NSString" _reason;
@"SBWindowSceneStatusBarAssertionManager" _assertionManager;
@"NSDate" _timestamp;
```

## Properties

```
@property (T@"SBWindowSceneStatusBarAssertionManager",R,W,N,V_assertionManager) assertionManager;
@property (Tq,R,N,V_mode) mode;
@property (T@"NSDate",R,C,N,V_timestamp) timestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N,V_reason) reason;
```

## Instance methods

```
-[SBWindowSceneStatusBarModeAssertion assertionManager];
-[SBWindowSceneStatusBarModeAssertion succinctDescriptionBuilder];
-[SBWindowSceneStatusBarModeAssertion init];
-[SBWindowSceneStatusBarModeAssertion dealloc];
-[SBWindowSceneStatusBarModeAssertion timestamp];
-[SBWindowSceneStatusBarModeAssertion descriptionWithMultilinePrefix:];
-[SBWindowSceneStatusBarModeAssertion succinctDescription];
-[SBWindowSceneStatusBarModeAssertion invalidate];
-[SBWindowSceneStatusBarModeAssertion mode];
-[SBWindowSceneStatusBarModeAssertion description];
-[SBWindowSceneStatusBarModeAssertion reason];
-[SBWindowSceneStatusBarModeAssertion descriptionBuilderWithMultilinePrefix:];
-[SBWindowSceneStatusBarModeAssertion _initWithWindowSceneStatusBarAssertionManager:statusBarMode:reason:];
```
