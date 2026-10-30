# `SBButterflyAppsLayoutModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 5 instance variables, 0 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _homeAffordanceReuseIdentifier;
@"SBAppLayout" _appLayout;
@"SBButterflyCoplanarWindowingModifier" _coplanarModifier;
@"_SBButterflyAppsLayoutModifier" _appsLayoutModifier;
B _handlesAssistantPresentationEvents;
```

## Instance methods

```
-[SBButterflyAppsLayoutModifier transitionDidUpdate:];
-[SBButterflyAppsLayoutModifier initWithActiveAppLayout:];
-[SBButterflyAppsLayoutModifier transitionWillBegin:];
-[SBButterflyAppsLayoutModifier _addAssistantModifierIfNeededForInterfaceOrientation:];
-[SBButterflyAppsLayoutModifier willBegin];
-[SBButterflyAppsLayoutModifier _addAssistantModifierIfNeededForTransition:];
-[SBButterflyAppsLayoutModifier _assistantIsEffectivelyPresentedAndWantsDeemphasizedBackdrop];
-[SBButterflyAppsLayoutModifier _updateCoplanarModifierIgnoredAppLayouts];
-[SBButterflyAppsLayoutModifier assistantPresentationChanged:];
-[SBButterflyAppsLayoutModifier itemInserted:];
-[SBButterflyAppsLayoutModifier splitViewHandleTapped:];
-[SBButterflyAppsLayoutModifier switcherShortcutActionPerformed:];
-[SBButterflyAppsLayoutModifier transitionDidComplete:];
```
