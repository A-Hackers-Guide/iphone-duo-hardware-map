# `SBExternalDisplayCoverSheetViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBFZStackParticipantDelegate`, `SBExternalDisplayWallpaperConfigurations`, `SBWallpaperEffectViewFactory`
- 8 instance variables, 12 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _isPresented;
@"UIView" _wallpaperContainerView;
@"UIView" _wallpaperEffectView;
@"SBFZStackParticipant" _zStackParticipant;
@"SBFloatingDockBehaviorAssertion" _externalDisplayFloatingDockBehaviorAssertion;
@"SBWindowScene" _sbWindowScene;
@"<SBWallpaperEffectViewFactory>" _wallpaperEffectViewFactory;
@"SBBacklightController" _backlightController;
```

## Properties

```
@property (T@"UIView",&,N,V_wallpaperContainerView) wallpaperContainerView;
@property (T@"UIView",&,N,V_wallpaperEffectView) wallpaperEffectView;
@property (T@"SBFZStackParticipant",&,N,V_zStackParticipant) zStackParticipant;
@property (TB,N,V_isPresented) isPresented;
@property (T@"SBFloatingDockBehaviorAssertion",&,N,V_externalDisplayFloatingDockBehaviorAssertion) externalDisplayFloatingDockBehaviorAssertion;
@property (T@"SBWindowScene",W,N,G_sbWindowScene,V_sbWindowScene) sbWindowScene;
@property (T@"<SBWallpaperEffectViewFactory>",R,N,V_wallpaperEffectViewFactory) wallpaperEffectViewFactory;
@property (T@"SBBacklightController",R,N,V_backlightController) backlightController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBExternalDisplayCoverSheetViewController zStackParticipant];
-[SBExternalDisplayCoverSheetViewController backlightController];
-[SBExternalDisplayCoverSheetViewController isPresented];
-[SBExternalDisplayCoverSheetViewController setZStackParticipant:];
-[SBExternalDisplayCoverSheetViewController zStackParticipant:updatePreferences:];
-[SBExternalDisplayCoverSheetViewController wallpaperEffectView];
-[SBExternalDisplayCoverSheetViewController dealloc];
-[SBExternalDisplayCoverSheetViewController prepareForPresentation];
-[SBExternalDisplayCoverSheetViewController viewDidLoad];
-[SBExternalDisplayCoverSheetViewController zStackParticipantDidChange:];
-[SBExternalDisplayCoverSheetViewController zStackParticipant:updateZOrderPreferences:];
-[SBExternalDisplayCoverSheetViewController setWallpaperEffectView:];
-[SBExternalDisplayCoverSheetViewController _sbWindowScene];
-[SBExternalDisplayCoverSheetViewController setIsPresented:];
-[SBExternalDisplayCoverSheetViewController _floatingDockController];
-[SBExternalDisplayCoverSheetViewController _initWithWindowScene:wallpaperEffectViewFactory:];
-[SBExternalDisplayCoverSheetViewController cleanupAfterDismissal];
-[SBExternalDisplayCoverSheetViewController enableBlurEffects];
-[SBExternalDisplayCoverSheetViewController externalDisplayFloatingDockBehaviorAssertion];
-[SBExternalDisplayCoverSheetViewController newWallpaperEffectView];
-[SBExternalDisplayCoverSheetViewController setExternalDisplayFloatingDockBehaviorAssertion:];
-[SBExternalDisplayCoverSheetViewController setSbWindowScene:];
-[SBExternalDisplayCoverSheetViewController setWallpaperContainerView:];
-[SBExternalDisplayCoverSheetViewController wallpaperContainerView];
-[SBExternalDisplayCoverSheetViewController wallpaperEffectViewFactory];
```
