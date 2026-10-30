# `SBAppSwitcherServicePageContentView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBAppSwitcherPageContentView`
- 3 instance variables, 11 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _active;
B _visible;
q _orientation;
```

## Properties

```
@property (Tq,N,V_orientation) orientation;
@property (Td,N) cornerRadius;
@property (TQ,N) maskedCorners;
@property (T{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}},N) cornerRadii;
@property (TB,R,N) contentRequiresGroupOpacity;
@property (TB,N,GisActive,V_active) active;
@property (TB,N,GisVisible,V_visible) visible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAppSwitcherServicePageContentView cornerRadii];
-[SBAppSwitcherServicePageContentView setOrientation:];
-[SBAppSwitcherServicePageContentView setVisible:];
-[SBAppSwitcherServicePageContentView contentRequiresGroupOpacity];
-[SBAppSwitcherServicePageContentView orientation];
-[SBAppSwitcherServicePageContentView setCornerRadii:];
-[SBAppSwitcherServicePageContentView isVisible];
-[SBAppSwitcherServicePageContentView maskedCorners];
-[SBAppSwitcherServicePageContentView setActive:];
-[SBAppSwitcherServicePageContentView setCornerRadius:];
-[SBAppSwitcherServicePageContentView invalidate];
-[SBAppSwitcherServicePageContentView sizeThatFits:];
-[SBAppSwitcherServicePageContentView setMaskedCorners:];
-[SBAppSwitcherServicePageContentView cornerRadius];
-[SBAppSwitcherServicePageContentView isActive];
-[SBAppSwitcherServicePageContentView initWithFrame:];
```
