# `_UIApplicationInfoParser`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 51 instance variables, 45 properties, 50 instance methods, 1 class methods

## Instance variables

```
@"NSString" _applicationSDKVersion;
B _describesCurrentProcess;
B _isExitsOnSuspend;
B _canChangeBackgroundStyle;
B _statusBarHidden;
B _statusBarHiddenWhenVerticallyCompact;
B _systemWindowsSecure;
B _optOutOfRTL;
B _disableLayoutAwareShortcuts;
B _requiresHighResolution;
B _supportsMultiwindow;
B _supportsSceneItemProviders;
B _supportedOnLockScreen;
B _hasSupportsIndirectInputEventsKey;
B _supportsIndirectInputEvents;
B _supportsiPhoneResizing;
B _supportsVerticalBars;
B _hidesAutomaticIntelligentAssistantInteractions;
B _uiRequiresFullScreenValue;
B _effectiveUIRequiresFullScreenValue;
B _usesSplashBoard;
B _requiresFullScreen;
B _requiresGameControllerBasedFocus;
B _requestsFlattenedGameControllerFocusMovement;
B _focusEnabledInLimitedControls;
B _forcesDefaultFocusAppearance;
B _focusSystemEnabled;
B _focusTabKeyLoadsScrollableContainersEnabled;
B _supportsPrintCommand;
B _supportsAlwaysOnDisplay;
B _supportsBacklightEnvironment;
q _requestedStatusBarStyle;
q _interfaceOrientation;
q _launchingInterfaceOrientationForSpringBoard;
Q _supportedInterfaceOrientations;
q _backgroundStyle;
Q _ignoredOverrides;
q _whitePointAdaptivityStyle;
Q _viewControllerBasedStatusBarAppearance;
@"NSString" _launchImageFile;
@"NSString" _keyColorAssetName;
@"NSArray" _canvasDefinitions;
@"NSString" _preferredDefaultSceneSessionRole;
@"NSDictionary" _sceneConfigurations;
q _supportedUserInterfaceStyle;
@"NSArray" _deviceFamilies;
Q _supportsVerticalBarLayoutMargins;
@"NSString" _uiRequiresFullScreenIgnoredStartingWithVersion;
@"NSDictionary" _utTypeToDocumentClassMap;
@"NSArray" _viewerRoleDocumentUTTypes;
@"NSArray" _editorRoleDocumentUTTypes;
```

## Properties

```
@property (Tq,R,N,V_requestedStatusBarStyle) requestedStatusBarStyle;
@property (Tq,R,N,V_interfaceOrientation) interfaceOrientation;
@property (Tq,R,N,V_launchingInterfaceOrientationForSpringBoard) launchingInterfaceOrientationForSpringBoard;
@property (TQ,R,N,V_supportedInterfaceOrientations) supportedInterfaceOrientations;
@property (Tq,R,N,V_backgroundStyle) backgroundStyle;
@property (TQ,R,N,V_ignoredOverrides) ignoredOverrides;
@property (Tq,R,N,V_whitePointAdaptivityStyle) whitePointAdaptivityStyle;
@property (TQ,R,N,V_viewControllerBasedStatusBarAppearance) viewControllerBasedStatusBarAppearance;
@property (T@"NSString",R,C,N,V_launchImageFile) launchImageFile;
@property (T@"NSString",R,C,N,V_keyColorAssetName) keyColorAssetName;
@property (TB,R,N,V_isExitsOnSuspend) isExitsOnSuspend;
@property (TB,R,N,V_canChangeBackgroundStyle) canChangeBackgroundStyle;
@property (TB,R,N,V_statusBarHidden) statusBarHidden;
@property (TB,R,N,V_statusBarHiddenWhenVerticallyCompact) statusBarHiddenWhenVerticallyCompact;
@property (TB,R,N,V_systemWindowsSecure) systemWindowsSecure;
@property (TB,R,N,V_optOutOfRTL) optOutOfRTL;
@property (TB,R,N,V_disableLayoutAwareShortcuts) disableLayoutAwareShortcuts;
@property (TB,R,N,V_requiresHighResolution) requiresHighResolution;
@property (TB,R,N,V_supportsMultiwindow) supportsMultiwindow;
@property (TB,R,N,V_supportsSceneItemProviders) supportsSceneItemProviders;
@property (T@"NSArray",R,C,N,V_canvasDefinitions) canvasDefinitions;
@property (T@"NSString",R,C,N,V_preferredDefaultSceneSessionRole) preferredDefaultSceneSessionRole;
@property (T@"NSDictionary",R,C,N,V_sceneConfigurations) sceneConfigurations;
@property (TB,R,N,V_supportedOnLockScreen) supportedOnLockScreen;
@property (Tq,R,N,V_supportedUserInterfaceStyle) supportedUserInterfaceStyle;
@property (TB,R,N,V_hasSupportsIndirectInputEventsKey) hasSupportsIndirectInputEventsKey;
@property (TB,R,N,V_supportsIndirectInputEvents) supportsIndirectInputEvents;
@property (T@"NSArray",R,C,N,V_deviceFamilies) deviceFamilies;
@property (TB,R,N,V_uiRequiresFullScreenValue) uiRequiresFullScreenValue;
@property (T@"NSString",R,C,N,V_uiRequiresFullScreenIgnoredStartingWithVersion) uiRequiresFullScreenIgnoredStartingWithVersion;
@property (TB,R,N,V_effectiveUIRequiresFullScreenValue) effectiveUIRequiresFullScreenValue;
@property (TB,R,N,V_usesSplashBoard) usesSplashBoard;
@property (TB,R,N,V_requiresFullScreen) requiresFullScreen;
@property (TB,R,N,V_requiresGameControllerBasedFocus) requiresGameControllerBasedFocus;
@property (TB,R,N,V_requestsFlattenedGameControllerFocusMovement) requestsFlattenedGameControllerFocusMovement;
@property (TB,R,N,V_focusEnabledInLimitedControls) focusEnabledInLimitedControls;
@property (TB,R,N,V_forcesDefaultFocusAppearance) forcesDefaultFocusAppearance;
@property (TB,R,N,V_focusSystemEnabled) focusSystemEnabled;
@property (TB,R,N,V_focusTabKeyLoadsScrollableContainersEnabled) focusTabKeyLoadsScrollableContainersEnabled;
@property (TB,R,N,V_supportsPrintCommand) supportsPrintCommand;
@property (TB,R,N,V_supportsAlwaysOnDisplay) supportsAlwaysOnDisplay;
@property (TB,R,N,V_supportsBacklightEnvironment) supportsBacklightEnvironment;
@property (T@"NSDictionary",R,N,V_utTypeToDocumentClassMap) utTypeToDocumentClassMap;
@property (T@"NSArray",R,N,V_viewerRoleDocumentUTTypes) viewerRoleDocumentUTTypes;
@property (T@"NSArray",R,N,V_editorRoleDocumentUTTypes) editorRoleDocumentUTTypes;
```

## Class methods

```
+[_UIApplicationInfoParser mainBundleInfoParser];
```

## Instance methods

```
-[_UIApplicationInfoParser preferredDefaultSceneSessionRole];
-[_UIApplicationInfoParser supportsAlwaysOnDisplay];
-[_UIApplicationInfoParser interfaceOrientation];
-[_UIApplicationInfoParser launchImageFile];
-[_UIApplicationInfoParser ignoredOverrides];
-[_UIApplicationInfoParser viewControllerBasedStatusBarAppearance];
-[_UIApplicationInfoParser _applicationLinkedOnOrAfter:];
-[_UIApplicationInfoParser statusBarHidden];
-[_UIApplicationInfoParser supportsPrintCommand];
-[_UIApplicationInfoParser uiRequiresFullScreenIgnoredStartingWithVersion];
-[_UIApplicationInfoParser requiresGameControllerBasedFocus];
-[_UIApplicationInfoParser supportedInterfaceOrientations];
-[_UIApplicationInfoParser keyColorAssetName];
-[_UIApplicationInfoParser supportsSceneItemProviders];
-[_UIApplicationInfoParser uiRequiresFullScreenValue];
-[_UIApplicationInfoParser editorRoleDocumentUTTypes];
-[_UIApplicationInfoParser supportsIndirectInputEvents];
-[_UIApplicationInfoParser canChangeBackgroundStyle];
-[_UIApplicationInfoParser focusEnabledInLimitedControls];
-[_UIApplicationInfoParser _computeSupportedUserInterfaceStyleFromInfo:];
-[_UIApplicationInfoParser requestedStatusBarStyle];
-[_UIApplicationInfoParser requiresHighResolution];
-[_UIApplicationInfoParser backgroundStyle];
-[_UIApplicationInfoParser usesSplashBoard];
-[_UIApplicationInfoParser _initWithApplicationPlistDictionary:applicationSDKVersion:describesCurrentProcess:];
-[_UIApplicationInfoParser statusBarHiddenWhenVerticallyCompact];
-[_UIApplicationInfoParser launchingInterfaceOrientationForSpringBoard];
-[_UIApplicationInfoParser disableLayoutAwareShortcuts];
-[_UIApplicationInfoParser focusTabKeyLoadsScrollableContainersEnabled];
-[_UIApplicationInfoParser requestsFlattenedGameControllerFocusMovement];
-[_UIApplicationInfoParser effectiveUIRequiresFullScreenValue];
-[_UIApplicationInfoParser viewerRoleDocumentUTTypes];
-[_UIApplicationInfoParser optOutOfRTL];
-[_UIApplicationInfoParser requiresFullScreen];
-[_UIApplicationInfoParser supportedOnLockScreen];
-[_UIApplicationInfoParser isExitsOnSuspend];
-[_UIApplicationInfoParser canvasDefinitions];
-[_UIApplicationInfoParser deviceFamilies];
-[_UIApplicationInfoParser sceneConfigurations];
-[_UIApplicationInfoParser forcesDefaultFocusAppearance];
-[_UIApplicationInfoParser hasSupportsIndirectInputEventsKey];
-[_UIApplicationInfoParser initWithApplicationProxy:];
-[_UIApplicationInfoParser supportsBacklightEnvironment];
-[_UIApplicationInfoParser supportsMultiwindow];
-[_UIApplicationInfoParser _computeSupportedInterfaceOrientationsWithInfo:];
-[_UIApplicationInfoParser whitePointAdaptivityStyle];
-[_UIApplicationInfoParser focusSystemEnabled];
-[_UIApplicationInfoParser systemWindowsSecure];
-[_UIApplicationInfoParser supportedUserInterfaceStyle];
-[_UIApplicationInfoParser utTypeToDocumentClassMap];
```
