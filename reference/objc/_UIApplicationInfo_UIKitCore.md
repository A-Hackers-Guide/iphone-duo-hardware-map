# `_UIApplicationInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSApplicationInfo`
- 22 instance variables, 21 properties, 28 instance methods, 2 class methods

## Instance variables

```
q _launchingInterfaceOrientation;
@"NSArray" _lazy_folderNames;
@"NSString" _lazy_fallbackFolderName;
B _canChangeBackgroundStyle;
B _statusBarHidden;
B _statusBarHiddenWhenVerticallyCompact;
B _effectiveUIRequiresFullScreenValue;
B _supportsiPhoneResizing;
B _supportsVerticalBars;
B _hidesAutomaticIntelligentAssistantInteractions;
B _systemWindowsSecure;
B _optOutOfRTL;
B _requiresHighResolution;
q _requestedStatusBarStyle;
q _backgroundStyle;
@"NSString" _launchImageFile;
@"NSString" _keyColorAssetName;
q _supportedUserInterfaceStyle;
Q _ignoredOverrides;
Q _viewControllerBasedStatusBarAppearance;
q _whitePointAdaptivityStyle;
Q _supportsVerticalBarLayoutMargins;
```

## Properties

```
@property (TQ,R,N,V_ignoredOverrides) ignoredOverrides;
@property (TQ,R,N,V_viewControllerBasedStatusBarAppearance) viewControllerBasedStatusBarAppearance;
@property (TB,R,N,V_systemWindowsSecure) systemWindowsSecure;
@property (TB,R,N,V_optOutOfRTL) optOutOfRTL;
@property (Tq,R,N,V_whitePointAdaptivityStyle) whitePointAdaptivityStyle;
@property (TB,R,N,V_requiresHighResolution) requiresHighResolution;
@property (TQ,R,N,V_supportsVerticalBarLayoutMargins) supportsVerticalBarLayoutMargins;
@property (Tq,R,N,V_requestedStatusBarStyle) requestedStatusBarStyle;
@property (TB,R,N,V_canChangeBackgroundStyle) canChangeBackgroundStyle;
@property (Tq,R,N,V_backgroundStyle) backgroundStyle;
@property (TB,R,N,V_statusBarHidden) statusBarHidden;
@property (TB,R,N,V_statusBarHiddenWhenVerticallyCompact) statusBarHiddenWhenVerticallyCompact;
@property (T@"NSString",R,C,N,V_launchImageFile) launchImageFile;
@property (T@"NSString",R,C,N,V_keyColorAssetName) keyColorAssetName;
@property (Tq,R,N,V_supportedUserInterfaceStyle) supportedUserInterfaceStyle;
@property (TB,R,N,V_effectiveUIRequiresFullScreenValue) effectiveUIRequiresFullScreenValue;
@property (TB,R,N,V_supportsiPhoneResizing) supportsiPhoneResizing;
@property (TB,R,N,V_supportsVerticalBars) supportsVerticalBars;
@property (TB,R,N,V_hidesAutomaticIntelligentAssistantInteractions) hidesAutomaticIntelligentAssistantInteractions;
@property (T@"NSArray",R,N) folderNames;
@property (T@"NSString",R,N) fallbackFolderName;
```

## Class methods

```
+[_UIApplicationInfo _genreNameForID:];
+[_UIApplicationInfo _localizedFolderNameForName:];
```

## Instance methods

```
-[_UIApplicationInfo launchImageFile];
-[_UIApplicationInfo ignoredOverrides];
-[_UIApplicationInfo viewControllerBasedStatusBarAppearance];
-[_UIApplicationInfo _loadFromProxy:];
-[_UIApplicationInfo statusBarHidden];
-[_UIApplicationInfo keyColorAssetName];
-[_UIApplicationInfo canChangeBackgroundStyle];
-[_UIApplicationInfo requestedStatusBarStyle];
-[_UIApplicationInfo requiresHighResolution];
-[_UIApplicationInfo backgroundStyle];
-[_UIApplicationInfo statusBarHiddenWhenVerticallyCompact];
-[_UIApplicationInfo effectiveUIRequiresFullScreenValue];
-[_UIApplicationInfo optOutOfRTL];
-[_UIApplicationInfo supportsVerticalBars];
-[_UIApplicationInfo whitePointAdaptivityStyle];
-[_UIApplicationInfo systemWindowsSecure];
-[_UIApplicationInfo supportedUserInterfaceStyle];
-[_UIApplicationInfo _launchingInterfaceOrientation];
-[_UIApplicationInfo _lock_loadFolderNamesIfNecessary];
-[_UIApplicationInfo fallbackFolderName];
-[_UIApplicationInfo folderNames];
-[_UIApplicationInfo hidesAutomaticIntelligentAssistantInteractions];
-[_UIApplicationInfo statusBarForcedHiddenForInterfaceOrientation:onDisplay:];
-[_UIApplicationInfo statusBarForcedHiddenForInterfaceOrientation:onDisplay:withUserInterfaceIdiom:];
-[_UIApplicationInfo statusBarHiddenForInterfaceOrientation:onDisplay:];
-[_UIApplicationInfo statusBarHiddenForInterfaceOrientation:onDisplay:withUserInterfaceIdiom:];
-[_UIApplicationInfo supportsVerticalBarLayoutMargins];
-[_UIApplicationInfo supportsiPhoneResizing];
```
