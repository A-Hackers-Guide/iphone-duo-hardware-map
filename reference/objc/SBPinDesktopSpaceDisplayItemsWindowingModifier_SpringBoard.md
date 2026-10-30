# `SBPinDesktopSpaceDisplayItemsWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 1 instance variables, 1 properties, 4 instance methods, 2 class methods

## Instance variables

```
@"SBAppLayout" _appLayoutToPin;
```

## Properties

```
@property (T@"SBAppLayout",&,N,V_appLayoutToPin) appLayoutToPin;
```

## Class methods

```
+[SBPinDesktopSpaceDisplayItemsWindowingModifier modifierForGestureWithSelectedDisplayItem:context:];
+[SBPinDesktopSpaceDisplayItemsWindowingModifier modifierForTransitionToAppLayout:context:];
```

## Instance methods

```
-[SBPinDesktopSpaceDisplayItemsWindowingModifier willBegin];
-[SBPinDesktopSpaceDisplayItemsWindowingModifier _initWithAppLayoutToPin:];
-[SBPinDesktopSpaceDisplayItemsWindowingModifier appLayoutToPin];
-[SBPinDesktopSpaceDisplayItemsWindowingModifier setAppLayoutToPin:];
```
