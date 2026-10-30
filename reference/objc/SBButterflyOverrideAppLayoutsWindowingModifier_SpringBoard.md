# `SBButterflyOverrideAppLayoutsWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 4 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _appLayouts;
Q _appLayoutsGenerationCount;
@"SBDeckRegionModel" _filteredDeckModel;
@"SBDeckRegionModel" _unfilteredDeckModel;
```

## Instance methods

```
-[SBButterflyOverrideAppLayoutsWindowingModifier appLayouts];
-[SBButterflyOverrideAppLayoutsWindowingModifier willBegin];
-[SBButterflyOverrideAppLayoutsWindowingModifier didComplete];
-[SBButterflyOverrideAppLayoutsWindowingModifier deckRegionModel];
-[SBButterflyOverrideAppLayoutsWindowingModifier _rebuildFilteredDeckModelIfNeeded];
-[SBButterflyOverrideAppLayoutsWindowingModifier appLayoutsGenerationCount];
-[SBButterflyOverrideAppLayoutsWindowingModifier initWithAppLayouts:];
-[SBButterflyOverrideAppLayoutsWindowingModifier willPerformAsTemporaryChildModifier];
```
