# `SBFlexibleWindowingToAppExposeWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 4 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _transitionID;
@"SBAppExposeWindowingModifier" _appExposeModifier;
@"NSSet" _appLayoutsVisibleBeforeTransition;
@"NSString" _bundleId;
```

## Instance methods

```
-[SBFlexibleWindowingToAppExposeWindowingModifier animationAttributesForLayoutElement:];
-[SBFlexibleWindowingToAppExposeWindowingModifier adjustedAppLayoutsForAppLayouts:];
-[SBFlexibleWindowingToAppExposeWindowingModifier transitionDidUpdate:];
-[SBFlexibleWindowingToAppExposeWindowingModifier transitionWillBegin:];
-[SBFlexibleWindowingToAppExposeWindowingModifier visibleItems];
-[SBFlexibleWindowingToAppExposeWindowingModifier initWithBundleIdentifier:];
-[SBFlexibleWindowingToAppExposeWindowingModifier frameForItem:];
-[SBFlexibleWindowingToAppExposeWindowingModifier willBegin];
-[SBFlexibleWindowingToAppExposeWindowingModifier didComplete];
-[SBFlexibleWindowingToAppExposeWindowingModifier shouldInterruptForActivity:];
-[SBFlexibleWindowingToAppExposeWindowingModifier transitionDidComplete:];
```
