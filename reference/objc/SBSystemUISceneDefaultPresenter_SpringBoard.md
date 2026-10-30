# `SBSystemUISceneDefaultPresenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSUIStatusBarSceneHostComponentDelegate`, `SBSUIFeaturePolicyHostComponentDelegate`, `SBSUIIdleTimerSceneHostComponentDelegate`, `FBSSceneObserver`, `SBScenePresenting`, `BSDescriptionProviding`
- 12 instance variables, 7 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _presentedScenes;
@"SBTraitsSceneParticipantDelegate" _currentParticipantDelegate;
@"<SBScenePresentingDelegate>" _presentingDelegate;
@"NSMutableDictionary" _sceneToWindowMap;
@"NSMutableDictionary" _hostingSceneToPresentedSceneMap;
@"NSMutableDictionary" _sceneToDisplayLayoutAssertionMap;
@"UIStatusBar" _statusBar;
@"<BSInvalidatable>" _idleTimerDisableAssertion;
@"NSMutableSet" _scenesDisablingIdleTimer;
B _shouldPublishAsDisplayLayoutElement;
q _presentationStyle;
@"NSNumber" _preferredWindowLevel;
```

## Properties

```
@property (Tq,R,N,V_presentationStyle) presentationStyle;
@property (T@"NSNumber",C,N,V_preferredWindowLevel) preferredWindowLevel;
@property (TB,N,V_shouldPublishAsDisplayLayoutElement) shouldPublishAsDisplayLayoutElement;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSystemUISceneDefaultPresenter setPresentingDelegate:];
-[SBSystemUISceneDefaultPresenter featurePolicyHostComponentDidChangeShouldDisableReachability:];
-[SBSystemUISceneDefaultPresenter dismissScene:];
-[SBSystemUISceneDefaultPresenter featurePolicyHostComponentDidChangeAudioCategoriesDisablingVolumeHUD:];
-[SBSystemUISceneDefaultPresenter sceneDidChangeDisplayIdentity:handler:];
-[SBSystemUISceneDefaultPresenter succinctDescriptionBuilder];
-[SBSystemUISceneDefaultPresenter conformsToStatusBarSceneHostComponentDelegate];
-[SBSystemUISceneDefaultPresenter scene:didUpdateSettings:];
-[SBSystemUISceneDefaultPresenter featurePolicyHostComponentDidChangeShouldDisableSiri:];
-[SBSystemUISceneDefaultPresenter featurePolicyHostComponentDidChangeDesiredBackgroundActivities:];
-[SBSystemUISceneDefaultPresenter statusBarForDisplayConfiguration:statusBarSceneHostComponent:];
-[SBSystemUISceneDefaultPresenter featurePolicyHostComponentDidChangeShouldDisableAlertItems:];
-[SBSystemUISceneDefaultPresenter dealloc];
-[SBSystemUISceneDefaultPresenter presentationStyle];
-[SBSystemUISceneDefaultPresenter _presentScene:onWindowScene:viewControllerBuilderBlock:];
-[SBSystemUISceneDefaultPresenter _serviceBundleIdentifierForScene:];
-[SBSystemUISceneDefaultPresenter featurePolicyHostComponentDidChangeAllowsMenuButtonDismissal:];
-[SBSystemUISceneDefaultPresenter descriptionWithMultilinePrefix:];
-[SBSystemUISceneDefaultPresenter presentScene:viewControllerBuilderBlock:];
-[SBSystemUISceneDefaultPresenter idleTimerSceneHostComponentDidChangeShouldDisableIdleTimer:];
-[SBSystemUISceneDefaultPresenter scene:didChangeTraitsParticipantDelegate:];
-[SBSystemUISceneDefaultPresenter featurePolicyHostComponentDidChangeDesiredHardwareButtonEvents:];
-[SBSystemUISceneDefaultPresenter _setDisplayLayoutElementActive:scene:];
-[SBSystemUISceneDefaultPresenter succinctDescription];
-[SBSystemUISceneDefaultPresenter featurePolicyHostComponentDidChangeShouldDisableInteractiveScreenshotGesture:];
-[SBSystemUISceneDefaultPresenter featurePolicyHostComponentDidChangeShouldDisableControlCenter:];
-[SBSystemUISceneDefaultPresenter _dismissScene:];
-[SBSystemUISceneDefaultPresenter shouldPublishAsDisplayLayoutElement];
-[SBSystemUISceneDefaultPresenter dismissAllScenes];
-[SBSystemUISceneDefaultPresenter setPreferredWindowLevel:];
-[SBSystemUISceneDefaultPresenter scene:hasVisibleContent:];
-[SBSystemUISceneDefaultPresenter featurePolicyHostComponentDidChangeShouldDisableBanners:];
-[SBSystemUISceneDefaultPresenter conformsToIdleTimerSceneHostComponentDelegate];
-[SBSystemUISceneDefaultPresenter _disableIdleTimer:sceneIdentityToken:];
-[SBSystemUISceneDefaultPresenter description];
-[SBSystemUISceneDefaultPresenter conformsToFeaturePolicyHostComponentDelegate];
-[SBSystemUISceneDefaultPresenter initWithPresentationStyle:];
-[SBSystemUISceneDefaultPresenter statusBarSceneHostComponent:didChangePreferredStatusBarVisibilityWithAnimationSettings:];
-[SBSystemUISceneDefaultPresenter _updateDisplayLayoutElementWindowLevelForScene:];
-[SBSystemUISceneDefaultPresenter setShouldPublishAsDisplayLayoutElement:];
-[SBSystemUISceneDefaultPresenter preferredWindowLevel];
-[SBSystemUISceneDefaultPresenter hostingWindowForScene:];
-[SBSystemUISceneDefaultPresenter descriptionBuilderWithMultilinePrefix:];
-[SBSystemUISceneDefaultPresenter sceneWillChangeDisplayIdentity:handler:];
```
