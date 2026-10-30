# `SBAppSwitcherTransientOverlayPageContentView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBAppSwitcherPageContentView`
- 7 instance variables, 15 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"BSUIOrientationTransformWrapperView" _contentWrapperView;
q _orientation;
B _active;
B _visible;
@"SBAppLayout" _appLayout;
@"UIView" _contentView;
@"<SBAppSwitcherTransientOverlayPageContentViewDelegate>" _delegate;
```

## Properties

```
@property (T@"SBAppLayout",R,C,N,V_appLayout) appLayout;
@property (TB,N,GisActive,V_active) active;
@property (TB,N,GisVisible,V_visible) visible;
@property (Tq,N) contentOrientation;
@property (T@"UIView",&,N,V_contentView) contentView;
@property (T@"<SBAppSwitcherTransientOverlayPageContentViewDelegate>",W,N,V_delegate) delegate;
@property (Td,N) cornerRadius;
@property (TQ,N) maskedCorners;
@property (T{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}},N) cornerRadii;
@property (Tq,N) orientation;
@property (TB,R,N) contentRequiresGroupOpacity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAppSwitcherTransientOverlayPageContentView cornerRadii];
-[SBAppSwitcherTransientOverlayPageContentView setOrientation:];
-[SBAppSwitcherTransientOverlayPageContentView setContentView:];
-[SBAppSwitcherTransientOverlayPageContentView setVisible:];
-[SBAppSwitcherTransientOverlayPageContentView contentRequiresGroupOpacity];
-[SBAppSwitcherTransientOverlayPageContentView appLayout];
-[SBAppSwitcherTransientOverlayPageContentView orientation];
-[SBAppSwitcherTransientOverlayPageContentView contentOrientation];
-[SBAppSwitcherTransientOverlayPageContentView setContentOrientation:];
-[SBAppSwitcherTransientOverlayPageContentView setCornerRadii:];
-[SBAppSwitcherTransientOverlayPageContentView isVisible];
-[SBAppSwitcherTransientOverlayPageContentView layoutSubviews];
-[SBAppSwitcherTransientOverlayPageContentView maskedCorners];
-[SBAppSwitcherTransientOverlayPageContentView setActive:];
-[SBAppSwitcherTransientOverlayPageContentView setCornerRadius:];
-[SBAppSwitcherTransientOverlayPageContentView invalidate];
-[SBAppSwitcherTransientOverlayPageContentView setMaskedCorners:];
-[SBAppSwitcherTransientOverlayPageContentView setDelegate:];
-[SBAppSwitcherTransientOverlayPageContentView cornerRadius];
-[SBAppSwitcherTransientOverlayPageContentView contentView];
-[SBAppSwitcherTransientOverlayPageContentView delegate];
-[SBAppSwitcherTransientOverlayPageContentView isActive];
-[SBAppSwitcherTransientOverlayPageContentView initWithFrame:appLayout:];
```
