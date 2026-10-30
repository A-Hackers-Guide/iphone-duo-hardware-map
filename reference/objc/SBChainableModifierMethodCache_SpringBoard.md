# `SBChainableModifierMethodCache`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBChainableModifier" _modifier;
^: _selectors;
q _selectorCount;
^^? _imps;
Q _genCount;
@"SBModifierCacheCoordinator" _cacheCoordinator;
^{SBModifierCacheDispatchData=@^?} _dispatchCache;
^? _nextFunc;
```

## Properties

```
@property (T@"SBChainableModifier",N,V_modifier) modifier;
@property (T@"SBModifierCacheCoordinator",&,N,V_cacheCoordinator) cacheCoordinator;
@property (TB,R,N) hasNonTrampolineIMPs;
```

## Instance methods

```
-[SBChainableModifierMethodCache modifier];
-[SBChainableModifierMethodCache dealloc];
-[SBChainableModifierMethodCache setModifier:];
-[SBChainableModifierMethodCache copyWithZone:];
-[SBChainableModifierMethodCache cacheCoordinator];
-[SBChainableModifierMethodCache hasNonTrampolineIMPs];
-[SBChainableModifierMethodCache initWithIMPs:selectorList:subsequentMethodCacheFunc:];
-[SBChainableModifierMethodCache setCacheCoordinator:];
```
