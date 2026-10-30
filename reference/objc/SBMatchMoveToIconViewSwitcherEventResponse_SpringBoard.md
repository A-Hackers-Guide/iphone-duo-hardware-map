# `SBMatchMoveToIconViewSwitcherEventResponse`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEventResponse`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _active;
@"SBAppLayout" _appLayout;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _iconFrame;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_appLayout) appLayout;
@property (TB,R,N,GisActive,V_active) active;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_iconFrame) iconFrame;
```

## Instance methods

```
-[SBMatchMoveToIconViewSwitcherEventResponse appLayout];
-[SBMatchMoveToIconViewSwitcherEventResponse iconFrame];
-[SBMatchMoveToIconViewSwitcherEventResponse type];
-[SBMatchMoveToIconViewSwitcherEventResponse initWithActivatingAppLayout:iconFrame:];
-[SBMatchMoveToIconViewSwitcherEventResponse _initWithAppLayout:active:iconFrame:];
-[SBMatchMoveToIconViewSwitcherEventResponse initWithDeactivatingAppLayout:];
-[SBMatchMoveToIconViewSwitcherEventResponse isActive];
-[SBMatchMoveToIconViewSwitcherEventResponse descriptionBuilderWithMultilinePrefix:];
```
