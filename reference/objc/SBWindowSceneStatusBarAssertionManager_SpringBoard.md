# `SBWindowSceneStatusBarAssertionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `UIStatusBarManager`
- 12 instance variables, 4 properties, 50 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _disableAlphaChangeAssertions;
@"NSHashTable" _disableUserInteractionChangeAssertions;
@"NSHashTable" _modeAssertions;
@"NSHashTable" _hideStatusBarAssertions;
[16@"NSPointerArray"] _statusBarSettingsAssertionsByLevel;
@"SBStatusBarSettings" _currentStatusBarSettings;
@"<BSInvalidatable>" _stateCaptureAssertion;
@"NSHashTable" _observers;
B _changingStatusBarStyle;
B _changingStatusBarAlpha;
Q _statusBarAlphaAnimationCount;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWindowSceneStatusBarAssertionManager currentEffectiveStatusBarStyleRequest];
-[SBWindowSceneStatusBarAssertionManager currentStatusBarMode];
-[SBWindowSceneStatusBarAssertionManager statusBar:effectiveBackgroundActivitiesForBackgroundActiviesWithIdentifiers:];
-[SBWindowSceneStatusBarAssertionManager _removeStatusBarSettingsAssertion:withAnimationParameters:];
-[SBWindowSceneStatusBarAssertionManager effectiveStatusBarStyleRequestWithSettings:];
-[SBWindowSceneStatusBarAssertionManager _addStatusBarModeAssertion:];
-[SBWindowSceneStatusBarAssertionManager succinctDescriptionBuilder];
-[SBWindowSceneStatusBarAssertionManager removeObserver:];
-[SBWindowSceneStatusBarAssertionManager effectiveStatusBarStyleForRequestedStyle:styleOverridesToSuppress:];
-[SBWindowSceneStatusBarAssertionManager statusBarSettingsForLevel:];
-[SBWindowSceneStatusBarAssertionManager _styleRequestForSettings:];
-[SBWindowSceneStatusBarAssertionManager acquireHideFrontmostStatusBarAssertionForReason:];
-[SBWindowSceneStatusBarAssertionManager dealloc];
-[SBWindowSceneStatusBarAssertionManager _modifiedStatusBarSettingsAssertion:withAnimationParameters:];
-[SBWindowSceneStatusBarAssertionManager _removeDisableWindowSceneStatusBarAlphaChangesAssertion:];
-[SBWindowSceneStatusBarAssertionManager _cleanUpAllStatusBarSettingsAssertions];
-[SBWindowSceneStatusBarAssertionManager _descriptionForPropertyWithAssertions:];
-[SBWindowSceneStatusBarAssertionManager _removeStatusBarSettingsAssertion:];
-[SBWindowSceneStatusBarAssertionManager acquireDisableUserInteractionChangesAssertionWithReason:];
-[SBWindowSceneStatusBarAssertionManager _modifiedStatusBarSettingsAssertion:];
-[SBWindowSceneStatusBarAssertionManager descriptionWithMultilinePrefix:];
-[SBWindowSceneStatusBarAssertionManager acquireDisableAlphaChangesAssertionWithReason:];
-[SBWindowSceneStatusBarAssertionManager isFrontmostStatusBarPartHidden:];
-[SBWindowSceneStatusBarAssertionManager _addDisableWindowSceneStatusBarAlphaChangesAssertion:];
-[SBWindowSceneStatusBarAssertionManager acquireModeAssertionWithMode:reason:];
-[SBWindowSceneStatusBarAssertionManager initWithWindowScene:];
-[SBWindowSceneStatusBarAssertionManager succinctDescription];
-[SBWindowSceneStatusBarAssertionManager addObserver:];
-[SBWindowSceneStatusBarAssertionManager statusBar:shouldSetAlpha:];
-[SBWindowSceneStatusBarAssertionManager effectiveStatusBarStyleRequestForLevel:];
-[SBWindowSceneStatusBarAssertionManager _setStatusBarValueForPropertyWithAssertions:setter:];
-[SBWindowSceneStatusBarAssertionManager newSettingsAssertionWithSettings:atLevel:reason:];
-[SBWindowSceneStatusBarAssertionManager _updateStatusBarModeIfNecessary];
-[SBWindowSceneStatusBarAssertionManager _removeDisableWindowSceneStatusBarUserInteractionChangesAssertion:];
-[SBWindowSceneStatusBarAssertionManager _resolveEffectiveStatusBarStyleForSettings:];
-[SBWindowSceneStatusBarAssertionManager isFrontmostStatusBarHidden];
-[SBWindowSceneStatusBarAssertionManager _evaluateSettingsWithStyleAnimations:];
-[SBWindowSceneStatusBarAssertionManager _removeStatusBarModeAssertion:];
-[SBWindowSceneStatusBarAssertionManager description];
-[SBWindowSceneStatusBarAssertionManager _addDisableWindowSceneStatusBarUserInteractionChangesAssertion:];
-[SBWindowSceneStatusBarAssertionManager _enumerateAssertionsToLevel:withBlock:];
-[SBWindowSceneStatusBarAssertionManager _statusBarUpdatedFromSettings:toSettings:withAnimations:];
-[SBWindowSceneStatusBarAssertionManager _addStatusBarSettingsAssertion:];
-[SBWindowSceneStatusBarAssertionManager statusBar:shouldRequestStyle:animationParameters:forced:];
-[SBWindowSceneStatusBarAssertionManager newSettingsAssertionWithStatusBarHidden:atLevel:reason:];
-[SBWindowSceneStatusBarAssertionManager statusBar:shouldRequestStyleAttributes:animationParameters:forced:];
-[SBWindowSceneStatusBarAssertionManager _addStatusBarSettingsAssertion:withAnimationParameters:];
-[SBWindowSceneStatusBarAssertionManager currentStatusBarSettings];
-[SBWindowSceneStatusBarAssertionManager statusBar:effectiveStyleOverridesForRequestedStyle:overrides:];
-[SBWindowSceneStatusBarAssertionManager descriptionBuilderWithMultilinePrefix:];
```
