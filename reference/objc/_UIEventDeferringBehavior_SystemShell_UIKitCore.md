# `_UIEventDeferringBehavior_SystemShell`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIEventDeferringBehavior_Default`
- Protocols: `BSDebugDescriptionProviding`
- 2 instance variables, 9 properties, 14 instance methods, 0 class methods

## Instance variables

```
{?="hasSystemShellBehaviorDelegate"b1"delegateWantsLocalCompatibilityRules"b1"delegateShouldSuppressRemoteRule"b1"delegateCompareRemoteRules"b1"delegateEvaluatesVisibilityOfRemoteRuleWindow"b1} _behaviorDelegateFlags;
@"<_UIEventDeferringSystemShellBehaviorDelegate>" _systemShellBehaviorDelegate;
```

## Properties

```
@property (TB,R,N) hasSystemShellDelegate;
@property (TB,R,N) systemShellBehaviorDelegateImplementsWantsLocalCompatibilityRules;
@property (TB,R,N) systemShellBehaviorDelegateImplementsShouldSuppressRemoteRule;
@property (TB,R,N) systemShellBehaviorDelegateImplementsComparisonOfRemoteRules;
@property (TB,R,N) systemShellBehaviorDelegateImplementsVisibilityOfRemoteRuleWindow;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIEventDeferringBehavior_SystemShell systemShellBehaviorDelegate];
-[_UIEventDeferringBehavior_SystemShell setSystemShellBehaviorDelegate:];
-[_UIEventDeferringBehavior_SystemShell descriptionBuilderWithMultilinePrefix:];
-[_UIEventDeferringBehavior_SystemShell compareRemoteRuleOwningElement:toElement:inEnvironment:];
-[_UIEventDeferringBehavior_SystemShell hasSystemShellDelegate];
-[_UIEventDeferringBehavior_SystemShell initWithEventDeferringManager:];
-[_UIEventDeferringBehavior_SystemShell isRemoteRuleOwningElement:andContainingWindow:visibleComparedToLocalTargetWindow:];
-[_UIEventDeferringBehavior_SystemShell shouldDisableRemoteViewControllerEventDeferringForKeyboardKeyWindowChanges];
-[_UIEventDeferringBehavior_SystemShell shouldSuppressRemoteRuleForOwningElement:inEnvironment:];
-[_UIEventDeferringBehavior_SystemShell systemShellBehaviorDelegateImplementsComparisonOfRemoteRules];
-[_UIEventDeferringBehavior_SystemShell systemShellBehaviorDelegateImplementsShouldSuppressRemoteRule];
-[_UIEventDeferringBehavior_SystemShell systemShellBehaviorDelegateImplementsVisibilityOfRemoteRuleWindow];
-[_UIEventDeferringBehavior_SystemShell systemShellBehaviorDelegateImplementsWantsLocalCompatibilityRules];
-[_UIEventDeferringBehavior_SystemShell wantsLocalCompatibilityRules];
```
