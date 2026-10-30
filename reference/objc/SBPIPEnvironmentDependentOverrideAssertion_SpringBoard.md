# `SBPIPEnvironmentDependentOverrideAssertion`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBPIPBehaviorOverrideAssertion`
- Protocols: `SBLayoutStateTransitionObserver`
- 3 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
B _invalidatesEarly;
@"NSSet" _allowedEnvironmentModes;
```

## Properties

```
@property (TB,N,V_invalidatesEarly) invalidatesEarly;
@property (T@"NSSet",C,N,V_allowedEnvironmentModes) allowedEnvironmentModes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBPIPEnvironmentDependentOverrideAssertion layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBPIPEnvironmentDependentOverrideAssertion dealloc];
-[SBPIPEnvironmentDependentOverrideAssertion _layoutCoordinator];
-[SBPIPEnvironmentDependentOverrideAssertion layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBPIPEnvironmentDependentOverrideAssertion descriptionBuilderWithMultilinePrefix:];
-[SBPIPEnvironmentDependentOverrideAssertion _environmentModeForLayoutState:];
-[SBPIPEnvironmentDependentOverrideAssertion _updateStateForTransitionWithContext:];
-[SBPIPEnvironmentDependentOverrideAssertion allowedEnvironmentModes];
-[SBPIPEnvironmentDependentOverrideAssertion initWithReason:identifier:windowScene:invalidationBlock:];
-[SBPIPEnvironmentDependentOverrideAssertion invalidatesEarly];
-[SBPIPEnvironmentDependentOverrideAssertion setAllowedEnvironmentModes:];
-[SBPIPEnvironmentDependentOverrideAssertion setInvalidatesEarly:];
```
