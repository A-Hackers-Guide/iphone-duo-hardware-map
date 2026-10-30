# `_UISceneHostingLegacyEventDeferringHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `FBSceneObserver`, `_UISceneHostingEventDeferringHostProviding_Internal`
- 4 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
{?="pendingRulesWhenEligible"b1"maintainHostFirstResponderWhenClientWantsKeyboard"b1} _flags;
@"_UIEventDeferringOwnershipToken" _eventDeferringOwnershipToken;
@"UIScene<_UISceneUIWindowHosting>" _eventDeferringParentScene;
@"UIScene<_UISceneUIWindowHosting>" _parentScenePendingEventDeferringRules;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N) maintainHostFirstResponderWhenClientWantsKeyboard;
@property (TB,N) requestEventDeferralForAllFirstResponderChanges;
```

## Instance methods

```
-[_UISceneHostingLegacyEventDeferringHostComponent scene:clientDidConnect:];
-[_UISceneHostingLegacyEventDeferringHostComponent sceneWillDeactivate:withContext:];
-[_UISceneHostingLegacyEventDeferringHostComponent scene:handleActions:];
-[_UISceneHostingLegacyEventDeferringHostComponent setScene:];
-[_UISceneHostingLegacyEventDeferringHostComponent setRequestEventDeferralForAllFirstResponderChanges:];
-[_UISceneHostingLegacyEventDeferringHostComponent invalidate];
-[_UISceneHostingLegacyEventDeferringHostComponent firstResponderDidChange:];
-[_UISceneHostingLegacyEventDeferringHostComponent _scene:isMovingToParent:];
-[_UISceneHostingLegacyEventDeferringHostComponent setMaintainHostFirstResponderWhenClientWantsKeyboard:];
-[_UISceneHostingLegacyEventDeferringHostComponent maintainHostFirstResponderWhenClientWantsKeyboard];
-[_UISceneHostingLegacyEventDeferringHostComponent requestEventDeferralForAllFirstResponderChanges];
-[_UISceneHostingLegacyEventDeferringHostComponent forceBeginDeferring];
```
