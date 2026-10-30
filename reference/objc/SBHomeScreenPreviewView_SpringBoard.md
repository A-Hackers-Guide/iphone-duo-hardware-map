# `SBHomeScreenPreviewView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBIconViewProviding`, `SBIconViewDelegate`
- 11 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UIView" _folderContent;
@"UIView" _floatingDock;
@"UIStatusBar" _statusBar;
@"SBRootFolderController" _rootFolderController;
@"_SBHomeScreenFolderDelegate" _folderDelegate;
@"SBWindowSceneStatusBarManager" _windowSceneStatusBarManager;
@"SBWallpaperController" _wallpaperController;
@"SBHIconManager" _iconManager;
@"SBFloatingDockViewController" _floatingDockViewController;
Q _snapshotOptions;
@"<SBDockOffscreenFractionModifying>" _dockOffscreenModifier;
```

## Properties

```
@property (T@"SBHIconManager",R,N,V_iconManager) iconManager;
@property (T@"SBFloatingDockViewController",R,N,V_floatingDockViewController) floatingDockViewController;
@property (TQ,R,N,V_snapshotOptions) snapshotOptions;
@property (T@"<SBDockOffscreenFractionModifying>",R,N,V_dockOffscreenModifier) dockOffscreenModifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBHomeScreenPreviewView dequeueReusableIconViewOfClass:];
-[SBHomeScreenPreviewView iconView:backgroundViewForComponentsOfType:];
-[SBHomeScreenPreviewView configureIconView:forIcon:];
-[SBHomeScreenPreviewView iconManager];
-[SBHomeScreenPreviewView floatingDockViewController];
-[SBHomeScreenPreviewView isIconViewRecycled:];
-[SBHomeScreenPreviewView recycleIconView:];
-[SBHomeScreenPreviewView dealloc];
-[SBHomeScreenPreviewView layoutSubviews];
-[SBHomeScreenPreviewView behaviorDelegateForIconView:];
-[SBHomeScreenPreviewView snapshotOptions];
-[SBHomeScreenPreviewView dockOffscreenModifier];
-[SBHomeScreenPreviewView initWithFrame:iconManager:wallpaperController:options:wallpaperImage:listView:];
-[SBHomeScreenPreviewView makeFolderContentWithWallpaperController:legibilitySettings:options:];
-[SBHomeScreenPreviewView makeIconFolderContentWithWallpaperController:legibilitySettings:options:];
-[SBHomeScreenPreviewView makeSilhouetteFolderContent];
```
