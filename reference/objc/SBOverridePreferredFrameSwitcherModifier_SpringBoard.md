# `SBOverridePreferredFrameSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 3 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"SBDisplayItem" _displayItem;
{CGSize="width"d"height"d} _newPreferredSize;
{CGPoint="x"d"y"d} _newPreferredCenter;
```

## Properties

```
@property (T{CGSize=dd},N,V_newPreferredSize) newPreferredSize;
@property (T{CGPoint=dd},N,V_newPreferredCenter) newPreferredCenter;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) newPreferredFrame;
@property (T@"SBDisplayItem",R,N,V_displayItem) displayItem;
```

## Instance methods

```
-[SBOverridePreferredFrameSwitcherModifier displayItem];
-[SBOverridePreferredFrameSwitcherModifier initWithDisplayItem:];
-[SBOverridePreferredFrameSwitcherModifier initWithNewPreferredCenter:forDisplayItem:];
-[SBOverridePreferredFrameSwitcherModifier initWithNewPreferredFrame:forDisplayItem:];
-[SBOverridePreferredFrameSwitcherModifier initWithNewPreferredSize:forDisplayItem:];
-[SBOverridePreferredFrameSwitcherModifier initWithNewPreferredSize:newPreferredCenter:forDisplayItem:];
-[SBOverridePreferredFrameSwitcherModifier newPreferredCenter];
-[SBOverridePreferredFrameSwitcherModifier newPreferredFrame];
-[SBOverridePreferredFrameSwitcherModifier newPreferredSize];
-[SBOverridePreferredFrameSwitcherModifier preferredFrameForLayoutRole:inAppLayout:bounds:interfaceOrientation:];
-[SBOverridePreferredFrameSwitcherModifier setNewPreferredCenter:];
-[SBOverridePreferredFrameSwitcherModifier setNewPreferredFrame:];
-[SBOverridePreferredFrameSwitcherModifier setNewPreferredSize:];
```
