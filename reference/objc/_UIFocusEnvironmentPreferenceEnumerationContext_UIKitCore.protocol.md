# `_UIFocusEnvironmentPreferenceEnumerationContext` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"<UIFocusEnvironment>",R,N) environment;
@property (TB,R,N) isPrimaryPreference;
@property (TB,R,N) isLeafPreference;
@property (TB,R,N,GisPreferredByItself) preferredByItself;
@property (TB,R,N) prefersNothingFocused;
@property (T@"<UIFocusEnvironment>",R,N) preferringEnvironment;
@property (T@"NSArray",R,N) preferredEnvironments;
@property (T@"_UIDebugLogStack",R,N) debugStack;
```

## Instance methods

```
-[_UIFocusEnvironmentPreferenceEnumerationContext environment];
-[_UIFocusEnvironmentPreferenceEnumerationContext debugStack];
-[_UIFocusEnvironmentPreferenceEnumerationContext isLeafPreference];
-[_UIFocusEnvironmentPreferenceEnumerationContext isPreferredByItself];
-[_UIFocusEnvironmentPreferenceEnumerationContext isPrimaryPreference];
-[_UIFocusEnvironmentPreferenceEnumerationContext preferredEnvironments];
-[_UIFocusEnvironmentPreferenceEnumerationContext preferringEnvironment];
-[_UIFocusEnvironmentPreferenceEnumerationContext prefersNothingFocused];
```
