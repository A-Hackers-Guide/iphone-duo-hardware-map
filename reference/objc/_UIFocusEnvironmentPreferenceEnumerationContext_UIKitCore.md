# `_UIFocusEnvironmentPreferenceEnumerationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFocusEnvironmentPreferenceEnumerationContext`
- 14 instance variables, 14 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"UIFocusSystem" _focusSystem;
@"<UIFocusEnvironment>" _preferredSubtree;
@"NSMutableArray" _visitedEnvironmentStack;
@"<UIFocusEnvironment>" _lastPrimaryPreferredEnvironment;
@"NSArray" _cachedPreferredEnvironments;
@"NSHashTable" _allVisitedEnvironments;
B _hasResolvedPreferredFocusEnvironments;
B _hasNeverPoppedInPreferredSubtree;
@"<UIFocusEnvironment>" _preferredSubtreeEntryPoint;
@"NSMapTable" _preferredEnvironmentsMap;
B _cachedPrefersNothingFocused;
@"<UIFocusEnvironment>" _environment;
@"<_UIFocusEnvironmentPreferenceEnumerationContextDelegate>" _delegate;
@"_UIDebugLogStack" _debugStack;
```

## Properties

```
@property (T@"<_UIFocusEnvironmentPreferenceEnumerationContextDelegate>",W,N,V_delegate) delegate;
@property (T@"_UIDebugLogStack",&,N,V_debugStack) debugStack;
@property (TB,R,N,GisInPreferredSubtree) inPreferredSubtree;
@property (T@"<UIFocusEnvironment>",R,N,V_environment) environment;
@property (TB,R,N) isPrimaryPreference;
@property (TB,R,N) isLeafPreference;
@property (TB,R,N,GisPreferredByItself) preferredByItself;
@property (TB,R,N,V_cachedPrefersNothingFocused) prefersNothingFocused;
@property (T@"<UIFocusEnvironment>",R,N) preferringEnvironment;
@property (T@"NSArray",R,N) preferredEnvironments;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFocusEnvironmentPreferenceEnumerationContext init];
-[_UIFocusEnvironmentPreferenceEnumerationContext setDelegate:];
-[_UIFocusEnvironmentPreferenceEnumerationContext delegate];
-[_UIFocusEnvironmentPreferenceEnumerationContext environment];
-[_UIFocusEnvironmentPreferenceEnumerationContext _inferPreferencesForEnvironment:];
-[_UIFocusEnvironmentPreferenceEnumerationContext _invalidatePreferredEnvironments];
-[_UIFocusEnvironmentPreferenceEnumerationContext _isAllowedToPreferEnvironment:];
-[_UIFocusEnvironmentPreferenceEnumerationContext _reportInferredPreferredFocusEnvironment:];
-[_UIFocusEnvironmentPreferenceEnumerationContext _resolvePreferredFocusEnvironments];
-[_UIFocusEnvironmentPreferenceEnumerationContext _startLogging];
-[_UIFocusEnvironmentPreferenceEnumerationContext _stopLogging];
-[_UIFocusEnvironmentPreferenceEnumerationContext debugStack];
-[_UIFocusEnvironmentPreferenceEnumerationContext initWithFocusEnvironment:enumerationMode:];
-[_UIFocusEnvironmentPreferenceEnumerationContext isInPreferredSubtree];
-[_UIFocusEnvironmentPreferenceEnumerationContext isLeafPreference];
-[_UIFocusEnvironmentPreferenceEnumerationContext isPreferredByItself];
-[_UIFocusEnvironmentPreferenceEnumerationContext isPrimaryPreference];
-[_UIFocusEnvironmentPreferenceEnumerationContext popEnvironment];
-[_UIFocusEnvironmentPreferenceEnumerationContext preferredEnvironments];
-[_UIFocusEnvironmentPreferenceEnumerationContext preferringEnvironment];
-[_UIFocusEnvironmentPreferenceEnumerationContext prefersNothingFocused];
-[_UIFocusEnvironmentPreferenceEnumerationContext pushEnvironment:];
-[_UIFocusEnvironmentPreferenceEnumerationContext setDebugStack:];
```
