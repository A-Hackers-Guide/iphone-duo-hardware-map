# `_UIFocusEnvironmentPreferenceEnumerator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFocusEnvironmentPreferenceEnumerationContextDelegate`
- 5 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
B _allowsInferringPreferences;
q _enumerationMode;
@? _didVisitAllPreferencesForEnvironmentHandler;
@? _shouldInferPreferenceForEnvironmentHandler;
@"_UIDebugLogNode" _debugLog;
```

## Properties

```
@property (Tq,R,N,V_enumerationMode) enumerationMode;
@property (T@?,C,N,V_didVisitAllPreferencesForEnvironmentHandler) didVisitAllPreferencesForEnvironmentHandler;
@property (TB,N,V_allowsInferringPreferences) allowsInferringPreferences;
@property (T@?,C,N,V_shouldInferPreferenceForEnvironmentHandler) shouldInferPreferenceForEnvironmentHandler;
@property (T@"_UIDebugLogNode",&,N,V_debugLog) debugLog;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFocusEnvironmentPreferenceEnumerator init];
-[_UIFocusEnvironmentPreferenceEnumerator enumerationMode];
-[_UIFocusEnvironmentPreferenceEnumerator _shouldInferDefaultPreferenceForEnvironmentInContext:];
-[_UIFocusEnvironmentPreferenceEnumerator allowsInferringPreferences];
-[_UIFocusEnvironmentPreferenceEnumerator debugLog];
-[_UIFocusEnvironmentPreferenceEnumerator didVisitAllPreferencesForEnvironmentHandler];
-[_UIFocusEnvironmentPreferenceEnumerator enumeratePreferencesForEnvironment:usingBlock:];
-[_UIFocusEnvironmentPreferenceEnumerator initWithEnumerationMode:];
-[_UIFocusEnvironmentPreferenceEnumerator setAllowsInferringPreferences:];
-[_UIFocusEnvironmentPreferenceEnumerator setDebugLog:];
-[_UIFocusEnvironmentPreferenceEnumerator setDidVisitAllPreferencesForEnvironmentHandler:];
-[_UIFocusEnvironmentPreferenceEnumerator setShouldInferPreferenceForEnvironmentHandler:];
-[_UIFocusEnvironmentPreferenceEnumerator shouldInferPreferenceForEnvironmentHandler];
```
