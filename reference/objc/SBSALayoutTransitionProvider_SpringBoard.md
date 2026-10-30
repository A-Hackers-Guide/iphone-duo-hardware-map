# `SBSALayoutTransitionProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSABasePreferencesProvider`
- Protocols: `SBSAElementLayoutModeTransitioning`
- 12 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"SBSABasePreferencesProvider<SBSAElementLayoutModeSupporting>" _previousLayoutProvider;
@"SBSABasePreferencesProvider<SBSAElementLayoutModeSupporting>" _targetLayoutProvider;
@"SBSARecombinationTransitionProvider" _childRecombinationProvider;
@"SBSAMitosisTransitionProvider" _childMitosisProvider;
@"SBSAVirtualVariantTransitionProvider" _childVirtualVariantProvider;
@"SBSAPopTransitionProvider" _childPopProvider;
@"SBSAVirtualVariantTransitionProvider" _childVirtualVariantCollapseProvider;
q _transitionKind;
B _awaitingCollision;
B _awaitingVirtualVariantCollapse;
B _deferringContentAppearanceForVirtualVariant;
B _initialized;
```

## Properties

```
@property (TB,R,N,GisInitialized,V_initialized) initialized;
@property (Tq,R,N) previousElementLayoutMode;
@property (Tq,R,N) targetElementLayoutMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSALayoutTransitionProvider initialize];
```

## Instance methods

```
-[SBSALayoutTransitionProvider encodeWithCoder:];
-[SBSALayoutTransitionProvider description];
-[SBSALayoutTransitionProvider isInitialized];
-[SBSALayoutTransitionProvider membersForCoder];
-[SBSALayoutTransitionProvider _adjunctElementIdentificationInContext:];
-[SBSALayoutTransitionProvider _elementLayoutModeSupportingChildProvider];
-[SBSALayoutTransitionProvider _layoutProviderForLayoutMode:];
-[SBSALayoutTransitionProvider _removeChildMitosisAndRecombinationProviders];
-[SBSALayoutTransitionProvider preferencesFromContext:];
-[SBSALayoutTransitionProvider previousElementLayoutMode];
-[SBSALayoutTransitionProvider removeFromParentProvider];
-[SBSALayoutTransitionProvider targetElementLayoutMode];
```
