# `_UIDeepestPreferredEnvironmentSearch`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _allowsOverridingPreferedFocusEnvironments;
@"_UIDebugLogNode" _debugLog;
```

## Properties

```
@property (TB,N,V_allowsOverridingPreferedFocusEnvironments) allowsOverridingPreferedFocusEnvironments;
@property (T@"_UIDebugLogNode",&,N,V_debugLog) debugLog;
```

## Instance methods

```
-[_UIDeepestPreferredEnvironmentSearch _overridingPreferredFocusEnvironmentForPreferredEnvironment:visitedFocusEnvironments:];
-[_UIDeepestPreferredEnvironmentSearch _reportDidFindLockedFocusEnvironment:];
-[_UIDeepestPreferredEnvironmentSearch _reportDidFindOverridingPreferredFocusEnvironment:source:];
-[_UIDeepestPreferredEnvironmentSearch _reportDidFinishEnumeratingPreferencesWithDeepestPreferredFocusableItem:];
-[_UIDeepestPreferredEnvironmentSearch _reportFinishedEvaluatingAllPreferencesForEnvironmentInContext:result:];
-[_UIDeepestPreferredEnvironmentSearch _reportFoundFocusableItem:inContext:];
-[_UIDeepestPreferredEnvironmentSearch _reportStartingSearch];
-[_UIDeepestPreferredEnvironmentSearch allowsOverridingPreferedFocusEnvironments];
-[_UIDeepestPreferredEnvironmentSearch debugLog];
-[_UIDeepestPreferredEnvironmentSearch deepestPreferredFocusEnvironmentForEnvironment:];
-[_UIDeepestPreferredEnvironmentSearch deepestPreferredFocusableItemForEnvironment:withRequest:];
-[_UIDeepestPreferredEnvironmentSearch setAllowsOverridingPreferedFocusEnvironments:];
-[_UIDeepestPreferredEnvironmentSearch setDebugLog:];
```
