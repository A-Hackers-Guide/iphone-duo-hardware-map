# `SBAppExposeWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 4 instance variables, 1 properties, 26 instance methods, 0 class methods

## Instance variables

```
q _numberOfHiddenAppLayouts;
B _isShowingReopenClosedWindowsButton;
@"SBAppLayout" _appLayoutToRestore;
@"NSString" _appExposeBundleIdentifier;
```

## Properties

```
@property (T@"NSString",R,C,N,V_appExposeBundleIdentifier) appExposeBundleIdentifier;
```

## Instance methods

```
-[SBAppExposeWindowingModifier transitionDidUpdate:];
-[SBAppExposeWindowingModifier appLayout];
-[SBAppExposeWindowingModifier reopenClosedWindowsButtonAlpha];
-[SBAppExposeWindowingModifier recentAppLayouts];
-[SBAppExposeWindowingModifier plusButtonStyle];
-[SBAppExposeWindowingModifier transitionWillBegin:];
-[SBAppExposeWindowingModifier appLayoutToScrollToBeforeReopeningClosedWindows];
-[SBAppExposeWindowingModifier appExposeAccessoryButtonsBundleIdentifier];
-[SBAppExposeWindowingModifier canPerformKeyboardShortcutAction:forBundleIdentifier:];
-[SBAppExposeWindowingModifier isItemContainerPointerInteractionEnabled];
-[SBAppExposeWindowingModifier reopenClosedWindowsButtonScale];
-[SBAppExposeWindowingModifier opacityForItem:];
-[SBAppExposeWindowingModifier wantsSpaceAccessoryViewPointerInteractionsForAppLayout:];
-[SBAppExposeWindowingModifier initWithBundleIdentifier:];
-[SBAppExposeWindowingModifier timerFired:];
-[SBAppExposeWindowingModifier plusButtonAlpha];
-[SBAppExposeWindowingModifier appExposeAccessoryButtonsOverrideUserInterfaceStyle];
-[SBAppExposeWindowingModifier _canShowReopenClosedWindowsButton];
-[SBAppExposeWindowingModifier _updateReopenClosedWindowsButtonPresence];
-[SBAppExposeWindowingModifier appExposeBundleIdentifier];
-[SBAppExposeWindowingModifier appLayoutTapped:];
-[SBAppExposeWindowingModifier desktopSpaceDisplayItems];
-[SBAppExposeWindowingModifier groupsWindowsByApp];
-[SBAppExposeWindowingModifier itemInserted:];
-[SBAppExposeWindowingModifier itemRemoved:];
-[SBAppExposeWindowingModifier tappedOutsideToDismiss:];
```
