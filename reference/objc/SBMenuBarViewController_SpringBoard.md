# `SBMenuBarViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBMenuBarMainMenuViewDelegate`, `_UISceneMainMenuHost`, `SBMenuBarHelpMenuProviderDelegate`, `SBHOpenApplicationWindowsContextMenuProviderDelegate`, `UIGestureRecognizerDelegate`
- 33 instance variables, 32 properties, 118 instance methods, 0 class methods

## Instance variables

```
B _animateInitialPresentation;
@? _alongsidePresentationAnimations;
@"NSMutableArray" _presentationCompletionBlocks;
B _dismissed;
@"_UIMainMenuSession" _pendingAuthenticatedCommandSession;
@"SBMenuBarSettings" _menuBarSettings;
@"SBApplicationController" _applicationController;
B _menuBarContentIsLight;
B _variableBlurNeeded;
B _menuSessionIsActiveForPointer;
@"FBScene" _menuProvidingScene;
@"<SBMenuBarViewControllerDelegate>" _delegate;
@"SBMenuBarHelpMenuProvider" _menuBarHelpMenuProvider;
@"<_UISceneMainMenuProviding>" _mainMenuProvider;
@"<_UISceneFocusSystemController>" _focusSystemController;
@"_UIMainMenuSession" _session;
@"_UIMainMenu" _baseMainMenu;
@"NSString" _clientName;
@"_UIMainMenuState" _uncategorizedMenuState;
@"NSArray" _appKeyboardShortcutActionsForSession;
@"UIAction" _leftArrowNavigationAction;
@"UIAction" _rightArrowNavigationAction;
@"SBStatusBarMenuBarView" _menuBarView;
@"SBMenuBarHeaderContainerView" _menuHeaderContainerView;
@"UIView" _contextMenuContainerView;
@"SBMenuBarMainMenuView" _presentedMainMenuView;
@"SBMenuBarMainMenuView" _previouslyPresentedMenu;
@"UIView" _backgroundEffectContainerView;
@"SBMenuBarBackgroundGradientView" _gradientView;
@"SBMenuBarBackgroundVariableBlurView" _variableBlurView;
@"NSTimer" _endActiveSessionTimer;
@"SBHRecentDocumentsContextMenuProvider" _recentDocumentsMenuProvider;
@"STUIStatusBarStyleAttributes" _currentStyleAttributes;
```

## Properties

```
@property (T@"<_UISceneMainMenuProviding>",R,N,V_mainMenuProvider) mainMenuProvider;
@property (T@"<_UISceneFocusSystemController>",R,W,N,V_focusSystemController) focusSystemController;
@property (T@"_UIMainMenuSession",R,N,V_session) session;
@property (T@"_UIMainMenu",&,N,V_baseMainMenu) baseMainMenu;
@property (T@"NSString",&,N,V_clientName) clientName;
@property (T@"_UIMainMenuState",&,N,V_uncategorizedMenuState) uncategorizedMenuState;
@property (T@"NSArray",&,N,V_appKeyboardShortcutActionsForSession) appKeyboardShortcutActionsForSession;
@property (T@"UIAction",&,N,V_leftArrowNavigationAction) leftArrowNavigationAction;
@property (T@"UIAction",&,N,V_rightArrowNavigationAction) rightArrowNavigationAction;
@property (TB,N,V_menuSessionIsActiveForPointer) menuSessionIsActiveForPointer;
@property (T@"SBStatusBarMenuBarView",&,N,V_menuBarView) menuBarView;
@property (T@"SBMenuBarHeaderContainerView",&,N,V_menuHeaderContainerView) menuHeaderContainerView;
@property (T@"UIView",&,N,V_contextMenuContainerView) contextMenuContainerView;
@property (T@"SBMenuBarMainMenuView",&,N,V_presentedMainMenuView) presentedMainMenuView;
@property (T@"SBMenuBarMainMenuView",W,N,V_previouslyPresentedMenu) previouslyPresentedMenu;
@property (T@"SBMenuBarHelpMenuProvider",&,N,V_menuBarHelpMenuProvider) menuBarHelpMenuProvider;
@property (T@"UIView",&,N,V_backgroundEffectContainerView) backgroundEffectContainerView;
@property (T@"SBMenuBarBackgroundGradientView",&,N,V_gradientView) gradientView;
@property (T@"SBMenuBarBackgroundVariableBlurView",&,N,V_variableBlurView) variableBlurView;
@property (T@"NSTimer",&,N,V_endActiveSessionTimer) endActiveSessionTimer;
@property (T@"SBHRecentDocumentsContextMenuProvider",&,N,V_recentDocumentsMenuProvider) recentDocumentsMenuProvider;
@property (T@"STUIStatusBarStyleAttributes",&,N,V_currentStyleAttributes) currentStyleAttributes;
@property (T@"FBScene",R,N,V_menuProvidingScene) menuProvidingScene;
@property (T@"<SBMenuBarViewControllerDelegate>",R,W,N,V_delegate) delegate;
@property (TB,N,V_menuBarContentIsLight) menuBarContentIsLight;
@property (TB,N,V_variableBlurNeeded) variableBlurNeeded;
@property (TB,R,N,GisShowingMenu) showingMenu;
@property (T@"NSArray",R,N) additionalKeyboardShortcutActionsForSession;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBMenuBarViewController gradientView];
-[SBMenuBarViewController setGradientView:];
-[SBMenuBarViewController setClientName:];
-[SBMenuBarViewController viewIsAppearing:];
-[SBMenuBarViewController dealloc];
-[SBMenuBarViewController viewDidAppear:];
-[SBMenuBarViewController loadView];
-[SBMenuBarViewController clientName];
-[SBMenuBarViewController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBMenuBarViewController delegate];
-[SBMenuBarViewController openApplicationWindowsContextMenuProvider:canProvideContextMenuSectionsForBundleIdentifier:];
-[SBMenuBarViewController viewDidDisappear:];
-[SBMenuBarViewController dataSourceForOpenApplicationWindowsContextMenuProvider:];
-[SBMenuBarViewController session];
-[SBMenuBarViewController focusSystemController];
-[SBMenuBarViewController hostKeyboardShortcutsForMainMenu:];
-[SBMenuBarViewController mainMenuDidInvalidate:];
-[SBMenuBarViewController mainMenuProvider];
-[SBMenuBarViewController mainMenuProvider:didReceiveCommandInvocationNotification:];
-[SBMenuBarViewController overrideClientNameForMainMenu:];
-[SBMenuBarViewController uncategorizedMenuState];
-[SBMenuBarViewController dismissPresentedMenu];
-[SBMenuBarViewController isShowingMenu];
-[SBMenuBarViewController currentStyleAttributes];
-[SBMenuBarViewController setCurrentStyleAttributes:];
-[SBMenuBarViewController setMenuBarView:];
-[SBMenuBarViewController menuBarView];
-[SBMenuBarViewController setVariableBlurView:];
-[SBMenuBarViewController variableBlurView];
-[SBMenuBarViewController addPresentationCompletionBlock:];
-[SBMenuBarViewController addWindowControlsAlongsideAnimations:completion:];
-[SBMenuBarViewController _createHelpMenuProviderIfNeeded];
-[SBMenuBarViewController setRecentDocumentsMenuProvider:];
-[SBMenuBarViewController _addOverflowMenuToContainerIfNeededForcingViewLayout:];
-[SBMenuBarViewController _adjustPresentedMenuForGestureOverViewInContainer:forPanGesture:isDirectTouch:];
-[SBMenuBarViewController _applyStyleAttributes:];
-[SBMenuBarViewController _baseContentOriginOffset];
-[SBMenuBarViewController _cancelEndSessionTimer];
-[SBMenuBarViewController _clearSessionState];
-[SBMenuBarViewController _collapsedContentOriginOffset];
-[SBMenuBarViewController _createMainMenuViewForUIMainMenu:type:];
-[SBMenuBarViewController _createVariableBlurView];
-[SBMenuBarViewController _expandedContentOriginOffset];
-[SBMenuBarViewController _loadAllMainMenusWithCompletion:];
-[SBMenuBarViewController _mainMenuViewPassingTest:];
-[SBMenuBarViewController _movePresentedMenuViewToPreviouslyPresented];
-[SBMenuBarViewController _navigateToNextMenuHeaderForArrowKeyPress:];
-[SBMenuBarViewController _performMainMenuCommandInvocationRequestForCommand:withSystemAuthenticationServiceMessage:session:];
-[SBMenuBarViewController _possiblyFlashMenuViewPassingTest:];
-[SBMenuBarViewController _presentMenuViewNonInteractively:forPointerHover:forKeyPress:];
-[SBMenuBarViewController _restoreKeyboardFocusToMenuProvidingScene];
-[SBMenuBarViewController _runCommandFromContext:];
-[SBMenuBarViewController _scheduleEndSessionTimer];
-[SBMenuBarViewController _setMenuViewEnabled:withProvidingAppRestricted:];
-[SBMenuBarViewController _systemHelpMenus];
-[SBMenuBarViewController _uiDeferredMenuElementForMainMenuDeferredElement:parentState:];
-[SBMenuBarViewController _uiMenuElementForChildMainMenuElement:parentMenuState:];
-[SBMenuBarViewController _uiMenuElementsForMainMenuElements:parentMenuState:];
-[SBMenuBarViewController _uiMenuForMainMenu:menuState:];
-[SBMenuBarViewController _uiMenuLeafForMainMenuCommand:parentMenuState:];
-[SBMenuBarViewController _updateWindowControlsPosition];
-[SBMenuBarViewController _windowControlsAvoidanceOffset];
-[SBMenuBarViewController addAlongsidePresentationAnimations:];
-[SBMenuBarViewController additionalKeyboardShortcutActionsForSession];
-[SBMenuBarViewController adjustPresentedMenuForInteractionOverView:];
-[SBMenuBarViewController appKeyboardShortcutActionsForSession];
-[SBMenuBarViewController backgroundEffectContainerView];
-[SBMenuBarViewController baseMainMenu];
-[SBMenuBarViewController beginSceneFocusSystemActivationAssertionForMainMenuView:];
-[SBMenuBarViewController contextMenuContainerView];
-[SBMenuBarViewController didPresentContextMenuForMainMenuView:forDirectTouchPan:];
-[SBMenuBarViewController dismissAnimated:fadeAppMenu:alongsideAnimations:completion:];
-[SBMenuBarViewController endActiveSessionTimer];
-[SBMenuBarViewController flashMainMenuIfPossible:];
-[SBMenuBarViewController handleDirectTouchPanOrLongPressReleased:];
-[SBMenuBarViewController handleMenuPanOrLongPressGesture:isDirectTouch:];
-[SBMenuBarViewController initWithScene:delegate:applicationController:animateInitialPresentation:loadCompletion:];
-[SBMenuBarViewController leftArrowNavigationAction];
-[SBMenuBarViewController loadMenuElementsForMainMenus:handler:];
-[SBMenuBarViewController menuBarContentIsLight];
-[SBMenuBarViewController menuBarHelpMenuProvider];
-[SBMenuBarViewController menuBarHelpMenuProvider:handleOpenApplicationTipWithURL:];
-[SBMenuBarViewController menuBarHelpMenuProviderDemoMenuProvider:];
-[SBMenuBarViewController menuBarHelpMenuProviderTargetScene:];
-[SBMenuBarViewController menuHeaderContainerView];
-[SBMenuBarViewController menuPresentationViewForMainMenuView:];
-[SBMenuBarViewController menuProvidingScene];
-[SBMenuBarViewController menuSessionIsActiveForPointer];
-[SBMenuBarViewController noteSearchUsedInMenuBarHelpMenuProvider:];
-[SBMenuBarViewController openApplicationMenu];
-[SBMenuBarViewController openHelpMenu];
-[SBMenuBarViewController presentedMainMenuView];
-[SBMenuBarViewController previouslyPresentedMenu];
-[SBMenuBarViewController recentDocumentsMenuProvider];
-[SBMenuBarViewController removeWindowControlsAlongsideAnimations:completion:];
-[SBMenuBarViewController rightArrowNavigationAction];
-[SBMenuBarViewController setAppKeyboardShortcutActionsForSession:];
-[SBMenuBarViewController setBackgroundEffectContainerView:];
-[SBMenuBarViewController setBaseMainMenu:];
-[SBMenuBarViewController setContextMenuContainerView:];
-[SBMenuBarViewController setEndActiveSessionTimer:];
-[SBMenuBarViewController setLeftArrowNavigationAction:];
-[SBMenuBarViewController setMenuBarContentIsLight:];
-[SBMenuBarViewController setMenuBarHelpMenuProvider:];
-[SBMenuBarViewController setMenuHeaderContainerView:];
-[SBMenuBarViewController setMenuSessionIsActiveForPointer:];
-[SBMenuBarViewController setPresentedMainMenuView:];
-[SBMenuBarViewController setPreviouslyPresentedMenu:];
-[SBMenuBarViewController setRightArrowNavigationAction:];
-[SBMenuBarViewController setUncategorizedMenuState:];
-[SBMenuBarViewController setVariableBlurNeeded:];
-[SBMenuBarViewController testInvalidation];
-[SBMenuBarViewController updateMenuEnablementForAppRestrictionChange];
-[SBMenuBarViewController variableBlurNeeded];
-[SBMenuBarViewController willDismissContextMenuForMainMenuView:forPointerClick:];
-[SBMenuBarViewController willLoadMenuElementsForMainMenuView:];
-[SBMenuBarViewController willPresentContextMenuForMainMenuView:forPointerClick:];
-[SBMenuBarViewController yOffsetForPresentedMenuForMainMenuView:];
```
