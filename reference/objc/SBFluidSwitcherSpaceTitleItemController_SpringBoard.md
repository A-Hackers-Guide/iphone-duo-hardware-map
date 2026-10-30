# `SBFluidSwitcherSpaceTitleItemController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDeviceApplicationSceneHandleObserver`, `SBIconObserver`, `BSInvalidatable`
- 16 instance variables, 10 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _appLayout;
@"SBWindowScene" _windowScene;
@"SBApplicationController" _applicationController;
@"NSArray" _displayItems;
@"NSMutableDictionary" _displayItemToIcon;
@"NSMutableDictionary" _displayItemToSceneHandle;
B _invalidated;
@"NSMutableDictionary" _displayItemToCustomTitleText;
q _numVisibleIcons;
{SBIconImageInfo="size"{CGSize="width"d"height"d}"scale"d"continuousCornerRadius"d} _headerIconImageInfo;
B _useDarkLabels;
B _isFlexibleWindowingEnabled;
B _isFooterViewOfItemContainer;
@"SBLayoutRoleSet" _multiWindowIndicatorRoles;
q _userInterfaceStyle;
@? _updateHandler;
```

## Properties

```
@property (TB,N,GisUsingDarkLabels,V_useDarkLabels) useDarkLabels;
@property (T@"SBLayoutRoleSet",&,N,V_multiWindowIndicatorRoles) multiWindowIndicatorRoles;
@property (TB,R,N,V_isFlexibleWindowingEnabled) isFlexibleWindowingEnabled;
@property (TB,R,N,V_isFooterViewOfItemContainer) isFooterViewOfItemContainer;
@property (Tq,N,V_userInterfaceStyle) userInterfaceStyle;
@property (T@?,C,N,V_updateHandler) updateHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFluidSwitcherSpaceTitleItemController updateHandler];
-[SBFluidSwitcherSpaceTitleItemController setUpdateHandler:];
-[SBFluidSwitcherSpaceTitleItemController isBadged];
-[SBFluidSwitcherSpaceTitleItemController _performUpdateHandler];
-[SBFluidSwitcherSpaceTitleItemController setUseDarkLabels:];
-[SBFluidSwitcherSpaceTitleItemController isUsingDarkLabels];
-[SBFluidSwitcherSpaceTitleItemController _iconForDisplayItem:];
-[SBFluidSwitcherSpaceTitleItemController iconImageDidUpdate:];
-[SBFluidSwitcherSpaceTitleItemController isFooterViewOfItemContainer];
-[SBFluidSwitcherSpaceTitleItemController dealloc];
-[SBFluidSwitcherSpaceTitleItemController _updateDisplayItemIcons];
-[SBFluidSwitcherSpaceTitleItemController setCustomTitleText:forDisplayItem:];
-[SBFluidSwitcherSpaceTitleItemController userInterfaceStyle];
-[SBFluidSwitcherSpaceTitleItemController setUserInterfaceStyle:];
-[SBFluidSwitcherSpaceTitleItemController invalidate];
-[SBFluidSwitcherSpaceTitleItemController _headerIconImageInfo];
-[SBFluidSwitcherSpaceTitleItemController sceneHandle:didChangeSceneTitle:];
-[SBFluidSwitcherSpaceTitleItemController multiWindowIndicatorRoles];
-[SBFluidSwitcherSpaceTitleItemController initWithAppLayout:windowScene:applicationController:showCanvasTitles:isFlexibleWindowingEnabled:isFooterViewOfItemContainer:];
-[SBFluidSwitcherSpaceTitleItemController setMultiWindowIndicatorRoles:];
-[SBFluidSwitcherSpaceTitleItemController setMaximumNumberOfVisibleIcons:];
-[SBFluidSwitcherSpaceTitleItemController _computeHeaderItems];
-[SBFluidSwitcherSpaceTitleItemController isFlexibleWindowingEnabled];
-[SBFluidSwitcherSpaceTitleItemController _iconViewForDisplayItem:];
-[SBFluidSwitcherSpaceTitleItemController _iconImageAppearance];
```
