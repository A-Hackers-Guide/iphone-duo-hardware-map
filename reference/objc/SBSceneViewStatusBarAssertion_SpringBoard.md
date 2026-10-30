# `SBSceneViewStatusBarAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 4 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
q _nubViewHidden;
@"SBStatusBarSettings" _settings;
Q _level;
```

## Properties

```
@property (TB,N,GisStatusBarHidden) statusBarHidden;
@property (Tq,N,V_nubViewHidden) nubViewHidden;
@property (T@"SBStatusBarSettings",C,N,V_settings) settings;
@property (TQ,R,N,V_level) level;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSceneViewStatusBarAssertion succinctDescriptionBuilder];
-[SBSceneViewStatusBarAssertion setSettings:];
-[SBSceneViewStatusBarAssertion removeObserver:];
-[SBSceneViewStatusBarAssertion settings];
-[SBSceneViewStatusBarAssertion dealloc];
-[SBSceneViewStatusBarAssertion level];
-[SBSceneViewStatusBarAssertion descriptionWithMultilinePrefix:];
-[SBSceneViewStatusBarAssertion succinctDescription];
-[SBSceneViewStatusBarAssertion addObserver:];
-[SBSceneViewStatusBarAssertion invalidate];
-[SBSceneViewStatusBarAssertion description];
-[SBSceneViewStatusBarAssertion descriptionBuilderWithMultilinePrefix:];
-[SBSceneViewStatusBarAssertion isStatusBarHidden];
-[SBSceneViewStatusBarAssertion setStatusBarHidden:];
-[SBSceneViewStatusBarAssertion _notifyObserversDidInvalidate];
-[SBSceneViewStatusBarAssertion _notifyObserversDidUpdate];
-[SBSceneViewStatusBarAssertion initWithStatusBarHidden:nubViewHidden:atLevel:];
-[SBSceneViewStatusBarAssertion initWithStatusBarSettings:nubViewHidden:atLevel:];
-[SBSceneViewStatusBarAssertion nubViewHidden];
-[SBSceneViewStatusBarAssertion setNubViewHidden:];
```
