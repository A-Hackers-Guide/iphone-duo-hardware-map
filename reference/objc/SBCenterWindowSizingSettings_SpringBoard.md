# `SBCenterWindowSizingSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PTSettings`
- 7 instance variables, 7 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _useCustomSizingForNewWindows;
d _fullWidthScaleFactor;
d _fullHeightScaleFactor;
d _topInset;
d _bottomInset;
d _leftInset;
d _rightInset;
```

## Properties

```
@property (TB,N,V_useCustomSizingForNewWindows) useCustomSizingForNewWindows;
@property (Td,N,V_fullWidthScaleFactor) fullWidthScaleFactor;
@property (Td,N,V_fullHeightScaleFactor) fullHeightScaleFactor;
@property (Td,N,V_topInset) topInset;
@property (Td,N,V_bottomInset) bottomInset;
@property (Td,N,V_leftInset) leftInset;
@property (Td,N,V_rightInset) rightInset;
```

## Class methods

```
+[SBCenterWindowSizingSettings settingsControllerModule];
```

## Instance methods

```
-[SBCenterWindowSizingSettings leftInset];
-[SBCenterWindowSizingSettings setRightInset:];
-[SBCenterWindowSizingSettings setDefaultValues];
-[SBCenterWindowSizingSettings rightInset];
-[SBCenterWindowSizingSettings setBottomInset:];
-[SBCenterWindowSizingSettings setTopInset:];
-[SBCenterWindowSizingSettings setLeftInset:];
-[SBCenterWindowSizingSettings bottomInset];
-[SBCenterWindowSizingSettings topInset];
-[SBCenterWindowSizingSettings fullHeightScaleFactor];
-[SBCenterWindowSizingSettings fullWidthScaleFactor];
-[SBCenterWindowSizingSettings setFullHeightScaleFactor:];
-[SBCenterWindowSizingSettings setFullWidthScaleFactor:];
-[SBCenterWindowSizingSettings setUseCustomSizingForNewWindows:];
-[SBCenterWindowSizingSettings useCustomSizingForNewWindows];
```
