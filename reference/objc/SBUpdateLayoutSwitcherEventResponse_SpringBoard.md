# `SBUpdateLayoutSwitcherEventResponse`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEventResponse`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
Q _options;
q _updateMode;
@"NSArray" _appLayouts;
```

## Properties

```
@property (TQ,R,N,V_options) options;
@property (Tq,R,N,V_updateMode) updateMode;
@property (T@"NSArray",C,N,V_appLayouts) appLayouts;
```

## Class methods

```
+[SBUpdateLayoutSwitcherEventResponse setNeedsLayout];
```

## Instance methods

```
-[SBUpdateLayoutSwitcherEventResponse appLayouts];
-[SBUpdateLayoutSwitcherEventResponse updateMode];
-[SBUpdateLayoutSwitcherEventResponse initWithOptions:updateMode:];
-[SBUpdateLayoutSwitcherEventResponse type];
-[SBUpdateLayoutSwitcherEventResponse setAppLayouts:];
-[SBUpdateLayoutSwitcherEventResponse options];
-[SBUpdateLayoutSwitcherEventResponse descriptionBuilderWithMultilinePrefix:];
```
