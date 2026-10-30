# `SBSwitcherWindowingSnapPaddingSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 5 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
d _multiAppCenterPadding;
d _singleAppCenterPadding;
d _edgePadding;
d _fullScreenSnapPadding;
d _interItemPadding;
```

## Properties

```
@property (Td,N,V_multiAppCenterPadding) multiAppCenterPadding;
@property (Td,N,V_singleAppCenterPadding) singleAppCenterPadding;
@property (Td,N,V_edgePadding) edgePadding;
@property (Td,N,V_fullScreenSnapPadding) fullScreenSnapPadding;
@property (Td,N,V_interItemPadding) interItemPadding;
```

## Class methods

```
+[SBSwitcherWindowingSnapPaddingSettings settingsControllerModule];
```

## Instance methods

```
-[SBSwitcherWindowingSnapPaddingSettings hash];
-[SBSwitcherWindowingSnapPaddingSettings initWithDefaultValues];
-[SBSwitcherWindowingSnapPaddingSettings setEdgePadding:];
-[SBSwitcherWindowingSnapPaddingSettings copyWithZone:];
-[SBSwitcherWindowingSnapPaddingSettings isEqual:];
-[SBSwitcherWindowingSnapPaddingSettings edgePadding];
-[SBSwitcherWindowingSnapPaddingSettings fullScreenSnapPadding];
-[SBSwitcherWindowingSnapPaddingSettings interItemPadding];
-[SBSwitcherWindowingSnapPaddingSettings multiAppCenterPadding];
-[SBSwitcherWindowingSnapPaddingSettings setFullScreenSnapPadding:];
-[SBSwitcherWindowingSnapPaddingSettings setInterItemPadding:];
-[SBSwitcherWindowingSnapPaddingSettings setMultiAppCenterPadding:];
-[SBSwitcherWindowingSnapPaddingSettings setSingleAppCenterPadding:];
-[SBSwitcherWindowingSnapPaddingSettings singleAppCenterPadding];
```
