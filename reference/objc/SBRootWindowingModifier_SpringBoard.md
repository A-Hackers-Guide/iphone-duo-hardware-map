# `SBRootWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 4 instance variables, 1 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" wallpaperAlphasForLeafAppLayouts;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cachedLeftStatusBarPartIntersectionRegion;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cachedRightStatusBarPartIntersectionRegion;
@"SBSwitcherModifier" _switcherModifier;
```

## Properties

```
@property (T@"SBSwitcherModifier",R,N,V_switcherModifier) switcherModifier;
```

## Instance methods

```
-[SBRootWindowingModifier wallpaperGradientAttributesForItem:];
-[SBRootWindowingModifier willUpdate];
-[SBRootWindowingModifier layoutViewModelsIfNeeded];
-[SBRootWindowingModifier didUpdate];
-[SBRootWindowingModifier _clearAllCachedValues];
-[SBRootWindowingModifier _steadyStateModifier];
-[SBRootWindowingModifier _updateChildModifiersIfNeeded];
-[SBRootWindowingModifier initWithSwitcherModifier:];
-[SBRootWindowingModifier leftStatusBarPartIntersectionRegion];
-[SBRootWindowingModifier rightStatusBarPartIntersectionRegion];
-[SBRootWindowingModifier switcherModifier];
```
