# `SBSwitcherLayoutCalculationsCache`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _cachedLayoutCalculationsByKey;
@"<SBSwitcherLayoutCalculationsCacheDelegate>" _delegate;
@"SBSwitcherLayoutCalculationsCacheValidityToken" _validityToken;
```

## Properties

```
@property (T@"<SBSwitcherLayoutCalculationsCacheDelegate>",W,N,V_delegate) delegate;
@property (T@"SBSwitcherLayoutCalculationsCacheValidityToken",R,N,V_validityToken) validityToken;
```

## Instance methods

```
-[SBSwitcherLayoutCalculationsCache init];
-[SBSwitcherLayoutCalculationsCache setDelegate:];
-[SBSwitcherLayoutCalculationsCache delegate];
-[SBSwitcherLayoutCalculationsCache frameForKey:validityToken:fallback:];
-[SBSwitcherLayoutCalculationsCache rebuildIfNecessaryForValidityToken:];
-[SBSwitcherLayoutCalculationsCache scaleForKey:validityToken:fallback:];
-[SBSwitcherLayoutCalculationsCache validityToken];
```
