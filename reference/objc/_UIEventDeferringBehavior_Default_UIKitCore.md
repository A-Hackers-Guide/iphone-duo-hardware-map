# `_UIEventDeferringBehavior_Default`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIEventDeferringBehaviorInternal`
- 3 instance variables, 7 properties, 28 instance methods, 0 class methods

## Instance variables

```
{?="systemShellManagesKeyboardFocus"b1} _behaviorFlags;
@"_UIEventDeferringManager" _eventDeferringManager;
@"<_UIEventDeferringSystemShellBehaviorDelegate>" _systemShellBehaviorDelegate;
```

## Properties

```
@property (T@"<_UIEventDeferringSystemShellBehaviorDelegate>",W,N,V_systemShellBehaviorDelegate) systemShellBehaviorDelegate;
@property (TB,N) systemShellManagesKeyboardFocus;
@property (T@"_UIEventDeferringManager",R,W,N,V_eventDeferringManager) eventDeferringManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIEventDeferringBehavior_Default wantsSystemKeyCommandOverlayRules];
-[_UIEventDeferringBehavior_Default debugDescription];
-[_UIEventDeferringBehavior_Default succinctDescriptionBuilder];
-[_UIEventDeferringBehavior_Default init];
-[_UIEventDeferringBehavior_Default descriptionWithMultilinePrefix:];
-[_UIEventDeferringBehavior_Default succinctDescription];
-[_UIEventDeferringBehavior_Default debugDescriptionWithMultilinePrefix:];
-[_UIEventDeferringBehavior_Default systemShellBehaviorDelegate];
-[_UIEventDeferringBehavior_Default description];
-[_UIEventDeferringBehavior_Default setSystemShellBehaviorDelegate:];
-[_UIEventDeferringBehavior_Default expectsSceneTargetedDeferringRules];
-[_UIEventDeferringBehavior_Default wantsLocalContainerRules];
-[_UIEventDeferringBehavior_Default descriptionBuilderWithMultilinePrefix:];
-[_UIEventDeferringBehavior_Default systemShellManagesKeyboardFocus];
-[_UIEventDeferringBehavior_Default compareRemoteRuleOwningElement:toElement:inEnvironment:];
-[_UIEventDeferringBehavior_Default eligibleForLocalCompatibilityRuleRemoval];
-[_UIEventDeferringBehavior_Default eventDeferringManager];
-[_UIEventDeferringBehavior_Default initWithEventDeferringManager:];
-[_UIEventDeferringBehavior_Default isRemoteRuleOwningElement:andContainingWindow:visibleComparedToLocalTargetWindow:];
-[_UIEventDeferringBehavior_Default setSystemShellManagesKeyboardFocus:];
-[_UIEventDeferringBehavior_Default shouldAllowFallbackWindowForEnvironment:];
-[_UIEventDeferringBehavior_Default shouldConsiderKeyWindowChangesForRemoteViewControllerAutomaticEventDeferring];
-[_UIEventDeferringBehavior_Default shouldDisableRemoteViewControllerEventDeferringForKeyboardKeyWindowChanges];
-[_UIEventDeferringBehavior_Default shouldDisableRemoteViewControllerEventDeferringForKeyboardSettingsSceneChanges];
-[_UIEventDeferringBehavior_Default shouldEvaluateEventDeferringForAnyRemoteViewControllerWindowMovement];
-[_UIEventDeferringBehavior_Default shouldSuppressRemoteRuleForOwningElement:inEnvironment:];
-[_UIEventDeferringBehavior_Default wantsLocalCompatibilityRules];
-[_UIEventDeferringBehavior_Default wantsLocalIdealRules];
```
