# `CSPosterSwitcherViewControllerConfiguring` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBFApplicationHosting`, `CSDismissableModalViewControllerDelegate`
- 0 instance variables, 15 properties, 29 instance methods, 0 class methods

## Properties

```
@property (T@"<CSTraitAwareAppHostConfiguring>",&,N) appHostConfiguring;
@property (T@"NSArray",&,N) activatingTouches;
@property (T@"UIView",W,N) coverSheetBackgroundView;
@property (T@"UIView",W,N) coverSheetWallpaperView;
@property (T@"UIView",W,N) coverSheetFloatingView;
@property (TB,N,GisCoverSheetWallpaperFloatingLayerInlined) coverSheetWallpaperFloatingLayerInlined;
@property (TB,N,GisCoverSheetComplicationRowHidden) coverSheetComplicationRowHidden;
@property (Td,N) lastAdaptiveTimeTextHeight;
@property (T@"UIWindow",&,N) targetWindow;
@property (T@"BSUIVibrancyConfiguration",C,N) vibrancyConfiguration;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) leadingTopButtonFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) trailingTopButtonFrame;
@property (T@?,C,N) invalidationHandler;
@property (T@?,C,N) toFullscreenBlock;
@property (T@?,?,C,N) stateCoordinationHandler;
```

## Instance methods

```
-[CSPosterSwitcherViewControllerConfiguring setVibrancyConfiguration:];
-[CSPosterSwitcherViewControllerConfiguring setAppHostConfiguring:];
-[CSPosterSwitcherViewControllerConfiguring setActivatingTouches:];
-[CSPosterSwitcherViewControllerConfiguring vibrancyConfiguration];
-[CSPosterSwitcherViewControllerConfiguring targetWindow];
-[CSPosterSwitcherViewControllerConfiguring lastAdaptiveTimeTextHeight];
-[CSPosterSwitcherViewControllerConfiguring setInvalidationHandler:];
-[CSPosterSwitcherViewControllerConfiguring isCoverSheetComplicationRowHidden];
-[CSPosterSwitcherViewControllerConfiguring trailingTopButtonFrame];
-[CSPosterSwitcherViewControllerConfiguring appHostConfiguring];
-[CSPosterSwitcherViewControllerConfiguring coverSheetFloatingView];
-[CSPosterSwitcherViewControllerConfiguring activatingTouches];
-[CSPosterSwitcherViewControllerConfiguring setCoverSheetBackgroundView:];
-[CSPosterSwitcherViewControllerConfiguring toFullscreenBlock];
-[CSPosterSwitcherViewControllerConfiguring setCoverSheetComplicationRowHidden:];
-[CSPosterSwitcherViewControllerConfiguring setLastAdaptiveTimeTextHeight:];
-[CSPosterSwitcherViewControllerConfiguring setLeadingTopButtonFrame:trailingTopButtonFrame:];
-[CSPosterSwitcherViewControllerConfiguring invalidationHandler];
-[CSPosterSwitcherViewControllerConfiguring setTargetWindow:];
-[CSPosterSwitcherViewControllerConfiguring setToFullscreenBlock:];
-[CSPosterSwitcherViewControllerConfiguring coverSheetBackgroundView];
-[CSPosterSwitcherViewControllerConfiguring setCoverSheetWallpaperView:];
-[CSPosterSwitcherViewControllerConfiguring setCoverSheetFloatingView:];
-[CSPosterSwitcherViewControllerConfiguring isCoverSheetWallpaperFloatingLayerInlined];
-[CSPosterSwitcherViewControllerConfiguring coverSheetWallpaperView];
-[CSPosterSwitcherViewControllerConfiguring leadingTopButtonFrame];
-[CSPosterSwitcherViewControllerConfiguring setCoverSheetWallpaperFloatingLayerInlined:];
-[CSPosterSwitcherViewControllerConfiguring setStateCoordinationHandler:];
-[CSPosterSwitcherViewControllerConfiguring stateCoordinationHandler];
```
