# `_UIEventDeferringBehaviorInternal` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `_UIEventDeferringBehavior`, `BSDebugDescriptionProviding`
- 0 instance variables, 2 properties, 20 instance methods, 1 class methods

## Properties

```
@property (T@"<_UIEventDeferringSystemShellBehaviorDelegate>",W,N) systemShellBehaviorDelegate;
@property (TB,N) systemShellManagesKeyboardFocus;
```

## Class methods

```
+[_UIEventDeferringBehaviorInternal new];
```

## Instance methods

```
-[_UIEventDeferringBehaviorInternal wantsSystemKeyCommandOverlayRules];
-[_UIEventDeferringBehaviorInternal init];
-[_UIEventDeferringBehaviorInternal systemShellBehaviorDelegate];
-[_UIEventDeferringBehaviorInternal setSystemShellBehaviorDelegate:];
-[_UIEventDeferringBehaviorInternal expectsSceneTargetedDeferringRules];
-[_UIEventDeferringBehaviorInternal wantsLocalContainerRules];
-[_UIEventDeferringBehaviorInternal systemShellManagesKeyboardFocus];
-[_UIEventDeferringBehaviorInternal compareRemoteRuleOwningElement:toElement:inEnvironment:];
-[_UIEventDeferringBehaviorInternal eligibleForLocalCompatibilityRuleRemoval];
-[_UIEventDeferringBehaviorInternal initWithEventDeferringManager:];
-[_UIEventDeferringBehaviorInternal isRemoteRuleOwningElement:andContainingWindow:visibleComparedToLocalTargetWindow:];
-[_UIEventDeferringBehaviorInternal setSystemShellManagesKeyboardFocus:];
-[_UIEventDeferringBehaviorInternal shouldAllowFallbackWindowForEnvironment:];
-[_UIEventDeferringBehaviorInternal shouldConsiderKeyWindowChangesForRemoteViewControllerAutomaticEventDeferring];
-[_UIEventDeferringBehaviorInternal shouldDisableRemoteViewControllerEventDeferringForKeyboardKeyWindowChanges];
-[_UIEventDeferringBehaviorInternal shouldDisableRemoteViewControllerEventDeferringForKeyboardSettingsSceneChanges];
-[_UIEventDeferringBehaviorInternal shouldEvaluateEventDeferringForAnyRemoteViewControllerWindowMovement];
-[_UIEventDeferringBehaviorInternal shouldSuppressRemoteRuleForOwningElement:inEnvironment:];
-[_UIEventDeferringBehaviorInternal wantsLocalCompatibilityRules];
-[_UIEventDeferringBehaviorInternal wantsLocalIdealRules];
```
