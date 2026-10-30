# `SBSAElementRemovalTransitionProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- 5 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"<SBSAStackablePreferencesProviding>" _elementContentProvider;
@"SBSAVirtualVariantTransitionProvider" _virtualVariantProvider;
@"NSMutableSet" _registeredContainerDismissalInterfacePropertyIdentifiers;
@"NSMutableSet" _pendingDismissalTransitionIdentifiers;
B _didDisappear;
```

## Instance methods

```
-[SBSAElementRemovalTransitionProvider description];
-[SBSAElementRemovalTransitionProvider preferencesFromContext:];
-[SBSAElementRemovalTransitionProvider removeFromParentProvider];
```
