# `SBSwitcherModelRemovalResults`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _appLayouts;
@"NSMutableDictionary" _appLayoutToAction;
@"NSMutableDictionary" _displayItemToHide;
@"NSMutableDictionary" _appLayoutToReplacement;
@"<SBSwitcherContentViewControlling>" _originatingSwitcherContentController;
```

## Properties

```
@property (T@"NSArray",R,C,N) appLayouts;
@property (T@"<SBSwitcherContentViewControlling>",&,N,V_originatingSwitcherContentController) originatingSwitcherContentController;
```

## Instance methods

```
-[SBSwitcherModelRemovalResults appLayouts];
-[SBSwitcherModelRemovalResults init];
-[SBSwitcherModelRemovalResults executeActionForAppLayout:];
-[SBSwitcherModelRemovalResults originatingSwitcherContentController];
-[SBSwitcherModelRemovalResults removeAppLayout:];
-[SBSwitcherModelRemovalResults replacementAppLayoutForAppLayout:];
-[SBSwitcherModelRemovalResults setAction:forAppLayout:];
-[SBSwitcherModelRemovalResults setHide:forDisplayItem:];
-[SBSwitcherModelRemovalResults setOriginatingSwitcherContentController:];
-[SBSwitcherModelRemovalResults setReplacementAppLayout:forAppLayout:];
-[SBSwitcherModelRemovalResults willHideDisplayItem:];
```
