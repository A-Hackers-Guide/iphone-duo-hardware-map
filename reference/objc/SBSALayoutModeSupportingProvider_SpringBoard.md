# `SBSALayoutModeSupportingProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 2 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"SBSALayoutTransitionProvider" _activeTransitionProvider;
@"SBSAElementRemovalTransitionProvider" _elementRemovalTransitionProvider;
```

## Class methods

```
+[SBSALayoutModeSupportingProvider initialize];
```

## Instance methods

```
-[SBSALayoutModeSupportingProvider membersForCoder];
-[SBSALayoutModeSupportingProvider _firstElementLayoutModeSupportingProvider];
-[SBSALayoutModeSupportingProvider _transitionToLayoutModeIfNecessary:customLayoutCustomizingOptions:context:];
-[SBSALayoutModeSupportingProvider preferencesFromContext:];
```
