# `SBSystemApertureCurtainViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBSystemApertureCurtainViewHoster`
- 6 instance variables, 2 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _indicatorSourceViewsToPortalViews;
@"_UIPortalView" _systemApertureViewControllerPortalView;
@"UIView" _highLevelBackgroundParent;
@"UIView" _highLevelSubBackgroundParent;
@"UIView" _curtainView;
@"<SBSystemApertureCurtainViewHosterDelegate>" _delegate;
```

## Properties

```
@property (T@"UIView",&,N,V_curtainView) curtainView;
@property (T@"<SBSystemApertureCurtainViewHosterDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SBSystemApertureCurtainViewController _commonInit];
-[SBSystemApertureCurtainViewController setIndicatorPortalViewsHidesSourceViewChanged];
-[SBSystemApertureCurtainViewController curtainView];
-[SBSystemApertureCurtainViewController setSystemAperturePortalViewsHidesSourceViewChanged];
-[SBSystemApertureCurtainViewController init];
-[SBSystemApertureCurtainViewController supportedInterfaceOrientations];
-[SBSystemApertureCurtainViewController portalViewForIndicatorSourceView:];
-[SBSystemApertureCurtainViewController setCurtainView:];
-[SBSystemApertureCurtainViewController removePortalForSystemApertureViewController:];
-[SBSystemApertureCurtainViewController viewDidLayoutSubviews];
-[SBSystemApertureCurtainViewController initWithNibName:bundle:];
-[SBSystemApertureCurtainViewController addPortalForSystemApertureViewController:];
-[SBSystemApertureCurtainViewController _canShowWhileLocked];
-[SBSystemApertureCurtainViewController setDelegate:];
-[SBSystemApertureCurtainViewController _layoutIndicatorPortalViewForIndicatorSourceView:];
-[SBSystemApertureCurtainViewController highLevelBackgroundParent];
-[SBSystemApertureCurtainViewController delegate];
-[SBSystemApertureCurtainViewController setIndicatorPortalViewFramesChanged];
-[SBSystemApertureCurtainViewController addPortalForIndicatorSourceView:];
-[SBSystemApertureCurtainViewController initWithCoder:];
-[SBSystemApertureCurtainViewController removePortalForIndicatorSourceView:];
-[SBSystemApertureCurtainViewController highLevelSubBackgroundParent];
-[SBSystemApertureCurtainViewController setIndicatorPortalViewFrameChangedForIndicatorSourceView:];
```
