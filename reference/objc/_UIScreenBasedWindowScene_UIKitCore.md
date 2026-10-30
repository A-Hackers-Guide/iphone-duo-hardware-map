# `_UIScreenBasedWindowScene`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIWindowScene`
- 7 instance variables, 0 properties, 25 instance methods, 6 class methods

## Instance variables

```
@"<NSCopying>" _lookupKey;
@"UIScreen" _screen;
@"UIMutableApplicationSceneSettings" _synthesizedSettings;
B _invalidationEvaluatorRegistered;
B _needsInvalidation;
@"<BSInvalidatable>" _screenDisconnectionPreventionAssertion;
@"NSMutableSet" _autoInvalidationPreventionAssertions;
```

## Class methods

```
+[_UIScreenBasedWindowScene unassociationCache];
+[_UIScreenBasedWindowScene alwaysKeepContexts];
+[_UIScreenBasedWindowScene autoInvalidates];
+[_UIScreenBasedWindowScene unassociationCacheAccessQueue];
+[_UIScreenBasedWindowScene shouldAllowComponents];
+[_UIScreenBasedWindowScene _unassociatedWindowSceneForScreen:create:];
```

## Instance methods

```
-[_UIScreenBasedWindowScene screen];
-[_UIScreenBasedWindowScene _displayInfoProvider];
-[_UIScreenBasedWindowScene _systemShellHostingEnvironment];
-[_UIScreenBasedWindowScene _invalidate];
-[_UIScreenBasedWindowScene _openURL:options:completionHandler:];
-[_UIScreenBasedWindowScene initWithScreen:session:lookupKey:];
-[_UIScreenBasedWindowScene _screenDisconnected:];
-[_UIScreenBasedWindowScene systemShellHostingEnvironment];
-[_UIScreenBasedWindowScene _referenceBoundsForOrientation:];
-[_UIScreenBasedWindowScene _referenceBounds];
-[_UIScreenBasedWindowScene _attachWindow:];
-[_UIScreenBasedWindowScene setDelegate:];
-[_UIScreenBasedWindowScene _homeAffordanceSceneNotifier];
-[_UIScreenBasedWindowScene _renderingEnvironment];
-[_UIScreenBasedWindowScene _synthesizedSettings];
-[_UIScreenBasedWindowScene _updateClientSettingsToInterfaceOrientation:withAnimationDuration:];
-[_UIScreenBasedWindowScene _addSubclassDebugDescriptionWithBuilder:];
-[_UIScreenBasedWindowScene _primaryViewServiceOperator];
-[_UIScreenBasedWindowScene _detachWindow:];
-[_UIScreenBasedWindowScene _setKeepContextAssociationInBackground:];
-[_UIScreenBasedWindowScene _shouldAllowFencing];
-[_UIScreenBasedWindowScene _addSubclassFlagsToDebugDescriptionWithBuilder:];
-[_UIScreenBasedWindowScene _removeAutoInvalidationPreventionAssertion:];
-[_UIScreenBasedWindowScene _usesMinimumSafeAreaInsets];
-[_UIScreenBasedWindowScene _screenInterfaceOrientationChanged:];
```
