# `_UISceneHostingLegacyEventDeferringClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `_UISceneHostingLegacyEventDeferringClientProviding_Internal`
- 0 instance variables, 2 properties, 10 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) requestEventDeferralForAllFirstResponderChanges;
@property (TB,R,N) avoidsRegisteringTopLevelAppKeyboardShortcuts;
```

## Instance methods

```
-[_UISceneHostingLegacyEventDeferringClientComponent setScene:];
-[_UISceneHostingLegacyEventDeferringClientComponent invalidate];
-[_UISceneHostingLegacyEventDeferringClientComponent firstResponderDidChange:];
-[_UISceneHostingLegacyEventDeferringClientComponent wantsKeyboardEvents:];
-[_UISceneHostingLegacyEventDeferringClientComponent requestEventDeferralForAllFirstResponderChanges];
-[_UISceneHostingLegacyEventDeferringClientComponent avoidsRegisteringTopLevelAppKeyboardShortcuts];
-[_UISceneHostingLegacyEventDeferringClientComponent beginObservingNotifications];
-[_UISceneHostingLegacyEventDeferringClientComponent requestKeyboardFocus];
-[_UISceneHostingLegacyEventDeferringClientComponent requestKeyboardFocusFromHostIfWindowFirstResponderIsEligibleForKeyboardFocus:];
-[_UISceneHostingLegacyEventDeferringClientComponent stopObservingNotifications];
```
