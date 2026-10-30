# `_UIEditMenuListItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 17 instance methods, 2 class methods

## Instance variables

```
B _wantsPasteSlotView;
B _singleItemMenu;
@"UIMenuElement" _menuElement;
@"NSString" _title;
@"UIImage" _image;
@"UISPasteVariant" _pasteVariant;
q _options;
@"UIView" _customView;
d _overrideMinimumWidth;
Q _displayMode;
```

## Properties

```
@property (T@"UIMenuElement",R,N,V_menuElement) menuElement;
@property (T@"NSString",R,N,V_title) title;
@property (T@"UIImage",R,N,V_image) image;
@property (T@"UISPasteVariant",R,N,V_pasteVariant) pasteVariant;
@property (Tq,R,N,V_options) options;
@property (T@"UIView",R,N,V_customView) customView;
@property (Td,N,V_overrideMinimumWidth) overrideMinimumWidth;
@property (TQ,N,V_displayMode) displayMode;
@property (TB,N,V_wantsPasteSlotView) wantsPasteSlotView;
@property (TB,N,GisSingleItemMenu,V_singleItemMenu) singleItemMenu;
```

## Class methods

```
+[_UIEditMenuListItem itemWithMenuElement:preferredDisplayMode:];
+[_UIEditMenuListItem itemWithTitle:];
```

## Instance methods

```
-[_UIEditMenuListItem customView];
-[_UIEditMenuListItem hidesImageForTraitCollection:];
-[_UIEditMenuListItem pasteVariant];
-[_UIEditMenuListItem setDisplayMode:];
-[_UIEditMenuListItem overrideMinimumWidth];
-[_UIEditMenuListItem displayMode];
-[_UIEditMenuListItem hidesTitleForTraitCollection:];
-[_UIEditMenuListItem wantsPasteSlotView];
-[_UIEditMenuListItem title];
-[_UIEditMenuListItem setOverrideMinimumWidth:];
-[_UIEditMenuListItem isSingleItemMenu];
-[_UIEditMenuListItem setSingleItemMenu:];
-[_UIEditMenuListItem description];
-[_UIEditMenuListItem setWantsPasteSlotView:];
-[_UIEditMenuListItem options];
-[_UIEditMenuListItem image];
-[_UIEditMenuListItem menuElement];
```
